---
title: "Route Class Reference"
slug: "sdk-for-ios-explore-classes-route"
---

# Route

<div class="declaration">

<div class="language">

``` highlight
public class Route
```

``` highlight
extension Route: NativeBase
```

``` highlight
extension Route: Hashable
```

</div>

</div>

A route is a path through a road network over which someone travels.

**Note:** Each <a href="sdk-for-ios-explore-classes-section">`Section`</a> of a route contains a list of <a href="sdk-for-ios-explore-structs-sectionnotice">`SectionNotice`</a> objects that describe *potential issues* after the route was calculated. If the list is non-empty, it is recommended to evaluate possible violations against the requested route options and reject the route if deemed necessary.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk5RouteC8sectionsSayAA7SectionCGvp"></span>` `<span id="//apple_ref/swift/Property/sections" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-route#/s:7heresdk5RouteC8sectionsSayAA7SectionCGvp" class="token"><code>sections</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The sections that make up this route.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public private(set) lazy var sections : [ Section ] { get set }
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk5RouteC8geometryAA11GeoPolylineVvp"></span>` `<span id="//apple_ref/swift/Property/geometry" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-route#/s:7heresdk5RouteC8geometryAA11GeoPolylineVvp" class="token"><code>geometry</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The <a href="sdk-for-ios-explore-structs-geopolyline">`GeoPolyline`</a> object representing the polyline of this route. It may not contain the original coordinates specified in the request for a route.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public private(set) lazy var geometry : GeoPolyline { get set }
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk5RouteC11boundingBoxAA03GeoD0Vvp"></span>` `<span id="//apple_ref/swift/Property/boundingBox" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-route#/s:7heresdk5RouteC11boundingBoxAA03GeoD0Vvp" class="token"><code>boundingBox</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The closest rectangular area where this route fits in.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var boundingBox: GeoBox { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk5RouteC14lengthInMeterss5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/lengthInMeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-route#/s:7heresdk5RouteC14lengthInMeterss5Int32Vvp" class="token"><code>lengthInMeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The length of this route in meters.

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

  ` `<span id="/s:7heresdk5RouteC8languageAA12LanguageCodeOvp"></span>` `<span id="//apple_ref/swift/Property/language" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-route#/s:7heresdk5RouteC8languageAA12LanguageCodeOvp" class="token"><code>language</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the language requested for all textual information related to this route.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var language: LanguageCode { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk5RouteC16optimizationModeAA012OptimizationD0Ovp"></span>` `<span id="//apple_ref/swift/Property/optimizationMode" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-route#/s:7heresdk5RouteC16optimizationModeAA012OptimizationD0Ovp" class="token"><code>optimizationMode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The optimization mode requested for route calculation.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var optimizationMode: OptimizationMode { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk5RouteC22requestedTransportModeAA0dE0Ovp"></span>` `<span id="//apple_ref/swift/Property/requestedTransportMode" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-route#/s:7heresdk5RouteC22requestedTransportModeAA0dE0Ovp" class="token"><code>requestedTransportMode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The transport mode requested for route calculation.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var requestedTransportMode: TransportMode { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk5RouteC26consumptionInKilowattHoursSdSgvp"></span>` `<span id="//apple_ref/swift/Property/consumptionInKilowattHours" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-route#/s:7heresdk5RouteC26consumptionInKilowattHoursSdSgvp" class="token"><code>consumptionInKilowattHours</code></a>` `

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

  ` `<span id="/s:7heresdk5RouteC11routeHandleAA0bD0VSgvp"></span>` `<span id="//apple_ref/swift/Property/routeHandle" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-route#/s:7heresdk5RouteC11routeHandleAA0bD0VSgvp" class="token"><code>routeHandle</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The route handle of this route. Note that it is provided only if <a href="sdk-for-ios-explore-structs-routeoptions#/s:7heresdk12RouteOptionsV06enableB6HandleSbvp">`RouteOptions.enableRouteHandle`</a> is set before route calculation.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var routeHandle: RouteHandle? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk5RouteC8durationSdvp"></span>` `<span id="//apple_ref/swift/Property/duration" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-route#/s:7heresdk5RouteC8durationSdvp" class="token"><code>duration</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The estimated time in seconds needed to travel along this route, including real-time traffic delays if available.

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

  ` `<span id="/s:7heresdk5RouteC12trafficDelaySdvp"></span>` `<span id="//apple_ref/swift/Property/trafficDelay" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-route#/s:7heresdk5RouteC12trafficDelaySdvp" class="token"><code>trafficDelay</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The estimated time in seconds spent in traffic along this route. Negative values indicate that the route can be traversed faster than usual.

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

  ` `<span id="/s:7heresdk5RouteC14routingOptionsAA07RoutingD0VSgvp"></span>` `<span id="//apple_ref/swift/Property/routingOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-route#/s:7heresdk5RouteC14routingOptionsAA07RoutingD0VSgvp" class="token"><code>routingOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The set of options used to calculate the route.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var routingOptions: RoutingOptions? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk5RouteC16railwayCrossingsSayAA0B15RailwayCrossingVGvp"></span>` `<span id="//apple_ref/swift/Property/railwayCrossings" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-route#/s:7heresdk5RouteC16railwayCrossingsSayAA0B15RailwayCrossingVGvp" class="token"><code>railwayCrossings</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Collection of railway crossings along the route. Railway crossing information is only available for routes created with the online <a href="sdk-for-ios-explore-classes-routingengine">`RoutingEngine`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public private(set) lazy var railwayCrossings : [ RouteRailwayCrossing ] { get set }
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk5RouteC11routeLabelsSayAA0B5LabelVGvp"></span>` `<span id="//apple_ref/swift/Property/routeLabels" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-route#/s:7heresdk5RouteC11routeLabelsSayAA0B5LabelVGvp" class="token"><code>routeLabels</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A collection containing a maximum of 2 <a href="sdk-for-ios-explore-structs-routelabel">`RouteLabel`</a> instances for the route. It will return an empty list if no labels are available. The main street names or route numbers through which the route is going to pass that differentiate it from other alternatives routes. The labels are ordered by importance based on how much time the route spends on each road segment, not by traversal sequence. This helps users quickly identify and distinguish between different route alternatives when alternative routes have been quested via <a href="sdk-for-ios-explore-structs-routeoptions">`RouteOptions`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public private(set) lazy var routeLabels : [ RouteLabel ] { get set }
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      serialize(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Serializes given route to a binary data. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func serialize ( _ route : Route ) -> Data ?
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
  <td><code> </code><em><code>route</code></em><code> </code></td>
  <td><div>
  <p>The route which should be serialized.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The binary data of the route.

  </div>

  </div>

  </div>

- <div>

      deserialize(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates route from the given binary data. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func deserialize ( _ routeData : Data ) -> Route ?
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
  <td><code> </code><em><code>routeData</code></em><code> </code></td>
  <td><div>
  <p>The binary of a serialized route.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The route object restored from the binary data.

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

