---
title: "LineDataSource Class Reference"
slug: "sdk-for-ios-navigate-classes-linedatasource"
---

# LineDataSource

<div class="declaration">

<div class="language">

``` highlight
public class LineDataSource
```

``` highlight
extension LineDataSource: NativeBase
```

``` highlight
extension LineDataSource: Hashable
```

</div>

</div>

Polyline data source allows the rendering engine access to the user provided polylines geometry and their attributes.

Polyline segments are rendered following the shortest path between their end vertices.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14LineDataSourceC0bC9Processora"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Alias-LineDataProcessor" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-linedatasource#sdk-for-ios-navigate-s-7heresdk14LineDataSourceC0bC9Processora" class="token"><code>LineDataProcessor</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Called for each line, allowing inspection, removal or update of coordinates and attributes.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias LineDataProcessor = (_ lineAccessor: LineDataAccessor) -> Bool
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-linedataaccessor">LineDataAccessor</a>

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
  <td><code> </code><em><code>lineAccessor</code></em><code> </code></td>
  <td><div>
  <p>the line data accessor.</p>
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

   <span id="sdk-for-ios-navigate-s-7heresdk14LineDataSourceC3addyyAA0bC0CF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-add-_" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-linedatasource#sdk-for-ios-navigate-s-7heresdk14LineDataSourceC3addyyAA0bC0CF" class="token"><code>add(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds a new line to the data source.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func add(_ line: LineData)
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
  <td><code> </code><em><code>line</code></em><code> </code></td>
  <td><div>
  <p>Line to add.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14LineDataSourceC3addyySayAA0bC0CGF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-add-_" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-linedatasource#sdk-for-ios-navigate-s-7heresdk14LineDataSourceC3addyySayAA0bC0CGF" class="token"><code>add(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds new lines to the data source.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func add(_ lines: [LineData])
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
  <td><code> </code><em><code>lines</code></em><code> </code></td>
  <td><div>
  <p>Lines to add.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14LineDataSourceC9removeAllyyF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-removeAll" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-linedatasource#sdk-for-ios-navigate-s-7heresdk14LineDataSourceC9removeAllyyF" class="token"><code>removeAll()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes all lines from the data source.

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

   <span id="sdk-for-ios-navigate-s-7heresdk14LineDataSourceC7forEachyySbAA0bC8AccessorCcF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-forEach-_" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-linedatasource#sdk-for-ios-navigate-s-7heresdk14LineDataSourceC7forEachyySbAA0bC8AccessorCcF" class="token"><code>forEach(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Iterates through all the lines from the data source and passes them to the given processor, one by one. The processor can update the line data. The iteration stops after all lines have been processed or the processor returns false from the process call.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func forEach(_ processor: @escaping LineDataSource.LineDataProcessor)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-linedatasource#sdk-for-ios-navigate-s-7heresdk14LineDataSourceC0bC9Processora">LineDataProcessor</a>

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
  <p>Line processor.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14LineDataSourceC8removeIfyySbAA0bC8AccessorCcF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-removeIf-_" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-linedatasource#sdk-for-ios-navigate-s-7heresdk14LineDataSourceC8removeIfyySbAA0bC8AccessorCcF" class="token"><code>removeIf(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Iterates through all the lines from the data source and passes them to the given inspector, one by one. All lines for which the inspector returns `true` get removed from the data source. The inspector cannot update the line data.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeIf(_ inspector: @escaping LineDataSource.LineDataProcessor)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-linedatasource#sdk-for-ios-navigate-s-7heresdk14LineDataSourceC0bC9Processora">LineDataProcessor</a>

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
  <td><code> </code><em><code>inspector</code></em><code> </code></td>
  <td><div>
  <p>Line data processor.</p>
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

