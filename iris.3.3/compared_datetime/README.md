```python

import datetime
from iris.time import PartialDateTime
dt = datetime.datetime(2011, 3, 7)
print(dt > PartialDateTime(year=2010, month=6))
True
print(dt > PartialDateTime(month=6))
False
```
