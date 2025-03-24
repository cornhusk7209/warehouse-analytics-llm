import pandas as pd
import random
from datetime import datetime, timedelta

# Sample data for the warehouse management system
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
locations = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1']
statuses = ['Picked', 'Packed', 'Shipped', 'Returned']
priorities = ['High', 'Medium', 'Low']
shipping_methods = ['Ground', 'Air', 'Express', 'Standard']
categories = ['Electronics', 'Clothing', 'Food', 'Accessories']

# Generate random data for the WMS
def generate_order_data(num_records):
    order_data = []
    
    for i in range(num_records):
        order_id = f"ORD{1000 + i}"
        product = random.choice(products)
        quantity = random.randint(1, 50)
        location = random.choice(locations)
        status = random.choice(statuses)
        priority = random.choice(priorities)
        shipping_method = random.choice(shipping_methods)
        category = random.choice(categories)
        # Randomly simulate times
        order_processing_time = random.randint(10, 60)  # Time in minutes
        pick_time = random.randint(5, 15)  # Time in minutes
        packing_time = random.randint(5, 20)  # Time in minutes
        shipping_time = random.randint(1, 5)  # Time in days
        
        # Create a timestamp that increments for each record
        timestamp = (datetime.now() + timedelta(seconds=i)).strftime('%Y-%m-%d %H:%M:%S')
        
        order_data.append([
            order_id, product, quantity, location, status, priority, shipping_method,
            category, order_processing_time, pick_time, packing_time, shipping_time, timestamp
        ])
    
    # Create a DataFrame
    df = pd.DataFrame(order_data, columns=[
        'Order ID', 'Product', 'Quantity', 'Location', 'Status', 'Priority', 'Shipping Method',
        'Category', 'Order Processing Time', 'Pick Time', 'Packing Time', 'Shipping Time', 'Timestamp'
    ])
    
    return df

# Generate data
warehouse_data = generate_order_data(1000)

# Save data to a CSV file
file_path = 'warehouse_data.csv'
warehouse_data.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")