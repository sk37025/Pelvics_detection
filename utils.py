import matplotlib.pyplot as plt
from typing import List
import pydicom 
from src.data.common import read_dicom_into_image,check_image_laterality,check_patient_sex
import os 
import random 
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
        plt.figure(figsize=[5,5])
        plt.title(f"Pathent sex: {check_patient_sex(list[0])}, id: {os.path.basename(list[0])}")
        plt.imshow(read_dicom_into_image(list[0]),cmap = plt.cm.bone)

    plt.tight_layout()
    
