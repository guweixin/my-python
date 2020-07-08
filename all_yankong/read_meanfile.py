# using coding: utf-8
import numpy as np
import sys,caffe

# path
MEAN_FILE='/work/01_project/caffe-master/models/ResNet-50/ResNet_mean.binaryproto'

blob = caffe.proto.caffe_pb2.BlobProto()
# 读取二进制文件
bin_mean = open( MEAN_FILE, 'rb' ).read()

blob.ParseFromString(bin_mean)
arr = np.array( caffe.io.blobproto_to_array(blob) )
npy_mean = arr[0]
# np.save( '/work/01_project/caffe-master/models/ResNet-50/means.txt' , npy_mean )
# FILE = '/work/01_project/caffe-master/models/ResNet-50/means.txt.npy'
# mu = np.load(FILE)
mu = npy_mean.mean(1).mean(1)

# 打印出来平均值
print 'mean-subtracted values: ', zip('BGR', mu)