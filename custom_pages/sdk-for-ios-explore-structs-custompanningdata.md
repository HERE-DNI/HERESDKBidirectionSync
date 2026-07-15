---
title: "CustomPanningData Structure Reference"
slug: "sdk-for-ios-explore-structs-custompanningdata"
---

# CustomPanningData

<div class="declaration">

<div class="language">

``` highlight
public struct CustomPanningData : Hashable
```

</div>

</div>

This class contains all the information regarding the next angular panning element, including a new estimated audio cue duration, and a new set of initial and sweep angular angle, allowing the customization of the spatial audio trajectories for any type of notification, such as speed or merge warners, maneuvers or even roundabouts notifications. The orientation in space for <a href="sdk-for-ios-explore-structs-custompanningdata#/s:7heresdk17CustomPanningDataV23initialAzimuthInDegreesSdSgvp">`CustomPanningData.initialAzimuthInDegrees`</a> and <a href="sdk-for-ios-explore-structs-custompanningdata#/s:7heresdk17CustomPanningDataV21sweepAzimuthInDegreesSdSgvp">`CustomPanningData.sweepAzimuthInDegrees`</a> can be represented by the following angular values:

| Front | Right |  Rear  | Left |
|:-----:|:-----:|:------:|:----:|
|  0°   | +90°  | +- 180 | -90° |

When any of the members of `CustomPanningData` are initialized as null, the default value provided by HERE SDK will be used instead. The audio cue is spatialized considering the action of both maneuvers, for example, the audio cue ‘Now turn right and then turn left’ will be spatialized as following: ‘Now turn right’ will be heard as coming from the right. ‘and then turn left’ will be heard as coming from the left. Note: The estimation for playing both audio cues could be not fully accurate and therefore a mismatch between the audio source and the audio cue message could be perceived.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk17CustomPanningDataV25estimatedAudioCueDurationSdSgvp"></span>` `<span id="//apple_ref/swift/Property/estimatedAudioCueDuration" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-custompanningdata#/s:7heresdk17CustomPanningDataV25estimatedAudioCueDurationSdSgvp" class="token"><code>estimatedAudioCueDuration</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Customized estimated duration for playing the audio cue on the selected TTS Engine. When not used, HERE SDK’s estimation will be used instead.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var estimatedAudioCueDuration: TimeInterval?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17CustomPanningDataV23initialAzimuthInDegreesSdSgvp"></span>` `<span id="//apple_ref/swift/Property/initialAzimuthInDegrees" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-custompanningdata#/s:7heresdk17CustomPanningDataV23initialAzimuthInDegreesSdSgvp" class="token"><code>initialAzimuthInDegrees</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Initial desired angular position of the upcoming audio cue. For example, for a maneuver such as “Turn right on” (`ManeuverAction.RightTurn`) we want to create a spatial audio arc from the front to the right, mimicking the maneuver geometry. In this case, it is good practice to start the trajectory from an initial azimuth that is slightly located on the opposite direction of the maneuver (e.g. slightly starting from “front-left”) and terminate the trajectory fully on the right side. The initial azimuth angle of such a trajectory would be, for example, -5.0 (slightly front-left). This azimuth value is needed to set the position of the audio renderer before starting to play the audio cue to avoid unwanted audio “jumps”.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var initialAzimuthInDegrees: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17CustomPanningDataV21sweepAzimuthInDegreesSdSgvp"></span>` `<span id="//apple_ref/swift/Property/sweepAzimuthInDegrees" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-custompanningdata#/s:7heresdk17CustomPanningDataV21sweepAzimuthInDegreesSdSgvp" class="token"><code>sweepAzimuthInDegrees</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sweep angle of the upcoming audio cue. For example, for a maneuver such as “Turn right on” (i.e. `ManeuverAction.RightTurn`), within an `initial_azimuth_in_degrees` of -5 degrees, we want to create a spatial audio arc trajectory from the front to the right, mimicking the maneuver geometry. In this case, the desired final angle would be +90 degrees, and therefore, a sweep angle of +95 degrees would be required. On the other hand, when the desired spatialization is to the left side (i.e. `ManeuverAction.LeftTurn`), the `initial_azimuth_in_degrees` could be set to +5 degrees and the `sweep_azimuth_in_degrees` to -95 degrees

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var sweepAzimuthInDegrees: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(estimatedAudioCueDuration: initialAzimuthInDegrees: sweepAzimuthInDegrees: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( estimatedAudioCueDuration : TimeInterval ? = nil , initialAzimuthInDegrees : Double ? = nil , sweepAzimuthInDegrees : Double ? = nil )
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

