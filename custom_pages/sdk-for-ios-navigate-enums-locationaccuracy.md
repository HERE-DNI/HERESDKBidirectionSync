---
title: "LocationAccuracy Enumeration Reference"
slug: "sdk-for-ios-navigate-enums-locationaccuracy"
---

# LocationAccuracy

<div class="declaration">

<div class="language">

``` highlight
public enum LocationAccuracy : UInt32, CaseIterable, Codable
```

</div>

</div>

Indicates the desired location accuracy, however the actual accuracy is not guaranteed. When requesting high-accuracy locations, the initial update delivered by the LocationEngine may not have the requested accuracy. Requesting higher accuracy location updates usually means higher power consumption, therefore you should use the lowest accuracy suitable for your use case to preserve the device battery.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16LocationAccuracyO13bestAvailableyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-bestAvailable" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-locationaccuracy#sdk-for-ios-navigate-s-7heresdk16LocationAccuracyO13bestAvailableyA2CmF" class="token"><code>bestAvailable</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The best level of accuracy available when you don’t need the level of accuracy required for navigation apps.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case bestAvailable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16LocationAccuracyO18subMeterNavigationyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-subMeterNavigation" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-locationaccuracy#sdk-for-ios-navigate-s-7heresdk16LocationAccuracyO18subMeterNavigationyA2CmF" class="token"><code>subMeterNavigation</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Not supported in iOS.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case subMeterNavigation
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16LocationAccuracyO10navigationyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-navigation" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-locationaccuracy#sdk-for-ios-navigate-s-7heresdk16LocationAccuracyO10navigationyA2CmF" class="token"><code>navigation</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The highest possible accuracy that uses additional sensor data to facilitate navigation apps.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case navigation
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16LocationAccuracyO12tensOfMetersyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-tensOfMeters" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-locationaccuracy#sdk-for-ios-navigate-s-7heresdk16LocationAccuracyO12tensOfMetersyA2CmF" class="token"><code>tensOfMeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Accurate to within tens of meters of the desired target.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case tensOfMeters
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16LocationAccuracyO16hundredsOfMetersyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-hundredsOfMeters" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-locationaccuracy#sdk-for-ios-navigate-s-7heresdk16LocationAccuracyO16hundredsOfMetersyA2CmF" class="token"><code>hundredsOfMeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Accurate to within hundreds of meters of the desired target.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case hundredsOfMeters
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16LocationAccuracyO10kilometersyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-kilometers" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-locationaccuracy#sdk-for-ios-navigate-s-7heresdk16LocationAccuracyO10kilometersyA2CmF" class="token"><code>kilometers</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Accurate to within kilometers of the desired target.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case kilometers
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

