---
title: "TextQuery Structure Reference"
slug: "sdk-for-ios-explore-structs-textquery"
---

# TextQuery

<div class="declaration">

<div class="language">

``` highlight
public struct TextQuery : Hashable
```

</div>

</div>

The options to specify a text query.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9TextQueryV5querySSvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-query" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-textquery#sdk-for-ios-explore-s-7heresdk9TextQueryV5querySSvp" class="token"><code>query</code></a> 

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

   <span id="sdk-for-ios-explore-s-7heresdk9TextQueryV4areaAC4AreaVvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-area" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-textquery#sdk-for-ios-explore-s-7heresdk9TextQueryV4areaAC4AreaVvp" class="token"><code>area</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Area which to provide the most relevant places.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var area: TextQuery.Area
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-textquery-area">Area</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9TextQueryV11placeFilterAA05PlaceE0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-placeFilter" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-textquery#sdk-for-ios-explore-s-7heresdk9TextQueryV11placeFilterAA05PlaceE0Vvp" class="token"><code>placeFilter</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-structs-placefilter">PlaceFilter</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9TextQueryV_4areaACSS_AC4AreaVtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-_-area" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-textquery#sdk-for-ios-explore-s-7heresdk9TextQueryV_4areaACSS_AC4AreaVtcfc" class="token"><code>init(_:</code><wbr></wbr><code>area:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs a TextQuery from the provided text query and geographic area. For Offline Search, search in a given <a href="sdk-for-ios-explore-structs-geobox">`GeoBox`</a>, <a href="sdk-for-ios-explore-structs-geocircle">`GeoCircle`</a> or <a href="sdk-for-ios-explore-structs-geocorridor">`GeoCorridor`</a> restricts the results to only POIs.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(_ query: String, area: TextQuery.Area)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-textquery-area">Area</a>

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
  <td><code> </code><em><code>area</code></em><code> </code></td>
  <td><div>
  <p>Area which to provide the most relevant places.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9TextQueryV4AreaV"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Struct-Area" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-textquery#sdk-for-ios-explore-s-7heresdk9TextQueryV4AreaV" class="token"><code>Area</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Area to perform search on.

  <a href="sdk-for-ios-explore-structs-textquery-area" class="slightly-smaller">See more</a>

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

