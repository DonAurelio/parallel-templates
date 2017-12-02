from flask import Flask

# __name__ name of the current python module
app = Flask(__name__)

# URLS ROUTING
# The route decorator tells the application
# which function should call the associated
# URL
# app.route(rule, options)
# @app.route('/login', methods=['GET', 'POST'])
@app.route('/hello')
def hello_world():
    return 'Hello World'

# Another way to do the same 
# def hello_world():
#     return 'Hello World'
# app.add_url_rule('/','hello',hello_world)


# PARAMETERS TO URLS
@app.route('/hello/<name>')
def say_hello(name):
    return 'Hello %s' % name


if __name__ == '__main__':
    # run the application on the local development server
    # app.run(host, port, debug, options)
    app.run(debug=True)

    # If you have the debugger disabled or trust the users on your network, 
    # you can make the server publicly available simply by adding --host=0.0.0.0 
    # to the command line
    # flask run --host=0.0.0.0