import pickle
import csv
association_rules = pickle.load(open('association_rules_15.pkl', 'rb'))
with open('new_Iris.csv') as test_db:
    test_file = list(csv.reader(test_db))
predictions=[]
for i, row in enumerate(test_file[1:]):
    f_vec = row[:4]
    matches = []
    _max = -1
    for key in association_rules:
        for k1 in association_rules[key]:
            n_match = len([1 for x in f_vec if x in k1[0]])
            score = n_match*k1[2]
            if score >= _max:
                if score > _max:
                    matches = []
                _max = score
                matches.append([k1,_max,key])
    if len(matches) > 1:
        pass
    else:
        predictions.append((i, matches[0][2]))

accuracy = 0
total = 0
for index, pred in predictions:
    if pred == test_file[index+1][-1].strip():
        accuracy += 1
    else:
        print("Predicted Class: '" + pred + "'","Actual Class: '" + test_file[index+1][-1].strip() + "'")
    total += 1
accuracy = round(accuracy / total,2)
print("Accuracy: ", accuracy)