# Задание 20
#def F(n):
#    if n == 1:
#        return 1
#    return 3*F(n-1)+G(n-1)-n+5

#def G(n):
#    if n == 1:
#        return 1
#    return F(n-1)+3*G(n-1)-3*n

#print(F(14)+G(14))


# задача 29 
#def F (n):
#    global s
#    s += n - 5
#    if n > 1:
#        s+= n + 8
#        F(n-2)
#        F(n-3)
#n = 0
#while True:
#    n +=1
#    s = 0
#    F(n)
#    if s > 3200000: break;
#print(n,s)


# Задание 62
#def F (n):
#    if n <= 15:
#        return 2 * n * n + 4 * n + 3
#    if n > 15 and n % 3 == 0:
#        return F(n-1) + n * n + 3
#    if n > 15 and n % 3 != 0:
#        return F(n-2) + n - 6
#count = 0
#for k in range (1, 1001):
#    p = 0
#    g = F(k)
#    while g > 0:
#        if g % 2 == 0:
#            p = p + 1
#        g = g // 10
#    if p == 0:
#        count += 1
#print(count)



