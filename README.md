# Modified Structure Function (MSF) algorithm

## Where MSF is used?
Dynamic speckle imaging (DSI) enables visualization of speed distribution for processes that occur in a controlled object and lead to micro-changes of its relief. 
Method is used in such fields as non-destructive testing, estimation of blood flow, measurement of bacterial response, observation of processes in plants,
food quality assessment, drying of paints, fire detection and etc.

Images that show activity distribution within controlled object are called ***activity maps***. Below are shown some examples.

**Blod flow estimation**   | **Non-destructive testing**| **Paint drying estimation**
:-------------------------:|:-------------------------:|:-------------------------:
 <img src="/Readme images/example1.png" alt="example" width="200"/>|<img src="/Readme images/example2.png" alt="example" width="200"/>|<img src="/Readme images/example3.png" alt="example" width="220"/>

## How to calculate activity maps?
Before obtaining activity maps, we have to capture speckle images. Setup for capturing images is shown below. It consists of vibration-isolated table, laser, laser expander and camera, connected to PC or laptop.

<img src="/Readme images/speckle_setup.png" alt="example" width="300"/>

Speckle image may look like this, for instance

<img src="/Readme images/speckle image.png" alt="example" width="300"/>

There are many algorithms to calculate activity maps, for instance, Laser Speckle Contrast Analysis (LACSA), Generalized Differences (GD), Fuji Algorithm and etc. In this code Modified Stucture Function algorithm is implemented as it is faster, more sensitive and calculated maps have better spatial resolution, comparing to other methods. Idea is to analize **N** correlated in time speckle images, consecutively captured with constant time interval. 

<img src="/Readme images/algorithm 2 .png" alt="example" width="1000"/>
 
