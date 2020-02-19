from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """sumtea User"""
    
    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(75), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    # relationships(~children)
    suggestions = db.relationship("Suggestion", backref="User")

    def __repr__(self):
        """User info when return object!"""

        return f"<User user_id={self.user_id} email={self.email}>"

    # functions to encrypt/hash passwords; RETURNS NONE
    def set_password(self, password):
        """Hashing the password."""

        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Checking to see if inputted password is correct."""

        return check_password_hash(self.password_hash, password)

# association table between suggestions and teas: many to many relationship
association_table = db.Table("associations", db.Model.metadata,
	# suggestions
    db.Column("sugg_id", db.Integer, db.ForeignKey("suggestions.sugg_id")),
    # teas
    db.Column("tea_id", db.Integer, db.ForeignKey("teas.tea_id"))
)

class Suggestion(db.Model):
    """Tea suggestions!"""

    __tablename__ = "suggestions"

    sugg_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    # foreign keys(~parent)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    # relationships(~children)
    tea = db.relationship("Tea", 
                        secondary=association_table)



class Tea(db.Model):
    """Tea info!"""

    __tablename__ = "teas"

    tea_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    tea_type = db.Column(db.String(75))
    tea_name = db.Column(db.String(75))
    caffeine = db.Column(db.Boolean)
    alertness = db.Column(db.Integer)
    mental_state = db.Column(db.Integer)
    body_temp = db.Column(db.Integer)

class Note(db.Model):
    """User's notes on teas they've tried."""

    __tablename__ = "notes"
    
    note_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    rating = db.Column(db.Integer)
    alertness = db.Column(db.Integer)
    mental_state = db.Column(db.Integer)
    body_temp = db.Column(db.Integer)
    tasting_notes = db.Column(db.String(128))
    comments = db.Column(db.String(500))

    # foreign keys(~parent)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    sugg_id = db.Column(db.Integer, db.ForeignKey("suggestions.sugg_id"))
    
    # relationships(~children)


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