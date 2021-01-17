#! /usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
#                  ΕΞΟΔΑ
#                  Ντίνι Ιορδάνης
#                  2021
# V 0.1
# -------------------------------------------------------------------------------
import datetime
import sys
from settings import database,  root_logger

from sqlalchemy import create_engine, Column, Integer,  String, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from sqlalchemy.ext.declarative import declarative_base

sys.stderr.write = root_logger.error
sys.stdout.write = root_logger.info


engine = create_engine(f"sqlite:///{database}")
Session = sessionmaker(bind=engine)()
Base = declarative_base()
metadata = MetaData


# Προμηθευτές
class Suppliers(Base):
    __tablename__ = "Suppliers"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    vat_nr = Column(Integer)
    phone = Column(String(16))
    address = Column(String(200))
    balance = Column(Integer)
    purchases = relationship("Purchases")
    payments = relationship("Payments")

    def __repr__(self):
        return "<Suppliers(id='%i', name='%s', vat_nr='%i', phone='%i', address='%s', balance='%i')>"\
               % (self.id, self.name, self.vat_nr, self.phone, self.address, self.balance)

    def __str__(self):
        return f"{self.name}"


# Παραλήπτες
class Recipients(Base):
    __tablename__ = "Recipients"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    phone = Column(String(16))
    address = Column(String(200))
    purchases = relationship("Purchases")

    def __repr__(self):
        return "<Recipients(id='%i', name='%s', phone='%i', address='%s')>" % (self.id, self.name,  self.phone, self.address)

    def __str__(self):
        return f"{self.name}"


# Αγορές
class Purchases(Base):
    __tablename__ = "Purchases"
    id = Column(Integer, primary_key=True)

    supplier_id = Column(Integer, ForeignKey('Suppliers.id'))
    supplier = relationship("Suppliers", backref=backref("purchase"))

    recipient_id = Column(Integer, ForeignKey('Recipients.id'))
    recipient = relationship("Recipients", backref=backref("recipient"))

    price = Column(Integer)
    product = Column(String(300))
    file = Column(String(360))
    date = Column(String(10))


# Πληρωμές
class Payments(Base):
    __tablename__ = "Payments"
    id = Column(Integer, primary_key=True)
    supplier_id = Column(Integer, ForeignKey("Suppliers.id"))
    supplier = relationship("Suppliers", backref=backref("supplier"))
    amount = Column(Integer,  nullable=False)
    date = Column(String(10))

    def __repr__(self):
        return "<Payments(supplier_id='%i', amount='%i', date='%date')>" % (self.supplier_id, self.amount, self.date)

    def __str__(self):
        return f"{self.supplier} {self.amount} {self.date}"

# Αποκόμηση δεδομένων απο τον πίνακα
def get_data(table):
    data = Session.query(table).all()
    return data


# Create Tables
# Base.metadata.create_all(engine)




# Insert data
# pay1 = Payments(supplier_id=9, amount=20, date=datetime.date.today())
# Session.add(pay1)
# Session.commit()
