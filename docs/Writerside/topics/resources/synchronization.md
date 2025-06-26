# Synchronization

In order to get motion capture data from multiple cameras, it's important that the videos from the different cameras are synchronized. What that means is that the frames from each camera are aligned in time, so that frmae number N from camera A was taken at the same time as frame number N from camera B, and so on for each camera being used. If the frames from different cameras were not synchronized, then the subject would be in a different position in each camera view, and FreeMoCap would not be able to triangulate a single 3D position.

In order to ensure a high data quality, FreeMoCap requires frame-perfect synchronization, meaning each video in a recording session has the exact same number of frames. If you record your motion captures videos from the FreeMoCap GUI, frame-perfect synchronization is done for you. However, if you want to pre-record videos and import them into FreeMoCap, they will need to be synchronized before they can be processed. FreeMoCap provides two different methods of synchronizing while importing videos, or you can import videos that have already been synchronized with a different tool. 

## Synchronization Methods

### Audio Cross Correlation Method


### Brightness Contrast Detection

## What's Required for Synchronization?
- frame rates match exactly (is this true actually?)
For Audio Cross Correlation Method:
- videos all have audio tracks
- audio frame rates match exactly

## How to Synchronize in FreeMoCap

You can easily synchronize videos while importing videos into FreeMoCap by using [Skelly Synchronize](https://github.com/freemocap/skelly_synchronize), FreeMoCap's custom synchronization tool. 

<procedure title="Step 0 - Install FFMPEG" collapsible="true">
The video processing methods in Skelly Synchronize require [FFMPEG](https://ffmpeg.org/), an open source video processing library. You may already have it on your system, and you can check by opening a terminal or command prompt and running `where ffmpeg` on Windows or `which ffmpeg` on Mac/Linux. If a path shows up in the terminal you should be set, but if not you will need to download FFMPEG and, on Windows, add it to your path. You can follow these instructions to install FFMPEG: [How to Install FFmpeg on Ubuntu, Windows, and macOS](https://www.clipcat.com/blog/how-to-install-ffmpeg-on-ubuntu-windows-and-macos-a-complete-setup-guide/).
</procedure>

> To run synchronization in FreeMoCap, you must have FFMPEG installed and on your path. You can find instructions on how to do this here: [How to Install FFmpeg on Ubuntu, Windows, and macOS](https://www.clipcat.com/blog/how-to-install-ffmpeg-on-ubuntu-windows-and-macos-a-complete-setup-guide/).
> {style="warning"}

<procedure title="Step 1 - Import Videos" collapsible="true">
Now that you've verified you have FFMPEG, open FreeMoCap and click the "Import Videos" button on the home screen. This will oipen a dialog that allows you to select a folder of videos you want to synchronize. **Note:** you must choose a folder that has the exact videos you want to import. You cannot choose individual videos from inside a folder.
</procedure>

<procedure title="Step 2 - Select 'Synchronize videos' option" collapsible="true">
Under the file information and paths listed on the next screen, and above the "Recording Name" input box, you will see a checkbox titled `Synchronize videos`. Check the box and it will show synchronization options and some notes on what is required to be able to synchronize.

[screenshot of synchronization checkbox]
</procedure>

<procedure title="Step 3 - Select Synchronization Method" collapsible="true">
There are two synchronization methods to choose from, `Audio Cross Correlation` and `Brightness Contrast Detection`. You can read more about each method above to choose the right one for your videos. There are no settings for `Audio Cross Correlation`, but `Brightness Contrast Detection` has a parameter `Brightness Contrast Threshold` that you can set to match your exact lighting setup. If you are using the brightness contrast method and getting poor results, try changing the brightness contrast threshold.

[screenshot of synchronization extension]

</procedure>

<procedure title="Step 4 - Run Synchronization and Import" collapsible="true">
Now that you've chosen your desired synchronization method and settings, click the blue `Continue` button. This will synchronize them and import them into FreeMoCap. It may take a while, depending on the number of videos and their size. When it's done, it will set the videos you imported as your active recording, and you can continue with processing the videos.
</procedure>


## Synchronizing Before Importing