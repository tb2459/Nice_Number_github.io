from flask import Flask, render_template
from datetime import timedelta

import requests
app = Flask(__name__, template_folder='templates')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
@app.route('/')
def home():
    rfi = requests.get("https://grist-ej.bballou.com/api/docs/cQbcmAcNgJ1u5YApQyF8WH/sql?q=SELECT COUNT(Number) FROM RFI_Log WHERE Status = 'Open'", headers={
     'Authorization': 'Bearer 7649966e88b32725ebd633ec124ab052414bb618'

    
})
    
    noc = requests.get("https://grist-ej.bballou.com/api/docs/cQbcmAcNgJ1u5YApQyF8WH/sql?q=SELECT COUNT(Description) FROM Change_Log WHERE Status = 'OPEN' AND Schedule_Impact=TRUE", headers={
     'Authorization': 'Bearer 7649966e88b32725ebd633ec124ab052414bb618'
     })

    
    incoming_correspondence = requests.get("https://grist-ej.bballou.com/api/docs/cQbcmAcNgJ1u5YApQyF8WH/sql?q=SELECT COUNT(Number) FROM Correspondence WHERE Status = 'Open' AND Recipient = 2", headers={
        'Authorization': 'Bearer 7649966e88b32725ebd633ec124ab052414bb618'
    })

    outgoing_correspondence = requests.get("https://grist-ej.bballou.com/api/docs/cQbcmAcNgJ1u5YApQyF8WH/sql?q=SELECT COUNT(Number) FROM Correspondence WHERE Status = 'Open' AND Sender = 2", headers={
        'Authorization': 'Bearer 7649966e88b32725ebd633ec124ab052414bb618'  
    })

    number = rfi.json()['records'][0]['fields']['COUNT(Number)']
    number2 = noc.json()['records'][0]['fields']['COUNT(Description)']
    number3 = incoming_correspondence.json()['records'][0]['fields']['COUNT(Number)']
    number4 = outgoing_correspondence.json()['records'][0]['fields']['COUNT(Number)']
    return render_template(
        'index.html',
        val=number, val2=number2, val3=number3, val4=number4 
      
    )

@app.route('/PM')
def PM():
    return render_template('PM.html')

@app.route('/JC')
def JC():
    open_changes = requests.get("https://grist-ej.bballou.com/api/docs/cQbcmAcNgJ1u5YApQyF8WH/sql?q=SELECT COUNT(Description) FROM Change_Log WHERE Status = 'OPEN' AND PM = 'JCA'", headers={
        'Authorization': 'Bearer 7649966e88b32725ebd633ec124ab052414bb618' })
    
    rfi_JCA = requests.get("https://grist-ej.bballou.com/api/docs/cQbcmAcNgJ1u5YApQyF8WH/sql?q=SELECT COUNT(Number) FROM RFI_Log WHERE Status = 'Open' AND Manager=6", headers={
     'Authorization': 'Bearer 7649966e88b32725ebd633ec124ab052414bb618'})
    
    
    JCA_open_changes = open_changes.json()['records'][0]['fields']['COUNT(Description)']
    JCA_open_rfis = rfi_JCA.json()['records'][0]['fields']['COUNT(Number)']

    return render_template('JC.html', change=JCA_open_changes, rfi=JCA_open_rfis)

@app.route('/MI')
def MI():
    open_changes_MI = requests.get("https://grist-ej.bballou.com/api/docs/cQbcmAcNgJ1u5YApQyF8WH/sql?q=SELECT COUNT(Description) FROM Change_Log WHERE Status = 'OPEN' AND PM = 'MI'", headers={
        'Authorization': 'Bearer 7649966e88b32725ebd633ec124ab052414bb618' })
    
    rfi_MI = requests.get("https://grist-ej.bballou.com/api/docs/cQbcmAcNgJ1u5YApQyF8WH/sql?q=SELECT COUNT(Number) FROM RFI_Log WHERE Status = 'Open' AND Manager=10", headers={
     'Authorization': 'Bearer 7649966e88b32725ebd633ec124ab052414bb618'})
    
    
    MI_open_changes = open_changes_MI.json()['records'][0]['fields']['COUNT(Description)']
    MI_open_rfis = rfi_MI.json()['records'][0]['fields']['COUNT(Number)']

    return render_template('MI.html', change=MI_open_changes, rfi=MI_open_rfis)

if __name__ == '__main__':
    app.run(debug=True)
