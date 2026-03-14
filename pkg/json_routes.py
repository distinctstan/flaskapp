import json
from pkg import app
from pkg.models import Brand

@app.route('/json/')
def jsonview():
    # jsondata = '{"name":"Python Guys"}'
    # jsondata = {
    #     "schoolName":"Moat Academy",
    #     "students":{
    #         "student1":{
    #             "name":"Godwin",
    #             "topics":["JS","MySQL"]
    #         },
    #         "student2":{
    #             "name":"Daniel",
    #             "topics":["html","css"]
    #         },
    #         "student3":{
    #             "name":"Folarin",
    #             "topics":["Python","MySQL"]
    #         },
    #         "student4":{
    #             "name":"Chidera",
    #             "topics":["JQuery","Flask"]
    #         }
    #     }
    # }
    # jsondata = '{"name":"Stan","topics":["BS","JS","Python","Flask"]}'
    # jsondict = json.loads(jsondata) # Converts json to python dictionary
    # print(jsondict['topics'])
    # return jsondata

    # jsondata = {"name":"Stan","topics":["BS","JS","Python","Flask"]}
    # jsonstr = json.dumps(jsondata,indent=3,sort_keys=True)
    bran = Brand.query.all()
    result = [b.name for b in bran]
    return json.dumps(result)

