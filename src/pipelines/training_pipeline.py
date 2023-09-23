import os
import sys
import logging
from exception import CustomException
import pandas as pd

from ..components.data_ingetion import DataIngestion

if __name__=='__main__':
    obj=DataIngestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion()
    print(train_data_path,test_data_path)