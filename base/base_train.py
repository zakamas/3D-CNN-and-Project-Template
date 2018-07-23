import tensorflow as tf


class BaseTrain:
    """docstring for BaseTrain."""
    def __init__(self, sess, model, data, config, logger):

        self.model = model
        self.sess = sess
        self.data = data
        self.config = config
        self.logger = logger
        self.init = tf.group(tf.global_variables_initializer(), tf.local_variables_initializer())
        self.sess.run(self.init)


        def train(self):

            for cur_epoch in range(self.model.cur_epoch_tensor.eval(self.sess), self.config.num_epochs+1, 1):
                self.train_epoch()
                self.sess.run(self.model.increment_cur_epoch_tensor)

        def train_epoch(self):
            #implement the logic of the epoch: loop and summaries
            raise NotImplementedError

        def train_step(self):
            #implement the logic of the train step : session and metrics

            raise NotImplementedError
   
