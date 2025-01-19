from bottle import route, run

@route('/')
@route('/hello')
def hello():
    return "Hello World!!!"

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)