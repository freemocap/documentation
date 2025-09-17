# Multiprocessing Setup

The multiprocessing option allows you to process multiple videos at the same time, decreasing the total processing time. Each process runs in a separate CPU core. You can set the number of CPU cores to use by changing the "Max Number of Processes to Use" option in the "2d Image Trackers" parameter group. The default is the maximum number of cores on your machine minus one, to account for the process the GUI is running in. In the example below, the machine has 8 cores total, and 7 show up as available. Freemocap will never create more processes than the number of videos in your active recording. If you would like to turn off multiprocessing entirely, you can set the "Max Number of Processes to Use" to one. 


![MultiProcessing Parameter Screenshot](multiprocessing_crop_detail.png){ width="450" }