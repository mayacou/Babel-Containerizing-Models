from fastapi import FastAPI
from routes.routes import setup_routes
import uvicorn

app = FastAPI()
setup_routes(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)