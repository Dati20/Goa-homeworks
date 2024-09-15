

# and ნიშნავს რომ თუ ყველა მონაცემი გვაქვს true მხოლოდ მაშინ იქნება true


#or ნიშნავს თუ ერთი მონაცემი მაინც არის true  გვექნება true





print((True or False) and (True and True))
#true and true -> true
print((True or False) and (False or False))
#true and false -> false
print((False and True) or (True and False))
#false or false ->false
print((False or False) and (True or True))
#false and true ->false
print((True and True) or (False and True))
#true or false ->true
print((False or True) and (True and False))
#true and false ->false
print((False and False) or (False or True))
#false or true -> true
print((True or False) and (False or True))
#true and true -> true
print((False or False) and (True or True))
#false and true ->false
print((True and True) or (False and True))
#true or false ->true
print((False or True) and (True and False))
#true and false ->false
print((False and False) or (False or True))
#false or true ->true
print((True or False) and (False or True))
#true and true -> true
print((True and False) or (True and False))
#false or false ->false
print((True and True) or (True and False))
#true or false -> true
print((True or True) and (False and False))
#true and false -> false

