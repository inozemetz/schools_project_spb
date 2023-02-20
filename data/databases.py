import sqlalchemy
from .db_session import SqlAlchemyBase


class Schools(SqlAlchemyBase):
    __tablename__ = 'schools'
    school_id = sqlalchemy.Column(sqlalchemy.Integer,primary_key=True)
    school_name = sqlalchemy.Column(sqlalchemy.String)
    res_ege = sqlalchemy.Column(sqlalchemy.Integer)
    district_id = sqlalchemy.Column(sqlalchemy.Integer)
    link = sqlalchemy.Column(sqlalchemy.String)

class Otzivi(SqlAlchemyBase):
    __tablename__ = 'feedback'
    review = sqlalchemy.Column(sqlalchemy.Text,primary_key=True)


