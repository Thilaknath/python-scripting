fruits = ['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']
newFruit = []

def test():
    for x in fruits:
        if fruits.index(x) % 2 == 0:
            newFruit.append(x)
            print (newFruit)

test()

    


    

