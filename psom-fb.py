from bottle import get, post, request, run


@get('/login')
def login():
    return '''
        <form action="/login" method="post">
        Username: <input name="username" type="text" />
        Password: <input name="password" type="password" />
        <input value="Login" type="submit" />
        </form>
    '''


@post('/login')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login was correct, .</p>"
    else:
        return "<p>Login failed.</p>"


def check_login(username, password):
    if username == "Marco" and password == '1234':
        return True


run(host='localhost', port=8080)







4$$%^^&*(())))))))))))_
































