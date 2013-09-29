from blogflask import app


@app.route('/')
def hello_world():
    ss = 'asd'
    dd = ss + 'qq'
    return 'Hello World!' + dd
