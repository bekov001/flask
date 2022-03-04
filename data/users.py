import datetime
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from werkzeug.security import check_password_hash, generate_password_hash

from .db_session import SqlAlchemyBase


class MarsUser(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    card = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    about = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)

    departments = orm.relation("Department", back_populates='user')
    jobs = orm.relation("Jobs", back_populates='user')

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    work_size = sqlalchemy.Column(sqlalchemy.Integer, nullable=True, default=0)
    collaborators = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, default=True)

    team_leader = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    user = orm.relation('MarsUser')

    categories = orm.relation("Category",
                              secondary="association",
                              backref="jobs")