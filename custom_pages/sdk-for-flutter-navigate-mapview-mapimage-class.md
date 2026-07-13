---
title: "MapImage class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapimage-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapImage-class-sidebar.html">

<div>

# <span class="kind-class">MapImage</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Represents a drawable resource that can be used by a <a href="sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker</a>, <a href="sdk-for-flutter-navigate-mapview-mapmarker3d-class">MapMarker3D</a> or <a href="sdk-for-flutter-navigate-mapview-mapimageoverlay-class">MapImageOverlay</a> to be shown on the map.

Supported formats are listed in <a href="sdk-for-flutter-navigate-mapview-imageformat">ImageFormat</a>. SVG format allows custom fonts in text using font-family attribute by prior registration via `AssetsManager.registerFont`.

It is recommended to associate a resource with a single `MapImage` instance in order to enable resource sharing and reduce the amount of needed memory.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapimage-mapimage-withfilepathandwidthandheight">MapImage.withFilePathAndWidthAndHeight</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withFilePathAndWidthAndHeight-param-filePath" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">filePath</span>, </span><span id="sdk-for-flutter-navigate-withFilePathAndWidthAndHeight-param-width" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">width</span>, </span><span id="sdk-for-flutter-navigate-withFilePathAndWidthAndHeight-param-height" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">height</span></span>)</span>  
Creates a new map image from the provided path to the SVG Tiny or PNG image.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapimage-mapimage-withimagedataimageformatwidthandheight">MapImage.withImageDataImageFormatWidthAndHeight</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withImageDataImageFormatWidthAndHeight-param-imageData" class="parameter"><span class="type-annotation">Uint8List</span> <span class="parameter-name">imageData</span>, </span><span id="sdk-for-flutter-navigate-withImageDataImageFormatWidthAndHeight-param-imageFormat" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-imageformat">ImageFormat</a></span> <span class="parameter-name">imageFormat</span>, </span><span id="sdk-for-flutter-navigate-withImageDataImageFormatWidthAndHeight-param-width" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">width</span>, </span><span id="sdk-for-flutter-navigate-withImageDataImageFormatWidthAndHeight-param-height" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">height</span></span>)</span>  
Creates a new map image from the provided image data.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapimage-mapimage-withpixeldataandimageformat">MapImage.withPixelDataAndImageFormat</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withPixelDataAndImageFormat-param-pixelData" class="parameter"><span class="type-annotation">Uint8List</span> <span class="parameter-name">pixelData</span>, </span><span id="sdk-for-flutter-navigate-withPixelDataAndImageFormat-param-imageFormat" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-imageformat">ImageFormat</a></span> <span class="parameter-name">imageFormat</span></span>)</span>  
Creates a new map image from the provided image data.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapimage-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapimage-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapimage-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapimage-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapimage-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

