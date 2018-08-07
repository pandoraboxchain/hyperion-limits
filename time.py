import timeit

from secretsharing import SecretSharer  

data = "baf011876aec65950556a5b3048b4d0e0e57008508270629f0d0e91aac916187561c9e94cb2b118633bd1c8174ac10d1dba342ee31f91fa4f83e398f25581448"

n = 2
m = 3
while m<8000:
    start = timeit.default_timer()
    secret = SecretSharer.split_secret(data, n, m)
    stop = timeit.default_timer()
    print(str(n) + " of " + str(m))
    print(str(stop - start) + " seconds")
    n+=1
    m+=2