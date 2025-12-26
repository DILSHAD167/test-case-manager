from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TestCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(50), default="Not Run")

def init_db(app):
    with app.app_context():
        db.create_all()
