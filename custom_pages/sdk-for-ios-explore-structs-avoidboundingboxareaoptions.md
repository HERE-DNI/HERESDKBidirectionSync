---
title: "AvoidBoundingBoxAreaOptions Structure Reference"
slug: "sdk-for-ios-explore-structs-avoidboundingboxareaoptions"
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

   <span id="sdk-for-ios-explore-s-7heresdk27AvoidBoundingBoxAreaOptionsV05avoidcdE0AA03GeoD0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-avoidBoundingBoxArea" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-avoidboundingboxareaoptions#sdk-for-ios-explore-s-7heresdk27AvoidBoundingBoxAreaOptionsV05avoidcdE0AA03GeoD0Vvp" class="token"><code>avoidBoundingBoxArea</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Area of rectangular shape which routes must not cross. Strictly enforced. **Note:** Violations are reported as \[sdk.routing.SectionNoticeCode.VIOLATED_BLOCKED_ROAD\]. This avoidance option is not supported for <a href="sdk-for-ios-explore-structs-isolineoptions">`IsolineOptions`</a>. If it is defined for isoline calculation then an \[sdk.routing.RoutingError.INVALID_PARAMETER\] error is generated.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var avoidBoundingBoxArea: GeoBox
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geobox">GeoBox</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk27AvoidBoundingBoxAreaOptionsV08boundingD14ExceptionAreasSayAA03GeoD0VGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-boundingBoxExceptionAreas" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-avoidboundingboxareaoptions#sdk-for-ios-explore-s-7heresdk27AvoidBoundingBoxAreaOptionsV08boundingD14ExceptionAreasSayAA03GeoD0VGvp" class="token"><code>boundingBoxExceptionAreas</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-structs-geobox">GeoBox</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk27AvoidBoundingBoxAreaOptionsV21polygonExceptionAreasSayAA10GeoPolygonVGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-polygonExceptionAreas" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-avoidboundingboxareaoptions#sdk-for-ios-explore-s-7heresdk27AvoidBoundingBoxAreaOptionsV21polygonExceptionAreasSayAA10GeoPolygonVGvp" class="token"><code>polygonExceptionAreas</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-structs-geopolygon">GeoPolygon</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk27AvoidBoundingBoxAreaOptionsV22corridorExceptionAreasSayAA11GeoCorridorVGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-corridorExceptionAreas" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-avoidboundingboxareaoptions#sdk-for-ios-explore-s-7heresdk27AvoidBoundingBoxAreaOptionsV22corridorExceptionAreasSayAA11GeoCorridorVGvp" class="token"><code>corridorExceptionAreas</code></a> 

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

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocorridor">GeoCorridor</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk27AvoidBoundingBoxAreaOptionsV05avoidcdE008boundingD14ExceptionAreas07polygoniJ008corridoriJ0AcA03GeoD0V_SayAIGSayAA0M7PolygonVGSayAA0M8CorridorVGtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-avoidBoundingBoxArea-boundingBoxExceptionAreas-polygonExceptionAreas-corridorExceptionAreas" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-avoidboundingboxareaoptions#sdk-for-ios-explore-s-7heresdk27AvoidBoundingBoxAreaOptionsV05avoidcdE008boundingD14ExceptionAreas07polygoniJ008corridoriJ0AcA03GeoD0V_SayAIGSayAA0M7PolygonVGSayAA0M8CorridorVGtcfc" class="token"><code>init(avoidBoundingBoxArea:</code><wbr></wbr><code>boundingBoxExceptionAreas:</code><wbr></wbr><code>polygonExceptionAreas:</code><wbr></wbr><code>corridorExceptionAreas:</code><wbr></wbr><code>)</code></a> 

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
  public init(avoidBoundingBoxArea: GeoBox, boundingBoxExceptionAreas: [GeoBox] = [], polygonExceptionAreas: [GeoPolygon] = [], corridorExceptionAreas: [GeoCorridor] = [])
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geobox">GeoBox</a>
  - <a href="sdk-for-ios-explore-structs-geopolygon">GeoPolygon</a>
  - <a href="sdk-for-ios-explore-structs-geocorridor">GeoCorridor</a>

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

