import tensorflow as tf

# create a tensor of shape and all elements are zeros
a = tf.zeros([2, 3], tf.int32) # ==> [[0, 0, 0], [0, 0, 0]]

with tf.Session() as session:
    writer = tf.summary.FileWriter('./graphs', session.graph)
    print(session.run(a))


writer.close()