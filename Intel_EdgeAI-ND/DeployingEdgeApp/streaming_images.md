Sometimes, you may still want a video feed to be streamed to a server. A security camera that detects a person where they shouldn’t be and sends an alert is useful, but you likely want to then view the footage. Since MQTT can’t handle images, we have to look elsewhere.

At the start of the course, we noted that network communications can be expensive in cost, bandwidth and power consumption. Video streaming consumes a ton of network resources, as it requires a lot of data to be sent over the network, clogging everything up. Even with high-speed internet, multiple users streaming video can cause things to slow down. As such, it’s important to first consider whether you even need to stream video to a server, or at least only stream it in certain situations, such as when your edge AI algorithm has detected a particular event.

## FFmpeg
Of course, there are certainly situations where streaming video is necessary. The FFmpeg library is one way to do this. The name comes from “fast forward” MPEG, meaning it’s supposed to be a fast way of handling the MPEG video standard (among others).

In our case, we’ll use the `ffserver` feature of FFmpeg, which, similar to MQTT, will actually have an intermediate FFmpeg server that video frames are sent to. The final Node server that displays a webpage will actually get the video from that FFmpeg server.

There are other ways to handle streaming video as well. In Python, you can also use a flask server to do some similar things, although we’ll focus on FFmpeg here.

## Setting up FFmpeg
You can download FFmpeg from ffmpeg.org. Using ffserver in particular requires a configuration file that we will provide for you. This config file sets the port and IP address of the server, as well as settings like the ports to receive video from, and the framerate of the video. These settings can also allow it to listen to the system stdout buffer, which is how you can send video frames to it in Python.

## Sending frames to FFmpeg
With the sys Python library, can use sys.stdout.buffer.write(frame) and sys.stdout.flush() to send the frame to the ffserver when it is running.

If you have a ffmpeg folder containing the configuration file for the server, you can launch the ffserver with the following from the command line:
```
sudo ffserver -f ./ffmpeg/server.conf
```
From there, you need to actually pipe the information from the Python script to FFmpeg. To do so, you add the | symbol after the python script (as well as being after any related arguments to that script, such as the model file or CPU extension), followed by ffmpeg and any of its related arguments.

For example:
```
python app.py -m “model.xml” | ffmpeg -framerate 24
```
And so on with additional arguments before or after the pipe symbol depending on whether they are for the Python application or for FFmpeg.

## Further Research
We covered [FFMPEG](https://www.ffmpeg.org/) and ffserver, but as you may guess, there are also other ways to stream video to a browser. Here are a couple other options you can investigate for your own use:

- [Set up Your Own Server on Linux](https://opensource.com/article/19/1/basic-live-video-streaming-server)
- [Use Flask and Python](https://www.pyimagesearch.com/2019/09/02/opencv-stream-video-to-web-browser-html-page/)