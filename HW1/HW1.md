# <center>CS5100 HW1</center>
<center>Yuchao Su</center>

### 1.
| Agent Type | Performance | Environment | Actuators | Sensors |
| :--------: | :---------: | :---------: | :--------:| :-----: |
|  Soccer Agent  | Goal, win the game | Court, ball, referee, other player, audiences | Kicking, steering, accelorator | Camera, wheel encoder, gyroscope (orientation) |
| Sweater knitting bot  |  |  |
| High jumping bot|
| Online book shopping bot | Low expense, high accuracy on books |  |
### 2.
#### a. 
State:
Initial State: No regions on the map is assigned a color.

Actions: Assign a color to a region.

Transition model:

Goal test: All regions are assigned a color, and no two adjacent region has the same color.

Path cost:The number of unassigned region -1.
#### b.
State:
Initial State: The monkey can not get the bananas and has two crates.

Actions: On a crate, off a crate, put a crate on the other, on the second crate, from first crate to the second crate.

Transition model:

Goal test: The monkey get the bananas.

Path cost:The number of unassigned region -1.
### 3.
### 4.
### 5.
### 6.
### 7.
### 8.