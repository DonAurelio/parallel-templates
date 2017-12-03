from flask_restful import Api

# Setting the name for the Flask application 
# __name__ name of the current python module
app = Flask(__name__)

class Service(Api):
    def handle_error(self, e):
        # Attach the exception to itself so Flask-Restful's error handler
        # tries to render it.
        if not hasattr(e, 'data'):
            e.data = e
