import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///instance/swastha.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USERNAME = 'your_email@gmail.com'
    MAIL_PASSWORD = 'your_app_password'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
