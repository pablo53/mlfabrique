class AbstractLayer:

    def __init__(self, name, type_name):
        self.name = name
        self.type_name = type_name
        self.linked_arch = False
        self.linked_data = False

    def layer_meta(self):
        return {
            "id": self.name,
            "nnlayertype": self.type_name
        }

    def link_arch(self):
        if not self.linked_arch:
            self.process_fn = lambda i: i
            self.output_shape = self.get_input_shape()
            self.linked_arch = True

    def link_data(self):
        self.link_arch()
        if not self.linked_data:
            self.input_data = self.get_input_data()
            self.output_data = self.process_fn(self.input_data)
            self.linked_data = True

    def get_input_data(self):
        return None  # to be overridden

    def get_input_shape(self):
        return []  # to be overridden

    def output(self):
        self.link_arch()
        self.link_data()
        return self.output_data

    def shape(self):
        self.link_arch()
        return self.output_shape

    def unlink_data(self):
        self.linked_data = False
        self.input_data = None
        self.output_data = None

    def unlink_arch(self):
        self.unlink_data()
        self.linked_arch = False
        self.process_fn = None
        self.output_shape = None


class InputLayer(AbstractLayer):

    def __init__(self, name, input_data=None):
        super(InputLayer, self).__init__(name, 'Input')
        self.input_data = input_data

    def get_input_data(self):
        return self.input_data

    def get_input_shape(self):
        return self.input_data.shape

    def set_input_data(self, input_data):
        self.input_data = input_data


class LinkedLayer(AbstractLayer):

    def __init__(self, name, type_name, input_layer=None):
        super(LinkedLayer, self).__init__(name, type_name)
        self.input_layer = input_layer

    def get_input_data(self):
        return self.input_layer.output()

    def get_input_shape(self):
        return self.input_layer.shape()

    def set_input_layer(self, input_layer):
        self.input_layer = input_layer

