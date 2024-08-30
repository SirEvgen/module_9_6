import itertools


def all_variants(text):
    for i in range(len(text) + 1):
        for j in itertools.combinations(text, i):
            yield "".join(j)


a = all_variants("abc")
for i in a:
    print(i)
