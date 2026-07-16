---
title: "TrafficEngine Class Reference"
slug: "sdk-for-ios-explore-classes-trafficengine"
---

# TrafficEngine

<div class="declaration">

<div class="language">

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

Use the TrafficEngine to get information about current traffic flow and incidents in an area specified by <a href="sdk-for-ios-explore-structs-geobox">`GeoBox`</a>, <a href="sdk-for-ios-explore-structs-geocircle">`GeoCircle`</a>, or <a href="sdk-for-ios-explore-structs-geocorridor">`GeoCorridor`</a>. Provides optional parameters given in <a href="sdk-for-ios-explore-structs-trafficincidentsqueryoptions">`TrafficIncidentsQueryOptions`</a> and <a href="sdk-for-ios-explore-structs-trafficflowqueryoptions">`TrafficFlowQueryOptions`</a> to filter the result.

By default, incidents are localized based on their geographical location. You can override that behavior by specifying the desired language that should be used for the incidents description and summary.

The resulting traffic data contains information on incident types such as congestion, construction for road works, road hazard, road closure, weather updates for road condition, lane restriction and others.

Traffic data is fetched online to get the most precise and freshest data available. In offline mode, live traffic data can be fetched using the traffic pass-through features. See <a href="sdk-for-ios-explore-classes-sdknativeengine#sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC19passThroughFeaturesShyAA04PassE7FeatureOGSgvp">`SDKNativeEngine.passThroughFeatures`</a>

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk13TrafficEngineCACyKcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-trafficengine#sdk-for-ios-explore-s-7heresdk13TrafficEngineCACyKcfc" class="token"><code>init()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of this class.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-explore-core#sdk-for-ios-explore-s-7heresdk18InstantiationErrora">`InstantiationError`</a> Indicates what went wrong when the instantiation was attempted.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init() throws
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk13TrafficEngineCyAcA09SDKNativeC0CKcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-trafficengine#sdk-for-ios-explore-s-7heresdk13TrafficEngineCyAcA09SDKNativeC0CKcfc" class="token"><code>init(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of this class.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-explore-core#sdk-for-ios-explore-s-7heresdk18InstantiationErrora">`InstantiationError`</a> Indicates what went wrong when the instantiation was attempted.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(_ sdkEngine: SDKNativeEngine) throws
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-sdknativeengine">SDKNativeEngine</a>

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
  <td><code> </code><em><code>sdkEngine</code></em><code> </code></td>
  <td><div>
  <p>An SDKEngine instance.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk13TrafficEngineC17queryForIncidents6inside0D7Options10completionAA10TaskHandle_pAA6GeoBoxV_AA0bf5QueryH0VyAA0bN5ErrorOSg_SayAA0B8IncidentCGSgtctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-queryForIncidents-inside-queryOptions-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-trafficengine#sdk-for-ios-explore-s-7heresdk13TrafficEngineC17queryForIncidents6inside0D7Options10completionAA10TaskHandle_pAA6GeoBoxV_AA0bf5QueryH0VyAA0bN5ErrorOSg_SayAA0B8IncidentCGSgtctF" class="token"><code>queryForIncidents(inside:</code><wbr></wbr><code>queryOptions:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously queries for traffic incidents using a bounding box as a filter.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult
  public func queryForIncidents(inside boxArea: GeoBox, queryOptions: TrafficIncidentsQueryOptions, completion: @escaping TrafficIncidentsQueryCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geobox">GeoBox</a>
  - <a href="sdk-for-ios-explore-structs-trafficincidentsqueryoptions">TrafficIncidentsQueryOptions</a>
  - <a href="sdk-for-ios-explore-traffic#sdk-for-ios-explore-s-7heresdk38TrafficIncidentsQueryCompletionHandlera">TrafficIncidentsQueryCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>

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
  <td><code> </code><em><code>boxArea</code></em><code> </code></td>
  <td><div>
  <p>The bounding box area to search for traffic incidents. The maximum width and height for a bounding box filter is 1 degree.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>queryOptions</code></em><code> </code></td>
  <td><div>
  <p>The options which are specific for incidents query.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>It is always invoked on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk13TrafficEngineC17queryForIncidents6inside0D7Options10completionAA10TaskHandle_pAA9GeoCircleV_AA0bf5QueryH0VyAA0bN5ErrorOSg_SayAA0B8IncidentCGSgtctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-queryForIncidents-inside-queryOptions-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-trafficengine#sdk-for-ios-explore-s-7heresdk13TrafficEngineC17queryForIncidents6inside0D7Options10completionAA10TaskHandle_pAA9GeoCircleV_AA0bf5QueryH0VyAA0bN5ErrorOSg_SayAA0B8IncidentCGSgtctF" class="token"><code>queryForIncidents(inside:</code><wbr></wbr><code>queryOptions:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously queries for traffic incidents using a circle as a filter.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult
  public func queryForIncidents(inside circleArea: GeoCircle, queryOptions: TrafficIncidentsQueryOptions, completion: @escaping TrafficIncidentsQueryCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocircle">GeoCircle</a>
  - <a href="sdk-for-ios-explore-structs-trafficincidentsqueryoptions">TrafficIncidentsQueryOptions</a>
  - <a href="sdk-for-ios-explore-traffic#sdk-for-ios-explore-s-7heresdk38TrafficIncidentsQueryCompletionHandlera">TrafficIncidentsQueryCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>

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
  <td><code> </code><em><code>circleArea</code></em><code> </code></td>
  <td><div>
  <p>The circle area to search for traffic incidents. The maximum radius of the circle filter is 50000 meters.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>queryOptions</code></em><code> </code></td>
  <td><div>
  <p>The options which are specific for incidents query.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>It is always invoked on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk13TrafficEngineC17queryForIncidents6inside0D7Options10completionAA10TaskHandle_pAA11GeoCorridorV_AA0bf5QueryH0VyAA0bN5ErrorOSg_SayAA0B8IncidentCGSgtctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-queryForIncidents-inside-queryOptions-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-trafficengine#sdk-for-ios-explore-s-7heresdk13TrafficEngineC17queryForIncidents6inside0D7Options10completionAA10TaskHandle_pAA11GeoCorridorV_AA0bf5QueryH0VyAA0bN5ErrorOSg_SayAA0B8IncidentCGSgtctF" class="token"><code>queryForIncidents(inside:</code><wbr></wbr><code>queryOptions:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously queries for traffic incidents by a corridor as a filter.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult
  public func queryForIncidents(inside corridorArea: GeoCorridor, queryOptions: TrafficIncidentsQueryOptions, completion: @escaping TrafficIncidentsQueryCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocorridor">GeoCorridor</a>
  - <a href="sdk-for-ios-explore-structs-trafficincidentsqueryoptions">TrafficIncidentsQueryOptions</a>
  - <a href="sdk-for-ios-explore-traffic#sdk-for-ios-explore-s-7heresdk38TrafficIncidentsQueryCompletionHandlera">TrafficIncidentsQueryCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>

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
  <td><code> </code><em><code>corridorArea</code></em><code> </code></td>
  <td><div>
  <p>The corridor box to search for traffic incidents. The maximum length for the corridor is 500000 meters and the maximum <code>GeoCorridor.half_width_in_meters</code> is 5000 meters. If the number of points in corridor is greater than 300 then request is split into smaller ones and results are aggregated into single response, this will result in multiple requests to the backend. This process does not change a shape of the corridor.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>queryOptions</code></em><code> </code></td>
  <td><div>
  <p>The options which are specific for incidents query.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>It is always invoked on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk13TrafficEngineC14lookupIncident4with0D7Options10completionAA10TaskHandle_pSS_AA0be6LookupG0VyAA0B10QueryErrorOSg_AA0bE0CSgtctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-lookupIncident-with-lookupOptions-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-trafficengine#sdk-for-ios-explore-s-7heresdk13TrafficEngineC14lookupIncident4with0D7Options10completionAA10TaskHandle_pSS_AA0be6LookupG0VyAA0B10QueryErrorOSg_AA0bE0CSgtctF" class="token"><code>lookupIncident(with:</code><wbr></wbr><code>lookupOptions:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously queries for traffic incident by the original id. See <a href="sdk-for-ios-explore-classes-trafficincident#sdk-for-ios-explore-s-7heresdk15TrafficIncidentC10originalIdSSvp">`TrafficIncident.originalId`</a> for more information.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult
  public func lookupIncident(with originalId: String, lookupOptions: TrafficIncidentLookupOptions, completion: @escaping TrafficIncidentCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-trafficincidentlookupoptions">TrafficIncidentLookupOptions</a>
  - <a href="sdk-for-ios-explore-traffic#sdk-for-ios-explore-s-7heresdk32TrafficIncidentCompletionHandlera">TrafficIncidentCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>

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
  <td><code> </code><em><code>originalId</code></em><code> </code></td>
  <td><div>
  <p>The requested incident original id.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>lookupOptions</code></em><code> </code></td>
  <td><div>
  <p>The options which are specific for the incident lookup query.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>The callback object that will be invoked after the incident lookup query. It is always invoked on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk13TrafficEngineC12queryForFlow6inside0D7Options10completionAA10TaskHandle_pAA6GeoBoxV_AA0bf5QueryH0VyAA0bN5ErrorOSg_SayAA0bF0CGSgtctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-queryForFlow-inside-queryOptions-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-trafficengine#sdk-for-ios-explore-s-7heresdk13TrafficEngineC12queryForFlow6inside0D7Options10completionAA10TaskHandle_pAA6GeoBoxV_AA0bf5QueryH0VyAA0bN5ErrorOSg_SayAA0bF0CGSgtctF" class="token"><code>queryForFlow(inside:</code><wbr></wbr><code>queryOptions:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously queries for traffic flow using a bounding box as a filter.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult
  public func queryForFlow(inside boxArea: GeoBox, queryOptions: TrafficFlowQueryOptions, completion: @escaping TrafficFlowQueryCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geobox">GeoBox</a>
  - <a href="sdk-for-ios-explore-structs-trafficflowqueryoptions">TrafficFlowQueryOptions</a>
  - <a href="sdk-for-ios-explore-traffic#sdk-for-ios-explore-s-7heresdk33TrafficFlowQueryCompletionHandlera">TrafficFlowQueryCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>

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
  <td><code> </code><em><code>boxArea</code></em><code> </code></td>
  <td><div>
  <p>The bounding box area to search for traffic flow.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>queryOptions</code></em><code> </code></td>
  <td><div>
  <p>The options which are specific for flow query.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>It is always invoked on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk13TrafficEngineC12queryForFlow6inside0D7Options10completionAA10TaskHandle_pAA9GeoCircleV_AA0bf5QueryH0VyAA0bN5ErrorOSg_SayAA0bF0CGSgtctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-queryForFlow-inside-queryOptions-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-trafficengine#sdk-for-ios-explore-s-7heresdk13TrafficEngineC12queryForFlow6inside0D7Options10completionAA10TaskHandle_pAA9GeoCircleV_AA0bf5QueryH0VyAA0bN5ErrorOSg_SayAA0bF0CGSgtctF" class="token"><code>queryForFlow(inside:</code><wbr></wbr><code>queryOptions:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously queries for traffic flow using a circle as a filter.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult
  public func queryForFlow(inside circleArea: GeoCircle, queryOptions: TrafficFlowQueryOptions, completion: @escaping TrafficFlowQueryCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocircle">GeoCircle</a>
  - <a href="sdk-for-ios-explore-structs-trafficflowqueryoptions">TrafficFlowQueryOptions</a>
  - <a href="sdk-for-ios-explore-traffic#sdk-for-ios-explore-s-7heresdk33TrafficFlowQueryCompletionHandlera">TrafficFlowQueryCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>

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
  <td><code> </code><em><code>circleArea</code></em><code> </code></td>
  <td><div>
  <p>The circle area to search for traffic flow. The maximum radius of the circle filter is 50000 meters.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>queryOptions</code></em><code> </code></td>
  <td><div>
  <p>The options which are specific for flow query.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>It is always invoked on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk13TrafficEngineC12queryForFlow6inside0D7Options10completionAA10TaskHandle_pAA11GeoCorridorV_AA0bf5QueryH0VyAA0bN5ErrorOSg_SayAA0bF0CGSgtctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-queryForFlow-inside-queryOptions-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-trafficengine#sdk-for-ios-explore-s-7heresdk13TrafficEngineC12queryForFlow6inside0D7Options10completionAA10TaskHandle_pAA11GeoCorridorV_AA0bf5QueryH0VyAA0bN5ErrorOSg_SayAA0bF0CGSgtctF" class="token"><code>queryForFlow(inside:</code><wbr></wbr><code>queryOptions:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously queries for traffic flow by a corridor as a filter.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult
  public func queryForFlow(inside corridorArea: GeoCorridor, queryOptions: TrafficFlowQueryOptions, completion: @escaping TrafficFlowQueryCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocorridor">GeoCorridor</a>
  - <a href="sdk-for-ios-explore-structs-trafficflowqueryoptions">TrafficFlowQueryOptions</a>
  - <a href="sdk-for-ios-explore-traffic#sdk-for-ios-explore-s-7heresdk33TrafficFlowQueryCompletionHandlera">TrafficFlowQueryCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>

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
  <td><code> </code><em><code>corridorArea</code></em><code> </code></td>
  <td><div>
  <p>The corridor box to search for traffic flow. The maximum length for the corridor is 500000 meters and the maximum <code>GeoCorridor.half_width_in_meters</code> is 5000 meters.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>queryOptions</code></em><code> </code></td>
  <td><div>
  <p>The options which are specific for flow query.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>It is always invoked on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task.

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

