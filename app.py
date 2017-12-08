from flask import Flask,jsonify
import json


app = Flask(__name__)
jData = json.loads(open('./car.json').read())
data=jData["Cars"]

@app.route('/')
def Car_main():
    return "RESTful API Assignment"

@app.route('/getcar/')
def car_all():
    myList=[]
    for element in data:
        myList.append(element)
    return jsonify(myList)

@app.route('/getcar/<string:id>/')
def car_model(id=''):
    myList=[]
    for element in data:
        if element['id'] == id:
            myList.append(element)
    result = jsonify(myList)
    return result

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
