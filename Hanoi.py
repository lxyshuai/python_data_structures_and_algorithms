def hanoi_move(n, source, dest, intermediate):
    if n == 0:
        return
    hanoi_move(n - 1, source, intermediate, dest)
    print("Move %s -> %s" % (source, dest))
    hanoi_move(n - 1, intermediate, dest, source)


hanoi_move(3, 'A', 'C', 'B')
