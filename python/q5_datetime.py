# Hint:  use Google to find python function

import datetime



####a) 
.



####b)  
date_start = datetime.datetime.strptime('12312013', '%m%d%Y')
date_stop = datetime.datetime.strptime('05282015', '%m%d%Y')

print(date_stop - date_start)

####c)  
date_start = datetime.datetime.strptime('15-Jan-1994', '%d-%b-%Y')
date_stop = datetime.datetime.strptime('14-Jul-2015', '%d-%b-%Y')

print(date_stop - date_start)