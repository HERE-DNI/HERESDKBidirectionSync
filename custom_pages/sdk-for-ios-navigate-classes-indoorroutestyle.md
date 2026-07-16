---
title: "IndoorRouteStyle Class Reference"
slug: "sdk-for-ios-navigate-classes-indoorroutestyle"
---

# IndoorRouteStyle

<div class="declaration">

<div class="language">

``` highlight
public class IndoorRouteStyle
```

``` highlight
extension IndoorRouteStyle: NativeBase
```

``` highlight
extension IndoorRouteStyle: Hashable
```

</div>

</div>

Represents a style of the indoor route. Contains information about route colors and widths. Optionally, this style allows to set <a href="sdk-for-ios-navigate-classes-mapmarker">`MapMarker`</a> instances that can be used for specific route elements.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16IndoorRouteStyleCACycfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-indoorroutestyle#sdk-for-ios-navigate-s-7heresdk16IndoorRouteStyleCACycfc" class="token"><code>init()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of this class.

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

   <span id="sdk-for-ios-navigate-s-7heresdk16IndoorRouteStyleC19indoorPolylineWidthSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-indoorPolylineWidth" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-indoorroutestyle#sdk-for-ios-navigate-s-7heresdk16IndoorRouteStyleC19indoorPolylineWidthSdvp" class="token"><code>indoorPolylineWidth</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The width in pixels. Default value is 15 pixels The width in pixels of polylines for indoor route sections.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var indoorPolylineWidth: Double { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16IndoorRouteStyleC19indoorPolylineColorSo7UIColorCvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-indoorPolylineColor" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-indoorroutestyle#sdk-for-ios-navigate-s-7heresdk16IndoorRouteStyleC19indoorPolylineColorSo7UIColorCvp" class="token"><code>indoorPolylineColor</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The color value. The default color is #48DAD0. The color of polylines for indoor route sections.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var indoorPolylineColor: UIColor { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16IndoorRouteStyleC11startMarkerAA03MapF0CSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-startMarker" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-indoorroutestyle#sdk-for-ios-navigate-s-7heresdk16IndoorRouteStyleC11startMarkerAA03MapF0CSgvp" class="token"><code>startMarker</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A <a href="sdk-for-ios-navigate-classes-mapmarker">`MapMarker`</a> instance representing the start of the route. By default, no map marker is provided. The start map marker of the resulting route.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var startMarker: MapMarker? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapmarker">MapMarker</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16IndoorRouteStyleC17destinationMarkerAA03MapF0CSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-destinationMarker" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-indoorroutestyle#sdk-for-ios-navigate-s-7heresdk16IndoorRouteStyleC17destinationMarkerAA03MapF0CSgvp" class="token"><code>destinationMarker</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A <a href="sdk-for-ios-navigate-classes-mapmarker">`MapMarker`</a> instance representing the destination of the route. By default, no map marker is provided The destination map marker of the resulting route.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var destinationMarker: MapMarker? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapmarker">MapMarker</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16IndoorRouteStyleC10walkMarkerAA03MapF0CSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-walkMarker" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-indoorroutestyle#sdk-for-ios-navigate-s-7heresdk16IndoorRouteStyleC10walkMarkerAA03MapF0CSgvp" class="token"><code>walkMarker</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A <a href="sdk-for-ios-navigate-classes-mapmarker">`MapMarker`</a> instance representing the walk point of the route. By default, no map marker is provided. The walk map marker of the resulting route. It signals that a user should leave their transport vehicle and continue on foot.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var walkMarker: MapMarker? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapmarker">MapMarker</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16IndoorRouteStyleC11driveMarkerAA03MapF0CSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-driveMarker" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-indoorroutestyle#sdk-for-ios-navigate-s-7heresdk16IndoorRouteStyleC11driveMarkerAA03MapF0CSgvp" class="token"><code>driveMarker</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A <a href="sdk-for-ios-navigate-classes-mapmarker">`MapMarker`</a> instance representing the drive point of the route. By default, no map marker is provided. The drive map marker of the resulting route. It signals that a user should take a transport vehicle.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var driveMarker: MapMarker? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapmarker">MapMarker</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16IndoorRouteStyleC03getB9MarkerFor7feature6deltaZAA03MapF0CSgAA0B19LevelChangeFeaturesO_s5Int32VtF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getIndoorMarkerFor-feature-deltaZ" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-indoorroutestyle#sdk-for-ios-navigate-s-7heresdk16IndoorRouteStyleC03getB9MarkerFor7feature6deltaZAA03MapF0CSgAA0B19LevelChangeFeaturesO_s5Int32VtF" class="token"><code>getIndoorMarkerFor(feature:</code><wbr></wbr><code>deltaZ:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns a <a href="sdk-for-ios-navigate-classes-mapmarker">`MapMarker`</a> for a given indoor feature and the number of levels to change. By default, no map markers are provided.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getIndoorMarkerFor(feature: IndoorLevelChangeFeatures, deltaZ: Int32) -> MapMarker?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-indoorlevelchangefeatures">IndoorLevelChangeFeatures</a>
  - <a href="sdk-for-ios-navigate-classes-mapmarker">MapMarker</a>

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
  <td><code> </code><em><code>feature</code></em><code> </code></td>
  <td><div>
  <p>An indoor feature.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>deltaZ</code></em><code> </code></td>
  <td><div>
  <p>A number of levels to change, positive for up, negative for down. In the case of 0, the method returns an exit map marker.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The result <a href="sdk-for-ios-navigate-classes-mapmarker">`MapMarker`</a>, if it was set.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16IndoorRouteStyleC03setB10MarkersFor7feature8upMarker04downJ004exitJ0yAA0B19LevelChangeFeaturesO_AA03MapJ0CSgA2MtF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-setIndoorMarkersFor-feature-upMarker-downMarker-exitMarker" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-indoorroutestyle#sdk-for-ios-navigate-s-7heresdk16IndoorRouteStyleC03setB10MarkersFor7feature8upMarker04downJ004exitJ0yAA0B19LevelChangeFeaturesO_AA03MapJ0CSgA2MtF" class="token"><code>setIndoorMarkersFor(feature:</code><wbr></wbr><code>upMarker:</code><wbr></wbr><code>downMarker:</code><wbr></wbr><code>exitMarker:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets map markers for the given indoor feature.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setIndoorMarkersFor(feature: IndoorLevelChangeFeatures, upMarker: MapMarker?, downMarker: MapMarker?, exitMarker: MapMarker?)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-indoorlevelchangefeatures">IndoorLevelChangeFeatures</a>
  - <a href="sdk-for-ios-navigate-classes-mapmarker">MapMarker</a>

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
  <td><code> </code><em><code>feature</code></em><code> </code></td>
  <td><div>
  <p>An indoor feature.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>upMarker</code></em><code> </code></td>
  <td><div>
  <p>A <a href="sdk-for-ios-navigate-classes-mapmarker"><code>MapMarker</code></a> to go up.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>downMarker</code></em><code> </code></td>
  <td><div>
  <p>A <a href="sdk-for-ios-navigate-classes-mapmarker"><code>MapMarker</code></a> to go down.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>exitMarker</code></em><code> </code></td>
  <td><div>
  <p>A <a href="sdk-for-ios-navigate-classes-mapmarker"><code>MapMarker</code></a> to exit the indoor feature.</p>
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

