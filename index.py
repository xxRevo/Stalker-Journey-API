from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from endpoints.character_endpoint import router as character_router

app = FastAPI()
app.include(character_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health", response_class=str)
def health():
    return "OK"