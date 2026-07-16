---
title: "SegmentData Class Reference"
slug: "sdk-for-ios-explore-classes-segmentdata"
---

# SegmentData

<div class="declaration">

<div class="language">

``` highlight
public class SegmentData
```

``` highlight
extension SegmentData: NativeBase
```

``` highlight
extension SegmentData: Hashable
```

</div>

</div>

Contains the requested information for a segment

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11SegmentDataC03ocmB2IdAA010OCMSegmentE0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-ocmSegmentId" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-segmentdata#sdk-for-ios-explore-s-7heresdk11SegmentDataC03ocmB2IdAA010OCMSegmentE0Vvp" class="token"><code>ocmSegmentId</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The <a href="sdk-for-ios-explore-structs-ocmsegmentid">`OCMSegmentId`</a> object representing the segment

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var ocmSegmentId: OCMSegmentId { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-ocmsegmentid">OCMSegmentId</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11SegmentDataC16segmentReferenceAA0bE0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-segmentReference" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-segmentdata#sdk-for-ios-explore-s-7heresdk11SegmentDataC16segmentReferenceAA0bE0Vvp" class="token"><code>segmentReference</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The <a href="sdk-for-ios-explore-structs-segmentreference">`SegmentReference`</a> object representing the segment

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var segmentReference: SegmentReference { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-segmentreference">SegmentReference</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11SegmentDataC8polylineAA11GeoPolylineVvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-polyline" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-segmentdata#sdk-for-ios-explore-s-7heresdk11SegmentDataC8polylineAA11GeoPolylineVvp" class="token"><code>polyline</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The <a href="sdk-for-ios-explore-structs-geopolyline">`GeoPolyline`</a> object representing the polyline of this segment.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public private(set) lazy var polyline: GeoPolyline { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geopolyline">GeoPolyline</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11SegmentDataC14lengthInMeterss5Int32Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-lengthInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-segmentdata#sdk-for-ios-explore-s-7heresdk11SegmentDataC14lengthInMeterss5Int32Vvp" class="token"><code>lengthInMeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The length of this segment in meters. This information is based on map data. It can differ from the length of <a href="sdk-for-ios-explore-classes-segmentdata#sdk-for-ios-explore-s-7heresdk11SegmentDataC8polylineAA11GeoPolylineVvp">`SegmentData.polyline`</a> due to approximations of the polyline.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var lengthInMeters: Int32 { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11SegmentDataC5spansSayAA0b4SpanC0CGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-spans" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-segmentdata#sdk-for-ios-explore-s-7heresdk11SegmentDataC5spansSayAA0b4SpanC0CGvp" class="token"><code>spans</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of <a href="sdk-for-ios-explore-classes-segmentspandata">`SegmentSpanData`</a> of the given segment for the requested attributes **Note:** If no span attributes is requested, the list will be empty.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var spans: [SegmentSpanData] { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-segmentspandata">SegmentSpanData</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11SegmentDataC14trafficSignalsSayAA13TrafficSignalVGSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-trafficSignals" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-segmentdata#sdk-for-ios-explore-s-7heresdk11SegmentDataC14trafficSignalsSayAA13TrafficSignalVGSgvp" class="token"><code>trafficSignals</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of <a href="sdk-for-ios-explore-structs-trafficsignal">`TrafficSignal`</a> of the given segment. Returns an empty list if no data is found. Returns `nil` if <a href="sdk-for-ios-explore-structs-segmentdataloaderoptions#sdk-for-ios-explore-s-7heresdk24SegmentDataLoaderOptionsV18loadTrafficSignalsSbvp">`SegmentDataLoaderOptions.loadTrafficSignals`</a> is set to `false`. The <a href="sdk-for-ios-explore-enums-trafficsignallocation">`TrafficSignalLocation`</a> indicates the location of a single traffic signal, which can be any combination of left, right and overhead. The <a href="sdk-for-ios-explore-structs-trafficsignal#sdk-for-ios-explore-s-7heresdk13TrafficSignalV14offsetInMeterss5Int32Vvp">`TrafficSignal.offsetInMeters`</a> is the location along the segment, while the traffic signal location have details on how the traffic signal is display/deploy in that specific location in the segment.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var trafficSignals: [TrafficSignal]? { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-trafficsignal">TrafficSignal</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11SegmentDataC9roadSignsSayAA8RoadSignVGSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-roadSigns" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-segmentdata#sdk-for-ios-explore-s-7heresdk11SegmentDataC9roadSignsSayAA8RoadSignVGSgvp" class="token"><code>roadSigns</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of <a href="sdk-for-ios-explore-structs-roadsign">`RoadSign`</a> of the given segment. Returns `nil` if <a href="sdk-for-ios-explore-structs-segmentdataloaderoptions#sdk-for-ios-explore-s-7heresdk24SegmentDataLoaderOptionsV13loadRoadSignsSbvp">`SegmentDataLoaderOptions.loadRoadSigns`</a> is set to `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var roadSigns: [RoadSign]? { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-roadsign">RoadSign</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11SegmentDataC16railwayCrossingsSayAA15RailwayCrossingVGSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-railwayCrossings" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-segmentdata#sdk-for-ios-explore-s-7heresdk11SegmentDataC16railwayCrossingsSayAA15RailwayCrossingVGSgvp" class="token"><code>railwayCrossings</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of <a href="sdk-for-ios-explore-structs-railwaycrossing">`RailwayCrossing`</a> of the given segment. Returns an empty list if no data is found. Returns `nil` if <a href="sdk-for-ios-explore-structs-segmentdataloaderoptions#sdk-for-ios-explore-s-7heresdk24SegmentDataLoaderOptionsV20loadRailwayCrossingsSbvp">`SegmentDataLoaderOptions.loadRailwayCrossings`</a> is set to `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var railwayCrossings: [RailwayCrossing]? { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-railwaycrossing">RailwayCrossing</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11SegmentDataC10tollPointsSayAA9TollPointVGSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-tollPoints" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-segmentdata#sdk-for-ios-explore-s-7heresdk11SegmentDataC10tollPointsSayAA9TollPointVGSgvp" class="token"><code>tollPoints</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of <a href="sdk-for-ios-explore-structs-tollpoint">`TollPoint`</a> of the given segment. Returns an empty list if no data is found. Returns `nil` if <a href="sdk-for-ios-explore-structs-segmentdataloaderoptions#sdk-for-ios-explore-s-7heresdk24SegmentDataLoaderOptionsV14loadTollPointsSbvp">`SegmentDataLoaderOptions.loadTollPoints`</a> is set to `false` or the `SegmentData` is not initialized using <a href="sdk-for-ios-explore-classes-segmentdataloader#sdk-for-ios-explore-s-7heresdk17SegmentDataLoaderC012loadDirectedbC07segment7optionsAA0bC0CAA0F12OCMSegmentIdV_AA0bcD7OptionsVtKF">`SegmentDataLoader.loadDirectedSegmentData(...)`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var tollPoints: [TollPoint]? { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-tollpoint">TollPoint</a>

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

