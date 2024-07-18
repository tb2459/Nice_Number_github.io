from flask import Flask, render_template
import requests
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    rfi = requests.get("https://grist-ej.bballou.com/api/docs/cQbcmAcNgJ1u5YApQyF8WH/sql?q=SELECT COUNT(Number) FROM RFI_Log WHERE Status = 'Open'", headers={
     'Authorization': 'Bearer 7649966e88b32725ebd633ec124ab052414bb618'
})


    number = rfi.json()['records'][0]['fields']['COUNT(Number)']
    return render_template(
        'index.html',
        val=number
      
    )

if __name__ == '__main__':
    app.run(debug=True)