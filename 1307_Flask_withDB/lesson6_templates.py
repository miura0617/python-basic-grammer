import sqlite3
from flask import Flask  # Webフレームワーク
from flask import g
from flask import render_template
from flask import request
from flask import Response


app = Flask(__name__)  # appをグローバルで宣言


def get_db():
    """
    DBを作られていなかったら作って、DBのコネクションを返す
    """
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('test_sqlite.db')
    return db

@app.teardown_appcontext
def close_connection(exception):
    """
    DBに接続状態だったら、接続を切断します    

    Parameters
    ----------
    exception : [type]
        [description]
    """
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/employee', methods=['POST', 'PUT', 'DELETE'])
@app.route('/employee/<name>', methods=['GET'])
def employee(name=None):
    db = get_db()
    curs = db.cursor()
    curs.execute(
        'CREATE TABLE IF NOT EXISTS persons( '
            'id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)')
    db.commit()

    name = request.values.get('name', name)  # nameが入っていたら、nameでDBから引っぱってくる
    if request.method == 'GET':
        curs.execute('SELECT * FROM persons WHERE name = "{}"'.format(name))
        person = curs.fetchone()
        if not person:
            return "No", 404      # 404はHTTPのステータスコード
        user_id, name = person
        return '{}:{}'.format(user_id, name), 200   # 200はHTTPのステータスコード

    if request.method == 'POST':
        curs.execute('INSERT INTO persons(name) values("{}")'.format(name))
        db.commit()
        return 'created {}'.format(name), 201
    

    if request.method == 'PUT':
        new_name = request.values['new_name']
        curs.execute('UPDATE persons set name = "{}" WHERE name = "{}"'.format(
            new_name, name
        ))
        db.commit()
        return 'updated {}: {}'.format(name, new_name), 200

    
    if request.method == 'DELETE':
        curs.execute('DELETE from persons WHERE name = "{}"'.format(name))
        db.commit()
        return 'deleted {}'.format(name), 200
    
    curs.close()

@app.route('/')
def hello_world():
    return 'top'

@app.route('/hello')              # <username> を入れない場合も表示したいときは、左のデコレータも入れておく
@app.route('/hello/<username>')   # <username> を入れてアクセスすると、usernameを変数として使える
def hello_world2(username=None):  # <username> を入れない場合も表示したいときは、デフォルト値Noneにしておく
    #return 'hello world! {}'.format(username)
    return render_template('hello.html', username=username)  # templatesを使うと、こうやって書ける

@app.route('/post', methods=['POST', 'PUT', 'DELETE'])  # GETでは /post にアクセスできない状態
def show_post():
    #return str(request.values)
    return str(request.values['username'])

def main():
    app.debug = True
    app.run()
    # app.run(host='127.0.0.1', port=5000)   # flaskのデフォルトのIPは「127.0.0.1」、ポートは「5000番」


if __name__ == '__main__':
    main()





