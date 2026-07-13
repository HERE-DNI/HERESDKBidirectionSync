---
title: "MapImageOverlay class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapimageoverlay-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapImageOverlay-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapImageOverlay-class-sidebar.html">

<div>

# <span class="kind-class">MapImageOverlay</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

`MapImageOverlay` is used to draw images over the map, at a view coordinate inside the map viewport.

The image to be displayed is represented by a <a href="sdk-for-flutter-explore-mapview-mapimage-class">MapImage</a> object. By default, the overlay is centered on the given view coordinate.

The resulting viewport area covered by the overlay is computed out of the overlay's view coordinate, the anchor point and the image size. The overlay subareas that fall outside of the map viewport get clipped.

To display the map overlay, it needs to be added to the scene using <a href="sdk-for-flutter-explore-mapview-mapscene-addmapimageoverlay">MapScene.addMapImageOverlay</a>. To stop displaying it, remove it from the scene using <a href="sdk-for-flutter-explore-mapview-mapscene-removemapimageoverlay">MapScene.removeMapImageOverlay</a>.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapimageoverlay-mapimageoverlay">MapImageOverlay</a></span><span class="signature">(<span id="sdk-for-flutter-explore-param-viewCoordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-point2d-class">Point2D</a></span> <span class="parameter-name">viewCoordinates</span>, </span><span id="sdk-for-flutter-explore-param-image" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapimage-class">MapImage</a></span> <span class="parameter-name">image</span></span>)</span>  
Creates an instance of an overlay at given view coordinates, represented by specified image.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapimageoverlay-mapimageoverlay-withanchor">MapImageOverlay.withAnchor</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withAnchor-param-viewCoordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-point2d-class">Point2D</a></span> <span class="parameter-name">viewCoordinates</span>, </span><span id="sdk-for-flutter-explore-withAnchor-param-image" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapimage-class">MapImage</a></span> <span class="parameter-name">image</span>, </span><span id="sdk-for-flutter-explore-withAnchor-param-anchor" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-anchor2d-class">Anchor2D</a></span> <span class="parameter-name">anchor</span></span>)</span>  
Creates an instance of an overlay at given view coordinates, represented by specified image, with anchor point specifying how the image is positioned relative to the overlay's view coordinates.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapimageoverlay-anchor">anchor</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-core-anchor2d-class">Anchor2D</a></span>  
The anchor point for the overlay image which specifies the position offset relative to the overlay's view coordinates. Gets current anchor point for the overlay image.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapimageoverlay-draworder">drawOrder</a></span> <span class="signature">↔ int</span>  
Draw order of this `MapImageOverlay`. Gets draw order of this `MapImageOverlay`. The default value is 0.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapimageoverlay-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapimageoverlay-image">image</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-mapview-mapimage-class">MapImage</a></span>  
Image overlayed on the map. Gets currently used map image.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapimageoverlay-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapimageoverlay-viewcoordinates">viewCoordinates</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-core-point2d-class">Point2D</a></span>  
The view point in pixels on the map viewport where the map overlay is drawn. Gets the view point in pixels on the map viewport where the overlay is drawn.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapimageoverlay-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapimageoverlay-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapimageoverlay-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
