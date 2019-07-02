import tensorflow as tf
import os




def myregression():
    """
    自实现一个线性回归预测
    :return: None
    """
    with tf.variable_scope("data"):
        # 1、准备数据，x特征值 [100, 1]   y 目标值[100]
        x = tf.random_normal([100, 1], mean=1.75, stddev=0.5, name="x_data")

        # 矩阵相乘必须是二维的
        y_true = tf.matmul(x, [[0.7]]) + 0.8

    with tf.variable_scope("model"):
        # 2、建立线性回归模型 1个特征 1个权重 1个偏置 y = x w + b
        # 随机给一个权重和偏置的值，让他去计算损失，然后在当前状态下优化
        # 用变量定义才能优化
        # trainable参数:指定这个变量能跟梯度下降一起优化
        weight = tf.Variable(tf.random_normal([1, 1], mean=0.0, stddev=1.0), name="w")
        bias = tf.Variable(0.0, name="b")

        y_predict = tf.matmul(x, weight) + bias

    with tf.variable_scope("loss"):
        # 3、建立损失函数，均方误差
        loss = tf.reduce_mean(tf.square(y_true - y_predict))

    with tf.variable_scope("optimizer"):
        # 4、梯度下降 优化损失 learning_rate: 0~1,2,3,5,7,10
        train_op = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

    # 添加权重参数，损失值等在tensorboard观察的情况
    # tf.summary.scalar     收集对于损失函数和准确率
    # tf.summary.histogram      收集高纬度的变量参数
    # tf.summary.image      收集输入的图片张量能显示图片
    # 1、收集变量tensor
    tf.summary.scalar("losses", loss)
    tf.summary.histogram("weights", weight)

    # 2、合并写入事件
    # 定义合并tensor的op
    merged = tf.summary.merge_all()

    # 定义一个初始化变量OP
    init_op = tf.global_variables_initializer()

    # 定义一个保存模型的实例
    saver = tf.train.Saver()

    # 通过会话运行程序
    with tf.Session() as sess:
        sess.run(init_op)

        # 打印随即最先初始化的权重和偏置
        print("随即初始化的参数权重为: %f, 偏置为: %f" % (weight.eval(), bias.eval()))

        # 建立事件文件
        filewriter = tf.summary.FileWriter("./tmp/summary/test/", graph=sess.graph)

        # 加载模型，覆盖模型中随机定义的参数，从上次的训练结果开始 (随即初始化的参数权重为: 0.466679, 偏置为: 0.000000
        if os.path.exists("./tmp/ckpt/checkpoint"):
            saver.restore(sess, "./tmp/ckpt/model")

        # 循环训练 运行优化
        for i in range(500):
            sess.run(train_op)

            # 运行合并的tensor
            summary = sess.run(merged)

            filewriter.add_summary(summary, i)

            print("第%d次优化,参数权重为: %f, 偏置为: %f" % (i, weight.eval(), bias.eval()))

        saver.save(sess, "./tmp/ckpt/model")
    return None


if __name__ == '__main__':
    myregression()

