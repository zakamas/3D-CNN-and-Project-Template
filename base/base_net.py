import tensorflow as tf

class BaseNet:

    def __init__(self, config):

        self.config = config
        self.init_global_step()
        self.init_cur_epoch()


    #save the model in the checkpoint_dir directory
    def save(self, sess):
        print("Saving model...")
        self.saver.save(sess, self.config.checkpoint_dir, self.global_step_tensor)
        print("Model saved")

    #load model from the the checkpoint
    def load(self, sess):

        latest_checkpoint = tf.train.latest_checkpoint(self.config.checkpoint_dir)
        if latest_checkpoint:
            print("Loading model checkpoint {} ...\n".format(latest_checkpoint))
            self.saver.restore(sess, latest_checkpoint)
            print("Model loaded")

    def init_cur_epoch(self):
        with tf.variable_scope('cur_epoch'):
            self.cur_epoch_tensor = tf.Variable(0, trainable=False, name='cur_epoch')
            self.increment_cur_epoch_tensor = tf.assign(self.cur_epoch_tensor,self.cur_epoch_tensor+1)

    # just initialize a tensorflow variable to use it as global step counter
    def init_global_step(self):
        # DON'T forget to add the global step tensor to the tensorflow trainer
        with tf.variable_scope('global_step'):
            self.global_step_tensor = tf.Variable(0, trainable=False, name='gloval_step')

    def init_saver(self):
        # self.saver = tf.train.Saver(max_to_keep = self.config.max_to_keep)
        raise NotImplementedError

    def build_model(self):
        raise NotImplementedError
