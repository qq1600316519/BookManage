from . import home_blue
from flask import render_template
#从当前包的_init_中导入文件
#初始化蓝图对象


#蓝图对象装饰路由
@home_blue.route("/",methods=["GET","POST"])
def index():
    return render_template("book_test.html")