from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(app)


class Project(db.Model):
    """Class to model projects for the Portfolio"""
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column('Created', db.DateTime, default=datetime.datetime.now)
    title = db.Column('Title', db.String())
    completion_date = db.Column('Date', db.DateTime)
    description = db.Column('Description', db.Text)
    skills = db.Column('Skills', db.Text)
    github = db.Column('Github', db.String())


def __repr__(self):
    return f'''< Project (Title = {self.title}
            Completion Date = {self.completion_date}
            Description = {self.description}
            Skills = {self.skills}
            Github = {self.github}'''
