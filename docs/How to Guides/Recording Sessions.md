# How to Guides

## HOW TO REPROCESS A PREVIOUSLY RECORDED `FreeMoCap` RECORDING SESSION

You can re-start the processing pipeline from any of the following processing stages (defined below)by specifying the `SessionID` desired `stage` in the call to `freemocap.RunMe()`

So to process the session named `sesh_2021-11-21_19_42_07` starting from stage 3 (aka, skipping the `1- recording` and `2- synchronization` stages), run:
```python
import freemocap
freemocap.RunMe(sessionID="sesh_2021-11-21_19_42_07", stage=3)
```

Note - if you leave `sessionID` unspecified but set `stage` to a number higher than 1, it will attempt to use the last recorded session (but this can be buggy atm)