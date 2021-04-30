def count_bits(n):
    c = bin(n)
    d = str(c)
    j=0
    for i in range(len(d)-2):
        j = j + (int(d[2:3+i])%2)
    return j
#made By: @Pdxr
