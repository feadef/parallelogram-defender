import os
from fastapi import FastAPI
import uvicorn

# Initialize the lightweight web server
app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "Active", "service": "Online", "my_secret": os.environ.get("MY_SECRET_EV")}

if __name__ == "__main__":
    # Render dynamically assigns a port via the PORT environment variable (defaulting to 10000)
    port = int(os.environ.get("PORT", 10000))
    
    # Bind to 0.0.0.0 so external health checks can reach it
    uvicorn.run(app, host="0.0.0.0", port=port)
