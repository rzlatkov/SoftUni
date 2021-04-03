# Key revolver

from collections import deque

price_of_bullet = int(input())
gun_barrel_size = int(input())
bullets = [int(bul) for bul in input().split()]
initial_bullets_len = len(bullets)
locks = [int(lock) for lock in input().split()]
value_of_int = int(input())

locks = deque(locks)
opened = False
left_in_barrel = gun_barrel_size

while len(bullets) > 0:
    if locks:
        current_bullet = bullets.pop()
        current_lock = locks.popleft()
        if current_bullet <= current_lock:
            print("Bang!")
        else:
            print("Ping!")
            locks.appendleft(current_lock)
        left_in_barrel -= 1
        if left_in_barrel == 0 and len(bullets) > 0:
            print("Reloading!")
            if len(bullets) >= gun_barrel_size:
                left_in_barrel = gun_barrel_size
            elif len(bullets) < gun_barrel_size:
                left_in_barrel = len(bullets)
        if not locks:
            opened = True
            break
    else:
        opened = True
        break

if not opened:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    costs = (initial_bullets_len - len(bullets)) * price_of_bullet
    total_costs = value_of_int - costs
    print(f"{len(bullets)} bullets left. Earned ${total_costs}")
