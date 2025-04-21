from uuid import UUID
from fastapi import FastAPI, HTTPException

from models import Gender, Role, User

app = FastAPI()

db :list[User] = [
    User(
        firstName='Temi', 
        lastName= 'Owolabi',
        email='temi@gmail.com',
        gender=Gender.male,
        roles = [Role.admin, Role.user]
    ),
    User(
        firstName='Alex', 
        lastName= 'Johnsns',
        email='Alex@gmail.com',
        gender=Gender.female,
        roles = [Role.admin, Role.user]
    )
]

@app.get('/')
def root():
    return {"message": "Hello Mondo"}

@app.get('/users')
def getUser():
    return db;

@app.post('/user')
def createUser(user: User):
    db.append(user)
    return user

@app.delete('/user/{userId}')
def deleteUser(userId: UUID):
    for user in db:
        if user.id == userId:
            db.remove(user)
            return {"message": "User deleted successfully"}
    # return {"message": "User not found"}
    raise HTTPException(status_code = 404, detail = f'User with id {userId} not found');