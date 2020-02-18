from flask_sqlalchemy import SQLAlchemy

# allows us to hash/encrypt passwords
from werkzeug.security import generate_password_hash, check_password_hash

db=SQLAlchemy()

class User(db.Model):
	"""sumtea User"""

	__tablename__="users"

	user_id=db.Column(db.Integer, autoincrement=True, primary_key=True)
	email=db.Column(db.String(75), nullable=False)
	password_hash=db.Column(db.String(128), nullable=False)

	# TODO: suggestion backreference

	def __repr__(self):
		"""User info when return object!"""

		return f"<User user_id={self.user_id} email={self.email}>"

	# functions to encrypt/hash passwords; RETURNS NONE
	def set_password(self, password):
		"""Hashing the password."""

		self.password_hash=generate_password_hash(password)

	def check_password(self, password):
		"""Checking to see if inputted password is correct."""

		return check_password_hash(self.password_hash, password)