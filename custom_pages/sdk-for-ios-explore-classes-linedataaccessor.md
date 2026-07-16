---
title: "LineDataAccessor Class Reference"
slug: "sdk-for-ios-explore-classes-linedataaccessor"
---

# LineDataAccessor

<div class="declaration">

<div class="language">

``` highlight
public class LineDataAccessor
```

``` highlight
extension LineDataAccessor: NativeBase
```

``` highlight
extension LineDataAccessor: Hashable
```

</div>

</div>

Line data accessor used for manipulating polylines that are part of a LineDataSource.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16LineDataAccessorC11getGeometryAA11GeoPolylineVyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getGeometry" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-linedataaccessor#sdk-for-ios-explore-s-7heresdk16LineDataAccessorC11getGeometryAA11GeoPolylineVyF" class="token"><code>getGeometry()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets polyline geometry.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getGeometry() -> GeoPolyline
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geopolyline">GeoPolyline</a>

  </div>

  <div>

  #### Return Value

  The line geometry.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16LineDataAccessorC13getAttributesAA0cfD0CyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getAttributes" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-linedataaccessor#sdk-for-ios-explore-s-7heresdk16LineDataAccessorC13getAttributesAA0cfD0CyF" class="token"><code>getAttributes()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets polyline attributes accessor.

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

  - <a href="sdk-for-ios-explore-classes-dataattributesaccessor">DataAttributesAccessor</a>

  </div>

  <div>

  #### Return Value

  The polyline attributes accessor.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16LineDataAccessorC11setGeometryyyAA11GeoPolylineVF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-setGeometry-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-linedataaccessor#sdk-for-ios-explore-s-7heresdk16LineDataAccessorC11setGeometryyyAA11GeoPolylineVF" class="token"><code>setGeometry(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Replaces polyline geometry. Altitude of the vertices is ignored.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setGeometry(_ geometry: GeoPolyline)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geopolyline">GeoPolyline</a>

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
  <p>The geometry.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16LineDataAccessorC13setAttributesyyAA0cF0CF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-setAttributes-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-linedataaccessor#sdk-for-ios-explore-s-7heresdk16LineDataAccessorC13setAttributesyyAA0cF0CF" class="token"><code>setAttributes(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Replaces polyline attributes.

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

  - <a href="sdk-for-ios-explore-classes-dataattributes">DataAttributes</a>

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

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

