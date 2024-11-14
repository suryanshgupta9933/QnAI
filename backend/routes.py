# Importing Dependencies
from fastapi import FastAPI

from api.org import router as organization_router
from api.dept import router as department_router
from api.user import router as user_router
from api.post import router as post_router
from api.response import router as response_router

# Create FastAPI instance
app = FastAPI()

# Include Routers
app.include_router(organization_router)
app.include_router(department_router, prefix="/organization")
app.include_router(user_router, prefix="/organization")
app.include_router(post_router, prefix="/organization/user")
app.include_router(response_router, prefix="/organization/post")

# Run FastAPI Application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("routes:app", host="0.0.0.0", port=8000, reload=True, debug=True)