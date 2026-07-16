---
title: "LocationSimulatorOptions Structure Reference"
slug: "sdk-for-ios-navigate-structs-locationsimulatoroptions"
---

# LocationSimulatorOptions

<div class="declaration">

<div class="language">

``` highlight
public struct LocationSimulatorOptions : Hashable
```

</div>

</div>

Options to specify how the location simulator will behave.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24LocationSimulatorOptionsV11speedFactorSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-speedFactor" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-locationsimulatoroptions#sdk-for-ios-navigate-s-7heresdk24LocationSimulatorOptionsV11speedFactorSdvp" class="token"><code>speedFactor</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A factor to scale the speed. Useful to speed up (or down) the simulation. By default, the speed factor is 1.0, which is equal to the speed that one normally drives along each route segment without taking into account any traffic-related constraints. The default speed may vary based on the road geometry, road condition and other statistical data. Values above 1.0 will increase the speed, values below 1.0 will reduce the speed. For example, a value of 2.0 will double the speed.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var speedFactor: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24LocationSimulatorOptionsV20notificationIntervalSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-notificationInterval" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-locationsimulatoroptions#sdk-for-ios-navigate-s-7heresdk24LocationSimulatorOptionsV20notificationIntervalSdvp" class="token"><code>notificationInterval</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Interval between notifications. Defaults to 1 second. Note that `TimeInterval` accepts seconds as double, so 500 ms can be set as 0.5 s. Values less than 1 ms are not acceptable and the interval is raised to this minimum in object constructors.

  Note: This value does not affect <a href="sdk-for-ios-navigate-classes-locationsimulator">`LocationSimulator`</a> when created with a <a href="sdk-for-ios-navigate-classes-gpxtrack">`GPXTrack`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var notificationInterval: TimeInterval
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24LocationSimulatorOptionsV11speedFactor20notificationIntervalACSd_Sdtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-speedFactor-notificationInterval" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-locationsimulatoroptions#sdk-for-ios-navigate-s-7heresdk24LocationSimulatorOptionsV11speedFactor20notificationIntervalACSd_Sdtcfc" class="token"><code>init(speedFactor:</code><wbr></wbr><code>notificationInterval:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of this class.

  - Parameters

    - speedFactor: A factor to scale the speed. Useful to speed up (or down) the simulation. By default, the speed factor is 1.0, which is equal to the speed that one normally drives along each route segment without taking into account any traffic-related constraints. The default speed may vary based on the road geometry, road condition and other statistical data. Values above 1.0 will increase the speed, values below 1.0 will reduce the speed. For example, a value of 2.0 will double the speed.
    - notificationInterval: Interval between notifications. Defaults to 1 second. Note that `TimeInterval` accepts seconds as double, so 500 ms can be set as 0.5 s. Values less than 1 ms are not acceptable and the interval is raised to this minimum in object constructors.

    Note: This value does not affect <a href="sdk-for-ios-navigate-classes-locationsimulator">`LocationSimulator`</a> when created with a <a href="sdk-for-ios-navigate-classes-gpxtrack">`GPXTrack`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(speedFactor: Double = 1.0, notificationInterval: TimeInterval = 1000 * 0.001)
  ```

  </div>

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

