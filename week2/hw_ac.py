import re
print sum( [float(num) for num in re.findall('[0-9]+', open('regex_sum_224705.txt').read())] )
