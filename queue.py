import sys
from collections import deque

queue = deque([])

num = int(sys.stdin.readline().strip())
for i in range(num):
    q = sys.stdin.readline().strip().split()
    if "push" == q[0]:
      queue.append(q[1])
    elif "pop" == q[0]:
      if len(queue) == 0:
          print(-1)
      else:
          print(queue.popleft())
    elif "size" == q[0]:
        print(len(queue))
    elif "empty" == q[0]:
      if len(queue) == 0:
          print(1)
      else:
          print(0)
    elif "front" == q[0]:
      if len(queue) == 0:
          print(-1)
      else:
          print(queue[0])
    elif "back" == q[0]:
      if len(queue) == 0:
          print(-1)
      else:
          print(queue[-1])