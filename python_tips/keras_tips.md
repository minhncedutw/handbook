
#### --------------------------------------------------
#### return effecient way
```python
return A if condition else B # return A if condition True, else return B
```

#### --------------------------------------------------
#### lambda(matmul example)
```python
def mat_mul(inputs):
    A, B = inputs
    return tf.matmul(A, B)

def mat_mul_out_shape(input_shapes):
    shapeA, shapeB = input_shapes
    print(shapeA, shapeB)
    assert shapeA[2]==shapeB[1]
    return tuple([shapeA[0], shapeA[1], shapeB[2]])

# Using
inputs = Input(shape=(num_points, 3))
transformation1 = T_net(inputs, num_hiddens1=[64, 128, 1024], num_hidden2=[512, 256], num_output_channels=3)
x1 = Lambda(mat_mul, output_shape=mat_mul_out_shape)([inputs, transformation1])
model = Model(inputs=inputs, outputs=x1)
print(model.summary())
```
Source: https://keras.io/layers/core/

#### --------------------------------------------------
#### keras custom layer(matmul example)
```python
class MatMul(keras.layers.Layer):
    """~tf.matmul
    Do tf.matmul 2 tensors
    :param inputs (list of 2 tensors): the path to save model checkpoints
    :return . (tensor): result of 1st tensor matmul with 2nd tensor
    """
    def __init__(self, **kwargs):
        super(MatMul, self).__init__(**kwargs)

    def build(self, input_shape):
        # Used purely for shape validation.
        if not isinstance(input_shape, list):
            raise ValueError('`MatMul` layer should be called '
                             'on a list of inputs')
        if len(input_shape) != 2:
            raise ValueError('The input of `MatMul` layer should be a list containing 2 elements')

        if len(input_shape[0]) != 3 or len(input_shape[1]) != 3:
            raise ValueError('The dimensions of each element of inputs should be 3')

        if input_shape[0][-1] != input_shape[1][1]:
            raise ValueError('The last dimension of inputs[0] should match the dimension 1 of inputs[1]')

    def call(self, inputs):
        A, B = inputs
        if not isinstance(inputs, list):
            raise ValueError('A `MatMul` layer should be called on a list of inputs.')
        return tf.matmul(A, B)

    def compute_output_shape(self, input_shape):
        shape_A, shape_B = input_shape
        output_shape = [shape_A[0], shape_A[1], shape_B[2]]
        return tuple(output_shape)

# Using
inputs = Input(shape=(num_points, 3))
transformation1 = T_net(inputs, num_hiddens1=[64, 128, 1024], num_hidden2=[512, 256], num_output_channels=3)
x1 = MatMul()([inputs, transformation1])
model = Model(inputs=inputs, outputs=x1)
print(model.summary())
```
Source: https://keras.io/layers/writing-your-own-keras-layers/

#### --------------------------------------------------
#### keyboard input dict
```python
# Define
def input_dict() -> Dict:
    user_input = input("Enter key and value separated by commas (;): ")
    input_kwargs = dict(map(lambda l: l.split(), user_input.split(sep=';')))
    return input_kwargs

# Usage
kwargs = input_dict()
if 'verbose' in kwargs:
    voxel_size = bool(kwargs['verbose'])
if 'voxel_size' in kwargs:
    voxel_size = float(kwargs['voxel_size'])
#or
attribute = kwargs.get('attribute', default_value)
#or
verbose = eval(str(verbose or kwargs.get('verbose')))
```

#### keyboard input CLI
```python
def input_cli():
    user_input = input("Enter key and value separated by commas (;): ")
    custom_parser = argparse.ArgumentParser()
    custom_parser.add_argument('-vb', '--verbose', type=bool, help='show detail results')
    custom_parser.add_argument('-vs', '--voxel_size', type=float, help='adjust voxel size')
    custom_parser.add_argument('-ft', '--fitness_threshold', type=float, help='adjust voxel size')
    custom_args = custom_parser.parse_args(user_input.split())
    return custom_args

# Usage
custom_args = input_cli()
if custom_args.verbose: verbose = custom_args.verbose
if custom_args.voxel_size: voxel_size = custom_args.voxel_size
if custom_args.fitness_threshold: fitness_threshold = custom_args.fitness_threshold
```
#### --------------------------------------------------