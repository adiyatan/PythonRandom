name = input('What is your name?\n')
print('Hi, %s.' % name)
print('I will write a love poem for you now.')
#some questions for u
crushname = input(str("what's the name of your crush?"))
print("wow, sounds crush-worthy!")
favthing = input(str("what's your favorite thing?"))
print("ok, that's nice.")
userverb = input(str("input something you do with your crush, e.g. dancing...>"))

#the love-letter writing bit
print("dear " + crushname + ":" )
print("roses are red,")
print("violets are blue,")
print("I like" + favthing)
print("and" + userverb + " with you!")
print("optional(will you go out to the dance with me?)")
print("love, " + name)

usable = input(str("do you like the poem?"))
if usable == "Yes":
  print("ok then. that's good.")
  if usable == "No":
    print("uh oh. lets try again.")
