print("Hey there, Welcome to the final exam centre")
print("Please enter ur prev exam test:")
attend=float(input(""))
em=attend
if (em<=60):
  print("Unfortunetly you aren't qualified for the examination")
elif (em<=75):
  print("You will be attending class C examination")
elif (em<=80):
  print("You will be attending class B examination")
elif (em<=90):
  print("You will be attending class A examination")
elif (em<=100):
  print("You are a top achiever meaning that you are going to the next grade")
else:
  print("Welcome to a new grade")