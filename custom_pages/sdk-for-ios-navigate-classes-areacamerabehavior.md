---
title: "AreaCameraBehavior Class Reference"
slug: "sdk-for-ios-navigate-classes-areacamerabehavior"
---

# AreaCameraBehavior

<div class="declaration">

<div class="language">

``` highlight
public class AreaCameraBehavior : CameraBehavior
```

``` highlight
extension AreaCameraBehavior: NativeBase
```

``` highlight
extension AreaCameraBehavior: Hashable
```

</div>

</div>

Use this class to show an overview of geo points. By default, the orientation of the camera will be perpendicular to the Earth’s surface (ie. looking towards the center of the Earth), while bearing will be towards north.

Note: This is a beta feature; there maybe bugs and unexpected behavior. Related API’s are subject to change without a deprecation process.

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

  ` `<span id="/s:7heresdk18AreaCameraBehaviorC24normalizedPrincipalPointAA8Anchor2DVvp"></span>` `<span id="//apple_ref/swift/Property/normalizedPrincipalPoint" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-areacamerabehavior#/s:7heresdk18AreaCameraBehaviorC24normalizedPrincipalPointAA8Anchor2DVvp" class="token"><code>normalizedPrincipalPoint</code></a>` `

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

  ` `<span id="/s:7heresdk18AreaCameraBehaviorC13viewRectangleAA11Rectangle2DVSgvp"></span>` `<span id="//apple_ref/swift/Property/viewRectangle" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-areacamerabehavior#/s:7heresdk18AreaCameraBehaviorC13viewRectangleAA11Rectangle2DVSgvp" class="token"><code>viewRectangle</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The view rectangle for camera updates. Defines a sub-space of the screen that the behavior should consider for camera updates. Defaults to `nil`. If not set, it uses the viewport bounds of the underlying map view.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var viewRectangle: Rectangle2D? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18AreaCameraBehaviorC23cameraAnimationDurationSdvp"></span>` `<span id="//apple_ref/swift/Property/cameraAnimationDuration" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-areacamerabehavior#/s:7heresdk18AreaCameraBehaviorC23cameraAnimationDurationSdvp" class="token"><code>cameraAnimationDuration</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The duration of camera animation in milliseconds. If there is an animation, it will last for specified period of time. Defaults to 500 milliseconds, or half a second.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var cameraAnimationDuration: TimeInterval { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18AreaCameraBehaviorC31principalPointAnimationDurationSdvp"></span>` `<span id="//apple_ref/swift/Property/principalPointAnimationDuration" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-areacamerabehavior#/s:7heresdk18AreaCameraBehaviorC31principalPointAnimationDurationSdvp" class="token"><code>principalPointAnimationDuration</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The duration of principal point animation in milliseconds. If the principal point is changed, the change will be animated over this duration. Defaults to 500 milliseconds, or half a second.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var principalPointAnimationDuration: TimeInterval { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18AreaCameraBehaviorC7maxZoomAA10MapMeasureVvp"></span>` `<span id="//apple_ref/swift/Property/maxZoom" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-areacamerabehavior#/s:7heresdk18AreaCameraBehaviorC7maxZoomAA10MapMeasureVvp" class="token"><code>maxZoom</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Maximal allowed zoom. Defines maximal zoom level to be applied to enclose geodetic bounding box. Defaults to a <a href="sdk-for-ios-navigate-structs-mapmeasure">`MapMeasure`</a> with kind <a href="sdk-for-ios-navigate-structs-mapmeasure-kind#/s:7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">`MapMeasure.Kind.zoomLevel`</a> and value 20.0. Note: <a href="sdk-for-ios-navigate-structs-mapmeasure-kind#/s:7heresdk10MapMeasureV4KindO5scaleyA2EmF">`MapMeasure.Kind.scale`</a> is not supported.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maxZoom: MapMeasure { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18AreaCameraBehaviorC22cameraBearingInDegreesSdvp"></span>` `<span id="//apple_ref/swift/Property/cameraBearingInDegrees" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-areacamerabehavior#/s:7heresdk18AreaCameraBehaviorC22cameraBearingInDegreesSdvp" class="token"><code>cameraBearingInDegrees</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Camera bearing in degrees. The direction in which the camera will point in degrees clockwise, relative to true North. The input should range between \[0, 360\]. Defaults to true North (0 degrees).

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var cameraBearingInDegrees: Double { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18AreaCameraBehaviorC19cameraTiltInDegreesSdvp"></span>` `<span id="//apple_ref/swift/Property/cameraTiltInDegrees" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-areacamerabehavior#/s:7heresdk18AreaCameraBehaviorC19cameraTiltInDegreesSdvp" class="token"><code>cameraTiltInDegrees</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Camera tilt in degrees. The tilt of the camera relative to the axis perpendicular to the ground. Defaults to 0 degrees, meaning that it will look straight down into the ground.

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

  ` `<span id="/s:7heresdk18AreaCameraBehaviorC25isCurrentPositionIncludedSbvp"></span>` `<span id="//apple_ref/swift/Property/isCurrentPositionIncluded" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-areacamerabehavior#/s:7heresdk18AreaCameraBehaviorC25isCurrentPositionIncludedSbvp" class="token"><code>isCurrentPositionIncluded</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Include current position in camera view. Decides if the current position should be added to the set of visible points. Note that if the current position is in the vicinity of any of the visible points, setting this to `false` will not explicitly exclude the current position from the camera view. However if displaying an area potentially away from the current position, this does need to be explicitly set to `false` or it will try to include the current position. Defaults to false.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isCurrentPositionIncluded: Bool { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      setVisiblePoints(visiblePoints: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the list of geo points to show in the camera view.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setVisiblePoints ( visiblePoints : [ GeoCoordinates ])
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>visiblePoints</code></em><code> </code></td>
  <td><div>
  <p>The list of geo points to visualize. The list can be empty.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      getVisiblePoints()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets configured visible geo points.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getVisiblePoints () -> [ GeoCoordinates ]
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  The list of geo points to show in the camera view. The list can be empty.

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

