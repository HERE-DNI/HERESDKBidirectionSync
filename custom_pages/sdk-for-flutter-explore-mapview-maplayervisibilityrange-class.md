---
title: "MapLayerVisibilityRange class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-maplayervisibilityrange-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapLayerVisibilityRange-class-sidebar.html">

<div>

# <span class="kind-class">MapLayerVisibilityRange</span> class

</div>

<div class="section desc markdown">

A layer's visibility along a zoom level range.

The range is half open - \<a href="https://pub.dev/documentation/meta/1.17.0/meta/immutable-constant.html">minimumZoomLevel, maximumZoomLevel), the given maximum value is not contained in the range.

</div>

<div class="section">

Annotations  
- @[immutable</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-mapview-maplayervisibilityrange-maplayervisibilityrange">MapLayerVisibilityRange</a></span><span class="signature">(<span id="sdk-for-flutter-explore-param-minimumZoomLevel" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">minimumZoomLevel</span>, </span><span id="sdk-for-flutter-explore-param-maximumZoomLevel" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">maximumZoomLevel</span></span>)</span>  
Creates a new instance.

<div class="constructor-modifier features">

const

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-explore-mapview-maplayervisibilityrange-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-maplayervisibilityrange-maximumzoomlevel">maximumZoomLevel</a></span> <span class="signature">→ double</span>  
Minimum zoom level from which the layer will not be visible. The value must be less than or equal to the `MapCameraLimits.MAX_ZOOM_LEVEL`. Note that the map layer is not visible at the maximum zoom level.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-maplayervisibilityrange-minimumzoomlevel">minimumZoomLevel</a></span> <span class="signature">→ double</span>  
Minimum zoom level on which the layer will be visible. The value must be greater than or equal to the `MapCameraLimits.MIN_ZOOM_LEVEL`.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-maplayervisibilityrange-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-mapview-maplayervisibilityrange-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-maplayervisibilityrange-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-mapview-maplayervisibilityrange-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

