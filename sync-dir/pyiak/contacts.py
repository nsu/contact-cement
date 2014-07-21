from flask import Flask, render_template, request
import json
import riak
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('contacts.html')

@app.route("/echo/json/", methods=['GET', 'POST'])
def mockjson():
    print request.data
    myClient = riak.RiakClient(pb_port=8087, protocol='pbc')
    bucket = myClient.bucket('contacts')
    bucket.enable_search()
    docs = bucket.search('state:Tennessee')['docs']
    return json.dumps(docs)
    return json.dumps([ {"id": 1, "firstName": "Peter", "lastName": "Jhons"} ])

@app.route("/search/")
def searchriak():
    pass

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')

