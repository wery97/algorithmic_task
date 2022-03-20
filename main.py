def is_prime_number(x):
    return not(x < 2 or any(x % i == 0 for i in range(2, int(x ** 0.5) + 1)))


def sorting(a, b):
    elements_to_remove = set([x for x in a if is_prime_number(b.count(x))])
    return [x for x in a if x not in elements_to_remove]



A=[2,3,9,2,5,1,3,7,10]

B=[2,1,3,4,3,10,6,6,1,7,10,10,10]

C=[2,9,2,5,7,10]

print(sorting(A, B))