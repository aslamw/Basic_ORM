import data_base as db
import time
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

engine = create_engine("sqlite:///./data_base_calc/formulas.db", echo = True)
session = Session(db.engine)

get_name = input('nome da formula: _')
get_form_visual = input('formula visual: _')
get_form_code = input('formula padrão python: _')

sub = db.Form(
        name = get_name,
        form_visual = get_form_visual,
        form_colde = get_form_code,
        data = f'{time.localtime()[2]}-{time.localtime()[1]}-{time.localtime()[0]}'
        
    )
session.add_all([sub])
session.commit()