---
title: "EVSEState Enumeration Reference"
slug: "sdk-for-ios-navigate-enums-evsestate"
---

# EVSEState

<div class="declaration">

<div class="language">

``` highlight
public enum EVSEState : UInt32, CaseIterable, Codable
```

</div>

</div>

Indicates the current short-term status of the EVSE at the time given in the modified property. There are no separate statuses available for individual connectors. A single EVSE can only be used by a single car, so same statuses apply to other connectors as well. So, if one connector is in use, the whole EVSE has status charging, and other connectors cannot be used at the same time, hence they should be considered in-use as well. If an EVSE can allow multiple connectors to be used at the same time, it is basically multiple EVSEs merged into a single physical box or device.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk9EVSEStateO7unknownyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-unknown" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-evsestate#sdk-for-ios-navigate-s-7heresdk9EVSEStateO7unknownyA2CmF" class="token"><code>unknown</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  No status information available or the EVSE/connector is offline.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case unknown
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk9EVSEStateO9availableyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-available" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-evsestate#sdk-for-ios-navigate-s-7heresdk9EVSEStateO9availableyA2CmF" class="token"><code>available</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The EVSE/connector is able to start a new charging session.

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

   <span id="sdk-for-ios-navigate-s-7heresdk9EVSEStateO7blockedyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-blocked" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-evsestate#sdk-for-ios-navigate-s-7heresdk9EVSEStateO7blockedyA2CmF" class="token"><code>blocked</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The EVSE/connector is not accessible because of a physical barrier, i.e. a car.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case blocked
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk9EVSEStateO8chargingyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-charging" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-evsestate#sdk-for-ios-navigate-s-7heresdk9EVSEStateO8chargingyA2CmF" class="token"><code>charging</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The EVSE/connector is in use.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case charging
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk9EVSEStateO11inoperativeyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-inoperative" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-evsestate#sdk-for-ios-navigate-s-7heresdk9EVSEStateO11inoperativeyA2CmF" class="token"><code>inoperative</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The EVSE/connector is temporarily not available for use, but not broken or defect.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case inoperative
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk9EVSEStateO10outOfOrderyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-outOfOrder" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-evsestate#sdk-for-ios-navigate-s-7heresdk9EVSEStateO10outOfOrderyA2CmF" class="token"><code>outOfOrder</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The EVSE/connector is currently out of order.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case outOfOrder
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk9EVSEStateO8reservedyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-reserved" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-evsestate#sdk-for-ios-navigate-s-7heresdk9EVSEStateO8reservedyA2CmF" class="token"><code>reserved</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The EVSE/connector is reserved for a particular EV driver and is unavailable for other drivers.

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

   <span id="sdk-for-ios-navigate-s-7heresdk9EVSEStateO11operationalyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-operational" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-evsestate#sdk-for-ios-navigate-s-7heresdk9EVSEStateO11operationalyA2CmF" class="token"><code>operational</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The EVSE/connector was operational when checked the last time, but the actual latest status is not available at the moment.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case operational
  ```

  </div>

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

