import sys
# To allow the api to see the 'catt' module
sys.path.extend(['.', '..'])

from flask import Flask
from flask_restful import Api
import resources


# API Error handling
class Service(Api):
    def handle_error(self,e):
        # Attach the exception to itself so Flask-Restful's error handler
        # tries to render it.
        if not hasattr(e, 'data'):
            e.data = e

# Flask API
app = Flask(__name__)
api = Service(app)


# Exceptions handling supported by the API
@api.representation('application/json')
def output_json_exception(data, code, *args, **kwargs):
    """Render exceptions as JSON documents with the exception's message."""
    if isinstance(data, TypeError):
        data = {'status': code, 'message': str(data)}

    return output_json(data, code, *args, **kwargs)


# Resources URLs
api.add_resource(resources.TemplateList,'/templates')
api.add_resource(resources.TemplateDetail,'/templates/<string:name>')

api.add_resource(resources.Catt,'/catt')


# API init
if __name__ == '__main__':
    # run the application on the local development server
    # app.run(host, port, debug, options)
    app.run(debug=True)

    # If you have the debugger disabled or trust the users on your network, 
    # you can make the server publicly available simply by adding --host=0.0.0.0 
    # to the command line
    # flask run --host=0.0.0.0