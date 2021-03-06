"""
Params for Back propagation model
"""
# Define which data set you are using
DATA_SET = 'meta_material'
# DATA_SET = 'gaussian_mixture'
#DATA_SET = 'sine_wave'
# DATA_SET = 'naval_propulsion'
# DATA_SET = 'robotic_arm'
# DATA_SET = 'ballistics'
TEST_RATIO = 0.2

# Model Architectural Params for meta_material data Set
USE_LORENTZ = False
LINEAR = [14, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 2000, 500]
CONV_OUT_CHANNEL = [4, 4, 4, 4]
CONV_KERNEL_SIZE = [8, 8, 5, 5]
CONV_STRIDE = [2, 2, 1, 1]


# Optimizer Params
OPTIM = "Adam"
REG_SCALE = 1e-6
BATCH_SIZE = 1024
EVAL_BATCH_SIZE = 1000
EVAL_STEP = 20
TRAIN_STEP = 500
BACKPROP_STEP = 300
LEARN_RATE = 1e-4
# DECAY_STEP = 25000 # This is for step decay, however we are using dynamic decaying
LR_DECAY_RATE = 0.2
STOP_THRESHOLD = 1e-9

# Data specific Params
X_RANGE = [i for i in range(2, 16)]
Y_RANGE = [i for i in range(16 , 2017)]                       # Real Meta-material dataset range
#Y_RANGE = [i for i in range(10 , 310 )]                         # Artificial Meta-material dataset
FORCE_RUN = True
MODEL_NAME = None
DATA_DIR = 'D:/Yang_MM_Absorber_ML'                                               # All simulated simple dataset
#DATA_DIR = '/work/sr365/'                                      # real Meta-material dataset
#DATA_DIR = '/work/sr365/NN_based_MM_data/'                      # Artificial Meta-material dataset
# DATA_DIR = '/home/omar/PycharmProjects/github/idlm_Pytorch-master/forward/'
GEOBOUNDARY =[0.3, 0.6, 1, 1.5, 0.1, 0.2, -0.7854, 0.7854]
NORMALIZE_INPUT = True

# Running specific
USE_CPU_ONLY = False
#EVAL_MODEL = "sine_wavereg2e-05trail_0_forward_swipe9"
EVAL_MODEL = "20200630_034731"
#EVAL_MODEL = "robotic_armreg0.0005trail_0_backward_complexity_swipe_layer500_num6"
#EVAL_MODEL = "ballisticsreg0.0005trail_0_complexity_swipe_layer500_num5"
#EVAL_MODEL = "meta_materialreg2e-05trail_0_forward_swipe6"
#EVAL_MODEL = "20200506_104444"