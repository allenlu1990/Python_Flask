import base64
from io import BytesIO
from matplotlib.figure import Figure
from flask import Flask,make_response
# Create your views here.


app = Flask(__name__)
# config对应同目录下的config.py（文件中定义DEBUG = True）
# app.config.from_object('config')


# 默认设置/hello/会自动将/hello重定向到/hello/
@app.route('/hello3', methods=["GET"])
def hello():
    headers = {
        # 默认为text/html
        'content-type': 'text/plain',
        # 设置跳转链接
        # 'location': 'http://alanhou.org'
    }
    fig = Figure()
    ax = fig.subplots()
    ax.plot([1, 2])
    buf = BytesIO()
    fig.savefig(buf, format='png')
    data = base64.b64encode(buf.getbuffer()).decode('ascii')
    response = make_response(f"<img src='data:image/png;base64,{data}'/>", 200)
    # response = make_response('Hello World!', 301)
    response.headers = headers
    return response

# 主入口文件时执行
if __name__ == '__main__':
    # 生产环境中使用nginx+uwsgi
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=8089)
