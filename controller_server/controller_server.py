import uvicorn

from Env import Env

if __name__ == "__main__":
    uvicorn.run("app.main:app", host=Env.Host, port=Env.PORT, reload=True)
