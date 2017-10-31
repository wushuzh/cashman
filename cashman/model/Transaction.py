import datetime as dt
from marshmallow import Schema, fields


class Transaction(object):
    def __init__(self, description, amount, typ):
        self.description = description
        self.amount = amount
        self.created_at = dt.datetime.now()
        self.typ = typ

    def __repr(self):
        return '<Transaction(name={self.description!r})>'.format(self=self)


class TransactionSchema(Schema):
    description = fields.Str()
    amount = fields.Number()
    created_at = fields.Date()
    typ = fields.Str()
