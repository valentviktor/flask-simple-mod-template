from app import db, User

def initialize_users():
    if not User.query.first():
        admin = [
            User(name='admin', username='admin', password=User.hash_password('admin123'), email='admin@mail.com'),
            User(name='user', username='user', password=User.hash_password('user123'), email='user@mail.com'),
        ]
        db.session.add_all(admin)
        db.session.commit()