# Importing Dependencies
from fastapi import FastAPI

from api.org import router as organization_router
from api.dept import router as department_router
from api.user import router as user_router
from api.post import router as post_router

# Create FastAPI instance
app = FastAPI()

# Include Routers
app.include_router(organization_router)
app.include_router(department_router)
app.include_router(user_router)
app.include_router(post_router)

# Run FastAPI Application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("routes:app", host="0.0.0.0", port=8000, reload=True, debug=True)