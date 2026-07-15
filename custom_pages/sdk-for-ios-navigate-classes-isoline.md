---
title: "Isoline Class Reference"
slug: "sdk-for-ios-navigate-classes-isoline"
---

# Isoline

<div class="declaration">

<div class="language">

``` highlight
public class Isoline
```

``` highlight
extension Isoline: NativeBase
```

``` highlight
extension Isoline: Hashable
```

</div>

</div>

Represents an isoline polygon around a center point. Any possible route between the center and any point on the edges of the polygon can be travelled within the given range restriction. The edges of the polygon are not guaranteed to be on the road as all reachable road endpoints are smoothened to fit into one polygon shape. This process can be influenced by setting <a href="sdk-for-ios-navigate-structs-isolineoptions-calculation#/s:7heresdk14IsolineOptionsV11CalculationV9maxPointss5Int32VSgvp">`IsolineOptions.Calculation.maxPoints`</a>.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

      init(rangeType: rangeValue: center: polygons: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs an isoline instance. This instance is provided by the <a href="sdk-for-ios-navigate-routing#/s:7heresdk33CalculateIsolineCompletionHandlera">`CalculateIsolineCompletionHandler`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( rangeType : IsolineRangeType , rangeValue : Double , center : MapMatchedCoordinates , polygons : [ GeoPolygon ])
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
  <td><code> </code><em><code>rangeType</code></em><code> </code></td>
  <td><div>
  <p>Specifies the range type of the provided</p>
  <pre><code>Isoline.init(...).rangeValue</code></pre>
  list.
  </p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>rangeValue</code></em><code> </code></td>
  <td><div>
  <p>A list of range values. At least one value must be set.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>center</code></em><code> </code></td>
  <td><div>
  <p>The center of the isoline.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>polygons</code></em><code> </code></td>
  <td><div>
  <p>A list of polygons that belong to this isoline. At least one value must be set.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk7IsolineC9rangeTypeAA0b5RangeD0Ovp"></span>` `<span id="//apple_ref/swift/Property/rangeType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-isoline#/s:7heresdk7IsolineC9rangeTypeAA0b5RangeD0Ovp" class="token"><code>rangeType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies the type of the restriction that was used to calculate this isoline.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var rangeType: IsolineRangeType { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk7IsolineC10rangeValueSdvp"></span>` `<span id="//apple_ref/swift/Property/rangeValue" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-isoline#/s:7heresdk7IsolineC10rangeValueSdvp" class="token"><code>rangeValue</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies the numerical value of the restriction that was used to calculate this isoline.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var rangeValue: Double { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk7IsolineC6centerAA21MapMatchedCoordinatesVvp"></span>` `<span id="//apple_ref/swift/Property/center" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-isoline#/s:7heresdk7IsolineC6centerAA21MapMatchedCoordinatesVvp" class="token"><code>center</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The center point that was used to calculate this isoline. Specifies the center point that was used to calculate this isoline. This includes the original center that was passed to the RoutingEngine.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var center: MapMatchedCoordinates { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk7IsolineC8polygonsSayAA10GeoPolygonVGvp"></span>` `<span id="//apple_ref/swift/Property/polygons" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-isoline#/s:7heresdk7IsolineC8polygonsSayAA10GeoPolygonVGvp" class="token"><code>polygons</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A list of polygons that belong to this isoline. An isoline can consist of multiple polygons. For example, islands that can be reached by a ferry are included. Each island is then represented as a separate polygon. However, in most cases only a single polygon is included.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var polygons: [GeoPolygon] { get }
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

