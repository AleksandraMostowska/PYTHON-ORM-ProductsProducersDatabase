from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    and_,
    func,
    MetaData,
    Table,
    ForeignKey,
    Numeric,
    text
)
from sqlalchemy.orm import declarative_base, sessionmaker
from decimal import Decimal
from typing import Self

USERNAME = 'user'
PASSWORD = 'user1234'
DATABASE = 'db_1'
PORT = 3307
URL = f'mysql://{USERNAME}:{PASSWORD}@localhost:{PORT}/{DATABASE}'
engine = create_engine(URL, echo=True)

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(225), unique=True, nullable=True)
    price = Column(Numeric(precision=6, scale=2))
    producer_id = Column(Integer)

    def save_or_update(self):
        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(self)
        session.commit()

    def __str__(self):
        return f'ID: {self.id}, NAME: {self.name}, PRICE: {self.price}, PRODUCERS ID: {self.producer_id}'

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return isinstance(other, Product) and self.id == other.id

    def __hash__(self):
        return hash((self.id, ))

    @staticmethod
    def get_all():
        Session = sessionmaker(bind=engine)
        session = Session()
        return session.query(Product).all()
