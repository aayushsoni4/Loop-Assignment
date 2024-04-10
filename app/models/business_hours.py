from app import db


class BusinessHours(db.Model):
    """
    Define the business hours model.
    """

    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.String(22), db.ForeignKey("store_status.id"))
    day_of_week = db.Column(db.Integer)
    open_time = db.Column(db.Time)
    close_time = db.Column(db.Time)
