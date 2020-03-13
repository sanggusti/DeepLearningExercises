# Supported Devices

The supported devices for the Inference Engine are all Intel® hardware, and are a variety of such devices: CPUs, including integrated graphics processors, GPUs, FPGAs, and VPUs. You likely know what CPUs and GPUs are already, but maybe not the others.

FPGAs, or Field Programmable Gate Arrays, are able to be further configured by a customer after manufacturing. Hence the “field programmable” part of the name.

VPUs, or Vision Processing Units, are going to be like the Intel® Neural Compute Stick. They are small, but powerful devices that can be plugged into other hardware, for the specific purpose of accelerating computer vision tasks.

There is a wide variety of Intel® hardware available to use with the Inference Engine! There are some additional considerations around using features like Shape Inference with OpenVINO™ that do depend on the plugins used with different hardware.

Difference between devices
- CPU extension for certain network layers
- Certain differences among supported layers by device
- Raspi + Neural compute stick **supports IE** *but* **not Model Optimizer**

Mostly, how the Inference Engine operates on one device will be the same as other supported devices; however, you may remember me mentioning a CPU extension in the last lesson. That’s one difference, that a CPU extension can be added to support additional layers when the Inference Engine is used on a CPU.

There are also some differences among supported layers by device, which is linked to at the bottom of this page. Another important one to note is regarding when you use an Intel® Neural Compute Stick (NCS). An easy, fairly low-cost method of testing out an edge app locally, outside of your own computer is to use the NCS2 with a Raspberry Pi. The Model Optimizer is not supported directly with this combination, so you may need to create an Intermediate Representation on another system first, although there are [some instructions](https://software.intel.com/en-us/articles/model-downloader-optimizer-for-openvino-on-raspberry-pi) for one way to do so on-device. The Inference Engine itself is still supported with this combination.

Links:
Depending on your device, the different plugins do have some differences in functionality and optimal configurations. You can read more on Supported Devices [here](https://docs.openvinotoolkit.org/2019_R3/_docs_IE_DG_supported_plugins_Supported_Devices.html).