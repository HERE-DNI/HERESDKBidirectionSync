---
title: "PolygonDataAccessor Class Reference"
slug: "sdk-for-ios-navigate-classes-polygondataaccessor"
---

# PolygonDataAccessor

<div class="declaration">

<div class="language">

``` highlight
public class PolygonDataAccessor
```

``` highlight
extension PolygonDataAccessor: NativeBase
```

``` highlight
extension PolygonDataAccessor: Hashable
```

</div>

</div>

Polygon data accessor used for manipulating polygons that are part of a PolygonDataSource.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19PolygonDataAccessorC11getGeometryAA03GeoB0VyF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getGeometry" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-polygondataaccessor#sdk-for-ios-navigate-s-7heresdk19PolygonDataAccessorC11getGeometryAA03GeoB0VyF" class="token"><code>getGeometry()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets polygon geometry.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getGeometry() -> GeoPolygon
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geopolygon">GeoPolygon</a>

  </div>

  <div>

  #### Return Value

  The polygon geometry.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19PolygonDataAccessorC13getAttributesAA0cfD0CyF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getAttributes" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-polygondataaccessor#sdk-for-ios-navigate-s-7heresdk19PolygonDataAccessorC13getAttributesAA0cfD0CyF" class="token"><code>getAttributes()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets polygon attributes accessor.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getAttributes() -> DataAttributesAccessor
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-dataattributesaccessor">DataAttributesAccessor</a>

  </div>

  <div>

  #### Return Value

  The polygon attributes accessor.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19PolygonDataAccessorC11setGeometryyyAA03GeoB0VF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-setGeometry-_" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-polygondataaccessor#sdk-for-ios-navigate-s-7heresdk19PolygonDataAccessorC11setGeometryyyAA03GeoB0VF" class="token"><code>setGeometry(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Replaces polygon geometry. The outer boundary has to be ordered clockwise and closed.

  Altitude of the vertices is ignored.

  The visual behaviour for self-intersecting outer boundary is undefined.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setGeometry(_ geometry: GeoPolygon)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geopolygon">GeoPolygon</a>

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
  <td><code> </code><em><code>geometry</code></em><code> </code></td>
  <td><div>
  <p>Geometry of the polygon. The outer boundary has to be ordered clockwise and closed. Altitude of the vertices is ignored. The visual behaviour for self-intersecting outer boundary is undefined.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19PolygonDataAccessorC13setAttributesyyAA0cF0CF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-setAttributes-_" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-polygondataaccessor#sdk-for-ios-navigate-s-7heresdk19PolygonDataAccessorC13setAttributesyyAA0cF0CF" class="token"><code>setAttributes(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Replaces polygon attributes.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setAttributes(_ attributes: DataAttributes)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-dataattributes">DataAttributes</a>

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
  <td><code> </code><em><code>attributes</code></em><code> </code></td>
  <td><div>
  <p>The attributes.</p>
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

