# ======================================================================================================================
# FOR
# QUICK for
a = [1, 2, 3, 4, 5]
a = [value*10 for value in a]
print(a)

digit_indices = [np.where(y_train == i)[0] for i in range(num_classes)]

'''
===================================================================================================
lambda
===================================================================================================
'''
def filterfunc(x):
    return x % 3 == 0
mult3 = filter(filterfunc, [1, 2, 3, 4, 5, 6, 7, 8, 9])

equal to:
mult3 = filter(lambda x: x % 3 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9])

equal to:
mult3 = [x for x in [1, 2, 3, 4, 5, 6, 7, 8, 9] if x % 3 == 0]
# ======================================================================================================================
# lib: RE
# Pattern-String MATCHING
import re
pattern = re.compile('(.+\/)?(\w+)\/([^_]+)_.+wav')
files = ['./data_ntut/train/audio/bed/00176480_nohash_0.wav',
         './data_ntut/trainaudiobed004ae714_nohash_0.wav',
         './data_ntut/trainaudiobed004ae714_nohash_1.wav',
         './data_ntut/train_audio004ae714_nohash_1.wav']
r = [re.match(pattern=pattern, string=file) for file in files]
print(r[0]) # still matched: <_sre.SRE_Match object; span=(0, 49), match='./data_ntut/train/audio/bed/00176480_nohash_0.wav>
print(r[1]) # still matched: <_sre.SRE_Match object; span=(0, 46), match='./data_ntut/train/audiobed004ae714_nohash_0.wav'>
print(r[2]) # not matched: None
print(r[3]) # not matched: None

# REPLACE all sub-strings
files = ['./data_ntut\\train/audio\\bed\\00176480_nohash_0.wav',
         './data_ntut\\train/audio\\bed\\004ae714_nohash_0.wav',
         './data_ntut\\train/audio\\bed\\004ae714_nohash_1.wav']
files = [re.sub(r'\\', r'/', file) for file in files] # Replace \\ into /
print(files)

# ======================================================================================================================
# lib: SYS
# add directory
import sys
sys.path.insert(0, "E:/STUDY/NTUT/2_1_Machine Learning/Homework/hw2/sample/SimpsonRecognition")

# ======================================================================================================================
# OpenCV TRANSFORMATIONS
# https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.html


# (rows, cols, channels)<->(channels, rows, cols)
x = x.transpose(1, 2, 0)

# RGB <-> BGR
img = img[:,:,::-1]
or
rgb = bgr[...,::-1]
or
gbr = rgb[...,[2,0,1]]

#=====================================================================
# split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75, test_size=0.25)

'''
===================================================================================================
Dict
===================================================================================================
'''
seen_labels = {} # Init a dict
    # Add an element to dict
    obj = {}
    obj['name'] = attr.text
    obj['xmin'] = int(round(float(dim.text)))
    ...

    # Check whether an element already in dict
    if obj['name'] in seen_labels:
        seen_labels[obj['name']] += 1 # if already in, increase count
    else:
        seen_labels[obj['name']] = 1 # if not already in, add new element and init count as 1

'''
===================================================================================================
List
===================================================================================================
'''
pairs = []
pairs += [[z1, z2]]

'''
===================================================================================================
Measure time
===================================================================================================
'''
import time
start_time = time.time()
foo()
print("--- %s seconds ---" % (time.time() - start_time))

'''
===================================================================================================
Monitor learning rate
===================================================================================================
'''
class MyCallback(Callback):
    def on_epoch_end(self, epoch, logs=None):
        lr = self.model.optimizer.lr
        decay = self.model.optimizer.decay
        iterations = self.model.optimizer.iterations
        lr_with_decay = lr / (1. + decay * K.cast(iterations, K.dtype(decay)))
        print(K.eval(lr_with_decay))
