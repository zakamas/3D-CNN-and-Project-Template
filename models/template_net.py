from base.base_net import BaseNet
import tensorflow as tf


class TemplateNet(BaseNet):
    """docstring for TemplateNet."""
    def __init__(self, config):
        super(TemplateNet, self).__init__(config)
        self.build_model()
        self.init_saver()


    def build_model(self):
        self.is_training = tf.placeholder(tf.bool)
        self.x = tf.placeholder(tf.float32, shape=[None] + self.config.state_size)
        self.y = tf.placeholder(tf.float32, shape=[None,10])

        parse_args

    def init_saver(self):
        self.saver = tf.train.Saver(mac_to_keep = self.config.max_to_keep)
        pass
