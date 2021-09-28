#    A program to compute the value of an investment
#    carried 10 years into the future
def principal_calculator():
    principal=int(input("Input the amount of the principal "))
    apr = int(input("Input the annual percentage rate (apr)"))
    for i in range(1,11):
        principal = principal * (1 + apr)
    return principal


print(principal_calculator())