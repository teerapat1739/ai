import tensorflow as tf

x = tf.Variable(10, name='x')
y = tf.Variable(20, name='y')

with tf.Session() as session:
    writer = tf.summary.FileWriter('./graphs', session.graph)
    session.run(tf.global_variables_initializer())

    for _ in range(10):
        session.run(tf.add(x, y))

    print(tf.get_default_graph().as_graph_def())

writer.close()