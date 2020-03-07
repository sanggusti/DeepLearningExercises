In this lesson we'll cover:

- Basics of the Model Optimizer
- Different Optimization Techniques and their impact on model performance
- Supported Frameworks in the Intel® Distribution of OpenVINO™ Toolkit
- Converting from models in those frameworks to Intermediate Representations
- And a bit on Custom Layers

# The model Optimizer

The Model Optimizer helps convert models in multiple different frameworks to an Intermediate Representation, which is used with the Inference Engine. If a model is not one of the pre-converted models in the Pre-Trained Models OpenVINO™ provides, it is a required step to move onto the Inference Engine.

The Model Optimizer converts a model to an Intermediate Representation for use with the Inference Engine. This process includes potential improvements related to model size and speed, with potential trade-offs with accuracy.

As part of the process, it can perform various optimizations that can help shrink the model size and help make it faster, although this will not give the model higher inference accuracy. In fact, there will be some loss of accuracy as a result of potential changes like lower precision. However, these losses in accuracy are minimized.

## Local Configuration

Configuring the Model Optimizer is pretty straight forward for your local machine, given that you already have OpenVINO™ installed. You can navigate to your OpenVINO™ install directory first, which is usually `/opt/intel/openvino`. Then, head to `/deployment_tools/model_optimizer/install_prerequisites`, and run the `install_prerequisites.sh` script therein.

## Developer Documentation

You can find the developer documentation [here](https://docs.openvinotoolkit.org/2019_R3/_docs_MO_DG_Deep_Learning_Model_Optimizer_DevGuide.html) for working with the Model Optimizer. We’ll delve deeper into it throughout the lesson.

## Optimization Techniques

Here, I mostly focused on three optimization techniques: quantization, freezing and fusion. Note that at the end of the video when I mention hardware optimizations, those are done by the Inference Engine (which we’ll cover in the next lesson), not the Model Optimizer.

- Quantization


