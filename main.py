from fastapi import FastAPI

from database.database import init_db
from routes.user_routes import router
from routes.posts import router as posts_router


app = FastAPI()


# Database startup
@app.on_event("startup")
def on_startup():
    init_db()


# User routes
app.include_router(router)
app.include_router(posts_router)

# from fastapi import FastAPI, HTTPException, Depends
# from sqlmodel import Session, select

# from database.database import init_db, get_session
# from model.models import User


# app = FastAPI()


# # ---- DATABASE STARTUP ----
# @app.on_event("startup")
# def on_startup():
#     init_db()


# # ---- SIGNUP ----
# @app.post("/signup")
# def signup(
#     username: str,
#     email: str,
#     password: str,
#     session: Session = Depends(get_session)
# ):
#     # Check username
#     existing_username = session.exec(
#         select(User).where(User.username == username)
#     ).first()

#     if existing_username:
#         raise HTTPException(
#             status_code=400,
#             detail="Username already exists"
#         )

#     # Check email
#     existing_email = session.exec(
#         select(User).where(User.email == email)
#     ).first()

#     if existing_email:
#         raise HTTPException(
#             status_code=400,
#             detail="Email already exists"
#         )

#     # Create new user
#     new_user = User(
#         username=username,
#         email=email,
#         password=password
#     )

#     session.add(new_user)
#     session.commit()
#     session.refresh(new_user)

#     return {
#         "message": "Signup successful",
#         "user_id": new_user.id
#     }


# # ---- LOGIN ----
# @app.post("/login")
# def login(
#     email: str,
#     password: str,
#     session: Session = Depends(get_session)
# ):
#     # Find user by email
#     user = session.exec(
#         select(User).where(User.email == email)
#     ).first()

#     # Check credentials
#     if not user or user.password != password:
#         raise HTTPException(
#             status_code=401,
#             detail="Invalid email or password"
#         )

#     return {
#         "message": "Login successful",
#         "user_id": user.id
#     }
# from fastapi import FastAPI, HTTPException, Depends
# from sqlmodel import Session, select
# from database.database import init_db, get_session
# from model.models import User
# from sqlalchemy import select

# app = FastAPI()

# @app.on_event("startup")
# def on_startup():
#     init_db()

# # ---- SIGNUP ----
# @app.post("/signup")
# def signup(username: str,email:str, password: str, session: Session = Depends(get_session)):
#     existing = session.exec(select(User).where(User.username == username)).first()
#     if existing:
#         raise HTTPException(status_code=400, detail="Username already exists")

#     existing = session.exec(select(User).where(User.email == email)).first()
#     if existing:
#         raise HTTPException(status_code=400, detail="email already exists")

#     new_user = User(username=username,email=email, password=password)
#     session.add(new_user)
#     session.commit()
#     session.refresh(new_user)
#     return {"message": "Signup successful", "user_id": new_user.id}

# # ---- LOGIN ----
# @app.post("/login")
# def login(email:str, password: str, session: Session = Depends(get_session)):
    
#     user = session.exec(select(User).where(User.email == email)).first()
#     if not user or user.password != password:
#         raise HTTPException(status_code=401, detail="Invalid email or password")

#     return {"message": "Login successful", "user_id": user.id}


# # @app.get("/getAllUser")
# # def getAllUser(session: Session = Depends(get_session)):
# #     users = session.exec(select(User)).all()

# #     return [
# #         {
# #             "id": user.id,
# #             "username": user.username,
# #             "email": user.email
# #         }
# #         for user in users
# #     ]

# @app.get("/getAllUser")
# def getAllUser(session: Session = Depends(get_session)):
#     users = session.exec(select(User)).all()


#     return [
#         {
#             "id": user.id,
#             "username": user.username,
#             "email": user.email
#         }
#         for user in users
#     ]

# @app.get("/findPerson")
# def getAllUser(name:str,session: Session = Depends(get_session)):
#     users = session.exec(
#         select(User).where(User.username.))


#     return [
#         {
#             "id": user.id,
#             "username": user.username,
#             "email": user.email
#         }
#         for user in users
#     ]

# # from fastapi import FastAPI
# # from routes.car_routes import router as car_router
# # from routes.train_routes import router as train_router
# # from routes.bus_routes import router as bus_router
# # from routes.airoplane import router as airoplane

# # app = FastAPI()

# # app.include_router(car_router)
# # app.include_router(train_router)
# # app.include_router(bus_router)
# # app.include_router(airoplane)


# # @app.get("/")
# # def home():
# #     return {"message": "Welcome to my Car API"}

# # from fastapi import FastAPI, HTTPException
# # from model.car_model import CarHouse

# # app = FastAPI()


# # carList=[]





# # @app.get("/getAllCar")
# # def showAllCar(car:CarHouse):
# #     carList.append(car)
# #     return carList;



# # users = []


# # @app.get("/")
# # def home():
# #     return {"message": "Welcome to my API"}


# # # @app.get("/users")
# # # def get_users():
# # #     return users


# # @app.post("/addvalue")
# # def addValue(name: str):
# #     users.append(name)
# #     return {"value add" :name}
    

# # @app.get("/alluser")
# # def showUser():
# #     return {"show user display here": users}

# # # @app.delete("/deleteUser")
# # # def deleteUser(name:str):
# # #     if name not in users:
# # #         raise HTTPException(status_code=404,detail="User '{name}' not found")
# # #     users.remove(name)
# # #     return {"remove this user in this list": name}

# # @app.delete("/deleteUser")
# # def delete_user(name: str):

# #     if name not in users:
# #         raise HTTPException(
# #             status_code=404,
# #             detail=f"User '{name}' not found"
# #         )

# #     users.remove(name)

# #     return {
# #         "message": "User deleted successfully",
# #         "user": name
# #     }


# # @app.put("/replacePerson")
# # def replacePerson(indexValue:int,name:str):
# #     users.insert(indexValue,name)
# #     return {"replace this person in index 2":name}


# # @app.delete("/deleteAll")
# # def deteteAll():
# #     users.clear()
# #     return {"clear full list now its clear for user"}