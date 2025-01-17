from flask import Flask, render_template
from datetime import timedelta

import requests
app = Flask(__name__, template_folder='templates')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
@app.route('/')
def home():
    rfi = requests.get("https://grist.ej1899.com/api/docs/7BSTDSBvrBZSQhuc3FsLhA/sql?q=SELECT COUNT(Number) FROM RFI_Log WHERE Status = 'Open'", headers={
     'Authorization': 'Bearer f33e0ae5f9d06e9fa3c9e09f87bb88ecc4cf3848'


})

    noc = requests.get("https://grist.ej1899.com/api/docs/7BSTDSBvrBZSQhuc3FsLhA/sql?q=SELECT COUNT(Description) FROM Change_Log WHERE Status = 'OPEN' AND Schedule_Impact=TRUE", headers={
     'Authorization': 'Bearer f33e0ae5f9d06e9fa3c9e09f87bb88ecc4cf3848'
     })


    incoming_correspondence = requests.get("https://grist.ej1899.com/api/docs/7BSTDSBvrBZSQhuc3FsLhA/sql?q=SELECT COUNT(Number) FROM Correspondence WHERE Status = 'Open' AND Recipient = 2", headers={
        'Authorization': 'Bearer f33e0ae5f9d06e9fa3c9e09f87bb88ecc4cf3848'
    })

    outgoing_correspondence = requests.get("https://grist.ej1899.com/api/docs/7BSTDSBvrBZSQhuc3FsLhA/sql?q=SELECT COUNT(Number) FROM Correspondence WHERE Status = 'Open' AND Sender = 2", headers={
        'Authorization': 'Bearer f33e0ae5f9d06e9fa3c9e09f87bb88ecc4cf3848'
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
    open_changes = requests.get("https://grist.ej1899.com/api/docs/7BSTDSBvrBZSQhuc3FsLhA/sql?q=SELECT COUNT(Description) FROM Change_Log WHERE Status = 'OPEN' AND PM = 'JCA'", headers={
        'Authorization': 'Bearer f33e0ae5f9d06e9fa3c9e09f87bb88ecc4cf3848' })

    rfi_JCA = requests.get("https://grist.ej1899.com/api/docs/7BSTDSBvrBZSQhuc3FsLhA/sql?q=SELECT COUNT(Number) FROM RFI_Log WHERE Status = 'Open' AND Manager=6", headers={
     'Authorization': 'Bearer f33e0ae5f9d06e9fa3c9e09f87bb88ecc4cf3848'})


    JCA_open_changes = open_changes.json()['records'][0]['fields']['COUNT(Description)']
    JCA_open_rfis = rfi_JCA.json()['records'][0]['fields']['COUNT(Number)']

    return render_template('JC.html', change=JCA_open_changes, rfi=JCA_open_rfis)

@app.route('/MI')
def MI():
    open_changes_MI = requests.get("https://grist.ej1899.com/api/docs/7BSTDSBvrBZSQhuc3FsLhA/sql?q=SELECT COUNT(Description) FROM Change_Log WHERE Status = 'OPEN' AND PM = 'MI'", headers={
        'Authorization': 'Bearer f33e0ae5f9d06e9fa3c9e09f87bb88ecc4cf3848' })

    rfi_MI = requests.get("https://grist.ej1899.com/api/docs/7BSTDSBvrBZSQhuc3FsLhA/sql?q=SELECT COUNT(Number) FROM RFI_Log WHERE Status = 'Open' AND Manager=10", headers={
     'Authorization': 'Bearer f33e0ae5f9d06e9fa3c9e09f87bb88ecc4cf3848'})

    submittals_MI = requests.get("https://grist.ej1899.com/api/docs/7BSTDSBvrBZSQhuc3FsLhA/sql?q=SELECT COUNT(Description) FROM Submittal_Revisions WHERE Status = 'Submitted' AND Responsible_PM=10", headers={
        'Authorization': 'Bearer f33e0ae5f9d06e9fa3c9e09f87bb88ecc4cf3848'})
    
    correspondence_MI = requests.get("https://grist.ej1899.com/api/docs/7BSTDSBvrBZSQhuc3FsLhA/sql?q=SELECT COUNT(Number) FROM Correspondence WHERE Status = 'Open' AND Responsibility = 10", headers={
        'Authorization': 'Bearer f33e0ae5f9d06e9fa3c9e09f87bb88ecc4cf3848'})

    MI_open_changes = open_changes_MI.json()['records'][0]['fields']['COUNT(Description)']
    MI_open_rfis = rfi_MI.json()['records'][0]['fields']['COUNT(Number)']
    MI_open_submittals = submittals_MI.json()['records'][0]['fields']['COUNT(Description)']
    correspondence_MI = correspondence_MI.json()['records'][0]['fields']['COUNT(Number)']
    return render_template('MI.html', change=MI_open_changes, rfi=MI_open_rfis, submittal=MI_open_submittals, corr=correspondence_MI)

if __name__ == '__main__':
    app.run(debug=True)
