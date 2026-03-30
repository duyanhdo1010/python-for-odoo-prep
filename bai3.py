def optimize_customer_transactions(transactions):
    customer_totals = {}

    for data in transactions:
        customer_id = data["customer_id"]
        amount = data["amount"]

        if customer_id in customer_totals:
            customer_totals[customer_id] += amount
        else:
            customer_totals[customer_id] = amount
    
    return customer_totals

input_data = [
    {"id": 1, "customer_id": 101, "amount": 500, "date": "2025-03-01"},
    {"id": 2, "customer_id": 101, "amount": 300, "date": "2025-03-02"},
    {"id": 3, "customer_id": 102, "amount": 1000, "date": "2025-03-01"}
]

result = optimize_customer_transactions(input_data)

for customer_id, total in result.items():
    print(f"Customer {customer_id}: {total}")