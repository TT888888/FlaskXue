# 导入第三方包，都放在这里
from flask_sqlalchemy import SQLAlchemy

from flask_session import Session

db = SQLAlchemy()

def init_ext(app):
    db.init_app(app=app)

    Session(app=app)
