# Creates an array of menu items tracking the names of the meals and how many you have ordered
total_order = [
  {
    'item': 'wings',
    'count': 0
  }, 
  {
    'item': 'cookies',
    'count': 0
  },
  {
    'item': 'spring rolls',
    'count': 0
  },
  {
    'item': 'salmon',
    'count': 0
  },
  {
    'item': 'steak',
    'count': 0
  },
  {
    'item': 'meat tornado',
    'count': 0
  },
  {
    'item': 'a literal garden',
    'count': 0
  },
  {
    'item': 'ice cream',
    'count': 0
  },
  {
    'item': 'cake',
    'count': 0
  },
  {
    'item': 'pie',
    'count': 0
  },
  {
    'item': 'coffee',
    'count': 0
  },
  {
    'item': 'tea',
    'count': 0
  },
  {
    'item': 'unicorn tears',
    'count': 0
  }
]

# The main function, prints a menu of all available meals then awaits input from the user to compare against the menu. Updates user with any orders placed and how many of the particular item ordered.
# Input: None
# Output: None
def menu():
  if first_time == True:
    print(f'''**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************''')  

  for food in total_order:
    if food['item'] == order:
      food['count'] += 1
      if food['count'] > 1:
        plural = 'orders'
        verb = 'has'
      else:
        plural = 'order'
        verb = 'have'
      
      order_item = food['item']
      order_count = food['count']
      print(f'** {order_count} {plural} of {order_item} {verb} been added to your meal **')

# main gate of program
# calls the menu function to display choices to user then provides a prmopt to place an order with. While user is still ordering meals, choices are stored and the prompt is returned.
# When a user selects to "quit" the final order is repeated back to the user and the app exits.
if __name__ == '__main__':
  order = ''
  first_time = True
  menu()
  first_time = False
  order = input('> ')
  order = order.lower()
  while order != 'quit' and order != 'q':
    print(order)
    menu()
    order = input('> ')
    order = order.lower()     

  if order == 'quit' or order == 'q':
    print('To review, your final order is: ')
    for food in total_order:         
      if food['count'] > 0:
        if food['count'] > 1:
          plural = 'orders'
          verb = 'has'
        else:
          plural = 'order'
          verb = 'have'

        print(f"{food['count']} {plural} of {food['item']}")
    print('We\'ll have that out to you shortly and thank you for eating at the Snakes Cafe!')
      