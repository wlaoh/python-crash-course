current_users = ['admin', 'winston', 'ashley', 'eric', 'martin', 'ben']
new_users = ['Winston', 'ashley', 'dianne', 'xia', 'calvin']

for new_user in new_users:
    if new_user.lower() in current_users:
        print('You will need to enter a new username')
    else:
        print('The username is available')