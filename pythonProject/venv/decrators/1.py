def shuffle (func):
    def wrapper(no1,no2):
        if no1<no2:
            (no1,no2)=(no2,no1)
        return func(no1,no2)
    return wrapper
@shuffle
def div(num1,num2):
    return num1/num2
@shuffle
def sub(no1,no2):
    return no1-no2
print(div(2,10))
print(sub(8,10))