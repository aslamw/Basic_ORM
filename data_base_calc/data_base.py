from sqlalchemy import \
Column, ForeignKey, Integer, String, create_engine

from sqlalchemy.orm import \
declarative_base

engine = create_engine("sqlite:///./data_base_calc/formulas.db", echo = True)

Base = declarative_base()

class Form(Base):
    __tablename__ = "formulas"
    
    id = Column(Integer, primary_key = True)
    name = Column(String(50))
    form_visual = Column(String, nullable = False)
    form_colde = Column(String, nullable = False)
    data = Column(String, nullable = False)
    
    def __repr__(self):
        return f'Form(name = \
            {self.name}, form_visual = {self.form_visual}, \
            form_colde = {self.form_colde}, data = {self.data})'
            
class History(Base):
    __tablename__ = "history_user"
    
    id = Column(Integer, primary_key = True)
    id_form = Column(Integer, ForeignKey("formulas.id"), nullable = False)
    save_calc = Column(String, nullable = False)
    data = Column(String, nullable = False)
    
    def __repr__(self):
        return f"History(save_calc = {self.save_calc} \
            data = {self.data})"
            
Base.metadata.create_all(engine)