import uvicorn
from Env import Env

if __name__ == "__main__":
    uvicorn.run("app.main:app", host=Env.HOST, port=Env.PORT, reload=True)
