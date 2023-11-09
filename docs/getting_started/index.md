``` mermaid
graph TD
    A1(Installation)
    A1-->A(Create New Recording)
    A --if single camera---> B(Record Videos)
    A -- if multiple cameras ---> C(Calibrate Capture Volume)    
    C --> B    
    B --> F(3D Reconstruction)    
    F --> H(Post Processing)
    H --> I(Visualization)
```

