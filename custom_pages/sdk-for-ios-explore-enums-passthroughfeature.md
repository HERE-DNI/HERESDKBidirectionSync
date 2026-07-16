---
title: "PassThroughFeature Enumeration Reference"
slug: "sdk-for-ios-explore-enums-passthroughfeature"
---

# PassThroughFeature

<div class="declaration">

<div class="language">

``` highlight
public enum PassThroughFeature : UInt32, CaseIterable, Codable
```

</div>

</div>

Represents features that are allowed to consume online data when the HERE SDK’s offline mode is activated via <a href="sdk-for-ios-explore-classes-sdknativeengine#sdk-for-ios-explore-s-7heresdk15SDKNativeEngineC13isOfflineModeSbvp">`SDKNativeEngine.isOfflineMode`</a> and/or <a href="sdk-for-ios-explore-structs-sdkoptions#sdk-for-ios-explore-s-7heresdk10SDKOptionsV11offlineModeSbvp">`SDKOptions.offlineMode`</a>.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18PassThroughFeatureO11trafficDatayA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-trafficData" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-passthroughfeature#sdk-for-ios-explore-s-7heresdk18PassThroughFeatureO11trafficDatayA2CmF" class="token"><code>trafficData</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  When set, then the <a href="sdk-for-ios-explore-classes-trafficengine">`TrafficEngine`</a> is not blocked from initiating online connections to search for traffic data such as incidents.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case trafficData
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18PassThroughFeatureO16trafficTilesFlowyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-trafficTilesFlow" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-passthroughfeature#sdk-for-ios-explore-s-7heresdk18PassThroughFeatureO16trafficTilesFlowyA2CmF" class="token"><code>trafficTilesFlow</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  When set, then the corresponding `MapFeature` will not be blocked and online connections can be initiated by the HERE SDK to retrieve traffic flow data.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case trafficTilesFlow
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18PassThroughFeatureO21trafficTilesIncidentsyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-trafficTilesIncidents" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-passthroughfeature#sdk-for-ios-explore-s-7heresdk18PassThroughFeatureO21trafficTilesIncidentsyA2CmF" class="token"><code>trafficTilesIncidents</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  When set, then the corresponding `MapFeature` will not be blocked and online connections can be initiated by the HERE SDK to retrieve traffic incident data.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case trafficTilesIncidents
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18PassThroughFeatureO13onlineRoutingyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-onlineRouting" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-passthroughfeature#sdk-for-ios-explore-s-7heresdk18PassThroughFeatureO13onlineRoutingyA2CmF" class="token"><code>onlineRouting</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  When set, online routing can be performed by the HERE SDK, allowing the retrieval of up-to-date routing information from online services even when offline mode is enabled.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case onlineRouting
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18PassThroughFeatureO12onlineSearchyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-onlineSearch" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-passthroughfeature#sdk-for-ios-explore-s-7heresdk18PassThroughFeatureO12onlineSearchyA2CmF" class="token"><code>onlineSearch</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  When set, online search can be performed by the HERE SDK, allowing the retrieval of up-to-date search information from online services even when offline mode is enabled.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case onlineSearch
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

