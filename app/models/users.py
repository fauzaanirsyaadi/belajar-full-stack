from app import db 
from datetime import datetime

class User(db.Model):
    user_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(250), nullable=False)
    user_email = db.Column(db.String(100), index=True, unique=True, nullable=False)# index untuk pencarian berdasarkan email, seperti login
    user_password = db.Column(db.String(250), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow())
    
    def __repr__(self):
        return f'User<{self.users_name}>'
        
