'''from collections import defaultdict            # in same module as namedtuple
letters = ['a', 'x', 'b', 'x', 'f', 'a', 'x']
freq_dict = defaultdict(int)   # int not int(); but int() returns 0 when called
for l in letters:              # iterate through each list value: a letter
    freq_dict[l] += 1           # in dict, exception raised if l not in d, but
print(freq_dict)    '''
import re

#re.match(^('?:(?P<star>\*)?(?:(?P<name>[a-zA-Z_][a-zA-Z_\d]*)))(?:=(?P<value>[+-]?\d{1,}))*$',c=5)

phone = r'^(?:\((\d{3})\))?(\d{3})[-.](\d{4})$'
m = re.search(phone,'(949)824-2704')
s=m.group(0)
print(m)