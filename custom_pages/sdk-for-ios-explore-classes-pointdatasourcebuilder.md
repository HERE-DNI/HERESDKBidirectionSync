---
title: "PointDataSourceBuilder Class Reference"
slug: "sdk-for-ios-explore-classes-pointdatasourcebuilder"
---

# PointDataSourceBuilder

<div class="declaration">

<div class="language">

``` highlight
public class PointDataSourceBuilder
```

``` highlight
extension PointDataSourceBuilder: NativeBase
```

``` highlight
extension PointDataSourceBuilder: Hashable
```

</div>

</div>

Builder of points data source.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22PointDataSourceBuilderCyAcA10MapContextCcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-pointdatasourcebuilder#sdk-for-ios-explore-s-7heresdk22PointDataSourceBuilderCyAcA10MapContextCcfc" class="token"><code>init(_:</code><wbr></wbr><code>)</code></a> 

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

  - <a href="sdk-for-ios-explore-classes-mapcontext">MapContext</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk22PointDataSourceBuilderC8withNameyACSSF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-withName-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-pointdatasourcebuilder#sdk-for-ios-explore-s-7heresdk22PointDataSourceBuilderC8withNameyACSSF" class="token"><code>withName(_:</code><wbr></wbr><code>)</code></a> 

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
  public func withName(_ dataSourceName: String) -> PointDataSourceBuilder
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

   <span id="sdk-for-ios-explore-s-7heresdk22PointDataSourceBuilderC04withB0yAcA0bC0CF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-withPoint-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-pointdatasourcebuilder#sdk-for-ios-explore-s-7heresdk22PointDataSourceBuilderC04withB0yAcA0bC0CF" class="token"><code>withPoint(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configures the builder to insert the given point in the data source.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withPoint(_ point: PointData) -> PointDataSourceBuilder
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-maps#sdk-for-ios-explore-s-7heresdk9PointDataC">PointData</a>

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
  <td><code> </code><em><code>point</code></em><code> </code></td>
  <td><div>
  <p>Point to be added.</p>
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

   <span id="sdk-for-ios-explore-s-7heresdk22PointDataSourceBuilderC10withPoints6pointsACSayAA0bC0CG_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-withPoints-points" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-pointdatasourcebuilder#sdk-for-ios-explore-s-7heresdk22PointDataSourceBuilderC10withPoints6pointsACSayAA0bC0CG_tF" class="token"><code>withPoints(points:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configures the builder to insert the given points in the data source.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withPoints(points: [PointData]) -> PointDataSourceBuilder
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-maps#sdk-for-ios-explore-s-7heresdk9PointDataC">PointData</a>

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
  <td><code> </code><em><code>points</code></em><code> </code></td>
  <td><div>
  <p>Points to be added.</p>
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

   <span id="sdk-for-ios-explore-s-7heresdk22PointDataSourceBuilderC5buildAA0bcD0CyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-build" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-pointdatasourcebuilder#sdk-for-ios-explore-s-7heresdk22PointDataSourceBuilderC5buildAA0bcD0CyF" class="token"><code>build()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Builds a PointDataSource instance and resets the builder instance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func build() -> PointDataSource
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-pointdatasource">PointDataSource</a>

  </div>

  <div>

  #### Return Value

  Instance of the data source created with given points and attributes.

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

