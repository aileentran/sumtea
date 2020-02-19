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
	suggestions=db.relationship("Suggestion", backref="user")

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

class Suggestion(db.Model):
	"""Tea suggestions given to user based on questions answered."""

	__tablename__="suggestions"

	sugg_id=db.Column(db.Integer, autoincrement=True, primary_key=True)

	# relationships (children?)
	teas=db.relationship("Tea", backref="suggestion")
	notes=db.relationship("Note", backref="suggestion")

	# foreign keys (parents?)
	user_id=db.Column(db.Integer, db.ForeignKey("users.user_id"))
	note_id=db.Column(db.Integer, db.ForeignKey("notes.note_id"))
	tea_id=db.Column(db.Integer, db.ForeignKey("teas.tea_id"))
	

	def __repr__(self):
		"""Suggestion info when return object!"""

		return f"<Suggestion sugg_id={self.sugg_id} user_id={self.user_id} note_id={self.note_id} tea_id={self.tea_id}>"

class Note(db.Model):
	"""User's notes on teas they've tried."""

	__tablename__="notes"

	note_id=db.Column(db.Integer, autoincrement=True, primary_key=True)
	alert=db.Column(db.String(500))
	body_temp=db.Column(db.String(500))
	tasting_notes=db.Column(db.String(500))
	rating=db.Column(db.Integer)
	comments=db.Column(db.String(500))

	# relationships (chilren)

	# foreign keys (parent)
	sugg_id=db.Column(db.Integer, db.ForeignKey("suggestions.sugg_id"))

class Tea(db.Model):
	"""Tea info!"""

	__tablename__="teas"

	tea_id=db.Column(db.Integer, autoincrement=True, primary_key=True)
	tea_type=db.Column(db.String(128))
	tea_name=db.Column(db.String(128))
	caffeine=db.Column(db.Boolean())
	alert=db.Column(db.String(500))
	body_temp=db.Column(db.String(500))
	energy=db.Column(db.String(500))
	tasting_notes=db.Column(db.String(500))

	# relationships (chilren)

	# foreign keys (parent)
	sugg_id=db.Column(db.Integer, db.ForeignKey("suggestions.sugg_id"))























# Creating environment to make tables
def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Connecting to database!
    app.config["SQLALCHEMY_DATABASE_URI"]="postgresql:///sumtea"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.
    from server import app

    connect_to_db(app)
    print("Connected to DB.")