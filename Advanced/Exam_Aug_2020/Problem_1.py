# Taxi express

from collections import deque

customers = [int(c) for c in input().split(', ')]
taxis = [int(t) for t in input().split(', ')]
total_time = 0

customers = deque(customers)

while len(taxis) > 0:
    if customers:
        current_customer = customers.popleft()
        current_taxi = taxis.pop()
        if current_customer <= current_taxi:
            total_time += current_customer
        else:
            customers.appendleft(current_customer)

if len(customers) == 0:
    print(f"All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
elif len(taxis) == 0:
    print(f"Not all customers were driven to their destinations")
    modified = [str(c) for c in customers]
    print(f"Customers left: {', '.join(modified)}")
