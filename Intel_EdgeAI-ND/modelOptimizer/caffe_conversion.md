The process for converting a Caffe model is fairly similar to the TensorFlow one, although there’s nothing about freezing the model this time around, since that’s a TensorFlow concept. Caffe does have some differences in the set of supported model architectures. Additionally, Caffe models need to feed both the `.caffemodel` file, as well as a `.prototxt` file, into the Model Optimizer. If they have the same name, only the model needs to be directly input as an argument, while if the `.prototxt` file has a different name than the model, it should be fed in with `--input_proto` as well.

links:
- documentation https://docs.openvinotoolkit.org/2019_R3/_docs_MO_DG_prepare_model_convert_model_Convert_Model_From_Caffe.html

## Exercise

In this exercise, you'll convert a Caffe Model into an Intermediate Representation using the Model Optimizer. You can find the related documentation [here](https://docs.openvinotoolkit.org/2018_R5/_docs_MO_DG_prepare_model_convert_model_Convert_Model_From_Caffe.html).

For this exercise, first download the SqueezeNet V1.1 model by cloning this [repository](https://github.com/DeepScale/SqueezeNet).

ollow the documentation above and feed in the Caffe model to the Model Optimizer.

If the conversion is successful, the terminal should let you know that it generated an IR model. The locations of the `.xml` and `.bin` files, as well as execution time of the Model Optimizer, will also be output.

You will need to specify --input_proto if the .prototxt file is not named the same as the model.

There is an important note in the documentation after the section Supported Topologies regarding Caffe models trained on ImageNet. If you notice poor performance in inference, you may need to specify mean and scale values in your arguments.

```
python /opt/intel/openvino/deployment_tools/model_optimizer/mo.py --input_model squeezenet_v1.1.caffemodel --input_proto deploy.prototxt
```

# Convert a Caffe Model - Solution

First, you can start by checking out the documentation specific to Caffe models [here](https://docs.openvinotoolkit.org/2018_R5/_docs_MO_DG_prepare_model_convert_model_Convert_Model_From_Caffe.html).

I did notice an additional helpful argument here: `--input_proto`, which is used to specify
a `.prototxt` file to pair with the `.caffemodel` file when the model name and `.prototxt`
filename do not match.

Now, given that I was in the directory with the Caffe model file & `.prototxt` file, here was the 
full path to convert my model:

```
python /opt/intel/openvino/deployment_tools/model_optimizer/mo.py --input_model squeezenet_v1.1.caffemodel --input_proto deploy.prototxt
```