name = "gabe"


subjects = ["English", "History","Science","Math"]

print("My name is " + name)

#print (subjects)

for i in subjects:
    print("one of my classes is " + i)


sports = ["Rugby", "wrestling", "skiing", "football"]

for i in sports:
    if i == "Rugby":
        print (i + "is my favorite ")
    else:
        print("One of my favortie sports is " + i)

movies = []

while True:
    print("what is one of your favorite movies? Type end to quit.")
    answer = input()
    if answer == "end":
        break
    else:
        movies.append(answer)


for i in movies:
    if i == "deadpool"
        print (i + " is my favorite) 
    print ("One of your favorite movies is " + i)
