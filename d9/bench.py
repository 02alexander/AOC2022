from time import perf_counter


def sets():
    s = set()
    for i in range(10000000):
        s.add(i)
    return s

def lists(l):
    for i in range(10000000):
        l[i] = i
    return l

start_time = perf_counter()
s = sets()
end_time = perf_counter()
print(end_time-start_time)

l = [None for _ in range(10000000)]
start_time = perf_counter()
l = lists(l)
end_time = perf_counter()


print(end_time-start_time)
print(len(s))
print(len(l))
