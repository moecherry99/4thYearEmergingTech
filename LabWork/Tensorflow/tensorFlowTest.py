import tensorflow as tf

def tf_descent(X_tf, d_tf, mu, N_epochs):
    N = X_tf.get_shape().as_list()[0]
    f = 2 / N

    w = tf.Variable(tf.zeros((2, 1)), name="w_tf")
    y = tf.matmul(X_tf, w, name="y_tf")
    e = y - d_tf
    grad = f * tf.matmul(tf.transpose(X_tf), e)

    training_op = tf.assign(w, w - mu * grad)
    init = tf.global_variables_initializer()

    with tf.Session() as sess:
        init.run()
        for epoch in range(N_epochs):
            sess.run(training_op)
        opt = w.eval()
    return opt

X_tf = tf.constant(X, dtype=tf.float32, name="X_tf")
d_tf = tf.constant(d, dtype=tf.float32, name="d_tf")

tf_w = tf_descent(X_tf, d_tf, mu, N_epochs)
print(tf_w)
