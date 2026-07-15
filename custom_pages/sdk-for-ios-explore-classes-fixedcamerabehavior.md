---
title: "FixedCameraBehavior Class Reference"
slug: "sdk-for-ios-explore-classes-fixedcamerabehavior"
---

# FixedCameraBehavior

<div class="declaration">

<div class="language">

``` highlight
public class FixedCameraBehavior : CameraBehavior
```

``` highlight
extension FixedCameraBehavior: NativeBase
```

``` highlight
extension FixedCameraBehavior: Hashable
```

</div>

</div>

Use this class to follow the current location of the user: The camera will permanently look at the target location that was fed into the navigator instance. Since location updates happen in discrete intervals, locations in-between will be interpolated to achieve a smooth camera movement.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

      init()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of this class.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ()
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19FixedCameraBehaviorC24normalizedPrincipalPointAA8Anchor2DVvp"></span>` `<span id="//apple_ref/swift/Property/normalizedPrincipalPoint" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-fixedcamerabehavior#/s:7heresdk19FixedCameraBehaviorC24normalizedPrincipalPointAA8Anchor2DVvp" class="token"><code>normalizedPrincipalPoint</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The normalized principal point. Normalized principal point to be used during navigation. Defaults to (0.5, 0.775), which means the camera will use the position slightly at the bottom of the mapview.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var normalizedPrincipalPoint: Anchor2D { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19FixedCameraBehaviorC22cameraDistanceInMetersSdvp"></span>` `<span id="//apple_ref/swift/Property/cameraDistanceInMeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-fixedcamerabehavior#/s:7heresdk19FixedCameraBehaviorC22cameraDistanceInMetersSdvp" class="token"><code>cameraDistanceInMeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Camera distance to current location. The default value is 150 meters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use `FixedCameraBehavior.zoom` instead.") public var cameraDistanceInMeters : Double { get set }
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19FixedCameraBehaviorC4zoomAA10MapMeasureVvp"></span>` `<span id="//apple_ref/swift/Property/zoom" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-fixedcamerabehavior#/s:7heresdk19FixedCameraBehaviorC4zoomAA10MapMeasureVvp" class="token"><code>zoom</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Zoom configuration. The default value is 150 meters. Camera zoom configuration. The default value is 150 meters. Note: <a href="sdk-for-ios-explore-structs-mapmeasure-kind#/s:7heresdk10MapMeasureV4KindO5scaleyA2EmF">`MapMeasure.Kind.scale`</a> is not supported.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var zoom: MapMeasure { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19FixedCameraBehaviorC19cameraTiltInDegreesSdvp"></span>` `<span id="//apple_ref/swift/Property/cameraTiltInDegrees" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-fixedcamerabehavior#/s:7heresdk19FixedCameraBehaviorC19cameraTiltInDegreesSdvp" class="token"><code>cameraTiltInDegrees</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Camera tilt with axis parallel to the ground. The default value is 50 degrees.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var cameraTiltInDegrees: Double { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19FixedCameraBehaviorC22cameraBearingInDegreesSdSgvp"></span>` `<span id="//apple_ref/swift/Property/cameraBearingInDegrees" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-fixedcamerabehavior#/s:7heresdk19FixedCameraBehaviorC22cameraBearingInDegreesSdSgvp" class="token"><code>cameraBearingInDegrees</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Camera bearing in degrees. Optional fixed bearing, from true North (0 degrees) in clockwise direction. The valid range is \[0, 360\]. If set, it will prevent the map from rotating to the direction of travel. For example, a value of zero results in “north up” mode. Defaults to `nil`, which means the camera derives the bearing from the <a href="sdk-for-ios-explore-structs-location">`Location`</a>, so that it points to the direction of travel. If this property is `nil` and the device does not provide bearing, the last known value is used or zero otherwise.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var cameraBearingInDegrees: Double? { get set }
  ```

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

