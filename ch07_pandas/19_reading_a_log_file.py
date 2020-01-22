import pandas as pd

data = pd.read_csv('../resources/access_.log', sep=r'\s+',
                   error_bad_lines=False, usecols=(0,3, 5, 6, 7),
                   names=['addr', 'req_date', 'request', 'status', 'size'])

data.req_date = pd.to_datetime(data.req_date.str.strip('['),
                               format='%d/%b/%Y:%H:%M:%S')
print(data.shape)
print(data)

#----------------------------------------------------------

specific_group = data.groupby('addr').get_group('hp-15.cae.wisc.edu')
print(specific_group[['addr', 'req_date', 'status']])
