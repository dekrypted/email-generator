import random
import os

os.system('') # Enables ANSI escape sequences on Windows.

address = input(f'\x1b[1;32m{os.getlogin()}@GmailGen$ \x1b[1;34mEnter Email: \x1b[0m')
address = address.split('@')
if len(address) == 1:
    input('\x1b[1;31mError: \x1b[1;33mInvalid Email! Press ENTER to continue.\x1b[0m')
    os._exit(0)

if address[1] != 'gmail.com':
    input('\x1b[1;33mWARNING: \x1b[1;33mThis tool may not work with other email providers.\x1b[0m')

dot = lambda: random.choice(['.', '']) # Chooses to create a dot or not
plus = lambda: '+' + random.choice(['1','2','3','4','5','6','7','8','9']) if random.choice([True, False]) else '' # Chooses to create a plus or not
amount = int(input(f'\x1b[1;32m{os.getlogin()}@GmailGen$ \x1b[1;34mEnter Amount: \x1b[0m'))
try:
    amount = int(amount)
except:
    print('\x1b[1;31mError: \x1b[1;33mInvalid Amount! Press ENTER to continue.\x1b[0m')
    os._exit(0)

if amount > (2**(len(address[0]) - 1))*10:
    input(f'\x1b[1;33mWARNING: \x1b[1;33mAbove maximum number of emails for this address. Lowering to {(2**(len(address[0]) - 1))*10}\x1b[0m')
    amount = (2**(len(address[0]) - 1))*10

print(f'\x1b[1;32m{os.getlogin()}@GmailGen$ \x1b[1;34mGenerating {amount} Emails!\x1b[0m')
generated = []
for i in range(amount):
    while True:
        new = ''.join(f'{char}{dot()}' for char in address[0][:-1])
        new += plus()
        new += '@' + address[1]
        if new not in generated:
            generated.append(new)
            break

with open('emails.txt', 'w') as file:
    file.write('\n'.join(generated))

input(f'\x1b[1;32m{os.getlogin()}@GmailGen$ \x1b[1;34mGenerated {len(generated)} Emails! Press ENTER to exit.\x1b[0m')