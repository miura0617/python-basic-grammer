from flask import Flask  # Webフレームワーク
from flask import g
from flask import render_template
from flask import request
from flask import Response


app = Flask(__name__)  # appをグローバルで宣言

@app.route('/')
def hello_world():
    return 'top'

@app.route('/hello')              # <username> を入れない場合も表示したいときは、左のデコレータも入れておく
@app.route('/hello/<username>')   # <username> を入れてアクセスすると、usernameを変数として使える
def hello_world3(username=None):  # <username> を入れない場合も表示したいときは、デフォルト値Noneにしておく
    return 'hello world! {}'.format(username)

def main():
    app.debug = True
    app.run()
    # app.run(host='127.0.0.1', port=5000)   # flaskのデフォルトのIPは「127.0.0.1」、ポートは「5000番」


if __name__ == '__main__':
    main()





