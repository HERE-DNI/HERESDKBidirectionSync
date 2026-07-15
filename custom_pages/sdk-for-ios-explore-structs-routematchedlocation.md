---
title: "RouteMatchedLocation Structure Reference"
slug: "sdk-for-ios-explore-structs-routematchedlocation"
---

# RouteMatchedLocation

<div class="declaration">

<div class="language">

``` highlight
public struct RouteMatchedLocation : Hashable
```

</div>

</div>

Represents a location matched to a specific position on a navigation route.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk20RouteMatchedLocationV12sectionIndexs5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/sectionIndex" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-routematchedlocation#/s:7heresdk20RouteMatchedLocationV12sectionIndexs5Int32Vvp" class="token"><code>sectionIndex</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Zero-based index of the route section containing this location.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var sectionIndex: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20RouteMatchedLocationV9spanIndexs5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/spanIndex" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-routematchedlocation#/s:7heresdk20RouteMatchedLocationV9spanIndexs5Int32Vvp" class="token"><code>spanIndex</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Zero-based index of the span within the current route section.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var spanIndex: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20RouteMatchedLocationV18spanOffsetInMetersSdvp"></span>` `<span id="//apple_ref/swift/Property/spanOffsetInMeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-routematchedlocation#/s:7heresdk20RouteMatchedLocationV18spanOffsetInMetersSdvp" class="token"><code>spanOffsetInMeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Distance in meters from the beginning of the current span to this location.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var spanOffsetInMeters: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20RouteMatchedLocationV23spanGeometryVertexIndexs5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/spanGeometryVertexIndex" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-routematchedlocation#/s:7heresdk20RouteMatchedLocationV23spanGeometryVertexIndexs5Int32Vvp" class="token"><code>spanGeometryVertexIndex</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Zero-based index of the geometry vertex that precedes this location.

  The span geometry is represented as a series of vertices. This index points to the vertex immediately before the matched location, allowing for interpolation between vertices if needed.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var spanGeometryVertexIndex: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(sectionIndex: spanIndex: spanOffsetInMeters: spanGeometryVertexIndex: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance.

  - Parameters

    - sectionIndex: Zero-based index of the route section containing this location.
    - spanIndex: Zero-based index of the span within the current route section.
    - spanOffsetInMeters: Distance in meters from the beginning of the current span to this location.
    - spanGeometryVertexIndex: Zero-based index of the geometry vertex that precedes this location.

    The span geometry is represented as a series of vertices. This index points to the vertex immediately before the matched location, allowing for interpolation between vertices if needed.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( sectionIndex : Int32 = 0 , spanIndex : Int32 = 0 , spanOffsetInMeters : Double = 0.0 , spanGeometryVertexIndex : Int32 = 0 )
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

