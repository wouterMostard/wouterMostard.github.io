def compose (*functions):
    def inner(arg):
        for f in functions:
            arg = f(arg)
        return arg
    return inner

lines = read('example_log.txt')
ip_addresses = list(map(lambda x: x.split()[0], lines))
filtered_ips = list(filter(lambda x: int(x.split('.')[0]) <= 20, ip_addresses))

map_ips = partial(
    map,
    lambda x : x.split()[0]
)

filter_ips = partial(
    filter,
    lambda x : int(x.split('.')[0]) <= 20
)

count_ips = partial(
    reduce,
    lambda x, _ : 2 if isinstance(x, str) else x + 1
)

composed = compose(
    map_ips,
    filter_ips,
    count_ips
)

counted = composed(lines)

ratio = count_filtered / count_all