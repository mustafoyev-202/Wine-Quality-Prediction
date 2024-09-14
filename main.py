from Wine_Quality_Prediction import logger
from Wine_Quality_Prediction.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
# from Wine_Quality_Prediction.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
# from Wine_Quality_Prediction.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
# from Wine_Quality_Prediction.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
# from Wine_Quality_Prediction.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

if __name__ == '__main__':

    # first stage
    STAGE_NAME = "Data Ingestion Stage"
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
