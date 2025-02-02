# Writeup: Track 3D-Objects Over Time

### 1. Write a short recap of the four tracking steps and what you implemented there (filter, track management, association, camera fusion). Which results did you achieve? Which part of the project was most difficult for you to complete, and why?

In step 1, I implemented Extended Kalman Filter. I implemented matrices used in Kalman Filter such as F, Q, and also implemented update and prediction. The position of a single vehicle was successfully tracked.

![RMSE plot](step1.png)

In step 2, I implemented track management. I implemented track score update and track state update, so that a new vehicle will be recognized after a few frames and similarly a disappering vehicle will be dropped in a few frames. The track state and the score of a single vehicle were successfully updated.

![RMSE plot](step2.png)

In step 3, I implemented association. I applied Mahalanobis distance and gating to associate measurements to tracks. The positions of multiple vehicles were successfully tracked.

![RMSE plot](step3.png)

In step 4, I implemented camera fusion. I implemented h(x) for camera measurements so that they can update the state of EKF. Also I implemented FoV so that tracks not visible from a certain censor because it's outside the field of view do not trigger track score updates. The positions of multiple vehicles were successfully tracked by using both camera and lidar.

![RMSE plot](step4.png)

The last step was the most difficult part, because at first my implementation of gating in step 3 was incomplete, and that caused an unexpected result in step 4, but it was not easy to debug that issue.

Notes for resubmission (October 31): I fixed bugs in trackmanagement.py based on feedback and updated RMSE plots 2 to 4.


### 2. Do you see any benefits in camera-lidar fusion compared to lidar-only tracking (in theory and in your concrete results)? 

In theory camera lidar fusion should improve the overall detection accuracy and complement the other sensor's weakness. In practice, tracks sometimes have slightly higher RMSE in step 4 than in step 3, so naive camera integration alone may actually result in worse results.

### 3. Which challenges will a sensor fusion system face in real-life scenarios? Did you see any of these challenges in the project?

In the project, I experienced vehicles in the parting lot causing confusion in the sensor fusion. Many of them are overlapped and barely visible to humans so ideally they should be ignored. In the project, the combination of gating and the fact only lidar is used to creating a new track worked around the issue, but in the real-life system camera observations may be used for creating new tracks as well, and the issue might be surfaced.


### 4. Can you think of ways to improve your tracking results in the future?

In the project the width and length of a camera measurement were not used. By taking account of them in EKF, we might be able to mitigate some of the weaknesses of the current implementation such as when there are multiple overlapping vehicles in a single frame.
