import pandas as pd
import random
from datetime import datetime, timedelta

# Sample data for the warehouse management system
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
locations = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1']
statuses = ['Picked', 'Packed', 'Shipped', 'Returned']

# Generate random data for the WMS
def generate_order_data(num_records):
    order_data = []
    
    for i in range(num_records):
        order_id = f"ORD{1000 + i}"
        product = random.choice(products)
        quantity = random.randint(1, 50)
        location = random.choice(locations)
        status = random.choice(statuses)
        timestamp = (datetime.now()+timedelta(seconds=i)).strftime('%Y-%m-%d %H:%M:%S')
        
        order_data.append([order_id, product, quantity, location, status, timestamp])
    
    # Create a DataFrame
    df = pd.DataFrame(order_data, columns=['Order ID', 'Product', 'Quantity', 'Location', 'Status', 'Timestamp'])
    
    return df

# Generate data
warehouse_data = generate_order_data(1000)

# Save data to a CSV file
file_path = 'warehouse_data.csv'
warehouse_data.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")