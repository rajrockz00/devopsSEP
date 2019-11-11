from collections import defaultdict

marks=[('phani',89),('shyam',92),('rajkumar',99),('rajkumar',98)]

dict_marks = defaultdict(list)

for key,value in marks:
    dict_marks[key].append(value)

print(list(dict_marks.items()))
