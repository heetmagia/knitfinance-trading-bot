from bot.client import BinanceFuturesClient
from bot.validators import validate_inputs

client = BinanceFuturesClient()

def place_trade(symbol, side, order_type, quantity, price=None):

    validate_inputs(symbol, side, order_type, quantity, price)

    params = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity
    }

    if order_type == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"

    return client.place_order(**params)
