import pickle

file = open('test.pkl','wb')
obj_1 = ['test_1', {'ability', 'mobility'}]
obj_2 = ['test_2', {'ability', 'mobility'}]
obj_3 = ['test_3', {'ability', 'mobility'}]

pickle.dump(obj_1, file)
pickle.dump(obj_2, file)
pickle.dump(obj_3, file)

file.close()

file = open('test.pkl', 'rb')
obj_1 = pickle.load(file)
obj_2 = pickle.load(file)
obj_3 = pickle.load(file)
print(obj_1)
print(obj_2)
print(obj_3)
file.close()