---
title: "MapMatchedLocation Structure Reference"
slug: "sdk-for-ios-navigate-structs-mapmatchedlocation"
---

# MapMatchedLocation

<div class="declaration">

<div class="language">

``` highlight
public struct MapMatchedLocation : Hashable
```

</div>

</div>

Describes a map-matched location in the world at a given time.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk18MapMatchedLocationV11coordinatesAA14GeoCoordinatesVvp"></span>` `<span id="//apple_ref/swift/Property/coordinates" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-mapmatchedlocation#/s:7heresdk18MapMatchedLocationV11coordinatesAA14GeoCoordinatesVvp" class="token"><code>coordinates</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The geographic coordinates of the map-matched location.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var coordinates: GeoCoordinates
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18MapMatchedLocationV16bearingInDegreesSdSgvp"></span>` `<span id="//apple_ref/swift/Property/bearingInDegrees" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-mapmatchedlocation#/s:7heresdk18MapMatchedLocationV16bearingInDegreesSdSgvp" class="token"><code>bearingInDegrees</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The bearing orientation points to the direction of travel, and has the same angle as the street where it is matched to. Therefore, it must not necessarily be the same as the bearing of a location source. Starts at 0 in the geographic north and rotates in a clockwise direction around the compass. It means that for going north it’s equal to 0, for northeast it’s equal to 45, for east it’s equal to 90, and so on. If it cannot be determined, the value is `nil`. Otherwise, it is guaranteed to be in the range \<a href="sdk-for-ios-navigate-structs-mapmatchedlocation#/s:7heresdk18MapMatchedLocationV26segmentOffsetInCentimeterss6UInt32Vvp">0, 360).

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var bearingInDegrees: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18MapMatchedLocationV16segmentReferenceAA07SegmentF0Vvp"></span>` `<span id="//apple_ref/swift/Property/segmentReference" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-mapmatchedlocation#/s:7heresdk18MapMatchedLocationV16segmentReferenceAA07SegmentF0Vvp" class="token"><code>segmentReference</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Reference to the current segment. The ratio of [`MapMatchedLocation.segmentOffsetInCentimeters`</a> to the segment length is between <a href="sdk-for-ios-navigate-structs-segmentreference#/s:7heresdk16SegmentReferenceV11offsetStartSdvp">`SegmentReference.offsetStart`</a> and <a href="sdk-for-ios-navigate-structs-segmentreference#/s:7heresdk16SegmentReferenceV9offsetEndSdvp">`SegmentReference.offsetEnd`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var segmentReference: SegmentReference
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18MapMatchedLocationV26segmentOffsetInCentimeterss6UInt32Vvp"></span>` `<span id="//apple_ref/swift/Property/segmentOffsetInCentimeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-mapmatchedlocation#/s:7heresdk18MapMatchedLocationV26segmentOffsetInCentimeterss6UInt32Vvp" class="token"><code>segmentOffsetInCentimeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Offset from start of segment in centimeters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var segmentOffsetInCentimeters: UInt32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18MapMatchedLocationV10confidenceSdvp"></span>` `<span id="//apple_ref/swift/Property/confidence" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-mapmatchedlocation#/s:7heresdk18MapMatchedLocationV10confidenceSdvp" class="token"><code>confidence</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Confidence level (between 0 and 1) of the matched location. A low confidence value means that the map-matched vehicle location is not reliable and it may not be clear which part of the road the vehicle has taken. This can happen when the accuracy or frequency of the provided location updates is poor. If the confidence level is too small then, for example, overspeed warnings may be also inaccurate.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var confidence: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18MapMatchedLocationV22isDrivingInTheWrongWaySbvp"></span>` `<span id="//apple_ref/swift/Property/isDrivingInTheWrongWay" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-mapmatchedlocation#/s:7heresdk18MapMatchedLocationV22isDrivingInTheWrongWaySbvp" class="token"><code>isDrivingInTheWrongWay</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Determines if the travel direction on a one-way street is against the allowed traffic direction. For two-way streets, this value is always `false`. This feature is supported in tracking mode and when deviating from a route. Note that the travel direction is determined based on the map-matched location.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isDrivingInTheWrongWay: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18MapMatchedLocationV26horizontalAccuracyInMetersSdSgvp"></span>` `<span id="//apple_ref/swift/Property/horizontalAccuracyInMeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-mapmatchedlocation#/s:7heresdk18MapMatchedLocationV26horizontalAccuracyInMetersSdSgvp" class="token"><code>horizontalAccuracyInMeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Horizontal accuracy measure of location. Estimated based on accuracy of input location and confidence of this map-matched location. Currently this value is not being provided by the Navigator.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var horizontalAccuracyInMeters: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18MapMatchedLocationV22speedInMetersPerSecondSdSgvp"></span>` `<span id="//apple_ref/swift/Property/speedInMetersPerSecond" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-mapmatchedlocation#/s:7heresdk18MapMatchedLocationV22speedInMetersPerSecondSdSgvp" class="token"><code>speedInMetersPerSecond</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Speed in meters per second.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var speedInMetersPerSecond: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18MapMatchedLocationV9timestamp10Foundation4DateVSgvp"></span>` `<span id="//apple_ref/swift/Property/timestamp" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-mapmatchedlocation#/s:7heresdk18MapMatchedLocationV9timestamp10Foundation4DateVSgvp" class="token"><code>timestamp</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Timestamp of the map matched position.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var timestamp: Date?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(coordinates: bearingInDegrees: segmentReference: segmentOffsetInCentimeters: confidence: isDrivingInTheWrongWay: horizontalAccuracyInMeters: speedInMetersPerSecond: timestamp: )

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

    - coordinates: The geographic coordinates of the map-matched location.
    - bearingInDegrees: The bearing orientation points to the direction of travel, and has the same angle as the street where it is matched to. Therefore, it must not necessarily be the same as the bearing of a location source. Starts at 0 in the geographic north and rotates in a clockwise direction around the compass. It means that for going north it’s equal to 0, for northeast it’s equal to 45, for east it’s equal to 90, and so on. If it cannot be determined, the value is `nil`. Otherwise, it is guaranteed to be in the range \<a href="sdk-for-ios-navigate-structs-mapmatchedlocation#/s:7heresdk18MapMatchedLocationV26segmentOffsetInCentimeterss6UInt32Vvp">0, 360).
    - segmentReference: Reference to the current segment. The ratio of [`MapMatchedLocation.segmentOffsetInCentimeters`</a> to the segment length is between <a href="sdk-for-ios-navigate-structs-segmentreference#/s:7heresdk16SegmentReferenceV11offsetStartSdvp">`SegmentReference.offsetStart`</a> and <a href="sdk-for-ios-navigate-structs-segmentreference#/s:7heresdk16SegmentReferenceV9offsetEndSdvp">`SegmentReference.offsetEnd`</a>.
    - segmentOffsetInCentimeters: Offset from start of segment in centimeters.
    - confidence: Confidence level (between 0 and 1) of the matched location. A low confidence value means that the map-matched vehicle location is not reliable and it may not be clear which part of the road the vehicle has taken. This can happen when the accuracy or frequency of the provided location updates is poor. If the confidence level is too small then, for example, overspeed warnings may be also inaccurate.
    - isDrivingInTheWrongWay: Determines if the travel direction on a one-way street is against the allowed traffic direction. For two-way streets, this value is always `false`. This feature is supported in tracking mode and when deviating from a route. Note that the travel direction is determined based on the map-matched location.
    - horizontalAccuracyInMeters: Horizontal accuracy measure of location. Estimated based on accuracy of input location and confidence of this map-matched location. Currently this value is not being provided by the Navigator.
    - speedInMetersPerSecond: Speed in meters per second.

    **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    - timestamp: Timestamp of the map matched position.

    **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( coordinates : GeoCoordinates , bearingInDegrees : Double ? = nil , segmentReference : SegmentReference = SegmentReference (), segmentOffsetInCentimeters : UInt32 = 0 , confidence : Double = 0.0 , isDrivingInTheWrongWay : Bool = false , horizontalAccuracyInMeters : Double ? = nil , speedInMetersPerSecond : Double ? = nil , timestamp : Date ? = nil )
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

