---
title: "registerFontWithFallback method - AssetsManager class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-assetsmanager-registerfontwithfallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- registerFontWithFallback.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/AssetsManager-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">registerFontWithFallback</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">registerFontWithFallback</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-registerFontWithFallback-param-fontName" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">fontName</span>, </span>
2.  <span id="sdk-for-flutter-navigate-registerFontWithFallback-param-fontPath" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">fontPath</span>, </span>
3.  <span id="sdk-for-flutter-navigate-registerFontWithFallback-param-fallbackFontFilePaths" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span> <span class="parameter-name">fallbackFontFilePaths</span></span>

)

</div>

<div class="section desc markdown">

Registers a font set under a font name.

After registration, the font name can be used in

- the SVG `text` tag as `font-family` attribute parameter when creating a <a href="sdk-for-flutter-navigate-mapview-mapimage-class">MapImage</a> with `ImageFormat.SVG`.
- <a href="sdk-for-flutter-navigate-mapview-mapmarkertextstyle-class">MapMarkerTextStyle</a>

Repeated registration with the same font name is ignored.

- `fontName` A font name.

- `fontPath` A font file path. TTF, OTF and WOFF formats are supported.

Can be an asset file path or an absolute file path.

- `fallbackFontFilePaths` Additional font files are intended to be used if main font does not contain required character symbol and shall be sorted starting from most useful.

</div>

## Implementation

``` dart
void registerFontWithFallback(String fontName, String fontPath, List<String> fallbackFontFilePaths);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
