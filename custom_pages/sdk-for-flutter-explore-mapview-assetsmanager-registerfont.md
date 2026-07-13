---
title: "registerFont method - AssetsManager class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-assetsmanager-registerfont"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- registerFont.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/AssetsManager-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">registerFont</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">registerFont</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-registerFont-param-fontName" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">fontName</span>, </span>
2.  <span id="sdk-for-flutter-explore-registerFont-param-fontPath" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">fontPath</span></span>

)

</div>

<div class="section desc markdown">

Registers a font under a font name.

After registration, the font name can be used in

- the SVG `text` tag as `font-family` attribute parameter when creating a <a href="sdk-for-flutter-explore-mapview-mapimage-class">MapImage</a> with `ImageFormat.SVG`.
- <a href="sdk-for-flutter-explore-mapview-mapmarkertextstyle-class">MapMarkerTextStyle</a>

Repeated registration with the same font name is ignored.

- `fontName` A font name.

- `fontPath` A font file path. TTF, OTF and WOFF formats are supported.

Can be an asset file path or an absolute file path.

</div>

## Implementation

``` dart
void registerFont(String fontName, String fontPath);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
