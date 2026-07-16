---
title: "TransportMode Enumeration Reference"
slug: "sdk-for-ios-explore-enums-transportmode"
---

# TransportMode

<div class="declaration">

<div class="language">

``` highlight
public enum TransportMode : UInt32, CaseIterable, Codable
```

</div>

</div>

Specifies the mode of transport used for route calculalation.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk13TransportModeO3caryA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-car" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-transportmode#sdk-for-ios-explore-s-7heresdk13TransportModeO3caryA2CmF" class="token"><code>car</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The calculated route is optimized for cars.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case car
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk13TransportModeO5truckyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-truck" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-transportmode#sdk-for-ios-explore-s-7heresdk13TransportModeO5truckyA2CmF" class="token"><code>truck</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The calculated route is optimized for trucks. This mode considers truck restrictions and uses truck specific speed assumptions when calculating the route.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case truck
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk13TransportModeO10pedestrianyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-pedestrian" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-transportmode#sdk-for-ios-explore-s-7heresdk13TransportModeO10pedestrianyA2CmF" class="token"><code>pedestrian</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The calculated route is optimized for pedestrians. As one effect, maneuvers will be optimized for walking, i.e. segments will consider actions relevant for pedestrians and maneuver instructions will contain texts suitable for a walking person. This mode disregards any traffic information.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case pedestrian
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk13TransportModeO7scooteryA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-scooter" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-transportmode#sdk-for-ios-explore-s-7heresdk13TransportModeO7scooteryA2CmF" class="token"><code>scooter</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The calculated route is optimized for scooters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case scooter
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk13TransportModeO7bicycleyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-bicycle" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-transportmode#sdk-for-ios-explore-s-7heresdk13TransportModeO7bicycleyA2CmF" class="token"><code>bicycle</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Route calculation for bicycles.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case bicycle
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk13TransportModeO13publicTransityA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-publicTransit" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-transportmode#sdk-for-ios-explore-s-7heresdk13TransportModeO13publicTransityA2CmF" class="token"><code>publicTransit</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The calculated route is optimized for public transit. Note that this transport mode is available only for some versions of the HERE SDK. Check <a href="sdk-for-ios-explore-classes-sdkbuildinformation">`SDKBuildInformation`</a> and consult your HERE representative if necessary.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case publicTransit
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk13TransportModeO4taxiyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-taxi" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-transportmode#sdk-for-ios-explore-s-7heresdk13TransportModeO4taxiyA2CmF" class="token"><code>taxi</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The taxi transport mode takes into account tax restricted streets as well as streets reserved for exclusive taxi access. Note that roads that are restricted or reserved for taxis are avoided, unless a waypoint is set on such a road - as this may indicate to pick-up or to drop-off a passenger.

  **Note:** This is a beta release of this transport mode, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases or even become unsupported, without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case taxi
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk13TransportModeO3busyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-bus" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-transportmode#sdk-for-ios-explore-s-7heresdk13TransportModeO3busyA2CmF" class="token"><code>bus</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Route calculation for buses. Denotes those vehicles operated by public transport provider. This transport mode has the access to the bus-only lane/road.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case bus
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk13TransportModeO10privateBusyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-privateBus" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-transportmode#sdk-for-ios-explore-s-7heresdk13TransportModeO10privateBusyA2CmF" class="token"><code>privateBus</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Route calculation for private buses. Denotes those vehicles operated by private transport company. This transport mode does not have the access to the bus-only lane/road.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case privateBus
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

