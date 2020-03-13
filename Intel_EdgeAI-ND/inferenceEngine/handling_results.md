# Handling Results

You saw at the end of the previous exercise that the inference `requests` are stored in a requests attribute in the `ExecutableNetwork`. There, we focused on the fact that the `InferRequest` object had a `wait` function for asynchronous requests.

Each `InferRequest` also has a few attributes - namely, `inputs`, `outputs` and `latency`. As the names suggest, `inputs` in our case would be an image frame, `outputs` contains the results, and `latency` notes the inference time of the current request, although we won’t worry about that right now.

It may be useful for you to print out exactly what the `outputs` attribute contains after a request is complete. For now, you can ask it for the `data` under the `“prob”` key, or sometimes `output_blob` ([see related documentation](https://docs.openvinotoolkit.org/2019_R3/classInferenceEngine_1_1Blob.html)), to get an array of the probabilities returned from the inference request.

An `ExecutableNetwork` contains an `InferRequest` attribute by the name of `requests`, and feeding a given request ID key to this attribute will get the specific inference request in question.

From within this `InferRequest` object, it has an attribute of `outputs` from which you can use your `output_blob` to get the results of that inference request.