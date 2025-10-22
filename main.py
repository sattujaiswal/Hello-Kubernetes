from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/health")
def health_check():
    """
    Health status endpoint.
    Returns 200 OK with a message if the service is running fine.
    """
    return JSONResponse(content={"status": "healthy", "message": "Service is running fine!"}, status_code=200)

@app.get("/test")
def health_check():
    """
    Health status endpoint.
    Returns 200 OK with a message if the service is running fine.
    """
    return JSONResponse(content={"status": "Cool", "message": "I am loving k8s!"}, status_code=200)    
