from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import energy
# adjust based on your structure

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(energy.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
