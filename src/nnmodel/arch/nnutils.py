
def conv_redim(dim, kernel_size, stride, dilation, padding):
    win_size = (kernel_size - 1) * dilation + 1
    ext_dim = dim + ((win_size - 1) if padding else 0)
    res_dim = max(0, ext_dim - win_size + stride) // stride
    return res_dim
