from CNN_Classifier import logger
from CNN_Classifier.pipeline.Stage1_Data_Ingestion import DataIngestionTrainingPipeline
from CNN_Classifier.pipeline.Stage2_Prepare_Base import PrepareBaseModelTrainingPipeline
from CNN_Classifier.pipeline.Stage3_Training import ModelTrainingPipeline
from CNN_Classifier.pipeline.Stage4_Evaluation import EvaluationPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>>{STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>{STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare base model"

try:
        logger.info(f"*******************")
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Training"

try:
        logger.info(f"*******************")
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Evaluation stage"

try:
        logger.info(f"*******************")
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e