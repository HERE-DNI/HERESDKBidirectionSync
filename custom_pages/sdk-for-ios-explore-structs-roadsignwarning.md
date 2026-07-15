---
title: "RoadSignWarning Structure Reference"
slug: "sdk-for-ios-explore-structs-roadsignwarning"
---

# RoadSignWarning

<div class="declaration">

<div class="language">

``` highlight
public struct RoadSignWarning : Hashable
```

</div>

</div>

A road sign. The main field describing the sign is <a href="sdk-for-ios-explore-structs-roadsignwarning#/s:7heresdk15RoadSignWarningV4typeAA0bC4TypeOvp">`RoadSignWarning.type`</a>. Some road types are standardized, others can be country specific. A valid road sign contains known <a href="sdk-for-ios-explore-structs-roadsignwarning#/s:7heresdk15RoadSignWarningV4typeAA0bC4TypeOvp">`RoadSignWarning.type`</a> or <a href="sdk-for-ios-explore-structs-roadsignwarning#/s:7heresdk15RoadSignWarningV8categoryAA0bC8CategoryOvp">`RoadSignWarning.category`</a>. Use `RoadSignWarningListener` to get notifications with current road signs.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk15RoadSignWarningV2ids5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/id" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-roadsignwarning#/s:7heresdk15RoadSignWarningV2ids5Int32Vvp" class="token"><code>id</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Unique identifier for this specific road sign warning instance. Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace. Use this ID to track, update, or dismiss individual warning instances of this type.

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

  ` `<span id="/s:7heresdk15RoadSignWarningV010distanceTobC8InMetersSdvp"></span>` `<span id="//apple_ref/swift/Property/distanceToRoadSignInMeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-roadsignwarning#/s:7heresdk15RoadSignWarningV010distanceTobC8InMetersSdvp" class="token"><code>distanceToRoadSignInMeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Distance to the road sign in meters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var distanceToRoadSignInMeters: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15RoadSignWarningV4typeAA0bC4TypeOvp"></span>` `<span id="//apple_ref/swift/Property/type" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-roadsignwarning#/s:7heresdk15RoadSignWarningV4typeAA0bC4TypeOvp" class="token"><code>type</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Type of the road sign.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var type: RoadSignType
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15RoadSignWarningV8categoryAA0bC8CategoryOvp"></span>` `<span id="//apple_ref/swift/Property/category" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-roadsignwarning#/s:7heresdk15RoadSignWarningV8categoryAA0bC8CategoryOvp" class="token"><code>category</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The main category to which the road sign belongs.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var category: RoadSignCategory
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15RoadSignWarningV07generalD4TypeAA07GeneraldbcF0Ovp"></span>` `<span id="//apple_ref/swift/Property/generalWarningType" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-roadsignwarning#/s:7heresdk15RoadSignWarningV07generalD4TypeAA07GeneraldbcF0Ovp" class="token"><code>generalWarningType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies the general warning to which the road sign belongs.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var generalWarningType: GeneralWarningRoadSignType
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15RoadSignWarningV010isPriorityC0Sbvp"></span>` `<span id="//apple_ref/swift/Property/isPrioritySign" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-roadsignwarning#/s:7heresdk15RoadSignWarningV010isPriorityC0Sbvp" class="token"><code>isPrioritySign</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Flag indicating if the road sign is a priority sign.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isPrioritySign: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15RoadSignWarningV12vehicleTypesSayAA0bC11VehicleTypeOGvp"></span>` `<span id="//apple_ref/swift/Property/vehicleTypes" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-roadsignwarning#/s:7heresdk15RoadSignWarningV12vehicleTypesSayAA0bC11VehicleTypeOGvp" class="token"><code>vehicleTypes</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies a list of vehicle types for which the road sign is applicable. The list will be empty when the road sign is applicable for all vehicles including cars.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var vehicleTypes: [RoadSignVehicleType]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15RoadSignWarningV11weatherTypeAA07WeatherF0Ovp"></span>` `<span id="//apple_ref/swift/Property/weatherType" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-roadsignwarning#/s:7heresdk15RoadSignWarningV11weatherTypeAA07WeatherF0Ovp" class="token"><code>weatherType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies the weather type for which the sign is applicable. If weather type is <a href="sdk-for-ios-explore-enums-weathertype#/s:7heresdk11WeatherTypeO7unknownyA2CmF">`WeatherType.unknown`</a>, the sign is actual for all weather types.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var weatherType: WeatherType
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15RoadSignWarningV9signValueAA13LocalizedTextVSgvp"></span>` `<span id="//apple_ref/swift/Property/signValue" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-roadsignwarning#/s:7heresdk15RoadSignWarningV9signValueAA13LocalizedTextVSgvp" class="token"><code>signValue</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Optional value visible on the main sign related to specific road sign types, as it is printed on the local road sign.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var signValue: LocalizedText?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15RoadSignWarningV03preD0AA13LocalizedTextVSgvp"></span>` `<span id="//apple_ref/swift/Property/preWarning" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-roadsignwarning#/s:7heresdk15RoadSignWarningV03preD0AA13LocalizedTextVSgvp" class="token"><code>preWarning</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Optional pre-warning in terms of distance, of the upcoming warning or regulation. The pre-warning information is given as printed on the local road sign.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var preWarning: LocalizedText?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15RoadSignWarningV8durationAA13LocalizedTextVSgvp"></span>` `<span id="//apple_ref/swift/Property/duration" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-roadsignwarning#/s:7heresdk15RoadSignWarningV8durationAA13LocalizedTextVSgvp" class="token"><code>duration</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Optional length information during which the warning is applicable. Usually, this information is shown on a separate shield below the main shield. For example, a sign may warn on playing children for a length of 100 m, starting from the location of the warning sign. The length information (most likely with units) is given as printed on the local road sign.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var duration: LocalizedText?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15RoadSignWarningV12validityTimeAA13LocalizedTextVSgvp"></span>` `<span id="//apple_ref/swift/Property/validityTime" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-roadsignwarning#/s:7heresdk15RoadSignWarningV12validityTimeAA13LocalizedTextVSgvp" class="token"><code>validityTime</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Optional text visible on the supplemental sign indicating specific time(s) at which the road sign is applicable. The time information is given as printed on the local road sign.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var validityTime: LocalizedText?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15RoadSignWarningV04roadC7SegmentAA0F9ReferenceVvp"></span>` `<span id="//apple_ref/swift/Property/roadSignSegment" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-roadsignwarning#/s:7heresdk15RoadSignWarningV04roadC7SegmentAA0F9ReferenceVvp" class="token"><code>roadSignSegment</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The reference to the segment where the road sign is located. It can be used to identify the location of the road sign. It allows to compare the road sign location with the `MapMatchedLocation.segment_reference` provided by the `NavigableLocationListener` or with the <a href="sdk-for-ios-explore-classes-span#/s:7heresdk4SpanC16segmentReferenceAA07SegmentD0Vvp">`Span.segmentReference`</a> available in the Route’s Span. By combining it with the geometry of the segment, that can be loaded using <a href="sdk-for-ios-explore-classes-segmentdataloader">`SegmentDataLoader`</a>, it is possible to identify the road sign’s coordinates.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var roadSignSegment: SegmentReference
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15RoadSignWarningV12distanceTypeAA08DistanceF0Ovp"></span>` `<span id="//apple_ref/swift/Property/distanceType" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-roadsignwarning#/s:7heresdk15RoadSignWarningV12distanceTypeAA08DistanceF0Ovp" class="token"><code>distanceType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The distance type for the warning, e.g. a warning for a new road sign ahead or a warning for passing a road sign. Since the road sign warning is given relative to a single position on the route, <a href="sdk-for-ios-explore-enums-distancetype#/s:7heresdk12DistanceTypeO7reachedyA2CmF">`DistanceType.reached`</a> will never be given for this warning.

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

      init(id: distanceToRoadSignInMeters: type: category: generalWarningType: isPrioritySign: vehicleTypes: weatherType: signValue: preWarning: duration: validityTime: roadSignSegment: distanceType: )

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
  public init ( id : Int32 = 0 , distanceToRoadSignInMeters : Double , type : RoadSignType , category : RoadSignCategory , generalWarningType : GeneralWarningRoadSignType , isPrioritySign : Bool , vehicleTypes : [ RoadSignVehicleType ], weatherType : WeatherType , signValue : LocalizedText ? = nil , preWarning : LocalizedText ? = nil , duration : LocalizedText ? = nil , validityTime : LocalizedText ? = nil , roadSignSegment : SegmentReference , distanceType : DistanceType )
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

