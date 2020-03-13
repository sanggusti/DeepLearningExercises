Integrating to your App
- Get an IR with the model optimizer to start
- Load it into the app with the inference engine
- Add pre-processing
- Make inference request
- Handle and process the output

extra steps:
- Add functionality for different confidence thresholds to determine when to drop bounding boxes for the output
- Adding functionality for different colors of the bounding boxes themselves

links:
There’s a ton of great potential edge applications out there for you to build. Here are some examples to hopefully get you thinking:

- [Intel®’s IoT Apps Across Industries](https://www.intel.com/content/www/us/en/internet-of-things/industry-solutions.html)
- [Starting Your First IoT Project](https://hackernoon.com/the-ultimate-guide-to-starting-your-first-iot-project-8b0644fbbe6d)
- [OpenVINO™ on a Raspberry Pi and Intel® Neural Compute Stick](https://www.pyimagesearch.com/2019/04/08/openvino-opencv-and-movidius-ncs-on-the-raspberry-pi/)

# Integrate the Inference Engine in An Edge App

You've come a long way from the first lesson where most of the code for working with
the OpenVINO toolkit was happening in the background. You worked with pre-trained models,
moved up to converting any trained model to an Intermediate Representation with the
Model Optimizer, and even got the model loaded into the Inference Engine and began making
inference requests.

In this final exercise of this lesson, you'll close off the OpenVINO workflow by extracting
the results of the inference request, and then integrating the Inference Engine into an existing
application. You'll still be given some of the overall application infrastructure, as more that of
will come in the next lesson, but all of that is outside of OpenVINO itself.

You will also add code allowing you to try out various confidence thresholds with the model,
as well as changing the visual look of the output, like bounding box colors.

Now, it's up to you which exact model you want to use here, although you are able to just
re-use the model you converted with TensorFlow before for an easy bounding box dectector.

Note that this application will run with a video instead of just images like we've done before.

So, your tasks are to:

1. Convert a bounding box model to an IR with the Model Optimizer.
2. Pre-process the model as necessary.
3. Use an async request to perform inference on each video frame.
4. Extract the results from the inference request.
5. Add code to make the requests and feed back the results within the application.
6. Perform any necessary post-processing steps to get the bounding boxes.
7. Add a command line argument to allow for different confidence thresholds for the model.
8. Add a command line argument to allow for different bounding box colors for the output.
9. Correctly utilize the command line arguments in #3 and #4 within the application.

When you are done, feed your model to `app.py`, and it will generate `out.mp4`, which you
can download and view. *Note that this app will take a little bit longer to run.* Also, if you need
to re-run inference, delete the `out.mp4` file first.

You only need to feed the model with `-m` before adding the customization; you should set
defaults for any additional arguments you add for the color and confidence so that the user
does not always need to specify them.

```bash
python app.py -m {your-model-path.xml}
```

# Integrate the Inference Engine - Solution

Let's step through the tasks one by one, with a potential approach for each.

> Convert a bounding box model to an IR with the Model Optimizer.

I used the SSD Mobilenet V2 architecture from TensorFlow from the earlier lesson here. Note
that the original was downloaded in a separate workspace, so I needed to download it again
and then convert it.

```
python /opt/intel/openvino/deployment_tools/model_optimizer/mo.py --input_model frozen_inference_graph.pb --tensorflow_object_detection_api_pipeline_config pipeline.config --reverse_input_channels --tensorflow_use_custom_operations_config /opt/intel/openvino/deployment_tools/model_optimizer/extensions/front/tf/ssd_v2_support.json
```

> Extract the results from the inference request

```
self.exec_network.requests[0].outputs[self.output_blob]
```

> Add code to make the requests and feed back the results within the application

```
self.exec_network.start_async(request_id=0, inputs={self.input_blob: image})
...
status = self.exec_network.requests[0].wait(-1)
```

> Add a command line argument to allow for different confidence thresholds for the model

I chose to use `-ct` as the argument name here, and added it to the existing arguments.

```
optional.add_argument("-ct", help="The confidence threshold to use with the bounding boxes", default=0.5)
```

I set a default of 0.5, so it does not need to be input by the user every time. 

> Add a command line argument to allow for different bounding box colors for the output

Similarly, I added the `-c` argument for inputting a bounding box color.
Note that in my approach, I chose to only allow "RED", "GREEN" and "BLUE", which also
impacts what I'll do in the next step; there are many possible approaches here.

```
optional.add_argument("-c", help="The color of the bounding boxes to draw; RED, GREEN or BLUE", default='BLUE')
```

> Correctly utilize the command line arguments in #3 and #4 within the application

Both of these will come into play within the `draw_boxes` function. For the first, a new line
should be added before extracting the bounding box points that check whether `box[2]`
(e.g. the probability of a given box) is above `args.ct` - assuming you have added 
`args.ct` as an argument passed to the `draw_boxes` function. If not, the box
should not be drawn. Without this, any random box will be drawn, which could be a ton of
very unlikely bounding box detections.

The second is just a small adjustment to the `cv2.rectangle` function that draws the 
bounding boxes we found to be above `args.ct`. I actually added a function to match
the different potential colors up to their RGB values first, due to how I took them in from the
command line:

```
def convert_color(color_string):
    '''
    Get the BGR value of the desired bounding box color.
    Defaults to Blue if an invalid color is given.
    '''
    colors = {"BLUE": (255,0,0), "GREEN": (0,255,0), "RED": (0,0,255)}
    out_color = colors.get(color_string)
    if out_color:
        return out_color
    else:
        return colors['BLUE']
```

I can also add the tuple returned from this function as an additional `color` argument to feed to
`draw_boxes`.

Then, the line where the bounding boxes are drawn becomes:

```
cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), color, 1)
```

I was able to run my app, if I was using the converted TF model from earlier (and placed in the 
current directory), using the below:

```bash
python app.py -m frozen_inference_graph.xml
```

Or, if I added additional customization with a confidence threshold of 0.6 and blue boxes:

```bash
python app.py -m frozen_inference_graph.xml -ct 0.6 -c BLUE
```

[Note that I placed my customized app actually in `app-custom.py`]
