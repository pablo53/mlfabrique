# NN Loader

This tools will allow to upload a Neural Network Architecture Definition via JSON file as per the following example:
'''
{
    "nnlayers": {
	"X": {
	    "input": "_input",
	    "sublayers": [
		{
		    "nnlayertype": "View",
		    "dims": [ -1, 1, 137, 236 ]
		}
	    ]
	},
	"Layer1": {
	    "input": "X",
	    "cuda": true,
	    "sublayers": [
		{
		    "id": "Z1",
		    "nnlayertype": "Conv2D",
		    "input_filters": 1,
		    "output_filters": 16,
		    "kernel_size": 5,
		    "stride": 1,
		    "padding": 1,
		    "cuda": true,
		    "half": false
		},
		{
		    "id": "A1",
		    "nnlayertype": "LeakyReLU",
		    "alpha": 0.2,
		    "cuda": true
		},
		{
		    "id": "M1",
		    "nnlayertype": "MaxPool2d",
		    "kernel_size": 2,
		    "stride": 2,
		    "padding": 1,
		    "cuda": true
		}
	    ]
	},
	"Y": {
	    "input": "Layer1",
	    "sublayers": [
		{
		    "nnlayertype": "View",
		    "dims": [ -1, 1, 137, 236 ]
		}
	    ]
	}
    }
}
'''

Necessary REST endpoints are exposed for this purpose.
