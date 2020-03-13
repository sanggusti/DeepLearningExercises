## Cutting Parts of a model
- Mostly for Tensorflow models
- pre/post processing parts that dont translate into existing inference engine layers
- unused parts
- too complex with unsupported ops
- SSD model post-processing
- Localize an issue

How to cut a model
- `--input` to specify the new entry layers if cutting from beginning
- `--output` to specify new ending layers if cutting from the end

Cutting a model is mostly applicable for TensorFlow models. As we saw earlier in converting these models, they sometimes have some extra complexities. Some common reasons for cutting are:

The model has pre- or post-processing parts that don’t translate to existing Inference Engine layers.
The model has a training part that is convenient to be kept in the model, but is not used during inference.
The model is too complex with many unsupported operations, so the complete model cannot be converted in one shot.
The model is one of the supported SSD models. In this case, you need to cut a post-processing part off.
There could be a problem with model conversion in the Model Optimizer or with inference in the Inference Engine. To localize the issue, cutting the model could help to find the problem
There’s two main command line arguments to use for cutting a model with the Model Optimizer, named intuitively as `--input` and `--output`, where they are used to feed in the layer names that should be either the new entry or exit points of the model.

links:
- Documentation: https://docs.openvinotoolkit.org/2019_R3/_docs_MO_DG_prepare_model_convert_model_Cutting_Model.html