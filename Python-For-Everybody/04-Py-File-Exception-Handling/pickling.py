import pickle

d = {
    'Name' : 'Jishnu',
    'Age' : 21,
    'Department' : 'CSE'
}

pickle_file = open("pickle_file.txt", "wb")
pickle.dump(d,pickle_file)

pickle_file = open("pickle_file.txt", "rb")
new = pickle.load(pickle_file)

print(new)
