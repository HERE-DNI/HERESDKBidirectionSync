---
title: "TrafficBroadcast Class Reference"
slug: "sdk-for-ios-explore-classes-trafficbroadcast"
---

# TrafficBroadcast

<div class="declaration">

<div class="language">

``` highlight
public class TrafficBroadcast : LocationDelegate
```

``` highlight
extension TrafficBroadcast: NativeBase
```

``` highlight
extension TrafficBroadcast: Hashable
```

</div>

Related types:

- <a href="sdk-for-ios-explore-protocols-locationdelegate">LocationDelegate</a>

</div>

A `TrafficBroadcast` is expecting the <a href="https://en.wikipedia.org/wiki/Traffic_message_channel">RDS-TMC</a> format and it can be used when there is no internet connection, so that the <a href="sdk-for-ios-explore-classes-offlineroutingengine">`OfflineRoutingEngine`</a> can utilize traffic data coming over a radio channel. The <a href="sdk-for-ios-explore-classes-trafficbroadcast#sdk-for-ios-explore-s-7heresdk16TrafficBroadcastC8activateyyF">`TrafficBroadcast.activate(...)`</a> method needs to be called to receive traffic data events.

**Note:** In order to adopt the <a href="sdk-for-ios-explore-traffic#sdk-for-ios-explore-s-7heresdk19TrafficDataProviderC">`TrafficDataProvider`</a> interface special hardware is required. Talk to your HERE representative for more details. Only by adopting the <a href="sdk-for-ios-explore-traffic#sdk-for-ios-explore-s-7heresdk19TrafficDataProviderC">`TrafficDataProvider`</a> interface you can integrate radio station signals providing traffic broadcasts. Traffic broadcasts are meant to be used *independently* from the already included traffic on routes, on the map and from the HERE backends (when using the <a href="sdk-for-ios-explore-classes-trafficengine">`TrafficEngine`</a>).

This class continuously reacts to new locations provided from a location source and acts as a <a href="sdk-for-ios-explore-protocols-locationdelegate">`LocationDelegate`</a>. The location must be updated regardless of calling <a href="sdk-for-ios-explore-classes-trafficbroadcast#sdk-for-ios-explore-s-7heresdk16TrafficBroadcastC8activateyyF">`TrafficBroadcast.activate(...)`</a>.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16TrafficBroadcastC10parametersAcA0bC10ParametersV_tKcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-parameters" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-trafficbroadcast#sdk-for-ios-explore-s-7heresdk16TrafficBroadcastC10parametersAcA0bC10ParametersV_tKcfc" class="token"><code>init(parameters:</code><wbr></wbr><code>)</code></a> 

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

  <a href="sdk-for-ios-explore-core#sdk-for-ios-explore-s-7heresdk18InstantiationErrora">`InstantiationError`</a> when the object was not initialized properly.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(parameters: TrafficBroadcastParameters) throws
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-trafficbroadcastparameters">TrafficBroadcastParameters</a>

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
  <td><code> </code><em><code>parameters</code></em><code> </code></td>
  <td><div>
  <p>The necessary parameters to start traffic broadcast.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16TrafficBroadcastC_10parametersAcA15SDKNativeEngineC_AA0bC10ParametersVtKcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-_-parameters" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-trafficbroadcast#sdk-for-ios-explore-s-7heresdk16TrafficBroadcastC_10parametersAcA15SDKNativeEngineC_AA0bC10ParametersVtKcfc" class="token"><code>init(_:</code><wbr></wbr><code>parameters:</code><wbr></wbr><code>)</code></a> 

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

  <a href="sdk-for-ios-explore-core#sdk-for-ios-explore-s-7heresdk18InstantiationErrora">`InstantiationError`</a> when the object was not initialized properly.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(_ sdkEngine: SDKNativeEngine, parameters: TrafficBroadcastParameters) throws
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-sdknativeengine">SDKNativeEngine</a>
  - <a href="sdk-for-ios-explore-structs-trafficbroadcastparameters">TrafficBroadcastParameters</a>

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
  <p>Instance of an existing SDKEngine.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>parameters</code></em><code> </code></td>
  <td><div>
  <p>The necessary parameters to start traffic broadcast.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16TrafficBroadcastC19trafficDataProviderAA0beF0CSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-trafficDataProvider" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-trafficbroadcast#sdk-for-ios-explore-s-7heresdk16TrafficBroadcastC19trafficDataProviderAA0beF0CSgvp" class="token"><code>trafficDataProvider</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The traffic data provider that provides the traffic information.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var trafficDataProvider: TrafficDataProvider? { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-traffic#sdk-for-ios-explore-s-7heresdk19TrafficDataProviderC">TrafficDataProvider</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16TrafficBroadcastC17onLocationUpdatedyyAA0E0VF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-onLocationUpdated-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-trafficbroadcast#sdk-for-ios-explore-s-7heresdk16TrafficBroadcastC17onLocationUpdatedyyAA0E0VF" class="token"><code>onLocationUpdated(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Called each time a new location is available. In a navigation context while using the <a href="sdk-for-ios-explore-classes-navigator">`Navigator`</a> or <a href="sdk-for-ios-explore-classes-visualnavigator">`VisualNavigator`</a>, it’s required to set the <a href="sdk-for-ios-explore-structs-location#sdk-for-ios-explore-s-7heresdk8LocationV4time10Foundation4DateVSgvp">`Location.time`</a> parameter for each <a href="sdk-for-ios-explore-structs-location">`Location`</a> object so that the HERE SDK can map-match the locations properly. If the <a href="sdk-for-ios-explore-structs-location#sdk-for-ios-explore-s-7heresdk8LocationV4time10Foundation4DateVSgvp">`Location.time`</a> parameter is missing, the location will be ignored. For navigation, it is also recommended to provide the `bearing` and `speed` parameters for each <a href="sdk-for-ios-explore-structs-location">`Location`</a> object. Invoked on the main thread.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func onLocationUpdated(_ location: Location)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-location">Location</a>

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
  <td><code> </code><em><code>location</code></em><code> </code></td>
  <td><div>
  <p>Current location.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16TrafficBroadcastC8activateyyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-activate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-trafficbroadcast#sdk-for-ios-explore-s-7heresdk16TrafficBroadcastC8activateyyF" class="token"><code>activate()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Activates the reception of traffic data over the radio channel. This method is supposed to be called when the system loses internet connection, so that traffic data can be switched from the online source to the radio channel. When activation is done, requestTMCService is called from TMCServiceInterface

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func activate()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16TrafficBroadcastC10deactivateyyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-deactivate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-trafficbroadcast#sdk-for-ios-explore-s-7heresdk16TrafficBroadcastC10deactivateyyF" class="token"><code>deactivate()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Deactivates the reception of traffic data over the radio channel. When deactivation is done, requestTMCService is called from TMCServiceInterface With special case of countryCode parameter = 0

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func deactivate()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16TrafficBroadcastC31onTMCServiceProviderInfoUpdated018tmcServiceProdiverG0yAA0efG0V_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-onTMCServiceProviderInfoUpdated-tmcServiceProdiverInfo" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-trafficbroadcast#sdk-for-ios-explore-s-7heresdk16TrafficBroadcastC31onTMCServiceProviderInfoUpdated018tmcServiceProdiverG0yAA0efG0V_tF" class="token"><code>onTMCServiceProviderInfoUpdated(tmcServiceProdiverInfo:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Must be called on every TMC service prodiver info update.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func onTMCServiceProviderInfoUpdated(tmcServiceProdiverInfo: TMCServiceProviderInfo)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-tmcserviceproviderinfo">TMCServiceProviderInfo</a>

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
  <td><code> </code><em><code>tmcServiceProdiverInfo</code></em><code> </code></td>
  <td><div>
  <p>Contains service prodiver info in RDS-TMC format.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16TrafficBroadcastC16onTMCDataUpdated7tmcDatayAA0E0V_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-onTMCDataUpdated-tmcData" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-trafficbroadcast#sdk-for-ios-explore-s-7heresdk16TrafficBroadcastC16onTMCDataUpdated7tmcDatayAA0E0V_tF" class="token"><code>onTMCDataUpdated(tmcData:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Must be called on every TMC data update.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func onTMCDataUpdated(tmcData: TMCData)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-tmcdata">TMCData</a>

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
  <td><code> </code><em><code>tmcData</code></em><code> </code></td>
  <td><div>
  <p>Contains the traffic events in RDS-TMC format.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

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

