# freemocap blender addon 

[![hackmd-github-sync-badge](https://hackmd.io/KZ3coCS0RTGWGlwfNHFiuA/badge)](https://hackmd.io/KZ3coCS0RTGWGlwfNHFiuA)


## Strategy
- Based on fork of - https://github.com/cgtinker/blendarmocap
1. figure out what was happening on `freemocap` branch of above
2. Revert to `main` branch, then build new `freemocap-auto-blender-output` script based on `main.py`

TO DO 
- [ ] auto-download sample data
- [x] why skelly face down? 
    - b/c he swaps XYZ -> -XZ-Y in the `body, hand, face _processing.py` files
- [-] don't load live
    - can replace`load_freemocap` with better version (the existing one hijacks the `holistic` processor, and that's not necessary)
- [ ] load body hands and face separately
- [ ] bind other parts of rig to data
- [ ] Remove hard-coded numbers in the `processing` functions  e.g. `pose_processing.py Line214`