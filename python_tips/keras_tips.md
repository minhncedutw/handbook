
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

#### --------------------------------------------------
