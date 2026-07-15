---
title: "PolygonDataSource Class Reference"
slug: "sdk-for-ios-explore-classes-polygondatasource"
---

# PolygonDataSource

<div class="declaration">

<div class="language">

``` highlight
public class PolygonDataSource
```

``` highlight
extension PolygonDataSource: NativeBase
```

``` highlight
extension PolygonDataSource: Hashable
```

</div>

</div>

Polygon data source allows the rendering engine access to the user provided polygons geometry and their attributes.

Polygon segments are rendered following the shortest path between their end points.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk17PolygonDataSourceC0bC9Processora"></span>` `<span id="//apple_ref/swift/Alias/PolygonDataProcessor" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-polygondatasource#/s:7heresdk17PolygonDataSourceC0bC9Processora" class="token"><code>PolygonDataProcessor</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Called for each polygon, allowing inspection, removal or update of coordinates and attributes.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias PolygonDataProcessor = ( _ polygonAccessor : PolygonDataAccessor ) -> Bool
  ```

  </pre>

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
  <td><code> </code><em><code>polygonAccessor</code></em><code> </code></td>
  <td><div>
  <p>the polygon data accessor.</p>
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

      add(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds a new polygon to the data source.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func add ( _ polygon : PolygonData )
  ```

  </pre>

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
  <td><code> </code><em><code>polygon</code></em><code> </code></td>
  <td><div>
  <p>Polygon to add.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      add(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds new polygons to the data source.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func add ( _ polygons : [ PolygonData ])
  ```

  </pre>

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
  <td><code> </code><em><code>polygons</code></em><code> </code></td>
  <td><div>
  <p>Polygons to add.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      removeAll()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes all polygons from the data source.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeAll ()
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      forEach(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Iterates through all the polygons from the data source and passes them to the given processor, one by one. The processor can update the polygon data.

  The iteration stops after all polygons have been processed or the processor returns false from the process call.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func forEach ( _ processor : @escaping PolygonDataSource . PolygonDataProcessor )
  ```

  </pre>

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
  <td><code> </code><em><code>processor</code></em><code> </code></td>
  <td><div>
  <p>Polygon processor.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      removeIf(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Iterates through all the polygons from the data source and passes them to the given inspector, one by one. All polygons for which the inspector returns `true` get removed from the data source. The inspector cannot update the polygon data.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeIf ( _ inspector : @escaping PolygonDataSource . PolygonDataProcessor )
  ```

  </pre>

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
  <td><code> </code><em><code>inspector</code></em><code> </code></td>
  <td><div>
  <p>Polygon data processor.</p>
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

