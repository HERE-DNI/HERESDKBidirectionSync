---
title: "MapImage.withPixelDataAndImageFormat constructor - MapImage - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapimage-mapimage-withpixeldataandimageformat"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapImage-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapImage.withPixelDataAndImageFormat</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapImage.withPixelDataAndImageFormat</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-withPixelDataAndImageFormat-param-pixelData" class="parameter"><span class="type-annotation">Uint8List</span> <span class="parameter-name">pixelData</span>, </span>
2.  <span id="sdk-for-flutter-explore-withPixelDataAndImageFormat-param-imageFormat" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-imageformat">ImageFormat</a></span> <span class="parameter-name">imageFormat</span></span>

)

</div>

<div class="section desc markdown">

Creates a new map image from the provided image data.

Currently only <a href="sdk-for-flutter-explore-mapview-imageformat">ImageFormat.png</a> is accepted.

- `pixelData` Data to be used for the image. The bytes of a PNG image datastream are expected as defined in <https://www.w3.org/TR/PNG>

- `imageFormat` The format of the image data to be used.

</div>

## Implementation

``` dart
factory MapImage.withPixelDataAndImageFormat(Uint8List pixelData, ImageFormat imageFormat) => $prototype.withPixelDataAndImageFormat(pixelData, imageFormat);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

