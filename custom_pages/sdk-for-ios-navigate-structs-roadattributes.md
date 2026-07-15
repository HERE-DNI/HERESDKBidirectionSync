---
title: "RoadAttributes Structure Reference"
slug: "sdk-for-ios-navigate-structs-roadattributes"
---

# RoadAttributes

<div class="declaration">

<div class="language">

``` highlight
public struct RoadAttributes : Hashable
```

</div>

</div>

Road attributes, including usage and physical characteristics. Note that a road can have more than one attribute at the same time.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk14RoadAttributesV06isDirtB0Sbvp"></span>` `<span id="//apple_ref/swift/Property/isDirtRoad" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-roadattributes#/s:7heresdk14RoadAttributesV06isDirtB0Sbvp" class="token"><code>isDirtRoad</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates whether the navigable segment is paved. Paved is primarily used for map display and routing by assigning higher penalties to unpaved roads. Paved roads are made of concrete, asphalt, cobblestone or brick. Unpaved roads do not have a solid surface, e.g. are made of gravel, dirt or grass.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isDirtRoad: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14RoadAttributesV8isTunnelSbvp"></span>` `<span id="//apple_ref/swift/Property/isTunnel" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-roadattributes#/s:7heresdk14RoadAttributesV8isTunnelSbvp" class="token"><code>isTunnel</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Identifies an enclosed (on all sides) passageway through or under an obstruction. This attribute can be used for display or route guidance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isTunnel: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14RoadAttributesV8isBridgeSbvp"></span>` `<span id="//apple_ref/swift/Property/isBridge" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-roadattributes#/s:7heresdk14RoadAttributesV8isBridgeSbvp" class="token"><code>isBridge</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Identifies a structure that allows a road, railway, or walkway to pass over another road, railway, waterway, or valley serving map display and route guidance functionalities. Bridge is published on segments that represent significant bridges and/or overpasses; elevated roads are not published as bridge.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isBridge: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14RoadAttributesV6isRampSbvp"></span>` `<span id="//apple_ref/swift/Property/isRamp" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-roadattributes#/s:7heresdk14RoadAttributesV6isRampSbvp" class="token"><code>isRamp</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Range is a ramp: connects roads that do not intersect at grade. Ramp allows explication of maneuvers involving ramps (e.g., “Take the ramp”) and for route guidance when determining if sign text should be used.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isRamp: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14RoadAttributesV18isControlledAccessSbvp"></span>` `<span id="//apple_ref/swift/Property/isControlledAccess" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-roadattributes#/s:7heresdk14RoadAttributesV18isControlledAccessSbvp" class="token"><code>isControlledAccess</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Controlled access roads are roads with limited entrances and exits that allow uninterrupted high-speed traffic flow. For example, the Interstate/Freeway network in the United States or the Motorway network in Europe. Controlled Access can be used for map display, avoidance of freeway/motorway, publishing speed limits, and route guidance timing.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isControlledAccess: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14RoadAttributesV9isPrivateSbvp"></span>` `<span id="//apple_ref/swift/Property/isPrivate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-roadattributes#/s:7heresdk14RoadAttributesV9isPrivateSbvp" class="token"><code>isPrivate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Private identifies roads that are not maintained by an organization responsible for maintenance of public roads. Allows for unique cartographic representation of roads that restrict public use. May be used to avoid routing through a private road.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isPrivate: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14RoadAttributesV11isNoThroughSbvp"></span>` `<span id="//apple_ref/swift/Property/isNoThrough" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-roadattributes#/s:7heresdk14RoadAttributesV11isNoThroughSbvp" class="token"><code>isNoThrough</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Identifies a no through road. This can also be a part of the route you can only enter or leave if it’s a waypoint.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isNoThrough: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14RoadAttributesV9isTollwaySbvp"></span>` `<span id="//apple_ref/swift/Property/isTollway" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-roadattributes#/s:7heresdk14RoadAttributesV9isTollwaySbvp" class="token"><code>isTollway</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Identifies a road for which a fee must be paid to use the road. Tollway may be used for map display (e.g., different rendering of toll roads) and routing. Tollway is flagged on roads that require a fee for traversal.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isTollway: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14RoadAttributesV09isDividedB0Sbvp"></span>` `<span id="//apple_ref/swift/Property/isDividedRoad" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-roadattributes#/s:7heresdk14RoadAttributesV09isDividedB0Sbvp" class="token"><code>isDividedRoad</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates if there is a physical structure or painted road marking intended to legally prohibit left turns in right-side driving countries, right turns in left-side driving countries, and U-turns at divided intersections or in the middle of divided segments.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isDividedRoad: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14RoadAttributesV18isRightDrivingSideSbvp"></span>` `<span id="//apple_ref/swift/Property/isRightDrivingSide" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-roadattributes#/s:7heresdk14RoadAttributesV18isRightDrivingSideSbvp" class="token"><code>isRightDrivingSide</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates if vehicles have to drive on the right-hand side of the road or the left-hand side. For example, in New York it is always `true` and in London always `false` as the United Kingdom is a left-hand driving country.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isRightDrivingSide: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14RoadAttributesV12isRoundaboutSbvp"></span>` `<span id="//apple_ref/swift/Property/isRoundabout" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-roadattributes#/s:7heresdk14RoadAttributesV12isRoundaboutSbvp" class="token"><code>isRoundabout</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the presence of a roundabout.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isRoundabout: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14RoadAttributesV13isBuiltUpAreaSbvp"></span>` `<span id="//apple_ref/swift/Property/isBuiltUpArea" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-roadattributes#/s:7heresdk14RoadAttributesV13isBuiltUpAreaSbvp" class="token"><code>isBuiltUpArea</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates if the navigable segment is a built up area.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isBuiltUpArea: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(isDirtRoad: isTunnel: isBridge: isRamp: isControlledAccess: isPrivate: isNoThrough: isTollway: isDividedRoad: isRightDrivingSide: isRoundabout: isBuiltUpArea: )

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
  public init ( isDirtRoad : Bool = false , isTunnel : Bool = false , isBridge : Bool = false , isRamp : Bool = false , isControlledAccess : Bool = false , isPrivate : Bool = false , isNoThrough : Bool = false , isTollway : Bool = false , isDividedRoad : Bool = false , isRightDrivingSide : Bool = false , isRoundabout : Bool = false , isBuiltUpArea : Bool = false )
  ```

  </pre>

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

