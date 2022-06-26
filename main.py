from fastapi import FastAPI

from core.configs import settings
from api.v1.api import api_router

app = FastAPI(title='Curso FastAPI - Segurança')
app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run("main:app", host="localhost", port=8000, log_level='info', reload=True)
    
"""
token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjU2NzkyNDc0LCJpYXQiOjE2NTYxODc2NzQsInN1YiI6IjMifQ.fjkrewGSE4PxmiQfC4ZKVVOD62bO4pdv1wGQ5EhFSqo
type: bearer
"""