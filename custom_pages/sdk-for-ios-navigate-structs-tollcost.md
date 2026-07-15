---
title: "TollCost Structure Reference"
slug: "sdk-for-ios-navigate-structs-tollcost"
---

# TollCost

<div class="declaration">

<div class="language">

``` highlight
public struct TollCost : Hashable
```

</div>

</div>

Contains informations about the toll costs for a specific vehicle profile.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk8TollCostV8currencySSvp"></span>` `<span id="//apple_ref/swift/Property/currency" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-tollcost#/s:7heresdk8TollCostV8currencySSvp" class="token"><code>currency</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The currency in which the toll is to be paid in ISO 4217 format, e.g. “USD”.

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

  ` `<span id="/s:7heresdk8TollCostV5priceSdvp"></span>` `<span id="//apple_ref/swift/Property/price" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-tollcost#/s:7heresdk8TollCostV5priceSdvp" class="token"><code>price</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The amount of currency to be paid for the toll.

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

  ` `<span id="/s:7heresdk8TollCostV14paymentMethodsSayAA13PaymentMethodOGvp"></span>` `<span id="//apple_ref/swift/Property/paymentMethods" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-tollcost#/s:7heresdk8TollCostV14paymentMethodsSayAA13PaymentMethodOGvp" class="token"><code>paymentMethods</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of accepted payment methods like cash and credit card.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var paymentMethods: [PaymentMethod]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8TollCostV29isPriceCalculatedPerKilometerSbvp"></span>` `<span id="//apple_ref/swift/Property/isPriceCalculatedPerKilometer" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-tollcost#/s:7heresdk8TollCostV29isPriceCalculatedPerKilometerSbvp" class="token"><code>isPriceCalculatedPerKilometer</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates if the toll cost is based on the distance traveled. Defaults to `false`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isPriceCalculatedPerKilometer: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8TollCostV15vehicleProfilesSayAA14VehicleProfileVGvp"></span>` `<span id="//apple_ref/swift/Property/vehicleProfiles" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-tollcost#/s:7heresdk8TollCostV15vehicleProfilesSayAA14VehicleProfileVGvp" class="token"><code>vehicleProfiles</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of vehicle profile containing vehicle characteristics for which the toll cost applies.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0. Use the `TollCost.transport_specifications` instead.") public var vehicleProfiles : [ VehicleProfile ]
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8TollCostV23transportSpecificationsSayAA22TransportSpecificationVGvp"></span>` `<span id="//apple_ref/swift/Property/transportSpecifications" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-tollcost#/s:7heresdk8TollCostV23transportSpecificationsSayAA22TransportSpecificationVGvp" class="token"><code>transportSpecifications</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of transport specifications containing the vehicle characteristics for which the toll cost applies.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var transportSpecifications: [TransportSpecification]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(currency: price: paymentMethods: isPriceCalculatedPerKilometer: transportSpecifications: )

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
  public init ( currency : String , price : Double = 0.0 , paymentMethods : [ PaymentMethod ] = [], isPriceCalculatedPerKilometer : Bool = false , transportSpecifications : [ TransportSpecification ] = [])
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      init(currency: price: paymentMethods: isPriceCalculatedPerKilometer: vehicleProfiles: transportSpecifications: )

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
  @available(*, deprecated) public init ( currency : String , price : Double = 0.0 , paymentMethods : [ PaymentMethod ] = [], isPriceCalculatedPerKilometer : Bool = false , vehicleProfiles : [ VehicleProfile ] = [], transportSpecifications : [ TransportSpecification ] = [])
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

