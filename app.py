import os
import sys
from dataclasses import dataclass
from src.MlProject.exception import CustomException
from src.MlProject.components.data_ingestion import DataIngestion
from src.MlProject.components.data_ingestion import DataIngestionConfig
from src.MlProject.logger import logging
from src.MlProject.utils import read_mysql_data


if __name__=="__main__":
    logging.info("The execution has started")

    try:
        # data_ingestion_config=DataIngestionConfig()
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
