#主文件
from flask import Flask, url_for
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from home import home_blue
app = Flask(__name__)

#设置ｓｅｓｓｉｏｎ秘钥
app.secret_key = "test"

#注册蓝图路由
app.register_blueprint(home_blue)

#配置数据库
# 设置数据库连接地址
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:mysql@127.0.0.1:3306/bookmanage"
# 是否追踪数据库修改  开启后, 会影响性能, 不建议开启
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# 创建数据库连接
db = SQLAlchemy(app)

#app管理器
mgr = Manager(app)
#数据迁移器
Migrate(app,db)
#使用管理器管理迁移器　
mgr.add_command("mc",MigrateCommand)


#创建作者表
class Author(db.Model):
    """创建作者表"""
    #表名
    __tablename__ = "author"
    #主键字段
    id = db.Column(db.Integer,primary_key=True)
    #作者名字段
    name = db.Column(db.String(50),unique=True)
    #关联属性,通过books可以查看关联的图书
    books = db.relationship("Book",backref="author")

#创建图书表
class Book(db.Model):
    """图书表"""
    #表名
    __tablename__ = "book"
    #主键字段
    id = db.Column(db.Integer,primary_key=True)
    #图书名字段
    name = db.Column(db.String(50))
    #外键,关联作者
    author_id = db.Column(db.Integer,db.ForeignKey("author.id"))



if __name__ == '__main__':
    print(app.url_map)
    mgr.run()


