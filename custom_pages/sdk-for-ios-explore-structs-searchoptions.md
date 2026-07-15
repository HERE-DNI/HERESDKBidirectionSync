---
title: "SearchOptions Structure Reference"
slug: "sdk-for-ios-explore-structs-searchoptions"
---

# SearchOptions

<div class="declaration">

<div class="language">

``` highlight
public struct SearchOptions : Hashable
```

</div>

</div>

Encapsulates options that control the behavior of search and suggest operations.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk13SearchOptionsV12languageCodeAA08LanguageE0OSgvp"></span>` `<span id="//apple_ref/swift/Property/languageCode" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-searchoptions#/s:7heresdk13SearchOptionsV12languageCodeAA08LanguageE0OSgvp" class="token"><code>languageCode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The preferred language of the result. When unset or unsupported language is chosen, results will be returned in their local language.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var languageCode: LanguageCode?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13SearchOptionsV8maxItemss5Int32VSgvp"></span>` `<span id="//apple_ref/swift/Property/maxItems" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-searchoptions#/s:7heresdk13SearchOptionsV8maxItemss5Int32VSgvp" class="token"><code>maxItems</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The maximum number of items in the response. It should be in the range \[1, 100\]. When not set, results will be limited to 20. For location search (reverse geocode) by default results limited to 1.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maxItems: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13SearchOptionsV26highDensityEncodingEnabledSbvp"></span>` `<span id="//apple_ref/swift/Property/highDensityEncodingEnabled" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-searchoptions#/s:7heresdk13SearchOptionsV26highDensityEncodingEnabledSbvp" class="token"><code>highDensityEncodingEnabled</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Allows enabling high density encoding of relevant parameters. For now, it only affects input parameters of type <a href="sdk-for-ios-explore-structs-geocorridor">`GeoCorridor`</a>. Only supported for search in <a href="sdk-for-ios-explore-classes-searchengine">`SearchEngine`</a>, otherwise it is ignored. **Note:** This is a closed-alpha release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process. Only participants of the closed-alpha group can get access from HERE to use this feature, otherwise, a <a href="sdk-for-ios-explore-enums-searcherror#/s:7heresdk11SearchErrorO9forbiddenyA2CmF">`SearchError.forbidden`</a> will be propagated in callbacks.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var highDensityEncodingEnabled: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13SearchOptionsV18distributedResultsSbvp"></span>` `<span id="//apple_ref/swift/Property/distributedResults" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-searchoptions#/s:7heresdk13SearchOptionsV18distributedResultsSbvp" class="token"><code>distributedResults</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates if search along the route should produce well-distributed results. It is only supported for:

  - `searchByCategory` API with <a href="sdk-for-ios-explore-structs-categoryquery-area#/s:7heresdk13CategoryQueryV4AreaV08corridorD0AA11GeoCorridorVSgvp">`CategoryQuery.Area.corridorArea`</a> set
  - `searchByText` API with <a href="sdk-for-ios-explore-structs-textquery-area#/s:7heresdk9TextQueryV4AreaV08corridorD0AA11GeoCorridorVSgvp">`TextQuery.Area.corridorArea`</a> set Otherwise, this value is ignored.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var distributedResults: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(languageCode: maxItems: highDensityEncodingEnabled: distributedResults: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an Options object. If no parameters are passed, uses default values (see fields description).

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( languageCode : LanguageCode ? = nil , maxItems : Int32 ? = nil , highDensityEncodingEnabled : Bool = false , distributedResults : Bool = false )
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

