---
title: "DashImageRepresentation Class Reference"
slug: "sdk-for-ios-explore-classes-mappolyline-dashimagerepresentation"
---

# DashImageRepresentation

<div class="declaration">

<div class="language">

``` highlight
public class DashImageRepresentation : MapPolyline.Representation
```

</div>

</div>

Represents a dash pattern for the map polyline consisting of images rendered with certain gaps from each other.

This dash pattern representation consists only of images rendered at certain points along the polyline. For rendering them without any distortions, polyline gets sliced into series of straight segments that are multiple of sum of dash and gap lengths. For this reason, the new polyline geometry might not align fully with original geometry.

The <a href="sdk-for-ios-explore-classes-mappolyline-dashimagerepresentation#/s:7heresdk11MapPolylineC23DashImageRepresentationC04dashE0AA0bE0Cvp">`MapPolyline.DashImageRepresentation.dashImage`</a> is stretched according to <a href="sdk-for-ios-explore-classes-mappolyline-dashimagerepresentation#/s:7heresdk11MapPolylineC23DashImageRepresentationC10dashLengthAA0B26MeasureDependentRenderSizeVvp">`MapPolyline.DashImageRepresentation.dashLength`</a> and <a href="sdk-for-ios-explore-classes-mappolyline-dashimagerepresentation#/s:7heresdk11MapPolylineC23DashImageRepresentationC9dashWidthAA0B26MeasureDependentRenderSizeVvp">`MapPolyline.DashImageRepresentation.dashWidth`</a>, with image’s width matched to `dashLength` and image’s height matched to `dashWidth`. The image is oriented so that its bottom is on the left-hand side between vertices `n` and `n+1`.

The spacing between images is specified by <a href="sdk-for-ios-explore-classes-mappolyline-dashimagerepresentation#/s:7heresdk11MapPolylineC23DashImageRepresentationC9gapLengthAA0B26MeasureDependentRenderSizeVvp">`MapPolyline.DashImageRepresentation.gapLength`</a>.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

      init(dashLength: dashWidth: image: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a uniform dash pattern in which the length of a gap is the same as the length of a dash. Dashes are rendered as image.

  This allows for patterns like `' — — — —'` or `' —— —— ——'`.

  For <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize">`MapMeasureDependentRenderSize`</a> supplied for <a href="sdk-for-ios-explore-classes-mappolyline-dashimagerepresentation#/s:7heresdk11MapPolylineC23DashImageRepresentationC10dashLengthAA0B26MeasureDependentRenderSizeVvp">`dashLength`</a> and <a href="sdk-for-ios-explore-classes-mappolyline-dashimagerepresentation#/s:7heresdk11MapPolylineC23DashImageRepresentationC9dashWidthAA0B26MeasureDependentRenderSizeVvp">`dashWidth`</a>, only <a href="sdk-for-ios-explore-structs-mapmeasure-kind#/s:7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">`MapMeasure.Kind.zoomLevel`</a> is supported for <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize#/s:7heresdk29MapMeasureDependentRenderSizeV11measureKindAA0bC0V0H0Ovp">`MapMeasureDependentRenderSize.measureKind`</a> and only <a href="sdk-for-ios-explore-structs-rendersize-unit#/s:7heresdk10RenderSizeV4UnitO6metersyA2EmF">`RenderSize.Unit.meters`</a> is supported for <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize#/s:7heresdk29MapMeasureDependentRenderSizeV8sizeUnitAA0eF0V0H0Ovp">`MapMeasureDependentRenderSize.sizeUnit`</a>.

  Only map measure values in range \[3-19\] are supported.

  The value of the keys in <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize#/s:7heresdk29MapMeasureDependentRenderSizeV5sizesSDyS2dGvp">`MapMeasureDependentRenderSize.sizes`</a> is truncated to integer values, hence only a single value can be provided per zoom level.

  The values are interpolated linearly between zoom levels.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-explore-classes-mappolyline-representation#/s:7heresdk11MapPolylineC14RepresentationC18InstantiationErrora">`MapPolyline.Representation.InstantiationError`</a> In case of invalid input parameters.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( dashLength : MapMeasureDependentRenderSize , dashWidth : MapMeasureDependentRenderSize , image : MapImage ) throws
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
  <td><code> </code><em><code>dashLength</code></em><code> </code></td>
  <td><div>
  <p>The map measure dependent length of a dash, to which image width is stretched.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>dashWidth</code></em><code> </code></td>
  <td><div>
  <p>The map measure dependent width of a dash, to which image height is stretched.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>image</code></em><code> </code></td>
  <td><div>
  <p>Image to be rendered in place of dash space. It is stretched to match <a href="sdk-for-ios-explore-classes-mappolyline-dashimagerepresentation#/s:7heresdk11MapPolylineC23DashImageRepresentationC9dashWidthAA0B26MeasureDependentRenderSizeVvp"><code>dashWidth</code></a> and <a href="sdk-for-ios-explore-classes-mappolyline-dashimagerepresentation#/s:7heresdk11MapPolylineC23DashImageRepresentationC10dashLengthAA0B26MeasureDependentRenderSizeVvp"><code>dashLength</code></a>.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      init(dashLength: gapLength: dashWidth: image: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a simple dash pattern in which the lengths of a dash and gap can be different. Dashes are rendered as image.

  This allows for patterns like `' — — — —'` or `' ——— ——— ———'`.

  For <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize">`MapMeasureDependentRenderSize`</a> supplied for <a href="sdk-for-ios-explore-classes-mappolyline-dashimagerepresentation#/s:7heresdk11MapPolylineC23DashImageRepresentationC10dashLengthAA0B26MeasureDependentRenderSizeVvp">`dashLength`</a>, <a href="sdk-for-ios-explore-classes-mappolyline-dashimagerepresentation#/s:7heresdk11MapPolylineC23DashImageRepresentationC9gapLengthAA0B26MeasureDependentRenderSizeVvp">`gapLength`</a> and <a href="sdk-for-ios-explore-classes-mappolyline-dashimagerepresentation#/s:7heresdk11MapPolylineC23DashImageRepresentationC9dashWidthAA0B26MeasureDependentRenderSizeVvp">`dashWidth`</a>, only <a href="sdk-for-ios-explore-structs-mapmeasure-kind#/s:7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">`MapMeasure.Kind.zoomLevel`</a> is supported for <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize#/s:7heresdk29MapMeasureDependentRenderSizeV11measureKindAA0bC0V0H0Ovp">`MapMeasureDependentRenderSize.measureKind`</a> and only <a href="sdk-for-ios-explore-structs-rendersize-unit#/s:7heresdk10RenderSizeV4UnitO6metersyA2EmF">`RenderSize.Unit.meters`</a> is supported for <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize#/s:7heresdk29MapMeasureDependentRenderSizeV8sizeUnitAA0eF0V0H0Ovp">`MapMeasureDependentRenderSize.sizeUnit`</a>.

  Only map measure values in range \[3-19\] are supported.

  The value of the keys in <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize#/s:7heresdk29MapMeasureDependentRenderSizeV5sizesSDyS2dGvp">`MapMeasureDependentRenderSize.sizes`</a> is truncated to integer values, hence only a single value can be provided per zoom level.

  The values are interpolated linearly between zoom levels.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-explore-classes-mappolyline-representation#/s:7heresdk11MapPolylineC14RepresentationC18InstantiationErrora">`MapPolyline.Representation.InstantiationError`</a> In case of invalid input parameters.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( dashLength : MapMeasureDependentRenderSize , gapLength : MapMeasureDependentRenderSize , dashWidth : MapMeasureDependentRenderSize , image : MapImage ) throws
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
  <td><code> </code><em><code>dashLength</code></em><code> </code></td>
  <td><div>
  <p>The map measure dependent length of a dash, to which image width is stretched.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>gapLength</code></em><code> </code></td>
  <td><div>
  <p>The map measure dependent length of a gap between dash images.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>dashWidth</code></em><code> </code></td>
  <td><div>
  <p>The map measure dependent width of a dash, to which image height is stretched.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>image</code></em><code> </code></td>
  <td><div>
  <p>Image to be rendered in place of dash space. It is stretched to match <a href="sdk-for-ios-explore-classes-mappolyline-dashimagerepresentation#/s:7heresdk11MapPolylineC23DashImageRepresentationC9dashWidthAA0B26MeasureDependentRenderSizeVvp"><code>dashWidth</code></a> and <a href="sdk-for-ios-explore-classes-mappolyline-dashimagerepresentation#/s:7heresdk11MapPolylineC23DashImageRepresentationC10dashLengthAA0B26MeasureDependentRenderSizeVvp"><code>dashLength</code></a>.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11MapPolylineC23DashImageRepresentationC04dashE0AA0bE0Cvp"></span>` `<span id="//apple_ref/swift/Property/dashImage" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mappolyline-dashimagerepresentation#/s:7heresdk11MapPolylineC23DashImageRepresentationC04dashE0AA0bE0Cvp" class="token"><code>dashImage</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Image to be rendered in place of dash space. It is stretched to fill whole polyline width and length of each dash.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var dashImage: MapImage { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11MapPolylineC23DashImageRepresentationC10dashLengthAA0B26MeasureDependentRenderSizeVvp"></span>` `<span id="//apple_ref/swift/Property/dashLength" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mappolyline-dashimagerepresentation#/s:7heresdk11MapPolylineC23DashImageRepresentationC10dashLengthAA0B26MeasureDependentRenderSizeVvp" class="token"><code>dashLength</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The map measure dependent length of a dash, to which image width is stretched.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var dashLength: MapMeasureDependentRenderSize { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11MapPolylineC23DashImageRepresentationC9gapLengthAA0B26MeasureDependentRenderSizeVvp"></span>` `<span id="//apple_ref/swift/Property/gapLength" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mappolyline-dashimagerepresentation#/s:7heresdk11MapPolylineC23DashImageRepresentationC9gapLengthAA0B26MeasureDependentRenderSizeVvp" class="token"><code>gapLength</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The map measure dependent length of a gap between dash images.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var gapLength: MapMeasureDependentRenderSize { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11MapPolylineC23DashImageRepresentationC9dashWidthAA0B26MeasureDependentRenderSizeVvp"></span>` `<span id="//apple_ref/swift/Property/dashWidth" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-mappolyline-dashimagerepresentation#/s:7heresdk11MapPolylineC23DashImageRepresentationC9dashWidthAA0B26MeasureDependentRenderSizeVvp" class="token"><code>dashWidth</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The map measure dependent width of a dash, to which image height is stretched.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var dashWidth: MapMeasureDependentRenderSize { get }
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

