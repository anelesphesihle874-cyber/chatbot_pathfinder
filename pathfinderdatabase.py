
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)


# =========================================================
# DATABASE
# =========================================================

db = SQLAlchemy()


# =========================================================
# PROGRAMMES TABLE
# =========================================================

class Programmes(db.Model):
    """
    Store all programmes available at UNIZULU.
    """

    # -----------------------------------------
    # Primary key
    # -----------------------------------------

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # -----------------------------------------
    # Programme information
    # -----------------------------------------

    name_of_prog = db.Column(
        db.String,
        nullable=False,
        unique=True
    )

    mathematics = db.Column(
        db.String,
        nullable=False
    )

    physx = db.Column(
        db.String,
        nullable=False
    )

    english = db.Column(
        db.String,
        nullable=False
    )

    req_points = db.Column(
        db.Integer,
        nullable=False
    )

    # -----------------------------------------
    # Date created
    # -----------------------------------------

    date_created = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


# =========================================================
# LEARNERS TABLE
# =========================================================

class Learners(db.Model):
    """
    Store registered learner information.
    """

    # -----------------------------------------
    # Primary key
    # -----------------------------------------

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # -----------------------------------------
    # Learner information
    # -----------------------------------------

    name = db.Column(
        db.String,
        nullable=False
    )


    email = db.Column(
        db.String,
        nullable=False,
        unique=True
    )


    password = db.Column(
        db.String,
        nullable=False
    )

    phone_no = db.Column(
            db.String,
            nullable=False
        )

    date_created = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    # -----------------------------------------
    # Password functions
    # -----------------------------------------

    def set_password(self, password):
        """
        Hash the learner's password
        before storing it in the database.
        """

        self.password = generate_password_hash(
            password
        )

    def check_password(self, password):
        """
        Check whether the entered password
        matches the stored password hash.
        """

        return check_password_hash(
            self.password,
            password
        )


class other_Programmes(db.Model):


    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name_of_prog = db.Column(
        db.String,
        nullable=False,
        unique=True
    )

    mathematics = db.Column(
        db.String,
        nullable=False
    )

    math_lit = db.Column(
        db.String,
        nullable=False
    )

    english = db.Column(
        db.String,
        nullable=False
    )

    life_science = db.Column(
            db.String,
            nullable=False
        )

    req_points = db.Column(
        db.Integer,
        nullable=False
    )

    date_created = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )