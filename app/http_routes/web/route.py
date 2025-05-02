from flask import Blueprint, session, redirect, url_for, request

web_bp = Blueprint('web', __name__)

@web_bp.route('/')
def index():
    if not session.get('user'):
        session['next'] = request.url
        return redirect(url_for('auth.login'))

    next_url = session.pop('next', None)
    if next_url:
        return redirect(next_url)

    return redirect(url_for('dashboard.index'))