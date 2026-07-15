---
title: "VenueGeometry Class Reference"
slug: "sdk-for-ios-navigate-classes-venuegeometry"
---

# VenueGeometry

<div class="declaration">

<div class="language">

``` highlight
public class VenueGeometry
```

``` highlight
extension VenueGeometry: NativeBase
```

``` highlight
extension VenueGeometry: Hashable
```

</div>

</div>

Represents a geometry inside the <a href="sdk-for-ios-navigate-classes-venuelevel">`VenueLevel`</a>. The geometry can be any object inside the level, like a room, a wall or a table. Also the geometry can represent virtual objects, like a team area in an open space.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk13VenueGeometryC19StringToPropertyMapa"></span>` `<span id="//apple_ref/swift/Alias/StringToPropertyMap" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-venuegeometry#/s:7heresdk13VenueGeometryC19StringToPropertyMapa" class="token"><code>StringToPropertyMap</code></a>` `

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

  ` `<span id="/s:7heresdk13VenueGeometryC10identifierSSvp"></span>` `<span id="//apple_ref/swift/Property/identifier" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-venuegeometry#/s:7heresdk13VenueGeometryC10identifierSSvp" class="token"><code>identifier</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The `id` of the geometry.

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

  ` `<span id="/s:7heresdk13VenueGeometryC5levelAA0B5LevelCvp"></span>` `<span id="//apple_ref/swift/Property/level" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-venuegeometry#/s:7heresdk13VenueGeometryC5levelAA0B5LevelCvp" class="token"><code>level</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The parent level of the geometry.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var level: VenueLevel { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13VenueGeometryC12geometryTypeAC0cE0Ovp"></span>` `<span id="//apple_ref/swift/Property/geometryType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-venuegeometry#/s:7heresdk13VenueGeometryC12geometryTypeAC0cE0Ovp" class="token"><code>geometryType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The type of the geometry.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var geometryType: VenueGeometry.GeometryType { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13VenueGeometryC6centerAA14GeoCoordinatesVvp"></span>` `<span id="//apple_ref/swift/Property/center" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-venuegeometry#/s:7heresdk13VenueGeometryC6centerAA14GeoCoordinatesVvp" class="token"><code>center</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The geographic coordinates of the center of the geometry.

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

  ` `<span id="/s:7heresdk13VenueGeometryC11boundingBoxAA03GeoE0Vvp"></span>` `<span id="//apple_ref/swift/Property/boundingBox" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-venuegeometry#/s:7heresdk13VenueGeometryC11boundingBoxAA03GeoE0Vvp" class="token"><code>boundingBox</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The <a href="sdk-for-ios-navigate-structs-geobox">`GeoBox`</a> of the bounding area of the geometry.

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

  ` `<span id="/s:7heresdk13VenueGeometryC10propertiesSDySSAA8PropertyCGvp"></span>` `<span id="//apple_ref/swift/Property/properties" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-venuegeometry#/s:7heresdk13VenueGeometryC10propertiesSDySSAA8PropertyCGvp" class="token"><code>properties</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The properties of the geometry.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var properties: VenueGeometry.StringToPropertyMap { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13VenueGeometryC15internalAddressAC08InternalE0CSgvp"></span>` `<span id="//apple_ref/swift/Property/internalAddress" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-venuegeometry#/s:7heresdk13VenueGeometryC15internalAddressAC08InternalE0CSgvp" class="token"><code>internalAddress</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The internal address of the geometry.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var internalAddress: VenueGeometry.InternalAddress? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13VenueGeometryC4nameSSvp"></span>` `<span id="//apple_ref/swift/Property/name" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-venuegeometry#/s:7heresdk13VenueGeometryC4nameSSvp" class="token"><code>name</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The name of the geometry. If no name has been set, returns a label name.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var name: String { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13VenueGeometryC9labelNameSSvp"></span>` `<span id="//apple_ref/swift/Property/labelName" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-venuegeometry#/s:7heresdk13VenueGeometryC9labelNameSSvp" class="token"><code>labelName</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The label name of the geometry.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var labelName: String { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13VenueGeometryC10lookupTypeAC06LookupE0Ovp"></span>` `<span id="//apple_ref/swift/Property/lookupType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-venuegeometry#/s:7heresdk13VenueGeometryC10lookupTypeAC06LookupE0Ovp" class="token"><code>lookupType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The lookup type of the geometry.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var lookupType: VenueGeometry.LookupType { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13VenueGeometryC06parentC0ACvp"></span>` `<span id="//apple_ref/swift/Property/parentGeometry" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-venuegeometry#/s:7heresdk13VenueGeometryC06parentC0ACvp" class="token"><code>parentGeometry</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The parent geometry. Defaults to `nil`, if the geometry represents a base shape.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var parentGeometry: VenueGeometry { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13VenueGeometryC5styleAA0bC5StyleCSgvp"></span>` `<span id="//apple_ref/swift/Property/style" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-venuegeometry#/s:7heresdk13VenueGeometryC5styleAA0bC5StyleCSgvp" class="token"><code>style</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The style of the geometry.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var style: VenueGeometryStyle? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13VenueGeometryC10labelStyleAA0b5LabelE0CSgvp"></span>` `<span id="//apple_ref/swift/Property/labelStyle" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-venuegeometry#/s:7heresdk13VenueGeometryC10labelStyleAA0b5LabelE0CSgvp" class="token"><code>labelStyle</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The label style of the geometry.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var labelStyle: VenueLabelStyle? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13VenueGeometryC7levelIDSSvp"></span>` `<span id="//apple_ref/swift/Property/levelID" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-venuegeometry#/s:7heresdk13VenueGeometryC7levelIDSSvp" class="token"><code>levelID</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The level ID of geometry.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var levelID: String { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13VenueGeometryC15InternalAddressC"></span>` `<span id="//apple_ref/swift/Class/InternalAddress" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-venuegeometry#/s:7heresdk13VenueGeometryC15InternalAddressC" class="token"><code>InternalAddress</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents an internal addresses of the geometry inside the venue. The internal address can be a number of a seat in a stadium, or a name of a classroom in a university. One internal address can be shared between few geometries. For example, if a store in a shopping mall is located on few floors, few different geometries will represent it. But each of them will have the same internal address.

  <a href="sdk-for-ios-navigate-classes-venuegeometry-internaladdress" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class InternalAddress
  ```

  ``` highlight
  extension VenueGeometry.InternalAddress: NativeBase
  ```

  ``` highlight
  extension VenueGeometry.InternalAddress: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13VenueGeometryC0C4TypeO"></span>` `<span id="//apple_ref/swift/Enum/GeometryType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-venuegeometry#/s:7heresdk13VenueGeometryC0C4TypeO" class="token"><code>GeometryType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Geometry types.

  <a href="sdk-for-ios-navigate-classes-venuegeometry-geometrytype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum GeometryType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13VenueGeometryC10LookupTypeO"></span>` `<span id="//apple_ref/swift/Enum/LookupType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-venuegeometry#/s:7heresdk13VenueGeometryC10LookupTypeO" class="token"><code>LookupType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines how the geometry will be presented.

  <a href="sdk-for-ios-navigate-classes-venuegeometry-lookuptype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum LookupType : UInt32, CaseIterable, Codable
  ```

  </div>

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

