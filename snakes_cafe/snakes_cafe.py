total_order = [
  {
    'item': 'Wings',
    'count': 0
  }, 
  {
    'item': 'Cookies',
    'count': 0
  },
  {
    'item': 'Spring Rolls',
    'count': 0
  },
  {
    'item': 'Salmon',
    'count': 0
  },
  {
    'item': 'Steak',
    'count': 0
  },
  {
    'item': 'Meat Tornado',
    'count': 0
  },
  {
    'item': 'A Literal Garden',
    'count': 0
  },
  {
    'item': 'Ice Cream',
    'count': 0
  },
  {
    'item': 'Cake',
    'count': 0
  },
  {
    'item': 'Pie',
    'count': 0
  },
  {
    'item': 'Coffee',
    'count': 0
  },
  {
    'item': 'Tea',
    'count': 0
  },
  {
    'item': 'Unicorn Tears',
    'count': 0
  }
]

def menu():
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

order = input('> ')

for food in total_order:
  if food['item'] == order:
    food['count'] += 1
    print(total_order)


if __name__ == '__main__':
    menu()