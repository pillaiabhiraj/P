#drawing_book
def drawing_book(n,p):
    if p < n//2 :
        return p//2
    else:
        return ( n//2 - p//2 )

n = int(input(''))
p = int(input('page number'))
print(drawing_book(n,p))