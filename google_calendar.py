import datetime
import os
import pytz
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv

# 必要な権限を指定
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

def get_google_calendar():
    """
    Googleカレンダーから直近のスケジュールを取得
    """
    creds = None

    # 認証情報が保存されている場合、それを使う
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    
    # 認証情報が無効の場合は再認証
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        
        # 新たな認証情報を保存
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("calendar", "v3", credentials=creds)
        now = datetime.datetime.utcnow().isoformat() + "Z"
        events_result = service.events().list(
            calendarId="primary", timeMin=now, maxResults=5, singleEvents=True, orderBy="startTime"
        ).execute()
        events = events_result.get("items", [])

        if not events:
            print("次のイベントはありません。")
            return []

        schedule_array = []
        japan_tz = pytz.timezone("Asia/Tokyo")

        # イベントの情報をリスト化
        for index, event in enumerate(events, 1):
            start = str(event["start"].get("dateTime", event["start"].get("date")))
            start_dt = datetime.datetime.fromisoformat(start)
            start_dt_japan = start_dt.astimezone(japan_tz)
            formatted_date = start_dt_japan.strftime("%Y年%m月%d日")
            event_summary = event.get("summary", "何かしらの予定あり")

            schedule_array.append(f"{index}: {formatted_date} {event_summary}")

        return schedule_array

    except HttpError as error:
        print(f"エラーが発生しました: {error}")
        return []
