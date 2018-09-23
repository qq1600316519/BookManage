from . import home_blue
from flask import render_template, request, flash
from main import *
from flask import redirect
#从当前包的_init_中导入文件


#用蓝图对象装饰路由
@home_blue.route("/delete_author/<int:author_id>")
def delete_author(author_id):
    #根据id
    try:
        author = Author.query.get(author_id)
        #先删除author对应的书
        for item in author.books:
            db.session.delete(item)
        db.session.delete(author)
        db.session.commit()

    except Exception:
        db.session.rollback()
        flash("数据库正在升级中!")
        return redirect(url_for("home_blue.index"))
    return redirect(url_for("home_blue.index"))


@home_blue.route("/delete_book/<int:book_id>")
def delete_book(book_id):
    #根据图书id删除
    try:
        book = Book.query.get(book_id)
        db.session.delete(book)
        db.session.commit()

    except Exception:
        db.session.rollback()
        flash("数据库升级中")
        return redirect(url_for("home_blue.index"))
    return redirect(url_for("home_blue.index"))