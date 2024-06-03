#part 1 
from datetime import datetime
current_datetime=datetime.now()
print("Today is: ", current_datetime)
import time
current_time = time.time()
local_time = time.localtime(current_time)
# Extract the hour and minute components
hour = local_time.tm_hour
minute = local_time.tm_min
second= local_time.tm_sec
# Print the extracted components
print(f"Current time:", hour, minute, second)
#part 2
poem_string = 'Tiny little secrets \nGet buried in the dirt, \nAnd if they were dug up, \nSomeone would probably get hurt.'
file= open('poem.txt', 'w')
print('File Name:', file.name)
print('File Open Mode:', file.mode)
with open('poem.txt', 'w') as file:
    file.write(poem_string)
    print('\nFile Now Closed?:', file.closed)
    print('File Now Closed?:', file.closed)
with open('poem.txt', 'r+') as file:
    poem_string=file.read()
    print('\nString:', poem_string)
file.close()