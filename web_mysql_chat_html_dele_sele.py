import pymysql
from flask import Flask, render_template, request
db = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="apmsetup", db="chatdb", charset='utf8')
app = Flask(__name__)
state='off'
rows='1234567890'
@app.route('/')
def iii():
        return render_template('index_chat_dele_sele.html', state=state)
@app.route('/chat')
def inser():
        global state
        send=request.args.get('send')
        recv=request.args.get('recv')
        record=request.args.get('record')
        cur = db.cursor()
        sql = "insert into basictable (bsendname, brecvname, brecord, bdate) values ('%s', '%s', '%s', NOW());" % (send, recv,record)
        cur.execute(sql)
        db.commit()
        return render_template('index_chat_dele_sele.html', state=state)
@app.route('/dele')
def dele():
        global state
        dele=request.args.get('dele')
        cur = db.cursor()
        sql = "delete from basictable where bsendname = '%s';" % dele
        cur.execute(sql)
        db.commit()
        return render_template('index_chat_dele_sele.html', state=state)
@app.route('/sele')
def sele():
        global rows
        sele=request.args.get('sele')
        cur = db.cursor()
        sql = "select * from basictable where bsendname = '%s';" % sele
        cur.execute(sql)
        rows = cur.fetchall()
        print(rows)
#        rows=rows
        return render_template('index_chat_dele_sele.html', rows=rows)
if __name__ == '__main__':
        print('Webserver ready...')
        app.run(host='0.0.0.0', port=8888)
        print('Webserver shutting down...')
        db.close()