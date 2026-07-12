import pandas as pd
import matplotlib.pyplot as plt
 

data=pd.read_csv("train.csv")

print(data.isnull().sum())
print(data.describe())

def check_survival(x):
    if x == 1:
        return 1
    else:
        return 0
    
    # Extract the column and save it as a variable
survival_column = data['Survived']



data['Survived'] = data['Survived'].apply(check_survival)


# Convert the column to integers just to be 100% sure there are no decimals
data['Survived'] = data['Survived'].astype(int)

# Fill missing age values with the median age
median_age = data['Age'].median()
data['Age'] = data['Age'].fillna(median_age)

# Round all decimal ages to the closest whole number and convert to integers
data['Age'] = data['Age'].round().astype(int)

print(data['Parch'].value_counts())
# fill missing values or values greater than 6 with mode of the column(the most common in entire Column)
data['Parch']=data['Parch'].fillna(data['Parch'].mode()[0])
data['Parch'] = data['Parch'].astype(int)

data['SibSp'] = data['SibSp'].fillna(data['SibSp'].mode()[0])
data['SibSp'] = data['SibSp'].astype(int)
# combining both columns to create a new column so that we can see the survival rate with respect to family size.
data['Family']=data['Parch']+data['SibSp']

data['Family'] = data['Family'].astype(int)

#dropping the cabin column as it has too many missing values and is not useful for our analysis (Around 70 percent data missing )

data.drop(columns=['Cabin'], inplace=True)

# checking the columns after dropping the cabin column
print(data.columns)

# Embarked shows taht the passengers boarded the ship from three different ports. We will fill the missing values with the mode of the column.
data['Embarked'] = data['Embarked'].fillna(data['Embarked'].mode()[0])

# the Pclass column shows the class of the passengers. We will check the value counts of the column to see how many passengers are in each class.
print(data['Pclass'].value_counts())

# Check who survived based on their class
print(data.groupby('Pclass')['Survived'].mean())



# Excel representation to see the cleaned data in a tabular format for better understanding and analysis.
data.to_excel('titanic_cleaned_data.xlsx', index=False)



# =====================================================================
#  SEPARATE VISUALIZATION SYSTEM
# =====================================================================
class_data = data.groupby('Pclass')['Survived'].value_counts().unstack()
class_data.columns = ['Perished', 'Survived']

family_data = data.groupby('Family')['Survived'].mean() * 100

port_data = data.groupby('Embarked')['Survived'].value_counts().unstack()
port_data.columns = ['Perished', 'Survived']


# --- GRAPH 1: THE CLASS DIVIDE ---
plt.figure(figsize=(6, 5))  
class_data.plot(kind='bar', stacked=True, color=["#0e0d0d", "#f5f395"], edgecolor='black')
plt.title('1. The Class Divide', fontsize=12, fontweight='bold', pad=12)
plt.xlabel('Ticket Class')
plt.ylabel('Number of Passengers')
plt.xticks([0, 1, 2], ['1st Class', '2nd Class', '3rd Class'], rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('class_discrimination.png', dpi=300)  


# --- GRAPH 2: THE FAMILY TRAP ---
plt.figure(figsize=(6, 5))  # Creates a fresh, dedicated window
plt.plot(family_data.index, family_data.values, marker='o', linewidth=3, color="#87f3dc", markersize=8)
plt.title('2. The Family Trap', fontsize=12, fontweight='bold', pad=12)
plt.xlabel('Number of Family Members Aboard')
plt.ylabel('Chance of Survival (%)')
plt.ylim(-5, 105)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('family.png', dpi=300)  


# --- GRAPH 3: THE PORT CONNECTION ---
plt.figure(figsize=(6, 5))  # Creates a fresh, dedicated window
port_data.plot(kind='bar', color=["#aeb5f3", "#46e260"], edgecolor='black')
plt.title('3. The Port Connection', fontsize=12, fontweight='bold', pad=12)
plt.xlabel('Boarding Port Location')
plt.ylabel('Number of Passengers')
plt.xticks([0, 1, 2], ['Cherbourg (Rich)', 'Queenstown', 'Southampton (Poor)'], rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('port_dependence.png', dpi=300)  


