
#### --------------------------------------------------
#### raise(show error notification)
```python
raise NotImplementedError("error message")

raise Exception('Architecture not supported!')

if len(input_shape) != 2:
    raise ValueError('The input_shape must contains 2 elements')
```

#### --------------------------------------------------
#### assert(show error notification)
Check whether condition is true, if not raise error
```python
assert shape1 == shape2  # else hadamard product isn't possible
```

#### --------------------------------------------------
#### isinstance(check type of variable)
```python
if not isinstance(inputs, list):
    raise ValueError('inputs must be a list')
```

#### --------------------------------------------------
