import data_base as db
from sqlalchemy.orm import Session
from sqlalchemy import select

session = Session(db.engine)

stms = select(db.Form).where(db.Form.name == 'soma')
form = session.scalars(stms).one()

form.form_visual = '1 + 1 = 2'

session.commit()