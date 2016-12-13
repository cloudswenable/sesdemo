import caffe

prefix = "/home/jimmy/deploy/"
model_def = prefix + "deploy.prototxt"
weights = prefix + "SSDH256_iter_50000.caffemodel"

image_dims = [227,227]
input_scale = None
raw_scale = 255.0
channel_swap = [2,1,0]
classifier = caffe.Classifier(model_file=model_def,
                              pretrained_file=weights,
                              image_dims=image_dims,
                              input_scale=input_scale,
                              raw_scale=raw_scale,
                              channel_swap=channel_swap)

def to_binary(inputs):
    t_str=''
    total = len(inputs)
    i = 0
    while i < total:
        if inputs[i] <= 0.5:
            t_str = t_str + '0'
        else:
            t_str = t_str + '1'
        i = i + 1
    print t_str
    return  t_str


def to_binary_int64s(predict):
    b_str = to_binary(predict)
    n_64 = len(b_str) / 64
    bcode_int64 = []
    for i in range (n_64):
        t_str = b_str[i*64:(i+1)*64]
        print t_str
        c_64 = int(t_str,2)
        print c_64
        bcode_int64.append(c_64)

    print bcode_int64
    return bcode_int64
