from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
import numpy as np
from keras.layers.normalization import BatchNormalization
from keras.layers import Dropout
from keras.models import load_model
# import matplotlib.pyplot as plt
import os
import format_data
from format_data import DataSample

list_key_cols =[67,43,25,19,18,64,60,23,61,55,56,59,70,51,35,66,34,47] #24-OSBuildLab
data = np.genfromtxt('./train.csv', 
    delimiter=',', 
    encoding='utf8', 
    max_rows=50000, 
    dtype=str, 
    #usecols=(8),
    invalid_raise=False,
    missing_values=None,
    skip_header=1
    )


# out = open('out.txt', 'w')
# for i in range(len(data[1])):

#     val_set = set()
#     count = 0
#     map_string = 'mappings = {'
#     for j in range(len(data)):
#         val = data[j][i]
#         if(val not in val_set):
#             val_set.add(val)
#             map_string+= '\'' + val + '\':' + str(count) + ', '
#             count+=1
#     map_string+= '}'
#     if('MachineIdentifier' not in map_string):
#         out.write(map_string)
#         out.write('\n')
# out.close()

# for i in range(len(data)):
#     for j in range(len(data[0])):
#         if(data[i][j] == ''):
#             if(j not in list_key_cols):
#                 data[i][j] = -1

# for val in data:
#     print(val)

# count = 0
# for val in data[0]:
#     print('self.' + str(val) + ' = self.data_row[' + str(count) +']')
#     count+=1

# for i in range(len(data[0])):
#     print(str(data[0][i]) + ': ' + str(data[1][i]) + '   ' + str(data[2][i]))

#first create data objects
all_data_objects = []
for row in data:
    data_object = DataSample(row)
    all_data_objects.append(data_object)

#next turn the data into feature vectors
all_data_feature_vecs, all_labels = format_data.clean_data(all_data_objects)


train_x = all_data_feature_vecs[:45500]
train_y = all_labels[:45500]

test_x = all_data_feature_vecs[-500:]
test_y = all_labels[-500:]

model = Sequential()

model = Sequential()
model.add(Dense(34, input_dim=96, activation='relu'))
model.add(BatchNormalization())
model.add(Dense(12, input_dim=34, activation='relu'))
model.add(BatchNormalization())
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])
hist = model.fit(np.array(train_x), np.array(train_y), epochs=1000, #batch_size=500,
                 validation_data=(np.array(test_x), np.array(test_y)), verbose=2)

for key, item in hist.history.items():
    print('Key: ' + str(key) + ', Value: ' + str(max(item)))


# plt.plot(hist.history["acc"], label='acc')
# plt.plot(hist.history["val_acc"], label='val_acc')
# plt.legend()
# plt.savefig('performance')
# plt.show()


# for i in range(len(data[1])):

#     val_set = set()
#     count = 0
#     map_string = 'mappings = {'
#     for j in range(len(data)):
#         val = data[j][i]
#         if(val not in val_set):
#             val_set.add(val)
#             map_string+= '\'' + val + '\':' + str(count) + ', '
#             count+=1
#     map_string+= '}'
#     print(map_string)



# val_set = set()
# for val in data:
#     val_set.add(val)

# print(val_set)

#all_data_objects = []



# for row in data:
#     print(row)


# count = 11
# for val in data[0]:
#     print('features[' + str(count) + '] = data_object.' + str(val))
#     count+=1

# data = format_data.clean_data(data)

# for i in range(len(data[0])):
#     print(str(data[0][i]) + ': ' + str(data[1][i]) + '   ' + str(data[2][i]))

# types = set()
# for row in data:
#     types.add(row[0])

# print(types)



