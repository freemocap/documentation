# Basic Workflow

0. [Prerequisites for Using FreeMoCap](./software_hardware_prerequisites.md)
1. [Installation](./Installation.md)
2. [Making your first Skelly - Single-Camera Recording](./single_camera_recording.md)
3. [Advanced skeleton wrangling - Multi-Camera Calibration Guide](./multi_camera_calibration.md)

Bonus -  [Getting a good recording - Setting up your recording environment](/)



## Basic Work flow
``` mermaid
graph TD
    A1(1. Installation)
    A1-->A(Create New Recording)
    A --if single camera---> B(Record Videos)
    A -- if multiple cameras ---> C(Calibrate Capture Volume)    
    C --> B    
    B --> F(3D Reconstruction)    
    F --> H(Post Processing)
    H --> I(Visualization)
```

