# different Methods For Printing!
#Synatx print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

#Print Multiple Times n python
print("Hello For 3 Times \n"*3)
# same as above
print(3*"Hello For 3 Times diff way \n")
#Let's Say We Have To Use Some Sepration
print('Welcome To','The',sep=' RANCHO ',end=' Classes')
print("\n")

# Writing Your Name With Formating in first method when Parameters are defined We Use f in begining
Name="Rancho Classes"
value=1
print(f"Hii {Name} and and you are {value}")
#Passing A parameter in print statement its self
print("You {} should know the use of {} {} programming and {}"
      .format("programmer", "Open", "Source", "Operating Systems"))

#Concatination in Print
print(Name," Ranho Classes Welcomes You because you are no ",value)
