from googlefinance import getQuotes

import json

print 'enter quote(eg MSFT) for getting stock details'
a=raw_input()
print json.dumps(getQuotes(a), indent=2)
