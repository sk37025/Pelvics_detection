import pydicom
from PIL import Image
import numpy as np


def check_patient_sex(file_name):
    '''
    환자의 성별을 체크하는 함수
    '''
    img = pydicom.read_file(file_name)
    try: 
        sex = img.PatientSex
    except AttributeError:
        sex = 'unknown'
    return sex

def check_image_laterality(file_name):
    '''
    ImageLaterality(x-ray 영상 부위) : R/RT (오른쪽) L/LT(왼쪽)
    해당 값이 기입이 안될 경우 Inversion Image
    '''
    img = pydicom.read_file(file_name)
    try:
        place = img.ImageLaterality
    except AttributeError:
        place = 'inversion'

    return place

def read_dicom_into_image(file_name):
    img = pydicom.read_file(file_name)
    return bit_Change_from_12_to_8(img.pixel_array)

def bit_Change_from_12_to_8(array):
    '''matrix must be a numpy array 
    returns uint8 version'''

    m_min = np.min(array)
    m_max = np.max(array)
    matrix = array-m_min
    return (np.array(np.rint( (matrix-m_min)/float(m_max-m_min) * 255.0),dtype=np.uint8))


