---
title: "PointDataSource Class Reference"
slug: "sdk-for-ios-explore-classes-pointdatasource"
---

# PointDataSource

<div class="declaration">

<div class="language">

``` highlight
public class PointDataSource
```

``` highlight
extension PointDataSource: NativeBase
```

``` highlight
extension PointDataSource: Hashable
```

</div>

</div>

Point data source allows the rendering engine access to the user provided geographical locations and their attributes.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15PointDataSourceC0bC9Processora"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Alias-PointDataProcessor" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-pointdatasource#sdk-for-ios-explore-s-7heresdk15PointDataSourceC0bC9Processora" class="token"><code>PointDataProcessor</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Called for each point, allowing inspection, removal or update of coordinates and attributes.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias PointDataProcessor = (_ pointAccessor: PointDataAccessor) -> Bool
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-pointdataaccessor">PointDataAccessor</a>

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
  <td><code> </code><em><code>pointAccessor</code></em><code> </code></td>
  <td><div>
  <p>the point data accessor.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  value indicating the result of the processing.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15PointDataSourceC3addyyAA0bC0CF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-add-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-pointdatasource#sdk-for-ios-explore-s-7heresdk15PointDataSourceC3addyyAA0bC0CF" class="token"><code>add(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds a new point to the data source. Altitude of the point coordinates is ignored.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func add(_ point: PointData)
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

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15PointDataSourceC3addyySayAA0bC0CGF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-add-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-pointdatasource#sdk-for-ios-explore-s-7heresdk15PointDataSourceC3addyySayAA0bC0CGF" class="token"><code>add(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds new points to the data source. Altitude of the points coordinates is ignored.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func add(_ points: [PointData])
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
  <p>Point positions.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15PointDataSourceC9removeAllyyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeAll" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-pointdatasource#sdk-for-ios-explore-s-7heresdk15PointDataSourceC9removeAllyyF" class="token"><code>removeAll()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes all points from the data source.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeAll()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15PointDataSourceC7forEachyySbAA0bC8AccessorCcF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-forEach-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-pointdatasource#sdk-for-ios-explore-s-7heresdk15PointDataSourceC7forEachyySbAA0bC8AccessorCcF" class="token"><code>forEach(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Iterates through all the points from the data source and passes them to the given processor, one by one. The processor can update the point data.

  The iteration stops after all points have been processed or the processor returns false from the process call.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func forEach(_ processor: @escaping PointDataSource.PointDataProcessor)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-pointdatasource#sdk-for-ios-explore-s-7heresdk15PointDataSourceC0bC9Processora">PointDataProcessor</a>

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
  <td><code> </code><em><code>processor</code></em><code> </code></td>
  <td><div>
  <p>Point data processor.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15PointDataSourceC8removeIfyySbAA0bC8AccessorCcF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeIf-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-pointdatasource#sdk-for-ios-explore-s-7heresdk15PointDataSourceC8removeIfyySbAA0bC8AccessorCcF" class="token"><code>removeIf(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Iterates through all the points from the data source and passes them to the given inspector, one by one. All points for which the inspector returns `true` get removed from the data source. The inspector cannot update the point data.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeIf(_ processor: @escaping PointDataSource.PointDataProcessor)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-pointdatasource#sdk-for-ios-explore-s-7heresdk15PointDataSourceC0bC9Processora">PointDataProcessor</a>

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
  <td><code> </code><em><code>processor</code></em><code> </code></td>
  <td><div>
  <p>Point data processor.</p>
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

