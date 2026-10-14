def simple_interest(principle, interest, time):
    return (principle * interest * time) / 100

if __name__ == "__main__":
    p = int(input("Enter principle: "))
    i = float(input("Enter interest rate: "))
    t = int(input("Enter time in months: "))
    
    print("SI: ", simple_interest(p, i, t))
