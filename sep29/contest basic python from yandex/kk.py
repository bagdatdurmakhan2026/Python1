from collections import deque
import sys


def solve():
  input_data = sys.stdin.read().split()
  if not input_data:
    return

  n = int(input_data[0])
  a = [int(x) for x in input_data[1 : n + 1]]
  b = [int(x) for x in input_data[n + 1 : 2 * n + 1]]
  c = [int(x) for x in input_data[2 * n + 1 : 3 * n + 1]]

  posA = [0] * (n + 1)
  posB = [0] * (n + 1)
  for i in range(n):
    posA[a[i]] = i + 1
    posB[b[i]] = i + 1

  C = [0] * (n + 1)
  for i in range(1, n + 1):
    C[i] = c[a[i - 1] - 1]

  P_inv = [0] * (n + 1)
  for u in range(1, n + 1):
    song = a[u - 1]
    v = posB[song]
    P_inv[v] = u

  V = n + 1
  adj = [[] for _ in range(V + 1)]

  # Добавление рёбер
  for i in range(1, n):
    adj[i].append((i + 1, 0))

  for u in range(1, n + 1):
    adj[V].append((u, C[u]))
    adj[u].append((V, 0))

  for v in range(1, n):
    u1 = P_inv[v]
    u2 = P_inv[v + 1]
    adj[u2].append((u1, C[u1] - C[u2]))

  # SPFA
  dist = [0] * (V + 1)
  cnt = [0] * (V + 1)
  inqueue = [True] * (V + 1)
  q = deque(range(1, V + 1))

  while q:
    u = q.popleft()
    inqueue[u] = False

    for to, w in adj[u]:
      if dist[u] + w < dist[to]:
        dist[to] = dist[u] + w
        cnt[to] = cnt[u] + 1
        if cnt[to] >= V:
          print("NO")
          return
        if not inqueue[to]:
          q.append(to)
          inqueue[to] = True

  print("YES")


if __name__ == "__main__":
  solve()