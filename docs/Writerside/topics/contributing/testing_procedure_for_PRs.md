
# Testing Steps for FreeMoCap
These steps are primarily made to test:
1. Starting a brand new recording from scratch and making sure it works
2. Reprocessing an existing recording and making sure it works
3. Running the pipeline from all the different stages to make sure that file loading and processing works as intended

## I. Single camera recording  
1. Record and process a single camera recording in full (meaning you get a Blender output)

## II. Sample/test data
1. Download and process either the sample or test data in full 

## III. Record and run a multi-camera recording
1. Record a calibration
2. Make a multi-camera recording
3. Process the recording in full

## IV. Load in an existing session
- Use this to test in the pipeline in different stages, to ensure you can run it from any point in the pipeline
- Bonus points if you load an existing session that was processed with a previous version of FreeMoCap, to make sure there are no version-related conflicts when it comes to processing
1. Check that the session loaded correctly (check the active recording directory)
1. Run from 2D image tracking onwards
2. Run from 3D triangulation onwards
3. Run from post-processing onwards 
4. Use the 'Export to Blender' button 

## V. Import video
1. Import any set of videos (can just use existing ones from a synchronized recording) and run in full 

