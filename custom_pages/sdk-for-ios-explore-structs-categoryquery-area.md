---
title: "Area Structure Reference"
slug: "sdk-for-ios-explore-structs-categoryquery-area"
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

  ` `<span id="/s:7heresdk13CategoryQueryV4AreaV10areaCenterAA14GeoCoordinatesVvp"></span>` `<span id="//apple_ref/swift/Property/areaCenter" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-categoryquery-area#/s:7heresdk13CategoryQueryV4AreaV10areaCenterAA14GeoCoordinatesVvp" class="token"><code>areaCenter</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Geographic coordinates of the center around which to provide the most relevant places.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public let areaCenter: GeoCoordinates
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13CategoryQueryV4AreaV03boxD0AA6GeoBoxVSgvp"></span>` `<span id="//apple_ref/swift/Property/boxArea" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-categoryquery-area#/s:7heresdk13CategoryQueryV4AreaV03boxD0AA6GeoBoxVSgvp" class="token"><code>boxArea</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Geographic rectangle area in which to provide the most relevant places.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public let boxArea: GeoBox?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13CategoryQueryV4AreaV06circleD0AA9GeoCircleVSgvp"></span>` `<span id="//apple_ref/swift/Property/circleArea" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-categoryquery-area#/s:7heresdk13CategoryQueryV4AreaV06circleD0AA9GeoCircleVSgvp" class="token"><code>circleArea</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Geographic circle area in which to provide the most relevant places.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public let circleArea: GeoCircle?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13CategoryQueryV4AreaV08corridorD0AA11GeoCorridorVSgvp"></span>` `<span id="//apple_ref/swift/Property/corridorArea" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-categoryquery-area#/s:7heresdk13CategoryQueryV4AreaV08corridorD0AA11GeoCorridorVSgvp" class="token"><code>corridorArea</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Geographic corridor area in which to provide the most relevant places. The contained polyline and half-width define the area that will be used in a search query.

  When used with <a href="sdk-for-ios-explore-classes-searchengine">`SearchEngine`</a>, the polyline is compressed and sent. More complex polylines with large amounts of coordinates and with smaller half-width may have the less relevant part removed, such as the one far away from the search center. This usually makes no difference, because there will be enough POIs near the search center. For use cases where it is important to search the entire polyline, half-width can be increased or not set. For example: Route between New York and Chicago with half-width 800 will be added to request without removing the far away part, but route of the same length (around 360km) between Milan (Italy) and Konstanz (Germany) will have the far away part removed due to its complexity.

  When `CategoryQuery.Area.corridorArea` is provided, <a href="sdk-for-ios-explore-structs-categoryquery-area#/s:7heresdk13CategoryQueryV4AreaV10areaCenterAA14GeoCoordinatesVvp">`CategoryQuery.Area.areaCenter`</a> has to be within it, otherwise <a href="sdk-for-ios-explore-structs-categoryquery-area#/s:7heresdk13CategoryQueryV4AreaV10areaCenterAA14GeoCoordinatesVvp">`CategoryQuery.Area.areaCenter`</a> is ignored when searching.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public let corridorArea: GeoCorridor?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(areaCenter: )

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
  public init ( areaCenter : GeoCoordinates )
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

      init(near: inBox: )

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
  public init ( near areaCenter : GeoCoordinates , inBox boxArea : GeoBox )
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
  <td><code> </code><em><code>areaCenter</code></em><code> </code></td>
  <td><div>
  <p>Geographic coordinates of the center around which to provide the most relevant places.</p>
  </div></td>
  </tr>
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

      init(near: inCircle: )

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
  public init ( near areaCenter : GeoCoordinates , inCircle circleArea : GeoCircle )
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
  <td><code> </code><em><code>areaCenter</code></em><code> </code></td>
  <td><div>
  <p>Geographic coordinates of the center around which to provide the most relevant places.</p>
  </div></td>
  </tr>
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

      init(inCorridor: near: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs a new instance of this class from provided parameters. The given corridor and center define the area that will be used in the search query.

  When used with <a href="sdk-for-ios-explore-classes-searchengine">`SearchEngine`</a>, the polyline is compressed and sent. More complex polylines with large amounts of coordinates and with smaller half-width may have the less relevant part removed, such as the one far away from the search center. This usually makes no difference, because there will be enough POIs near the search center. For use cases where it is important to search the entire polyline, half-width can be increased or not set. For example: Route between New York and Chicago with half-width 800 will be added to request without removing the far away part, but route of the same length (around 360km) between Milan (Italy) and Konstanz (Germany) will have the far away part removed due to its complexity.

  The area center has to be within the corridor, otherwise it is ignored.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( inCorridor corridorArea : GeoCorridor , near areaCenter : GeoCoordinates )
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

</div>

</div>

</div>

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

