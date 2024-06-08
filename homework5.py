immutable_var = 12, 'число', 5.5
print(immutable_var)
# immutable_var[1] = 24 # кортеж - это список, который нельзя изменить,так же кортеж занимает меньше памяти чем список

mutable_list = ["red", "green", "black"]
print(mutable_list)
mutable_list[2] = "yellow"
print(mutable_list)
mutable_list[0] = 234 
print(mutable_list)