---
title: "Options Structure Reference"
slug: "sdk-for-ios-explore-classes-polylinesimplifier-options"
---

# Options

<div class="declaration">

<div class="language">

``` highlight
public struct Options
```

</div>

</div>

Controls the strategy of <a href="sdk-for-ios-explore-classes-polylinesimplifier#sdk-for-ios-explore-s-7heresdk18PolylineSimplifierC8simplify8polyline24simplificationParameters10completionAA10TaskHandle_pSayAA14GeoCoordinatesVG_AC7OptionsVyAA0B19SimplificationErrorOSg_AKSgtctF">`PolylineSimplifier.simplify(...)`</a> when reducing a size of polyline.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18PolylineSimplifierC7OptionsV33simplificationInMeters14ZoomLevels6UInt64VvpZ"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Variable-simplificationInMeters14ZoomLevel" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-polylinesimplifier-options#sdk-for-ios-explore-s-7heresdk18PolylineSimplifierC7OptionsV33simplificationInMeters14ZoomLevels6UInt64VvpZ" class="token"><code>simplificationInMeters14ZoomLevel</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Value for simplification tolerance for 14 zoom level without significant artifacts.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let simplificationInMeters14ZoomLevel: UInt64
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18PolylineSimplifierC7OptionsV9maxPointss6UInt64Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-maxPoints" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-polylinesimplifier-options#sdk-for-ios-explore-s-7heresdk18PolylineSimplifierC7OptionsV9maxPointss6UInt64Vvp" class="token"><code>maxPoints</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the upper limit on the resulting collection for the <a href="sdk-for-ios-explore-classes-polylinesimplifier#sdk-for-ios-explore-s-7heresdk18PolylineSimplifierC8simplify8polyline24simplificationParameters10completionAA10TaskHandle_pSayAA14GeoCoordinatesVG_AC7OptionsVyAA0B19SimplificationErrorOSg_AKSgtctF">`PolylineSimplifier.simplify(...)`</a>. Lower value results in the lower accuracy of the resulting polyline. If `maxPoints` is less than `2` then resulting polyline will not have an upper limit on the size and only <a href="sdk-for-ios-explore-classes-polylinesimplifier-options#sdk-for-ios-explore-s-7heresdk18PolylineSimplifierC7OptionsV31simplificationToleranceInMeterss6UInt64Vvp">`PolylineSimplifier.Options.simplificationToleranceInMeters`</a> will be considered. When `maxPoints` is greater than size of the passed polyline then simplification algorithm will take into account only <a href="sdk-for-ios-explore-classes-polylinesimplifier-options#sdk-for-ios-explore-s-7heresdk18PolylineSimplifierC7OptionsV31simplificationToleranceInMeterss6UInt64Vvp">`PolylineSimplifier.Options.simplificationToleranceInMeters`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maxPoints: UInt64
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18PolylineSimplifierC7OptionsV31simplificationToleranceInMeterss6UInt64Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-simplificationToleranceInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-polylinesimplifier-options#sdk-for-ios-explore-s-7heresdk18PolylineSimplifierC7OptionsV31simplificationToleranceInMeterss6UInt64Vvp" class="token"><code>simplificationToleranceInMeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the accuracy limit for the <a href="sdk-for-ios-explore-classes-polylinesimplifier#sdk-for-ios-explore-s-7heresdk18PolylineSimplifierC8simplify8polyline24simplificationParameters10completionAA10TaskHandle_pSayAA14GeoCoordinatesVG_AC7OptionsVyAA0B19SimplificationErrorOSg_AKSgtctF">`PolylineSimplifier.simplify(...)`</a>:

  - higher tolerance results in more simplification (fewer points);
  - lower tolerance keeps the line closer to its original shape.

  If removing a point produces polyline, which deviates from the original one more than `simplificationToleranceInMeters`, then this point is left in the collection.

  If specified tolerance will not allow to create a polyline conforming to <a href="sdk-for-ios-explore-classes-polylinesimplifier-options#sdk-for-ios-explore-s-7heresdk18PolylineSimplifierC7OptionsV9maxPointss6UInt64Vvp">`PolylineSimplifier.Options.maxPoints`</a>, then `simplificationToleranceInMeters` is ignored.

  Default value is equal to <a href="sdk-for-ios-explore-classes-polylinesimplifier-options#sdk-for-ios-explore-s-7heresdk18PolylineSimplifierC7OptionsV33simplificationInMeters14ZoomLevels6UInt64VvpZ">`PolylineSimplifier.Options.simplificationInMeters14ZoomLevel`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var simplificationToleranceInMeters: UInt64
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18PolylineSimplifierC7OptionsV9maxPoints31simplificationToleranceInMetersAEs6UInt64V_AItcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-maxPoints-simplificationToleranceInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-polylinesimplifier-options#sdk-for-ios-explore-s-7heresdk18PolylineSimplifierC7OptionsV9maxPoints31simplificationToleranceInMetersAEs6UInt64V_AItcfc" class="token"><code>init(maxPoints:</code><wbr></wbr><code>simplificationToleranceInMeters:</code><wbr></wbr><code>)</code></a> 

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
  public init(maxPoints: UInt64 = 0, simplificationToleranceInMeters: UInt64 = PolylineSimplifier.Options.simplificationInMeters14ZoomLevel)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-polylinesimplifier">PolylineSimplifier</a>
  - <a href="sdk-for-ios-explore-classes-polylinesimplifier-options#sdk-for-ios-explore-s-7heresdk18PolylineSimplifierC7OptionsV33simplificationInMeters14ZoomLevels6UInt64VvpZ">simplificationInMeters14ZoomLevel</a>

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

