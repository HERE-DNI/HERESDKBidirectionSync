---
title: "PolygonDataSourceBuilder Class Reference"
slug: "sdk-for-ios-navigate-classes-polygondatasourcebuilder"
---

# PolygonDataSourceBuilder

<div class="declaration">

<div class="language">

``` highlight
public class PolygonDataSourceBuilder
```

``` highlight
extension PolygonDataSourceBuilder: NativeBase
```

``` highlight
extension PolygonDataSourceBuilder: Hashable
```

</div>

</div>

Builder of the polygons data source.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24PolygonDataSourceBuilderCyAcA10MapContextCcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-_" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-polygondatasourcebuilder#sdk-for-ios-navigate-s-7heresdk24PolygonDataSourceBuilderCyAcA10MapContextCcfc" class="token"><code>init(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a data source builder instance in the given context.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(_ context: MapContext)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapcontext">MapContext</a>

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
  <td><code> </code><em><code>context</code></em><code> </code></td>
  <td><div>
  <p>Map context to associate the data source with.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24PolygonDataSourceBuilderC8withNameyACSSF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-withName-_" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-polygondatasourcebuilder#sdk-for-ios-navigate-s-7heresdk24PolygonDataSourceBuilderC8withNameyACSSF" class="token"><code>withName(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configures the builder to use the given name for data source.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withName(_ dataSourceName: String) -> PolygonDataSourceBuilder
  ```

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
  <td><code> </code><em><code>dataSourceName</code></em><code> </code></td>
  <td><div>
  <p>Name of the created data source. Must be unique.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  This data source builder instance.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24PolygonDataSourceBuilderC04withB0yAcA0bC0CF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-withPolygon-_" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-polygondatasourcebuilder#sdk-for-ios-navigate-s-7heresdk24PolygonDataSourceBuilderC04withB0yAcA0bC0CF" class="token"><code>withPolygon(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configures the builder to insert the given polygon in the data source.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withPolygon(_ polygon: PolygonData) -> PolygonDataSourceBuilder
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-maps#sdk-for-ios-navigate-s-7heresdk11PolygonDataC">PolygonData</a>

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
  <td><code> </code><em><code>polygon</code></em><code> </code></td>
  <td><div>
  <p>The polygon to add.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  This data source builder instance.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24PolygonDataSourceBuilderC12withPolygonsyACSayAA0bC0CGF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-withPolygons-_" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-polygondatasourcebuilder#sdk-for-ios-navigate-s-7heresdk24PolygonDataSourceBuilderC12withPolygonsyACSayAA0bC0CGF" class="token"><code>withPolygons(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configures the builder to insert the given polygons in the data source.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withPolygons(_ polygon: [PolygonData]) -> PolygonDataSourceBuilder
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-maps#sdk-for-ios-navigate-s-7heresdk11PolygonDataC">PolygonData</a>

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
  <td><code> </code><em><code>polygon</code></em><code> </code></td>
  <td><div>
  <p>The polygons to add.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  This data source builder instance.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24PolygonDataSourceBuilderC5buildAA0bcD0CyF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-build" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-polygondatasourcebuilder#sdk-for-ios-navigate-s-7heresdk24PolygonDataSourceBuilderC5buildAA0bcD0CyF" class="token"><code>build()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Builds a PolygonDataSource instance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func build() -> PolygonDataSource
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-polygondatasource">PolygonDataSource</a>

  </div>

  <div>

  #### Return Value

  Instance of the data source created with given polygons and attributes.

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

