import os
from binance.client import Client
from dotenv import load_dotenv
from bot.logging_config import setup_logger

load_dotenv()
logger = setup_logger()

class BinanceFuturesClient:
    def __init__(self):
        self.client = Client(
            os.getenv("BINANCE_API_KEY"),
            os.getenv("BINANCE_API_SECRET")
        )
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"
        logger.info("Binance Futures Testnet Client Initialized")

    def place_order(self, **params):
        logger.info(f"Sending Order: {params}")
        response = self.client.futures_create_order(**params)
        logger.info(f"Response: {response}")
        return response
