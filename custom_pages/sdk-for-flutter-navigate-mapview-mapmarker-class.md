---
title: "MapMarker class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapmarker-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapMarker-class-sidebar.html">

<div>

# <span class="kind-class">MapMarker</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

`MapMarker` is used to draw images on the map, for example to mark a specific location.

By default, the marker is centered on the given geographic coordinates. Markers keep their size regardless of the current zoom level of the map view.

The image to be displayed is represented by <a href="sdk-for-flutter-navigate-mapview-mapimage-class">MapImage</a> object. For performance reasons, it is highly recommended to reuse a single instance of the image when creating multiple identical markers.

To display the map marker, it needs to be added to the scene using <a href="sdk-for-flutter-navigate-mapview-mapscene-addmapmarker">MapScene.addMapMarker</a>. To stop displaying it, remove it from the scene using <a href="sdk-for-flutter-navigate-mapview-mapscene-removemapmarker">MapScene.removeMapMarker</a>.

The display of a map marker is only guaranteed in case its origin is within the viewport. At the moment, this is a known limitation that mostly affects map markers which are visually large and cover a sizeable part of the viewport.

**Note:** Due to technical limitations using the MapMarkers API to add a very large number of markers (several thousands, especially 10000+) is not recommended. Adding this many markers will have a negative impact on the performance leading to stuttering of the app and lower frame rates. To work around this limitation the following approach can be used: Register to map camera updates using <a href="sdk-for-flutter-navigate-mapview-mapcamera-addlistener">MapCamera.addListener</a>. Query the bounding box of the camera viewport using <a href="sdk-for-flutter-navigate-mapview-mapcamera-boundingbox">MapCamera.boundingBox</a> (it may be extended) and then use the method <a href="sdk-for-flutter-navigate-core-geobox-containsgeocoordinates">GeoBox.containsGeoCoordinates</a> in combination with <a href="sdk-for-flutter-navigate-mapview-mapcamerastate-distancetotargetinmeters">MapCameraState.distanceToTargetInMeters</a> to determine which MapMarkers are actually visible to the user in the current camera viewport and thus need to be added to the map.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmarker-mapmarker">MapMarker</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-coordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">coordinates</span>, </span><span id="sdk-for-flutter-navigate-param-image" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapimage-class">MapImage</a></span> <span class="parameter-name">image</span></span>)</span>  
Creates an instance of a marker at given coordinates, represented by specified image.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmarker-mapmarker-withanchor">MapMarker.withAnchor</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withAnchor-param-coordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">coordinates</span>, </span><span id="sdk-for-flutter-navigate-withAnchor-param-image" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapimage-class">MapImage</a></span> <span class="parameter-name">image</span>, </span><span id="sdk-for-flutter-navigate-withAnchor-param-anchor" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-anchor2d-class">Anchor2D</a></span> <span class="parameter-name">anchor</span></span>)</span>  
Creates an instance of a marker at given coordinates, represented by specified image, with anchor point specifying how the image is positioned relative to the marker's coordinates.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmarker-mapmarker-withimageandtext">MapMarker.withImageAndText</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withImageAndText-param-coordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">coordinates</span>, </span><span id="sdk-for-flutter-navigate-withImageAndText-param-image" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapimage-class">MapImage</a></span> <span class="parameter-name">image</span>, </span><span id="sdk-for-flutter-navigate-withImageAndText-param-text" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">text</span></span>)</span>  
Creates a `MapMarker` instance at given coordinates with specified image and text and a default text style.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmarker-anchor">anchor</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-anchor2d-class">Anchor2D</a></span>  
The anchor point for the marker image which specifies the position offset relative to the marker's coordinates. Gets current anchor point for the marker image.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmarker-coordinates">coordinates</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span>  
The point on the map where the map marker is drawn. Gets the point on the map where the marker is drawn.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmarker-draworder">drawOrder</a></span> <span class="signature">↔ int</span>  
The draw order of this marker relative to other markers. Gets draw order of this marker relative to other markers. The default value is 0.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmarker-fadeduration">fadeDuration</a></span> <span class="signature">↔ Duration</span>  
Duration of a fade-in effect on marker addition to a scene or a fade-out effect on marker removal from a scene. Gets the current duration of a fade-in effect on marker addition to a scene or a fade-out effect on marker removal from a scene.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmarker-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmarker-image">image</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-mapview-mapimage-class">MapImage</a></span>  
Image representing the marker on the screen. Gets currently used map image.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmarker-isoverlapallowed">isOverlapAllowed</a></span> <span class="signature">↔ bool</span>  
Determines whether or not the marker can overlap other markers. Returns `true` if the marker allows overlap with other markers, `false` otherwise. Defaults to `true`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmarker-istextoptional">isTextOptional</a></span> <span class="signature">↔ bool</span>  
Determines if the marker can be displayed with icon and without text. Returns `true` if the marker allows text to be hidden, `false` otherwise. Defaults to `false`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmarker-metadata">metadata</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-metadata-class">Metadata</a>?</span>  
The Metadata instance attached to this marker, see <a href="sdk-for-flutter-navigate-core-metadata-class">Metadata</a>. Gets the Metadata instance attached to this marker. This will be `null` if nothing has been attached before.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmarker-opacity">opacity</a></span> <span class="signature">↔ double</span>  
Opacity, the factor applied to the alpha channel of the marker image. Gets the current opacity of the marker image. Value is in the range of \[0.0, 1.0\]. Default value is 1.0.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmarker-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmarker-text">text</a></span> <span class="signature">↔ String</span>  
The text to be drawn on the map along with the image of the `MapMarker`. Gets the text drawn on the map by the `MapMarker`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmarker-textstyle">textStyle</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-mapview-mapmarkertextstyle-class">MapMarkerTextStyle</a></span>  
The `TextStyle` applied to the text of the `MapMarker`. Gets a copy of the `TextStyle` currently in use by the `MapMarker`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmarker-visibilityranges">visibilityRanges</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapview-mapmeasurerange-class">MapMeasureRange</a></span>\></span></span>  
The list of visibility ranges. The map marker is visible only inside these map measure ranges. Gets the list of visibility ranges. The map marker is visible only inside these map measure ranges. When empty (the default), the map marker is visible without map measure restrictions.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmarker-cancelanimation">cancelAnimation</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-cancelAnimation-param-animation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-animation-mapmarkeranimation-class">MapMarkerAnimation</a></span> <span class="parameter-name">animation</span></span>) <span class="returntype parameter">→ void</span> </span>  
Cancels single ongoing animation.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmarker-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmarker-startanimation">startAnimation</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-startAnimation-param-animation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-animation-mapmarkeranimation-class">MapMarkerAnimation</a></span> <span class="parameter-name">animation</span>, </span><span id="sdk-for-flutter-navigate-startAnimation-param-animationListener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-animation-animationlistener-class">AnimationListener</a>?</span> <span class="parameter-name">animationListener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Starts animation of this map marker according to provided <a href="sdk-for-flutter-navigate-animation-mapmarkeranimation-class">MapMarkerAnimation</a>.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmarker-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmarker-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

