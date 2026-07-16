---
title: "Section Class Reference"
slug: "sdk-for-ios-navigate-classes-section"
---

# Section

<div class="declaration">

<div class="language">

``` highlight
public class Section
```

``` highlight
extension Section: NativeBase
```

``` highlight
extension Section: Hashable
```

</div>

</div>

A section is a part of the route between two stopovers. A stopover is a location on the route where a stop is made.

**Note:** A section contains a list of <a href="sdk-for-ios-navigate-structs-sectionnotice">`SectionNotice`</a> objects that describe *potential issues* after the route was calculated. If the list is non-empty, it is recommended to evaluate possible violations against the requested route options and reject the route if deemed necessary.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7SectionC8geometryAA11GeoPolylineVvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-geometry" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-section#sdk-for-ios-navigate-s-7heresdk7SectionC8geometryAA11GeoPolylineVvp" class="token"><code>geometry</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The <a href="sdk-for-ios-navigate-structs-geopolyline">`GeoPolyline`</a> object representing the polyline of this section.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public private(set) lazy var geometry: GeoPolyline { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geopolyline">GeoPolyline</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7SectionC5spansSayAA4SpanCGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-spans" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-section#sdk-for-ios-navigate-s-7heresdk7SectionC5spansSayAA4SpanCGvp" class="token"><code>spans</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The <a href="sdk-for-ios-navigate-classes-span">`Span`</a>‘s that constitute this section.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public private(set) lazy var spans: [Span] { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-span">Span</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7SectionC9maneuversSayAA8ManeuverCGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-maneuvers" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-section#sdk-for-ios-navigate-s-7heresdk7SectionC9maneuversSayAA8ManeuverCGvp" class="token"><code>maneuvers</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The maneuvers for this section.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public private(set) lazy var maneuvers: [Maneuver] { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-maneuver">Maneuver</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7SectionC11boundingBoxAA03GeoD0Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-boundingBox" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-section#sdk-for-ios-navigate-s-7heresdk7SectionC11boundingBoxAA03GeoD0Vvp" class="token"><code>boundingBox</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The closest rectangular area where this section fits in.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var boundingBox: GeoBox { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geobox">GeoBox</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7SectionC14lengthInMeterss5Int32Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-lengthInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-section#sdk-for-ios-navigate-s-7heresdk7SectionC14lengthInMeterss5Int32Vvp" class="token"><code>lengthInMeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The length of this section in meters.

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

   <span id="sdk-for-ios-navigate-s-7heresdk7SectionC20sectionTransportModeAA0bdE0Ovp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-sectionTransportMode" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-section#sdk-for-ios-navigate-s-7heresdk7SectionC20sectionTransportModeAA0bdE0Ovp" class="token"><code>sectionTransportMode</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The transport mode of this section.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var sectionTransportMode: SectionTransportMode { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-sectiontransportmode">SectionTransportMode</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7SectionC14departurePlaceAA05RouteD0Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-departurePlace" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-section#sdk-for-ios-navigate-s-7heresdk7SectionC14departurePlaceAA05RouteD0Vvp" class="token"><code>departurePlace</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Describes the departure place.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var departurePlace: RoutePlace { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-routeplace">RoutePlace</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7SectionC12arrivalPlaceAA05RouteD0Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-arrivalPlace" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-section#sdk-for-ios-navigate-s-7heresdk7SectionC12arrivalPlaceAA05RouteD0Vvp" class="token"><code>arrivalPlace</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The arrival place. Describes the arrival place.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var arrivalPlace: RoutePlace { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-routeplace">RoutePlace</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7SectionC21departureLocationTimeAA0dE0VSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-departureLocationTime" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-section#sdk-for-ios-navigate-s-7heresdk7SectionC21departureLocationTimeAA0dE0VSgvp" class="token"><code>departureLocationTime</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The departure location time of this section.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var departureLocationTime: LocationTime? { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-locationtime">LocationTime</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7SectionC19arrivalLocationTimeAA0dE0VSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-arrivalLocationTime" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-section#sdk-for-ios-navigate-s-7heresdk7SectionC19arrivalLocationTimeAA0dE0VSgvp" class="token"><code>arrivalLocationTime</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The arrival location time of this section.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var arrivalLocationTime: LocationTime? { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-locationtime">LocationTime</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7SectionC10preActionsSayAA9PreActionVGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-preActions" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-section#sdk-for-ios-navigate-s-7heresdk7SectionC10preActionsSayAA9PreActionVGvp" class="token"><code>preActions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The preceding actions that must be done prior to departure at the beginning of the section.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public private(set) lazy var preActions: [PreAction] { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-preaction">PreAction</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7SectionC11postActionsSayAA10PostActionVGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-postActions" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-section#sdk-for-ios-navigate-s-7heresdk7SectionC11postActionsSayAA10PostActionVGvp" class="token"><code>postActions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The post actions that must be done after the arrival at the end of the section.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public private(set) lazy var postActions: [PostAction] { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-postaction">PostAction</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-sectionNotices" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-section#sdk-for-ios-navigate-s-7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp" class="token"><code>sectionNotices</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The notices which explain the issues encountered during processing of this section. For example, while the scooter transport mode is selected, if no reasonable alternative route is possible except violating controlled-access to highway rule for the section, one notice is generated for the violation. The user must judge all the notices carefully before proceeding.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public private(set) lazy var sectionNotices: [SectionNotice] { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-sectionnotice">SectionNotice</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7SectionC06indoorB7DetailsAA06IndoorbD0CSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-indoorSectionDetails" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-section#sdk-for-ios-navigate-s-7heresdk7SectionC06indoorB7DetailsAA06IndoorbD0CSgvp" class="token"><code>indoorSectionDetails</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indoor routing section information.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var indoorSectionDetails: IndoorSectionDetails? { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-indoorsectiondetails">IndoorSectionDetails</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7SectionC26consumptionInKilowattHoursSdSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-consumptionInKilowattHours" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-section#sdk-for-ios-navigate-s-7heresdk7SectionC26consumptionInKilowattHoursSdSgvp" class="token"><code>consumptionInKilowattHours</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Estimated net energy consumption (in kWh) if the transportation mode used for this route is an electric vehicle. Note that it can be negative due to energy recuperation.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var consumptionInKilowattHours: Double? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7SectionC14transitDetailsAA07TransitbD0VSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-transitDetails" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-section#sdk-for-ios-navigate-s-7heresdk7SectionC14transitDetailsAA07TransitbD0VSgvp" class="token"><code>transitDetails</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The transit details which are avilable for transit sections of a route.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var transitDetails: TransitSectionDetails? { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-transitsectiondetails">TransitSectionDetails</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7SectionC5tollsSayAA4TollVGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-tolls" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-section#sdk-for-ios-navigate-s-7heresdk7SectionC5tollsSayAA4TollVGvp" class="token"><code>tolls</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  All the tolls for this section. Note that tolls are found depending on the transport mode. For example, if pedestrian or bicycle transport mode specified, route sections have no tolls. Indoor route sections have no tolls, too. **Note**: If you’re using the <a href="sdk-for-ios-navigate-classes-offlineroutingengine">`OfflineRoutingEngine`</a>, be aware that this feature is currently in **beta**. As a result, there may be some bugs or unexpected behaviors. Additionally, this feature and related APIs may be updated in future releases without going through the deprecation process. Note that the <a href="sdk-for-ios-navigate-classes-offlineroutingengine">`OfflineRoutingEngine`</a> is only available with the Navigate license. If you’re using the <a href="sdk-for-ios-navigate-classes-routingengine">`RoutingEngine`</a>, this feature is considered to be stable.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public private(set) lazy var tolls: [Toll] { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-toll">Toll</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7SectionC16trafficIncidentsSayAA22TrafficIncidentOnRouteCGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-trafficIncidents" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-section#sdk-for-ios-navigate-s-7heresdk7SectionC16trafficIncidentsSayAA22TrafficIncidentOnRouteCGvp" class="token"><code>trafficIncidents</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of traffic incidents that are found on the section.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public private(set) lazy var trafficIncidents: [TrafficIncidentOnRoute] { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-trafficincidentonroute">TrafficIncidentOnRoute</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7SectionC8durationSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-duration" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-section#sdk-for-ios-navigate-s-7heresdk7SectionC8durationSdvp" class="token"><code>duration</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The estimated time in seconds needed to travel along this section, including real-time traffic delays if available.

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

   <span id="sdk-for-ios-navigate-s-7heresdk7SectionC12trafficDelaySdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-trafficDelay" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-section#sdk-for-ios-navigate-s-7heresdk7SectionC12trafficDelaySdvp" class="token"><code>trafficDelay</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The estimated extra time in seconds spent due to traffic delays along this section. Negative values indicate that the route can be traversed faster than usual.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var trafficDelay: TimeInterval { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7SectionC20passthroughWaypointsSayAA19PassThroughWaypointVGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-passthroughWaypoints" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-section#sdk-for-ios-navigate-s-7heresdk7SectionC20passthroughWaypointsSayAA19PassThroughWaypointVGvp" class="token"><code>passthroughWaypoints</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of passthrough waypoints in this section.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var passthroughWaypoints: [PassThroughWaypoint] { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-passthroughwaypoint">PassThroughWaypoint</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7SectionC21noThroughRestrictionsSayAA19ViolatedRestrictionVGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-noThroughRestrictions" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-section#sdk-for-ios-navigate-s-7heresdk7SectionC21noThroughRestrictionsSayAA19ViolatedRestrictionVGvp" class="token"><code>noThroughRestrictions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of no through restriction The no through restriction area is part of the road network that do not allow through traffic. For example the `Resident only` sign indicates that vehicles are only allowed to enter this area if they are making a stop. This area will be set only if `origin, destination` or `via` waypoint will be requested within the area.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var noThroughRestrictions: [ViolatedRestriction] { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-violatedrestriction">ViolatedRestriction</a>

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

