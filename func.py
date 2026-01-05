import os

# 1 usage

def initialize_file():
  if not os.path.exists('expenses.txt'):
    with open('expenses.txt','w') as file:
      file.write('Date,Amount,Category,Description\n')

def add_expenses(date, amount,category,description):
  with open('expence.txt', 'a') as file:
    file.write(f'{date},{amount},{category},{description}\n')
  print('expenses added')

def view_expenses():
  with open('expenses.txt','r') as file:
    lines = file.readlines()
    print(lines[0])
    for line in lines[1:]:
      print(line)

def filter_expenses(filter_by,filter_values):
  with open('expenses.txt','r') as file:
    lines = file.readlines()
    print(lines[0])
    for line in lines[1:]:
      data = line.split(',')
      if filter_by == 'date' and filter_values == data[0]:
        print(line)
      elif filter_by == 'category' and filter_values == data[2]:
        print(line)
      
def delete_expence(date, amount,category,description):
  lines = []
  with open('expenses.txt','r') as file:
    lines = file.readlines()
  with open('expenses.txt','w') as file:
    for line in lines:
     if line != f'{date},{amount},{category},{description}':
       file.write(line)
  print('expense deleted')


import datetime

def monthly_summary():
  current_month = datetime.datetime.now().strftime('%y-%m')
  total_expense = 0.0
  category_expense = {}

  with open('expenses.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
      date = line.strip().split(',')
      if date[0].startswith(current_month): #yaha error aaya ek startwith likha tha but startswith hona chiye aisa jab error to ye sentence pura white dikh raha tha aise error dekh sakta hu mai aage ke liye
        amount = float(data[1])
        category = data[2]
        total_expense+= amount
        if category in category_expense:
          category_expense[category] += amount
        else:
          category_expense[category] = amount
  print(f'Total expence for {current_month}:{total_expense} ')
  for category,amount in category_expense.items():
    print(f'{category}:{amount}')
  