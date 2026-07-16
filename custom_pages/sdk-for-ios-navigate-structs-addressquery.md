---
title: "AddressQuery Structure Reference"
slug: "sdk-for-ios-navigate-structs-addressquery"
---

# AddressQuery

<div class="declaration">

<div class="language">

``` highlight
public struct AddressQuery : Hashable
```

</div>

</div>

The options to specify an address query. A <a href="sdk-for-ios-navigate-structs-addressquery#sdk-for-ios-navigate-s-7heresdk12AddressQueryV5querySSvp">`AddressQuery.query`</a> can consist of parts of an address or full addresses, optionally comma separated. `AddressQuery` should only be used to search for parts of the address, excluding the POI name. For example, “Invalidenstraße 116, Berlin, Germany” is appropriate, whereas “HERE, Invalidenstraße 116, Berlin, Germany” is not. To be able to include the POI name, use <a href="sdk-for-ios-navigate-structs-textquery">`TextQuery`</a> instead. <a href="sdk-for-ios-navigate-structs-searchoptions#sdk-for-ios-navigate-s-7heresdk13SearchOptionsV12languageCodeAA08LanguageE0OSgvp">`SearchOptions.languageCode`</a> specifies the language of the <a href="sdk-for-ios-navigate-structs-addressquery#sdk-for-ios-navigate-s-7heresdk12AddressQueryV5querySSvp">`AddressQuery.query`</a> and determines the preferred language of the results.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12AddressQueryV5querySSvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-query" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-addressquery#sdk-for-ios-navigate-s-7heresdk12AddressQueryV5querySSvp" class="token"><code>query</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Desired address query to search.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public let query: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12AddressQueryV10areaCenterAA14GeoCoordinatesVSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-areaCenter" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-addressquery#sdk-for-ios-navigate-s-7heresdk12AddressQueryV10areaCenterAA14GeoCoordinatesVSgvp" class="token"><code>areaCenter</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Geographical coordinates of the center around which to provide the most relevant places. For Offline Search null value will result in <a href="sdk-for-ios-navigate-enums-searcherror#sdk-for-ios-navigate-s-7heresdk11SearchErrorO11invalidAreayA2CmF">`SearchError.invalidArea`</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public let areaCenter: GeoCoordinates?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geocoordinates">GeoCoordinates</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12AddressQueryV9countriesSayAA11CountryCodeOGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-countries" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-addressquery#sdk-for-ios-navigate-s-7heresdk12AddressQueryV9countriesSayAA11CountryCodeOGvp" class="token"><code>countries</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A list of countries that the query is applied in. Not supported in <a href="sdk-for-ios-navigate-classes-offlinesearchengine">`OfflineSearchEngine`</a> (only available for the Navigate license).

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public let countries: [CountryCode]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-countrycode">CountryCode</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12AddressQueryV_4nearACSS_AA14GeoCoordinatesVtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-_-near" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-addressquery#sdk-for-ios-navigate-s-7heresdk12AddressQueryV_4nearACSS_AA14GeoCoordinatesVtcfc" class="token"><code>init(_:</code><wbr></wbr><code>near:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs an AddressQuery from the provided text query and geographical coordinates.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(_ query: String, near areaCenter: GeoCoordinates)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geocoordinates">GeoCoordinates</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>query</code></em><code> </code></td>
  <td><div>
  <p>Desired query to search.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>areaCenter</code></em><code> </code></td>
  <td><div>
  <p>Geographical coordinates of the center around which to provide the most relevant places.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12AddressQueryV_4near11inCountriesACSS_AA14GeoCoordinatesVSayAA11CountryCodeOGtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-_-near-inCountries" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-addressquery#sdk-for-ios-navigate-s-7heresdk12AddressQueryV_4near11inCountriesACSS_AA14GeoCoordinatesVSayAA11CountryCodeOGtcfc" class="token"><code>init(_:</code><wbr></wbr><code>near:</code><wbr></wbr><code>inCountries:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs an AddressQuery from the provided text query, geographical coordinates and the list of countries the query is applied in.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(_ query: String, near areaCenter: GeoCoordinates, inCountries countries: [CountryCode])
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geocoordinates">GeoCoordinates</a>
  - <a href="sdk-for-ios-navigate-enums-countrycode">CountryCode</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>query</code></em><code> </code></td>
  <td><div>
  <p>Desired query to search.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>areaCenter</code></em><code> </code></td>
  <td><div>
  <p>Geographical coordinates of the center around which to provide the most relevant places.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>countries</code></em><code> </code></td>
  <td><div>
  <p>A list of countries that the query is applied in.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12AddressQueryVyACSScfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-_" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-addressquery#sdk-for-ios-navigate-s-7heresdk12AddressQueryVyACSScfc" class="token"><code>init(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs an AddressQuery from the provided text query. Not supported in <a href="sdk-for-ios-navigate-classes-offlinesearchengine">`OfflineSearchEngine`</a> (only available for the Navigate license).

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(_ query: String)
  ```

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>query</code></em><code> </code></td>
  <td><div>
  <p>Desired query to search.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

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

