from fastapi import APIRouter
from src import schemas
from src.openai_client import OpenAIClient, create_image_message
import base64

router_shortcuts = APIRouter(
    prefix="/shortcuts",
    tags=["shortcuts-快捷指令"],
)


@router_shortcuts.post("/chat_with_image")
async def create_shortcut(shortcut: schemas.ShortcutChatWithImage):
    client = OpenAIClient()
    # TODO: 异步保存到数据库
    image_url = f"data:image/png;base64,{shortcut.image_base64}"

    msg = create_image_message("user", shortcut.query, [image_url])

    # 保存图片 /Users/zeke/work/workspace/py_work/LifeCapsule/run.py
    with open("/Users/zeke/work/workspace/py_work/LifeCapsule/run.png", "wb") as f:
        f.write(base64.b64decode(shortcut.image_base64))

    response = await client.chat_with_image(messages=[msg])
    resp = response["choices"][0]["message"]["content"]
    print(resp)
    return {"data": resp}
