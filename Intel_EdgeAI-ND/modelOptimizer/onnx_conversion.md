# Using the Model Optimizer with ONNX Models

- Configue the model optimizer for onnx
- Convert the ONNX model with the model optimizer
  - may want/need certain general arguments
- Test the model in the IR format using the inference engine

The process for converting an ONNX model is again quite similar to the previous two, although ONNX does not have any ONNX-specific arguments to the Model Optimizer. So, you’ll only have the general arguments for items like changing the precision.

Additionally, if you are working with PyTorch or Apple ML models, they need to be converted to ONNX format first, which is done outside of the OpenVINO™ Toolkit. See the link further down on this page if you are interested in doing so.

Differences:
- No frozen or unfrozen models
- Different set of supported model architecture
- No ONNX-specific args to the model optimizer
- pytorch or apple core ML models must be in ONNX format before using the Model Optimizer

## Pytorch to ONNX

If you are interested in converting a PyTorch model using ONNX for use with the OpenVINO™ Toolkit, check out this [link](https://michhar.github.io/convert-pytorch-onnx/) for the steps to do so. From there, you can follow the steps for ONNX models to get an Intermediate Representation.

## Further Research

- The developer documentation for Converting ONNX Models can be found [here](https://docs.openvinotoolkit.org/2019_R3/_docs_MO_DG_prepare_model_convert_model_Convert_Model_From_ONNX.html). You’ll work through this process in the next exercise.

- ONNX also has additional models available in the [ONNX Model Zoo](https://github.com/onnx/models). By converting these over to Intermediate Representations, you can expand even further on the pre-trained models available to you.

## Exercise

In this exercise, you'll convert an ONNX Model into an Intermediate Representation using the Model Optimizer. You can find the related documentation [here](https://docs.openvinotoolkit.org/2018_R5/_docs_MO_DG_prepare_model_convert_model_Convert_Model_From_ONNX.html).

For this exercise, first download the bvlc_alexnet model from [here](https://s3.amazonaws.com/download.onnx/models/opset_8/bvlc_alexnet.tar.gz). Use the `tar -xvf` command with the downloaded file to unpack it.

Follow the documentation above and feed in the ONNX model to the Model Optimizer.

If the conversion is successful, the terminal should let you know that it generated an IR model. The locations of the `.xml` and `.bin` files, as well as execution time of the Model Optimizer, will also be output.

## Pytorch models

Note that we will only cover converting directly from an ONNX model here. If you are interested in converting a PyTorch model using ONNX for use with OpenVINO, check out this [link](https://michhar.github.io/convert-pytorch-onnx/) for the steps to do so. From there, you can follow the steps in the rest of this exercise once you have an ONNX model.

# Convert an ONNX Model - Solution

First, you can start by checking out the documentation specific to ONNX models [here](https://docs.openvinotoolkit.org/2018_R5/_docs_MO_DG_prepare_model_convert_model_Convert_Model_From_ONNX.html).

Now, given that I was in the directory with the ONNX model file, here was the 
full path to convert my model:

```
python /opt/intel/openvino/deployment_tools/model_optimizer/mo.py --input_model model.onnx
```