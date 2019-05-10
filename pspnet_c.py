#-*- coding:utf-8 -*-
import sys,os
caffe_root='/home/lizhenxing/caffe_v11'
sys.path.insert(0,os.path.join(caffe_root,'python'))
import cv2
import caffe
import numpy as np
import matplotlib.pyplot as plt
import json
import argparse


size_h=473
size_w=473
model_def='/home/lizhenxing/QtProject/chejian_v5_gitlab/chejian_v5_gitlab_lzx/model/normal/se_chewaiguan.prototxt'
model_weights='/home/lizhenxing/QtProject/chejian_v5_gitlab/chejian_v5_gitlab_lzx/model/normal/se_chewaiguan.caffemodel'
# image_file='/data_2/waiguan_obj_dataset/sum_dataset/sz_waiguan_obj_result/0111_pic'
image_file='/data_1/caffe_segmentation_project/large_vehicle/标注数据/2018.05.16dachefenge/mark'
# image_file='/data_1/caffe_segmentation_project/cemenpentu/train_dataset/1203/test.txt'
# image_file='/data_1/caffe_segmentation_project/cemenpentu/train_dataset/1203/mark/rot_0_0157_E2J972_LGDCW91L7BA113482_check1888.jpg'
##28classes
#B->G->R
color_segmentation=np.asarray([
    [0,0,0],
    [180,120,120],
    [6,230,230],
    [80,50,50],
    [4,200,3],
    [120,120,80],
    [140,140,140],
    [204,5,255],
    [230,230,230],
    [4,250,7],
    [40,150,255],
    [235,255,7],
    [150,5,61],
    [120,120,70],
    [8,255,51],
    [255,6,82],
    [143,255,140],
    [204,255,4],
    [255,51,7],
    [204,70,3],
    [0,102,200],
    [61,230,250],
    [255,6,51],
    [11,102,255],
    [255,7,71],
    [255,9,224],
    [9,7,230],
    [220,220,220]
],dtype=np.uint8)

class Caffe_PSP_Segmentation:
    def __init__(self,gpu_id,model_def,model_weights,size_h,size_w):        
        caffe.set_mode_gpu()
        self.size_w=size_w
        self.size_h=size_h
        self.net=caffe.Net(model_def,model_weights,caffe.TEST)
        self.net.blobs['data'].reshape(1,3,size_h,size_w)                        

        # input preprocessing: 'data' is the name of the input blob == net.inputs[0]
        # self.transformer=caffe.io.Transformer({'data':self.net.blobs['data'].data.shape})
        self.transformer=caffe.io.Transformer({'data':self.net.blobs[self.net.inputs[0]].data.shape})        
        self.transformer.set_transpose('data',(2,0,1))  ##set the input channel order for e.g. RGB to BGR conversion
        
        ##input_blob=input*scale.While Python represents images in [0, 1], certain Caffe models
        # like CaffeNet and AlexNet represent images in [0, 255] so the raw_scale
        # of these models must be 255.
        self.transformer.set_raw_scale('data',255)    

        # Set the mean to subtract for centering the data.  
        self.transformer.set_mean('data',np.array([123.68, 116.779, 103.939]))
        
        # Set the scale of preprocessed inputs s.t. the blob = blob * scale.
        # N.B. input_scale is done AFTER mean subtraction and other preprocessing
        # while raw_scale is done BEFORE.
        self.transformer.set_input_scale('data',0.0078125)
        
        #Set the input channel order for e.g. RGB to BGR conversion
        # as needed for the reference ImageNet model.
        # N.B. this assumes the channels are the first dimension AFTER transpose.
        self.transformer.set_channel_swap('data',(2,1,0))
            

    def prdict(self,imagename,nclasses=28):        
        image=caffe.io.load_image(imagename.strip()) #type:np.float32,size:(HxWx3) or (HxWx1)
        
        ##preprocess:
        #        - convert to single
        #- resize to input dimensions (preserving number of channels)
        #- transpose dimensions to K x H x W
        # - reorder channels (for instance color to BGR)
        # - scale raw input (e.g. from [0, 1] to [0, 255] for ImageNet models)
        # - subtract mean
        # - scale feature
        #data:(HxWxK) ndarray
        #returns:caffe_in:(KxHxW) ndarray for input to a Net
        transformed_image=self.transformer.preprocess('data',image)        

        self.net.blobs['data'].data[...]=transformed_image
        
        ##returns:{blob_name:blob_ndarray} dict
        output=self.net.forward()
        # print self.net.outputs[0]  ##conv9_interp
        output_prob=output[self.net.outputs[0]][0] 
        # print type(output_prob)  ##np.ndarray
        # print output_prob.shape  ##(28,473,473)

        merge_gray = None        
        feature_maps = None
        output_prob=output_prob.transpose((1,2,0))
        merge_gray=np.argmax(output_prob[:,:,...],axis=2)
        merge_gray=merge_gray.astype(np.uint8)
        merge_color=np.zeros((self.size_w,self.size_h,3),dtype=np.uint8)
        #show img
        for i in range(nclasses):
            print (str(i), ': ', color_segmentation[i])            
            merge_color[np.where(merge_gray == i)[0], np.where(merge_gray == i)[1]] = color_segmentation[i]
        return merge_color  

def get_pspnet_model():    
    prediction=Caffe_PSP_Segmentation(0,model_def,model_weights,size_h,size_w)
    return prediction  

def load_images(image_file):
    imgnames=[]
    if os.path.isfile(image_file):
        if image_file.endswith('.txt'):
            with open(image_file,'r') as f:
                imagelists=f.readlines()
            for imgname in imagelists:
                imgname=imgname.strip()
                imgnames.append(imgname)                
        else:
            imgnames.append(image_file)
        
    if os.path.isdir(image_file):
        imgnames=[os.path.join(image_file,image_name) for image_name in os.listdir(image_file)]    

    return imgnames

def parse_args():
    '''parse args'''
    parser = argparse.ArgumentParser()
    parser.add_argument('--gpu_id', type=int, default=0, help='gpu id')
    parser.add_argument('--model_def',default=model_def)    
    parser.add_argument('--model_weights',default=model_weights)
    parser.add_argument('--size_w',default=size_w)
    parser.add_argument('--size_h',default=size_h)    
    parser.add_argument('--image_file',default=image_file)
    return parser.parse_args()

if __name__=='__main__':
    args=parse_args()
    prediction=Caffe_PSP_Segmentation(args.gpu_id,args.model_def,args.model_weights,args.size_h,args.size_w)

    imgnames = load_images(image_file)
    for imgfilename in imgnames:
        print(imgfilename)
        img = cv2.imread(imgfilename)
        colormat = prediction.prdict(imgfilename)
        img = cv2.resize(img, (size_w, size_h))
        cv2.imshow('orgimg', img)
        cv2.imshow('colormat', colormat)
        cv2.waitKey()

    #
    # if os.path.isdir(args.image_file):
    #     for image_name in os.listdir(args.image_file):
    #         image_name=os.path.join(args.image_file,image_name)
    #         colormat=prediction.prdict(image_name)
    #         img=cv2.imread(image_name)
    #         img=cv2.resize(img,(size_w,size_h))
    #         cv2.imshow('orgimg',img)
    #         cv2.imshow('colormat',colormat)
    #         cv2.waitKey()
    # elif image_file.endswith('.txt'):
    #     with open(image_file,'r') as f:
    #         image_names=f.readlines()
    #     for image_name in image_names:
    #         image_name=image_name.split(' ')[0]
    #         img=cv2.imread(image_name)
    #         colormat=prediction.prdict(image_name)
    #         cv2.imshow('orgimg',img)
    #         cv2.imshow("colormat",colormat)
    #         cv2.waitKey()
    # else:
    #     colormat=prediction.prdict(args.image_file)
    #     img=cv2.imread(args.image_file)
    #     cv2.imshow('orgimg',img)
    #     cv2.imshow('colormat',colormat)
    #     cv2.waitKey()
