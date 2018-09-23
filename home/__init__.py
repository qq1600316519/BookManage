from flask import Blueprint
#创建蓝图对象
home_blue = Blueprint("home_blue",__name__)

from  .index import *