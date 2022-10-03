import fastapi
import uvicorn


print("hello fm")
api = fastapi.FastAPI()


@api.get("/")
def endpoint():
    return {"msg": "hello world FM", "list of ports": [8000, 9000, 6789]}


uvicorn.run(api, port=9000)
