from flask import Blueprint, request, jsonify, url_for
from app import db, mail
from app.models import User
from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer
import os

# Define the blueprint for routes
main = Blueprint('main', __name__)

@main.route('/')
def hello_world():
    return "<p>Welcome!</p>"
    
    
