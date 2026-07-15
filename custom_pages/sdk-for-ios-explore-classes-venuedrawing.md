---
title: "VenueDrawing Class Reference"
slug: "sdk-for-ios-explore-classes-venuedrawing"
---

# VenueDrawing

<div class="declaration">

<div class="language">

``` highlight
public class VenueDrawing
```

``` highlight
extension VenueDrawing: NativeBase
```

``` highlight
extension VenueDrawing: Hashable
```

</div>

</div>

Represents a drawing inside the <a href="sdk-for-ios-explore-classes-venuemodel">`VenueModel`</a>. The drawing can be a separate building in a complex of buildings, or show a different view of a venue. For example, in an airport, one drawing can be used as an overview of all buildings in this venue, while other drawings contains details for each terminal in this airport.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk12VenueDrawingC13GeometryArraya"></span>` `<span id="//apple_ref/swift/Alias/GeometryArray" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-venuedrawing#/s:7heresdk12VenueDrawingC13GeometryArraya" class="token"><code>GeometryArray</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Undocumented

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias GeometryArray = [VenueGeometry]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12VenueDrawingC19StringToPropertyMapa"></span>` `<span id="//apple_ref/swift/Alias/StringToPropertyMap" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-venuedrawing#/s:7heresdk12VenueDrawingC19StringToPropertyMapa" class="token"><code>StringToPropertyMap</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Undocumented

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias StringToPropertyMap = [String : Property]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12VenueDrawingC10LevelArraya"></span>` `<span id="//apple_ref/swift/Alias/LevelArray" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-venuedrawing#/s:7heresdk12VenueDrawingC10LevelArraya" class="token"><code>LevelArray</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Undocumented

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias LevelArray = [VenueLevel]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12VenueDrawingC24StringToGeometryArrayMapa"></span>` `<span id="//apple_ref/swift/Alias/StringToGeometryArrayMap" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-venuedrawing#/s:7heresdk12VenueDrawingC24StringToGeometryArrayMapa" class="token"><code>StringToGeometryArrayMap</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Undocumented

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias StringToGeometryArrayMap = [String : VenueDrawing.GeometryArray]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12VenueDrawingC11DoubleArraya"></span>` `<span id="//apple_ref/swift/Alias/DoubleArray" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-venuedrawing#/s:7heresdk12VenueDrawingC11DoubleArraya" class="token"><code>DoubleArray</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Undocumented

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias DoubleArray = [Double]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12VenueDrawingC13TopologyArraya"></span>` `<span id="//apple_ref/swift/Alias/TopologyArray" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-venuedrawing#/s:7heresdk12VenueDrawingC13TopologyArraya" class="token"><code>TopologyArray</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Undocumented

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias TopologyArray = [VenueTopology]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12VenueDrawingC10identifierSSvp"></span>` `<span id="//apple_ref/swift/Property/identifier" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-venuedrawing#/s:7heresdk12VenueDrawingC10identifierSSvp" class="token"><code>identifier</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The `id` of the drawing. This describes the identifier for drawing.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var identifier: String { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12VenueDrawingC8isIsRootSbvp"></span>` `<span id="//apple_ref/swift/Property/isIsRoot" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-venuedrawing#/s:7heresdk12VenueDrawingC8isIsRootSbvp" class="token"><code>isIsRoot</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  `True` if this is the root drawing and `false` otherwise. This can be used to check if this is top level drawing in venue.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isIsRoot: Bool { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12VenueDrawingC10venueModelAA0bE0Cvp"></span>` `<span id="//apple_ref/swift/Property/venueModel" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-venuedrawing#/s:7heresdk12VenueDrawingC10venueModelAA0bE0Cvp" class="token"><code>venueModel</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The parent venue model. It can be used to get the <a href="sdk-for-ios-explore-classes-venuemodel">`VenueModel`</a> where this Drawing belong.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var venueModel: VenueModel { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12VenueDrawingC6levelsSayAA0B5LevelCGvp"></span>` `<span id="//apple_ref/swift/Property/levels" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-venuedrawing#/s:7heresdk12VenueDrawingC6levelsSayAA0B5LevelCGvp" class="token"><code>levels</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The array with Level objects. This describes for which all level this drawing belongs.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var levels: VenueDrawing.LevelArray { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12VenueDrawingC6centerAA14GeoCoordinatesVvp"></span>` `<span id="//apple_ref/swift/Property/center" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-venuedrawing#/s:7heresdk12VenueDrawingC6centerAA14GeoCoordinatesVvp" class="token"><code>center</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The Geographic coordinates of the center of the drawing. It can be used to get center coordinates of drawing.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var center: GeoCoordinates { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12VenueDrawingC11boundingBoxAA03GeoE0Vvp"></span>` `<span id="//apple_ref/swift/Property/boundingBox" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-venuedrawing#/s:7heresdk12VenueDrawingC11boundingBoxAA03GeoE0Vvp" class="token"><code>boundingBox</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The <a href="sdk-for-ios-explore-structs-geobox">`GeoBox`</a> of the bounding area of the drawing. This is used to check if at certain zoom level and inside view this GeoBox belongs, then need to render.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var boundingBox: GeoBox { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12VenueDrawingC10propertiesSDySSAA8PropertyCGvp"></span>` `<span id="//apple_ref/swift/Property/properties" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-venuedrawing#/s:7heresdk12VenueDrawingC10propertiesSDySSAA8PropertyCGvp" class="token"><code>properties</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The key-value pairs of properties. This can be used to get different properties like name belonging to Drawing.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var properties: VenueDrawing.StringToPropertyMap { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12VenueDrawingC16geometriesByNameSayAA0B8GeometryCGvp"></span>` `<span id="//apple_ref/swift/Property/geometriesByName" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-venuedrawing#/s:7heresdk12VenueDrawingC16geometriesByNameSayAA0B8GeometryCGvp" class="token"><code>geometriesByName</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The geometries ordered by the name. This can be used to search geometries by name.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var geometriesByName: VenueDrawing.GeometryArray { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12VenueDrawingC21geometriesByIconNamesSDySSSayAA0B8GeometryCGGvp"></span>` `<span id="//apple_ref/swift/Property/geometriesByIconNames" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-venuedrawing#/s:7heresdk12VenueDrawingC21geometriesByIconNamesSDySSSayAA0B8GeometryCGGvp" class="token"><code>geometriesByIconNames</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The map from the icon names to the geometries in the drawing. This can be used to search the geometries by icon names.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var geometriesByIconNames: VenueDrawing.StringToGeometryArrayMap { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk12VenueDrawingC10topologiesSayAA0B8TopologyCGvp"></span>` `<span id="//apple_ref/swift/Property/topologies" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-venuedrawing#/s:7heresdk12VenueDrawingC10topologiesSayAA0B8TopologyCGvp" class="token"><code>topologies</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of topologies of the drawing. This can be used to check for which all topologies are realted to Drawing.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var topologies: VenueDrawing.TopologyArray { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      getGeometryById(geometryId: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets a geometry by an id.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getGeometryById ( geometryId : String ) -> VenueGeometry ?
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
  <td><code> </code><em><code>geometryId</code></em><code> </code></td>
  <td><div>
  <p>The id of the geometry.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The geometry with the given id or `nil`.

  </div>

  </div>

  </div>

- <div>

      getGeometryByAddress(geometryAddress: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets a geometry by the <a href="sdk-for-ios-explore-classes-venuegeometry-internaladdress">`VenueGeometry.InternalAddress`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getGeometryByAddress ( geometryAddress : String ) -> VenueGeometry ?
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
  <td><code> </code><em><code>geometryAddress</code></em><code> </code></td>
  <td><div>
  <p>The internal address as a String.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The geometry with the given address or `nil`.

  </div>

  </div>

  </div>

- <div>

      filterGeometry(filter: filterType: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets filtered geometries in an ascending order.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func filterGeometry ( filter : String , filterType : VenueGeometryFilterType ) -> VenueDrawing . GeometryArray
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
  <td><code> </code><em><code>filter</code></em><code> </code></td>
  <td><div>
  <p>The filter string.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>filterType</code></em><code> </code></td>
  <td><div>
  <p>The filter type.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The list of the filtered geometries or an empty list.

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

