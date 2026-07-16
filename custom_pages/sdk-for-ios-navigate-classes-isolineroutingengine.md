---
title: "IsolineRoutingEngine Class Reference"
slug: "sdk-for-ios-navigate-classes-isolineroutingengine"
---

# IsolineRoutingEngine

<div class="declaration">

<div class="language">

``` highlight
public class IsolineRoutingEngine
```

``` highlight
extension IsolineRoutingEngine: NativeBase
```

``` highlight
extension IsolineRoutingEngine: Hashable
```

</div>

</div>

Use the IsolineRoutingEngine to calculate a reachable area from a center point. The calculation is done asynchronously and requires an online connection.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20IsolineRoutingEngineCACyKcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-isolineroutingengine#sdk-for-ios-navigate-s-7heresdk20IsolineRoutingEngineCACyKcfc" class="token"><code>init()</code></a> 

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

   <span id="sdk-for-ios-navigate-s-7heresdk20IsolineRoutingEngineC18connectionSettingsAcA0c10ConnectionF0V_tKcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-connectionSettings" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-isolineroutingengine#sdk-for-ios-navigate-s-7heresdk20IsolineRoutingEngineC18connectionSettingsAcA0c10ConnectionF0V_tKcfc" class="token"><code>init(connectionSettings:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of RoutingEngine.

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
  public init(connectionSettings: RoutingConnectionSettings) throws
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-routingconnectionsettings">RoutingConnectionSettings</a>

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
  <td><code> </code><em><code>connectionSettings</code></em><code> </code></td>
  <td><div>
  <p>Settings for the route calculation.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20IsolineRoutingEngineC_18connectionSettingsAcA09SDKNativeD0C_AA0c10ConnectionF0VtKcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-_-connectionSettings" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-isolineroutingengine#sdk-for-ios-navigate-s-7heresdk20IsolineRoutingEngineC_18connectionSettingsAcA09SDKNativeD0C_AA0c10ConnectionF0VtKcfc" class="token"><code>init(_:</code><wbr></wbr><code>connectionSettings:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of RoutingEngine.

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
  public init(_ sdkEngine: SDKNativeEngine, connectionSettings: RoutingConnectionSettings) throws
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-sdknativeengine">SDKNativeEngine</a>
  - <a href="sdk-for-ios-navigate-structs-routingconnectionsettings">RoutingConnectionSettings</a>

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
  <tr>
  <td><code> </code><em><code>connectionSettings</code></em><code> </code></td>
  <td><div>
  <p>Settings for the route calculation.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20IsolineRoutingEngineCyAcA09SDKNativeD0CKcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-_" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-isolineroutingengine#sdk-for-ios-navigate-s-7heresdk20IsolineRoutingEngineCyAcA09SDKNativeD0CKcfc" class="token"><code>init(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of IsolineRoutingEngine.

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

   <span id="sdk-for-ios-navigate-s-7heresdk20IsolineRoutingEngineC09calculateB06center14isolineOptions10completionAA10TaskHandle_pAA8WaypointV_AA0bH0VyAA0C5ErrorOSg_SayAA0B0CGSgtctF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-calculateIsoline-center-isolineOptions-completion" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-isolineroutingengine#sdk-for-ios-navigate-s-7heresdk20IsolineRoutingEngineC09calculateB06center14isolineOptions10completionAA10TaskHandle_pAA8WaypointV_AA0bH0VyAA0C5ErrorOSg_SayAA0B0CGSgtctF" class="token"><code>calculateIsoline(center:</code><wbr></wbr><code>isolineOptions:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Asynchronously calculates isolines to indicate the reachable area from a center point. This finds all destinations that can be reached in a specific amount of time, a maximum travel distance, or even the charge level available in an electric vehicle. The result is a polygon area where each point is reachable within the provided limit.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult
  public func calculateIsoline(center: Waypoint, isolineOptions: IsolineOptions, completion: @escaping CalculateIsolineCompletionHandler) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-waypoint">Waypoint</a>
  - <a href="sdk-for-ios-navigate-structs-isolineoptions">IsolineOptions</a>
  - <a href="sdk-for-ios-navigate-routing#sdk-for-ios-navigate-s-7heresdk33CalculateIsolineCompletionHandlera">CalculateIsolineCompletionHandler</a>
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
  <td><code> </code><em><code>center</code></em><code> </code></td>
  <td><div>
  <p>Center point from which isolines are calculated. At minimum, the waypoint must contain the coordinates as point of origin.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>isolineOptions</code></em><code> </code></td>
  <td><div>
  <p>Options for isoline calculation.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback object that will be invoked after isoline calculation. It is always invoked on the main thread.</p>
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

   <span id="sdk-for-ios-navigate-s-7heresdk20IsolineRoutingEngineC15setCustomOption4name5valueAA0C5ErrorOSgSS_SSSgtF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-setCustomOption-name-value" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-isolineroutingengine#sdk-for-ios-navigate-s-7heresdk20IsolineRoutingEngineC15setCustomOption4name5valueAA0C5ErrorOSgSS_SSSgtF" class="token"><code>setCustomOption(name:</code><wbr></wbr><code>value:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets a custom option for routing backend queries. The custom option is applied to all the queries that `IsolineRoutingEngine` performs. For a complete list of available parameter names and their valid values, refer to <a href="https://www.here.com/docs/bundle/batch-api-developer-guide/page/topics/constructing-request.html">HERE Routing API v8</a>. **Note:** It’s easy to set a wrong option that makes queries invalid, so make sure you read and understand the backend documentation.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setCustomOption(name: String, value: String?) -> RoutingError?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-routingerror">RoutingError</a>

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
  <td><code> </code><em><code>name</code></em><code> </code></td>
  <td><div>
  <p>An option name. If the engine already has an option with the same name, the option will be overwritten. The option name must be a non-empty string. The option name should’t duplicate option names that SDK creates by itself for usage in the query, otherwise the query will callback with the error <code>RoutingError.INTERNAL_ERROR</code>.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>value</code></em><code> </code></td>
  <td><div>
  <p>An option value. If the value is <code>nil</code>, the option will be removed. The option value must be a non-empty string.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  An optional error of setting the option. It’s `nil` if the option has been set successfully. It’s `RoutingError.INVALID_PARAMETER` if the input name and/or value haven’t passed internal validation.

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

