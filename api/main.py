import sys
# To allow the api to see the 'catt' module
sys.path.extend(['.', '..'])

from flask import Flask
from flask_restful import Api
import resources

# Setting the name for the Flask application 
# __name__ name of the current python module
app = Flask(__name__)
api = Api(app)


# Resources URLs
api.add_resource(resources.TemplateList,
    '/catt/templates', endpoint = 'templates')
api.add_resource(resources.TemplateDetail, 
    '/catt/templates/<string:name>',endpoint = 'template')

if __name__ == '__main__':
    # run the application on the local development server
    # app.run(host, port, debug, options)
    app.run(debug=True)

    # If you have the debugger disabled or trust the users on your network, 
    # you can make the server publicly available simply by adding --host=0.0.0.0 
    # to the command line
    # flask run --host=0.0.0.0