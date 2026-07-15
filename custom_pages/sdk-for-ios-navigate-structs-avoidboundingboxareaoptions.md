---
title: "AvoidBoundingBoxAreaOptions Structure Reference"
slug: "sdk-for-ios-navigate-structs-avoidboundingboxareaoptions"
---

# AvoidBoundingBoxAreaOptions

<div class="declaration">

<div class="language">

``` highlight
public struct AvoidBoundingBoxAreaOptions : Hashable
```

</div>

</div>

The options to specify rectangular shape which routes must not cross.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk27AvoidBoundingBoxAreaOptionsV05avoidcdE0AA03GeoD0Vvp"></span>` `<span id="//apple_ref/swift/Property/avoidBoundingBoxArea" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-avoidboundingboxareaoptions#/s:7heresdk27AvoidBoundingBoxAreaOptionsV05avoidcdE0AA03GeoD0Vvp" class="token"><code>avoidBoundingBoxArea</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Area of rectangular shape which routes must not cross. Strictly enforced. **Note:** Violations are reported as \[sdk.routing.SectionNoticeCode.VIOLATED_BLOCKED_ROAD\]. This avoidance option is not supported for <a href="sdk-for-ios-navigate-structs-isolineoptions">`IsolineOptions`</a>. If it is defined for isoline calculation then an \[sdk.routing.RoutingError.INVALID_PARAMETER\] error is generated.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var avoidBoundingBoxArea: GeoBox
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk27AvoidBoundingBoxAreaOptionsV08boundingD14ExceptionAreasSayAA03GeoD0VGvp"></span>` `<span id="//apple_ref/swift/Property/boundingBoxExceptionAreas" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-avoidboundingboxareaoptions#/s:7heresdk27AvoidBoundingBoxAreaOptionsV08boundingD14ExceptionAreasSayAA03GeoD0VGvp" class="token"><code>boundingBoxExceptionAreas</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Areas of rectangular shape to exclude from avoidance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var boundingBoxExceptionAreas: [GeoBox]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk27AvoidBoundingBoxAreaOptionsV21polygonExceptionAreasSayAA10GeoPolygonVGvp"></span>` `<span id="//apple_ref/swift/Property/polygonExceptionAreas" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-avoidboundingboxareaoptions#/s:7heresdk27AvoidBoundingBoxAreaOptionsV21polygonExceptionAreasSayAA10GeoPolygonVGvp" class="token"><code>polygonExceptionAreas</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Areas of polygon shape to exclude from avoidance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var polygonExceptionAreas: [GeoPolygon]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk27AvoidBoundingBoxAreaOptionsV22corridorExceptionAreasSayAA11GeoCorridorVGvp"></span>` `<span id="//apple_ref/swift/Property/corridorExceptionAreas" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-avoidboundingboxareaoptions#/s:7heresdk27AvoidBoundingBoxAreaOptionsV22corridorExceptionAreasSayAA11GeoCorridorVGvp" class="token"><code>corridorExceptionAreas</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Areas of corridor shape to exclude from avoidance. **Note:** Even though `GeoCorridor.half_width_in_meters` is an optional property in case of exception areas it is mandatory. Otherwise route calculation will fail with an \[sdk.routing.RoutingError.INVALID_PARAMETER\] error.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var corridorExceptionAreas: [GeoCorridor]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(avoidBoundingBoxArea: boundingBoxExceptionAreas: polygonExceptionAreas: corridorExceptionAreas: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( avoidBoundingBoxArea : GeoBox , boundingBoxExceptionAreas : [ GeoBox ] = [], polygonExceptionAreas : [ GeoPolygon ] = [], corridorExceptionAreas : [ GeoCorridor ] = [])
  ```

  </pre>

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

