# Add any model classes for Flask-SQLAlchemy here
import datetime

from . import db
from werkzeug.security import generate_password_hash


class Movies(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of Movies would create a
    # movies (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.Text(128))
    poster = db.Column(db.String(80))
    created_at = db.Column(db.DateTime, default=datetime.UTC)

    def __init__(self, title, description, poster, created_at):
        self.title = title
        self.description = description
        self.poster = poster
        self.created_at = created_at

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)