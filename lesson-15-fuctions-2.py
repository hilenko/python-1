
def create_record(name, age, phone):
    '''creater a record'''
    record = {
        'name': name,
        'age': age,
        'phone': phone
    }
    return record


user1 = create_record('vasya', '25', '+789328498394')
user2 = create_record('serpapa', '35', '+9345932849983544')

print(user1)
print(user2)


def awards (medal, *name):
    '''Give medal to name'''
    for person in name:
        print('Товарищь ' + person.title() + ' награждаеться медалью ' + medal)

awards('Za Berlin', 'Vasya', 'Petya')
awards('Za otvagu', 'Petya', 'alex', 'Vol')