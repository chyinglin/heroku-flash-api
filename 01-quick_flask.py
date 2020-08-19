
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello_world():
    process = subprocess.run(['robot', 'testcase.robot'], 
                         stdout=subprocess.PIPE, 
                         universal_newlines=True)

    # process = subprocess.run(['echo', 'testcase.robot'], 
    #                      stdout=subprocess.PIPE, 
    #                      universal_newlines=True)

    return 'run testcase\n' + process.stdout

@app.route('/test')
def test_page():
    return 'In test page!'


class APIDocs(Resource):
    def get(self, id):
        return {
            "id": id, 
            "version": "This is Version"
        }

api.add_resource(APIDocs, '/api/<string:id>')
