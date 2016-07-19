###Stage2 - FUNCTIONS

#Functions follow below format

def func(arg1, arg2):
  do something
  return something
  print something

It takes time and practice to really understand:

  what a function is
  how to make a function
  how to use a function
  when you should write a function
  why functions are so valuable.


#functions can sometimes have an extra input e.g.
text_to_search.find("text_to_find")
#in this case, we are looking for arg1 and arg2 in string input1
## Generally this applies to built in functions, not ones you create yourself


### EXAMPLE of variables being defined within a function
# Video: SUM procedure https://classroom.udacity.com/nanodegrees/nd000/parts/0001345403/modules/356813882475460/lessons/4141089439/concepts/487193330923
# Useful example of a function of the same name as an input variable, that when defined within the function, it creates anew version of
# named input variable after executing, but only temporarily. Once function completed and you go back to Python CL, the original input variable reverts
def sum(a,b):
    a = a + b
#essentially the above code does nothing as there is no return or print statement in the function, so it has no value
