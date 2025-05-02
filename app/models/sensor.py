from app.providers.extensions import db
from config.timezone import ID_timezone

class Sensor(db.Model):
    __tablename__ = 'sensors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    value = db.Column(db.Float, nullable=True)
    created_at = db.Column(db.DateTime, default=ID_timezone)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "value": self.value,
            "created_at": self.created_at.isoformat()
        }
