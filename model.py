from flask_sqlalchemy import SQLAlchemy

# allows us to hash/encrypt passwords
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
	"""sumtea User"""

	__tablename__ = "users"

	user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	email = db.Column(db.String(75), nullable=False)
	password_hash = db.Column(db.String(128), nullable=False)

	# TODO: suggestion backreference

	