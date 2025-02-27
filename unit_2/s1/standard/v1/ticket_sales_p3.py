"""
    Prompt:

    A dictionary ticket_sales is used to map ticket type to number of tickets sold. 

    Return the total number of tickets of all types sold.
"""

def total_sales(ticket_sales: dict):
    total = 0
    for k, v in ticket_sales.items():
        total += v
    return total


ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}
print(total_sales(ticket_sales))