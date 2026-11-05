def rent_cost(days):
    if(days==0){
        return 0
    }else if(days>=1 and days<=5){
        return 500
    }else{
        return 3000
    }

if __name__ == "__main__":
    days = int(input("Enter the number of days you want to rent the vehicle: "))
    cost = rent_cost(days)
    print(f"The total cost for renting the vehicle for {days} days is: {cost}")