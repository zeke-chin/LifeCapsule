from pydantic import BaseModel


class ShortcutChatWithImage(BaseModel):
    query: str
    image_base64: str
