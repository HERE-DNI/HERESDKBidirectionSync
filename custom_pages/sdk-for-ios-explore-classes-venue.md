---
title: "Venue Class Reference"
slug: "sdk-for-ios-explore-classes-venue"
---

# Venue

<div class="declaration">

<div class="language">

``` highlight
public class Venue
```

``` highlight
extension Venue: NativeBase
```

``` highlight
extension Venue: Hashable
```

</div>

</div>

Controls the <a href="sdk-for-ios-explore-classes-venuemodel">`VenueModel`</a> inside the <a href="sdk-for-ios-explore-classes-venuemap">`VenueMap`</a> object. The venue controls the selection of the <a href="sdk-for-ios-explore-classes-venuedrawing">`VenueDrawing`</a> and the <a href="sdk-for-ios-explore-classes-venuelevel">`VenueLevel`</a> of the <a href="sdk-for-ios-explore-classes-venuemodel">`VenueModel`</a>. It provides the possibility to customize styles for the <a href="sdk-for-ios-explore-classes-venuegeometry">`VenueGeometry`</a>. Objects of this class can only be created using methods

    VenueMap.addVenueAsync(String, VenueLoadErrorHandler)

and

    VenueMap.selectVenueAsync(String, VenueLoadErrorHandler)

.
</p>

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk5VenueC10venueModelAA0bD0Cvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-venueModel" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venue#sdk-for-ios-explore-s-7heresdk5VenueC10venueModelAA0bD0Cvp" class="token"><code>venueModel</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The <a href="sdk-for-ios-explore-classes-venuemodel">`VenueModel`</a> controlled by this object. It can be used to get the <a href="sdk-for-ios-explore-classes-venuemodel">`VenueModel`</a> belonging to this object, like a building or a complex of buildings.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var venueModel: VenueModel { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-venuemodel">VenueModel</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk5VenueC10venueStyleAA0bD0Cvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-venueStyle" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venue#sdk-for-ios-explore-s-7heresdk5VenueC10venueStyleAA0bD0Cvp" class="token"><code>venueStyle</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The <a href="sdk-for-ios-explore-classes-venuestyle">`VenueStyle`</a> associated with the <a href="sdk-for-ios-explore-classes-venuemodel">`VenueModel`</a> controlled by this object. It can be used to get the style of the venue. Contains the information about the geometry and label styles available for the venue.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var venueStyle: VenueStyle { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-venuestyle">VenueStyle</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk5VenueC15selectedDrawingAA0bD0Cvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-selectedDrawing" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venue#sdk-for-ios-explore-s-7heresdk5VenueC15selectedDrawingAA0bD0Cvp" class="token"><code>selectedDrawing</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The selected drawing. Only the selected drawing will be visible as active on the map. All others will be hidden or displayed without details, depending on the implementation of the renderer.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var selectedDrawing: VenueDrawing { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-venuedrawing">VenueDrawing</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk5VenueC13selectedLevelAA0bD0Cvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-selectedLevel" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venue#sdk-for-ios-explore-s-7heresdk5VenueC13selectedLevelAA0bD0Cvp" class="token"><code>selectedLevel</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The selected level. Only the selected level will be visible as active on the map. All others will be hidden or displayed without details, depending on a renderer implementation. If the level doesn’t belong to the currently selected drawing, it can not be selected.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var selectedLevel: VenueLevel { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-venuelevel">VenueLevel</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk5VenueC19selectedLevelZIndexs5Int32Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-selectedLevelZIndex" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venue#sdk-for-ios-explore-s-7heresdk5VenueC19selectedLevelZIndexs5Int32Vvp" class="token"><code>selectedLevelZIndex</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The Z index value of the <a href="sdk-for-ios-explore-classes-venuelevel">`VenueLevel`</a> selected. Z index 0 represents the ground level, negative values represent underground levels, positive values - levels above the ground. Z index can also be taken from <a href="sdk-for-ios-explore-classes-venuelevel#sdk-for-ios-explore-s-7heresdk10VenueLevelC6zIndexs5Int32Vvp">`VenueLevel.zIndex`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var selectedLevelZIndex: Int32 { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk5VenueC18selectedLevelIndexs5Int32Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-selectedLevelIndex" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venue#sdk-for-ios-explore-s-7heresdk5VenueC18selectedLevelIndexs5Int32Vvp" class="token"><code>selectedLevelIndex</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The index of the <a href="sdk-for-ios-explore-classes-venuelevel">`VenueLevel`</a> selected from the level array of the <a href="sdk-for-ios-explore-classes-venuedrawing">`VenueDrawing`</a>. Unlike the Z index, it can’t have a negative value.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var selectedLevelIndex: Int32 { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk5VenueC17isTopologyVisibleSbvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-isTopologyVisible" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venue#sdk-for-ios-explore-s-7heresdk5VenueC17isTopologyVisibleSbvp" class="token"><code>isTopologyVisible</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns true if topology is visible. It can be used to check the status of topology visibility.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isTopologyVisible: Bool { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk5VenueC14setCustomStyle10geometries5style05labelE0ySayAA0B8GeometryCG_AA0biE0CSgAA0b5LabelE0CSgtF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-setCustomStyle-geometries-style-labelStyle" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venue#sdk-for-ios-explore-s-7heresdk5VenueC14setCustomStyle10geometries5style05labelE0ySayAA0B8GeometryCG_AA0biE0CSgAA0b5LabelE0CSgtF" class="token"><code>setCustomStyle(geometries:</code><wbr></wbr><code>style:</code><wbr></wbr><code>labelStyle:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets a custom style for geometries and related labels.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setCustomStyle(geometries: [VenueGeometry], style: VenueGeometryStyle?, labelStyle: VenueLabelStyle?)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-venuegeometry">VenueGeometry</a>
  - <a href="sdk-for-ios-explore-classes-venuegeometrystyle">VenueGeometryStyle</a>
  - <a href="sdk-for-ios-explore-classes-venuelabelstyle">VenueLabelStyle</a>

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
  <td><code> </code><em><code>geometries</code></em><code> </code></td>
  <td><div>
  <p>The list of geometries to apply the new style.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>style</code></em><code> </code></td>
  <td><div>
  <p>The style for geometries, or <code>nil</code> to reset the style to default.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>labelStyle</code></em><code> </code></td>
  <td><div>
  <p>The style for geometry labels, or <code>nil</code> to reset the label style to default.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk5VenueC14setCustomStyle10topologies5styleySayAA0B8TopologyCG_AA0b8GeometryE0CSgtF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-setCustomStyle-topologies-style" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venue#sdk-for-ios-explore-s-7heresdk5VenueC14setCustomStyle10topologies5styleySayAA0B8TopologyCG_AA0b8GeometryE0CSgtF" class="token"><code>setCustomStyle(topologies:</code><wbr></wbr><code>style:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets a custom style for topologies.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setCustomStyle(topologies: [VenueTopology], style: VenueGeometryStyle?)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-venuetopology">VenueTopology</a>
  - <a href="sdk-for-ios-explore-classes-venuegeometrystyle">VenueGeometryStyle</a>

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
  <td><code> </code><em><code>topologies</code></em><code> </code></td>
  <td><div>
  <p>The list of topologies to apply the new style.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>style</code></em><code> </code></td>
  <td><div>
  <p>The style for geometries, or <code>nil</code> to reset the style to default.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk5VenueC25setCustomStyleToCrosswalk10crosswalks5styleySayAA0G0CG_AA0b8GeometryE0CSgtF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-setCustomStyleToCrosswalk-crosswalks-style" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venue#sdk-for-ios-explore-s-7heresdk5VenueC25setCustomStyleToCrosswalk10crosswalks5styleySayAA0G0CG_AA0b8GeometryE0CSgtF" class="token"><code>setCustomStyleToCrosswalk(crosswalks:</code><wbr></wbr><code>style:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets a custom style for crosswalk.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setCustomStyleToCrosswalk(crosswalks: [Crosswalk], style: VenueGeometryStyle?)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-crosswalk">Crosswalk</a>
  - <a href="sdk-for-ios-explore-classes-venuegeometrystyle">VenueGeometryStyle</a>

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
  <td><code> </code><em><code>crosswalks</code></em><code> </code></td>
  <td><div>
  <p>The list of crosswalk to apply the new style.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>style</code></em><code> </code></td>
  <td><div>
  <p>The style for geometries, or <code>nil</code> to reset the style to default.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

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

