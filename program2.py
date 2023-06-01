
salesData = [["Hamilton", "Priest", 1000.50], ["Toronto", "santan", 2000.60],
["Regina", "jordan", 3000.50], ["Mississauga", "Ify", 11000.50], ["Thunder Bay", "darlo", 4000.50] ]
sales = []
def overall():
    for s in range(len(salesData)):
        s = salesData[s][2]
        sales.append(s)
    return sales

sales = overall()

def average_sales():
    sum_sales = sum(sales)
    len_sales = len(sales)
    average_sales = sum_sales/len_sales
    return average_sales

  
     
  
def highestsales():
    for names in salesData:
        if names[2] == max(sales):
            return names[1]



print('The average sales for all locations is: ' + '$',average_sales() )
print('congratulations, ', highestsales() ,' you are eligible for a bonus!')

