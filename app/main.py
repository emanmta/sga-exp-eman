from fastapi import FastAPI, status
from app.api.v1.endpoints import tickets as tickets_router
from app.api.v1.routers import auth as auth_router

app = FastAPI(
    title="Guest Assistant AI",
    description="API for Ticketing and FAQ for Guest Assistant",
    version="0.1.0",
)

@app.get(
    "/health",
    tags=["Health Check"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
)
def health_check():
    """
    ## Perform a Health Check
    
    A simple health check endpoint to confirm the API is running.
    
    - **Returns:** `{"status": "OK"}`
    """
    return {"status": "OK"}

app.include_router(
    tickets_router.router,
    prefix="/api/v1/tickets",
    tags=["Tickets"],
)
app.include_router(
    auth_router.router,
    prefix="/api/v1/auth",
    tags=["Authentication"],
)