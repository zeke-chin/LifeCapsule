from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from src.router.shortcuts import router_shortcuts

app = FastAPI()

app.include_router(router_shortcuts)

# 注册CORS中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/ping")
async def root():
    return "pong!!"


@app.post("/test")
async def test(request: Request):
    data = await request.json()
    print(data)
    return {"message": "success"}
