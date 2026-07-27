from fastapi import FastAPI

app = FastAPI(
    title="DevOps Demo App",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to the DevOps Demo App!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/version")
def version():
    return {
        "version": "1.0.0"
    }
