---
title: "AssetsManager Class Reference"
slug: "sdk-for-ios-explore-classes-assetsmanager"
---

# AssetsManager

<div class="declaration">

<div class="language">

``` highlight
public class AssetsManager
```

``` highlight
extension AssetsManager: NativeBase
```

``` highlight
extension AssetsManager: Hashable
```

</div>

</div>

Assets manager interface. Can be used to make assets available to the SDK.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk13AssetsManagerCyAcA10MapContextCcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-assetsmanager#sdk-for-ios-explore-s-7heresdk13AssetsManagerCyAcA10MapContextCcfc" class="token"><code>init(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an instance of AssetsManager.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(_ context: MapContext)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapcontext">MapContext</a>

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
  <td><code> </code><em><code>context</code></em><code> </code></td>
  <td><div>
  <p>MapContext to which the assets belong.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk13AssetsManagerC12registerFont8fontName0F4PathySS_SStF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-registerFont-fontName-fontPath" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-assetsmanager#sdk-for-ios-explore-s-7heresdk13AssetsManagerC12registerFont8fontName0F4PathySS_SStF" class="token"><code>registerFont(fontName:</code><wbr></wbr><code>fontPath:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Registers a font under a font name. After registration, the font name can be used in

  - the SVG `text` tag as `font-family` attribute parameter when creating a <a href="sdk-for-ios-explore-classes-mapimage">`MapImage`</a> with `ImageFormat.SVG`.
  - <a href="sdk-for-ios-explore-classes-mapmarker-textstyle">`MapMarker.TextStyle`</a>

  Repeated registration with the same font name is ignored.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func registerFont(fontName: String, fontPath: String)
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
  <td><code> </code><em><code>fontName</code></em><code> </code></td>
  <td><div>
  <p>A font name.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>fontPath</code></em><code> </code></td>
  <td><div>
  <p>A font file path. TTF, OTF and WOFF formats are supported. Can be an absolute file path or a resolved bundle resource path.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk13AssetsManagerC24registerFontWithFallback8fontName0H4Path08fallbackE9FilePathsySS_SSSaySSGtF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-registerFontWithFallback-fontName-fontPath-fallbackFontFilePaths" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-assetsmanager#sdk-for-ios-explore-s-7heresdk13AssetsManagerC24registerFontWithFallback8fontName0H4Path08fallbackE9FilePathsySS_SSSaySSGtF" class="token"><code>registerFontWithFallback(fontName:</code><wbr></wbr><code>fontPath:</code><wbr></wbr><code>fallbackFontFilePaths:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Registers a font set under a font name. After registration, the font name can be used in

  - the SVG `text` tag as `font-family` attribute parameter when creating a <a href="sdk-for-ios-explore-classes-mapimage">`MapImage`</a> with `ImageFormat.SVG`.
  - <a href="sdk-for-ios-explore-classes-mapmarker-textstyle">`MapMarker.TextStyle`</a>

  Repeated registration with the same font name is ignored.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func registerFontWithFallback(fontName: String, fontPath: String, fallbackFontFilePaths: [String])
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
  <td><code> </code><em><code>fontName</code></em><code> </code></td>
  <td><div>
  <p>A font name.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>fontPath</code></em><code> </code></td>
  <td><div>
  <p>A font file path. TTF, OTF and WOFF formats are supported. Can be an absolute file path or a resolved bundle resource path.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>fallbackFontFilePaths</code></em><code> </code></td>
  <td><div>
  <p>Additional font files are intended to be used if main font does not contain required character symbol and shall be sorted starting from most useful.</p>
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

