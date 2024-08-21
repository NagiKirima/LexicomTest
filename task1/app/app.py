from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from contextlib import asynccontextmanager

from routes import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    ''' app startup '''
    yield
    ''' app shutdown '''


app = FastAPI(title='Lexicom test API', lifespan=lifespan)
app.include_router(router)


# cors midlleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5000, log_level='info')