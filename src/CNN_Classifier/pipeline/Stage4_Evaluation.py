from CNN_Classifier.config.configuration import ConfigurationManager
from CNN_Classifier.components.Evaluate_Model import Evaluation
from CNN_Classifier import logger


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()


            