---
title: "PolygonDataBuilder Class Reference"
slug: "sdk-for-ios-navigate-classes-polygondatabuilder"
---

# PolygonDataBuilder

<div class="declaration">

<div class="language">

``` highlight
public class PolygonDataBuilder
```

``` highlight
extension PolygonDataBuilder: NativeBase
```

``` highlight
extension PolygonDataBuilder: Hashable
```

</div>

</div>

Builder of <a href="sdk-for-ios-navigate-maps#sdk-for-ios-navigate-s-7heresdk11PolygonDataC">`PolygonData`</a> instances.

The builder can create <a href="sdk-for-ios-navigate-maps#sdk-for-ios-navigate-s-7heresdk11PolygonDataC">`PolygonData`</a> instances for polygons with an outer boundary and optionally one or more inner boundaries (holes).

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18PolygonDataBuilderCACycfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-polygondatabuilder#sdk-for-ios-navigate-s-7heresdk18PolygonDataBuilderCACycfc" class="token"><code>init()</code></a> 

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

   <span id="sdk-for-ios-navigate-s-7heresdk18PolygonDataBuilderC12withGeometryyAcA03GeoB0VF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-withGeometry-_" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-polygondatabuilder#sdk-for-ios-navigate-s-7heresdk18PolygonDataBuilderC12withGeometryyAcA03GeoB0VF" class="token"><code>withGeometry(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configures the builder with geometry for the polygon to be created.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withGeometry(_ geometry: GeoPolygon) -> PolygonDataBuilder
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
  <p>Geometry of the polygon. The outer boundary has to be ordered clockwise and closed. Any inner boundary has to be ordered counterclockwise and closed. Altitude of boundary vertices is ignored. The visual behaviour for self-intersecting outer boundary is undefined.</p>
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

   <span id="sdk-for-ios-navigate-s-7heresdk18PolygonDataBuilderC14withAttributesyAcA0cF0CF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-withAttributes-_" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-polygondatabuilder#sdk-for-ios-navigate-s-7heresdk18PolygonDataBuilderC14withAttributesyAcA0cF0CF" class="token"><code>withAttributes(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configures the builder with custom attributes for polygon to be created.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withAttributes(_ attributes: DataAttributes) -> PolygonDataBuilder
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
  <p>Custom data attributes to be associated with the polygon.</p>
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

   <span id="sdk-for-ios-navigate-s-7heresdk18PolygonDataBuilderC5buildAA0bC0CyF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-build" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-polygondatabuilder#sdk-for-ios-navigate-s-7heresdk18PolygonDataBuilderC5buildAA0bC0CyF" class="token"><code>build()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Builds an instance of <a href="sdk-for-ios-navigate-maps#sdk-for-ios-navigate-s-7heresdk11PolygonDataC">`PolygonData`</a> and resets the builder instance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func build() -> PolygonData
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-maps#sdk-for-ios-navigate-s-7heresdk11PolygonDataC">PolygonData</a>

  </div>

  <div>

  #### Return Value

  Instance of <a href="sdk-for-ios-navigate-maps#sdk-for-ios-navigate-s-7heresdk11PolygonDataC">`PolygonData`</a> created with the configured parameters.

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

