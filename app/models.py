from datetime import datetime

from sqlalchemy.dialects.postgresql import UUID

from app import db
import uuid


class PaymentModel(db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key=True)
    shop_order_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    amount = db.Column(db.DECIMAL)
    currency = db.Column(db.CHAR(3))
    description = db.Column(db.Text, default="")
    date_created = db.Column(db.DateTime, default=datetime.utcnow())
