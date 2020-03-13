## `IECore` and `IENetwork`

To load an IR into the Inference Engine, you’ll mostly work with two classes in the `openvino.inference_engine` library (if using Python):

- `IECore`, which is the Python wrapper to work with the Inference Engine
- `IENetwork`, which is what will initially hold the network and get loaded into `IECore`

The next step after importing is to set a couple variables to actually use the IECore and IENetwork. In the [IECore documentation](https://docs.openvinotoolkit.org/2019_R3/classie__api_1_1IECore.html), no arguments are needed to initialize. To use [IENetwork](https://docs.openvinotoolkit.org/2019_R3/classie__api_1_1IENetwork.html), you need to load arguments named `model` and `weights` to initialize - the XML and Binary files that make up the model’s Intermediate Representation.

## Check Supported Layers

In the [IECore documentation](https://docs.openvinotoolkit.org/2019_R3/classie__api_1_1IECore.html), there was another function called `query_network`, which takes in an IENetwork as an argument and a device name, and returns a list of layers the Inference Engine supports. You can then iterate through the layers in the IENetwork you created, and check whether they are in the supported layers list. If a layer was not supported, a CPU extension may be able to help.

The `device_name` argument is just a string for which device is being used - `”CPU”`, `”GPU”`, `”FPGA”`, or `”MYRIAD”` (which applies for the Neural Compute Stick).

## CPU extension

If layers were successfully built into an Intermediate Representation with the Model Optimizer, some may still be unsupported by default with the Inference Engine when run on a CPU. However, there is likely support for them using one of the available CPU extensions.

These do differ by operating system a bit, although they should still be in the same overall location. If you navigate to your OpenVINO™ install directory, then `deployment_tools`, `inference_engine`, `lib`, `intel64`:

- On Linux, you’ll see a few CPU extension files available for AVX and SSE. That’s a bit outside of the scope of the course, but look up Advanced Vector Extensions if you want to know more there. In the classroom workspace, the SSE file will work fine.
  - Intel® Atom processors use SSE4, while Intel® Core processors will utilize AVX.
  - This is especially important to make note of when transferring a program from a Core-based laptop to an Atom-based edge device. If the incorrect extension is specified in the application, the program will crash.
  - AVX systems can run SSE4 libraries, but not vice-versa.
- On Mac, there’s just a single CPU extension file.

You can add these directly to the `IECore` using their full path. After you’ve added the CPU extension, if necessary, you should re-check that all layers are now supported. If they are, it’s finally time to load the model into the IECore.

Links:
As you get more into working with the Inference Engine in the next exercise and into the future, here are a few pages of documentation I found useful in working with it.

- [IE Python API](https://docs.openvinotoolkit.org/2019_R3/ie_python_api.html)
- [IE Network](https://docs.openvinotoolkit.org/2019_R3/classie__api_1_1IENetwork.html)
- [IE Core](https://docs.openvinotoolkit.org/2019_R3/classie__api_1_1IECore.html)