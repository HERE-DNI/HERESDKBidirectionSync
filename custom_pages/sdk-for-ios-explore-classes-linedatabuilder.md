---
title: "LineDataBuilder Class Reference"
slug: "sdk-for-ios-explore-classes-linedatabuilder"
---

# LineDataBuilder

<div class="declaration">

<div class="language">

``` highlight
public class LineDataBuilder
```

``` highlight
extension LineDataBuilder: NativeBase
```

``` highlight
extension LineDataBuilder: Hashable
```

</div>

</div>

Builder of <a href="sdk-for-ios-explore-maploader#sdk-for-ios-explore-s-7heresdk8LineDataC">`LineData`</a> instances.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15LineDataBuilderCACycfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-linedatabuilder#sdk-for-ios-explore-s-7heresdk15LineDataBuilderCACycfc" class="token"><code>init()</code></a> 

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

   <span id="sdk-for-ios-explore-s-7heresdk15LineDataBuilderC12withGeometryyAcA11GeoPolylineVF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-withGeometry-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-linedatabuilder#sdk-for-ios-explore-s-7heresdk15LineDataBuilderC12withGeometryyAcA11GeoPolylineVF" class="token"><code>withGeometry(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configures the builder with geometry for line to be created.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withGeometry(_ geometry: GeoPolyline) -> LineDataBuilder
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
  <p>Geometry of the polyline. Each vertex defines two line segments: one with a previous vertex and one with a next vertex. First and last vertices don’t have resp. previous and next vertices and thus belong to single line segments. Consecutive duplicate vertices are ignored. Altitude of polyline vertices is ignored.</p>
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

   <span id="sdk-for-ios-explore-s-7heresdk15LineDataBuilderC14withAttributesyAcA0cF0CF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-withAttributes-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-linedatabuilder#sdk-for-ios-explore-s-7heresdk15LineDataBuilderC14withAttributesyAcA0cF0CF" class="token"><code>withAttributes(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configures the builder with custom attributes for line to be created.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withAttributes(_ attributes: DataAttributes) -> LineDataBuilder
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
  <p>Custom data attributes to be associated with the line.</p>
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

   <span id="sdk-for-ios-explore-s-7heresdk15LineDataBuilderC5buildAA0bC0CyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-build" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-linedatabuilder#sdk-for-ios-explore-s-7heresdk15LineDataBuilderC5buildAA0bC0CyF" class="token"><code>build()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Builds an instance of <a href="sdk-for-ios-explore-maploader#sdk-for-ios-explore-s-7heresdk8LineDataC">`LineData`</a> and resets the builder instance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func build() -> LineData
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-maploader#sdk-for-ios-explore-s-7heresdk8LineDataC">LineData</a>

  </div>

  <div>

  #### Return Value

  Instance of <a href="sdk-for-ios-explore-maploader#sdk-for-ios-explore-s-7heresdk8LineDataC">`LineData`</a> created with the configured parameters.

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

