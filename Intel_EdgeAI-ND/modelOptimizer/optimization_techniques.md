Here, I mostly focused on three optimization techniques: quantization, freezing and fusion. Note that at the end of the video when I mention hardware optimizations, those are done by the Inference Engine (which we’ll cover in the next lesson), not the Model Optimizer.

## Quantization

Quantization is related to the topic of precision I mentioned before, or how many bits are used to represent the weights and biases of the model. During training, having these very accurate numbers can be helpful, but it’s often the case in inference that the precision can be reduced without substantial loss of accuracy. Quantization is the process of **reducing the precision** of a model.

With the OpenVINO™ Toolkit, models usually default to FP32, or 32-bit floating point values, while FP16 and INT8, for 16-bit floating point and 8-bit integer values, are also available (INT8 is only currently available in the Pre-Trained Models; the Model Optimizer does not currently support that level of precision). FP16 and INT8 will lose some accuracy, but the model will be smaller in memory and compute times faster. Therefore, quantization is a common method used for running models at the edge.

## Freezing

- Differenct context than freezing individual layers
- Used with tensorflow models
- removes operations and metadata only needed for training

Freezing in this context is used for TensorFlow models. Freezing TensorFlow models will remove certain operations and metadata only needed for training, such as those related to backpropagation. Freezing a TensorFlow model is usually a good idea whether before performing direct inference or converting with the Model Optimizer.

## Fusion

- Combined operations (Batch norm + activation + convolution = Comb Ops)

Fusion relates to combining multiple layer operations into a single operation. For example, a batch normalization layer, activation layer, and convolutional layer could be combined into a single operation. This can be particularly useful for GPU inference, where the separate operations may occur on separate GPU kernels, while a fused operation occurs on one kernel, thereby incurring less overhead in switching from one kernel to the next.

some optimizations done automatically

links:
- more about quantization: https://nervanasystems.github.io/distiller/quantization.html
- more about optimizations performed by the model optimizer in the openvino toolkit: https://docs.openvinotoolkit.org/2019_R3/_docs_MO_DG_prepare_model_Model_Optimization_Techniques.html

