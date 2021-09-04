# Pyromises 🐍

Promises for Python

### What it does 🤔

Pyromises is a high-level wrapper over threads for Python, it provides an API very similar to Javascript for dealing with asynchronous code.

### Examples 🤓

In Javascript

```javascript
fetch('https://api.github.com/Nxrth-x')
  .then(res => res.json())
  .then(console.log)
```

In Python

```py
import requests
from pyromise import Promise

def fetch_data():
  response = requests.get('https://api.github.com/Nxrth-x')
  return response.json()

Promise(fetch_data).then(print)
```

### Author 🙋‍♂️

- [GitHub](https://github.com/Nxrth-x)
- [Email](mailto:lima.eder101@gmail.com)
