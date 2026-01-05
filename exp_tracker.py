from func import *

print('Personal Expenses Tracker'.center(50, '*'))

print()

def main():
  initialize_file()
  while True:
    print('1 Add Expense')
    print('2 View Expense')
    print('3 Filter Expense')
    print('4 Delete Expense')
    print('5 Monthly Summary')
    print('6 Exit')
    choice = input('Select any one: ')

    if choice =='1':
      date = input('Select date(yyyy-mm-dd): ')
      amount= input('Enter Amount : ')
      category = input('Enter Category: ')
      description = input("Enter Description: ")
      add_expenses(date, amount,category,description)
      print()
    
    elif choice == '2':
      view_expenses()
      # print()
    
    elif choice == '3':
      filter_by = input('Filter by (date/category:')
      filter_value = input(f"enter{filter_by}: ")
      filter_expenses(filter_by,filter_value)
      print()

    elif choice == '4':
      date = input('Enter date(yyy-mm-dd): ')
      amount = input('Enter amount: ')
      category = input('Enter category: ')
      description = input('Enter description: ')
      delete_expence(date, amount,category,description)
      print()
    elif choice == '5':
      monthly_summary()
    
    elif choice == '6':
      print('Exit from program ')
      break

    else:
      print('Invalid option')

if __name__ =='__main__':
  main()

