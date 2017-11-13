print("what's your favorite sport?")
sport = input ().title()

if sport == "Skiing":
    print ("That's my favorite too!")
elif sport == "Golf":
    print ("I'm decent, but I'm practing.")
elif sport == "Wrestling":
    print ("I love wrestling")
else:
    print (sport + " sounds fun.")



print("What's your favorite TY show?")
show = input().title()

if show == "The Flash":
    print ("I love the show!")
elif show == "Aressted Devolpment":
    print ("I've made a hige mistake.")
else:
    print ("I haven't watched" + show)



print ("What's your favorite color")
color = input().title()

if color == "Green":
    ("Mine Too!")
elif color == "Blue":
   print ("Thats my second favorite.")


mymovies = ["Anchorman, Anchorman2, Deadpool, Fast and Furious, Space Balls, 21 jump street, 22 jump street, Cars, Any Marvle Movie"]
print(" what is your favorite movie")
movie = input()
if movie in mymovies:
    print ("I love watching" + movie)
