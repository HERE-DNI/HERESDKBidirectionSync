---
title: "LaneDecreaseWarning Structure Reference"
slug: "sdk-for-ios-navigate-structs-lanedecreasewarning"
---

# LaneDecreaseWarning

<div class="declaration">

<div class="language">

``` highlight
public struct LaneDecreaseWarning : Hashable
```

</div>

</div>

Represents a lane decrease warning that notifies about upcoming reductions in the number of available lanes.

Lane decrease warnings are generated when the road ahead has fewer lanes than the previous road segment provided by `sdk.electronic_horizon.ElectronicHorizonEngine`, requiring drivers to merge or change lanes. Lane decrease is provided only on highways and motorways. It will not be provided for junctions, when maneuver is given for the lane decrease situation or when the <a href="sdk-for-ios-navigate-structs-trafficmergewarning">`TrafficMergeWarning`</a> is provided. Special lanes (e.g. Bus lane, HOV) will only be included to the lane decrease warning generation if the according options are set in <a href="sdk-for-ios-navigate-structs-transportspecification">`TransportSpecification`</a>.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk19LaneDecreaseWarningV2ids5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/id" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-lanedecreasewarning#/s:7heresdk19LaneDecreaseWarningV2ids5Int32Vvp" class="token"><code>id</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Unique identifier for this lane decrease warning instance. Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace. Use this ID to track, update, or dismiss individual warning instances of this type.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var id: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19LaneDecreaseWarningV08previousB6Numbers5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/previousLaneNumber" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-lanedecreasewarning#/s:7heresdk19LaneDecreaseWarningV08previousB6Numbers5Int32Vvp" class="token"><code>previousLaneNumber</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Number of lanes before the lane decrease event.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var previousLaneNumber: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19LaneDecreaseWarningV03newB6Numbers5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/newLaneNumber" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-lanedecreasewarning#/s:7heresdk19LaneDecreaseWarningV03newB6Numbers5Int32Vvp" class="token"><code>newLaneNumber</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Number of lanes after the lane decrease event.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var newLaneNumber: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19LaneDecreaseWarningV22lanesDecreasedFromLefts5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/lanesDecreasedFromLeft" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-lanedecreasewarning#/s:7heresdk19LaneDecreaseWarningV22lanesDecreasedFromLefts5Int32VSgvp" class="token"><code>lanesDecreasedFromLeft</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Number of lanes decreased on the left side of the road, `nil` if the left-side change is unknown or not applicable.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var lanesDecreasedFromLeft: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19LaneDecreaseWarningV23lanesDecreasedFromRights5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/lanesDecreasedFromRight" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-lanedecreasewarning#/s:7heresdk19LaneDecreaseWarningV23lanesDecreasedFromRights5Int32VSgvp" class="token"><code>lanesDecreasedFromRight</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Number of lanes decreased on the right side of the road, `nil` if the right-side change is unknown or not applicable.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var lanesDecreasedFromRight: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19LaneDecreaseWarningV16distanceInMetersSdvp"></span>` `<span id="//apple_ref/swift/Property/distanceInMeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-lanedecreasewarning#/s:7heresdk19LaneDecreaseWarningV16distanceInMetersSdvp" class="token"><code>distanceInMeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The distance from the current location to the Lane decrease event.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var distanceInMeters: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19LaneDecreaseWarningV12distanceTypeAA08DistanceF0Ovp"></span>` `<span id="//apple_ref/swift/Property/distanceType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-lanedecreasewarning#/s:7heresdk19LaneDecreaseWarningV12distanceTypeAA08DistanceF0Ovp" class="token"><code>distanceType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates if the specified event is ahead of the vehicle or has just passed by. If it is ahead, then <a href="sdk-for-ios-navigate-structs-lanedecreasewarning#/s:7heresdk19LaneDecreaseWarningV16distanceInMetersSdvp">`LaneDecreaseWarning.distanceInMeters`</a> is greater than 0.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var distanceType: DistanceType
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(id: previousLaneNumber: newLaneNumber: lanesDecreasedFromLeft: lanesDecreasedFromRight: distanceInMeters: distanceType: )

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
  public init ( id : Int32 = 0 , previousLaneNumber : Int32 = 0 , newLaneNumber : Int32 = 0 , lanesDecreasedFromLeft : Int32 ? = nil , lanesDecreasedFromRight : Int32 ? = nil , distanceInMeters : Double , distanceType : DistanceType )
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

