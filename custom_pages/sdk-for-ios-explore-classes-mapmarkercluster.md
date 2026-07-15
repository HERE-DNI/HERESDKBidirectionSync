---
title: "MapMarkerCluster Class Reference"
slug: "sdk-for-ios-explore-classes-mapmarkercluster"
---

# MapMarkerCluster

<div class="declaration">

<div class="language">

``` highlight
public class MapMarkerCluster
```

``` highlight
extension MapMarkerCluster: NativeBase
```

``` highlight
extension MapMarkerCluster: Hashable
```

</div>

</div>

Groups map markers and enables their clustering to reduce visual clutter when there are many of them in a small area.

The markers that are close to each other are replaced by a single cluster marker. Cluster groups are generated based on geographical distance between objects, not based on screen space collision. Hence it is possible, that cluster markers can overlap.

The markers can be added to a cluster or to a scene, but not to both. To display the cluster on the map, add it to the scene using

    MapScene.addMapMarkerCluster(...)

. The display of a cluster is only guaranteed in case its origin is within the viewport. At the moment, this is a known limitation that mostly affects clusters which are visually large and cover a sizeable part of the viewport.
</p>

Markers part of the cluster with opacity set to zero are still on the map and are considered for picking and clustering.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

      init(imageStyle: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of a map marker cluster which is represented as an image.

  Any modification to object passed as `imageStyle` after creation of `MapMarkerCluster` does not have any effect.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( imageStyle : MapMarkerCluster . ImageStyle )
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
  <td><code> </code><em><code>imageStyle</code></em><code> </code></td>
  <td><div>
  <p>The visual representation for the cluster.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      init(imageStyle: counterStyle: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of a map marker cluster which is represented as an image along with a counter showing how many markers are actually grouped under particular cluster icon.

  Any modification to `imageStyle` or `counterStyle` after creation of `MapMarkerCluster` does not have any effect.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( imageStyle : MapMarkerCluster . ImageStyle , counterStyle : MapMarkerCluster . CounterStyle )
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
  <td><code> </code><em><code>imageStyle</code></em><code> </code></td>
  <td><div>
  <p>Describes the visual appearance of cluster icon.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>counterStyle</code></em><code> </code></td>
  <td><div>
  <p>Describes the appearance of marker count label.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16MapMarkerClusterC7markersSayAA0bC0CGvp"></span>` `<span id="//apple_ref/swift/Property/markers" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapmarkercluster#/s:7heresdk16MapMarkerClusterC7markersSayAA0bC0CGvp" class="token"><code>markers</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of map markers which currently belong to this cluster. Modifying the list has no effect on the marker cluster.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var markers: [MapMarker] { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16MapMarkerClusterC7opacitySdvp"></span>` `<span id="//apple_ref/swift/Property/opacity" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapmarkercluster#/s:7heresdk16MapMarkerClusterC7opacitySdvp" class="token"><code>opacity</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Opacity is the factor which is applied to the alpha channel of the image used for marker cluster. The value is clamped in range \[0.0, 1.0\]. Default value is 1.0 which means marker cluster is displayed with the default opacity of the image.

  Marker clusters with opacity value set to 0.0 are still on map and are considered for picking.

  Markers part of cluster will use their respective opacity when not displayed as a cluster icon.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var opacity: Double { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16MapMarkerClusterC8GroupingV"></span>` `<span id="//apple_ref/swift/Struct/Grouping" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapmarkercluster#/s:7heresdk16MapMarkerClusterC8GroupingV" class="token"><code>Grouping</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a group of map markers belonging to a cluster.

  It contains a list of map markers grouped on map view under single icon of marker cluster or single map marker entry for markers being part of cluster but spread enough not to be grouped.

  <a href="sdk-for-ios-explore-classes-mapmarkercluster-grouping" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct Grouping
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16MapMarkerClusterC10ImageStyleV"></span>` `<span id="//apple_ref/swift/Struct/ImageStyle" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapmarkercluster#/s:7heresdk16MapMarkerClusterC10ImageStyleV" class="token"><code>ImageStyle</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This class specifies the visual appearance of a cluster marker.

  <a href="sdk-for-ios-explore-classes-mapmarkercluster-imagestyle" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct ImageStyle
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16MapMarkerClusterC12CounterStyleV"></span>` `<span id="//apple_ref/swift/Struct/CounterStyle" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mapmarkercluster#/s:7heresdk16MapMarkerClusterC12CounterStyleV" class="token"><code>CounterStyle</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Styling options for a marker cluster which is represented by the marker count as a text.

  <a href="sdk-for-ios-explore-classes-mapmarkercluster-counterstyle" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct CounterStyle
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      addMapMarker(marker: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds a map marker to this cluster. Adding a marker which is already part of the cluster or which was already added to the map scene has no effect.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addMapMarker ( marker : MapMarker )
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
  <td><code> </code><em><code>marker</code></em><code> </code></td>
  <td><div>
  <p>The marker.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      addMapMarkers(markers: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds a list of map markers to this cluster.

  Markers which are already part of the cluster or which were already added to the map scene will be ignored.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addMapMarkers ( markers : [ MapMarker ])
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
  <td><code> </code><em><code>markers</code></em><code> </code></td>
  <td><div>
  <p>The list of markers.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      removeMapMarker(marker: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes a map marker from this cluster.

  Removing a marker which is not part of this cluster has no effect.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeMapMarker ( marker : MapMarker )
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
  <td><code> </code><em><code>marker</code></em><code> </code></td>
  <td><div>
  <p>The marker.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      removeMapMarkers(markers: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes a list of map markers from this cluster.

  Removing markers which are not part of this cluster has no effect.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeMapMarkers ( markers : [ MapMarker ])
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
  <td><code> </code><em><code>markers</code></em><code> </code></td>
  <td><div>
  <p>The list of markers.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      removeAllMapMarkers()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes all map markers from this cluster.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeAllMapMarkers ()
  ```

  </pre>

  </div>

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

