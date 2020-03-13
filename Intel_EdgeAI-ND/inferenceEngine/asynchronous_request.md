Synchronous request:
- waits and does nothing else until inference is complete
- the main thread is "blocked"
- The next frame is not gathered until the current frame's inference request is complete

Asynchronous Request
- Similar to front-end/networking concept
- Doesnt hold everything up if response is slow
- Send frame for inference start preprocessing next frame while waiting on inference result

## Synchronous
Synchronous requests will wait and do nothing else until the inference response is returned, blocking the main thread. In this case, only one frame is being processed at once, and the next frame cannot be gathered until the current frame’s inference request is complete.

## Asynchronous
You may have heard of asynchronous if you do front-end or networking work. In that case, you want to process things asynchronously, so in case the response for a particular item takes a long time, you don’t hold up the rest of your website or app from loading or operating appropriately.

Asynchronous, in our case, means other tasks may continue while waiting on the IE to respond. This is helpful when you want other things to still occur, so that the app is not completely frozen by the request if the response hangs for a bit.

Where the main thread was *blocked* in synchronous, asynchronous does not block the main thread. So, you could have a frame sent for inference, while still gathering and pre-processing the next frame. You can make use of the "wait" process to wait for the inference result to be available.

You could also use this with multiple webcams, so that the app could "grab" a new frame from one webcam while performing inference for the other.

## Further Research
- For more on Synchronous vs. Asynchronous, check out this [helpful post](https://whatis.techtarget.com/definition/synchronous-asynchronous-API).
- You can also check out the [documentation](https://docs.openvinotoolkit.org/2019_R3/_docs_IE_DG_Integrate_with_customer_application_new_API.html) on integrating the inference engine into an application to see the different functions calls from an Inference Request for sync (`Infer`) vs. async (`StartAsync`).
- Lastly, for further practice with Asynchronous Inference Requests, you can check out [this useful demo](https://github.com/opencv/open_model_zoo/blob/master/demos/object_detection_demo_ssd_async/README.md). You’ll get a chance to practice with Synchronous and Asynchronous Requests in the upcoming exercise.