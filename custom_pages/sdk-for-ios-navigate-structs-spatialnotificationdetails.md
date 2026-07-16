---
title: "SpatialNotificationDetails Structure Reference"
slug: "sdk-for-ios-navigate-structs-spatialnotificationdetails"
---

# SpatialNotificationDetails

<div class="declaration">

<div class="language">

``` highlight
public struct SpatialNotificationDetails : Hashable
```

</div>

</div>

This class provides all the information for a spatial text notification, including the maneuver data and extra data which is required to set the direction of spatialization of the audio cue.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk26SpatialNotificationDetailsV23initialAzimuthInDegreesSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-initialAzimuthInDegrees" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-spatialnotificationdetails#sdk-for-ios-navigate-s-7heresdk26SpatialNotificationDetailsV23initialAzimuthInDegreesSdvp" class="token"><code>initialAzimuthInDegrees</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Initial desired angular position of the upcoming audio cue. For example, for a maneuver such as “Turn right on” (`ManeuverAction.RightTurn`) we want to create a spatial audio arc trajectory from the front to the right, mimicking the maneuver geometry. In this case, it is good practice to start the trajectory from an initial azimuth that is located slightly on the opposite direction of the maneuver (e.g. slightly starting from “front-left”) and terminate the trajectory fully on the right side. The initial azimuth angle of such a trajectory would be, for example, -5.0 (slightly front-left). This azimuth value is needed to set the position of the audio renderer before starting to play the audio cue to avoid unwanted audio “jumps”. The orientation in space for `SpatialNotificationDetails.initialAzimuthInDegrees` can be represented by the following angular values:

  | Front | Right |  Rear  | Left |
  |:-----:|:-----:|:------:|:----:|
  |  0°   | +90°  | +- 180 | -90° |

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var initialAzimuthInDegrees: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk26SpatialNotificationDetailsV15audioCuePanningAA0b5AudiofG0Cvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-audioCuePanning" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-spatialnotificationdetails#sdk-for-ios-navigate-s-7heresdk26SpatialNotificationDetailsV15audioCuePanningAA0b5AudiofG0Cvp" class="token"><code>audioCuePanning</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Object to start the angular panning when spatialization of the text notification is desired

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var audioCuePanning: SpatialAudioCuePanning
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-spatialaudiocuepanning">SpatialAudioCuePanning</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk26SpatialNotificationDetailsV25estimatedAudioCueDurationSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-estimatedAudioCueDuration" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-spatialnotificationdetails#sdk-for-ios-navigate-s-7heresdk26SpatialNotificationDetailsV25estimatedAudioCueDurationSdvp" class="token"><code>estimatedAudioCueDuration</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Estimation of the required time to play an audio cue at speech rate 1.0. For example the cue “Turn right on Name-Of-A-Street” will playback over an X number of milliseconds. Therefore, an estimation of this audio cue duration is needed to correctly sync the movement of sound to the cue (so that audio movement and audio duration match).

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var estimatedAudioCueDuration: TimeInterval
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk26SpatialNotificationDetailsV23initialAzimuthInDegrees15audioCuePanning014estimatedAudioJ8DurationACSd_AA0bmjK0CSdtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-initialAzimuthInDegrees-audioCuePanning-estimatedAudioCueDuration" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-spatialnotificationdetails#sdk-for-ios-navigate-s-7heresdk26SpatialNotificationDetailsV23initialAzimuthInDegrees15audioCuePanning014estimatedAudioJ8DurationACSd_AA0bmjK0CSdtcfc" class="token"><code>init(initialAzimuthInDegrees:</code><wbr></wbr><code>audioCuePanning:</code><wbr></wbr><code>estimatedAudioCueDuration:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance.

  - Parameters

    - initialAzimuthInDegrees: Initial desired angular position of the upcoming audio cue. For example, for a maneuver such as “Turn right on” (`ManeuverAction.RightTurn`) we want to create a spatial audio arc trajectory from the front to the right, mimicking the maneuver geometry. In this case, it is good practice to start the trajectory from an initial azimuth that is located slightly on the opposite direction of the maneuver (e.g. slightly starting from “front-left”) and terminate the trajectory fully on the right side. The initial azimuth angle of such a trajectory would be, for example, -5.0 (slightly front-left). This azimuth value is needed to set the position of the audio renderer before starting to play the audio cue to avoid unwanted audio “jumps”. The orientation in space for <a href="sdk-for-ios-navigate-structs-spatialnotificationdetails#sdk-for-ios-navigate-s-7heresdk26SpatialNotificationDetailsV23initialAzimuthInDegreesSdvp">`SpatialNotificationDetails.initialAzimuthInDegrees`</a> can be represented by the following angular values:

    \| Front \| Right \| Rear \| Left \| \|:—-:\|:—-:\|:—-:\|:—-:\| \| 0° \| +90° \| +- 180 \| -90° \|

    - audioCuePanning: Object to start the angular panning when spatialization of the text notification is desired
    - estimatedAudioCueDuration: Estimation of the required time to play an audio cue at speech rate 1.0. For example the cue “Turn right on Name-Of-A-Street” will playback over an X number of milliseconds. Therefore, an estimation of this audio cue duration is needed to correctly sync the movement of sound to the cue (so that audio movement and audio duration match).

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(initialAzimuthInDegrees: Double, audioCuePanning: SpatialAudioCuePanning, estimatedAudioCueDuration: TimeInterval)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-spatialaudiocuepanning">SpatialAudioCuePanning</a>

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-navigate-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

