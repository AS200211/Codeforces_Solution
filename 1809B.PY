# for n in[*map(int,open(0))][1:]:r=int(n**.5);print(r-(r*r>=n))
for i in range(int(input())):
    n=int(input())
    c=int(n**(.5))
    print(c-(c*c>=n))
