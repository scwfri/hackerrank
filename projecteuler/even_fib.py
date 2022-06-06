def iter_fib(max):
    def it(res, prev, pprev):
        res = prev + pprev
        pprev = prev
        prev = res
        return (res, prev, pprev)
    
    accum, p, pp, l = 1, 1, 1, []
    while accum < max:
        accum, p, pp = it(accum, p, pp)
        l.append(accum)
     
    return l

sum(x for x in iter_fib(4000000) if x % 2 == 0)
