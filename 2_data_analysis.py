# Task 1: Duplicate Entries Cleanup

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

def new_set(customer_ids):
    my_set = set(customer_ids) 
    return my_set
print(new_set(customer_ids))