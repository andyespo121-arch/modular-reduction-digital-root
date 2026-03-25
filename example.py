def digital_root(n):
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n

def F(n):
    dr = digital_root(n)
    return n % dr if dr != 0 else 0

# Test examples
for n in range(1, 41):
    print(f"n={n}, F(n)={F(n)}")
