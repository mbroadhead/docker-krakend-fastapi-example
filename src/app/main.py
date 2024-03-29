from fastapi import FastAPI

app = FastAPI()

@app.get("/guest")
def guest_hello():
    return {"message": "Hello guest"}

@app.get("/member")
def member_hello():
    return {"message": "Hello member"}

@app.get("/admin")
def admin_hello():
    return {"message": "Hello admin"}
