# Vocore2 GPIO Python Library

This is an Arduino inspired library for Vocore2 GPIO pins control.

Made by Bryan Barbosa from [Federal University of Juiz de Fora](https://ufjf.br/) and [CREA - University of California, Berkeley](https://crea.berkeley.edu/).

## Importing

The library can be used simply by importing the Python file to your project.

```python
import vocoreGPIO
```
For an easier and more Arduino-like control, we recommend to import as:
```python
from vocoreGPIO import *
```

## Usage
The usage of the library is simple as a normal Arduino pin control. For example, for a classic blink led:

```python
from vocoreGPIO import *

pinMode(40, 'OUTPUT')

while(1):
    digitalWrite(40, 'HIGH')
    delay(1000)
    digitalWrite(40, 'LOW')
    delay(1000)
```

Note that the only differences between these commands and the commands used in Arduino are the quotation marks for passing the words 'OUTPUT', 'INPUT', 'HIGH' and 'LOW' as parameters.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
