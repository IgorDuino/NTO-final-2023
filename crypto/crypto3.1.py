import gmpy2
import requests
from math import ceil, sqrt


def factorized(n): #складывание простых множителей в массив
   ans = []
   d = 2
   nsqr = min(ceil(sqrt(n)) + 1, 9999999)
   while d <= nsqr:
       if n % d == 0:
           ans.append(d)
           n //= d
       else:
           d += 1
   return ans

def get_data():
    url = "http://10.10.12.10:1176/shared_flag"
    r = requests.get(url).json()
    assert r['g'] == 2

    return (r['p'], r['shared_flag']) # (p, shared)

def phi(p):
    # for primes p only!
    return p - 1


def solve(a, b, p):
    #  a = b ^ x mod p
    _factorization = factorized(p - 1)
    qi = [(i, _factorization.count(i)) for i in set(_factorization)]

    phi_p = phi(p)
    res = []
    for (p_i, e) in qi:
        if p_i > 99999:
            continue
        
        con = phi_p // p_i ** e
        b_con = pow(b, con, p)
        for r in range(p_i ** e):
            if pow(a, con, p) == pow(b_con, r, p):
                res.append((r, p_i ** e ))
                break

    print(res)


if __name__ == "__main__":
    for _ in range(50):
        p, s = get_data()
        solve(s, 2, p)
 