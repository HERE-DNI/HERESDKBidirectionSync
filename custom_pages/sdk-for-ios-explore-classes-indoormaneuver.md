---
title: "IndoorManeuver Class Reference"
slug: "sdk-for-ios-explore-classes-indoormaneuver"
---

# IndoorManeuver

<div class="declaration">

<div class="language">

``` highlight
public class IndoorManeuver
```

``` highlight
extension IndoorManeuver: NativeBase
```

``` highlight
extension IndoorManeuver: Hashable
```

</div>

</div>

Represents a maneuver within an indoor section.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk14IndoorManeuverC6actionAA0bC7ActionsOSgvp"></span>` `<span id="//apple_ref/swift/Property/action" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-indoormaneuver#/s:7heresdk14IndoorManeuverC6actionAA0bC7ActionsOSgvp" class="token"><code>action</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The action type of this maneuver.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var action: IndoorManeuverActions? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14IndoorManeuverC10coordinateAA14GeoCoordinatesVvp"></span>` `<span id="//apple_ref/swift/Property/coordinate" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-indoormaneuver#/s:7heresdk14IndoorManeuverC10coordinateAA14GeoCoordinatesVvp" class="token"><code>coordinate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The geographic coordinates of this maneuver.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var coordinate: GeoCoordinates { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14IndoorManeuverC6offsets5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/offset" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-indoormaneuver#/s:7heresdk14IndoorManeuverC6offsets5Int32Vvp" class="token"><code>offset</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The offset of this maneuver from the start of the section.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var offset: Int32 { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14IndoorManeuverC12sectionIndexs5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/sectionIndex" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-indoormaneuver#/s:7heresdk14IndoorManeuverC12sectionIndexs5Int32Vvp" class="token"><code>sectionIndex</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The section index this maneuver belongs to.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var sectionIndex: Int32 { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14IndoorManeuverC14lengthInMetersSfvp"></span>` `<span id="//apple_ref/swift/Property/lengthInMeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-indoormaneuver#/s:7heresdk14IndoorManeuverC14lengthInMetersSfvp" class="token"><code>lengthInMeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The length of this maneuver in meters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var lengthInMeters: Float { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14IndoorManeuverC8durationSdvp"></span>` `<span id="//apple_ref/swift/Property/duration" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-indoormaneuver#/s:7heresdk14IndoorManeuverC8durationSdvp" class="token"><code>duration</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The duration to complete this maneuver.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var duration: TimeInterval { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14IndoorManeuverC11levelZIndexs5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/levelZIndex" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-indoormaneuver#/s:7heresdk14IndoorManeuverC11levelZIndexs5Int32Vvp" class="token"><code>levelZIndex</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The vertical level index of this maneuver.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var levelZIndex: Int32 { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14IndoorManeuverC15indoorSpaceDataAA0beF0VSgvp"></span>` `<span id="//apple_ref/swift/Property/indoorSpaceData" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-indoormaneuver#/s:7heresdk14IndoorManeuverC15indoorSpaceDataAA0beF0VSgvp" class="token"><code>indoorSpaceData</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The indoor space data for this maneuver. This will be not null if the IndoorManeuverAction is ENTER_ACTION or LEAVE_ACTION.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var indoorSpaceData: IndoorSpaceData? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14IndoorManeuverC21indoorLevelChangeDataAA0befG0VSgvp"></span>` `<span id="//apple_ref/swift/Property/indoorLevelChangeData" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-indoormaneuver#/s:7heresdk14IndoorManeuverC21indoorLevelChangeDataAA0befG0VSgvp" class="token"><code>indoorLevelChangeData</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The level change data for this maneuver. This will be not null if the IndoorManeuverAction is LEVEL_CHANGE_ACTION.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var indoorLevelChangeData: IndoorLevelChangeData? { get }
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

