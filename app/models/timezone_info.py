from app import db


class TimezoneInfo(db.Model):
    """
    Define the timezone info model.
    """

    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.String(22), db.ForeignKey("store_status.id"))
    timezone = db.Column(db.String(100))
