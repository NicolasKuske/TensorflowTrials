import tensorflow as tf

hello = tf.constant('hello world of tensorflow')
sess = tf.Session()
print(sess.run(hello))

