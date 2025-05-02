from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_required

dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@dashboard.route('/')
@login_required
def index():
    return render_template('pages/dashboard/index.html')