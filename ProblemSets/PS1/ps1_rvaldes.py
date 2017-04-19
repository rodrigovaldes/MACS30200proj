import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

NAME_FILE = "data/jan16pub.dat"

col_names = ["age", "sex", "family_income", "marital_status", "spanish_only", "children", "years_college", "work_weekly"]
locations = [(121,123), (128,130), (38,40), (124,126), (26, 28), (634, 636), (825, 827), (398, 400)]
data = pd.read_fwf(NAME_FILE, locations, names=col_names)
data = data.replace(-1, np.nan)

def delete_minus_one(df, name_column):

    df = df[df[name_column] != -1]

    return df

def replace_in_row(df, name_column, old_val, new_val):

    df[name_column] = df[name_column].replace(old_val, new_val)

    return df


def describe_data(df):
    '''
    Auxiliary function to undertand the general characteristics of
    the data

    Imput:
        df = pandas dataframe
    Output:
        None
    '''

    print(" ")
    print("*********************************")
    print("Description of the data")
    print("*********************************")
    print(df.describe())
    print(" ")

    print("*********************************")
    print("General Information")
    print("*********************************")
    print(df.info())
    print(" ")

    print("*********************************")
    print("About Misisng Values")
    print("*********************************")
    print(df.isnull().sum())

    print(" ")
    return "Done"

# Work Weekly to meaningful values
one = np.mean([0,20])
two = np.mean([21,34])
three = np.mean([35,39])
four = np.mean([40])
five = np.mean([41,49])
six = np.mean([50]) # this is 50 or more
seven = None
eight = None
list_replacements = [one, two, three, four, five, six, seven, eight]

for i in range(1,9):
    data = replace_in_row(data, "work_weekly", i, list_replacements[i - 1])

# Years or College, relevant values
one_2 = 0.5
two_2 = 1
three_2 = 2
four_2 = 3
five_2 = 4
list_replacements_2 = [one_2, two_2, three_2, four_2, five_2]


for i in range(1,6):
    data = replace_in_row(data, "years_college", i, list_replacements_2[i - 1])

# Family Income, relevant values
num_1 = 2500 
num_2 = np.mean([5000, 7499])
num_3 = np.mean([7500 , 9999])
num_4 = np.mean([10000 , 12499])
num_5 = np.mean([12500 , 14999])
num_6 = np.mean([15000 , 19999])
num_7 = np.mean([20000 , 24999])
num_8 = np.mean([25000 , 29999])
num_9 = np.mean([30000 , 34999])
num_10 = np.mean([35000 , 39999])
num_11 = np.mean([40000 , 49999])
num_12 = np.mean([50000 , 59999])
num_13 = np.mean([60000 , 74999])
num_14 = np.mean([75000 , 99999])
num_15 = np.mean([100000 , 149999])
num_16 = np.mean([150000])

list_replacements_3 = [num_1, num_2, num_3, num_4, num_5, num_6, num_7,
num_8, num_9, num_10, num_11, num_12, num_13, num_14,
num_15, num_16]

for i in range(1,17):
    data = replace_in_row(data, "family_income", i, list_replacements_3[i - 1])

# Family inbcome by marital status
d_mstatus = data.groupby(["marital_status"]).mean().reset_index()

# Years of college by sex
d_colsex = data.groupby(["sex"]).mean().reset_index()

# Children vs family income
d_children = data.groupby(["children"]).mean().reset_index()

# Create Scatter Plot
y = data["children"]
x = data["age"]
colors = data["family_income"] / 60
# colors = np.concatenate((np.repeat(48, len(data)-20), np.repeat(10, 20))) / 60
# More purple are smaller numbers. More yellow are bigger numbers


# Make the plot

title = "Number of Children, Age, and Income"
x_label = "Age"
y_label = "Number of Children"
name_file = "income_children.png"

plt.title(title)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.text(60, 12, 'High Income', style='italic',
        bbox={'facecolor':'yellow', 'alpha':0.6, 'pad':3})

plt.text(60, 10, ' Low Income', style='italic',
        bbox={'facecolor':'purple', 'alpha':0.6, 'pad':3})
plt.scatter(x, y, alpha=0.2, c=colors)
plt.savefig(name_file, bbox_inches='tight')
plt.show()
plt.close()










