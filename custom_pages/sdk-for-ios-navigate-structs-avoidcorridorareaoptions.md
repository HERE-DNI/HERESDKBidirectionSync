---
title: "AvoidCorridorAreaOptions Structure Reference"
slug: "sdk-for-ios-navigate-structs-avoidcorridorareaoptions"
---

# AvoidCorridorAreaOptions

<div class="declaration">

<div class="language">

``` highlight
public struct AvoidCorridorAreaOptions : Hashable
```

</div>

</div>

Area of corridor shape which routes must not cross and exceptions for this area.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24AvoidCorridorAreaOptionsV05avoidcD0AA03GeoC0Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-avoidCorridorArea" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-avoidcorridorareaoptions#sdk-for-ios-navigate-s-7heresdk24AvoidCorridorAreaOptionsV05avoidcD0AA03GeoC0Vvp" class="token"><code>avoidCorridorArea</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Area of corridor shape which routes must not cross. Strictly enforced. Violations are reported as <a href="sdk-for-ios-navigate-enums-sectionnoticecode#sdk-for-ios-navigate-s-7heresdk17SectionNoticeCodeO19violatedBlockedRoadyA2CmF">`SectionNoticeCode.violatedBlockedRoad`</a>. **Note:** This avoidance option is not supported for <a href="sdk-for-ios-navigate-structs-isolineoptions">`IsolineOptions`</a>. If it is defined for isoline calculation then an \[sdk.routing.RoutingError.INVALID_PARAMETER\] error is generated. Even though `GeoCorridor.half_width_in_meters` is an optional property in case of exception areas it is mandatory. Otherwise route calculation will fail with an \[sdk.routing.RoutingError.INVALID_PARAMETER\] error.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var avoidCorridorArea: GeoCorridor
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geocorridor">GeoCorridor</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24AvoidCorridorAreaOptionsV25boundingBoxExceptionAreasSayAA03GeoG0VGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-boundingBoxExceptionAreas" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-avoidcorridorareaoptions#sdk-for-ios-navigate-s-7heresdk24AvoidCorridorAreaOptionsV25boundingBoxExceptionAreasSayAA03GeoG0VGvp" class="token"><code>boundingBoxExceptionAreas</code></a> 

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

  - <a href="sdk-for-ios-navigate-structs-geobox">GeoBox</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24AvoidCorridorAreaOptionsV21polygonExceptionAreasSayAA10GeoPolygonVGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-polygonExceptionAreas" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-avoidcorridorareaoptions#sdk-for-ios-navigate-s-7heresdk24AvoidCorridorAreaOptionsV21polygonExceptionAreasSayAA10GeoPolygonVGvp" class="token"><code>polygonExceptionAreas</code></a> 

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

  - <a href="sdk-for-ios-navigate-structs-geopolygon">GeoPolygon</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24AvoidCorridorAreaOptionsV22corridorExceptionAreasSayAA03GeoC0VGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-corridorExceptionAreas" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-avoidcorridorareaoptions#sdk-for-ios-navigate-s-7heresdk24AvoidCorridorAreaOptionsV22corridorExceptionAreasSayAA03GeoC0VGvp" class="token"><code>corridorExceptionAreas</code></a> 

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

  - <a href="sdk-for-ios-navigate-structs-geocorridor">GeoCorridor</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24AvoidCorridorAreaOptionsV05avoidcD025boundingBoxExceptionAreas07polygoniJ008corridoriJ0AcA03GeoC0V_SayAA0mH0VGSayAA0M7PolygonVGSayAIGtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-avoidCorridorArea-boundingBoxExceptionAreas-polygonExceptionAreas-corridorExceptionAreas" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-avoidcorridorareaoptions#sdk-for-ios-navigate-s-7heresdk24AvoidCorridorAreaOptionsV05avoidcD025boundingBoxExceptionAreas07polygoniJ008corridoriJ0AcA03GeoC0V_SayAA0mH0VGSayAA0M7PolygonVGSayAIGtcfc" class="token"><code>init(avoidCorridorArea:</code><wbr></wbr><code>boundingBoxExceptionAreas:</code><wbr></wbr><code>polygonExceptionAreas:</code><wbr></wbr><code>corridorExceptionAreas:</code><wbr></wbr><code>)</code></a> 

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
  public init(avoidCorridorArea: GeoCorridor, boundingBoxExceptionAreas: [GeoBox] = [], polygonExceptionAreas: [GeoPolygon] = [], corridorExceptionAreas: [GeoCorridor] = [])
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geocorridor">GeoCorridor</a>
  - <a href="sdk-for-ios-navigate-structs-geobox">GeoBox</a>
  - <a href="sdk-for-ios-navigate-structs-geopolygon">GeoPolygon</a>

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

