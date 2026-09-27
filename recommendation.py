from datetime import date
from flask_sqlalchemy import SQLAlchemy

from pathfinderdatabase import DATABASE_FILE

def get_connection():
    connection = SQLAlchemy.connect(
        DATABASE_FILE
    )

    connection.row_factory = SQLAlchemy.row
    return connection



def get_closing_dates(
        connection,
        programme_id

):

    cursor = connection.cursor()
    cursor.execute(


        (
            programme_id
        )
    )

    rows = cursor.fetchall()

    closing_dates =[]
    for row in rows:
        closing_dates.append(
            {
                
            }
        )