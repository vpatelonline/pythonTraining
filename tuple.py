stock_price=[('APPL',200),('GOGL',500),('TSL',150),('MSFT',600)]

for item in stock_price:
    print(item)

for stock, price in stock_price:
    print(stock)



work_hour = [('Abby',100),('Billy',200),('Cilly',50),('Dolly',300)]
work_hour1 = [(100,'Abby'),(200,'Billy'),(50, 'Cilly'),(300,'Dolly')]

def best_emp(work_hour):
    '''Find best employee'''
    current_max = 0
    best_emp_name = ''

    for emp,hrs in work_hour:
        if hrs>current_max:
            current_max=hrs
            best_emp_name=emp
        else:
            pass

    return(best_emp_name,current_max)

print(best_emp(work_hour))

import operator
#Find worse employee
item = min(work_hour,key=operator.itemgetter(1))
print(item)

#Find best employee
item = max(work_hour,key=operator.itemgetter(1))
print(item)

#Find worse employee
print(min(work_hour1,key=operator.itemgetter(1)))

#Find best employee
print(max(work_hour1,key=operator.itemgetter(1)))





