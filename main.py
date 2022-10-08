import pandas as pd


data = pd.read_csv('files/titanic.csv', index_col='PassengerId')

x = data['Pclass'].value_counts()  # group by Pclass (parameters), just 3 class was found
# print(x)

sex_quantity = data['Sex'].value_counts()
print(str(sex_quantity[0]) + " " + str(sex_quantity[1]))  # 1 - men , 2 - women


# all = data['Survived'].count()  # all survived or not passengers
survived = data['Survived'].value_counts('1')
print(round((survived[1]*100), 2))  # rounding to 0.01


first_class_share = data['Pclass'].value_counts('1')
print(round((first_class_share[1]*100), 2))  # rounding to 0.01
# print(data)

average_age = data['Age'].mean()
median_age = data['Age'].median()
print(str(round(average_age, 2)) + " " + str(median_age))


corr = (round(data['SibSp'].corr(data['Parch']), 2))
print(str(corr) + " ,low positive correlation")

# name = (data['Name'][26])
# print(name.split())
# print(name.split(" "))


print(data.index)

names = []
count = 0
for x in data.index:
  if data.loc[x, "Sex"] == "female":
    name = (data['Name'][x])
    count = count + 1
    #print(name.split())
    names.extend(name.split())

print("the count is " + (str(count)))

data_new = pd.array(names)

print(data_new.value_counts(" "))





