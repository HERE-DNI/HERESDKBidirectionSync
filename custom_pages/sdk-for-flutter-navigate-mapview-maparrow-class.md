---
title: "MapArrow class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-maparrow-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapArrow-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapArrow-class-sidebar.html">

<div>

# <span class="kind-class">MapArrow</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

A visual representation of an arrow on the map.

It consists of a tail - a polyline with an arbitrary number of points - and a head at its end.

The map arrows are only visible on zoom levels \>= 13.

Altitude component of `GeoPolyline`'s vertices is ignored.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maparrow-maparrow">MapArrow</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-geometry" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geopolyline-class">GeoPolyline</a></span> <span class="parameter-name">geometry</span>, </span><span id="sdk-for-flutter-navigate-param-widthInPixels" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">widthInPixels</span>, </span><span id="sdk-for-flutter-navigate-param-color" class="parameter"><span class="type-annotation">Color</span> <span class="parameter-name">color</span></span>)</span>  
Creates a new `MapArrow` instance.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maparrow-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maparrow-measuredependenttailwidth">measureDependentTailWidth</a></span> <span class="signature">↔ Map<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a></span>, <span class="type-parameter">double</span>\></span></span>  
The width of the arrow tail in pixels, where the key is a <a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a> and the value is a tail width in pixels at this <a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a>. Gets the <a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a> dependent arrow tail width in pixels.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maparrow-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maparrow-visibilityranges">visibilityRanges</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapview-mapmeasurerange-class">MapMeasureRange</a></span>\></span></span>  
The list of visibility ranges, in which the map arrow is visible. A range is half-open - \<a href="sdk-for-flutter-navigate-mapview-maparrow-nosuchmethod">minimumZoomLevel, maximumZoomLevel), the given maximum value is not contained in the range.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name">[noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maparrow-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maparrow-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
