import tensorflow as tf


def en_test():
    # 模拟一下同步处理数据
    Q = tf.FIFOQueue(3, tf.float32)

    # 放入一些数据
    enq_many = Q.enqueue_many([[0.1, 0.2, 0.3], ])

    # 定义一些处理数据的逻辑，取数据的过程
    out_q = Q.dequeue()

    data = out_q + 1

    en_q = Q.enqueue(data)

    with tf.Session() as sess:
        # 初始化队列
        sess.run(enq_many)

        # 处理数据
        for i in range(10):
            sess.run(en_q)  # 关联性

        # 训练数据
        for i in range(Q.size().eval()):
            print(sess.run(Q.dequeue()))


if __name__ == '__main__':
    en_test()
