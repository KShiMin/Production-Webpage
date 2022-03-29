# file to run when want to start web server / website
from website import create_app

app = create_app()

if __name__ == '__main__': # only allow web server to run if this file is ran directly
    # going to run the web server
    # debug = true --> anytime python code is ran, we server is automatically re-run
    # host = '0.0.0.0' allow external visibility 
    app.run(debug=True, host='0.0.0.0', port="8080")