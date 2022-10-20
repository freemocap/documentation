

# FAQ
This is a Live Ongoing Draft

## Freemocap Project Info  

### **When will FreeMoCap Alpha launch?**

Our Alpha, which will be a streamlined and faster version of our pre-Alpha, will launch sometime the summer of 2022! (this is subject to change, but progress is promising :) )

### **Does FreeMoCap run in real-time?**

Not at the moment (writing this in June 2022). We know folks are excited for real-time! Real-time FreeMoCap will become easier to achieve once our Alpha is released, we'll have a better idea on the "road-to-real-time" at that point.

### **Does FreeMoCap work on pre-recorded videos?**

Yes! Start the RunMe() pipeline at Stage 2, and specify the folder containing the videos you wish to process.

### **What hardware does FreeMoCap require?**

There are no hardware requirements to run FreeMoCap, but the more powerful CPU/GPU you have, the faster FreeMoCap will run.

### **How accurate is Freemocap?**
1. [Here's a link to the current discussion on GitHub...](https://github.com/freemocap/freemocap/discussions/211)

[Here's a deeper explanation of this topic](Accuracy.md).

### **What OS does FreeMoCap run on?**

Currently, FreeMoCap only runs on Windows. Our Alpha release will have support for Windows, Mac and Linux.

### **Why does FreeMoCap have an AGPLv3 license?**

The AGPLv3 License most closely aligns with the goals of FreeMoCap: to create free motion capture for everyone who wants it. To learn more about this license, and to understand why most other software licenses aren't actually free, check out the "Preamble" of the License on from the Free Software Foundation

### **Is FreeMoCap a non-profit?**

Yes! FreeMoCap's Federal 501c3 tax exampt status is pending, for more information, see "Legal Status" on our "about us" webpage

### **How can I support the FreeMoCap Project?**

There are many ways to support our work:

Star our repo!
Follow us on your social media platforms of choice! ( our home page has links to majority of options )
Join our discord!
Share your freemocap recordings on social media/in discord and tag us!
Donate to The FreeMoCap Foundation!

---

## Freemocap Data 

### **What data types does FreeMoCap output?**

FreeMoCap outputs the calculated joint positions in an .npy file, and can also create a blender animation (.blend file) if you have blender installed & connected to FreeMoCap  

### **How do I interact with Freemocap Data?**
1.  [Here's an ipynb that converts the giant npy file that freemocap produces into a more manageable form...](https://discord.com/channels/760487252379041812/760489602917466133/1006245448933191820)
2. [Convert standard freemocap npy output to pandas.DataFrame csv files](https://github.com/freemocap/freemocap/blob/jon/npy_to_csv_ipynb/ipython_jupyter_notebooks/export_freemocap_npy_as_pandas_data_frame_csv.ipynb)

---

## Blener and freemocap
### **How do I get Blender to work with freemocap?**

---

## Calibration Considerations

### **I'm having calibration issues / charucco board questions**: 

1. [How to use previous calibration settings](https://discord.com/channels/760487252379041812/760489602917466133/995426530614329344)
2. [I am having a hard time getting FreeMoCap to recognize the charuco board...consider fiddling with these settings...](https://discord.com/channels/760487252379041812/760489602917466133/1005106418820587551)

### **How big does the charuco board need to be?**

1. [charucuSquareSize parameter...](https://discord.com/channels/760487252379041812/760489602917466133/991639791382823032)
2. [Can the Charuco Board be partially obscurred? Turns out yes it can...](https://discord.com/channels/760487252379041812/760489602917466133/1006407164186865694)

---

## Camera Considerations

### **How many cameras do you need to run FreeMoCap?**

We recommend at least 3 to get a good 3D calibration.

### **Physically connecting cameras to your computer** 
USB-C 3.1 vs USB 2.0? And do you use a USB hub to connect all the cameras?
1. [Avoid USB hubs...](https://discord.com/channels/760487252379041812/760489602917466133/1001865605927936061)
2. [I'm getting good results with Logitech C922 pro cameras...](https://discord.com/channels/760487252379041812/760489602917466133/1005071174994251796)

### **What kind of cameras should I use?**

1. The short answer is that it depends and you have many options.  Our team will either use [these USB webcams](https://www.amazon.com/Streaming-Microphone-Widescreen-Conferencing-Recording/dp/B082X91MPP) (easy set up but gives us less data) or we'll use GoPro's (more challending post production workflow, but gives us more data). 
2. [What resolution camera should I chose? 720? 1080?](https://www.amazon.com/Streaming-Microphone-Widescreen-Conferencing-Recording/dp/B082X91MPP)

### **Using GoPro's with freemocap**
1. Currently, we process these files in Adobe Premiere. [Here is a link to a tutorial on how we do this](https://drive.google.com/file/d/1npqiNffNQ1BAmZTQJeRDo0kouA1jQOMl/view?usp=sharing). We know that's not a free software, but it's the best tool we have access to right now. We are working on building these functions into the freemocap software. 
2. After you've synced and trimmed the original files, put them in a folder on your computer and feed that folder into the freemocap runme script so that it "looks" for those files when it begins. I Need to explain the file organization so people can set this up on their own. 

---
## Solutions to common error messages
Below are links to discussions in the discord channel about common errors installing and running freemocap.

* Install Errors:

    1. **The first thing to check if you're getting strange errors** / not able to get things up and running is to ensure you've set things up properly to begin with. Have you created a virtual environment for freemocap? Have you activated that environment? Ar you in that environment when you run freemocap? [Here are the install instructions from the github readme.](https://github.com/freemocap/freemocap#installation) 
    2. [these package versions have conflicting dependencies...](https://discord.com/channels/760487252379041812/760489602917466133/1006407164186865694)  

* I'm getting weird system / install errors**:
[Here's a link to a discord conversation about this](https://discord.com/channels/760487252379041812/760489602917466133/997279303098187857)

* TypeError: Descriptors cannot be created directly
    1.  https://discord.com/channels/760487252379041812/760489602917466133/983771678523936858

* Blender Errors:
    1.  [I'm having an issue exporting to Blender...](https://discord.com/channels/760487252379041812/760489602917466133/985287355344777216)
    2. [I'm having trouble creating Blender files...](https://discord.com/channels/760487252379041812/760489602917466133/981606000249430067)
    3.  https://discord.com/channels/760487252379041812/760489602917466133/987048594072830012
* Calibration Errors
    1. [IndexError: list index out of range...](https://discord.com/channels/760487252379041812/760489602917466133/984471465015529482) This hasn't been responded to on the discord channel yet...



---

