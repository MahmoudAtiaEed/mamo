import random
import re
from random import randint
import names
import pandas as pd
import string


number_of_sales = None
num_of_employees = None
df = pd.DataFrame({"ID":[], "First Name":[], "Last Name":[],"Gender":[]})  #frist table "employee"
df2 = pd.DataFrame({"ID":[],"number of sales":[] ,"price":[],"profit": [], "COG":[] , "product":[]}) # second table "sales"
letters = re.findall(r"\w", string.ascii_uppercase)[0:10] # creating a list of letters for product
print("please waite")
with open(r"dist.male.first","r",encoding="UTF-8") as m:
    male = m.read() #converting to string


def employees(num_of_employees):
    for i in range(
            num_of_employees):  # range(num_of_employees) gives error but without range there is a problems with the number of loops

        i = randint(1234567, 2345678)
        ID = i
        frist_name = names.get_first_name()
        if re.findall(frist_name, male, re.I):  # i couldn't write it as r"first"
            Gender = "male"
        else:
            Gender = "female"

        last_name = names.get_last_name()

        df.loc[len(df.index)] = [ID, frist_name, last_name, Gender]  # insert a row inside the dataframe
    return df
def sales(number_of_sales):
    for n in range(
            number_of_sales):  # sales table #range(num_of_employees) gives error but without range there is a problems with the number of loops
        id = random.choice(df.ID)  # get a random num from a list
        numberofsales = randint(1, 30)
        price = randint(20000, 50000)
        profit = randint(2000, 5000)
        cog = price - profit
        product = random.choice(letters)
        df2.loc[len(df2.index)] = [id, numberofsales, price, profit, cog, product]
    return  df2





