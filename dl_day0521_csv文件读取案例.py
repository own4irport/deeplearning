import os
import tensorflow as tf


def csvread(filelist):
    """
    读取CSV文件
    :param filelist: 文件路径 + 名字的列表
    :return: 读取的内容
    """
    # 1、构造文件的队列
    file_queue = tf.train.string_input_producer(filelist)

    # 2、构造csv阅读器读取队列数据（按一行）
    reader = tf.TextLineReader()

    key, value = reader.read(file_queue)

    # 3、对每行内容解码
    # record_defaults:指定一个样本每一列的类型
    records = [["None"], ["None"]]

    example, label = tf.decode_csv(value, record_defaults=records)

    # 4、需要多数据 批处理
    # batch_size : 从队列中读取的批处理大小
    # num_threads : 进入队列的线程数
    # capacity : 整数，队列中元素的最大数量
    example_batch, label_batch = tf.train.batch([example, label], batch_size=3, num_threads=1, capacity=9)

    return example_batch, label_batch


if __name__ == '__main__':
    # 1、找到文件，放入列表  路径 + 名字 -> 列表当中
    file_name = os.listdir("./csvdata/")

    filelist = [os.path.join("./csvdata/", file) for file in file_name]

    example, label = csvread(filelist)

    with tf.Session() as sess:
        # 定义一个线程协调器
        coord = tf.train.Coordinator()

        # 开启读文件的线程
        threads = tf.train.start_queue_runners(sess, coord=coord)

        # 打印读取内容
        print(sess.run([example, label]))

        # 回收子线程
        coord.request_stop()

        coord.join(threads)


