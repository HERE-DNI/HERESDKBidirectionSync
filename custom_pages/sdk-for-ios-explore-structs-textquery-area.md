---
title: "Area Structure Reference"
slug: "sdk-for-ios-explore-structs-textquery-area"
---

# Area

<div class="declaration">

<div class="language">

``` highlight
public struct Area : Hashable
```

</div>

</div>

Area to perform search on.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9TextQueryV4AreaV10areaCenterAA14GeoCoordinatesVSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-areaCenter" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-textquery-area#sdk-for-ios-explore-s-7heresdk9TextQueryV4AreaV10areaCenterAA14GeoCoordinatesVSgvp" class="token"><code>areaCenter</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Geographic coordinates of the center around which to provide the most relevant places. For Offline Search, one of `TextQuery.Area.areaCenter`, <a href="sdk-for-ios-explore-structs-textquery-area#sdk-for-ios-explore-s-7heresdk9TextQueryV4AreaV03boxD0AA6GeoBoxVSgvp">`TextQuery.Area.boxArea`</a> and <a href="sdk-for-ios-explore-structs-textquery-area#sdk-for-ios-explore-s-7heresdk9TextQueryV4AreaV06circleD0AA9GeoCircleVSgvp">`TextQuery.Area.circleArea`</a> has to be set, otherwise it will result in <a href="sdk-for-ios-explore-enums-searcherror#sdk-for-ios-explore-s-7heresdk11SearchErrorO11invalidAreayA2CmF">`SearchError.invalidArea`</a>.

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

  - <a href="sdk-for-ios-explore-structs-geocoordinates">GeoCoordinates</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9TextQueryV4AreaV03boxD0AA6GeoBoxVSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-boxArea" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-textquery-area#sdk-for-ios-explore-s-7heresdk9TextQueryV4AreaV03boxD0AA6GeoBoxVSgvp" class="token"><code>boxArea</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Geographic rectangle area in which to provide the most relevant places. For Offline Search, one of <a href="sdk-for-ios-explore-structs-textquery-area#sdk-for-ios-explore-s-7heresdk9TextQueryV4AreaV10areaCenterAA14GeoCoordinatesVSgvp">`TextQuery.Area.areaCenter`</a>, `TextQuery.Area.boxArea` and <a href="sdk-for-ios-explore-structs-textquery-area#sdk-for-ios-explore-s-7heresdk9TextQueryV4AreaV06circleD0AA9GeoCircleVSgvp">`TextQuery.Area.circleArea`</a> has to be set, otherwise it will result in <a href="sdk-for-ios-explore-enums-searcherror#sdk-for-ios-explore-s-7heresdk11SearchErrorO11invalidAreayA2CmF">`SearchError.invalidArea`</a>. Also, for Offline Search, search in a given <a href="sdk-for-ios-explore-structs-geobox">`GeoBox`</a> restricts the results to only POIs.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public let boxArea: GeoBox?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geobox">GeoBox</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9TextQueryV4AreaV06circleD0AA9GeoCircleVSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-circleArea" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-textquery-area#sdk-for-ios-explore-s-7heresdk9TextQueryV4AreaV06circleD0AA9GeoCircleVSgvp" class="token"><code>circleArea</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Geographic circle area in which to provide the most relevant places. For Offline Search, one of <a href="sdk-for-ios-explore-structs-textquery-area#sdk-for-ios-explore-s-7heresdk9TextQueryV4AreaV10areaCenterAA14GeoCoordinatesVSgvp">`TextQuery.Area.areaCenter`</a>, <a href="sdk-for-ios-explore-structs-textquery-area#sdk-for-ios-explore-s-7heresdk9TextQueryV4AreaV03boxD0AA6GeoBoxVSgvp">`TextQuery.Area.boxArea`</a> and `TextQuery.Area.circleArea` has to be set, otherwise it will result in <a href="sdk-for-ios-explore-enums-searcherror#sdk-for-ios-explore-s-7heresdk11SearchErrorO11invalidAreayA2CmF">`SearchError.invalidArea`</a>. Also, for Offline Search, search in a given <a href="sdk-for-ios-explore-structs-geocircle">`GeoCircle`</a> restricts the results to only POIs.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public let circleArea: GeoCircle?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocircle">GeoCircle</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9TextQueryV4AreaV08corridorD0AA11GeoCorridorVSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-corridorArea" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-textquery-area#sdk-for-ios-explore-s-7heresdk9TextQueryV4AreaV08corridorD0AA11GeoCorridorVSgvp" class="token"><code>corridorArea</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Geographic corridor area in which to provide the most relevant places. The contained polyline and half-width define the area that will be used in a search query.

  When used with SearchEngine, the polyline is compressed and sent. More complex polylines with large amounts of coordinates and with smaller half-width may have the less relevant part removed, such as the one far away from the search center. This usually makes no difference, because there will be enough POIs near the search center. For use cases where it is important to search the entire polyline, half-width can be increased or not set. For example: Route between New York and Chicago with half-width 800 will be added to request without removing the far away part, but route of the same length (around 360km) between Milan (Italy) and Konstanz (Germany) will have the far away part removed due to its complexity.

  When `TextQuery.Area.corridorArea` is provided, <a href="sdk-for-ios-explore-structs-textquery-area#sdk-for-ios-explore-s-7heresdk9TextQueryV4AreaV10areaCenterAA14GeoCoordinatesVSgvp">`TextQuery.Area.areaCenter`</a> has to be within it, otherwise <a href="sdk-for-ios-explore-structs-textquery-area#sdk-for-ios-explore-s-7heresdk9TextQueryV4AreaV10areaCenterAA14GeoCoordinatesVSgvp">`TextQuery.Area.areaCenter`</a> is ignored when searching.

  For Offline Search, search in a given <a href="sdk-for-ios-explore-structs-geocorridor">`GeoCorridor`</a> restricts the results to only POIs.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public let corridorArea: GeoCorridor?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocorridor">GeoCorridor</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9TextQueryV4AreaV9countriesSayAA11CountryCodeOGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-countries" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-textquery-area#sdk-for-ios-explore-s-7heresdk9TextQueryV4AreaV9countriesSayAA11CountryCodeOGvp" class="token"><code>countries</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A list of countries that the query is applied in. Not supported in <a href="sdk-for-ios-explore-classes-offlinesearchengine">`OfflineSearchEngine`</a> (which is only available for the Navigate license).

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

  - <a href="sdk-for-ios-explore-enums-countrycode">CountryCode</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9TextQueryV4AreaV10areaCenterAeA14GeoCoordinatesV_tcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-areaCenter" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-textquery-area#sdk-for-ios-explore-s-7heresdk9TextQueryV4AreaV10areaCenterAeA14GeoCoordinatesV_tcfc" class="token"><code>init(areaCenter:</code><wbr></wbr><code>)</code></a> 

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
  public init(areaCenter: GeoCoordinates)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocoordinates">GeoCoordinates</a>

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
  <td><code> </code><em><code>areaCenter</code></em><code> </code></td>
  <td><div>
  <p>Geographic coordinates of the center around which to provide the most relevant places.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9TextQueryV4AreaV5inBoxAeA03GeoF0V_tcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-inBox" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-textquery-area#sdk-for-ios-explore-s-7heresdk9TextQueryV4AreaV5inBoxAeA03GeoF0V_tcfc" class="token"><code>init(inBox:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs a new instance of this class from provided parameters. For Offline Search, search in a given <a href="sdk-for-ios-explore-structs-geobox">`GeoBox`</a> restricts the results to only POIs.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(inBox boxArea: GeoBox)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geobox">GeoBox</a>

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
  <td><code> </code><em><code>boxArea</code></em><code> </code></td>
  <td><div>
  <p>Geographic rectangle area in which to provide the most relevant places.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9TextQueryV4AreaV8inCircleAeA03GeoF0V_tcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-inCircle" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-textquery-area#sdk-for-ios-explore-s-7heresdk9TextQueryV4AreaV8inCircleAeA03GeoF0V_tcfc" class="token"><code>init(inCircle:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs a new instance of this class from provided parameters. For Offline Search, search in a given <a href="sdk-for-ios-explore-structs-geocircle">`GeoCircle`</a> restricts the results to only POIs.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(inCircle circleArea: GeoCircle)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocircle">GeoCircle</a>

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
  <td><code> </code><em><code>circleArea</code></em><code> </code></td>
  <td><div>
  <p>Geographic circle area in which to provide the most relevant places.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9TextQueryV4AreaV10inCorridor4nearAeA03GeoF0V_AA0H11CoordinatesVtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-inCorridor-near" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-textquery-area#sdk-for-ios-explore-s-7heresdk9TextQueryV4AreaV10inCorridor4nearAeA03GeoF0V_AA0H11CoordinatesVtcfc" class="token"><code>init(inCorridor:</code><wbr></wbr><code>near:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs a new instance of this class from provided parameters. The given corridor and center define the area that will be used in the search query.

  When used with SearchEngine, the polyline is compressed and sent. More complex polylines with large amounts of coordinates and with smaller half-width may have the less relevant part removed, such as the one far away from the search center. This usually makes no difference, because there will be enough POIs near the search center. For use cases where it is important to search the entire polyline, half-width can be increased or not set. For example: Route between New York and Chicago with half-width 800 will be added to request without removing the far away part, but route of the same length (around 360km) between Milan (Italy) and Konstanz (Germany) will have the far away part removed due to its complexity.

  The area center has to be within the corridor, otherwise it is ignored.

  For Offline Search, search in a given <a href="sdk-for-ios-explore-structs-geocorridor">`GeoCorridor`</a> restricts the results to only POIs.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(inCorridor corridorArea: GeoCorridor, near areaCenter: GeoCoordinates)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocorridor">GeoCorridor</a>
  - <a href="sdk-for-ios-explore-structs-geocoordinates">GeoCoordinates</a>

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
  <td><code> </code><em><code>corridorArea</code></em><code> </code></td>
  <td><div>
  <p>Geographic corridor area in which to provide the most relevant places.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>areaCenter</code></em><code> </code></td>
  <td><div>
  <p>Geographic coordinates of the prioritized area center.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9TextQueryV4AreaV11inCountries4nearAESayAA11CountryCodeOG_AA14GeoCoordinatesVtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-inCountries-near" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-textquery-area#sdk-for-ios-explore-s-7heresdk9TextQueryV4AreaV11inCountries4nearAESayAA11CountryCodeOG_AA14GeoCoordinatesVtcfc" class="token"><code>init(inCountries:</code><wbr></wbr><code>near:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs a new instance of this class from provided parameters. The given list of countries and center define the area that will be used in the search query.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(inCountries countries: [CountryCode], near areaCenter: GeoCoordinates)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-countrycode">CountryCode</a>
  - <a href="sdk-for-ios-explore-structs-geocoordinates">GeoCoordinates</a>

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
  <td><code> </code><em><code>countries</code></em><code> </code></td>
  <td><div>
  <p>A list of countries that the query is applied in.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>areaCenter</code></em><code> </code></td>
  <td><div>
  <p>Geographic coordinates of the prioritized area center.</p>
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

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

