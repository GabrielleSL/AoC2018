def run():
    part1()
    part2()

def part1():
    f = open("in.txt", "r")
    n = 0
    for x in f:
        if x[0] == "+":
            n+=int(x[1:-1])
        elif x[0] == "-":
            n-=int(x[1:-1])
    print("PART 1: "+str(n))

def part2():
    f = open("in.txt", "r")
    n = 0
    t = 0
    a = [2]
    while True:
        f = open("in.txt", "r")
        for x in f:
            if x[0] == "+":
                n+=int(x[1:-1])
            elif x[0] == "-":
                n-=int(x[1:-1])
            if n in a:
                t=1
                break
            else:
                a.append(n)
    print("PART 2: "+str(n))

run()
