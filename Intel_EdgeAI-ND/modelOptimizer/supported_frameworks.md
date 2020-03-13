- caffe
- Tensorflow
- MXnet
- ONNX (including pytorch and apple ML )
- Kaldi

These are all open source, just like the OpenVINO™ Toolkit. Caffe is originally from UC Berkeley, TensorFlow is from Google Brain, MXNet is from Apache Software, ONNX is combined effort of Facebook and Microsoft, and Kaldi was originally an individual’s effort. Most of these are fairly multi-purpose frameworks, while Kaldi is primarily focused on speech recognition data.

There are some differences in how exactly to handle these, although most differences are handled under the hood of the OpenVINO™ Toolkit. For example, TensorFlow has some different steps for certain models, or frozen vs. unfrozen models. However, most of the functionality is shared across all of the supported frameworks.

## Differnces among frameworks
- Some differences exist using model optimizer with each
- E.g Tensorlow has different steps for certain mdels or frozen vs unforzen models
- Certain frameworks have additional optional parameters

Links:
- Caffe https://caffe.berkeleyvision.org/
- Tensorflow https://www.tensorflow.org/
- MXNet https://mxnet.apache.org/
- ONNX https://onnx.ai/
- Kaldi https://kaldi-asr.org/doc/dnn.html