
'''
int bkmLoadData(char *datafile, int bits)  // 从feature文件加载数据
int bkmSaveModel(char *modelfile) // 保存训练好的模型文件
int bkmLoadModel(char *modelfile) // 加载训练好的模型文件
int bkmCluster(int k, int iter)   // training,
int bkmNearestCenter(int num)     // 找中心点， num表示对第几个数据找中心点，数据从0开始
void bkmKNN(int *arr, int k, int num) // 针对第num个数据找到k个相近的点，保存到arr里
void bkmKNeighbors(int *arr, int k, uint64_t *bincode)// 同上

'''