# Code to generate dictionary summary reports

import json

def generate_sales_report(orders_data):


    report = {}

    # 1. Total products sold
    total_products_sold = sum(order.get("quantity", 0) for order in orders_data)
    report["total_products_sold"] = total_products_sold

    # 2. Most popular product
    product_counts = {}
    for order in orders_data:
        product_name = order.get("product_name")
        quantity = order.get("quantity", 0)
        if product_name:
            product_counts[product_name] = product_counts.get(product_name, 0) + quantity

    if product_counts:
        most_popular_product = max(product_counts, key=product_counts.get)
        report["most_popular_product"] = most_popular_product
        report["most_popular_product_quantity"] = product_counts[most_popular_product]
    else:
        report["most_popular_product"] = "N/A"
        report["most_popular_product_quantity"] = 0

    # 3. Revenue per customer
    revenue_per_customer = {}
    for order in orders_data:
        customer_id = order.get("customer_id")
        total_price = order.get("total_price", 0.0)
        if customer_id is not None:
            revenue_per_customer[customer_id] = revenue_per_customer.get(customer_id, 0.0) + total_price

    # Format revenue to 2 decimal places for display
    report["revenue_per_customer"] = {
        cid: f"{rev:.2f}" for cid, rev in revenue_per_customer.items()
    }

    return report

def save_report_to_json(report, filename="sales_report.json"):


    try:
        with open(filename, 'w') as f:
            json.dump(report, f, indent=4)
        return f"Report successfully saved to {filename}"
    except IOError as e:
        return f"Error saving report to {filename}: {e}"

def print_formatted_report(report):
   
    print("\n--- Sales Report Summary ---")
    print(f"Total Products Sold: {report.get('total_products_sold', 0)}")
    print(f"Most Popular Product: {report.get('most_popular_product', 'N/A')} (Quantity: {report.get('most_popular_product_quantity', 0)})")
    print("\nRevenue Per Customer:")
    for customer_id, revenue in report.get('revenue_per_customer', {}).items():
        print(f"  Customer {customer_id}: ${revenue}")
    print("----------------------------")
