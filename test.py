import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib import gridspec
import cPickle as pickle
from numpy import dot, reshape, random, float64, exp, newaxis, float, asarray, delete, linspace, clip, load, arange, linalg, argmin, array, random, zeros, fill_diagonal, average, amax, amin, sort, sum
import os, os.path
from PIL import Image
from random import shuffle
import sys, time, argparse
from tensorflow.contrib.layers import l2_regularizer
from tensorflow.contrib.layers import batch_norm
import matplotlib.gridspec as gridspec
import sys, time, argparse
import tensorflow as tf
from utilize import normlization, loaddata_face, loaddata_face_batch
import csv
from heapq import nsmallest
# from sklearn import linear_model
import shutil
import scipy.misc
from resizeimage import resizeimage
from face.dcgan import Generator
from tensorflow.examples.tutorials.mnist import input_data





'''
#icd9_groups.pkl: type: list, len: 942, type of each: unicode
#feature_dictionary.pkl: type: dict, len: 942, MIMIC_ICD9['619']: 508
#patient_vectors.pkl: type: dict, len: 46520, len of each: 942, type of each: list

print "we need to print out something"
print "something change"
print "Test begin"
print "Test end"
print bx.shape
matrix1 = tf.constant([[3., 3.]])
a = [1,2]
b = 3
a = array([1,19])
b = array([1,51])
c = array([[1,20],[1,3],[1,50]])
i = [1,2,3]
g = [1,2]
tr = [[1,3], [2,3], [3,3], [2,5]]
tr = array([[1,3], [2,3], [3,3], [2,5]])
tr = array([[1,3,2], [2,3], [3,3], [2,5]])
tr = [[1,3,2], [2,3], [3,3], [2,5]]
array([4,6])
Y = [1,4,7,0,3]
X1 = [[1,2],[3,2],[4,2],[1,6],[12,2]]
X2 = [[8,2],[4,2],[5,2],[5,6],[1,2]]
lis = [1,2,4,5, None]
v = [array([1,1]),array([3,4]),array([1,2,2,4])]
a = array([1,4,7,0,3])
a = [1,4,7,0,3]
in_list = [3, 8, 9, 2, 12, 7]
train = [[2,2.9],[3,3.5],[4,4],[4,2],[3,1],[1,4],[2,2]]
gen = [2.5,2.5]
a = [1, 2]
b = asarray(a)
r = array([[1,3,4,1], [2,3,5,3], [3,3,1,5], [2,5,6,11]])
g = array([[1,3,2,4], [2,3,5,8], [3,3,5,2], [2,5,2,5]])
te = array([[1,3,12,6], [2,3,4,7], [3,3,6,8], [2,5,9,0]])
a = [3, 8, 9, 2, 12, 7]
b = [4, 7, 9, 2, 12, 7]
r = array([[0.8,0.1,0.4,0.1], [0.2,0.3,0.5,0.6], [0.7,0.3,0.1,0.5], [0.9,0.5,0.6,0.11]])
g = array([[0.1,0.3,0.2,0.4], [0.12,0.3,0.51,0.8], [0.23,0.13,0.5,0.2], [0.22,0.5,0.12,0.5]])
te = array([[0.1,0.3,0.12,0.6], [0.2,0.3,0.4,0.7], [0.3,0.3,0.6,0.8], [0.2,0.5,0.9,0.03]])
r = array([[[1,3],[4,1]], [[2,3],[5,3]], [[3,3],[1,5]], [[2,5],[6,11]]])
a = array([[1],[4]])


# a test on Generator in dcgan.py in face folder
g_net = Generator()
z = tf.placeholder(tf.float32, [None, g_net.z_dim], name='z')
z_feed = random.uniform(-1.0, 1.0, [3, g_net.z_dim])
x_ = g_net(z)
with tf.Session() as sess:
    sess.run(tf.initialize_all_variables())
    print g_net.vars
    print sess.run(x_, feed_dict={z:z_feed})

# move (not copy) 1 out of r files from paths to pathd
paths = "/home/decs/2017-DPGAN/data/img_align_celeba/"
pathd = "/home/decs/2017-DPGAN/data/img_align_celeba_5/"
r = 5.0
N = int(round(len([name for name in os.listdir(paths) if os.path.isfile(os.path.join(paths, name))])/r)) # count files in directory and select 1 out of 10 of them, total: "000001.jpg" to "202599.jpg"
M = 6 # the total number of digit to represent a image
print N
for i in range(1,N+1):
    s = '0'*(M-len(str(i)))
    file = paths + s + str(i) + ".jpg"
    # print file
    shutil.move(file, pathd)

# randomly select from numpy array
r = array([[[1,3],[4,1]], [[2,3],[5,3]], [[3,3],[1,5]], [[2,5],[6,11]]])
n = random.choice(len(r), 2)
print type(r[n])

# draw graph in exp1
with open('/home/decs/2017-DPGAN/result/07302017dp15/genefinalfig/x_gene.pickle', 'rb') as fp:
    x_gene = pickle.load(fp)
print array(x_gene).shape
x_gene = array(x_gene)*255
list = [1, 4, 5, 6, 9, 10, 12, 14, 16, 18] # select 10 from 20, make sure all digits from 0 to 9 is included
plt.figure(figsize=(5, 30))
N = 10  # generate images from generator, after finish training
# N = 20  # generate images from generator, after finish training
G = gridspec.GridSpec(N, 1)
for i in range(N):
    g = x_gene[list[i]].reshape((28, 28))
    # g = x_gene[i].reshape((28, 28))
    plt.subplot(G[i, :])
    plt.imshow(g, interpolation='nearest', cmap='gray')
    plt.xticks(())
    plt.yticks(())
plt.tight_layout()
plt.show()

# draw graph in exp1, continue
def find_M(gen, train, M):
    #find M nearest training points of gen in train
    dist = []
    for i in range(len(train)):
        dist.append(linalg.norm(array(gen) - array(train[i])))
    inds = []
    for i in nsmallest(M, dist):
        inds.append(dist.index(i))
    return inds

with open('/home/decs/2017-DPGAN/result/07302017dp15/genefinalfig/x_gene.pickle', 'rb') as fp:
    x_gene = pickle.load(fp)
list = [1, 4, 5, 6, 9, 10, 12, 14, 16, 18]
MNIST_data, MNIST_labels = loaddata('0123456789', 'training', r'./mnist/MNIST')  # # load whole training set of MNIST database
MNIST_data_n = [] # normlized (/255)
for i in range(len(MNIST_data)):
    MNIST_data_n.append(normlization(MNIST_data[i]))
MNIST_data_n = array(MNIST_data_n)
x_training_data = []  # corresponding nearest training points in whole MNIST
x_training_label = []  # corresponding nearest training points' labels

N = 10
M = 3
for i in range(N):
    print i
    x_inds = find_M(x_gene[list[i]], MNIST_data_n, M) # find the nearest training point for each generated data point in whole MNIST
    for j in range(len(x_inds)):
        x_training_data.append(MNIST_data_n[x_inds[j]])
        x_training_label.append(MNIST_labels[x_inds[j]])

with open('/home/decs/2017-DPGAN/result/07302017dp15/genefinalfig/x_training_data.pickle', 'wb') as fp:
    pickle.dump(x_training_data, fp)
with open('/home/decs/2017-DPGAN/result/07302017dp15/genefinalfig/x_training_label.pickle', 'wb') as fp:
    pickle.dump(x_training_label, fp)

plt.figure(figsize=(15, 30))
G = gridspec.GridSpec(N, M)
for i in range(N):
    for j in range(M):
        g = x_training_data[M*i+j].reshape((28, 28))
        plt.subplot(G[i, j])
        plt.imshow(g, interpolation='nearest', cmap='gray')
        plt.xticks(())
        plt.yticks(())
plt.tight_layout()
plt.show()


# draw graph in exp2
name = 'wdis'
with open('/home/decs/2017-DPGAN/result/Test/' + name +'1.pckl', 'rb') as fp:
    name1 = pickle.load(fp)
with open('/home/decs/2017-DPGAN/result/Test/' + name +'2.pckl', 'rb') as fp:
    name2 = pickle.load(fp)
with open('/home/decs/2017-DPGAN/result/Test/' + name +'3.pckl', 'rb') as fp:
    name3 = pickle.load(fp)
with open('/home/decs/2017-DPGAN/result/Test/' + name +'4.pckl', 'rb') as fp:
    name4 = pickle.load(fp)
with open('/home/decs/2017-DPGAN/result/Test/' + name +'5.pckl', 'rb') as fp:
    name5 = pickle.load(fp)
with open('/home/decs/2017-DPGAN/result/Test/' + name +'6.pckl', 'rb') as fp:
    name6 = pickle.load(fp)
with open('/home/decs/2017-DPGAN/result/Test/' + name +'7.pckl', 'rb') as fp:
    name7 = pickle.load(fp)
t = arange(len(name1))
name1p, = plt.plot(t, name1, 'b--')
name2p, = plt.plot(t, name2, 'g--')
name3p, = plt.plot(t, name3, 'r--')
name4p, = plt.plot(t, name4, 'c--')
name5p, = plt.plot(t, name5[:2000], 'm--')
name6p, = plt.plot(t, name6[:2000], 'y-')
name7p, = plt.plot(t, name7[:2000], 'k--')
plt.legend([name1p, name2p, name3p, name4p, name5p, name6p, name7p], ["non-DP", "std=0.01", "std=0.05", "std=1", "std=5", "std=10", "eps=15"], prop={'weight':'bold'})
plt.xlabel('Generator iterations (*10^{2})')
plt.ylabel('Wasserstein Distance')
plt.savefig('exp2.jpg')


# resize rgb image, see "https://pypi.python.org/pypi/python-resize-image"->"resize_cover(image, size, validate=True)"
paths = "/home/decs/2017-DPGAN/data/img_align_celeba_10000_1st/"
pathd = "/home/decs/2017-DPGAN/data/img_align_celeba_10000_1st_r/"
im_name = [name for name in os.listdir(paths) if os.path.isfile(os.path.join(paths, name))]
N = len(im_name)
# N = 3 # for test use
print N
for i in range(N):
    if i % 100 == 0:
        print i
    fd_img = open(paths + im_name[i], 'r')
    img = Image.open(fd_img)
    img = resizeimage.resize_cover(img, [32, 32, 3])
    # print asarray(img.getdata(),dtype=float64).shape
    # print img.size
    img.save(pathd + im_name[i], img.format)
fd_img.close()

my_const = tf.constant([1.0, 2.0], name="my_const")
print tf.get_default_graph().as_graph_def()

W = tf.Variable(tf.truncated_normal([700,10]))
with tf.Session() as ss:
    ss.run(W.initializer)
    print W.eval()

# matrix1 = tf.linspace(10.0,20.0,4,name=None)
matrix1 = tf.range(3, 18, 3, name='range')
init = tf.initialize_all_variables()
with tf.Session() as ss:
    ss.run(init)
    print type(ss.run(matrix1))

matrix1 = tf.constant([[3., 3.],[4., 5.],[6., 7.]])
matrix2 = dpnoise(matrix1, 64)
init = tf.initialize_all_variables()
with tf.Session() as ss:
    ss.run(init)
    print ss.run(matrix1)
    print ss.run(matrix2)

a =tf.constant(2, name="a")
b =tf.constant(3, name="b")
x =tf.add(a, b, name="and")
with tf.Session() as sess:
    writer = tf.train.SummaryWriter("./my_graph", sess.graph)
    print sess.run(x)
writer.close()
# type on terminal: tensorboard --logdir="./my_graph"

input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
output = tf.mul(input1, input2)
with tf.Session() as ss:
    print ss.run([output], feed_dict={input1:[7.0], input2:[2.0]})

sess = tf.InteractiveSession()
x = tf.Variable([1.0,2.0])
a = tf.constant([3.0,3.0])
x.initializer.run()
sub = tf.sub(x,a)
print sub.eval()
sess.close()

inputDim=2
embeddingDim = 2
x_input = tf.ones([2, 1], tf.float32)
tempVec = x_input
W = tf.ones([2, 2], tf.float32)
b = tf.ones([2, 1], tf.float32)
with tf.variable_scope('autoencoder'):
    for i in range(3):
        tempVec = tf.add(tf.matmul(W, tempVec), b)
sess = tf.Session()
print (sess.run(tempVec))

variable = tf.Variable(42, name='foo')
initialize = tf.initialize_all_variables() # this does not mean random initialization, it means initialize variable to 42
assign = variable.assign(13)


a = tf.constant([1.0, 2.0, 3.0, 4.0])
x2_input = tf.Variable(a)
loss = tf.log(x2_input)
sess = tf.Session()
sess.run(tf.initialize_all_variables())
print (sess.run(loss))

x_input = tf.constant([[3., 3.],[4., 5.],[5., 7.]])
inputMean = tf.reshape(tf.tile(tf.reduce_mean(x_input,0), [3]), (3, 2))
tempVec = tf.concat(1, [x_input, inputMean])
sess = tf.Session()
print (sess.run(tempVec))

def get_size(obj, seen=None):
    """Recursively finds size of objects, https://goshippo.com/blog/measure-real-size-any-python-object/"""
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    return size

class A(object):
    def __init__(self):
        self.l = [1,2,3]

    @property
    def vars(self):
        return [1,2,4]


# generate images in 4*2 grid
DIR = '/home/decs/2017-DPGAN/result/07132017Exp1non/test'
im_name = [name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]
s = [] # get the number
image = [] # store the image
for im in im_name:
    s.append(int(im[:-4])) # remove .jpg then transform to integer
s = sorted(s)

fig = plt.figure()
row = 2 # number of rows in the figure
col = len(im_name)/row # number of columns in the figure
gs = gridspec.GridSpec(row, col, width_ratios=[20, 10], height_ratios=[10, 5])
print gs

for i in range(row):
    for j in range(col):
        ax = fig.add_subplot(gs[i])
        ax = fig.add_subplot(gs[i,j])
        ima = mpimg.imread(DIR + '/' + str(s[i*col+j]) + '.jpg')
        ax.set_title(str(s[i*col+j]*100))
        plt.axis('off')
        ax.imshow(ima)
plt.show()

# following code have something wrong, don't use, list here just in case
# reduce the size of image and store in other directory, in GPU
path = "/home/xieliyan/Desktop/img_align_celeba_10000_3rd/"
pathd = "/home/xieliyan/Desktop/img_align_celeba_10000_3rd_r/"
lname = [name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]
N = len(lname)
print N
for i in range(N):
    if i % 100 == 0:
        print i
    jpgfile = Image.open(path + lname[i])
    jpgfile = scipy.misc.imresize(jpgfile, (128, 128, 3))  # remember the channel = 3, see "https://stackoverflow.com/questions/6086621/how-to-reduce-an-image-size-in-image-processing-scipy-numpy-python"
    plt.imshow(jpgfile)
    plt.savefig(pathd + lname[i])
'''