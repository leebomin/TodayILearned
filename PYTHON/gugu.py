# goo = 0
#
# for i in range(2, 10):
#     for x in range(1, 10):
#         goo = i*x
#         print('%d * %d = %d'%(i,x,goo))
#         print(i, '*', x, '=', goo)

def gugu(n):
    goo = 0

    for x in range(1, 10):
        goo = n*x
        print('%d * %d = %d' % (n, x, goo))
    return

gugu(1)
gugu(2)