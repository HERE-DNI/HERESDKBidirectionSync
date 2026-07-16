---
title: "PointDataAccessor Class Reference"
slug: "sdk-for-ios-explore-classes-pointdataaccessor"
---

# PointDataAccessor

<div class="declaration">

<div class="language">

``` highlight
public class PointDataAccessor
```

``` highlight
extension PointDataAccessor: NativeBase
```

``` highlight
extension PointDataAccessor: Hashable
```

</div>

</div>

Point data accessor used for manipulating points that are part of a PointDataSource.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17PointDataAccessorC14getCoordinatesAA03GeoF0VyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getCoordinates" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-pointdataaccessor#sdk-for-ios-explore-s-7heresdk17PointDataAccessorC14getCoordinatesAA03GeoF0VyF" class="token"><code>getCoordinates()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets point coordinates.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getCoordinates() -> GeoCoordinates
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocoordinates">GeoCoordinates</a>

  </div>

  <div>

  #### Return Value

  The point coordinates.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17PointDataAccessorC13getAttributesAA0cfD0CyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getAttributes" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-pointdataaccessor#sdk-for-ios-explore-s-7heresdk17PointDataAccessorC13getAttributesAA0cfD0CyF" class="token"><code>getAttributes()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets point attributes accessor.

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

  The point attributes accessor.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17PointDataAccessorC14setCoordinatesyyAA03GeoF0VF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-setCoordinates-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-pointdataaccessor#sdk-for-ios-explore-s-7heresdk17PointDataAccessorC14setCoordinatesyyAA03GeoF0VF" class="token"><code>setCoordinates(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Updates point coordinates.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setCoordinates(_ position: GeoCoordinates)
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
  <td><code> </code><em><code>position</code></em><code> </code></td>
  <td><div>
  <p>The new point coordinates.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17PointDataAccessorC13setAttributesyyAA0cF0CF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-setAttributes-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-pointdataaccessor#sdk-for-ios-explore-s-7heresdk17PointDataAccessorC13setAttributesyyAA0cF0CF" class="token"><code>setAttributes(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Replaces point attributes.

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
  <p>The new point attributes.</p>
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

