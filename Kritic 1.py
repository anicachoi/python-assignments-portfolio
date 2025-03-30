def func(x):
    if x < 0 or x > 1:
        print("Error")
    else:
        n=0
        my_est = 0
        error_bound = 1000

        while error_bound > 0.0001:
            n=n+1
            # for i in range(0,n):
            #     my_est=my_est+((-1)**i)*(x**(2*i+1))/(2*i+1)
            error_bound = x**(2*n+1)/(2*n+1)

        return (x,n,error_bound)


def main():
    x = float(input("Enter the value of x:"))  # It prompts the user to input some value.
    print(func(x))

main()

