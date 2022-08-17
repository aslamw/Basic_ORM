import data_base as db
from sqlalchemy.orm import Session
from sqlalchemy import select

session = Session(db.engine)

stmt = select(db.Form).where(db.Form.name.in_(['soma', 'divisão']))

for user in session.scalars(stmt):
    print(user.form_visual)


