from app import db


class StoreStatus(db.Model):
    """
    Define the store status model.
    """

    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.String(22))
    status = db.Column(db.String)
    timestamp_utc = db.Column(db.String)
    business_hours = db.relationship("BusinessHours", backref="store", lazy=True)
    timezone_info = db.relationship("TimezoneInfo", backref="store", lazy=True)
