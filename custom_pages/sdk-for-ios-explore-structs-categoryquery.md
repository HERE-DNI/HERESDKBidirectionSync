---
title: "CategoryQuery Structure Reference"
slug: "sdk-for-ios-explore-structs-categoryquery"
---

# CategoryQuery

<div class="declaration">

<div class="language">

``` highlight
public struct CategoryQuery : Hashable
```

</div>

</div>

The options to specify a query by categories.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk13CategoryQueryV10categoriesSayAA05PlaceB0CGvp"></span>` `<span id="//apple_ref/swift/Property/categories" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-categoryquery#/s:7heresdk13CategoryQueryV10categoriesSayAA05PlaceB0CGvp" class="token"><code>categories</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of categories to be included. A place can be assigned multiple categories. If any of them is in `CategoryQuery.categories`, but none are in <a href="sdk-for-ios-explore-structs-categoryquery#/s:7heresdk13CategoryQueryV17excludeCategoriesSayAA05PlaceB0CGvp">`CategoryQuery.excludeCategories`</a>, that place will be included in the response.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var categories: [PlaceCategory]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13CategoryQueryV17excludeCategoriesSayAA05PlaceB0CGvp"></span>` `<span id="//apple_ref/swift/Property/excludeCategories" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-categoryquery#/s:7heresdk13CategoryQueryV17excludeCategoriesSayAA05PlaceB0CGvp" class="token"><code>excludeCategories</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of categories and subcategories to be excluded. A place can be assigned multiple categories. If any of them is in `CategoryQuery.excludeCategories`, that place will not be included in the response, regardless of whether any of its assigned categories have been included in <a href="sdk-for-ios-explore-structs-categoryquery#/s:7heresdk13CategoryQueryV10categoriesSayAA05PlaceB0CGvp">`CategoryQuery.categories`</a>. In short, an exclusion will always win over an inclusion. This is especially useful for excluding specific subcategories from the main category.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var excludeCategories: [PlaceCategory]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13CategoryQueryV13includeChainsSayAA10PlaceChainVGvp"></span>` `<span id="//apple_ref/swift/Property/includeChains" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-categoryquery#/s:7heresdk13CategoryQueryV13includeChainsSayAA10PlaceChainVGvp" class="token"><code>includeChains</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of chains to be included. A place can be assigned multiple chains. If any of them is in `CategoryQuery.includeChains`, but none are in <a href="sdk-for-ios-explore-structs-categoryquery#/s:7heresdk13CategoryQueryV13excludeChainsSayAA10PlaceChainVGvp">`CategoryQuery.excludeChains`</a>, that place will be included in the response.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var includeChains: [PlaceChain]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13CategoryQueryV13excludeChainsSayAA10PlaceChainVGvp"></span>` `<span id="//apple_ref/swift/Property/excludeChains" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-categoryquery#/s:7heresdk13CategoryQueryV13excludeChainsSayAA10PlaceChainVGvp" class="token"><code>excludeChains</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of chains to be excluded. A place can be assigned multiple chains. If any of them is in `CategoryQuery.excludeChains`, that place will not be included in the response, regardless of whether any of its assigned chains have been included in <a href="sdk-for-ios-explore-structs-categoryquery#/s:7heresdk13CategoryQueryV13includeChainsSayAA10PlaceChainVGvp">`CategoryQuery.includeChains`</a>. In short, an exclusion will always win over an inclusion.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var excludeChains: [PlaceChain]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13CategoryQueryV16includeFoodTypesSayAA05PlaceE4TypeVGvp"></span>` `<span id="//apple_ref/swift/Property/includeFoodTypes" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-categoryquery#/s:7heresdk13CategoryQueryV16includeFoodTypesSayAA05PlaceE4TypeVGvp" class="token"><code>includeFoodTypes</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of food types to be included. A place can be assigned multiple food types. If any of them is in `CategoryQuery.includeFoodTypes`, but none are in <a href="sdk-for-ios-explore-structs-categoryquery#/s:7heresdk13CategoryQueryV16excludeFoodTypesSayAA05PlaceE4TypeVGvp">`CategoryQuery.excludeFoodTypes`</a>, that place will be included in the response.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var includeFoodTypes: [PlaceFoodType]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13CategoryQueryV16excludeFoodTypesSayAA05PlaceE4TypeVGvp"></span>` `<span id="//apple_ref/swift/Property/excludeFoodTypes" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-categoryquery#/s:7heresdk13CategoryQueryV16excludeFoodTypesSayAA05PlaceE4TypeVGvp" class="token"><code>excludeFoodTypes</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of food types to be excluded. A place can be assigned multiple food types. If any of them is in `CategoryQuery.excludeFoodTypes`, that place will not be included in the response, regardless of whether any of its assigned food types have been included in <a href="sdk-for-ios-explore-structs-categoryquery#/s:7heresdk13CategoryQueryV16includeFoodTypesSayAA05PlaceE4TypeVGvp">`CategoryQuery.includeFoodTypes`</a>. In short, an exclusion will always win over an inclusion.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var excludeFoodTypes: [PlaceFoodType]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13CategoryQueryV6filterSSSgvp"></span>` `<span id="//apple_ref/swift/Property/filter" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-categoryquery#/s:7heresdk13CategoryQueryV6filterSSSgvp" class="token"><code>filter</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Full-text filter on POI names/titles. Results with a partial match are included in the response. By default the value is set to null and results will be based on other parameters provided.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var filter: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13CategoryQueryV11placeFilterAA05PlaceE0Vvp"></span>` `<span id="//apple_ref/swift/Property/placeFilter" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-categoryquery#/s:7heresdk13CategoryQueryV11placeFilterAA05PlaceE0Vvp" class="token"><code>placeFilter</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The filter options to specify a place in query. Consists of fuel and truck options.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var placeFilter: PlaceFilter
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13CategoryQueryV4areaAC4AreaVvp"></span>` `<span id="//apple_ref/swift/Property/area" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-categoryquery#/s:7heresdk13CategoryQueryV4areaAC4AreaVvp" class="token"><code>area</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Area in which to provide the most relevant places.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var area: CategoryQuery.Area
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(_: area: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs a new instance of this class from provided parameters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( _ category : PlaceCategory , area : CategoryQuery . Area )
  ```

  </pre>

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
  <td><code> </code><em><code>category</code></em><code> </code></td>
  <td><div>
  <p>Category for query</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>area</code></em><code> </code></td>
  <td><div>
  <p>Area in which to provide the most relevant places.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      init(_: area: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs a new instance of this class from provided parameters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( _ categories : [ PlaceCategory ], area : CategoryQuery . Area )
  ```

  </pre>

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
  <td><code> </code><em><code>categories</code></em><code> </code></td>
  <td><div>
  <p>List of categories.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>area</code></em><code> </code></td>
  <td><div>
  <p>Area in which to provide the most relevant places.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      init(_: filter: area: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs a new instance of this class from provided parameters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( _ category : PlaceCategory , filter : String , area : CategoryQuery . Area )
  ```

  </pre>

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
  <td><code> </code><em><code>category</code></em><code> </code></td>
  <td><div>
  <p>Category for query</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>filter</code></em><code> </code></td>
  <td><div>
  <p>Full-text filter on POI names/titles. Results with a partial match are included in the response.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>area</code></em><code> </code></td>
  <td><div>
  <p>Area in which to provide the most relevant places.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      init(_: filter: area: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs a new instance of this class from provided parameters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( _ categories : [ PlaceCategory ], filter : String , area : CategoryQuery . Area )
  ```

  </pre>

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
  <td><code> </code><em><code>categories</code></em><code> </code></td>
  <td><div>
  <p>List of categories.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>filter</code></em><code> </code></td>
  <td><div>
  <p>Full-text filter on POI names/titles. Results with a partial match are included in the response.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>area</code></em><code> </code></td>
  <td><div>
  <p>Area in which to provide the most relevant places.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13CategoryQueryV4AreaV"></span>` `<span id="//apple_ref/swift/Struct/Area" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-categoryquery#/s:7heresdk13CategoryQueryV4AreaV" class="token"><code>Area</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Area to perform search on.

  <a href="sdk-for-ios-explore-structs-categoryquery-area" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct Area : Hashable
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

