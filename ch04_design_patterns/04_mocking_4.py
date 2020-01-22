import unittest
from unittest.mock import MagicMock

m = MagicMock()
m.foo.return_value = 'hello'
print(m.foo())

m.alpha = 10
print(m.beta)
m.gamma = 30
print(vars(m))
