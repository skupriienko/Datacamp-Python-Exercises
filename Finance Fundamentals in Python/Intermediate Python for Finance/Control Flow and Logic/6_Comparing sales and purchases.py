# Get number of purchases
num_purchases = len(purchases)
# Get number of sales
num_sales = len(sales)

# Check if more sales than purchases
if num_purchases < num_sales:
    print('buy more')

# Get number of purchases
num_purchases = len(purchases)
# Get number of sales
num_sales = len(sales)

# Check if fewer sales than purchases
if num_sales < num_purchases:
    print('sell more')

# Get number of purchases
num_purchases = len(purchases)
# Get number of sales
num_sales = len(sales)

# Check if both lists are empty
if not (purchases or sales):
    print('No sales or purchases')
