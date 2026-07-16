---
title: "VenueLabelStyle Class Reference"
slug: "sdk-for-ios-explore-classes-venuelabelstyle"
---

# VenueLabelStyle

<div class="declaration">

<div class="language">

``` highlight
public class VenueLabelStyle
```

``` highlight
extension VenueLabelStyle: NativeBase
```

``` highlight
extension VenueLabelStyle: Hashable
```

</div>

</div>

Represents a style of the label.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VenueLabelStyleC9fillColor07outlineF00G5Width7maxFontACSo7UIColorC_AISfs5Int32Vtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-fillColor-outlineColor-outlineWidth-maxFont" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuelabelstyle#sdk-for-ios-explore-s-7heresdk15VenueLabelStyleC9fillColor07outlineF00G5Width7maxFontACSo7UIColorC_AISfs5Int32Vtcfc" class="token"><code>init(fillColor:</code><wbr></wbr><code>outlineColor:</code><wbr></wbr><code>outlineWidth:</code><wbr></wbr><code>maxFont:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a custom label style with specific parameters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(fillColor: UIColor, outlineColor: UIColor, outlineWidth: Float, maxFont: Int32)
  ```

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
  <td><code> </code><em><code>fillColor</code></em><code> </code></td>
  <td><div>
  <p>The fill color.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>outlineColor</code></em><code> </code></td>
  <td><div>
  <p>The outline color.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>outlineWidth</code></em><code> </code></td>
  <td><div>
  <p>The width color.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>maxFont</code></em><code> </code></td>
  <td><div>
  <p>The max font.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VenueLabelStyleC7maxFonts5Int32Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-maxFont" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuelabelstyle#sdk-for-ios-explore-s-7heresdk15VenueLabelStyleC7maxFonts5Int32Vvp" class="token"><code>maxFont</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The maximum font size for this label style.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maxFont: Int32 { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VenueLabelStyleC9fillColorSo7UIColorCvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-fillColor" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuelabelstyle#sdk-for-ios-explore-s-7heresdk15VenueLabelStyleC9fillColorSo7UIColorCvp" class="token"><code>fillColor</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The fill color for this label style.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var fillColor: UIColor { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VenueLabelStyleC12outlineColorSo7UIColorCSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-outlineColor" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuelabelstyle#sdk-for-ios-explore-s-7heresdk15VenueLabelStyleC12outlineColorSo7UIColorCSgvp" class="token"><code>outlineColor</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The outline color. Defaults to `nil` if an outline color has not been set for this label style.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var outlineColor: UIColor? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15VenueLabelStyleC12outlineWidthSfvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-outlineWidth" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-venuelabelstyle#sdk-for-ios-explore-s-7heresdk15VenueLabelStyleC12outlineWidthSfvp" class="token"><code>outlineWidth</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The outline width for this label style.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var outlineWidth: Float { get }
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

