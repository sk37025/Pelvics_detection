import matplotlib.pyplot as plt
from typing import List
import pydicom 
from src.data.common import read_dicom_into_image,check_image_laterality,check_patient_sex
import os 
import random 
import pandas as pd
from PIL import Image, ImageDraw

dir_ = os.getcwd()
raw_data_dir = os.path.join(dir_,"data/raw/")

def display_Image_in_rows(list,random_=False):
    list = [os.path.join("C://Users//sk370//Desktop//AI-VOUCHER//데이터",i)for i in list]
    if random_:
        # random으로 12개 보여 주는 것 
        plt.figure(figsize=[30,30])
        for i in range(1,13):
            tmp = random.randint(0,500)
            plt.subplot(3,4,i)
            plt.title(f"Pathent sex: {check_patient_sex(list[tmp])}, id: {os.path.basename(list[tmp])}")
            plt.imshow(read_dicom_into_image(list[tmp]),cmap = plt.cm.bone)
    else: 
        # 지정된 것들만 보여줌 
        img = pydicom.read_file(list[0])
        plt.figure(figsize=[img.Columns/100,img.Rows/100])
        plt.title(f"Pathent sex: {check_patient_sex(list[0])}, id: {os.path.basename(list[0])}")
        plt.imshow(read_dicom_into_image(list[0]),cmap = plt.cm.bone)

    plt.tight_layout()


def plot_image(img_path,save_path):
    img,cols, rows = read_dicom_into_image(img_path)
    img = Image.fromarray(img).convert("L")
    img2 = img.resize((cols,rows))
    img2.save(save_path)
    return img2

def create_label(lst,label_path):
    if lst[0]!= "fracture":
        raise "You entered wrong Label Please Check your Results file"
    else:
        with open(label_path,"w") as f:
            f.write("0 {} {} {} {}\n".format(lst[1],lst[2],lst[3],lst[4]))

    
def image_j_into_yolo_dir(csv_):
    '''
    Results(csv 형식)를 읽고 yolo형식에 맞게 데이터를 배치하는 코드 
    '''
    label_df = pd.read_csv(os.path.join(raw_data_dir,csv_),index_col=[0]).reset_index(drop=True)
    img_dir =  os.path.join(raw_data_dir, "train/images")
    label_dir = os.path.join(raw_data_dir, "train/labels")
    check_dir = os.path.join(raw_data_dir, "train/checks")
    for i,v in label_df.iterrows():
        # img있는지 확인
        file_name = v['Label'].split(":")[0]
        img_path = os.path.join(raw_data_dir,"FRACTURE/{}".format(file_name))
        isExist = os.path.exists(img_path)
        if isExist:
            # train/images/label 이름으로 저장 
            img = plot_image(img_path,os.path.join(img_dir, file_name.split(".")[0]+".png") )
            # train/labels/label 이름으로 저장
            create_label([v['Label'].split(":")[1],v['BX'],v['BY'],v['Width'],v['Height']],os.path.join(label_dir, file_name.split(".")[0]+".txt"))
            # train/checks/label 이름으로 저장
            draw = ImageDraw.Draw(img)
            draw.rectangle([(v["BX"],v["BY"]),(v["BX"]+v["Width"], v["BY"]+v['Height'])], outline = "red",width = 10)
            img.save(os.path.join(check_dir, file_name.split(".")[0]+".png"))
        else: 
            print("File not found!!!!")

if __name__ == "__main__":
    image_j_into_yolo_dir("Results.csv")
