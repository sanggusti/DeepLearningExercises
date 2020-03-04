Deploy an App at the edge

In this lesson we covered:

- Basics of the Intel® Distribution of OpenVINO™ Toolkit
- Different Computer Vision model types
- Available Pre-Trained Models in the Software
- Choosing the right Pre-Trained Model for your App
- Loading and Deploying a Basic App with a Pre-Trained Model

# Deploying an App at the Edge

## Early steps and Car meta output handling

The code for calling preprocessing and utilizing the output handling functions from within app.py is fairly straightforward:

```python
preprocessed_image = preprocessing(image, h, w)
```

This is just feeding in the input image, along with height and width of the network, which the given `inference_network.load_model` function actually returned for you.

```python
output_func = handle_output(args.t)
processed_output = output_func(output, image.shape)
```
This is partly based on the helper function I gave you, which can return the correct output handling function by feeding in the model type. The second line actually sends the output of inference and image shape to whichever output handling function is appropriate.

**Car Meta Output Handling**

Given that the two outputs for the Car Meta Model are "type" and "color", and are just the softmax probabilities by class, I wanted you to just return the np.argmax, or the index where the highest probability was determined.

```python
def handle_car(output, input_shape):
    '''
    Handles the output of the Car Metadata model.
    Returns two integers: the argmax of each softmax output.
    The first is for color, and the second for type.
    '''
    # Get rid of unnecessary dimensions
    color = output['color'].flatten()
    car_type = output['type'].flatten()
    # TODO 1: Get the argmax of the "color" output
    color_pred = np.argmax(color)
    # TODO 2: Get the argmax of the "type" output
    type_pred = np.argmax(car_type)

    return color_pred, type_pred
```

**Run the Car Meta model**

```
python app.py -i "images/blue-car.jpg" -t "CAR_META" -m "/home/workspace/models/vehicle-attributes-recognition-barrier-0039.xml" -c "/opt/intel/openvino/deployment_tools/inference_engine/lib/intel64/libcpu_extension_sse4.so"
```

For the other models, make sure to update the input image `-i`, model type `-t`, and model `-m` accordingly.

## Pose Estimation Output Handling

Handling the car output was fairly straightforward by using `np.argmax`, but the outputs for the pose estimation and text detection models is a bit trickier. However, there's a lot of similar code between the two. In this second part of the solution, I'll go into detail on the pose estimation model, and then we'll finish with a quick video on handling the output of the text detection model.

The model keys are not explicitly said in the documentation, so it would be better for you to check the keys simply with `print(output.keys)`.

Pose Estimation is more difficult, and doesn't have as nicely named outputs. I noted you just need the second one in this exercise, called `'Mconv7_stage2_L2'`, which is just the keypoint heatmaps, and not the associations between these keypoints. From there, I created an empty array to hold the output heatmaps once they are re-sized, as I decided to iterate through each heatmap 1 by 1 and re-size it, which can't be done in place on the original output.

```python
def handle_pose(output, input_shape):
    '''
    Handles the output of the Pose Estimation model.
    Returns ONLY the keypoint heatmaps, and not the Part Affinity Fields.
    '''
    # TODO 1: Extract only the second blob output (keypoint heatmaps)
    heatmaps = output['Mconv7_stage2_L2']
    # TODO 2: Resize the heatmap back to the size of the input
    # Create an empty array to handle the output map
    out_heatmap = np.zeros([heatmaps.shape[1], input_shape[0], input_shape[1]])
    # Iterate through and re-size each heatmap
    for h in range(len(heatmaps[0])):
        out_heatmap[h] = cv2.resize(heatmaps[0][h], input_shape[0:2][::-1])

    return out_heatmap
```

Note that the `input_shape[0:2][::-1]` line is taking the original image shape of HxWxC, taking just the first two (HxW), and reversing them to be WxH as `cv2.resize` uses.

## Text Detection Model Handling

Text Detection had a very similar output processing function, just using the `'model/segm_logits/add'` output and only needing to resize over two "channels" of output. I likely could have extracted this out into its own output handling function that both Pose Estimation and Text Detection could have used.

```python
def handle_text(output, input_shape):
    '''
    Handles the output of the Text Detection model.
    Returns ONLY the text/no text classification of each pixel,
        and not the linkage between pixels and their neighbors.
    '''
    # TODO 1: Extract only the first blob output (text/no text classification)
    text_classes = output['model/segm_logits/add']
    # TODO 2: Resize this output back to the size of the input
    out_text = np.empty([text_classes.shape[1], input_shape[0], input_shape[1]])
    for t in range(len(text_classes[0])):
        out_text[t] = cv2.resize(text_classes[0][t], input_shape[0:2][::-1])

    return out_text
```