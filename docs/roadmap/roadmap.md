---
comments: true
---

# Roadmap 

## In preparation for `v0.1.0 alpha GUI` release 
- [ ] Fix the Blender output
    - Probably going to build something based on the methods developed in @cgtinker's `BlendArMocap` add-on
      - [link to notes on this topic](https://github.com/freemocap/notes_plans_scratchpad/blob/main/works_in_progress_notes/2022-11-13_blender_addon.md)

- [ ] Fix the cameras
    - `alpha` GUI starts lagging after about 3 cameras on a fast PC because cameras are run by threads (which compete for CPU with the GUI, vs the pre-alpha where it was all Terminal)
    - Gonna implement a smarter method of connecting to cameras that involves splitting them across separate processes
    - got some promising stuff on `freemocap/fast-camera-capture`, it just needs some more testing and then we can implement it in the `GUI`

## Planned work **after** `v0.1.0 alpha GUI` release
- [ ] UI/UX Workflow improvements
- [ ] Improve and validate the post processing pipeline
    - Improve, streamline and develop validations/tests/diagnostics for: 
        - Gap-filling 
            - current method - Linear interpolation
        - Filtering 
            - current method - Zero-lag 4th order low-pass Butterworth filter with cut off at, like, 7Hz
        - Origin Align 
            - current method - a variety of things that don't work as well as I'd like, lol
            - Try to automatically place skeleton on origin with feet on 'ground' (i.e. the XY plane)            
- [ ] Add automated test suite (via GitHub Actions)
    - [ ] for folder structure (e.g. 'completeness')
    - [ ] for accuracy of post processing pipeline (e.g. 'kinematic diagnostics')
    - [ ] for camera recording quality (e.g. 'timestamp diagnostics')
    - 
- [ ] New architecture for `TUI Mothership` method to develop alongside the standalone QtGUI
    - Simple textual/TUI mothership terminal based app that launches `qt` wizards for each recording/processing stage
    - Basically:
      - it's just a simple launcher
      - we can ask contributors to develop add-ons/plug-ins/improvements via `QWidget` objects that can launch from a `widget.show()` method. 
      - That way we can test/develop new capactites and organize them via the TUI interface before trying to integrate into the core `freemocap` GUI
        - Kinda like a 'plug-in' system
        - Kinda like `pyqthgraph`'s `examples` thing
      - Keeps things nice and modular and easy to develop/collaborate
      - Lets higher XP folks make tools that Lower XP folks can use/test/learn!!



## The Road to Real-time

### Desired workflow

!!! take-note "NOTE - This is the *desired* workflow, not the *current* one lol"


#### Install and launch `FreeMoCap` software 
  - Go to `freemocap.org/downloads`
  - Download and install the latest version of `FreeMoCap` for your OS  
  - Run installation wizard 
  - Double click on Skelly icon and launch the GUI
#### Set up Cameras
  - Plug them into the PC
  - Set them up so they are pointing at the subject with sufficient lighting and overlapping fields of view
#### Calibrate capture volume
  - Show charuco board to each camera, each camera has shared views of the same board with at least one other cameras
#### Press 'record/stream' or whatever 
  - A little thing pops up with info/diagnostics about the stream (IP address, success rate, framerate on both sides, system load info, etc)
#### Connect to another 3d software (say `Blender`)
  - You see a rigged humanoid mesh pop up in a 3d viewport and the skeleton matches your movement (with max possible accuracy and min possible latency)

### Capacities needed
#### Install
- standalone installers for Windows, Mac and Linux
- downloadable from freemocap website
- auto-build and update versions via Github Actions
   
#### Core software

  - improve workflow and UX as much as possible
  - clean and sanitize skeleton output as much as possible
  - minimize/optimize/distribute computational load as much as possible (and provide users with 'Speed vs Accuracy' knob based on their needs (and try to automate this process like they do in video game?))
  - Handle camera synchronization/processing in real-time
  - Format skeleton in some intelligent way and stuff it into a Queue/PIPE that connects to a socket or something
#### External apps
- Blender/Unreal/Unity/Gadot (or whatever) opens a socket and listens for skeleton data
- Skeleton data drives some 3d human skeleton/model/avatar/whatever

#### And that's realtime baybee :sunglasses: :sparkles:

- That's the dream, anyway.

#### Expected timeline 
- "Soon" ¯\\\_(ツ)_/¯ 
