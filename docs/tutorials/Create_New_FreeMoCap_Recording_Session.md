
 #  HOW TO CREATE A *NEW* `FreeMoCap` RECORDING SESSION

In order to follow this tutorial, you'll need to have already successfully [installed the software.](Freemocap_Software_Installation.md)

*This tutorial will use the pre-alpha version of freemocap and (version 0.0.54) to record the synchronized videos and then load them into the alpha version of freemocap to process them. That's just the status of things for now folks. We'll update things as they change. 

## Setting Up your Equipment

You'll want to set up your cameras in a semi circle such that their fields of view are partially overlapping. That overlapping field of view is going to define what's called the **"Capture Volume"**, which is the 3D space in the room that you can get a good recording of someone doing something. So, what ever action you're recording, each camera needs to have that person in its view. 

### **How far away should the cameras be from the person you're recording?** 
- This really depends on the space you're recording in and the activity you plan to record. You'll want each camera generally as close as possible (to get as much data as you can) **BUT** you also need each camera to be set up far enough away such that they can capture the entire body of the person they're recording. Keep in mind the action the person is doing, if they're reaching their arms out, or jumping, or moving side to side, your cameras need to be able to see all of the person the entire time throughout the recording. 

This software doesn't handle incomplete bodies very well at the moment. 

**Some other helpful considerations:** 
- If possible, it's helpful for the background of the recording to be as visually simple as possible (a white wall, or a white sheet covering up your aweseom art on the wall). This will remove visual complexities and improve the trackability of the movement. 
- If there are any mirrors around, cover those up or remove them. 
- It's helpful (but not necessary) to be in a room where you have some control over lighting (dimmers, blinds, curtains, etc). 
- Avoid having shadows in your recording space. 

You'll do some final tweaking of the camera orientation as you go through the calibration process below. 

---

## Calibration

### **1.) Open the Freemocap GUI**

This process is a little jenky right now, we're working to clean this up, but here it is. 

Open up the terminal and activate the freemocap-gui environment. You created this environment when you installed the software, according to [this tutorial](Freemocap_Software_Installation.md).
```
(base) $ conda activate freemocap-gui
(freemocap-gui)
```
Now you'll need to point your terminal towards whichever location you git cloned the repository to when you followed the [sofware installation tutorial](Freemocap_Software_Installation.md). If you forgot, locate the freemocap folder on your machine (it's a folder called freemocap) and then copy the folder path. Then you can paste it into the terminal using the command 'cd' before it. 
```
(freemocap-gui) $ cd freemocap
```
Now you'll run the .py file that will start the alpha GUI. 
```
(freemocap-gui) python src/gui/main/main.py
```
And there you have it, the alpha GUI should pop up in its own window on your machine. 

### **2.) Create New Session:**

On the GUI, click the "Create New Session" Button. 
 
## Recording movement
## 
