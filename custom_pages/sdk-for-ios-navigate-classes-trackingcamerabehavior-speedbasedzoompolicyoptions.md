---
title: "SpeedBasedZoomPolicyOptions Structure Reference"
slug: "sdk-for-ios-navigate-classes-trackingcamerabehavior-speedbasedzoompolicyoptions"
---

# SpeedBasedZoomPolicyOptions

<div class="declaration">

<div class="language">

``` highlight
public struct SpeedBasedZoomPolicyOptions
```

</div>

</div>

Configuration for computing zoom levels from speed thresholds defined per road classification. For correct default initialization, use <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC34defaultSpeedBasedZoomPolicyOptionsAC0fghiJ0VyFZ">`TrackingCameraBehavior.defaultSpeedBasedZoomPolicyOptions(...)`</a>.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC27SpeedBasedZoomPolicyOptionsV28delayBetweenThresholdChangesSdSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-delayBetweenThresholdChanges" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior-speedbasedzoompolicyoptions#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC27SpeedBasedZoomPolicyOptionsV28delayBetweenThresholdChangesSdSgvp" class="token"><code>delayBetweenThresholdChanges</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Minimum time interval that must pass before the zoom level is allowed to switch to a new speed threshold. If <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC34defaultSpeedBasedZoomPolicyOptionsAC0fghiJ0VyFZ">`TrackingCameraBehavior.defaultSpeedBasedZoomPolicyOptions(...)`</a> is not used for `TrackingCameraBehavior.SpeedBasedZoomPolicyOptions`, it will be `nil`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var delayBetweenThresholdChanges: TimeInterval?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC27SpeedBasedZoomPolicyOptionsV020roadClassificationToE9ThresholdSDyAA04RoadK0OSayAC0eM0VGGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-roadClassificationToSpeedThreshold" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior-speedbasedzoompolicyoptions#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC27SpeedBasedZoomPolicyOptionsV020roadClassificationToE9ThresholdSDyAA04RoadK0OSayAC0eM0VGGvp" class="token"><code>roadClassificationToSpeedThreshold</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines, per road classification, how the zoom level should change in response to different vehicle speeds. If <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC34defaultSpeedBasedZoomPolicyOptionsAC0fghiJ0VyFZ">`TrackingCameraBehavior.defaultSpeedBasedZoomPolicyOptions(...)`</a> is not used for `TrackingCameraBehavior.SpeedBasedZoomPolicyOptions`, it will be an empty map.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var roadClassificationToSpeedThreshold: [RoadClassification : [TrackingCameraBehavior.SpeedThreshold]]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-roadclassification">RoadClassification</a>
  - <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior">TrackingCameraBehavior</a>
  - <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior-speedthreshold">SpeedThreshold</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC27SpeedBasedZoomPolicyOptionsV28delayBetweenThresholdChanges020roadClassificationToeL0AESdSg_SDyAA04RoadO0OSayAC0eL0VGGtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-delayBetweenThresholdChanges-roadClassificationToSpeedThreshold" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior-speedbasedzoompolicyoptions#sdk-for-ios-navigate-s-7heresdk22TrackingCameraBehaviorC27SpeedBasedZoomPolicyOptionsV28delayBetweenThresholdChanges020roadClassificationToeL0AESdSg_SDyAA04RoadO0OSayAC0eL0VGGtcfc" class="token"><code>init(delayBetweenThresholdChanges:</code><wbr></wbr><code>roadClassificationToSpeedThreshold:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance.

  Note: This is a beta feature; there maybe bugs and unexpected behavior. Related API’s are subject to change without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(delayBetweenThresholdChanges: TimeInterval? = nil, roadClassificationToSpeedThreshold: [RoadClassification : [TrackingCameraBehavior.SpeedThreshold]] = [:])
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-roadclassification">RoadClassification</a>
  - <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior">TrackingCameraBehavior</a>
  - <a href="sdk-for-ios-navigate-classes-trackingcamerabehavior-speedthreshold">SpeedThreshold</a>

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

