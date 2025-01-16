from fastapi import FastAPI
from pydantic import BaseModel
from scheduler.chat_service import ChatService
from scheduler.cache import Cache
from dotenv import load_dotenv

# .envから環境変数を読み込む
load_dotenv()

app = FastAPI()

# キャッシュを管理するインスタンスを作成
cache = Cache()

# チャットサービスを作成
chat_service = ChatService(cache)

class ChatRequest(BaseModel):
    input: str  # ユーザーからのインプット

@app.post("/chat")
def chat(request: ChatRequest):
    schedule = cache.get_cached_schedule()
    bot_return = chat_service.continual_chat(schedule, request.input)
    return {"message": f"{bot_return}"}
