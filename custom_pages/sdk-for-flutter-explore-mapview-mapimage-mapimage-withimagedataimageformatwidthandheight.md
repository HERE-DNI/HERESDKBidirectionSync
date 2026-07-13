---
title: "MapImage.withImageDataImageFormatWidthAndHeight constructor - MapImage - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapimage-mapimage-withimagedataimageformatwidthandheight"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapImage.withImageDataImageFormatWidthAndHeight.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapImage-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapImage.withImageDataImageFormatWidthAndHeight</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapImage.withImageDataImageFormatWidthAndHeight</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-withImageDataImageFormatWidthAndHeight-param-imageData" class="parameter"><span class="type-annotation">Uint8List</span> <span class="parameter-name">imageData</span>, </span>
2.  <span id="sdk-for-flutter-explore-withImageDataImageFormatWidthAndHeight-param-imageFormat" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-imageformat">ImageFormat</a></span> <span class="parameter-name">imageFormat</span>, </span>
3.  <span id="sdk-for-flutter-explore-withImageDataImageFormatWidthAndHeight-param-width" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">width</span>, </span>
4.  <span id="sdk-for-flutter-explore-withImageDataImageFormatWidthAndHeight-param-height" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">height</span>, </span>

)

</div>

<div class="section desc markdown">

Creates a new map image from the provided image data.

- `imageData` Data to be used for the image. For image format <a href="sdk-for-flutter-explore-mapview-imageformat">ImageFormat.svg</a> the bytes of a UTF-8 encoded string in SVG Tiny format are expected. For the format specification see <https://www.w3.org/TR/SVGTiny12>

- `imageFormat` The format of the image data to be used.

- `width` The width of the image in pixels.

- `height` The height of the image in pixels.

</div>

## Implementation

``` dart
factory MapImage.withImageDataImageFormatWidthAndHeight(Uint8List imageData, ImageFormat imageFormat, int width, int height) => $prototype.withImageDataImageFormatWidthAndHeight(imageData, imageFormat, width, height);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
