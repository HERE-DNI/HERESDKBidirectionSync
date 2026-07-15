---
title: "AvoidPolygonAreaOptions Structure Reference"
slug: "sdk-for-ios-navigate-structs-avoidpolygonareaoptions"
---

# AvoidPolygonAreaOptions

<div class="declaration">

<div class="language">

``` highlight
public struct AvoidPolygonAreaOptions : Hashable
```

</div>

</div>

The options to specify polygon shape which routes must not cross.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk23AvoidPolygonAreaOptionsV05avoidcD0AA03GeoC0Vvp"></span>` `<span id="//apple_ref/swift/Property/avoidPolygonArea" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-avoidpolygonareaoptions#/s:7heresdk23AvoidPolygonAreaOptionsV05avoidcD0AA03GeoC0Vvp" class="token"><code>avoidPolygonArea</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Area of polygon shape which routes must not cross. Strictly enforced. Violations are reported as <a href="sdk-for-ios-navigate-enums-sectionnoticecode#/s:7heresdk17SectionNoticeCodeO19violatedBlockedRoadyA2CmF">`SectionNoticeCode.violatedBlockedRoad`</a>. **Note:** This avoidance option is not supported for <a href="sdk-for-ios-navigate-structs-isolineoptions">`IsolineOptions`</a>. If it is defined for isoline calculation then an \[sdk.routing.RoutingError.INVALID_PARAMETER\] error is generated.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var avoidPolygonArea: GeoPolygon
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk23AvoidPolygonAreaOptionsV25boundingBoxExceptionAreasSayAA03GeoG0VGvp"></span>` `<span id="//apple_ref/swift/Property/boundingBoxExceptionAreas" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-avoidpolygonareaoptions#/s:7heresdk23AvoidPolygonAreaOptionsV25boundingBoxExceptionAreasSayAA03GeoG0VGvp" class="token"><code>boundingBoxExceptionAreas</code></a>` `

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

  ` `<span id="/s:7heresdk23AvoidPolygonAreaOptionsV21polygonExceptionAreasSayAA03GeoC0VGvp"></span>` `<span id="//apple_ref/swift/Property/polygonExceptionAreas" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-avoidpolygonareaoptions#/s:7heresdk23AvoidPolygonAreaOptionsV21polygonExceptionAreasSayAA03GeoC0VGvp" class="token"><code>polygonExceptionAreas</code></a>` `

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

  ` `<span id="/s:7heresdk23AvoidPolygonAreaOptionsV22corridorExceptionAreasSayAA11GeoCorridorVGvp"></span>` `<span id="//apple_ref/swift/Property/corridorExceptionAreas" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-avoidpolygonareaoptions#/s:7heresdk23AvoidPolygonAreaOptionsV22corridorExceptionAreasSayAA11GeoCorridorVGvp" class="token"><code>corridorExceptionAreas</code></a>` `

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

      init(avoidPolygonArea: boundingBoxExceptionAreas: polygonExceptionAreas: corridorExceptionAreas: )

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
  public init ( avoidPolygonArea : GeoPolygon , boundingBoxExceptionAreas : [ GeoBox ] = [], polygonExceptionAreas : [ GeoPolygon ] = [], corridorExceptionAreas : [ GeoCorridor ] = [])
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

