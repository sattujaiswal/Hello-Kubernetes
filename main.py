from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/health")
def health_check():
    return JSONResponse(content={"status": "healthy", "message": "Service is running fine!"}, status_code=200)

@app.get("/test")
def test_check():
    return JSONResponse(content={"status": "Cool", "message": "I am loving k8s!"}, status_code=200)