# Quick Check to verify Tensorflow can see your machine's GPU

import sys
import tensorflow as tf

print (sys.version)

# returns True if a GPU is available 
GPU_availability = tf.test.is_gpu_available();

# print out the number of accessible GPUs
if GPU_availability == True:
        
        
    physical_devices = tf.config.list_physical_devices('GPU');
    print("Num GPUs:", len(physical_devices))
    
else:
    
    print('GPU is not recognized')
    

# The top of the output terminal should print Number of GPUs available and the system version. There will be a lot of output from
# tensorflow that just opens libraries from CUDA and the Developer Kit to see the GPU

# if this file does not run try installing the latest version of NVIDIA CUDA and the Developer Kit