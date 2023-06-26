import pickle
some_data = ["a list", "containing", 5,
             "values including another list",
             ["inner", "list"]]

with open("pickled_list", 'wb') as file:
    pickle.dump(some_data, file)

with open("pickled_list", 'rb') as file:
    loaded_data = pickle.load(file)

print(help(pickle))
print(some_data)
print(loaded_data)
print(loaded_data == some_data)
assert loaded_data == some_data
