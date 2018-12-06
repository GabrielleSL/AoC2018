import string

def run():
    part1()
    part2()

def part1():
    f = open("in.txt", "r")
    t2, t3 = 0, 0
    for x in f:
        p2, p3 = 0, 0
        for a in string.ascii_lowercase:
            c = x.count(a, 0, -1)
            if c == 2:
                p2 = 1
            elif c == 3:
                p3 = 1
        t2+=p2
        t3+=p3
    print(f"PART 1: {t2*t3}")

def part2():
    f = open("in.txt", "r")
    z = f.read().split('\n')
    t = ""
    for x in z:
        for y in z:
            c = 0
            s = ""
            u=zip(x, y)
            for i, j in u:
                if i!=j:
                    c+=1
                else:
                    s+=i
            if c==1:
                t = s
                break
    print(f"PART 2: {t}")

run()
