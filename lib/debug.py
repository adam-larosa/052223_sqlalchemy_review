
import ipdb
from models import session, Fighter

session.query( Fighter ).delete()
session.commit()

new_fighter = Fighter( name = 'Ryu' )
session.add( new_fighter )
session.commit()

ipdb.set_trace()
print( 'Welcome to the Fight Shoppe!' )
print( '\nPress a for all fighter names or x to exit' )


user_input = 'not x'

while user_input != 'x':
    user_input = input( '<3 ' )
    if user_input == 'a':

        for fighter in session.query( Fighter ).all():
            print( f'    {fighter.name}' )
    
    elif user_input != 'x':
        print( f'{user_input} is not a valid option' )

print( 'byebye!')

