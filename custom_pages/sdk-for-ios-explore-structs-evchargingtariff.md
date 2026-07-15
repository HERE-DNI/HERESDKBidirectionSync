---
title: "EVChargingTariff Structure Reference"
slug: "sdk-for-ios-explore-structs-evchargingtariff"
---

# EVChargingTariff

<div class="declaration">

<div class="language">

``` highlight
public struct EVChargingTariff : Hashable
```

</div>

</div>

Tariffs provide detailed pricing information for charging electric vehicles at a specific location. Each tariff describes how costs are calculated based on various factors such as energy consumed, time spent charging, and session duration. Tariffs are typically associated with specific connectors or connector groups, and are only included in the response when relevant data is available and requested. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk16EVChargingTariffV4nameSSSgvp"></span>` `<span id="//apple_ref/swift/Property/name" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingtariff#/s:7heresdk16EVChargingTariffV4nameSSSgvp" class="token"><code>name</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Name of the tariff. The name is not mandatory for ad-hoc tariffs, but may exist.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var name: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16EVChargingTariffV4typeAA0bC4TypeOvp"></span>` `<span id="//apple_ref/swift/Property/type" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingtariff#/s:7heresdk16EVChargingTariffV4typeAA0bC4TypeOvp" class="token"><code>type</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the pricing model.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var type: EVChargingTariffType
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16EVChargingTariffV7partnerSSvp"></span>` `<span id="//apple_ref/swift/Property/partner" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingtariff#/s:7heresdk16EVChargingTariffV7partnerSSvp" class="token"><code>partner</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Name of the partner providing the tariff, either the charge point operator or eMSP.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var partner: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16EVChargingTariffV9partnerIDSSvp"></span>` `<span id="//apple_ref/swift/Property/partnerID" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingtariff#/s:7heresdk16EVChargingTariffV9partnerIDSSvp" class="token"><code>partnerID</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A unique ID representing the partner. The same id is used also in other parts of the API and other related HERE APIs.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var partnerID: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16EVChargingTariffV8currencySSvp"></span>` `<span id="//apple_ref/swift/Property/currency" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingtariff#/s:7heresdk16EVChargingTariffV8currencySSvp" class="token"><code>currency</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The currency in which the prices are given, represented by the ISO 4217 standard currency code (e.g., EUR, DKK).

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

  ` `<span id="/s:7heresdk16EVChargingTariffV8elementsSayAA0bC7ElementVGvp"></span>` `<span id="//apple_ref/swift/Property/elements" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingtariff#/s:7heresdk16EVChargingTariffV8elementsSayAA0bC7ElementVGvp" class="token"><code>elements</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Elements composing the tariff. Each element can have multiple components. When multiple elements are present, the associated condition helps the client to select the element that matches the charging session. If no condition matches, the element without any condition applies.

  Please note that tariff elements or conditions requiring access to vehicle APIs are not present in this API. The provided elements can only be used to derive a price estimate, which in most cases is reasonably close to the final price.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var elements: [EVChargingTariffElement]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(name: type: partner: partnerID: currency: elements: )

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

    - name: Name of the tariff. The name is not mandatory for ad-hoc tariffs, but may exist.
    - type: Indicates the pricing model.
    - partner: Name of the partner providing the tariff, either the charge point operator or eMSP.
    - partnerID: A unique ID representing the partner. The same id is used also in other parts of the API and other related HERE APIs.
    - currency: The currency in which the prices are given, represented by the ISO 4217 standard currency code (e.g., EUR, DKK).
    - elements: Elements composing the tariff. Each element can have multiple components. When multiple elements are present, the associated condition helps the client to select the element that matches the charging session. If no condition matches, the element without any condition applies.

    Please note that tariff elements or conditions requiring access to vehicle APIs are not present in this API. The provided elements can only be used to derive a price estimate, which in most cases is reasonably close to the final price.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( name : String ? = nil , type : EVChargingTariffType = EVChargingTariffType . adHoc , partner : String = "" , partnerID : String = "" , currency : String = "" , elements : [ EVChargingTariffElement ] = [])
  ```

  </pre>

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

