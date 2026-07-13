---
title: "MapSceneLightsDirection class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapscenelightsdirection-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapSceneLightsDirection-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapSceneLightsDirection-class-sidebar.html">

<div>

# <span class="kind-class">MapSceneLightsDirection</span> class

</div>

<div class="section desc markdown">

The direction of lights as a pair of azimuth and altitude angles.

See <https://en.wikipedia.org/wiki/Horizontal_coordinate_system>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapscenelightsdirection-mapscenelightsdirection">MapSceneLightsDirection</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-azimuth" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">azimuth</span>, </span><span id="sdk-for-flutter-navigate-param-altitude" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">altitude</span></span>)</span>  
Constructs a Direction from the values.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapscenelightsdirection-mapscenelightsdirection-zero">MapSceneLightsDirection.zero</a></span><span class="signature">()</span>  
Constructs a Direction with default values: azimuth = 0.0, altitude = 0.0.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapscenelightsdirection-altitude">altitude</a></span> <span class="signature">↔ double</span>  
Direction altitude value in degrees in the range \[0, 90\]. The default value is 0.0. The altitude value is clamped to this range. If the value falls outside its supported range, it will be adjusted to stay within the range. Specifically, values less than 0 will be set to 0, and values greater than 90 will be set to 90. Note: Unlike azimuth, altitude values are not wrapped around; they are clamped directly. For example, an altitude value of -10 will be adjusted to 0, and an altitude value of 100 will be adjusted to 90. When both azimuth and altitude values are provided, they are adjusted independently: For instance, (0, -10) is changed to (0, 0) rather than (180, 10).

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapscenelightsdirection-azimuth">azimuth</a></span> <span class="signature">↔ double</span>  
Direction azimuth value in degrees in the range \<a href="sdk-for-flutter-navigate-mapview-mapscenelightsdirection-hashcode">0, 360). The default value is 0.0. The azimuth range is half-open, meaning the maximum value is not included in the range. If the azimuth value falls outside the range, it is wrapped to stay within \[0, 360). Specifically, values less than 0 will be increased by 360 until they fall within the range, and values greater than or equal to 360 will be reduced by 360 until they fall within the range. By convention, an azimuth of 0 degrees corresponds to North, and azimuth values increase clockwise. Thus, 90 degrees corresponds to East, 180 degrees to South, and 270 degrees to West.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name">[hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapscenelightsdirection-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapscenelightsdirection-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapscenelightsdirection-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapscenelightsdirection-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
