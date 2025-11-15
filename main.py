from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {'message':'Hello World'} #1st Endpoint

@app.get('/about')
def about():
    return {'message':'So its my first multi-endpoint api request'} #2nd Endpoint

#URL(Localhost or 127.0.0.1:8000)/docs gives autmatic generated documentation of FastAPI.
#Thus No POSTMAN like Software needed for this to be installed.