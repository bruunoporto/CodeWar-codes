def iq_test(numbers):
    d= numbers.split()
    for i in range(len(d)):
        b = int(d[i])%2
        e = int(d[i-1])%2
        f = int(d[i-2])%2
        if b != e and b!=f :
            return i+1
#made by: Pdxr
