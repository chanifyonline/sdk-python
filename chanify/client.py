import httpx
import asyncio
from typing import Optional

CHANIFY_API_URL = "https://api.chanify.online/v1/ad"
DEFAULT_DELAY = 1.0
TIMEOUT = 3.0


class Chanify:
    def __init__(self, api_key: str):
        if not api_key or not api_key.startswith("chanify_live_"):
            raise ValueError("Invalid Chanify API key. Expected format: chanify_live_...")
        self._api_key = api_key
        self._client = httpx.AsyncClient(timeout=TIMEOUT)

    async def show_ad(
        self,
        chat_id: int,
        user=None,
        country: Optional[str] = None,
        after_delay: float = DEFAULT_DELAY,
    ) -> bool:
        if after_delay > 0:
            await asyncio.sleep(after_delay)

        meta = {}
        if user is not None:
            lang = getattr(user, "language_code", None)
            if lang:
                meta["languageCode"] = lang
            if getattr(user, "is_premium", False):
                meta["isPremium"] = True
        if country:
            meta["country"] = country

        user_id = getattr(user, "id", chat_id) if user is not None else chat_id

        try:
            response = await self._client.post(CHANIFY_API_URL, json={
                "apiKey":   self._api_key,
                "chatId":   chat_id,
                "userId":   user_id,
                "userMeta": meta,
            })
            data = response.json()
            return bool(data.get("shown", False))
        except Exception:
            return False

    async def close(self):
        await self._client.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        await self.close()
