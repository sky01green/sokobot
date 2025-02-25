from levels import level

p1 = [[1, 1, 1, 1, 1, 6, 6, 6, 6],
      [1, 0, 0, 0, 1, 1, 1, 1, 1],
      [1, 0, 3, 0, 1, 0, 0, 0, 1],
      [1, 0, 0, 0, 1, 3, 1, 0, 1],
      [1, 1, 1, 3, 0, 0, 0, 0, 1],
      [6, 1, 0, 0, 0, 1, 1, 1, 1],
      [6, 1, 0, 0, 2, 2, 2, 1, 6],
      [6, 1, 1, 1, 1, 1, 1, 1, 6]]

p2 = [[6, 6, 1, 1, 1, 1, 6, 6, 6],
      [6, 6, 1, 0, 0, 1, 6, 6, 6],
      [1, 1, 1, 0, 3, 1, 1, 1, 1],
      [1, 0, 3, 2, 2, 0, 3, 0, 1],
      [1, 0, 0, 2, 5, 0, 0, 0, 1],
      [1, 1, 1, 0, 0, 1, 1, 1, 1],
      [6, 6, 1, 0, 0, 1, 1, 1, 1],
      [6, 6, 1, 1, 1, 1, 6, 6, 6]]

p3 = [[1, 1, 1, 1, 1, 1, 1],
      [1, 0, 0, 2, 0, 1, 1],
      [1, 0, 3, 0, 3, 0, 1],
      [1, 2, 0, 5, 0, 2, 1],
      [1, 0, 3, 0, 3, 0, 1],
      [1, 1, 0, 2, 0, 0, 1]]

p4 = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 0, 3, 2, 3, 2, 3, 0, 1],
      [1, 0, 2, 3, 2, 3, 2, 0, 1],
      [1, 0, 3, 2, 3, 2, 3, 0, 1],
      [1, 0, 2, 3, 2, 3, 2, 0, 1],
      [1, 0, 3, 2, 3, 2, 3, 0, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 1, 1, 1, 1, 1, 1, 1, 1]]

p5 = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 3, 3, 3, 3, 3, 3, 3, 1],
      [1, 2, 2, 2, 1, 2, 2, 2, 1],
      [1, 2, 2, 2, 2, 2, 2, 2, 1],
      [1, 3, 3, 3, 0, 3, 3, 3, 1],
      [1, 0, 0, 0, 0, 0, 0, 0, 1],
      [1, 1, 1, 1, 1, 1, 1, 1, 1]]


l1 = level(p1, (6, 3))
l2 = level(p2, (3, 1))
l3 = level(p3, (5, 5))
l4 = level(p4, (1, 7))
l5 = level(p5, (1, 4))

boxxle2 = [l5, l3]
