from base.base_train import BaseTrain
from tqdm import tqdm
import numpy as np

class TemplateTrainer(BaseTrain):
    """docstring for TemplateTrainer."""
    def __init__(self, sess, model, date, config, logger):
        super(TemplateTrainer, self).__init__(self, sess, model, date, config, logger)

    def train_epoch(self):

        pass

    def train_step(self):

        pass
        
