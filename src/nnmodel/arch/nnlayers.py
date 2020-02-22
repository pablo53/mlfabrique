import torch
from functools import reduce

from nnmodel.arch.layers import LinkedLayer
from nnmodel.arch import nnutils


class LeakyReLULayer(LinkedLayer):

    def __init__(self, name, alpha, input_layer=None):
        super(LeakyReLULayer, self).__init__(name, 'LeakyReLU', input_layer)
        self.alpha = alpha

    def link_arch(self):
        if not self.linked_arch:
            super(LeakyReLULayer, self).link_arch()
            self.process_fn = torch.nn.LeakyReLU(self.alpha)

    def layer_meta(self):
        meta = super(LeakyReLULayer, self).layer_meta()
        meta['alpha'] = self.alpha
        return meta


class Conv2DLayer(LinkedLayer):

    def __init__(self, name, output_filters, kernel_size, stride, dilation, padding, input_layer=None):
        super(Conv2DLayer, self).__init__(name, 'Conv2D', input_layer)
        self.output_filters = output_filters
        self.kernel_size = kernel_size
        self.stride = stride
        self.dilation = dilation
        self.padding = padding

    def link_arch(self):
        if not self.linked_arch:
            super(Conv2DLayer, self).link_arch()
            self.process_fn = torch.nn.Conv2D(self.output_shape[0], self.output_filters, kernel_size=self.kernel_size, stride=self.stride, dilation=self.dilation, padding=self.padding)
            self.output_shape = [self.output_filters] + [ nnutils.conv_redim(dim, kernel_size, stride, dilation, padding) for _, dim in enumerate(self.output_shape[1:3]) ]  # TODO: treat each dimension separately

    def layer_meta(self):
        meta = super(Cond2DLayer, self).layer_meta()
        meta['output_filters'] = self.output_filters
        meta['kernel_size'] = self.kernel_size
        meta['stride'] = self.stride
        meta['dilation'] = self.dilation
        meta['padding'] = self.padding
        return meta


class MaxPool2DLayer(LinkedLayer):

    def __init__(self, name, kernel_size, stride, dilation, padding, input_layer=None):
        super(MaxPool2DLayer, self).__init__(name, 'MaxPool2D', input_layer)
        self.kernel_size = kernel_size
        self.stride = stride
        self.dilation = dilation
        self.padding = padding

    def link_arch(self):
        if not self.linked_arch:
            super(MaxPool2DLayer, self).link_arch()
            self.process_fn = torch.nn.MaxPool2D(kernel_size=self.kernel_size, stride=self.stride, dilation=self.dilation, padding=self.padding)
            self.output_shape = [self.output_shape[0]] + [ nnutils.conv_redim(dim, kernel_size, stride, dilation, padding) for _, dim in enumerate(self.output_shape[1:3]) ]  # TODO: treat each dimension separately

    def layer_meta(self):
        meta = super(MaxPool2DLayer, self).layer_meta()
        meta['kernel_size'] = self.kernel_size
        meta['stride'] = self.stride
        meta['dilation'] = self.dilation
        meta['padding'] = self.padding
        return meta


class FlattenLayer(LinkedLayer):

    def __init__(self, name, input_layer=None):
        super(FlattenLayer, self).__init__(name, 'Flatten', input_layer)

    def link_arch(self):
        if not self.linked_arch:
            super(FlattenLayer, self).link_arch()
            self.output_shape = [ reduce(lambda a, b: a * b, self.output_shape) ]
            self.process_fn = lambda inp: inp.view(-1, self.output_shape[0])


class DenseLayer(LinkedLayer):

    def __init__(self, name, no_outputs, bias=True, input_layer=None):
        super(FlattenLayer, self).__init__(name, 'Dense', input_layer)
        self.bias = bias
        self.no_outputs = no_outputs

    def link_arch(self):
        if not self.linked_arch:
            super(FlattenLayer, self).link_arch()
            self.process_fn = torch.nn.Linear(self.output_shape[-1], self.no_outputs, bias=self.bias)
            self.output_shape = [ self.no_outputs ]

    def layer_meta(self):
        meta = super(DenseLayer, self).layer_meta()
        meta['with_bias'] = self.bias
        meta['no_of_outputs'] = self.no_outputs
        return meta
