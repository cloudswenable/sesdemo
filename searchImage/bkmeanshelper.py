import ctypes

import sesdemo.settings

libbkmeans_path = sesdemo.settings.BKMEANS_PATH


so = ctypes.CDLL(libbkmeans_path + "/libbkmeans.so")

so.bkmLoadData(libbkmeans_path+"/bcode_int64s.txt", 256)
so.bkmLoadModel(libbkmeans_path+"/model")
#so.bkmNearestCenter(0)
#data = ctypes.ARRAY(ctypes.c_int, 50)()
#so.bkmKNN(data,50, 0)

K = 50 #default to find only 50 neighbours


image_list = [i.strip("\n").split(" ") for i in open(libbkmeans_path+"/images.txt")]
image_path = [i[0]  for i in image_list]
image_label = [i[1] for i in image_list]

print len(image_list)
image_path_dict = zip(image_path)
image_label_dict = zip(image_label)

def dump(arrays):
    for i in range(len(arrays)):
        print arrays[i], image_path_dict[arrays[i]] , image_label_dict[arrays[i]]

def findKNN(bcode_int64s):
    resultIDs = ctypes.ARRAY(ctypes.c_int, 50)()
    codearray = ctypes.c_ulonglong * 4
    bcodes = codearray(bcode_int64s[0], bcode_int64s[1], bcode_int64s[2], bcode_int64s[3])
    so.bkmKNeighbors(resultIDs, K, bcodes)
    dump(resultIDs)
    print len(resultIDs)
    return resultIDs