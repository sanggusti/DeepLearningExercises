# Sending Inference Requests to the IE

Making inference request:
- Loading IENetwork into IECore creates ExecutableNetwork
- Inference Requests sent to the Executable Network
- Two methods of inference: Synchronous and Asynchronous
- 'infer' (Sync) or 'start_async' and 'wait' (Async)

After you load the `IENetwork` into the `IECore`, you get back an `ExecutableNetwork`, which is what you will send inference requests to. There are two types of inference requests you can make: Synchronous and Asynchronous. There is an important difference between the two on whether your app sits and waits for the inference or can continue and do other tasks.

With an `ExecutableNetwork`, synchronous requests just use the `infer` function, while asynchronous requests begin with `start_async`, and then you can `wait` until the request is complete. These requests are `InferRequest` objects, which will hold both the input and output of the request.

We'll look a little deeper into the difference between synchronous and asynchronous on the next page.

# Further Research
- [Executable Network documentation](https://docs.openvinotoolkit.org/2019_R3/classie__api_1_1ExecutableNetwork.html)
- [Infer Request documentation](https://docs.openvinotoolkit.org/2019_R3/classie__api_1_1InferRequest.html)