# Hardware/Software Requirements

## 1. Required Equipment

The absolute minimum required equipment is a computer with a single camera on it. Even a simple laptop with a built-in camera can be used to create a single-camera recording. However, single-camera recordings will not produce reliable 3D estimates but will produce solid two-dimensional tracking, suitable for 2D animators. To get a viable multi-camera recording that will produce reliable estimates of 3D movement, users will need at least two cameras (one of which could be the laptop camera), however we recommend using three cameras for better results.

These cameras should be connected directly to the computer's USB ports. We are working on support for using multiple cameras through a single USB hub, but for now, we recommend plugging the cameras straight into the computer for better results. For 3D reconstructions, users will also need to print out a Charuco board for the calibration process, which will be described in greater detail in the calibration section.

You might find it helpful to have USB extension cables and tripods to set up their webcams in a way that will allow them to get a good recording, but these are not necessary, just convenient.

## 2. Necessary Software

All of the packages needed for reconstructing movement data are included in the FreeMoCap software, with the exception of Blender, which is a free software that we recommend downloading from [https://blender.org](https://blender.org). Blender will be used at the end of the reconstruction process to create a Blender scene. If users want to explore the Jupyter notebooks generated with each recording, they'll need to install either VS Code or JupyterLab, and we can provide links to those resources.

For now, the only way to install FreeMoCap is through a terminal, and we recommend using a virtual environment management software like Anaconda. Soon, we will include an option for downloading the software directly from the website. We'll have a section for the installation process and standard troubleshooting in another section.
