a=input("ki tu thu 1:")
b=input("ki tu thu 2:")
next_letter_lambda = lambda a, b: a if ord(a) >= ord(b) else b
print(next_letter_lambda(a,b))
