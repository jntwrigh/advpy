import pandas as pd

log = pd.read_csv('../resources/new_access.log', usecols=(0, 3, 5, 6, 7, 9), sep='\s+',
                  names=['addr', 'req_date', 'request', 'status', 'size', 'browser'],
                  error_bad_lines=False)
log.req_date = pd.to_datetime(log.req_date, format='[%d/%b/%Y:%H:%M:%S')

date_based_log = log.set_index('req_date')
print(date_based_log.head())
print(date_based_log.info())

print(date_based_log['2015-12-12'].shape)
print(date_based_log['2015'].shape)
print(date_based_log['2016-01'].shape)
print(date_based_log['2015-12-12 18:00:00':'2015-12-12 18:30:00'])