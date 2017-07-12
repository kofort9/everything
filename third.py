#define a dictionary

groceries_by_price ={
    'Eggs' : 2.59,
    'Milk' : 3.19,
    'Butter' : 2.69,
    'Yogurt' : 3.19
    }

#print groceries_by_price['Eggs']


for item in groceries_by_price:
    print item + ' $' + str(groceries_by_price[item])
    
    
