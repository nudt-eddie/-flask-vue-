from flask import Flask, jsonify, request, Response
from flask_cors import *
from flask import render_template #引入模板插件
from prettytable import from_json
from WeiboLogin import loginClient
import json
from info import Info

app = Flask(__name__,
static_folder='vue/static',  # 设置静态文件夹目录
template_folder = "vue")  # 设置vue编译输出目录dist文件夹，为Flask模板文件目录
CORS(app, supports_credentials=True) # 跨域解决方案

global cookie
global info
global uid
global statuses_dict


def execute(uname:str, passwd:str):
    """登录到微博

    Args:
        uname (str): 用户名
        passwd (str): 密码
    """
    client = loginClient(debug=True)
    cookie = client.main(uname, passwd)
    return cookie
def get_Cookie():
    try:
        with open('cookies.json', 'r') as f:
            cookie = json.load(f)
            return cookie
    except FileNotFoundError:
        pass
    
@app.route('/')
@app.route('/login')
def index():
    return render_template('index.html',name='index') #使用模板插件，引入index.html。此处会自动Flask模板文件目录寻找index.html文件。

"""
login 的后端api
""" 
@app.route("/api/checklogin", methods=['POST'])
def login():
    global cookie
    if request.method == 'POST' and request.form.get('username') and request.form.get('password'):
        data = request.form.to_dict()
        uname = data.get("username")
        passwd = data.get("password")
        cookie = execute(uname, passwd)
        if cookie == -1:
            return Response("-1")
        else:
            with open('cookies.json', 'w+') as f:
                json.dump(cookie, f)
            return Response("0")
    else:
        return Response("-1")

@app.route("/api/search", methods=['POST'])
def search():
    global uid
    global info
    global cookie
    cookie = get_Cookie()
    info = Info(cookie)
    if request.method == 'POST' and request.form.get('uname'):
        data = request.form.to_dict()
        uname = data.get("uname")
        uid = info.get_Info(uname)
        if uid == 0:
            print("cookie已失效,请重新登录")
            return Response("-1")
        else:
            res = info.show_Info(uid)
            return jsonify(res)

@app.route("/api/friends", methods=['GET'])
def friends():
    if request.method == 'GET':
        res = info.get_Friends(uid)
        '''with open("C:\\Users\\Lenovo\\Desktop\\json_tmp.txt", "w") as fp:
            fp.write(json.dumps(res,indent=4))'''
        return jsonify(res)
    
@app.route("/api/fans", methods=['GET'])
def fans():
    if request.method == 'GET':
        res = info.get_Followers(uid)
        return jsonify(res)
    
@app.route("/api/statuses", methods=['GET'])
def statuses():
    global statuses_dict
    if request.method == 'GET':
        info.get_weibo(uid)
        statuses_dict = info.get_Statuses(uid)
        res = statuses_dict
        return jsonify(res)

@app.route("/api/comments", methods=['GET'])
def comments():
    if request.method == 'GET':
        info.get_Commentstxt(uid)
        res = info.get_Comments(uid, statuses_dict)
        return jsonify(res)    

@app.route("/api/check", methods=['GET'])
def check():
    global statuses_dict
    if request.method == 'GET':
        res = info.check(uid, statuses_dict)
        if res == -1:
            return Response("-1")
        else:
            statuses_dict = res
            return jsonify(res)
            
if __name__ == '__main__':
    app.run(debug=True)