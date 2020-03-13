> Each framework has its own pages concerning conversion event hough the process is pretty similar.

## Tensorflow conversion
- configure the model optimizer for tensorflow
- Freezer tf model if your model is not already frozen
- or use the separate instructions to convert a non frozen model
- convert tf model with the model
- Convert the tf model with model optimizer to an optimized IR (may want/need certain general or TF-specific arguments)
- Test the model in the IR using inference engine

Differences with other frameworks

- Unfrozen models use --mean_value and --scale
- Object detection model zoo
  - tensorflow_use_custom_operation_config
  - tensorflow_object_detection_api_pipeline_config
  - reverse_input_channels (RGB vs BGR)
- YOLO, DeepSpeech and certain others have own pages
- Even further extend the pretrained models availabele
- in tf format so need to convert to IR with model optimizer
- focused on object detection with bounding boxes

Once the Model Optimizer is configured, the next thing to do with a TensorFlow model is to determine whether to use a frozen or unfrozen model. You can either freeze your model, which I would suggest, or use the separate instructions in the documentation to convert a non-frozen model. Some models in TensorFlow may already be frozen for you, so you can skip this step.

From there, you can feed the model into the Model Optimizer, and get your Intermediate Representation. However, there may be a few items specific to TensorFlow for that stage, which you’ll need to feed into the Model Optimizer before it can create an IR for use with the Inference Engine.

TensorFlow models can vary for what additional steps are needed by model type, being unfrozen or frozen, or being from the TensorFlow Detection Model Zoo. Unfrozen models usually need the `--mean_values` and `--scale parameters` fed to the Model Optimizer, while the frozen models from the Object Detection Model Zoo don’t need those parameters. However, the frozen models will need TensorFlow-specific parameters like `--tensorflow_use_custom_operations_config` and `--tensorflow_object_detection_api_pipeline_config`. Also, `--reverse_input_channels` is usually needed, as TF model zoo models are trained on RGB images, while OpenCV usually loads as BGR. Certain models, like YOLO, DeepSpeech, and more, have their own separate pages.

## Tensorflow object detection model zoo
The models in the TensorFlow Object Detection Model Zoo can be used to even further extend the pre-trained models available to you. These are in TensorFlow format, so they will need to be fed to the Model Optimizer to get an IR. The models are just focused on object detection with bounding boxes, but there are plenty of different model architectures available.

links:
- The developer documentation for Converting TensorFlow Models can be found [here](https://docs.openvinotoolkit.org/2019_R3/_docs_MO_DG_prepare_model_convert_model_Convert_Model_From_TensorFlow.html). You’ll work through this process in the next exercise.
- TensorFlow also has additional models available in the [TensorFlow Detection Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md). By converting these over to Intermediate Representations, you can expand even further on the pre-trained models available to you.

## Exercise

n this exercise, you'll convert a TensorFlow Model from the Object Detection Model Zoo into an Intermediate Representation using the Model Optimizer.

As noted in the related [documentation](https://docs.openvinotoolkit.org/latest/_docs_MO_DG_prepare_model_convert_model_Convert_Model_From_TensorFlow.html), there is a difference in method when using a frozen graph vs. an unfrozen graph. Since freezing a graph is a TensorFlow-based function and not one specific to OpenVINO itself, in this exercise, you will only need to work with a frozen graph. However, I encourage you to try to freeze and load an unfrozen model on your own as well.

For this exercise, first download the SSD MobileNet V2 COCO model from [here](http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v2_coco_2018_03_29.tar.gz). Use the `tar -xvf` command with the downloaded file to unpack it.

From there, find the Convert a TensorFlow* Model header in the documentation, and feed in the downloaded SSD MobileNet V2 COCO model's .pb file.

If the conversion is successful, the terminal should let you know that it generated an IR model. The locations of the .xml and .bin files, as well as execution time of the Model Optimizer, will also be output.

Note: Converting the TF model will take a little over one minute in the workspace.

Make sure to pay attention to the note in this section regarding the --reverse_input_channels argument. If you are unsure about this argument, you can read more [here](https://docs.openvinotoolkit.org/latest/_docs_MO_DG_prepare_model_convert_model_Converting_Model_General.html#when_to_reverse_input_channels).

There is additional documentation specific to converting models from TensorFlow's Object Detection Zoo [here](https://docs.openvinotoolkit.org/latest/_docs_MO_DG_prepare_model_convert_model_tf_specific_Convert_Object_Detection_API_Models.html). You will likely need both the --tensorflow_use_custom_operations_config and --tensorflow_object_detection_api_pipeline_config arguments fed with their related files.


## Solution

# Convert a TensorFlow Model - Solution

First, you can start by checking out the additional documentation specific to TensorFlow
models from the Model Detection Zoo [here](https://docs.openvinotoolkit.org/latest/_docs_MO_DG_prepare_model_convert_model_tf_specific_Convert_Object_Detection_API_Models.html).

I noticed three additional arguments that were important here:

- `--tensorflow_object_detection_api_pipeline_config`
- `--tensorflow_use_custom_operations_config`
- `--reverse_input_channels`

The first of these just needs the `pipeline.config` file that came with the downloaded model.

The second of these needs a JSON support file for TensorFlow models. I found that the
`ssd_v2_support.json` extension worked with the MobileNet model here.

The final of these is due to the TensorFlow models being trained on RGB images, but the
Inference Engine otherwise defaulting to BGR.

Now, given that I was in the directory with the frozen model file from TensorFlow, here was the 
full path to convert my model:

```
python /opt/intel/openvino/deployment_tools/model_optimizer/mo.py --input_model frozen_inference_graph.pb --tensorflow_object_detection_api_pipeline_config pipeline.config --reverse_input_channels --tensorflow_use_custom_operations_config /opt/intel/openvino/deployment_tools/model_optimizer/extensions/front/tf/ssd_v2_support.json
```