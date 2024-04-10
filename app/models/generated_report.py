from app import db

class GeneratedReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    csv_data = db.Column(db.LargeBinary, nullable=False)
