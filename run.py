import uvicorn
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", default=8080)
    opt = parser.parse_args()

    app_str = "src.server:app"  # 修改为src目录下的server.py
    uvicorn.run(app_str, host=opt.host, port=int(opt.port), reload=True, timeout_keep_alive=60)
