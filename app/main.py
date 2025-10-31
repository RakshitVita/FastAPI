from fastapi import FastAPI
from app.routers import auth, admin, hr, user

app = FastAPI(title="HR Recruitment Portal", version="1.0.0")

# Include all routers
app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(hr.router)
app.include_router(user.router)

@app.get("/")
async def root():
    return {"message": "Welcome to HR Recruitment Portal API"}
