import data_base as db
from sqlalchemy.orm import Session

session = Session(db.engine)

soma = session.get(db.Form, 2)

session.delete(soma)

session.commit()