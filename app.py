from bottle import route, template, static_file, run, get


@route('/')
def index():
    return template("index.html", root='')


@get('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/img/<filename:re:.*\.(jpg|png|svg|jpeg)>')
def images(filename):
    return static_file(filename, root='img')


@get('/js/<filename:re:.*\.js>')
def logic(filename):
    return static_file(filename, root='js')


def main():
    run(host='localhost', port=7001, debug=True)


if __name__ == '__main__':
    main()
