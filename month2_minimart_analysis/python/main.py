# Entry point for the MiniMart data reporting system

from utils import to_float, calculate_discounted_total, convert_currency, check_large_order
from report_generator import generate_report, print_report_summary, save_report_json

def main():
    print("Starting MiniMart Python Analysis tasks...")

    # Simulated raw order data (as if from DB/CSV)
    raw_orders = [
        {"customer_id": 1, "product_name": "Espresso", "price": "3.50", "quantity": 3},
        {"customer_id": 2, "product_name": "Croissant", "price": "2.75", "quantity": 1},
        {"customer_id": 1, "product_name": "Sandwich", "price": "7.00", "quantity": 2},
        {"customer_id": 3, "product_name": "Orange Juice", "price": "4.00", "quantity": 5},
        {"customer_id": 4, "product_name": "Espresso", "price": "3.50", "quantity": 1},
        {"customer_id": 3, "product_name": "Muffin", "price": "3.25", "quantity": 4},
        {"customer_id": 5, "product_name": "Salad", "price": "8.50", "quantity": 1},
        {"customer_id": 1, "product_name": "Espresso", "price": "3.50", "quantity": 10},
        {"customer_id": 2, "product_name": "Invalid Product", "price": "abc", "quantity": 2}
    ]

    processed_orders = []
    exchange_rate_to_eur = 0.92

    for order in raw_orders:
        item_price_usd = to_float(order.get("price"))
        quantity = order.get("quantity", 0)

        if item_price_usd is None: continue # Skip invalid price entries

        total_price_usd, discount_amount_usd = calculate_discounted_total(item_price_usd, quantity)
        total_price_eur = convert_currency(total_price_usd, exchange_rate_to_eur)

        processed_orders.append({
            "customer_id": order.get("customer_id"),
            "product_name": order.get("product_name"),
            "quantity": quantity,
            "total_price": total_price_usd, # Final USD price after discount
            "total_price_eur": total_price_eur,
            "discount_applied_usd": discount_amount_usd
        })

        if check_large_order(total_price_usd):
            print(f"Large Order Flagged: Cust {order['customer_id']} - {order['product_name']} (Total: ${total_price_usd:.2f})")

    sales_report = generate_report(processed_orders)
    print_report_summary(sales_report)
    print(save_report_json(sales_report, "minimart_sales_report.json"))

if __name__ == "__main__":
    main()
