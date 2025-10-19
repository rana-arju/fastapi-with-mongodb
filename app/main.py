from fastapi import FastAPI, HTTPException,Query
from app.routers import user
from app.routers import extract
from fastapi.middleware.cors import CORSMiddleware
from app.database.database import connect_to_mongo, close_mongo_connection,init_db

app = FastAPI(
    title="AI Analysis API",
    description="API for AI-powered analysis of documents, audio, and text files",
    version="1.0.0"
    )

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)

app.include_router(user.router)
app.include_router(extract.router)

# MongoDB connection management
# Connect to MongoDB on startup and close connection on shutdown
@app.on_event("startup")
async def on_startup():
    await init_db()

@app.on_event("shutdown")
async def on_shutdown():
    await close_mongo_connection()

@app.get("/")
def root():
    return {"message": "Server Runing...."}
