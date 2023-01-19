from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/',methods=['get'])
def view():
    file = open("data.json")
    data = json.load(file)
    return data

@app.route('/add',methods=['post'])
def add():
    val = request.get_json()
    with open("data.json") as file:
        d = json.load(file)
    d.append(val)
    with open("data.json", "w") as file:
        json.dump(d, file)
    return {"status":"successfull","data":d}

@app.route('/update',methods=['put'])
def data_update():
    val = request.get_json()
    with open("data.json") as file:
        d = json.load(file)
    for i in d:
        if i["emp_name"]==val["emp_name"]:
            index_i=d.index(i)
            d[index_i]=val
    with open("data.json",'w') as y:
        json.dump(d,y)
    
    return "updated successfully"

@app.route('/delete',methods=['delete'])
def delete_data():
    val = request.get_json()
    with open("data.json") as file:
        d = json.load(file)
    for i in d:
        if i["emp_name"]==val["emp_name"]:
            index_i=d.index(i)
            del d[index_i]
    with open("data.json",'w') as y:
        json.dump(d,y)
    
    return "deleted successfully"

if __name__ == '__main__':
    app.run(debug= True)