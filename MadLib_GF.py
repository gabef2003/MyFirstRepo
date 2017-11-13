import time 
### MAD LIBS ###
### Source: https://i.pinimg.com/736x/79/70/e6/7970e63a364e7f4d70c7b318b9cc9d6d--mad-libs-game-funny-mad-libs.jpg

print ("Give me an adjective")
adj1 = input()
print ("Give me a noun")
noun1 = input()


print ("give me a plural noun")
pluralnoun = input()


print ("Give me a person in the room ( Female )")
personinroomfemale1 = input()
print ("Give me an adjective")
adj2 = input()
print ("Give me an article of clothing")
articleofclothing1 = input() 

print ("Give me a noun")
noun2 = input()
print ("Give me a City")
city1 = input()

print ("Give me a plural noun")
pluralnoun2 = input()
print ("Give me an adjective")
adj3 = input()
print ("Give me a part of the body")
partofthebody1 = input()
print ("Give me a letter of the alphabet")
letterofthealphabet1 = input()
print ("Give me a celebrity")
celebrity1 = input()
print ("Give me a plural noun")
pluralnoun3 = input()


### Begin Mad Lib ### 
print ("There are many " + adj1 + " ways to choose a/an " + noun1 + " to read.")
print ("First, you could ask for recommendations from your friends and " + pluralnoun)
print ("Just don't ask aunt " + personinroomfemale1 + " - she only reads " + adj2+ " books with" + articleofclothing1 + "-ripping goddeses on the cover."   )
print ("If your friends and family are no help, try checking out the " + noun2 + "Review in The " + city1 + "Times")
print ("If the " + pluralnoun2 + " featured there are too" + adj3 + " for your taste try something a little more low " + partofthebody1 + " like " + letterofthealphabet1 + ": The " + celebrity1)
time.sleep(500)
