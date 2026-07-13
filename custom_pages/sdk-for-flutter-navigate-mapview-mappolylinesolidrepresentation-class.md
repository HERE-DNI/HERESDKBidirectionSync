---
title: "MapPolylineSolidRepresentation class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mappolylinesolidrepresentation-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapPolylineSolidRepresentation-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapPolylineSolidRepresentation-class-sidebar.html">

<div>

# <span class="kind-class">MapPolylineSolidRepresentation</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Representation for a solid line without outline.

Can represent polylines that have constant width or width dependent on the map zoom.

To achieve constant width lines, use <a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a> with a single value.

To achieve line width dependent on map zoom, use <a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a> with multiple values.

For <a href="sdk-for-flutter-navigate-mapview-mapmeasurekind">MapMeasureKind</a> only <a href="sdk-for-flutter-navigate-mapview-mapmeasurekind">MapMeasureKind.zoomLevel</a> is supported.

For <a href="sdk-for-flutter-navigate-mapview-rendersizeunit">RenderSizeUnit</a> only <a href="sdk-for-flutter-navigate-mapview-rendersizeunit">RenderSizeUnit.pixels</a> is supported.

</div>

<div class="section">

Implemented types  
- <a href="sdk-for-flutter-navigate-mapview-mappolylinerepresentation-class">MapPolylineRepresentation</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolylinesolidrepresentation-mappolylinesolidrepresentation">MapPolylineSolidRepresentation</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-lineWidth" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span> <span class="parameter-name">lineWidth</span>, </span><span id="sdk-for-flutter-navigate-param-color" class="parameter"><span class="type-annotation">Color</span> <span class="parameter-name">color</span>, </span><span id="sdk-for-flutter-navigate-param-capShape" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-linecap">LineCap</a></span> <span class="parameter-name">capShape</span></span>)</span>  
Creates a representation for a solid line without outline.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolylinesolidrepresentation-mappolylinesolidrepresentation-withoutline">MapPolylineSolidRepresentation.withOutline</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withOutline-param-lineWidth" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span> <span class="parameter-name">lineWidth</span>, </span><span id="sdk-for-flutter-navigate-withOutline-param-color" class="parameter"><span class="type-annotation">Color</span> <span class="parameter-name">color</span>, </span><span id="sdk-for-flutter-navigate-withOutline-param-outlineWidth" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span> <span class="parameter-name">outlineWidth</span>, </span><span id="sdk-for-flutter-navigate-withOutline-param-outlineColor" class="parameter"><span class="type-annotation">Color</span> <span class="parameter-name">outlineColor</span>, </span><span id="sdk-for-flutter-navigate-withOutline-param-capShape" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-linecap">LineCap</a></span> <span class="parameter-name">capShape</span></span>)</span>  
Creates a representation for a solid line with outline.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolylinesolidrepresentation-capshape">capShape</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-mapview-linecap">LineCap</a></span>  
The cap shape applied to both ends of the polyline and its outline. Returns the cap shape of the polyline and its outline.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapitemrepresentation-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolylinesolidrepresentation-linecolor">lineColor</a></span> <span class="signature">→ Color</span>  
The color of the polyline. Gets the color of the polyline.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolylinesolidrepresentation-linewidth">lineWidth</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span>  
The width of the polyline depending on the map measure. At map measures smaller than smallest map measure in the `lineWidth` line width is constant and equal to the width given for the smallest map measure in the `lineWidth`.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolylinesolidrepresentation-outlinecolor">outlineColor</a></span> <span class="signature">→ Color</span>  
The outline color of the polyline. Gets the color of outline of the polyline.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolylinesolidrepresentation-outlinewidth">outlineWidth</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span>  
The width of the outline on one side of the polyline depending on the map measure. The total width of the polyline is `line width + 2 * outline width`.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapitemrepresentation-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapitemrepresentation-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapitemrepresentation-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapitemrepresentation-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
