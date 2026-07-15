---
title: "RealisticViewWarning Structure Reference"
slug: "sdk-for-ios-explore-structs-realisticviewwarning"
---

# RealisticViewWarning

<div class="declaration">

<div class="language">

``` highlight
public struct RealisticViewWarning : Hashable
```

</div>

</div>

A realistic view notification. This notification is given for complex junctions and it includes a visual representation of that junction, in order to help the user to better navigate it. When <a href="sdk-for-ios-explore-structs-realisticviewwarning#/s:7heresdk20RealisticViewWarningV12distanceTypeAA08DistanceF0Ovp">`RealisticViewWarning.distanceType`</a> is <a href="sdk-for-ios-explore-enums-distancetype#/s:7heresdk12DistanceTypeO5aheadyA2CmF">`DistanceType.ahead`</a>, the <a href="sdk-for-ios-explore-structs-realisticviewwarning#/s:7heresdk20RealisticViewWarningV09realisticC11VectorImageAA0bcfG0VSgvp">`RealisticViewWarning.realisticViewVectorImage`</a> object will be provided with the junction view and the signpost representations. For <a href="sdk-for-ios-explore-structs-realisticviewwarning#/s:7heresdk20RealisticViewWarningV12distanceTypeAA08DistanceF0Ovp">`RealisticViewWarning.distanceType`</a> with value <a href="sdk-for-ios-explore-enums-distancetype#/s:7heresdk12DistanceTypeO6passedyA2CmF">`DistanceType.passed`</a>, the <a href="sdk-for-ios-explore-structs-realisticviewwarning#/s:7heresdk20RealisticViewWarningV09realisticC11VectorImageAA0bcfG0VSgvp">`RealisticViewWarning.realisticViewVectorImage`</a> object will be null. Use `RealisticViewWarningListener` to get notifications about the realistic views of the upcoming junctions.

Realistic view notifications require an online connection in order to function properly, or that the junction or signpost map layer data is cached, installed or preloaded as part of a <a href="sdk-for-ios-explore-structs-region">`Region`</a>. This can be enabled via feature configurations.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk20RealisticViewWarningV2ids5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/id" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-realisticviewwarning#/s:7heresdk20RealisticViewWarningV2ids5Int32Vvp" class="token"><code>id</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Unique identifier for this specific realistic view warning instance. Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace. Use this ID to track, update, or dismiss individual warning instances of this type.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var id: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20RealisticViewWarningV010distanceTobC8InMetersSdvp"></span>` `<span id="//apple_ref/swift/Property/distanceToRealisticViewInMeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-realisticviewwarning#/s:7heresdk20RealisticViewWarningV010distanceTobC8InMetersSdvp" class="token"><code>distanceToRealisticViewInMeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Distance to the junction, for which the realistic view is given, expressed in meters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var distanceToRealisticViewInMeters: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20RealisticViewWarningV09realisticC11VectorImageAA0bcfG0VSgvp"></span>` `<span id="//apple_ref/swift/Property/realisticViewVectorImage" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-realisticviewwarning#/s:7heresdk20RealisticViewWarningV09realisticC11VectorImageAA0bcfG0VSgvp" class="token"><code>realisticViewVectorImage</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The realistic view object for which the warning is given. Image resources are stored as vector graphics. Within `RealisticViewWarning`, only one type of image, either raster or vector, will be provided. If this property is not `nil`, then <a href="sdk-for-ios-explore-structs-realisticviewwarning#/s:7heresdk20RealisticViewWarningV09realisticC11RasterImageAA0bcfG0VSgvp">`RealisticViewWarning.realisticViewRasterImage`</a> will be `nil`.

  **Note:** The realistic views for most of the countries are stored as vector images.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var realisticViewVectorImage: RealisticViewVectorImage?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20RealisticViewWarningV09realisticC11RasterImageAA0bcfG0VSgvp"></span>` `<span id="//apple_ref/swift/Property/realisticViewRasterImage" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-realisticviewwarning#/s:7heresdk20RealisticViewWarningV09realisticC11RasterImageAA0bcfG0VSgvp" class="token"><code>realisticViewRasterImage</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The realistic view object for which the warning is given. Image resources are stored as raster graphics. Within `RealisticViewWarning`, only one type of image, either raster or vector, will be provided. If this property is not `nil`, then <a href="sdk-for-ios-explore-structs-realisticviewwarning#/s:7heresdk20RealisticViewWarningV09realisticC11VectorImageAA0bcfG0VSgvp">`RealisticViewWarning.realisticViewVectorImage`</a> will be `nil`. **Note:** Certain countries support only raster images as realistic views. Currently, this is the case only for Japan, but in the future, more countries might support this type of realistic views.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var realisticViewRasterImage: RealisticViewRasterImage?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20RealisticViewWarningV12distanceTypeAA08DistanceF0Ovp"></span>` `<span id="//apple_ref/swift/Property/distanceType" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-realisticviewwarning#/s:7heresdk20RealisticViewWarningV12distanceTypeAA08DistanceF0Ovp" class="token"><code>distanceType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The distance type for the warning, e.g. a warning for a new realistic view ahead or a warning for passing a realistic view. Since the realistic view warning is given relative to a single position on the route, <a href="sdk-for-ios-explore-enums-distancetype#/s:7heresdk12DistanceTypeO7reachedyA2CmF">`DistanceType.reached`</a> will never be given for this warning.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var distanceType: DistanceType
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(id: distanceToRealisticViewInMeters: realisticViewVectorImage: realisticViewRasterImage: distanceType: )

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

    - id: Unique identifier for this specific realistic view warning instance. Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace. Use this ID to track, update, or dismiss individual warning instances of this type.
    - distanceToRealisticViewInMeters: Distance to the junction, for which the realistic view is given, expressed in meters.
    - realisticViewVectorImage: The realistic view object for which the warning is given. Image resources are stored as vector graphics. Within `RealisticViewWarning`, only one type of image, either raster or vector, will be provided. If this property is not `nil`, then <a href="sdk-for-ios-explore-structs-realisticviewwarning#/s:7heresdk20RealisticViewWarningV09realisticC11RasterImageAA0bcfG0VSgvp">`RealisticViewWarning.realisticViewRasterImage`</a> will be `nil`.

    **Note:** The realistic views for most of the countries are stored as vector images.

    - realisticViewRasterImage: The realistic view object for which the warning is given. Image resources are stored as raster graphics. Within `RealisticViewWarning`, only one type of image, either raster or vector, will be provided. If this property is not `nil`, then <a href="sdk-for-ios-explore-structs-realisticviewwarning#/s:7heresdk20RealisticViewWarningV09realisticC11VectorImageAA0bcfG0VSgvp">`RealisticViewWarning.realisticViewVectorImage`</a> will be `nil`. **Note:** Certain countries support only raster images as realistic views. Currently, this is the case only for Japan, but in the future, more countries might support this type of realistic views.
    - distanceType: The distance type for the warning, e.g. a warning for a new realistic view ahead or a warning for passing a realistic view. Since the realistic view warning is given relative to a single position on the route, <a href="sdk-for-ios-explore-enums-distancetype#/s:7heresdk12DistanceTypeO7reachedyA2CmF">`DistanceType.reached`</a> will never be given for this warning.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( id : Int32 = 0 , distanceToRealisticViewInMeters : Double , realisticViewVectorImage : RealisticViewVectorImage ? = nil , realisticViewRasterImage : RealisticViewRasterImage ? = nil , distanceType : DistanceType )
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

