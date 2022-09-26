import uvicorn
from fastapi import FastAPI

from api.v1.users import router as users_router

app = FastAPI(
    title='python-web-fall-2022',
    version='0.0.1',
    docs_url='/docs',
    redoc_url='/docs/redoc',
)

app.include_router(users_router)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
    )
