from fastapi import FastAPI
from routes.user import user
from routes.tweet import tweet

app = FastAPI(
        title="canary_app",
        description="esto es un nuevo proyecto",
        version="0.0.1",
        openapi_tags=[{
            "name": "users_tweets",
            "description": "routes"
        }]
)

app.include_router(user)
app.include_router(tweet)