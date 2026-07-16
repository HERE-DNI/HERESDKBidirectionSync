---
title: "TransitRoutingEngine Class Reference"
slug: "sdk-for-ios-navigate-classes-transitroutingengine"
---

# TransitRoutingEngine

<div class="declaration">

<div class="language">

``` highlight
public class TransitRoutingEngine
```

``` highlight
extension TransitRoutingEngine: NativeBase
```

``` highlight
extension TransitRoutingEngine: Hashable
```

</div>

</div>

Use the TransitRoutingEngine to calculate a public transit route from A to B with a number of waypoints in between. Route calculation is done asynchronously and requires an online connection. The resulting route contains various information such as the polyline, route length in meters, estimated time to traverse along the route and maneuver data.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20TransitRoutingEngineCACyKcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-transitroutingengine#sdk-for-ios-navigate-s-7heresdk20TransitRoutingEngineCACyKcfc" class="token"><code>init()</code></a> 

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

  <a href="sdk-for-ios-navigate-core#sdk-for-ios-navigate-s-7heresdk18InstantiationErrora">`InstantiationError`</a> Indicates what went wrong when the instantiation was attempted.

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

   <span id="sdk-for-ios-navigate-s-7heresdk20TransitRoutingEngineCyAcA09SDKNativeD0CKcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-_" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-transitroutingengine#sdk-for-ios-navigate-s-7heresdk20TransitRoutingEngineCyAcA09SDKNativeD0CKcfc" class="token"><code>init(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of TransitRoutingEngine.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-core#sdk-for-ios-navigate-s-7heresdk18InstantiationErrora">`InstantiationError`</a> Indicates what went wrong when the instantiation was attempted.

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

  - <a href="sdk-for-ios-navigate-classes-sdknativeengine">SDKNativeEngine</a>

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

   <span id="sdk-for-ios-navigate-s-7heresdk20TransitRoutingEngineC14calculateRoute13startingPoint11destination12routeOptions10completionAA10TaskHandle_pAA0B8WaypointV_AkA0bfK0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-calculateRoute-startingPoint-destination-routeOptions-completion" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-transitroutingengine#sdk-for-ios-navigate-s-7heresdk20TransitRoutingEngineC14calculateRoute13startingPoint11destination12routeOptions10completionAA10TaskHandle_pAA0B8WaypointV_AkA0bfK0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF" class="token"><code>calculateRoute(startingPoint:</code><wbr></wbr><code>destination:</code><wbr></wbr><code>routeOptions:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously calculates a public transit route from the origin to the destination.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult
  public func calculateRoute(startingPoint: TransitWaypoint, destination: TransitWaypoint, routeOptions: TransitRouteOptions, completion: @escaping CalculateRouteCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-transitwaypoint">TransitWaypoint</a>
  - <a href="sdk-for-ios-navigate-structs-transitrouteoptions">TransitRouteOptions</a>
  - <a href="sdk-for-ios-navigate-routing#sdk-for-ios-navigate-s-7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a>
  - <a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a>

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
  <td><code> </code><em><code>startingPoint</code></em><code> </code></td>
  <td><div>
  <p>Position of starting point.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>destination</code></em><code> </code></td>
  <td><div>
  <p>Position of destination.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>routeOptions</code></em><code> </code></td>
  <td><div>
  <p>Options for public transit route calculation.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback object that will be invoked after route calculation. It is always invoked on the main thread.</p>
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

<div id="sdk-for-ios-navigate-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

