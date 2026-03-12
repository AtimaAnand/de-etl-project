from extract import extract_data
from transform import transform_data
from load import load_data
from logger import logger

def run_pipeline():
    logger.info("Starting ETL pipeline")

    data = extract_data()
    logger.info("Data extracted")

    transformed = transform_data(data)
    logger.info("Data transformed")

    load_data(transformed)
    logger.info("Data loaded into database")

if __name__ == "__main__":
    run_pipeline()