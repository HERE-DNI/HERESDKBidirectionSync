---
title: "PointDataBuilder Class Reference"
slug: "sdk-for-ios-navigate-classes-pointdatabuilder"
---

# PointDataBuilder

<div class="declaration">

<div class="language">

``` highlight
public class PointDataBuilder
```

``` highlight
extension PointDataBuilder: NativeBase
```

``` highlight
extension PointDataBuilder: Hashable
```

</div>

</div>

Builder of <a href="sdk-for-ios-navigate-maps#sdk-for-ios-navigate-s-7heresdk9PointDataC">`PointData`</a> instances.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16PointDataBuilderCACycfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-pointdatabuilder#sdk-for-ios-navigate-s-7heresdk16PointDataBuilderCACycfc" class="token"><code>init()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a builder instance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16PointDataBuilderC15withCoordinatesyAcA03GeoF0VF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-withCoordinates-_" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-pointdatabuilder#sdk-for-ios-navigate-s-7heresdk16PointDataBuilderC15withCoordinatesyAcA03GeoF0VF" class="token"><code>withCoordinates(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configures the builder with geodetic coordinates for point to be created.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withCoordinates(_ coordinates: GeoCoordinates) -> PointDataBuilder
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geocoordinates">GeoCoordinates</a>

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
  <td><code> </code><em><code>coordinates</code></em><code> </code></td>
  <td><div>
  <p>Geodetic coordinates of the point. Altitude of coordinates is ignored.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The builder.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16PointDataBuilderC14withAttributesyAcA0cF0CF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-withAttributes-_" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-pointdatabuilder#sdk-for-ios-navigate-s-7heresdk16PointDataBuilderC14withAttributesyAcA0cF0CF" class="token"><code>withAttributes(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configures the builder with custom attributes for point to be created.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withAttributes(_ attributes: DataAttributes) -> PointDataBuilder
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
  <p>Custom data attributes to be associated with the point.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The builder.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16PointDataBuilderC5buildAA0bC0CyF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-build" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-pointdatabuilder#sdk-for-ios-navigate-s-7heresdk16PointDataBuilderC5buildAA0bC0CyF" class="token"><code>build()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Builds an instance of <a href="sdk-for-ios-navigate-maps#sdk-for-ios-navigate-s-7heresdk9PointDataC">`PointData`</a> and resets the builder instance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func build() -> PointData
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-maps#sdk-for-ios-navigate-s-7heresdk9PointDataC">PointData</a>

  </div>

  <div>

  #### Return Value

  Instance of <a href="sdk-for-ios-navigate-maps#sdk-for-ios-navigate-s-7heresdk9PointDataC">`PointData`</a> created with the configured parameters.

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

