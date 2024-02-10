# Calibration Troubleshooting 

Camera calibration is a smooth process once you get the hang of it, but it can take some trial and error to get your set up right. The following tips will help you smooth out the road bumps, and at the bottom is a list of common error messages you may see in the logging console, along with common solutions. 

If this guide isn't enough to get you calibrating your cameras successfully, reach out to us on our [Discord](https://discord.gg/j76UGWfEeA) to ask for more help.

## Charuco Board Size
Using a bigger charuco board can make it easier for your cameras to detect the board, especially in difficult lighting. Printing the board on a standard sheet of printer paper can work, but often bigger is better. Larger charuco boards can be printed directly on large poster board, or made by pasting together smaller partial printouts into a complete board.

You can help make a small charuco board work by holding it closer to the cameras while recording, but make sure the board is still visible from multiple cameras at a time.

## Rigid Charuco Board
The software detecting the charuco is expecting the board to be perfectly flat. To calibrate properly, make sure your board is mounted to something rigid, like a piece of cardboard or poster board.

## Recording Length
Taking time to record a longer calibration can help reduce your chances of a failed calibration. We recommend spending 5-10 seconds displaying the board to each pair of cameras. 

At 30fps, that should result in about 200 shared views of the board for each camera pair.

## Glare
Glare from the sun or a bright light can obscure the charuco pattern and prevent the software from recognizing the charuco board. It can be helpful to tilt te board up and down while showing it to the cameras in order to ensure each camera has views of the board without glare.

## Missing Shared Views
Each camera must not only see the charuco board during calibration, but must share a view of the charuco board with another camera. It's best to avoid overly wide angles between cameras. As long as each camera is connected to each other camera by some combination of shared views with other cameras, the calibration can work.

## Reversed Images
Reversed or mirrored images, like those recorded from some front-facing cameras on mobile phones, will prevent the software from recognizing the charuco board. 

Some phones will allow you to turn off image mirroring in the settings, but if not you may have to switch to using the rear camera.

## Common Error Messages


### `ValueError: not enough values to unpack (expected 2, got 0)`
```
freemocap_anipose.py", line 1810, in calibrate_rows
    objp, imgp = zip(*mixed)
    ^^^^^^^^^^
ValueError: not enough values to unpack (expected 2, got 0)
```
This issue comes up when one or more cameras do not have any shared views of the charuco with other cameras. This can due to the physical setup of your cameras. Make sure each camera can clearly see the charuco board at the same time as another camera. This issue can also happen if a camera is not properly detecting a charuco board due to an issue like a mirrored view, glare, or a charuco board that's too small in the cameras view.
