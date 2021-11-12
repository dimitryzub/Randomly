## Documentation

This page is created for additional functionality without feeling overwhelmed on the GitHub page.

Most of the functionality you can read in the [Quickstart](https://dimitryzub.github.io/randomit/#-quickstart) section.

### Get phone number

```python
from randomit.randomizer import PhoneNumbers

PhoneNumbers().randomize()

# +204 352-8092
# +69 596-9094
# +2 295-5912
# +159 720-930

for _ in range(10):
    print(PhoneNumbers().randomize())
    # prints 10 random phone numbers
```

### Get email address

```python
import random
from randomit.randomizer import Emails

for _ in range(5):
    print(Emails().randomize(email_chars=random.randint(6,15)))
    
'''
vaqldoj@outlook.com
hstmbjskbd@gmail.com
wocptlruxnihlvo@zoho.com
foyonafdcyvgzj@hotmail.com
eqdmkmlzpiqkb@gmail.com
'''
```



