def hanoi_solver(n):
    A = list(range(n, 0, -1))
    B = []
    C = []
    steps = []

    steps.append(f"{A} {B} {C}")

    def move(disks, source, auxiliary, target):
        if disks == 0:
            return

        move(disks - 1, source, target, auxiliary)



        target.append(source.pop())
        steps.append(f"{A} {B} {C}")

        move(disks - 1, auxiliary, source, target)

    move(n, A, B, C)
    return "\n".join(steps)


print(hanoi_solver(2))