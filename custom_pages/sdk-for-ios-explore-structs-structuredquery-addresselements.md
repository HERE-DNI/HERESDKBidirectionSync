---
title: "AddressElements Structure Reference"
slug: "sdk-for-ios-explore-structs-structuredquery-addresselements"
---

# AddressElements

<div class="declaration">

<div class="language">

``` highlight
public struct AddressElements : Hashable
```

</div>

</div>

Defines query address elements which will be used to build address hierarchy during searches. It is advised to provide at least one intermediate address element when a large address element is provided for small admin area searches. For example if a user is building a query for a street and providing only country as an address element, consider providing city along with it.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15StructuredQueryV15AddressElementsV7countrySSSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-country" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-structuredquery-addresselements#sdk-for-ios-explore-s-7heresdk15StructuredQueryV15AddressElementsV7countrySSSgvp" class="token"><code>country</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  An optional field of country name or code, which will be used to get the results only from the given country.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var country: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15StructuredQueryV15AddressElementsV4citySSSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-city" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-structuredquery-addresselements#sdk-for-ios-explore-s-7heresdk15StructuredQueryV15AddressElementsV4citySSSgvp" class="token"><code>city</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  An optional field of city name, which will be used to get the results only from the given city.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var city: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15StructuredQueryV15AddressElementsV10postalCodeSSSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-postalCode" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-structuredquery-addresselements#sdk-for-ios-explore-s-7heresdk15StructuredQueryV15AddressElementsV10postalCodeSSSgvp" class="token"><code>postalCode</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  An optional field of postal code, which will be used to get the results only within the given postal code.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var postalCode: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15StructuredQueryV15AddressElementsV8districtSSSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-district" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-structuredquery-addresselements#sdk-for-ios-explore-s-7heresdk15StructuredQueryV15AddressElementsV8districtSSSgvp" class="token"><code>district</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  An optional field of district, which will be used to get the results only from the given district.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var district: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15StructuredQueryV15AddressElementsV7country4city10postalCode8districtAESSSg_A3Jtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-country-city-postalCode-district" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-structuredquery-addresselements#sdk-for-ios-explore-s-7heresdk15StructuredQueryV15AddressElementsV7country4city10postalCode8districtAESSSg_A3Jtcfc" class="token"><code>init(country:</code><wbr></wbr><code>city:</code><wbr></wbr><code>postalCode:</code><wbr></wbr><code>district:</code><wbr></wbr><code>)</code></a> 

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
  public init(country: String? = nil, city: String? = nil, postalCode: String? = nil, district: String? = nil)
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

