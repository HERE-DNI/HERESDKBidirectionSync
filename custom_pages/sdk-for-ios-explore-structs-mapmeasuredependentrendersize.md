---
title: "MapMeasureDependentRenderSize Structure Reference"
slug: "sdk-for-ios-explore-structs-mapmeasuredependentrendersize"
---

# MapMeasureDependentRenderSize

<div class="declaration">

<div class="language">

``` highlight
public struct MapMeasureDependentRenderSize : Hashable
```

</div>

</div>

Represents a render size, described as map measure dependent values.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk29MapMeasureDependentRenderSizeV11measureKindAA0bC0V0H0Ovp"></span>` `<span id="//apple_ref/swift/Property/measureKind" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize#/s:7heresdk29MapMeasureDependentRenderSizeV11measureKindAA0bC0V0H0Ovp" class="token"><code>measureKind</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The unit used for the key in <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize#/s:7heresdk29MapMeasureDependentRenderSizeV5sizesSDyS2dGvp">`MapMeasureDependentRenderSize.sizes`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public let measureKind: MapMeasure.Kind
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk29MapMeasureDependentRenderSizeV8sizeUnitAA0eF0V0H0Ovp"></span>` `<span id="//apple_ref/swift/Property/sizeUnit" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize#/s:7heresdk29MapMeasureDependentRenderSizeV8sizeUnitAA0eF0V0H0Ovp" class="token"><code>sizeUnit</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The unit used for the value in <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize#/s:7heresdk29MapMeasureDependentRenderSizeV5sizesSDyS2dGvp">`MapMeasureDependentRenderSize.sizes`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public let sizeUnit: RenderSize.Unit
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk29MapMeasureDependentRenderSizeV5sizesSDyS2dGvp"></span>` `<span id="//apple_ref/swift/Property/sizes" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize#/s:7heresdk29MapMeasureDependentRenderSizeV5sizesSDyS2dGvp" class="token"><code>sizes</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The dictionary describing the size (value) per map measure (key).

  Units of keys and values are defined in <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize#/s:7heresdk29MapMeasureDependentRenderSizeV11measureKindAA0bC0V0H0Ovp">`MapMeasureDependentRenderSize.measureKind`</a> and <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize#/s:7heresdk29MapMeasureDependentRenderSizeV8sizeUnitAA0eF0V0H0Ovp">`MapMeasureDependentRenderSize.sizeUnit`</a>.

  `sizes` with a single entry indicates using a fixed size value across all map measures.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public let sizes: [Double : Double]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(measureKind: sizeUnit: sizes: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs a `MapMeasureDependentRenderSize` from given parameters.

  Supplying <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize#/s:7heresdk29MapMeasureDependentRenderSizeV5sizesSDyS2dGvp">`sizes`</a> map with a single entry indicates using a fixed size value across all map measures.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize#/s:7heresdk29MapMeasureDependentRenderSizeV18InstantiationErrora">`MapMeasureDependentRenderSize.InstantiationError`</a> Instantiation error if <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize#/s:7heresdk29MapMeasureDependentRenderSizeV5sizesSDyS2dGvp">`sizes`</a> map is empty or contains negative keys or values.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( measureKind : MapMeasure . Kind , sizeUnit : RenderSize . Unit , sizes : [ Double : Double ]) throws
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
  <td><code> </code><em><code>measureKind</code></em><code> </code></td>
  <td><div>
  <p>The unit used for the key in <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize#/s:7heresdk29MapMeasureDependentRenderSizeV5sizesSDyS2dGvp"><code>sizes</code></a>.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>sizeUnit</code></em><code> </code></td>
  <td><div>
  <p>The unit used for the value in <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize#/s:7heresdk29MapMeasureDependentRenderSizeV5sizesSDyS2dGvp"><code>sizes</code></a>.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>sizes</code></em><code> </code></td>
  <td><div>
  <p>The dictionary describing the size (value) per map measure (key).</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      init(sizeUnit: size: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs a `MapMeasureDependentRenderSize` from single size value which is constant across all map measures.

  The given `size` value is stored in <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize#/s:7heresdk29MapMeasureDependentRenderSizeV5sizesSDyS2dGvp">`MapMeasureDependentRenderSize.sizes`</a> map at key 0 and <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize#/s:7heresdk29MapMeasureDependentRenderSizeV11measureKindAA0bC0V0H0Ovp">`MapMeasureDependentRenderSize.measureKind`</a> is set to <a href="sdk-for-ios-explore-structs-mapmeasure-kind#/s:7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">`MapMeasure.Kind.zoomLevel`</a>.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize#/s:7heresdk29MapMeasureDependentRenderSizeV18InstantiationErrora">`MapMeasureDependentRenderSize.InstantiationError`</a> Instantiation error if `size` is negative.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( sizeUnit : RenderSize . Unit , size : Double ) throws
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
  <td><code> </code><em><code>sizeUnit</code></em><code> </code></td>
  <td><div>
  <p>The unit used for the value in <code>size</code>.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>size</code></em><code> </code></td>
  <td><div>
  <p>The size independent of map measure. Must not be negative.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk29MapMeasureDependentRenderSizeV22InstantiationErrorCodeO"></span>` `<span id="//apple_ref/swift/Enum/InstantiationErrorCode" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize#/s:7heresdk29MapMeasureDependentRenderSizeV22InstantiationErrorCodeO" class="token"><code>InstantiationErrorCode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Describes a reason for failing to create a <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize">`MapMeasureDependentRenderSize`</a>.

  <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize-instantiationerrorcode" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum InstantiationErrorCode : UInt32, CaseIterable, Codable
  ```

  ``` highlight
  extension MapMeasureDependentRenderSize.InstantiationErrorCode : Error
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk29MapMeasureDependentRenderSizeV18InstantiationErrora"></span>` `<span id="//apple_ref/swift/Alias/InstantiationError" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize#/s:7heresdk29MapMeasureDependentRenderSizeV18InstantiationErrora" class="token"><code>InstantiationError</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Thrown when a problem occurs while trying to create `MapMeasureDependentRenderSize`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias InstantiationError = InstantiationErrorCode
  ```

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

