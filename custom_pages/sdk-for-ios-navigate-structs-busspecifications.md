---
title: "BusSpecifications Structure Reference"
slug: "sdk-for-ios-navigate-structs-busspecifications"
---

# BusSpecifications

<div class="declaration">

<div class="language">

``` highlight
@available(*, deprecated, message: "Will be removed in v4.28.0. Use `TransportSpecification` instead.")
public struct BusSpecifications : Hashable
```

</div>

</div>

Bus specifications contain vehicle related attributes. Examples: height, weight, width. Only the fields that are set are considered for restriction handling.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk17BusSpecificationsV22grossWeightInKilogramss5Int32VSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-grossWeightInKilograms" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-busspecifications#sdk-for-ios-navigate-s-7heresdk17BusSpecificationsV22grossWeightInKilogramss5Int32VSgvp" class="token"><code>grossWeightInKilograms</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Total vehicle weight in kilograms. By default, it is not set.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var grossWeightInKilograms: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk17BusSpecificationsV19heightInCentimeterss5Int32VSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-heightInCentimeters" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-busspecifications#sdk-for-ios-navigate-s-7heresdk17BusSpecificationsV19heightInCentimeterss5Int32VSgvp" class="token"><code>heightInCentimeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Bus height in centimeters. By default, it is not set.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var heightInCentimeters: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk17BusSpecificationsV18widthInCentimeterss5Int32VSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-widthInCentimeters" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-busspecifications#sdk-for-ios-navigate-s-7heresdk17BusSpecificationsV18widthInCentimeterss5Int32VSgvp" class="token"><code>widthInCentimeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Bus width in centimeters. By default, it is not set.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var widthInCentimeters: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk17BusSpecificationsV19lengthInCentimeterss5Int32VSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-lengthInCentimeters" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-busspecifications#sdk-for-ios-navigate-s-7heresdk17BusSpecificationsV19lengthInCentimeterss5Int32VSgvp" class="token"><code>lengthInCentimeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Bus length in centimeters. By default, it is not set.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var lengthInCentimeters: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk17BusSpecificationsV22grossWeightInKilograms06heightF11Centimeters05widthfI006lengthfI0ACs5Int32VSg_A3Jtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-grossWeightInKilograms-heightInCentimeters-widthInCentimeters-lengthInCentimeters" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-busspecifications#sdk-for-ios-navigate-s-7heresdk17BusSpecificationsV22grossWeightInKilograms06heightF11Centimeters05widthfI006lengthfI0ACs5Int32VSg_A3Jtcfc" class="token"><code>init(grossWeightInKilograms:</code><wbr></wbr><code>heightInCentimeters:</code><wbr></wbr><code>widthInCentimeters:</code><wbr></wbr><code>lengthInCentimeters:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(grossWeightInKilograms: Int32? = nil, heightInCentimeters: Int32? = nil, widthInCentimeters: Int32? = nil, lengthInCentimeters: Int32? = nil)
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

