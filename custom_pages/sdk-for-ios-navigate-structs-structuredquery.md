---
title: "StructuredQuery Structure Reference"
slug: "sdk-for-ios-navigate-structs-structuredquery"
---

# StructuredQuery

<div class="declaration">

<div class="language">

``` highlight
public struct StructuredQuery : Hashable
```

</div>

</div>

The options to specify a structured query. Only supported in <a href="sdk-for-ios-navigate-classes-offlinesearchengine">`OfflineSearchEngine`</a> (only available for the Navigate license).

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15StructuredQueryV5querySSvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-query" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-structuredquery#sdk-for-ios-navigate-s-7heresdk15StructuredQueryV5querySSvp" class="token"><code>query</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Desired query to search.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var query: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15StructuredQueryV10areaCenterAA14GeoCoordinatesVvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-areaCenter" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-structuredquery#sdk-for-ios-navigate-s-7heresdk15StructuredQueryV10areaCenterAA14GeoCoordinatesVvp" class="token"><code>areaCenter</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Geographic coordinates of the prioritized area center.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var areaCenter: GeoCoordinates
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geocoordinates">GeoCoordinates</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15StructuredQueryV15addressElementsAC07AddressE0Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-addressElements" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-structuredquery#sdk-for-ios-navigate-s-7heresdk15StructuredQueryV15addressElementsAC07AddressE0Vvp" class="token"><code>addressElements</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Query address elements to get the results from a specific geographical area.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var addressElements: StructuredQuery.AddressElements
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-structuredquery-addresselements">AddressElements</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15StructuredQueryV10resultTypeAC06ResultE0OSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-resultType" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-structuredquery#sdk-for-ios-navigate-s-7heresdk15StructuredQueryV10resultTypeAC06ResultE0OSgvp" class="token"><code>resultType</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  An optional field to indicates the type of result expected.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var resultType: StructuredQuery.ResultType?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-structuredquery-resulttype">ResultType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15StructuredQueryV5query10areaCenter15addressElements10resultTypeACSS_AA14GeoCoordinatesVAC07AddressH0VAC06ResultJ0OSgtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-query-areaCenter-addressElements-resultType" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-structuredquery#sdk-for-ios-navigate-s-7heresdk15StructuredQueryV5query10areaCenter15addressElements10resultTypeACSS_AA14GeoCoordinatesVAC07AddressH0VAC06ResultJ0OSgtcfc" class="token"><code>init(query:</code><wbr></wbr><code>areaCenter:</code><wbr></wbr><code>addressElements:</code><wbr></wbr><code>resultType:</code><wbr></wbr><code>)</code></a> 

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
  public init(query: String, areaCenter: GeoCoordinates, addressElements: StructuredQuery.AddressElements = StructuredQuery.AddressElements(), resultType: StructuredQuery.ResultType? = nil)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geocoordinates">GeoCoordinates</a>
  - <a href="sdk-for-ios-navigate-structs-structuredquery-addresselements">AddressElements</a>
  - <a href="sdk-for-ios-navigate-structs-structuredquery-resulttype">ResultType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15StructuredQueryV10ResultTypeO"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Enum-ResultType" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-structuredquery#sdk-for-ios-navigate-s-7heresdk15StructuredQueryV10ResultTypeO" class="token"><code>ResultType</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies expected result type.

  <a href="sdk-for-ios-navigate-structs-structuredquery-resulttype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum ResultType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15StructuredQueryV15AddressElementsV"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Struct-AddressElements" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-structuredquery#sdk-for-ios-navigate-s-7heresdk15StructuredQueryV15AddressElementsV" class="token"><code>AddressElements</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines query address elements which will be used to build address hierarchy during searches. It is advised to provide at least one intermediate address element when a large address element is provided for small admin area searches. For example if a user is building a query for a street and providing only country as an address element, consider providing city along with it.

  <a href="sdk-for-ios-navigate-structs-structuredquery-addresselements" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct AddressElements : Hashable
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

