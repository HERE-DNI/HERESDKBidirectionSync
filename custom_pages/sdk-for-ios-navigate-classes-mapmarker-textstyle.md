---
title: "TextStyle Class Reference"
slug: "sdk-for-ios-navigate-classes-mapmarker-textstyle"
---

# TextStyle

<div class="declaration">

<div class="language">

``` highlight
public class TextStyle
```

``` highlight
extension MapMarker.TextStyle: NativeBase
```

``` highlight
extension MapMarker.TextStyle: Hashable
```

</div>

</div>

Styling options for the text of a <a href="sdk-for-ios-navigate-classes-mapmarker">`MapMarker`</a>.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk9MapMarkerC9TextStyleC18InstantiationErrora"></span>` `<span id="//apple_ref/swift/Alias/InstantiationError" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-mapmarker-textstyle#/s:7heresdk9MapMarkerC9TextStyleC18InstantiationErrora" class="token"><code>InstantiationError</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Thrown when a problem occurs while trying to create a `MapMarker.TextStyle` instance.

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

- <div>

      init()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a default set of styling options for the text of a <a href="sdk-for-ios-navigate-classes-mapmarker">`MapMarker`</a> that consists of the following values:

  - Text size: 18 pixels
  - Text color: opaque white
  - Text outline size: 0 pixels
  - Text outline color: opaque black
  - Text placement: <a href="sdk-for-ios-navigate-classes-mapmarker-textstyle-placement#/s:7heresdk9MapMarkerC9TextStyleC9PlacementO6bottomyA2GmF">`MapMarker.TextStyle.Placement.bottom`</a>

  Once the resulting `TextStyle` is applied to a <a href="sdk-for-ios-navigate-classes-mapmarker">`MapMarker`</a>, its text will be centered over its image. The font will be 18 pixels wide, colored opaque white and will have no visible outline.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ()
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      init(textSize: textColor: textOutlineSize: textOutlineColor: placements: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a set of styling options for the text of a <a href="sdk-for-ios-navigate-classes-mapmarker">`MapMarker`</a>.

  List of placements is used to specify allowed placement of text relative to the icon. When marker overlapping is allowed as set by <a href="sdk-for-ios-navigate-classes-mapmarker#/s:7heresdk9MapMarkerC16isOverlapAllowedSbvp">`MapMarker.isOverlapAllowed`</a>, only first placement element is considered. Otherwise the placement value is chosen so that the text does not overlap with other <a href="sdk-for-ios-navigate-classes-mapmarker">`MapMarker`</a> instances.

  Placement values are prioritized according to the order in which they appear in the list. Lists with duplicate entries as well as empty lists are not supported.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-classes-mapmarker-textstyle#/s:7heresdk9MapMarkerC9TextStyleC18InstantiationErrora">`MapMarker.TextStyle.InstantiationError`</a> In case of invalid input parameters.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( textSize : Double , textColor : UIColor , textOutlineSize : Double , textOutlineColor : UIColor , placements : [ MapMarker . TextStyle . Placement ]) throws
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
  <td><code> </code><em><code>textSize</code></em><code> </code></td>
  <td><div>
  <p>The size of the text in pixels. Only positive values are supported.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>textColor</code></em><code> </code></td>
  <td><div>
  <p>The text color.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>textOutlineSize</code></em><code> </code></td>
  <td><div>
  <p>The size of the text outline in pixels. Only non-negative values are supported.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>textOutlineColor</code></em><code> </code></td>
  <td><div>
  <p>The color of the text outline.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>placements</code></em><code> </code></td>
  <td><div>
  <p>List of allowed placements of the text relative to the icon of a <a href="sdk-for-ios-navigate-classes-mapmarker"><code>MapMarker</code></a>.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      init(textSize: textColor: textOutlineSize: textOutlineColor: placements: fontName: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a set of styling options for the text of a <a href="sdk-for-ios-navigate-classes-mapmarker">`MapMarker`</a>.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  List of placements is used to specify allowed placement of text relative to the icon. When marker overlapping is allowed as set by <a href="sdk-for-ios-navigate-classes-mapmarker#/s:7heresdk9MapMarkerC16isOverlapAllowedSbvp">`MapMarker.isOverlapAllowed`</a>, only first placement element is considered. Otherwise the placement value is chosen so that the text does not overlap with other <a href="sdk-for-ios-navigate-classes-mapmarker">`MapMarker`</a> instances.

  Placement values are prioritized according to the order in which they appear in the list. Lists with duplicate entries as well as empty lists are not supported.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-classes-mapmarker-textstyle#/s:7heresdk9MapMarkerC9TextStyleC18InstantiationErrora">`MapMarker.TextStyle.InstantiationError`</a> In case of invalid input parameters.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( textSize : Double , textColor : UIColor , textOutlineSize : Double , textOutlineColor : UIColor , placements : [ MapMarker . TextStyle . Placement ], fontName : String ) throws
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
  <td><code> </code><em><code>textSize</code></em><code> </code></td>
  <td><div>
  <p>The size of the text in pixels. Only positive values are supported.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>textColor</code></em><code> </code></td>
  <td><div>
  <p>The text color.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>textOutlineSize</code></em><code> </code></td>
  <td><div>
  <p>The size of the text outline in pixels. Only non-negative values are supported.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>textOutlineColor</code></em><code> </code></td>
  <td><div>
  <p>The color of the text outline.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>placements</code></em><code> </code></td>
  <td><div>
  <p>List of allowed placements of the text relative to the icon of a <a href="sdk-for-ios-navigate-classes-mapmarker"><code>MapMarker</code></a>.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>fontName</code></em><code> </code></td>
  <td><div>
  <p>Font name, registered with <code>AssetsManager.registerFont</code>. If empty string is provided, a default font will be used.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9MapMarkerC9TextStyleC8fontNameSSvp"></span>` `<span id="//apple_ref/swift/Property/fontName" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-mapmarker-textstyle#/s:7heresdk9MapMarkerC9TextStyleC8fontNameSSvp" class="token"><code>fontName</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The font used in the text style.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var fontName: String { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9MapMarkerC9TextStyleC8textSizeSdvp"></span>` `<span id="//apple_ref/swift/Property/textSize" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-mapmarker-textstyle#/s:7heresdk9MapMarkerC9TextStyleC8textSizeSdvp" class="token"><code>textSize</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The text size in pixels.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var textSize: Double { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9MapMarkerC9TextStyleC9textColorSo7UIColorCvp"></span>` `<span id="//apple_ref/swift/Property/textColor" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-mapmarker-textstyle#/s:7heresdk9MapMarkerC9TextStyleC9textColorSo7UIColorCvp" class="token"><code>textColor</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The text color.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var textColor: UIColor { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9MapMarkerC9TextStyleC15textOutlineSizeSdvp"></span>` `<span id="//apple_ref/swift/Property/textOutlineSize" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-mapmarker-textstyle#/s:7heresdk9MapMarkerC9TextStyleC15textOutlineSizeSdvp" class="token"><code>textOutlineSize</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The text outline size in pixels.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var textOutlineSize: Double { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9MapMarkerC9TextStyleC16textOutlineColorSo7UIColorCvp"></span>` `<span id="//apple_ref/swift/Property/textOutlineColor" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-mapmarker-textstyle#/s:7heresdk9MapMarkerC9TextStyleC16textOutlineColorSo7UIColorCvp" class="token"><code>textOutlineColor</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The text outline color.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var textOutlineColor: UIColor { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9MapMarkerC9TextStyleC10placementsSayAE9PlacementOGvp"></span>` `<span id="//apple_ref/swift/Property/placements" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-mapmarker-textstyle#/s:7heresdk9MapMarkerC9TextStyleC10placementsSayAE9PlacementOGvp" class="token"><code>placements</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of possible text placements relative to the icon of a <a href="sdk-for-ios-navigate-classes-mapmarker">`MapMarker`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var placements: [MapMarker.TextStyle.Placement] { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9MapMarkerC9TextStyleC22InstantiationErrorCodeO"></span>` `<span id="//apple_ref/swift/Enum/InstantiationErrorCode" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-mapmarker-textstyle#/s:7heresdk9MapMarkerC9TextStyleC22InstantiationErrorCodeO" class="token"><code>InstantiationErrorCode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Describes a reason for failing to create a <a href="sdk-for-ios-navigate-classes-mapmarker-textstyle">`MapMarker.TextStyle`</a>.

  <a href="sdk-for-ios-navigate-classes-mapmarker-textstyle-instantiationerrorcode" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum InstantiationErrorCode : UInt32, CaseIterable, Codable
  ```

  ``` highlight
  extension MapMarker.TextStyle.InstantiationErrorCode : Error
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk9MapMarkerC9TextStyleC9PlacementO"></span>` `<span id="//apple_ref/swift/Enum/Placement" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-mapmarker-textstyle#/s:7heresdk9MapMarkerC9TextStyleC9PlacementO" class="token"><code>Placement</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents text placement with respect to the icon of a <a href="sdk-for-ios-navigate-classes-mapmarker">`MapMarker`</a>.

  <a href="sdk-for-ios-navigate-classes-mapmarker-textstyle-placement" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum Placement : UInt32, CaseIterable, Codable
  ```

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

