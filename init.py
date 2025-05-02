from app import db, User

def initialize_users():
    if not User.query.first():
        admin = [
            User(username='admin', password=User.hash_password('admin123'), email='admin@mail.com'),
            User(username='user', password=User.hash_password('user123'), email='user@mail.com'),
        ]
        db.session.add(admin)
        db.session.commit()