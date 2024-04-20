import glob 
import pandas as pd 
import xml.etree.ElementTree as ET 
from datetime import datetime


def extract_from_csv(file_to_process): 
    dataframe = pd.read_csv(file_to_process) 
    return dataframe 