## What is the Inference Engine

The Inference Engine, as the name suggests, does the real legwork of inference at the edge.

- Runs the actual inference on a model(IR) at the edge
- Optimized for intel hardware
- Provides a straightforward API so you can focus more on your edge application itself
- Built with C++ under the hood for fast operations
- Can use built in python wrapper to work with the inference engine

The Inference Engine runs the actual inference on a model. It only works with the Intermediate Representations that come from the Model Optimizer, or the Intel® Pre-Trained Models in OpenVINO™ that are already in IR format.

Where the Model Optimizer made some improvements to size and complexity of the models to improve memory and computation times, the Inference Engine provides hardware-based optimizations to get even further improvements from a model. This really empowers your application to run at the edge and use up as little of device resources as possible.

The Inference Engine has a straightforward API to allow easy integration into your edge application. The Inference Engine itself is actually built in C++ (at least for the CPU version), leading to overall faster operations; however, it is very common to utilize the built-in Python wrapper to interact with it in Python code.

## Developer Documentation
You can find the developer documentation [here](https://docs.openvinotoolkit.org/2019_R3/_docs_IE_DG_Deep_Learning_Inference_Engine_DevGuide.html) for working with the Inference Engine. We’ll delve deeper into it throughout the lesson.