---
title: "CarSpecifications Structure Reference"
slug: "sdk-for-ios-navigate-structs-carspecifications"
---

# CarSpecifications

<div class="declaration">

<div class="language">

``` highlight
@available(*, deprecated, message: "Will be removed in v4.28.0. Use `TransportSpecification` instead.")
public struct CarSpecifications : Hashable
```

</div>

</div>

Car specifications contain vehicle related attributes. Examples: Dimensions, weight, axle count. Only the fields that are set are considered for restriction handling.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk17CarSpecificationsV22grossWeightInKilogramss5Int32VSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-grossWeightInKilograms" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-carspecifications#sdk-for-ios-navigate-s-7heresdk17CarSpecificationsV22grossWeightInKilogramss5Int32VSgvp" class="token"><code>grossWeightInKilograms</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Car weight including trailers and shipped goods in kilograms. The provided value must be greater than or equal to 0. By default, it is not set. **Note:** This parameter is limited to a maximum weight of 4250 kg without trailer and 7550 kg with trailer.

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

   <span id="sdk-for-ios-navigate-s-7heresdk17CarSpecificationsV19heightInCentimeterss5Int32VSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-heightInCentimeters" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-carspecifications#sdk-for-ios-navigate-s-7heresdk17CarSpecificationsV19heightInCentimeterss5Int32VSgvp" class="token"><code>heightInCentimeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Car height in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.

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

   <span id="sdk-for-ios-navigate-s-7heresdk17CarSpecificationsV18widthInCentimeterss5Int32VSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-widthInCentimeters" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-carspecifications#sdk-for-ios-navigate-s-7heresdk17CarSpecificationsV18widthInCentimeterss5Int32VSgvp" class="token"><code>widthInCentimeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Car width in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.

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

   <span id="sdk-for-ios-navigate-s-7heresdk17CarSpecificationsV19lengthInCentimeterss5Int32VSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-lengthInCentimeters" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-carspecifications#sdk-for-ios-navigate-s-7heresdk17CarSpecificationsV19lengthInCentimeterss5Int32VSgvp" class="token"><code>lengthInCentimeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Car length in centimeters. The provided value must be in the range \[0, 30000\]. By default, it is not set.

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

   <span id="sdk-for-ios-navigate-s-7heresdk17CarSpecificationsV9axleCounts5Int32VSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-axleCount" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-carspecifications#sdk-for-ios-navigate-s-7heresdk17CarSpecificationsV9axleCounts5Int32VSgvp" class="token"><code>axleCount</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines total number of axles in the vehicle. The provided value must be greater than or equal to 2. By default, it is not set. Route calculation: When not set, possible axle count restrictions will not be taken into consideration. When specifying <a href="sdk-for-ios-navigate-structs-carspecifications#sdk-for-ios-navigate-s-7heresdk17CarSpecificationsV16trailerAxleCounts5Int32VSgvp">`CarSpecifications.trailerAxleCount`</a>, then `CarSpecifications.axleCount` is required and must be greater than <a href="sdk-for-ios-navigate-structs-carspecifications#sdk-for-ios-navigate-s-7heresdk17CarSpecificationsV16trailerAxleCounts5Int32VSgvp">`CarSpecifications.trailerAxleCount`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var axleCount: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk17CarSpecificationsV12trailerCounts5Int32VSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-trailerCount" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-carspecifications#sdk-for-ios-navigate-s-7heresdk17CarSpecificationsV12trailerCounts5Int32VSgvp" class="token"><code>trailerCount</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines number of trailers attached to the vehicle. The provided value must be in the range \[0, 1\]. By default, it is not set. When specifying <a href="sdk-for-ios-navigate-structs-carspecifications#sdk-for-ios-navigate-s-7heresdk17CarSpecificationsV16trailerAxleCounts5Int32VSgvp">`CarSpecifications.trailerAxleCount`</a>, then `CarSpecifications.trailerCount` is required and must be greater than 0.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var trailerCount: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk17CarSpecificationsV16trailerAxleCounts5Int32VSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-trailerAxleCount" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-carspecifications#sdk-for-ios-navigate-s-7heresdk17CarSpecificationsV16trailerAxleCounts5Int32VSgvp" class="token"><code>trailerAxleCount</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines total number of axles across all the trailers attached to the vehicle. This number is included in <a href="sdk-for-ios-navigate-structs-carspecifications#sdk-for-ios-navigate-s-7heresdk17CarSpecificationsV9axleCounts5Int32VSgvp">`CarSpecifications.axleCount`</a>, hence `CarSpecifications.trailerAxleCount` must be less than <a href="sdk-for-ios-navigate-structs-carspecifications#sdk-for-ios-navigate-s-7heresdk17CarSpecificationsV9axleCounts5Int32VSgvp">`CarSpecifications.axleCount`</a> and greater than or equal to 1. <a href="sdk-for-ios-navigate-structs-carspecifications#sdk-for-ios-navigate-s-7heresdk17CarSpecificationsV9axleCounts5Int32VSgvp">`CarSpecifications.axleCount`</a> and <a href="sdk-for-ios-navigate-structs-carspecifications#sdk-for-ios-navigate-s-7heresdk17CarSpecificationsV12trailerCounts5Int32VSgvp">`CarSpecifications.trailerCount`</a> are required to specify `CarSpecifications.trailerAxleCount`. By default, it is not set.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var trailerAxleCount: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk17CarSpecificationsV22grossWeightInKilograms06heightF11Centimeters05widthfI006lengthfI09axleCount07trailerM00n4AxleM0ACs5Int32VSg_A6Mtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-grossWeightInKilograms-heightInCentimeters-widthInCentimeters-lengthInCentimeters-axleCount-trailerCount-trailerAxleCount" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-carspecifications#sdk-for-ios-navigate-s-7heresdk17CarSpecificationsV22grossWeightInKilograms06heightF11Centimeters05widthfI006lengthfI09axleCount07trailerM00n4AxleM0ACs5Int32VSg_A6Mtcfc" class="token"><code>init(grossWeightInKilograms:</code><wbr></wbr><code>heightInCentimeters:</code><wbr></wbr><code>widthInCentimeters:</code><wbr></wbr><code>lengthInCentimeters:</code><wbr></wbr><code>axleCount:</code><wbr></wbr><code>trailerCount:</code><wbr></wbr><code>trailerAxleCount:</code><wbr></wbr><code>)</code></a> 

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
  public init(grossWeightInKilograms: Int32? = nil, heightInCentimeters: Int32? = nil, widthInCentimeters: Int32? = nil, lengthInCentimeters: Int32? = nil, axleCount: Int32? = nil, trailerCount: Int32? = nil, trailerAxleCount: Int32? = nil)
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

