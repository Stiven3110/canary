from unittest import result
from fastapi import APIRouter, Response, status
from config.db import conn
from models.tweet import tweets
from schema.tweet import Tweet
from starlette.status import HTTP_204_NO_CONTENT

tweet = APIRouter()

#funciones de app 

@tweet.get("/tweets", response_model=list[Tweet], tags=["tweet"])
def get_tweet():
    return conn.execute(tweet.select()).fetchall()

@tweet.post("/tweets", response_model=Tweet, tags=["tweets"])
def create_tweet(tweet: Tweet):
    new_tweet = {"write": tweet.write}
    result = conn.execute(tweets.insert().values(new_tweet))
    return conn.execute(tweets.select().where(tweets.c.id == result.lastrowid)).first

@tweet.get("/tweets", response_model=Tweet, tags=["tweets"])
def get_tweet(id: str):
    return conn.execute(tweets.select().where(tweets.c.id == id)).first()

