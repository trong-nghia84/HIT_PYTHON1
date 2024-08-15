def calculate(operation,*args):
    if operation=='add':
        return sum(args)
    elif operation=='multiply':
        tich=1
        for i in args:
            tich *=i
        return tich
    elif operation == "max":
        return max(args)
    elif operation == "min":
        return min(args)
    else:
        return "Invalid operation"

operation=input("operation:")
print(calculate(operation,1,2,3,4,5,6,7))
