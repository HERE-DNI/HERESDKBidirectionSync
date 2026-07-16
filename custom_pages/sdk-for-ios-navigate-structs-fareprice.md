---
title: "FarePrice Structure Reference"
slug: "sdk-for-ios-navigate-structs-fareprice"
---

# FarePrice

<div class="declaration">

<div class="language">

``` highlight
public struct FarePrice : Hashable
```

</div>

</div>

Price of a fare.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk9FarePriceV4typeAA0bC4TypeOvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-type" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-fareprice#sdk-for-ios-navigate-s-7heresdk9FarePriceV4typeAA0bC4TypeOvp" class="token"><code>type</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Type of price represented by this object. Defaults to <a href="sdk-for-ios-navigate-enums-farepricetype#sdk-for-ios-navigate-s-7heresdk13FarePriceTypeO5valueyA2CmF">`FarePriceType.value`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var type: FarePriceType
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-farepricetype">FarePriceType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk9FarePriceV9estimatedSbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-estimated" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-fareprice#sdk-for-ios-navigate-s-7heresdk9FarePriceV9estimatedSbvp" class="token"><code>estimated</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  `True` when the fare price is estimated based on best guess and the actual price may differ. Defaults to `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var estimated: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk9FarePriceV8currencySSvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-currency" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-fareprice#sdk-for-ios-navigate-s-7heresdk9FarePriceV8currencySSvp" class="token"><code>currency</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Local currency of the price compliant to ISO 4217. For example, “GBP” for the British pound sterling. Defaults to “EUR” string.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var currency: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk9FarePriceV7minimumSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-minimum" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-fareprice#sdk-for-ios-navigate-s-7heresdk9FarePriceV7minimumSdvp" class="token"><code>minimum</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Minimum price when the price is of <a href="sdk-for-ios-navigate-enums-farepricetype#sdk-for-ios-navigate-s-7heresdk13FarePriceTypeO5rangeyA2CmF">`FarePriceType.range`</a> type. Otherwise, it is equal to <a href="sdk-for-ios-navigate-structs-fareprice#sdk-for-ios-navigate-s-7heresdk9FarePriceV7maximumSdvp">`FarePrice.maximum`</a>. Defaults to 0.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var minimum: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk9FarePriceV7maximumSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-maximum" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-fareprice#sdk-for-ios-navigate-s-7heresdk9FarePriceV7maximumSdvp" class="token"><code>maximum</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Maximum price when the price is of <a href="sdk-for-ios-navigate-enums-farepricetype#sdk-for-ios-navigate-s-7heresdk13FarePriceTypeO5rangeyA2CmF">`FarePriceType.range`</a> type. Otherwise, it is equal to <a href="sdk-for-ios-navigate-structs-fareprice#sdk-for-ios-navigate-s-7heresdk9FarePriceV7minimumSdvp">`FarePrice.minimum`</a>. Defaults to 0.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maximum: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk9FarePriceV14validityPeriodSdSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-validityPeriod" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-fareprice#sdk-for-ios-navigate-s-7heresdk9FarePriceV14validityPeriodSdSgvp" class="token"><code>validityPeriod</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  When set, the price is paid for a specific duration.

  **Examples**:

  3600 seconds - price for one hour

  28800 seconds - price for eight hours

  86400 seconds - price for one day

  **Note:** When the ticket validity period starts depends on the <a href="sdk-for-ios-navigate-structs-agency">`Agency`</a> providing the service. Defaults to `nil`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var validityPeriod: TimeInterval?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk9FarePriceV4type9estimated8currency7minimum7maximum14validityPeriodAcA0bC4TypeO_SbSSS3dSgtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-type-estimated-currency-minimum-maximum-validityPeriod" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-fareprice#sdk-for-ios-navigate-s-7heresdk9FarePriceV4type9estimated8currency7minimum7maximum14validityPeriodAcA0bC4TypeO_SbSSS3dSgtcfc" class="token"><code>init(type:</code><wbr></wbr><code>estimated:</code><wbr></wbr><code>currency:</code><wbr></wbr><code>minimum:</code><wbr></wbr><code>maximum:</code><wbr></wbr><code>validityPeriod:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance.

  - Parameters

    - type: Type of price represented by this object. Defaults to <a href="sdk-for-ios-navigate-enums-farepricetype#sdk-for-ios-navigate-s-7heresdk13FarePriceTypeO5valueyA2CmF">`FarePriceType.value`</a>.
    - estimated: `True` when the fare price is estimated based on best guess and the actual price may differ. Defaults to `false`.
    - currency: Local currency of the price compliant to ISO 4217. For example, “GBP” for the British pound sterling. Defaults to “EUR” string.
    - minimum: Minimum price when the price is of <a href="sdk-for-ios-navigate-enums-farepricetype#sdk-for-ios-navigate-s-7heresdk13FarePriceTypeO5rangeyA2CmF">`FarePriceType.range`</a> type. Otherwise, it is equal to <a href="sdk-for-ios-navigate-structs-fareprice#sdk-for-ios-navigate-s-7heresdk9FarePriceV7maximumSdvp">`FarePrice.maximum`</a>. Defaults to 0.
    - maximum: Maximum price when the price is of <a href="sdk-for-ios-navigate-enums-farepricetype#sdk-for-ios-navigate-s-7heresdk13FarePriceTypeO5rangeyA2CmF">`FarePriceType.range`</a> type. Otherwise, it is equal to <a href="sdk-for-ios-navigate-structs-fareprice#sdk-for-ios-navigate-s-7heresdk9FarePriceV7minimumSdvp">`FarePrice.minimum`</a>. Defaults to 0.
    - validityPeriod: When set, the price is paid for a specific duration.

    **Examples**:

    3600 seconds - price for one hour

    28800 seconds - price for eight hours

    86400 seconds - price for one day

    **Note:** When the ticket validity period starts depends on the <a href="sdk-for-ios-navigate-structs-agency">`Agency`</a> providing the service. Defaults to `nil`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(type: FarePriceType = FarePriceType.value, estimated: Bool = false, currency: String = "EUR", minimum: Double = 0.0, maximum: Double = 0.0, validityPeriod: TimeInterval? = nil)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-farepricetype">FarePriceType</a>

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

