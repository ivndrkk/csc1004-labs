def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
    dx = x1 - x2
    dy = y1 - y2
    distance = (dx ** 2 + dy ** 2) ** 0.5
    return distance < (r1 + r2)