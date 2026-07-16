---
title: "EVSECapability Enumeration Reference"
slug: "sdk-for-ios-explore-enums-evsecapability"
---

# EVSECapability

<div class="declaration">

<div class="language">

``` highlight
public enum EVSECapability : UInt32, CaseIterable, Codable
```

</div>

</div>

Represents the administrative functionality that an EVSE is capable of. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14EVSECapabilityO15chargingProfileyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-chargingProfile" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-evsecapability#sdk-for-ios-explore-s-7heresdk14EVSECapabilityO15chargingProfileyA2CmF" class="token"><code>chargingProfile</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The EVSE supports charging profiles.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case chargingProfile
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14EVSECapabilityO19chargingPreferencesyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-chargingPreferences" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-evsecapability#sdk-for-ios-explore-s-7heresdk14EVSECapabilityO19chargingPreferencesyA2CmF" class="token"><code>chargingPreferences</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The EVSE supports charging preferences.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case chargingPreferences
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14EVSECapabilityO15remoteStartStopyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-remoteStartStop" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-evsecapability#sdk-for-ios-explore-s-7heresdk14EVSECapabilityO15remoteStartStopyA2CmF" class="token"><code>remoteStartStop</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The EVSE can remotely be started/stopped.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case remoteStartStop
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14EVSECapabilityO10reservableyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-reservable" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-evsecapability#sdk-for-ios-explore-s-7heresdk14EVSECapabilityO10reservableyA2CmF" class="token"><code>reservable</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The EVSE can be reserved.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case reservable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14EVSECapabilityO10tokenGroupyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-tokenGroup" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-evsecapability#sdk-for-ios-explore-s-7heresdk14EVSECapabilityO10tokenGroupyA2CmF" class="token"><code>tokenGroup</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This EVSE supports token groups, two or more tokens work as one, so that a session can be started with one token and stopped with another. This is handy when a card and key-fob are given to the EV-driver.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case tokenGroup
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14EVSECapabilityO6unlockyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-unlock" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-evsecapability#sdk-for-ios-explore-s-7heresdk14EVSECapabilityO6unlockyA2CmF" class="token"><code>unlock</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Connectors have mechanical lock that can be requested by the eMSP to be unlocked.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case unlock
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

