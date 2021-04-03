# Fast Food

# FIFO == append + pop(0)
# LIFO == append + pop(-1)
# append() == put() & pop() == get()
# queue.Queue() == FIFO
# queue.LifoQueue() == LIFO (stack)
# queue.SimpleQueue() == FIFO + task tracking disabled.

total_food = int(input())
orders = input().split()
orders = [int(el) for el in orders]

print(max(orders))

count = len(orders)

while count:
    if total_food - orders[0] >= 0:
        total_food -= orders[0]
        orders.pop(0)
    count -= 1

if not len(orders):
    print("Orders complete")
else:
    print("Orders left: ", end='')
    for order in orders:
        print(f"{order}", end=' ')
