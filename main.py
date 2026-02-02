from fastapi import FastAPI
from fastapi.params import Body
from model import Post

app = FastAPI()

@app.get("/")
def home():
    return {"message" : "welcome to homepage"}

@app.get("/posts")
def all_posts():
    return {"message" : "All posts"}

@app.post("/post")
def create_post(new_post:Post):
    return {
        "post created" : f"Title : coming soon"
    }
