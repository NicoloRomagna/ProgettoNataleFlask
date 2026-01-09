from . import db
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(200))

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    min_players = db.Column(db.Integer)
    max_players = db.Column(db.Integer)
    difficulty = db.Column(db.String(20))

class GameNight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    date = db.Column(db.Date)
    location = db.Column(db.String(100))
    notes = db.Column(db.Text)
    created_by = db.Column(db.Integer, db.ForeignKey("user.id"))

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    night_id = db.Column(db.Integer, db.ForeignKey("game_night.id"))