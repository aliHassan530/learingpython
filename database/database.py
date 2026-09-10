from sqlmodel import create_engine, SQLModel, Session

# apna MySQL username, password, database name yahan daalo
DATABASE_URL = "mysql+pymysql://root:Ah7163259%21%21@localhost:3306/myapp_db"
engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session