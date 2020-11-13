from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

from app import db

class UserMail(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(256), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    register_date = db.Column(db.DateTime, default=datetime.utcnow)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f'<User {self.email}>'
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_email(email):
        return UserMail.query.filter_by(email=email).first()

    @staticmethod
    def get_by_email_token(email):
        return UserMail.query.filter_by(email=email).first_or_404()

    @staticmethod
    def get_by_id(user_id):
        return UserMail.query.filter_by(id=user_id).first()

    @staticmethod
    def get_all():
        return UserMail.query.all()