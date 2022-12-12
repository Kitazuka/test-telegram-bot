import requests
import random
from bs4 import BeautifulSoup

AVAILABLE_TIMEFRAMES = ["5m", "15m", "1h", "4h", "1d", "1w", "1M"]
URL = "https://paper-trader.frwd.one/"
PAIR = "BTCUSDT"


def get_image_url():
    timeframe = AVAILABLE_TIMEFRAMES[
        random.randint(0, len(AVAILABLE_TIMEFRAMES) - 1)
    ]
    candles = str(random.randint(1, 999))
    ma_periods = str(random.randint(1, 100))
    take_profit = str(random.randint(1, 100))
    stop_loss = str(random.randint(1, 100))

    data = {
        "pair": PAIR,
        "timeframe": timeframe,
        "candles": candles,
        "ma": ma_periods,
        "tp": take_profit,
        "sl": stop_loss,
    }

    response = requests.post(
        url=URL,
        data=data,
    )
    soup = BeautifulSoup(response.text, "html.parser")

    image = soup.find("img")

    return URL + image.get("src")
