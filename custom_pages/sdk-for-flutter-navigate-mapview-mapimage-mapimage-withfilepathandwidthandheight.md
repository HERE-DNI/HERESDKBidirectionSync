---
title: "MapImage.withFilePathAndWidthAndHeight constructor - MapImage - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapimage-mapimage-withfilepathandwidthandheight"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapImage-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapImage.withFilePathAndWidthAndHeight</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapImage.withFilePathAndWidthAndHeight</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-withFilePathAndWidthAndHeight-param-filePath" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">filePath</span>, </span>
2.  <span id="sdk-for-flutter-navigate-withFilePathAndWidthAndHeight-param-width" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">width</span>, </span>
3.  <span id="sdk-for-flutter-navigate-withFilePathAndWidthAndHeight-param-height" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">height</span></span>

)

</div>

<div class="section desc markdown">

Creates a new map image from the provided path to the SVG Tiny or PNG image.

Will throw an error if either the height or width equals zero or the path is empty.

Trying to load a file that is not compliant with SVG Tiny or PNG results in an undefined behavior. In particular, loading SVG that exceeds Tiny SVG specification may result in an image that exhibits unexpected artifacts.

The caller must ensure that the file remains accessible for the entire duration of its usage by the SDK. If that cannot be ensured, then it is recommended to either copy the file to a location that remains accessible for the entire duration of its usage by the SDK or load and pass the file content to one of the `MapImage` constructors that creates instances out of image data (<a href="sdk-for-flutter-navigate-mapview-mapimage-mapimage-withpixeldataandimageformat">MapImage.withPixelDataAndImageFormat</a>, <a href="sdk-for-flutter-navigate-mapview-mapimage-mapimage-withimagedataimageformatwidthandheight">MapImage.withImageDataImageFormatWidthAndHeight</a>).}

Please note that on iOS, file paths that originate, for example from a file picker (like `FilePicker`) can be deleted by the system while the application is still running.

- `filePath` The path to image file.

- `width` The width of image in pixels.

- `height` The height of image in pixels.

Throws <a href="sdk-for-flutter-navigate-core-errors-instantiationexception-class">InstantiationException</a>. Indicates what went wrong when the instantiation was attempted.

</div>

## Implementation

``` dart
factory MapImage.withFilePathAndWidthAndHeight(String filePath, int width, int height) => $prototype.withFilePathAndWidthAndHeight(filePath, width, height);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

