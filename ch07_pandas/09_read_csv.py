import pandas as pd
contacts = pd.read_csv('contacts.dat', header=None, dtype='str')
contacts.columns = ['name', 'address', 'state', 'zip', 'area_code', 'phone', 'email', 'company', 'position']

print(contacts)
