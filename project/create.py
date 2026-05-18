import pickle

acc = {}

with open('database.pkl', 'wb') as f:
    pickle.dump(acc, f)

print("New database file created")