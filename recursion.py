from stack import Stack


def print_num_use_stack(n):
    s = Stack()
    while n > 0:
        s.push(n)
        n -= 1

    while not s.is_empty():
        print s.pop()

print_num_use_stack(10)