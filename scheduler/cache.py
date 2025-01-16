import time
import google_calendar

CACHE_EXPIRY_TIME = 10 * 60  # 10分

class Cache:
    def __init__(self):
        self.cached_schedule = None
        self.last_fetched_time = None

    def get_cached_schedule(self):
        current_time = time.time()

        # キャッシュが存在していて、キャッシュが有効期限内であればキャッシュを返す
        if self.cached_schedule and (current_time - self.last_fetched_time < CACHE_EXPIRY_TIME):
            return self.cached_schedule

        # キャッシュが無効または期限切れの場合、新たにGoogleカレンダーから取得
        self.cached_schedule = google_calendar.get_google_calendar()
        self.last_fetched_time = current_time
        return self.cached_schedule
