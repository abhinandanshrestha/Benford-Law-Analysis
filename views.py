from pyramid.view import view_config
import csv
from pyramid.httpexceptions import HTTPBadRequest
from benfordParams import benfordParams
from pyramid.response import Response
import json

@view_config(route_name='home', renderer='templates/index.jinja2')
def home_view(request):
    return {'title':'Benford Law Analysis','message':'Note* that it only sends json response for the data that follows Benford\'s Law'}

@view_config(route_name="benford",renderer="json")
def benford(request):
    if request.method=='POST' and request.POST['csvInput'].file:
        csv_file = request.POST['csvInput'].file
        filename = request.POST['csvInput'].filename 
        name, ext = filename.split('.')
        if not ext == 'csv':
            return {"Error": "Invalid File Input! Please upload CSV file"}
        else:
            data=[]
            reader = csv.reader(csv_file.read().decode('utf-8').splitlines())
            for row in reader:
                data.extend(row)

            results, conform = benfordParams(data)

            if conform==True:
                with open("uploads/benford.json", "w") as f:
                    json.dump(results, f)
                    return Response(json.dumps(results))
            else:
                return Response("Data doesn't follow Benford's Law.")