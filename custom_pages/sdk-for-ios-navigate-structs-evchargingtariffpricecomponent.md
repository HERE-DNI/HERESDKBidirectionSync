---
title: "EVChargingTariffPriceComponent Structure Reference"
slug: "sdk-for-ios-navigate-structs-evchargingtariffpricecomponent"
---

# EVChargingTariffPriceComponent

<div class="declaration">

<div class="language">

``` highlight
public struct EVChargingTariffPriceComponent : Hashable
```

</div>

</div>

Represents the price component of an EV charging tariff. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk30EVChargingTariffPriceComponentV9dimensionAA0bC9DimensionOvp"></span>` `<span id="//apple_ref/swift/Property/dimension" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-evchargingtariffpricecomponent#/s:7heresdk30EVChargingTariffPriceComponentV9dimensionAA0bC9DimensionOvp" class="token"><code>dimension</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The dimension or type of the price component.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var dimension: EVChargingTariffDimension
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk30EVChargingTariffPriceComponentV5priceSdvp"></span>` `<span id="//apple_ref/swift/Property/price" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-evchargingtariffpricecomponent#/s:7heresdk30EVChargingTariffPriceComponentV5priceSdvp" class="token"><code>price</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The price per unit, excluding VAT. The units are defined by the <a href="sdk-for-ios-navigate-structs-evchargingtariffpricecomponent#/s:7heresdk30EVChargingTariffPriceComponentV9dimensionAA0bC9DimensionOvp">`EVChargingTariffPriceComponent.dimension`</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var price: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk30EVChargingTariffPriceComponentV3vatSdSgvp"></span>` `<span id="//apple_ref/swift/Property/vat" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-evchargingtariffpricecomponent#/s:7heresdk30EVChargingTariffPriceComponentV3vatSdSgvp" class="token"><code>vat</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The VAT percentage of the price component. If not present, no VAT is applicable.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var vat: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk30EVChargingTariffPriceComponentV4stepSdSgvp"></span>` `<span id="//apple_ref/swift/Property/step" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-evchargingtariffpricecomponent#/s:7heresdk30EVChargingTariffPriceComponentV4stepSdSgvp" class="token"><code>step</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Dimension quantity used as a unit of billing. Present for all other dimensions except <a href="sdk-for-ios-navigate-enums-evchargingtariffdimension#/s:7heresdk25EVChargingTariffDimensionO4flatyA2CmF">`EVChargingTariffDimension.flat`</a>. The customer is charged price for each full or partial step of the dimension consumed. For <a href="sdk-for-ios-navigate-enums-evchargingtariffdimension#/s:7heresdk25EVChargingTariffDimensionO6energyyA2CmF">`EVChargingTariffDimension.energy`</a>, the step size unit is 1 Wh, for <a href="sdk-for-ios-navigate-enums-evchargingtariffdimension#/s:7heresdk25EVChargingTariffDimensionO4timeyA2CmF">`EVChargingTariffDimension.time`</a> and <a href="sdk-for-ios-navigate-enums-evchargingtariffdimension#/s:7heresdk25EVChargingTariffDimensionO11parkingTimeyA2CmF">`EVChargingTariffDimension.parkingTime`</a> it is 1 second. For example, if step is 300 for time, then time is billed in 5 minute steps, rounded upwards. Similarly, if step is 100 for energy, then energy is billed in 100 Wh = 0.1 kWh steps.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var step: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(dimension: price: vat: step: )

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
  public init ( dimension : EVChargingTariffDimension = EVChargingTariffDimension . flat , price : Double = 0.0 , vat : Double ? = nil , step : Double ? = nil )
  ```

  </pre>

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

