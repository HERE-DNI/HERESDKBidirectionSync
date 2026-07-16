---
title: "LineDataSourceBuilder Class Reference"
slug: "sdk-for-ios-navigate-classes-linedatasourcebuilder"
---

# LineDataSourceBuilder

<div class="declaration">

<div class="language">

``` highlight
public class LineDataSourceBuilder
```

``` highlight
extension LineDataSourceBuilder: NativeBase
```

``` highlight
extension LineDataSourceBuilder: Hashable
```

</div>

</div>

Builder of lines data source.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk21LineDataSourceBuilderCyAcA10MapContextCcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-_" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-linedatasourcebuilder#sdk-for-ios-navigate-s-7heresdk21LineDataSourceBuilderCyAcA10MapContextCcfc" class="token"><code>init(_:</code><wbr></wbr><code>)</code></a> 

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

   <span id="sdk-for-ios-navigate-s-7heresdk21LineDataSourceBuilderC8withNameyACSSF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-withName-_" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-linedatasourcebuilder#sdk-for-ios-navigate-s-7heresdk21LineDataSourceBuilderC8withNameyACSSF" class="token"><code>withName(_:</code><wbr></wbr><code>)</code></a> 

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
  public func withName(_ dataSourceName: String) -> LineDataSourceBuilder
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

   <span id="sdk-for-ios-navigate-s-7heresdk21LineDataSourceBuilderC12withPolylineyAcA0bC0CF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-withPolyline-_" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-linedatasourcebuilder#sdk-for-ios-navigate-s-7heresdk21LineDataSourceBuilderC12withPolylineyAcA0bC0CF" class="token"><code>withPolyline(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configures the builder to insert the given polyline in the data source.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withPolyline(_ polyline: LineData) -> LineDataSourceBuilder
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk8LineDataC">LineData</a>

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
  <td><code> </code><em><code>polyline</code></em><code> </code></td>
  <td><div>
  <p>Polyline to add.</p>
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

   <span id="sdk-for-ios-navigate-s-7heresdk21LineDataSourceBuilderC13withPolylinesyACSayAA0bC0CGF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-withPolylines-_" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-linedatasourcebuilder#sdk-for-ios-navigate-s-7heresdk21LineDataSourceBuilderC13withPolylinesyACSayAA0bC0CGF" class="token"><code>withPolylines(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configures the builder to insert the given polylines in the data source.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withPolylines(_ polylines: [LineData]) -> LineDataSourceBuilder
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-maploader#sdk-for-ios-navigate-s-7heresdk8LineDataC">LineData</a>

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
  <td><code> </code><em><code>polylines</code></em><code> </code></td>
  <td><div>
  <p>Polylines to add.</p>
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

   <span id="sdk-for-ios-navigate-s-7heresdk21LineDataSourceBuilderC5buildAA0bcD0CyF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-build" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-linedatasourcebuilder#sdk-for-ios-navigate-s-7heresdk21LineDataSourceBuilderC5buildAA0bcD0CyF" class="token"><code>build()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Builds instance of LineDataSource.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func build() -> LineDataSource
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-linedatasource">LineDataSource</a>

  </div>

  <div>

  #### Return Value

  Instance of the data source created with given polylines and attributes.

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

