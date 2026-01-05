import os
import numpy as np
import argparse
import os

parser = argparse.ArgumentParser(description="Dataset")
parser.add_argument("--root_dir", type=str, default="/scratch/FIDTM")
args = parser.parse_args()

if not os.path.exists('.npydata/npy'):
    os.makedirs('.npydata/npy')

'''please set your dataset path'''
shanghai_root = os.path.join(args.root_dir, "ShanghaiTech")
jhu_root = os.path.join(args.root_dir, "jhu_crowd_v2.0")
qnrf_root = os.path.join(args.root_dir, "UCF-QNRF_ECCV18")
carpk_root = os.path.join(args.root_dir, "CARPK")
pucpr_root = os.path.join(args.root_dir, "PUCPR")
large_root = os.path.join(args.root_dir, "large-vehicle")
small_root = os.path.join(args.root_dir, "small-vehicle")
jhu_root = os.path.join(args.root_dir, "jhu_crowd_v2.0")
# ucf50_root = os.path.join(args.root_dir, "UCF50")
ship_root = os.path.join(args.root_dir, "ship")
building_root = os.path.join(args.root_dir, "building")
ucf50_root = "/scratch/jingan/UCF50" 


#筛选数据集的上海Tech路径
select_shanghai = "/scratch/FIDTM/adaptation_chen_energy_FN_KM_datasets/select_dataset/A_B_10_100"
unlabeled_shanghai = "/scratch/FIDTM/adaptation_chen_energy_FN_KM_datasets/unlabeled_dataset/A_B_10_100"

#筛选数据集的QNRF路径
select_qnrf_root = "/scratch/FIDTM/adaptation_chen_energy_FN_KM_datasets/select_dataset/B_Q"
unlabeled_qnrf_root = "/scratch/FIDTM/adaptation_chen_energy_FN_KM_datasets/unlabeled_dataset/B_Q"


parser = argparse.ArgumentParser()
parser.add_argument(
    "--dataset",
    type=str,
    default="Select_ShanghaiB",  #修改数据集
    choices=[
        "ShanghaiA","ShanghaiB", "UCF_QNRF", "JHU", "NWPU",
        "Select_ShanghaiA","Select_ShanghaiB", "Select_UCF_QNRF","Ablation_partB",
        "UCF50_1", "UCF50_2", "UCF50_3", "UCF50_4", "UCF50_5",
        "CARPK", "PUCPR", "large", "small", "TRANCOS", "ship", "building",
    ],
    help="choice train dataset",
)
args = parser.parse_args()


if args.dataset == "Select_ShanghaiB":
    try:
        shanghaiBtrain_path = select_shanghai + '/part_B_final/train_data/images/'
        shanghaiBtest_path = "/scratch/FIDTM/ShanghaiTech" + '/part_B_final/test_data/images/'

        train_list = []
        for filename in os.listdir(shanghaiBtrain_path):
            if filename.split('.')[1] == 'jpg':
                train_list.append(shanghaiBtrain_path + filename)
        train_list.sort()
        np.save('./npydata/select_ShanghaiB_train.npy', train_list)

        test_list = []
        for filename in os.listdir(shanghaiBtest_path):
            if filename.split('.')[1] == 'jpg':
                test_list.append(shanghaiBtest_path + filename)
        test_list.sort()
        np.save('./npydata/select_ShanghaiB_test.npy', test_list)
        print("Generate select ShanghaiB image list successfully")
    except:
        print("The select ShanghaiB dataset path is wrong. Please check your path.")
        
    try:
        shanghaiBtrain_path = unlabeled_shanghai + '/part_B_final/train_data/images/'
        shanghaiBtest_path = "/scratch/FIDTM/ShanghaiTech" + '/part_B_final/test_data/images/'

        train_list = []
        for filename in os.listdir(shanghaiBtrain_path):
            if filename.split('.')[1] == 'jpg':
                train_list.append(shanghaiBtrain_path + filename)
        train_list.sort()
        np.save('./npydata/unlabeled_ShanghaiB_train.npy', train_list)

        test_list = []
        for filename in os.listdir(shanghaiBtest_path):
            if filename.split('.')[1] == 'jpg':
                test_list.append(shanghaiBtest_path + filename)
        test_list.sort()
        np.save('./npydata/unlabeled_ShanghaiB_test.npy', test_list)
        print("Generate unlabeled ShanghaiB image list successfully")
    except:
        print("The unlabeled ShanghaiB dataset path is wrong. Please check your path.")

if args.dataset == "Select_ShanghaiA":
    try:
        shanghaiAtrain_path = select_shanghai + '/part_A_final/train_data/images/'
        shanghaiAtest_path = "/scratch/FIDTM/ShanghaiTech" + '/part_A_final/test_data/images/'

        train_list = []
        for filename in os.listdir(shanghaiAtrain_path):
            if filename.split('.')[1] == 'jpg':
                train_list.append(shanghaiAtrain_path + filename)

        train_list.sort()
        np.save('./npydata/select_ShanghaiA_train.npy', train_list)

        test_list = []
        for filename in os.listdir(shanghaiAtest_path):
            if filename.split('.')[1] == 'jpg':
                test_list.append(shanghaiAtest_path + filename)
        test_list.sort()
        np.save('./npydata/select_ShanghaiA_test.npy', test_list)

        print("generate select ShanghaiA image list successfully")
    except:
        print("The select ShanghaiA dataset path is wrong. Please check you path.")

    try:
        shanghaiAtrain_path = unlabeled_shanghai + '/part_A_final/train_data/images/'
        shanghaiAtest_path = "/scratch/FIDTM/ShanghaiTech" + '/part_A_final/test_data/images/'

        train_list = []
        for filename in os.listdir(shanghaiAtrain_path):
            if filename.split('.')[1] == 'jpg':
                train_list.append(shanghaiAtrain_path + filename)

        train_list.sort()
        np.save('./npydata/unlabeled_ShanghaiA_train.npy', train_list)

        test_list = []
        for filename in os.listdir(shanghaiAtest_path):
            if filename.split('.')[1] == 'jpg':
                test_list.append(shanghaiAtest_path + filename)
        test_list.sort()
        np.save('./npydata/unlabeled_ShanghaiA_test.npy', test_list)

        print("generate unlabeled ShanghaiA image list successfully")
    except:
        print("The unlabeled ShanghaiA dataset path is wrong. Please check you path.")    

if args.dataset == "Select_UCF_QNRF":
    try:
        Qnrf_train_path = unlabeled_qnrf_root + '/train_data/images/'
        Qnrf_test_path = "/scratch/FIDTM/UCF-QNRF_ECCV18" + '/test_data/images/'

        train_list = []
        for filename in os.listdir(Qnrf_train_path):
            if filename.split('.')[1] == 'jpg':
                train_list.append(Qnrf_train_path + filename)
        train_list.sort()
        np.save('./npydata/unlabeled_qnrf_train.npy', train_list)

        test_list = []
        for filename in os.listdir(Qnrf_test_path):
            if filename.split('.')[1] == 'jpg':
                test_list.append(Qnrf_test_path + filename)
        test_list.sort()
        np.save('./npydata/unlabeled_qnrf_test.npy', test_list)
        print("Generate unlabeled QNRF image list successfully")
    except:
        print("The unlabeled QNRF dataset path is wrong. Please check your path.")

    try:
        Qnrf_train_path = select_qnrf_root + '/train_data/images/'
        Qnrf_test_path = "/scratch/FIDTM/UCF-QNRF_ECCV18" + '/test_data/images/'

        train_list = []
        for filename in os.listdir(Qnrf_train_path):
            if filename.split('.')[1] == 'jpg':
                train_list.append(Qnrf_train_path + filename)
        train_list.sort()
        np.save('./npydata/select_qnrf_train.npy', train_list)

        test_list = []
        for filename in os.listdir(Qnrf_test_path):
            if filename.split('.')[1] == 'jpg':
                test_list.append(Qnrf_test_path + filename)
        test_list.sort()
        np.save('./npydata/select_qnrf_test.npy', test_list)
        print("Generate select QNRF image list successfully")
    except:
        print("The select QNRF dataset path is wrong. Please check your path.")

if args.dataset == "ShanghaiA":   
    try:
        shanghaiAtrain_path = "/scratch/FIDTM/ShanghaiTech" + '/part_A_final/train_data/images/'
        shanghaiAtest_path = "/scratch/FIDTM/ShanghaiTech" + '/part_A_final/test_data/images/'

        train_list = []
        for filename in os.listdir(shanghaiAtrain_path):
            if filename.split('.')[1] == 'jpg':
                train_list.append(shanghaiAtrain_path + filename)

        train_list.sort()
        np.save('./npydata/ShanghaiA_train.npy', train_list)

        test_list = []
        for filename in os.listdir(shanghaiAtest_path):
            if filename.split('.')[1] == 'jpg':
                test_list.append(shanghaiAtest_path + filename)
        test_list.sort()
        np.save('./npydata/ShanghaiA_test.npy', test_list)

        print("generate ShanghaiA image list successfully")
    except:
        print("The ShanghaiA dataset path is wrong. Please check you path.")

if args.dataset == "ShanghaiB": 
    try:
        shanghaiBtrain_path = "/scratch/FIDTM/ShanghaiTech" + '/part_B_final/train_data/images/'
        shanghaiBtest_path = "/scratch/FIDTM/ShanghaiTech" + '/part_B_final/test_data/images/'

        train_list = []
        for filename in os.listdir(shanghaiBtrain_path):
            if filename.split('.')[1] == 'jpg':
                train_list.append(shanghaiBtrain_path + filename)
        train_list.sort()
        np.save('./npydata/ShanghaiB_train.npy', train_list)

        test_list = []
        for filename in os.listdir(shanghaiBtest_path):
            if filename.split('.')[1] == 'jpg':
                test_list.append(shanghaiBtest_path + filename)
        test_list.sort()
        np.save('./npydata/ShanghaiB_test.npy', test_list)
        print("Generate ShanghaiB image list successfully")
    except:
        print("The ShanghaiB dataset path is wrong. Please check your path.")

if args.dataset == "UCF_QNRF": 

    try:
        Qnrf_train_path = qnrf_root + '/train_data/images/'
        Qnrf_test_path = qnrf_root + '/test_data/images/'

        train_list = []
        for filename in os.listdir(Qnrf_train_path):
            if filename.split('.')[1] == 'jpg':
                train_list.append(Qnrf_train_path + filename)
        train_list.sort()
        np.save('./npydata/qnrf_train.npy', train_list)

        test_list = []
        for filename in os.listdir(Qnrf_test_path):
            if filename.split('.')[1] == 'jpg':
                test_list.append(Qnrf_test_path + filename)
        test_list.sort()
        np.save('./npydata/qnrf_test.npy', test_list)
        print("Generate QNRF image list successfully")
    except:
        print("The QNRF dataset path is wrong. Please check your path.")
 
if args.dataset == "JHU":       
    try:
        Jhu_train_path = jhu_root + '/train/images_2048/'
        Jhu_val_path = jhu_root + '/val/images_2048/'
        jhu_test_path = jhu_root + '/test/images_2048/'

        train_list = []
        for filename in os.listdir(Jhu_train_path):
            if filename.split('.')[1] == 'jpg':
                train_list.append(Jhu_train_path + filename)
        train_list.sort()
        np.save('./npydata/jhu_train.npy', train_list)

        val_list = []
        for filename in os.listdir(Jhu_val_path):
            if filename.split('.')[1] == 'jpg':
                val_list.append(Jhu_val_path + filename)
        val_list.sort()
        np.save('./npydata/jhu_val.npy', val_list)

        test_list = []
        for filename in os.listdir(jhu_test_path):
            if filename.split('.')[1] == 'jpg':
                test_list.append(jhu_test_path + filename)
        test_list.sort()
        np.save('./npydata/jhu_test.npy', test_list)

        print("Generate JHU image list successfully")
    except:
        print("The JHU dataset path is wrong. Please check your path.")


if args.dataset == "Ablation_partB": 
    try:
        shanghaiBtrain_path = select_shanghai + '/part_B_final/train_data/images/'
        shanghaiBtest_path = "/scratch/FIDTM/ShanghaiTech" + '/part_B_final/test_data/images/'

        train_list = []
        for filename in os.listdir(shanghaiBtrain_path):
            if filename.split('.')[1] == 'jpg':
                train_list.append(shanghaiBtrain_path + filename)
        train_list.sort()
        np.save('./npydata/select_ShanghaiB_train.npy', train_list)

        test_list = []
        for filename in os.listdir(shanghaiBtest_path):
            if filename.split('.')[1] == 'jpg':
                test_list.append(shanghaiBtest_path + filename)
        test_list.sort()
        np.save('./npydata/select_ShanghaiB_test.npy', test_list)
        print("Generate random select ShanghaiB image list successfully")
    except:
        print("The random select ShanghaiB dataset path is wrong. Please check your path.")
        
    try:
        shanghaiBtrain_path = unlabeled_shanghai + '/part_B_final/train_data/images/'
        shanghaiBtest_path = "/scratch/FIDTM/ShanghaiTech" + '/part_B_final/test_data/images/'

        train_list = []
        for filename in os.listdir(shanghaiBtrain_path):
            if filename.split('.')[1] == 'jpg':
                train_list.append(shanghaiBtrain_path + filename)
        train_list.sort()
        np.save('./npydata/unlabeled_ShanghaiB_train.npy', train_list)

        test_list = []
        for filename in os.listdir(shanghaiBtest_path):
            if filename.split('.')[1] == 'jpg':
                test_list.append(shanghaiBtest_path + filename)
        test_list.sort()
        np.save('./npydata/unlabeled_ShanghaiB_test.npy', test_list)
        print("Generate random unlabeled ShanghaiB image list successfully")
    except:
        print("The random unlabeled ShanghaiB dataset path is wrong. Please check your path.")



    

