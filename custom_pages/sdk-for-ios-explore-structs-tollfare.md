---
title: "TollFare Structure Reference"
slug: "sdk-for-ios-explore-structs-tollfare"
---

# TollFare

<div class="declaration">

<div class="language">

``` highlight
public struct TollFare : Hashable
```

</div>

</div>

This struct presents all the fare data for a toll.

**Note**: If you’re using the <a href="sdk-for-ios-explore-classes-offlineroutingengine">`OfflineRoutingEngine`</a>, be aware that this feature is currently in **beta**. As a result, there may be some bugs or unexpected behaviors. Additionally, this feature and related APIs may be updated in future releases without going through the deprecation process. Note that the <a href="sdk-for-ios-explore-classes-offlineroutingengine">`OfflineRoutingEngine`</a> is only available for the Navigate license. If you’re using the <a href="sdk-for-ios-explore-classes-routingengine">`RoutingEngine`</a>, this feature is considered to be stable.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8TollFareV8currencySSvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-currency" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-tollfare#sdk-for-ios-explore-s-7heresdk8TollFareV8currencySSvp" class="token"><code>currency</code></a> 

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

   <span id="sdk-for-ios-explore-s-7heresdk8TollFareV5priceSdvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-price" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-tollfare#sdk-for-ios-explore-s-7heresdk8TollFareV5priceSdvp" class="token"><code>price</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The amount of the toll be paid.

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

   <span id="sdk-for-ios-explore-s-7heresdk8TollFareV14paymentMethodsSayAA13PaymentMethodOGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-paymentMethods" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-tollfare#sdk-for-ios-explore-s-7heresdk8TollFareV14paymentMethodsSayAA13PaymentMethodOGvp" class="token"><code>paymentMethods</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-enums-paymentmethod">PaymentMethod</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8TollFareV8timeRuleAA04TimeE0CSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-timeRule" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-tollfare#sdk-for-ios-explore-s-7heresdk8TollFareV8timeRuleAA04TimeE0CSgvp" class="token"><code>timeRule</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The time domain when this fare is valid. If this field is missing, it means the fare is always valid. For a detailed description of the Time Domain specification and usage in routing services, please refer to the documentation available in the <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/time-domain.html">Time Domain</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var timeRule: TimeRule?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-timerule">TimeRule</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8TollFareV12transpondersSaySSGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-transponders" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-tollfare#sdk-for-ios-explore-s-7heresdk8TollFareV12transpondersSaySSGvp" class="token"><code>transponders</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of available transponders.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var transponders: [String]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8TollFareV4passAA0bC4PassVSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-pass" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-tollfare#sdk-for-ios-explore-s-7heresdk8TollFareV4passAA0bC4PassVSgvp" class="token"><code>pass</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies whether this `TollFare` is a multi-travel pass, and its characteristics.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var pass: TollFarePass?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-tollfarepass">TollFarePass</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8TollFareV8currency5price14paymentMethods8timeRule12transponders4passACSS_SdSayAA13PaymentMethodOGAA04TimeI0CSgSaySSGAA0bC4PassVSgtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-currency-price-paymentMethods-timeRule-transponders-pass" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-tollfare#sdk-for-ios-explore-s-7heresdk8TollFareV8currency5price14paymentMethods8timeRule12transponders4passACSS_SdSayAA13PaymentMethodOGAA04TimeI0CSgSaySSGAA0bC4PassVSgtcfc" class="token"><code>init(currency:</code><wbr></wbr><code>price:</code><wbr></wbr><code>paymentMethods:</code><wbr></wbr><code>timeRule:</code><wbr></wbr><code>transponders:</code><wbr></wbr><code>pass:</code><wbr></wbr><code>)</code></a> 

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
  public init(currency: String, price: Double, paymentMethods: [PaymentMethod], timeRule: TimeRule? = nil, transponders: [String] = [], pass: TollFarePass? = nil)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-paymentmethod">PaymentMethod</a>
  - <a href="sdk-for-ios-explore-classes-timerule">TimeRule</a>
  - <a href="sdk-for-ios-explore-structs-tollfarepass">TollFarePass</a>

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

