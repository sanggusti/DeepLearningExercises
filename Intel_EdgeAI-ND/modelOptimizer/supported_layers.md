# Supported layers

Earlier, we saw some of the supported layers when looking at the names when converting from a supported framework to an IR. While that list is useful for one-offs, you probably don’t want to check whether each and every layer in your model is supported. You can also just see when you run the Model Optimizer what will convert.

While just about every layer you’d likely be using in your own neural network is supported with the Model Optimizer, sometimes you’ll need to make use of Custom Layers, which we’ll cover next.

What happens when a layer isn’t supported by the Model Optimizer? One potential solution is the use of custom layers, which we’ll go into more shortly. Another solution is actually running the given unsupported layer in its original framework. For example, you could potentially use TensorFlow to load and process the inputs and outputs for a specific layer you built in that framework, if it isn’t supported with the Model Optimizer. Lastly, there are also unsupported layers for certain hardware, that you may run into when working with the Inference Engine. In this case, there are sometimes extensions available that can add support. We’ll discuss that approach more in the next lesson.


Checking for supported layers
- List of layer translations from supported framework to IR
- Some differences among hardwares
- Will see more with inference engine which can directly check for supported layers of a given device

Handling  unsupported layers
- Custom layers
- Running layer with original framework
- hardware based cpu extension