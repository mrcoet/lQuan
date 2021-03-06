from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from routers import latestPairs
from routers import pairModal
from routers import latestPairsNew

app = FastAPI()

origins = ["http://localhost:3000"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(latestPairs.router_latest_pairs)
app.include_router(pairModal.router_pair_modal)
app.include_router(latestPairsNew.router_latest_pairs_new)
