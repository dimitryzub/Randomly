## Documentation

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



