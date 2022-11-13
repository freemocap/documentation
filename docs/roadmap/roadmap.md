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
- [ ] Improve and validate the post processing pipeline
    - Improve, streamline and develop diagnostics for: 
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
- [ ] New architecture for `v0.2.0 TUI Mothership` realease
    - [ ] Simple textual/TUI mothership terminal based app that launches `qt` wizards for each recording/processing stage
    - [ ] built from central parameter dict/yaml/json

