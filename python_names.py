#part 1
list_of_names= ['Kurt', 'David', 'Katherine']
for name in list_of_names:
    print("Where is" +" "+ name +" "+ "today?")

#part 2
my_favorite_cars= ["Escape", "Santa Fe", "Caravan"]
my_favorite_flowers= ["daisies", "lilacs", "tiger lillies", "peoney"]
my_favorite_animals=["dog", "cat", "horse", "rabbit", "parrot"]

my_favorite_things=my_favorite_cars + my_favorite_flowers + my_favorite_animals

for item in my_favorite_things:
    if len(item) %2==0:
        print(item)

#part 3
number_range=list(range(1,21))

for number in number_range:
    if number %3 == 0 and number %5 ==0:
        print("ZipZap")
    elif number %3 == 0:
        print("Zip")
    elif number %5 == 0:
        print("Zap")
    else:
        print(number)