---
title: "EVSEStatus Enumeration Reference"
slug: "sdk-for-ios-explore-enums-evsestatus"
---

# EVSEStatus

<div class="declaration">

<div class="language">

``` highlight
public enum EVSEStatus : UInt32, CaseIterable, Codable
```

</div>

</div>

EVSE status

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10EVSEStatusO9availableyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-available" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-evsestatus#sdk-for-ios-explore-s-7heresdk10EVSEStatusO9availableyA2CmF" class="token"><code>available</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The EVSE is able to start a new charging session.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case available
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10EVSEStatusO8occupiedyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-occupied" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-evsestatus#sdk-for-ios-explore-s-7heresdk10EVSEStatusO8occupiedyA2CmF" class="token"><code>occupied</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The EVSE is in use.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case occupied
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10EVSEStatusO7offlineyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-offline" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-evsestatus#sdk-for-ios-explore-s-7heresdk10EVSEStatusO7offlineyA2CmF" class="token"><code>offline</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  No status information available. Also used when offline.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case offline
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10EVSEStatusO5otheryA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-other" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-evsestatus#sdk-for-ios-explore-s-7heresdk10EVSEStatusO5otheryA2CmF" class="token"><code>other</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  No status information available. Also used when offline.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case other
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10EVSEStatusO12outOfServiceyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-outOfService" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-evsestatus#sdk-for-ios-explore-s-7heresdk10EVSEStatusO12outOfServiceyA2CmF" class="token"><code>outOfService</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The EVSE is currently out of order.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case outOfService
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10EVSEStatusO8reservedyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-reserved" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-evsestatus#sdk-for-ios-explore-s-7heresdk10EVSEStatusO8reservedyA2CmF" class="token"><code>reserved</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The EVSE has been reserved for a particular EV driver and is unavailable for other drivers.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case reserved
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10EVSEStatusO11unavailableyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-unavailable" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-evsestatus#sdk-for-ios-explore-s-7heresdk10EVSEStatusO11unavailableyA2CmF" class="token"><code>unavailable</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The EVSE is not available because of a physical barrier, for example a car.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case unavailable
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

