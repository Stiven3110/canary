from fastapi import FastAPI
from routes.user import user

app = FastAPI(
        title="canary_app",
        description="esto es un nuevo proyecto",
        version="0.0.1",
        openapi_tags=[{
            "name": "users",
            "description": "users routes"
        }]
)

app.include_router(user)