# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print("hi azmat")
flavors=["cinnamon","pumpkin","apple pie"]
print("new flavors:")
print(flavors)
ratings=[4,2.5,3]
print("consummer ratings:")
print(ratings)
passed=[True,False,True]
print("release:")
print(passed)

apple_stocks=[298.18,304.18,289.23]

apple_stocks[0]=310
print("latest value:")
print(apple_stocks[0])

apple_stocks[1]=310
print("highest value:")
print(apple_stocks[1])

print("lowest value:")
print(apple_stocks[2])

print("chiffre de liste")
print(apple_stocks)

user_scores=[12,42,55,100,11,22]
highest= user_scores[0]

for score in user_scores:
    if score > highest:
        highest=score
print(f"highest score:{highest}")

signups=[30,6,20,12]
print(sum(signups))

dataset_1=[1,2,3]
dataset_2=[4,5]
datasets=dataset_1+dataset_2
print(dataset_1+ dataset_2)
print(sum(datasets))

answers=[5,3,4,5,6,5,11,88,77,66,55,]
print(answers.count(5))

seizes=[7340,2117,22300,31700,1679,1014,23000,9910,685]
largest=max(seizes)
print("the largest lake in usa:")
print(largest)

smallest=min(seizes)
print("the smallest lake in usa:")
print(smallest)

difference=largest-smallest
print("difference:")
print(difference)

new_users="Ann Jon Alex"
users_list=new_users.split()
print(users_list)

path= "arazgugu.com/menu/products"
path_list=path.split("/")
print(path_list)

special="today's special is polo"
new_special=special.replace("polo","leghmen")
print(new_special)
print(special)

sign="44-55-77-99"
sign_list=sign.split("-")
print(sign_list)

print("stock manager app:")

stock= 80
items= "webcam"
orders=21

print(f"{stock}{items}in stock")
print(f"{stock-orders}available")

print(type("azmat"))
print(type(True))

size=15.4
print(bool(size))
print(str(size))
print(int(size))

position=5
message="you are number"+str(position)+"in the range"
print(message)

user_1=[1,'sara']
user_2=[2,'andy']
data=dict([user_1,user_2])
print(data)

def karmay ():
    print("yahximu balangza?")
    print("yahxi ozlequ?")

karmay()

def display_half(number):
    half=number/2
    print(half)
display_half(50)

def greet(name):
    print(f"salam {name}!")

greet("azmatjon")

def age_label(age):
    label="user age:"+age
    return label
print(age_label("22"))

def age_labels(ages):
    labels="客户岁数："+ str(2*ages)
    return labels
print(age_labels(20))

def half_twice(numéro):
    half=numéro/2
    half_again=half/2
    return half_again
result=half_twice(12)
print(result)

def add_ten(numur):
    hemmisi=10+numur
    return hemmisi
print(add_ten(10))

def show_winners(first,second,third):
    print("First place:"+first)
    print("seconde place:"+second)
    print("third place:"+third)

show_winners("kim","Lee","Ava")

def creat_email(name,year):
  return name+year+"@hutmail.com"
email=creat_email("jo","1989")
print(email)

def is_freezing(temperature):
    return temperature<0
freezing=is_freezing(-3)
print(f"is freezing: {freezing}")

def get_free_seats(booked,total):
    return total-booked
free=get_free_seats(13,20)
print(f"{free} free seats left")

def is_renting_age(age):
  print(age>=25)
is_renting_age(25)

def add_shipping(cart):
    if cart < 100:
        print(f"Total:{cart+10}")
    else:
        print(f"total:{cart}")

add_shipping(45)
add_shipping(200)

def calculate(operator,x,y):
    if operator=="+":
        print(x+y)
    elif operator=="-":
        print(x-y)
    else:
        print(f"unknown:{operator}")

calculate("-",30,10)

def show_status(inbox):
    if inbox > 1000:
        print("inbox full")
    print("you have new message!")

show_status(900)

def show_notification(score):
    if score<30:
        print("score too low")
    else:
        print("onto the next level!")

show_notification(40)

def is_multiplayer(players):
    print(len(players)>1)

players=["Amy","Jay"]
is_multiplayer(players)

def display_programme(movies):
    print(f"Airing tonight:{movies}")

movie_list=["Alienss","Moon"]
display_programme(movie_list)

def count_passengers(passengers):
    print(len(passengers))

passengers=["june","sam","lee"]
count_passengers(passengers)

def is_booked(passengers):
    print(len(passengers)>4)
passengers=["june","sam","lee"]
is_booked(passengers)



def get_winner(top_players):
    winner=top_players[0]
    print(f"Game winner:{winner}")
top_players=["jay","meg","cy"]
get_winner(top_players)



