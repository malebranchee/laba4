from flask import Flask, request, render_template
from UserLogin import login_check
import unittest

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

data = login_check()
@app.route('/form_login', methods=['POST', 'GET'])
def login():
    user_log = request.form['username']
    user_password = request.form['password']
    if user_log not in data:
        return render_template('index.html',
                               info='Invalid User')
    else:
        if data[user_log] != user_password:
            return render_template('index.html',
                                   info='Invalid Password')
        else:
            return render_template('processed.html',
                                   name=user_log)




class TestLogin(unittest.TestCase):
        def setUp(self):
            self.app = app.test_client()

        def test_page_access(self):
            pointer = self.app.get('/')
            self.assertEqual(pointer.status, '200 OK') #All is good
            pointer = self.app.get('/form_login')
            self.assertEqual(pointer.status, '400 BAD REQUEST') #Bad request

        def test_login(self):
            getInfo = login_check()
            self.assertEqual(getInfo, {'Pavel': 'JohnMcTavish', 'zxc': 'qwe'}) #Testing UserLogin.py function
            self.assertTrue(getInfo, None)

        def test_404(self):
            pointer = self.app.get('/other')
            self.assertEqual(pointer.status, '404 NOT FOUND') #Not found :(

if __name__ == "__main__":
 unittest.main()
