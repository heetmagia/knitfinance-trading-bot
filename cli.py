import argparse
from bot.orders import place_trade

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--qty", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    print("\n--- ORDER REQUEST ---")
    print(vars(args))

    try:
        order = place_trade(
            symbol=args.symbol.upper(),
            side=args.side.upper(),
            order_type=args.type.upper(),
            quantity=args.qty,
            price=args.price
        )

        print("\n--- ORDER RESPONSE ---")
        print(f"Order ID: {order.get('orderId','N/A')}")
        print(f"Status: {order.get('status','N/A')}")
        print(f"Executed Qty: {order.get('executedQty','N/A')}")
        print(f"Avg Price: {order.get('avgPrice','N/A')}")


        print("\n✅ Order placed successfully")

    except Exception as e:
        print("\n❌ Error:", str(e))

if __name__ == "__main__":
    main()
