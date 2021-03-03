'''myMath'''

mySeq = [ 'a','b','c','d','e' ]

def plus(a,b,c,d,e):
    return int(a+b+c+d+e)

def avg(a,b,c,d,e):
    N = len(mySeq)
    return (plus(a,b,c,d,e)/N)
