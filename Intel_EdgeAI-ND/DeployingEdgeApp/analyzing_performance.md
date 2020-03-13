# Analyzing Performance Basics

We’ve talked a lot about optimizing for inference and running apps at the edge, but it’s important not to skip past the accuracy of your edge AI model. Lighter, quicker models are helpful for the edge, and certain optimizations like lower precision that help with these will have some impact on accuracy, as we discussed earlier on.

No amount of skillful post-processing and attempting to extract useful data from the output will make up for a poor model choice, or one where too many sacrifices were made for speed.

Of course, it all depends on the exact application as to how much loss of accuracy is acceptable. Detecting a pet getting into the trash likely can handle less accuracy than a self-driving car in determining where objects are on the road.

The considerations of speed, size and network impacts are still very important for AI at the Edge. Faster models can free up computation for other tasks, lead to less power usage, or allow for use of cheaper hardware. Smaller models can also free up memory for other tasks, or allow for devices with less memory to begin with. We’ve also discussed some of the network impacts earlier. Especially for remote edge devices, the power costs of heavy network communication may significantly hamper their use,

Lastly, there can be other differences in cloud vs edge costs other than just network effects. While potentially lower up front, cloud storage and computation costs can add up over time. Data sent to the cloud could be intercepted along the way. Whether this is better or not at the edge does depend on a secure edge device, which isn’t always the case for IoT.

OpenVINO™ can help reduce model size and speed up inference, while its use at the edge can help reduce impacts on your network vs. streaming the same input data to cloud services.

Further Research
- We'll cover more on performance with the Intel® Distribution of OpenVINO™ Toolkit in later courses, but you can check out the [developer docs](https://docs.openvinotoolkit.org/2019_R3/_docs_IE_DG_Intro_to_Performance.html) here for a preview.
- Did you know [Netflix uses 15% of worldwide bandwidth](https://www.sandvine.com/hubfs/downloads/phenomena/phenomena-presentation-final.pdf) with its video streaming? Cutting down on streaming your video to the cloud vs. performing work at the edge can vastly cut down on network costs.