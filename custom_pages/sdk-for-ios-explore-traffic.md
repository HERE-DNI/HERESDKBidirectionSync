---
title: "Traffic  Reference"
slug: "sdk-for-ios-explore-traffic"
---

# Traffic

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19TrafficDataProviderC"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Class-TrafficDataProvider" class="dashAnchor"></span> <a href="sdk-for-ios-explore-traffic#sdk-for-ios-explore-s-7heresdk19TrafficDataProviderC" class="token"><code>TrafficDataProvider</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This protocol provides traffic information from radio signals to other HERE SDK modules. For now, only the <a href="sdk-for-ios-explore-classes-offlineroutingengine">`OfflineRoutingEngine`</a> is supported.

  For more information, take a look at the <a href="sdk-for-ios-explore-classes-trafficbroadcast">`TrafficBroadcast`</a> class, if available for your license.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class TrafficDataProvider
  ```

  ``` highlight
  extension TrafficDataProvider: NativeBase
  ```

  ``` highlight
  extension TrafficDataProvider: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk13TrafficEngineC"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Class-TrafficEngine" class="dashAnchor"></span> <a href="sdk-for-ios-explore-traffic#sdk-for-ios-explore-s-7heresdk13TrafficEngineC" class="token"><code>TrafficEngine</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Use the TrafficEngine to get information about current traffic flow and incidents in an area specified by <a href="sdk-for-ios-explore-structs-geobox">`GeoBox`</a>, <a href="sdk-for-ios-explore-structs-geocircle">`GeoCircle`</a>, or <a href="sdk-for-ios-explore-structs-geocorridor">`GeoCorridor`</a>. Provides optional parameters given in <a href="sdk-for-ios-explore-structs-trafficincidentsqueryoptions">`TrafficIncidentsQueryOptions`</a> and <a href="sdk-for-ios-explore-structs-trafficflowqueryoptions">`TrafficFlowQueryOptions`</a> to filter the result.

  By default, incidents are localized based on their geographical location. You can override that behavior by specifying the desired language that should be used for the incidents description and summary.

  The resulting traffic data contains information on incident types such as congestion, construction for road works, road hazard, road closure, weather updates for road condition, lane restriction and others.

  Traffic data is fetched online to get the most precise and freshest data available. In offline mode, live traffic data can be fetched using the traffic pass-through features. See <a href="sdk-for-ios-explore-classes-sdknativeengine#sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC19passThroughFeaturesShyAA04PassE7FeatureOGSgvp">`SDKNativeEngine.passThroughFeatures`</a>

  <a href="sdk-for-ios-explore-classes-trafficengine" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class TrafficEngine
  ```

  ``` highlight
  extension TrafficEngine: NativeBase
  ```

  ``` highlight
  extension TrafficEngine: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11TrafficFlowC"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Class-TrafficFlow" class="dashAnchor"></span> <a href="sdk-for-ios-explore-traffic#sdk-for-ios-explore-s-7heresdk11TrafficFlowC" class="token"><code>TrafficFlow</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This class provides details about traffic flow along a <a href="sdk-for-ios-explore-structs-geocorridor">`GeoCorridor`</a>, inside a <a href="sdk-for-ios-explore-structs-geocircle">`GeoCircle`</a> or a <a href="sdk-for-ios-explore-structs-geobox">`GeoBox`</a>, that represents particular path of the road network.\
  Backends for TrafficEngine and traffic vector tiles are different however backends may share the same data.\
  For additional information about fields, refer to <a href="https://www.here.com/docs/bundle/traffic-api-v7-api-reference/page/index.html#tag/Real-Time-Traffic">Traffic API v7 API Reference: Traffic API v7</a>.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-classes-trafficflow" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class TrafficFlow : TrafficFlowBase
  ```

  ``` highlight
  extension TrafficFlow: NativeBase
  ```

  ``` highlight
  extension TrafficFlow: Hashable
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-trafficflowbase">TrafficFlowBase</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15TrafficFlowBaseP"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Protocol-TrafficFlowBase" class="dashAnchor"></span> <a href="sdk-for-ios-explore-traffic#sdk-for-ios-explore-s-7heresdk15TrafficFlowBaseP" class="token"><code>TrafficFlowBase</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This interface provides details about a traffic flow.\
  For additional information about fields, refer to <a href="https://www.here.com/docs/bundle/traffic-api-v7-api-reference/page/index.html#tag/Real-Time-Traffic">Traffic API v7 API Reference: Traffic API v7</a>.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-protocols-trafficflowbase" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol TrafficFlowBase : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk23TrafficFlowQueryOptionsV"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Struct-TrafficFlowQueryOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-traffic#sdk-for-ios-explore-s-7heresdk23TrafficFlowQueryOptionsV" class="token"><code>TrafficFlowQueryOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The options to specify how traffic flow data should be queried.

  <a href="sdk-for-ios-explore-structs-trafficflowqueryoptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TrafficFlowQueryOptions : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk33TrafficFlowQueryCompletionHandlera"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Alias-TrafficFlowQueryCompletionHandler" class="dashAnchor"></span> <a href="sdk-for-ios-explore-traffic#sdk-for-ios-explore-s-7heresdk33TrafficFlowQueryCompletionHandlera" class="token"><code>TrafficFlowQueryCompletionHandler</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Callback passed to following functions:

      TrafficEngine.queryForFlow(GeoBox, TrafficFlowQueryOptions, TrafficFlowQueryCompletionHandler)

      TrafficEngine.queryForFlow(GeoCircle, TrafficFlowQueryOptions, TrafficFlowQueryCompletionHandler)

      TrafficEngine.queryForFlow(GeoCorridor, TrafficFlowQueryOptions, TrafficFlowQueryCompletionHandler)

  The method will be called on the main thread when a search call has been completed. The first argument is the error in the case of the failure. It is `nil` for an operation that succeeds. The second argument is the list of flow items in the case of the success. It is `nil` in case of an error.
  </p>

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias TrafficFlowQueryCompletionHandler = (_ queryError: TrafficQueryError?, _ result: [TrafficFlow]?) -> Void
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-trafficqueryerror">TrafficQueryError</a>
  - <a href="sdk-for-ios-explore-classes-trafficflow">TrafficFlow</a>

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
  <td><code> </code><em><code>queryError</code></em><code> </code></td>
  <td><div>
  <p>The error in the case of the failure. It is <code>nil</code> for an operation that succeeds.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>result</code></em><code> </code></td>
  <td><div>
  <p>The list of incidents in the case of the success. It is <code>nil</code> in case of an error.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15TrafficIncidentC"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Class-TrafficIncident" class="dashAnchor"></span> <a href="sdk-for-ios-explore-traffic#sdk-for-ios-explore-s-7heresdk15TrafficIncidentC" class="token"><code>TrafficIncident</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  TrafficIncident provides details about a traffic incident.

  <a href="sdk-for-ios-explore-classes-trafficincident" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class TrafficIncident : TrafficIncidentBase
  ```

  ``` highlight
  extension TrafficIncident: NativeBase
  ```

  ``` highlight
  extension TrafficIncident: Hashable
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-trafficincidentbase">TrafficIncidentBase</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19TrafficIncidentBaseP"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Protocol-TrafficIncidentBase" class="dashAnchor"></span> <a href="sdk-for-ios-explore-traffic#sdk-for-ios-explore-s-7heresdk19TrafficIncidentBaseP" class="token"><code>TrafficIncidentBase</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  TrafficIncident provides details about a traffic incident.

  <a href="sdk-for-ios-explore-protocols-trafficincidentbase" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol TrafficIncidentBase : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk32TrafficIncidentCompletionHandlera"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Alias-TrafficIncidentCompletionHandler" class="dashAnchor"></span> <a href="sdk-for-ios-explore-traffic#sdk-for-ios-explore-s-7heresdk32TrafficIncidentCompletionHandlera" class="token"><code>TrafficIncidentCompletionHandler</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Callback passed to <a href="sdk-for-ios-explore-classes-trafficengine#sdk-for-ios-explore-s-7heresdk13TrafficEngineC14lookupIncident4with0D7Options10completionAA10TaskHandle_pSS_AA0be6LookupG0VyAA0B10QueryErrorOSg_AA0bE0CSgtctF">`TrafficEngine.lookupIncident(...)`</a>. The method will be called on the main thread when a search call has been completed. The first argument is the error in the case of the failure. It is `nil` for an operation that succeeds. The second argument is the incident in the case of the success. It is `nil` in case of an error.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias TrafficIncidentCompletionHandler = (_ queryError: TrafficQueryError?, _ result: TrafficIncident?) -> Void
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-trafficqueryerror">TrafficQueryError</a>
  - <a href="sdk-for-ios-explore-classes-trafficincident">TrafficIncident</a>

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
  <td><code> </code><em><code>queryError</code></em><code> </code></td>
  <td><div>
  <p>The error in the case of the failure. It is <code>nil</code> for an operation that succeeds.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>result</code></em><code> </code></td>
  <td><div>
  <p>The incident in the case of the success. It is <code>nil</code> in case of an error.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk21TrafficIncidentImpactO"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Enum-TrafficIncidentImpact" class="dashAnchor"></span> <a href="sdk-for-ios-explore-traffic#sdk-for-ios-explore-s-7heresdk21TrafficIncidentImpactO" class="token"><code>TrafficIncidentImpact</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Impact of a traffic incident.

  <a href="sdk-for-ios-explore-enums-trafficincidentimpact" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum TrafficIncidentImpact : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk28TrafficIncidentLookupOptionsV"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Struct-TrafficIncidentLookupOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-traffic#sdk-for-ios-explore-s-7heresdk28TrafficIncidentLookupOptionsV" class="token"><code>TrafficIncidentLookupOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  All the options to specify how a single incident should be queried.

  <a href="sdk-for-ios-explore-structs-trafficincidentlookupoptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TrafficIncidentLookupOptions : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22TrafficIncidentOnRouteC"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Class-TrafficIncidentOnRoute" class="dashAnchor"></span> <a href="sdk-for-ios-explore-traffic#sdk-for-ios-explore-s-7heresdk22TrafficIncidentOnRouteC" class="token"><code>TrafficIncidentOnRoute</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Traffic incidents on a route. Use <a href="sdk-for-ios-explore-classes-section#sdk-for-ios-explore-s-7heresdk7SectionC16trafficIncidentsSayAA22TrafficIncidentOnRouteCGvp">`Section.trafficIncidents`</a> to get a list of incidents on a route section. Use <a href="sdk-for-ios-explore-classes-span#sdk-for-ios-explore-s-7heresdk4SpanC22trafficIncidentIndexesSays5Int32VGvp">`Span.trafficIncidentIndexes`</a> to associate incidents with spans. Each incident takes at least the whole geometry of matching spans. Also, an incident can take some place out of the built route.

  <a href="sdk-for-ios-explore-classes-trafficincidentonroute" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class TrafficIncidentOnRoute : TrafficIncidentBase
  ```

  ``` highlight
  extension TrafficIncidentOnRoute: NativeBase
  ```

  ``` highlight
  extension TrafficIncidentOnRoute: Hashable
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-trafficincidentbase">TrafficIncidentBase</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19TrafficIncidentTypeO"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Enum-TrafficIncidentType" class="dashAnchor"></span> <a href="sdk-for-ios-explore-traffic#sdk-for-ios-explore-s-7heresdk19TrafficIncidentTypeO" class="token"><code>TrafficIncidentType</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Category of a traffic incident.

  <a href="sdk-for-ios-explore-enums-trafficincidenttype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum TrafficIncidentType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk38TrafficIncidentsQueryCompletionHandlera"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Alias-TrafficIncidentsQueryCompletionHandler" class="dashAnchor"></span> <a href="sdk-for-ios-explore-traffic#sdk-for-ios-explore-s-7heresdk38TrafficIncidentsQueryCompletionHandlera" class="token"><code>TrafficIncidentsQueryCompletionHandler</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Callback passed to

      TrafficEngine.queryForIncidents(GeoCorridor, TrafficIncidentsQueryOptions, TrafficIncidentsQueryCompletionHandler)

  . The method will be called on the main thread when a search call has been completed. The first argument is the error in the case of the failure. It is `nil` for an operation that succeeds. The second argument is the list of incidents in the case of the success. It is `nil` in case of an error.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias TrafficIncidentsQueryCompletionHandler = (_ queryError: TrafficQueryError?, _ result: [TrafficIncident]?) -> Void
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-trafficqueryerror">TrafficQueryError</a>
  - <a href="sdk-for-ios-explore-classes-trafficincident">TrafficIncident</a>

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
  <td><code> </code><em><code>queryError</code></em><code> </code></td>
  <td><div>
  <p>The error in the case of the failure. It is <code>nil</code> for an operation that succeeds.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>result</code></em><code> </code></td>
  <td><div>
  <p>The list of incidents in the case of the success. It is <code>nil</code> in case of an error.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk28TrafficIncidentsQueryOptionsV"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Struct-TrafficIncidentsQueryOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-traffic#sdk-for-ios-explore-s-7heresdk28TrafficIncidentsQueryOptionsV" class="token"><code>TrafficIncidentsQueryOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The options to specify how incidents should be queried.

  <a href="sdk-for-ios-explore-structs-trafficincidentsqueryoptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TrafficIncidentsQueryOptions : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15TrafficLocationV"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Struct-TrafficLocation" class="dashAnchor"></span> <a href="sdk-for-ios-explore-traffic#sdk-for-ios-explore-s-7heresdk15TrafficLocationV" class="token"><code>TrafficLocation</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The location reference to the traffic incident.

  <a href="sdk-for-ios-explore-structs-trafficlocation" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct TrafficLocation : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17TrafficQueryErrorO"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Enum-TrafficQueryError" class="dashAnchor"></span> <a href="sdk-for-ios-explore-traffic#sdk-for-ios-explore-s-7heresdk17TrafficQueryErrorO" class="token"><code>TrafficQueryError</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents various errors that could occur from a traffic queries.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-enums-trafficqueryerror" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum TrafficQueryError : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14TraversabilityO"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Enum-Traversability" class="dashAnchor"></span> <a href="sdk-for-ios-explore-traffic#sdk-for-ios-explore-s-7heresdk14TraversabilityO" class="token"><code>Traversability</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Junctions traversability of some traffic incident or flow section.

  <a href="sdk-for-ios-explore-enums-traversability" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum Traversability : UInt32, CaseIterable, Codable
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

