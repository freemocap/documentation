# Data Format

During a recording, FreeMoCap outputs numerous files. Some are formatted for easy use in other programs, while some are primarily used as intermediary steps during processing. FreeMoCap keeps all the files created during processing, which allows you to restart processing from any part of the pipeline, and gives you fine-grained control of what output data you use. All the files from a recording session are saved to the recording folder (see the [Freemocap Data Folder Guide](freemocap_data_folder_guide.md)).

You can see the layout of a FreeMoCap recording session below:
```
freemocap_sample_data
├── annotated_videos
├── freemocap_sample_data.blend
├── freemocap_sample_data.ipynb
├── freemocap_sample_data_by_frame.json
├── freemocap_sample_data_by_trajectory.csv
├── freemocap_sample_data_camera_calibration.toml
├── freemocap_sample_data_frame_name_xyz.npy
├── output_data
├── saved_data
└── synchronized_videos
```

The contents of the folder described here are for a complete recording. Depending on your processing parameters, or if you encounter an error during processing, some of these files may be missing.

>To get a copy of the sample data to follow along with this guide, you can:
>1. Open FreeMoCap
>2. Go to Data in the menu bar
>3. Select `Download Sample Data`
>4. Process the sample data by clicking `Process Motion Capture Videos` in the `Process Data` tab
>5. Navigate to `freemocap_data/recording_sessions/freemocap_sample_data`


## Top Level Files
The top level files in a recording folder, or the files that aren't in a subfolder, are the recommended outputs. These files contain the fully processed data, and formatted for easy use in other programs. FreeMoCap provides this final data in the form of `.npy`, `.csv`, and .`json` files, covering the most common data formats. In addition to the data files, the top level of the recording folder contains output files to help you directly view and use your data. These include a `.blend` file for displaying and animating your data, and a `.ipynb` notebook to guide you through interacting with your data in Python.

### Data Files
`freemocap_sample_data_frame_name_xyz.npy` is a numpy data array, where the first dimension is the frame number, the second dimension is the keypoint, and the third dimension is the xyz location of the keypoint. 

`freemocap_sample_data_by_trajectory.csv` is comma separated values file, where each column is a trajectory of a keypoint in one dimension, and each row is a frame. The first two columns are `timestamp` and `timestamp_by_camera`, giving the timestamps for each frame if they're available. The rest of the columns are the trajectory of each tracked keypoint, split into a column for each xyz dimension. The column names look like `body_nose_x`, `right_forearm_y`, and `full_body_com_z`.

`freemocap_sample_data_by_frame.json` gives the data in JavaScript Object Notation and provides additional metadata. The first field is `info`, which contains the tracked point schema under `schema`. This provides a `proximal` and `distal` keypoint for each keypoint in the schema. These can be used to recreate the skeleton connections used by the tracking model. The other primary field is `data_by_frame`, which contains a field for each frame number. Each frame then contains a `timestamps` field with `mean` and `by_camera`, and a `tracked_points` field. The `tracked_points` field contains a field for each point with `x`, `y`, and `z` fields.

### Output Files

`freemocap_sample_data.blend` is a Blender file that is the primary output visualization of FreeMoCap. It shows a mesh of our mascot Skelly driven by your data, in front of the annotated videos from the recording. This is also the starting point for using FreeMoCap data for animation.

`freemocap_sample_data.ipynb` is a Python notebook that shows you interactively how to use your data in Python. It covers importing necessary modules, loading your data, plotting individual joint trajectories, and plotting the 3d data.

`freemocap_sample_data_camera_calibration.toml` is the calibration file used to process the recording. This is necessary for reprocessing the data, and can be useful in debugging quality issues in your data.

## Synchronized and Annotated Videos

There are two folders of videos accompanying each recording, `synchronized_videos` and `annotated_videos`. 

The `synchronized_videos` folder contains the videos that are used to run the motion capture pipeline. They are synchronized in that they each have the exact same number of frames. The synchronized videos and the `calibration.toml` are the input data that FreeMoCap uses to get motion capture data. You can always reprocess a recording if you have the `synchronized videos` and `calibration.toml`.

The `annotated_videos` folder contains videos produced during processing. These videos are annotated with the pose estimation output, and are useful for diagnosing the quality of the 2D image data that the 3D data is triangulated from. The annotated videos are also synchronized, but should not be used as input for processing, as the annotations will interfere with the pose estimation models.

## Output Data folder

```
freemocap_sample_data/output_data
├── center_of_mass
│   ├── mediapipe_segmentCOM_frame_joint_xyz.npy
│   └── mediapipe_total_body_center_of_mass_xyz.npy
├── mediapipe_body_3d_xyz.csv
├── mediapipe_body_3d_xyz.npy
├── mediapipe_face_3d_xyz.csv
├── mediapipe_face_3d_xyz.npy
├── mediapipe_left_hand_3d_xyz.csv
├── mediapipe_left_hand_3d_xyz.npy
├── mediapipe_right_hand_3d_xyz.csv
├── mediapipe_right_hand_3d_xyz.npy
├── mediapipe_rigid_bones_3d.npy
├── mediapipe_skeleton_3d.npy
├── raw_data
│   ├── mediapipe_2dData_numCams_numFrames_numTrackedPoints_pixelXY.npy
│   ├── mediapipe_3dData_numCams_numFrames_numTrackedPoints_reprojectionError.npy
│   ├── mediapipe_3dData_numFrames_numTrackedPoints_reprojectionError.npy
│   └── mediapipe_3dData_numFrames_numTrackedPoints_spatialXYZ.npy
└── recording_parameters.json
```

## Saved Data Folder

```
freemocap_sample_data/saved_data
├── _BONE_AND_JOINT_DATA_README.md
├── _FREEMOCAP_DATA_README.md
├── all_trajectories.csv
├── csv
│   ├── body_trajectories.csv
│   ├── center_of_mass_trajectories.csv
│   ├── face_trajectories.csv
│   ├── left_hand_trajectories.csv
│   └── right_hand_trajectories.csv
├── freemocap_sample_data_bone_and_joint_data.csv
├── info
│   ├── freemocap_data_handler.pkl
│   ├── metadata.json
│   └── trajectory_names.json
└── npy
    ├── all_frame_name_xyz.npy
    ├── body_frame_name_xyz.npy
    ├── center_of_mass_frame_name_xyz.npy
    ├── face_frame_name_xyz.npy
    ├── left_hand_frame_name_xyz.npy
    └── right_hand_frame_name_xyz.npy
```