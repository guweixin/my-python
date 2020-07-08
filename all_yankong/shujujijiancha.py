import os
path="/mnt/sources2/train_data/ssd_wenbenkeymsg/Annotation/"
txt="/mnt/sources2/train_data/ssd_wenbenkeymsg/ImageSets/Main/trainval.txt"
xmls=os.listdir(path)
for xml in xmls:
    x=xml.split('.',1)
    a=str(x[0])
    #print a
    with open(txt, 'r') as f:
    #for line in open("/mnt/sources2/train_data/ssd_wenbenkeymsg/ImageSets/Main/trainval.txt"):
     #   line = line.strip('\n')
        if a in f:
            print "ok"
    #if not os.path.exists(xmlpath):
     #   print line
    