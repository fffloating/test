import numpy as np


def conv2d(image, kernel):
    """
    实现 Conv2D 卷积操作
    :param image: 输入图像，shape 为 (H, W, C)
    :param kernel: 卷积核，shape 为 (kh, kw, C, n_filters)
    :return: 卷积结果，shape 为 (H', W', n_filters)
    """
    # 获取输入图像和卷积核的尺寸
    C,H, W = image.shape
    n_filters,k_C,kh, kw = kernel.shape
    # 计算输出图像的尺寸
    H_out = H - kh + 1
    W_out = W - kw + 1
    # 初始化卷积结果矩阵
    conv_out = np.zeros((n_filters,H_out, W_out))
    # 对每个卷积核进行卷积操作
    for i in range(n_filters):
        # 获取当前卷积核
        kernel_i = kernel[i,:, :, :]
        # 对每个通道进行卷积操作
        for j in range(C):
            # 获取当前通道的输入图像和卷积核
            image_j = image[j,:, :]
            kernel_ij = kernel_i[j,:, :]
            # 对当前通道进行卷积操作
            for m in range(H_out):
                for n in range(W_out):
                    conv_out[i,m, n] += np.sum(image_j[m:m + kh, n:n + kw] * kernel_ij)
    return conv_out


# 定义输入图像和卷积核
image = np.array([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
    [[19, 20, 21], [22, 23, 24], [25, 26, 27]],

])#(3,3,3)C H W
kernel = np.array([
    [[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]],
    [[[13, 14], [15, 16]], [[17, 18], [19, 20]], [[21, 22], [23, 24]]],
    [[[25, 26], [27, 28]], [[29, 30], [31, 32]], [[33, 34], [35, 36]]],
[[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]],
])# (4,3,2,2) kn,C,ks,ks
# 进行卷积操作
conv_out = conv2d(image, kernel)
# 输出卷积结果
print(conv_out)
