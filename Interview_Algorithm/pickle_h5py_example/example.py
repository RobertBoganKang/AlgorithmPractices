import h5py
import numpy as np
import pickle

data = np.array([222, 333, 444])
label = np.array([0, 1, 0])
img_num = np.array([0, 1, 2])

dct = {'train_set_x': data, 'train_set_y': label, 'train_set_num': img_num}

# create h5py
with h5py.File('TrainSet_rotate.h5', 'w') as file:
    # write
    file.create_dataset('train_set_x', data=data)
    file.create_dataset('train_set_y', data=label)
    file.create_dataset('train_set_num', data=img_num)

# load h5py
with h5py.File('TrainSet_rotate.h5', 'r') as file:
    print(file['train_set_x'].shape)
    print(file['train_set_x'].value)
    print(file['train_set_x'].name)
    train_set_data = file['train_set_x'].value
    train_set_y = file['train_set_y'].value
    train_set_img_num = file['train_set_num'].value

# save to pickle
with open('TrainSet_rotate.pickle', 'wb') as file:
    pickle.dump(dct, file)

# load pickle
with open('TrainSet_rotate.pickle', 'rb') as file:
    data = pickle.load(file)
    print(data['train_set_x'])
    print(data['train_set_y'])
    print(data['train_set_num'])
