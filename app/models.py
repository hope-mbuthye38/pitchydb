from . import db

#...

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    bio = db.Column(db.string(255))
    profile_pic_path = db.Column(db.string(255))
    password = db.Column (db.string(255))
    confirm_password =db.Column(db.string(255))
    def __repr__(self):
        return f'User {self.username}'

        _