import pandas as pd

Sport = {'USA':'Football',
		 'Brazil': 'Soccer',
		 'England':'Rugby'
	};
A = pd.Series(Sport)
print(A)


total =0;
b = [1,2,None,4,None,5,9,11,3];
for i in b:
	if i is None:
		continue
	if i ==11:
		break
	total += i;
print(total)