---
title: "GeoPolygon Structure Reference"
slug: "sdk-for-ios-explore-structs-geopolygon"
---

# GeoPolygon

<div class="declaration">

<div class="language">

``` highlight
public struct GeoPolygon : Hashable
```

</div>

</div>

Represents a `GeoPolygon` area as a series of geographic coordinates, and optionally, a list of inner boundaries (also known as holes). An instance of this class, initialized with appropriate vertices.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk10GeoPolygonV8verticesSayAA0B11CoordinatesVGvp"></span>` `<span id="//apple_ref/swift/Property/vertices" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-geopolygon#/s:7heresdk10GeoPolygonV8verticesSayAA0B11CoordinatesVGvp" class="token"><code>vertices</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of geographic coordinates representing the outer boundary vertices of polygon.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public let vertices: [GeoCoordinates]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10GeoPolygonV15innerBoundariesSaySayAA0B11CoordinatesVGGvp"></span>` `<span id="//apple_ref/swift/Property/innerBoundaries" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-geopolygon#/s:7heresdk10GeoPolygonV15innerBoundariesSaySayAA0B11CoordinatesVGGvp" class="token"><code>innerBoundaries</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of polygon inner boundaries (holes), each defined as a list of geographic coordinates.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public let innerBoundaries: [[GeoCoordinates]]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(vertices: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs an instance of this class from the provided vertices. Throws InstantiationError if the number of vertices is less than three.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-explore-core#/s:7heresdk18InstantiationErrora">`InstantiationError`</a> Instantiation error.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( vertices : [ GeoCoordinates ]) throws
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
  <td><code> </code><em><code>vertices</code></em><code> </code></td>
  <td><div>
  <p>List of vertices representing the polygon outer boundary in clockwise order.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      init(vertices: innerBoundaries: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs an instance of this class from the provided vertices and inner boundaries (holes). Throws InstantiationError if the number of vertices is less than three.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-explore-core#/s:7heresdk18InstantiationErrora">`InstantiationError`</a> Instantiation error.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( vertices : [ GeoCoordinates ], innerBoundaries : [[ GeoCoordinates ]]) throws
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
  <td><code> </code><em><code>vertices</code></em><code> </code></td>
  <td><div>
  <p>List of vertices representing the polygon outer boundary in clockwise order.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>innerBoundaries</code></em><code> </code></td>
  <td><div>
  <p>List of polygon inner boundaries (holes), each in counterclockwise order.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      init(geoCircle: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs an instance of this class from <a href="sdk-for-ios-explore-structs-geocircle">`GeoCircle`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( geoCircle : GeoCircle )
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
  <td><code> </code><em><code>geoCircle</code></em><code> </code></td>
  <td><div>
  <p>A <a href="sdk-for-ios-explore-structs-geocircle"><code>GeoCircle</code></a> to be converted into <code>GeoPolygon</code>.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      init(geoBox: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs an instance of this class from <a href="sdk-for-ios-explore-structs-geobox">`GeoBox`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( geoBox : GeoBox )
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
  <td><code> </code><em><code>geoBox</code></em><code> </code></td>
  <td><div>
  <p>A rectangle defined by the <a href="sdk-for-ios-explore-structs-geobox"><code>GeoBox</code></a> to be converted into <code>GeoPolygon</code>. The corner coordinates defined by the <a href="sdk-for-ios-explore-structs-geobox"><code>GeoBox</code></a> will define the outer boundary verticies of the <code>GeoPolygon</code>.</p>
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

