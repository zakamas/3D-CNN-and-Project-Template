import tensorflow as tf

from models.template_net import TemplateNet
from trainers.template.trainer import TemplateTrainer
from utilities.utils import process_config, create_dirs, get_args
from utilities.logger import Logger


def main():

    try:
        args = get_args()
        config = process_config(args.config)
    except:
        print("Missing or invalid arguments")
        exit(0)

    create_dirs([config.summary_dir, config.checkpoint_dir])

    sess = tf.Session()

    data = DataGenerator(config)

    model = TemplateNet(config)

    logger = Logger(sess, config)

    trainer = TemplateTrainer(sess, model, data, config, logger)

    model.load(sess)

    trainer.train()

if __name__ == '__main__':
    main()
