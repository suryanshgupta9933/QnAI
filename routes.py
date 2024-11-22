# Importing Dependencies
from fastapi import FastAPI

from api.org import router as organization_router
from api.dept import router as department_router
from api.user import router as user_router
from api.question import router as question_router
from api.answer import router as answer_router

from api.search import router as search_router

# Create FastAPI instance
app = FastAPI()

# Include Routers
app.include_router(organization_router)
app.include_router(department_router, prefix="/organization")
app.include_router(user_router, prefix="/organization")
app.include_router(question_router, prefix="/user")
app.include_router(answer_router, prefix="/question")

app.include_router(search_router)

# Health Check
@app.get("/ready")
async def ready():
    return {"status": "Server is up and running!"}