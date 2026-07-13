---
title: "MapPolyline class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mappolyline-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapPolyline-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapPolyline-class-sidebar.html">

<div>

# <span class="kind-class">MapPolyline</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

A visual representation of a line on the map.

The geometry to be visualized is represented by an instance of <a href="sdk-for-flutter-navigate-core-geopolyline-class">GeoPolyline</a>.

Altitude component of `GeoPolyline`'s vertices is ignored.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolyline-mappolyline-withrepresentation">MapPolyline.withRepresentation</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withRepresentation-param-geometry" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geopolyline-class">GeoPolyline</a></span> <span class="parameter-name">geometry</span>, </span><span id="sdk-for-flutter-navigate-withRepresentation-param-representation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mappolylinerepresentation-class">MapPolylineRepresentation</a></span> <span class="parameter-name">representation</span></span>)</span>  
Creates a new `MapPolyline` instance with a specified visual representation.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolyline-draworder">drawOrder</a></span> <span class="signature">↔ int</span>  
The draw order of the polyline. Gets the draw order of the polyline.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolyline-drawordertype">drawOrderType</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-mapview-drawordertype">DrawOrderType</a></span>  
The draw order type of the polyline. Gets the draw order type of the polyline.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolyline-geometry">geometry</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-geopolyline-class">GeoPolyline</a></span>  
The list of vertices that represent the geometry of the polyline. Gets the geometry of the polyline.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolyline-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolyline-mapcontentcategoriestoblock">mapContentCategoriesToBlock</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapview-mapcontentcategory">MapContentCategory</a></span>\></span></span>  
List of map content categories this polyline should block. Gets list of map content categories this polyline should block.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolyline-metadata">metadata</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-metadata-class">Metadata</a>?</span>  
The `Metadata` instance attached to this polyline. Gets the `Metadata` instance attached to this polyline. This will be `null` if nothing has been attached before.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolyline-progress">progress</a></span> <span class="signature">↔ double</span>  
The progress from the polyline's starting point, as a ratio of its total length clamped to the range \[0, 1\]. Gets the progress of the polyline, 0 by default.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolyline-progresscolor">progressColor</a></span> <span class="signature">↔ Color</span>  
The color used for the progress part of the polyline. Gets the progress color of the polyline, opaque white by default.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolyline-progressgradientlength">progressGradientLength</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span>  
The maximum gradient length between `MapPolyline.lineColor' and 'MapPolyline.progressColor` in zoom level dependent pixels. Gets the maximum gradient length between `MapPolyline.lineColor' and 'MapPolyline.progressColor` in zoom level dependent pixels.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolyline-progressoutlinecolor">progressOutlineColor</a></span> <span class="signature">↔ Color</span>  
The color used for outline of the progress part of the polyline. Gets the progress outline color of the polyline, opaque white by default.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolyline-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolyline-visibilityranges">visibilityRanges</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapview-mapmeasurerange-class">MapMeasureRange</a></span>\></span></span>  
The list of visibility ranges. The map polyline is visible only inside these map measure ranges. Gets the list of visibility ranges. The map polyline is visible only inside these map measure ranges. When empty (the default), the map polyline is visible without map measure restrictions.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolyline-cancelanimation">cancelAnimation</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-cancelAnimation-param-animation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-animation-mappolylineanimation-class">MapPolylineAnimation</a></span> <span class="parameter-name">animation</span></span>) <span class="returntype parameter">→ void</span> </span>  
Cancels single ongoing animation of this map polyline.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolyline-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolyline-setrepresentation">setRepresentation</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setRepresentation-param-representation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mappolylinerepresentation-class">MapPolylineRepresentation</a></span> <span class="parameter-name">representation</span></span>) <span class="returntype parameter">→ void</span> </span>  
Changes the appearance of the `MapPolyline` instance.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolyline-startanimation">startAnimation</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-startAnimation-param-animation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-animation-mappolylineanimation-class">MapPolylineAnimation</a></span> <span class="parameter-name">animation</span>, </span><span id="sdk-for-flutter-navigate-startAnimation-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-animation-animationlistener-class">AnimationListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Starts an animation of this map polyline.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolyline-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolyline-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
