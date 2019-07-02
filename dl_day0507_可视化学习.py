import tensorflow as tf


def main():
    a = tf.constant([1, 2, 3, 4, 5])

    var = tf.Variable(tf.random_normal([2, 3], mean=0.0, stddev=1.0))

    print(a, var)

    # 必须做一步显示的初始化
    init_op = tf.global_variables_initializer()

    with tf.Session() as sess:
        sess.run(init_op)

        # 把程序的图结构写入事件文件，graph:把指定的图写进事件当中
        filewriter = tf.summary.FileWriter("./tmp/summary/test/", graph=sess.graph)

        print(sess.run([a, var]))


if __name__ == '__main__':
    main()

