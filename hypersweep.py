"""
This file serves as a evaluation interface for the network
"""
# Built in
import os
import sys

sys.path.append('../utils/')
# Torch

# Own
import flag_reader
from class_wrapper import Network
from model_maker import Backprop
from utils import data_reader
from utils.helper_functions import load_flags
from utils.evaluation_helper import plotMSELossDistrib
# Libs
import numpy as np
import matplotlib.pyplot as plt
from thop import profile, clever_format


def evaluate_from_model(model_dir, multi_flag=False, eval_data_all=False, save_misc=False, MSE_Simulator=False,
                        save_Simulator_Ypred=False):
    """
    Evaluating interface. 1. Retreive the flags 2. get data 3. initialize network 4. eval
    :param model_dir: The folder to retrieve the model
    :param multi_flag: The switch to turn on if you want to generate all different inference trial results
    :param eval_data_all: The switch to turn on if you want to put all data in evaluation data
    :return: None
    """
    # Retrieve the flag object
    print("Retrieving flag object for parameters")
    if (model_dir.startswith("models")):
        model_dir = model_dir[7:]
        print("after removing prefix models/, now model_dir is:", model_dir)
    print(model_dir)
    flags = load_flags(os.path.join("models", model_dir))
    flags.eval_model = model_dir  # Reset the eval mode
    flags.backprop_step = eval_flags.backprop_step
    if flags.data_set == 'ballistics':
        flags.test_ratio = 0.0078  # 12800 in total
    elif flags.data_set == 'sine_wave':
        flags.test_ratio = 0.001  # 8000 in total
    elif flags.data_set == 'robotic_arm':
        flags.test_ratio = 0.1  # 10000 in total
    else:
        flags.test_ratio = 0.0051062/2
        #flags.test_ratio = 0
        #flags.test_ratio = 0.00025                        # 20000 in total for Meta material
    flags.batch_size = 1  # For backprop eval mode, batchsize is always 1
    flags.lr = 1e-2
    if flags.data_set == 'ballistics':
        flags.lr = 1

    flags.train_step = eval_flags.train_step

    for i in range(4000, 5000, 2000):
        for j in range(3):
            flags.eval_batch_size = i
            # Get the data
            train_loader, test_loader = data_reader.read_data(flags, eval_data_all=eval_data_all)
            print("Making network now")

            # Make Network
            ntwk = Network(Backprop, flags, train_loader, test_loader, inference_mode=True, saved_model=flags.eval_model)
            print("number of trainable parameters is :")
            pytorch_total_params = sum(p.numel() for p in ntwk.model.parameters() if p.requires_grad)
            print(pytorch_total_params)

            # Evaluation process
            print("Start eval now:")
            if multi_flag:
                pred_file, truth_file = ntwk.evaluate(save_dir='D:/Yang_MM_Absorber_ML/NA/' + flags.data_set, save_all=True,
                                                      save_misc=save_misc, MSE_Simulator=MSE_Simulator,
                                                      save_Simulator_Ypred=save_Simulator_Ypred)
            else:
                pred_file, truth_file = ntwk.evaluate(save_dir='D:/Yang_MM_Absorber_ML/Backprop/data/'+str(i)+'/'+str(j+1), save_misc=save_misc, MSE_Simulator=MSE_Simulator,
                                                      save_Simulator_Ypred=save_Simulator_Ypred)

            # Plot the MSE distribution
            plotMSELossDistrib(pred_file, truth_file, flags, save_dir='D:/Yang_MM_Absorber_ML/Backprop/data/'+str(i)+'/'+str(j+1))
            print("Evaluation finished")


def evaluate_all(models_dir="models"):
    """
    This function evaluate all the models in the models/. directory
    :return: None
    """
    for file in os.listdir(models_dir):
        if os.path.isfile(os.path.join(models_dir, file, 'flags.obj')):
            evaluate_from_model(os.path.join(models_dir, file))
    return None


def evaluate_different_dataset(multi_flag, eval_data_all, save_Simulator_Ypred=False, MSE_Simulator=False):
    """
    This function is to evaluate all different datasets in the model with one function call
    """
    # data_set_list = ["meta_materialreg0.0005trail_2_complexity_swipe_layer1000_num6"]
    data_set_list = ["robotic_armreg0.0005trail_0_backward_complexity_swipe_layer500_num6",
                     "20200506_104444",
                     "ballisticsreg0.0005trail_0_complexity_swipe_layer500_num5"]
    for eval_model in data_set_list:
        useless_flags = flag_reader.read_flag()
        useless_flags.eval_model = eval_model
        evaluate_from_model(useless_flags.eval_model, multi_flag=multi_flag, eval_data_all=eval_data_all,
                            save_Simulator_Ypred=save_Simulator_Ypred, MSE_Simulator=MSE_Simulator)


if __name__ == '__main__':
    # Read the flag, however only the flags.eval_model is used and others are not used
    eval_flags = flag_reader.read_flag()

    # print(eval_flags.eval_model)
    # Call the evaluate function from model
    # evaluate_all()
    # For Meta-material !!!!!
    # evaluate_from_model(eval_flags.eval_model, save_misc=False, multi_flag=True, save_Simulator_Ypred=False, MSE_Simulator=False)
    # For non Meta-material !!!!!
    # evaluate_from_model(eval_flags.eval_model, save_misc=False, multi_flag=True, save_Simulator_Ypred=True, MSE_Simulator=False)
    # evaluate_from_model(eval_flags.eval_model, save_misc=False, multi_flag=False, save_Simulator_Ypred=True, MSE_Simulator=False)
    # evaluate_from_model(eval_flags.eval_model, save_misc=False, multi_flag=True)
    # evaluate_from_model(eval_flags.eval_model, multi_flag=True)
    # evaluate_different_dataset(multi_flag=False, eval_data_all=False, save_Simulator_Ypred=False, MSE_Simulator=False)
    # evaluate_from_model(eval_flags.eval_model, multi_flag=False, eval_data_all=True)

    # evaluate_from_model(eval_flags.eval_model)
    # evaluate_all(models_dir="models/")

    # Eval META_MATERIAL
    evaluate_from_model(eval_flags.eval_model, save_misc=False, multi_flag=False, save_Simulator_Ypred=False,
                        MSE_Simulator=False)

