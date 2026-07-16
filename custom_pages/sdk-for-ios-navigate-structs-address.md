---
title: "Address Structure Reference"
slug: "sdk-for-ios-navigate-structs-address"
---

# Address

<div class="declaration">

<div class="language">

``` highlight
public struct Address : Hashable
```

</div>

</div>

Information about the address of a location.

Used in <a href="sdk-for-ios-navigate-classes-place#sdk-for-ios-navigate-s-7heresdk5PlaceC7addressAA7AddressVvp">`Place.address`</a>.

Note that while `OfflineSearchEngine.suggest` and `OfflineSearchEngine.suggestByText` set all available details, `SearchEngine.suggest` and `SearchEngine.suggestByText` set only <a href="sdk-for-ios-navigate-structs-address#sdk-for-ios-navigate-s-7heresdk7AddressV11addressTextSSvp">`Address.addressText`</a>. Complete address details can be obtained by searching with <a href="sdk-for-ios-navigate-structs-placeidquery">`PlaceIdQuery`</a>.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7AddressV4citySSvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-city" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-address#sdk-for-ios-navigate-s-7heresdk7AddressV4citySSvp" class="token"><code>city</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The city name for the address, for example, “Brooklyn”. Note: This String can be empty when no data is available.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var city: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7AddressV11countryCodeSSvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-countryCode" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-address#sdk-for-ios-navigate-s-7heresdk7AddressV11countryCodeSSvp" class="token"><code>countryCode</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  An ISO-3166-1 (3-letter) country code for the address, for example, “USA”. Note: This String can be empty when no data is available.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var countryCode: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7AddressV7countrySSvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-country" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-address#sdk-for-ios-navigate-s-7heresdk7AddressV7countrySSvp" class="token"><code>country</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The country name for the address, for example, “United States”. Note: This String can be empty when no data is available.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var country: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7AddressV8districtSSvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-district" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-address#sdk-for-ios-navigate-s-7heresdk7AddressV8districtSSvp" class="token"><code>district</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The district name for the address. It is a division of city, typically an administrative unit within a larger city or a customary name of a city’s neighborhood, for example, “Bedford-Stuyvesant”. Note: This String can be empty when no data is available.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var district: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7AddressV11subdistrictSSvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-subdistrict" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-address#sdk-for-ios-navigate-s-7heresdk7AddressV11subdistrictSSvp" class="token"><code>subdistrict</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The subdistrict name for the address. It is a subdivision of a district. Note: This String can be empty when no data is available.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var subdistrict: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7AddressV14houseNumOrNameSSvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-houseNumOrName" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-address#sdk-for-ios-navigate-s-7heresdk7AddressV14houseNumOrNameSSvp" class="token"><code>houseNumOrName</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The house name or number for the address, for example, “347”. Note: This String can be empty when no data is available.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var houseNumOrName: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7AddressV10postalCodeSSvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-postalCode" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-address#sdk-for-ios-navigate-s-7heresdk7AddressV10postalCodeSSvp" class="token"><code>postalCode</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The postal code for the address. It is an alphanumeric string included in a postal address to facilitate mail sorting, known locally in various countries throughout the world as a postcode, post code, PIN or ZIP Code, for example, “11233”. Note: This String can be empty when no data is available.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var postalCode: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7AddressV5stateSSvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-state" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-address#sdk-for-ios-navigate-s-7heresdk7AddressV5stateSSvp" class="token"><code>state</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The state name for the address. It is the name of the state division of a country, for example, “New York”. Note: This String can be empty when no data is available.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var state: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7AddressV6countySSvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-county" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-address#sdk-for-ios-navigate-s-7heresdk7AddressV6countySSvp" class="token"><code>county</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The county name for the address. It is a division of a state, typically a secondary-level administrative division of a country or equivalent, for example, “Kings”. Note: This String can be empty when no data is available.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var county: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7AddressV6streetSSvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-street" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-address#sdk-for-ios-navigate-s-7heresdk7AddressV6streetSSvp" class="token"><code>street</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The street name for the address, for example, “Lewis Ave”. Note: This String can be empty when no data is available.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var street: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7AddressV5blockSSvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-block" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-address#sdk-for-ios-navigate-s-7heresdk7AddressV5blockSSvp" class="token"><code>block</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The block number for the address. It is part of Japanese addressing system. Note: This String can be empty when no data is available.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var block: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7AddressV8subBlockSSvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-subBlock" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-address#sdk-for-ios-navigate-s-7heresdk7AddressV8subBlockSSvp" class="token"><code>subBlock</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The sub-block number for the address. It is part of Japanese addressing system. Note: This String can be empty when no data is available.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var subBlock: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7AddressV11addressTextSSvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-addressText" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-address#sdk-for-ios-navigate-s-7heresdk7AddressV11addressTextSSvp" class="token"><code>addressText</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The text for the address, for example, “Secret Garden, 347 Lewis Ave, Brooklyn, NY 11233, United States”. Note: This String can be empty when no data is available.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var addressText: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7AddressV4typeAA0B4TypeOSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-type" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-address#sdk-for-ios-navigate-s-7heresdk7AddressV4typeAA0B4TypeOSgvp" class="token"><code>type</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies the address type.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var type: AddressType?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-addresstype">AddressType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7AddressV9stateCodeSSvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-stateCode" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-address#sdk-for-ios-navigate-s-7heresdk7AddressV9stateCodeSSvp" class="token"><code>stateCode</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The state code for the address. It is code/abbreviation of the state division of a country, for example, “NY”. Note: This String can be empty when no data is available.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var stateCode: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7AddressV4city11countryCode0D08district11subdistrict14houseNumOrName06postalE05state6county6street5block8subBlock11addressText4type0mE0ACSS_S12SAA0B4TypeOSgSStcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-city-countryCode-country-district-subdistrict-houseNumOrName-postalCode-state-county-street-block-subBlock-addressText-type-stateCode" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-address#sdk-for-ios-navigate-s-7heresdk7AddressV4city11countryCode0D08district11subdistrict14houseNumOrName06postalE05state6county6street5block8subBlock11addressText4type0mE0ACSS_S12SAA0B4TypeOSgSStcfc" class="token"><code>init(city:</code><wbr></wbr><code>countryCode:</code><wbr></wbr><code>country:</code><wbr></wbr><code>district:</code><wbr></wbr><code>subdistrict:</code><wbr></wbr><code>houseNumOrName:</code><wbr></wbr><code>postalCode:</code><wbr></wbr><code>state:</code><wbr></wbr><code>county:</code><wbr></wbr><code>street:</code><wbr></wbr><code>block:</code><wbr></wbr><code>subBlock:</code><wbr></wbr><code>addressText:</code><wbr></wbr><code>type:</code><wbr></wbr><code>stateCode:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Undocumented

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(city: String = "", countryCode: String = "", country: String = "", district: String = "", subdistrict: String = "", houseNumOrName: String = "", postalCode: String = "", state: String = "", county: String = "", street: String = "", block: String = "", subBlock: String = "", addressText: String = "", type: AddressType? = nil, stateCode: String = "")
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-addresstype">AddressType</a>

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

