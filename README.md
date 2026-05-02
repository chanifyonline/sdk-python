# Chanify Python SDK

Official Python SDK for [Chanify](https://chanify.online) — the ad network for Telegram bots, channels, and Mini Apps.

## Installation

```bash
pip install chanify
```

## Quick Start

```python
from chanify import Chanify

chanify = Chanify("chanify_live_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

# After each bot response — add one line:
await chanify.show_ad(chat_id=message.chat.id, user=message.from_user)
```

## Usage with aiogram 3.x

```python
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from chanify import Chanify

router = Router()
chanify = Chanify("chanify_live_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Hello! How can I help?")
    await chanify.show_ad(chat_id=message.chat.id, user=message.from_user)
```

## Full API

```python
await chanify.show_ad(
    chat_id=message.chat.id,
    user=message.from_user,
    country="US",        # optional — if your bot knows the user's country
    after_delay=1.5      # seconds to wait before showing ad, default 1.0
)
```

| Parameter | Type | Required | Description |
|---|---|---|---|
| `chat_id` | int | Yes | Telegram chat ID |
| `user` | object | No | Telegram user object — passes language, Premium status |
| `country` | str | No | ISO 3166-1 alpha-2 country code |
| `after_delay` | float | No | Delay in seconds before the ad is sent (default: 1.0) |

Returns `True` if an ad was shown, `False` otherwise. **Never raises exceptions** — safe to call without try/except.

## Requirements

- Python 3.8+
- httpx >= 0.24.0

## Get your API key

1. Sign up at [chanify.online](https://chanify.online)
2. Go to **Publisher → My Bots → Add Bot**
3. Copy your `chanify_live_` API key from Step 3

## Links

- [Website](https://chanify.online)
- [Documentation](https://chanify.online/docs)
- [npm package](https://npmjs.com/package/chanify)
- [Packagist package](https://packagist.org/packages/chanify/sdk)

## License

MIT
