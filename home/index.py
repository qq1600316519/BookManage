from . import home_blue
from flask import render_template, request, flash
from main import *
from flask import redirect
#从当前包的_init_中导入文件
#初始化蓝图对象


#蓝图对象装饰路由
@home_blue.route("/",methods=["GET","POST"])
def index():
    if request.method == "GET":
        #读取数据库中的作者列表，作为模板变量
        try:
            authors = Author.query.all()
        except BaseException:
            flash("数据库正在升级中,请稍后操作!")
            return redirect(url_for("home_blue.index"))
        return render_template("book_test.html", authors=authors)

    if request.method == "POST":
        #获取作者名
        author_name = request.form.get("author_name")
        #获取图书名
        book_name = request.form.get("book_name")
        #判断作者名和图书名是否为空
        #all当列表元素不是None,''等返回true,当其中有空的，返回ｆａｌｓｅ
        # 为空,return
        if not all([author_name,book_name]):
            flash("参数不能为空!")
            return redirect(url_for("home_blue.index"))

        #不为空,执行
        #判断数据库中是否存在作者名,不存在返回Ｎｏｎｅ
        try:
            author = Author.query.filter(Author.name==author_name).first()
        except BaseException:
            flash("数据库正在升级中!")
            return  redirect(url_for("home_blue.index"))

        # 存在，只添加图书名
        if author:
            # 创建一条图书记录
            add_book = Book(name=book_name)
            #添加到作者的关联属性中
            author.books.append(add_book)
            #提交
            db.session.add(add_book)
            db.session.commit()
            return redirect(url_for("home_blue.index"))
        #不存在,添加作者名　和　图书名　到数据库
        else:
            #创建一条作者记录
            add_author = Author(name=author_name)
            #创建一条图书记录
            add_book = Book(name=book_name)
            #添加到作者的关联属性中
            add_author.books.append(add_book)
            #提交
            db.session.add(add_book)
            db.session.commit()
            return redirect(url_for("home_blue.index"))






