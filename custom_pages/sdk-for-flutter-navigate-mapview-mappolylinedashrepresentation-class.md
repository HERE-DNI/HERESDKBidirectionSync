---
title: "MapPolylineDashRepresentation class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mappolylinedashrepresentation-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapPolylineDashRepresentation-class-sidebar.html">

<div>

# <span class="kind-class">MapPolylineDashRepresentation</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Represents a dash pattern for map polyline where the dash can be rendered as a colored line and the gap can be either empty or colored.

The length of the dash and gap are set independently, allowing for patterns like `' — — — —'` (dash length = gap length) or `' ——— ——— ———'` (dash length != gap length).

</div>

<div class="section">

Implemented types  
- <a href="sdk-for-flutter-navigate-mapview-mappolylinerepresentation-class">MapPolylineRepresentation</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolylinedashrepresentation-mappolylinedashrepresentation">MapPolylineDashRepresentation</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-lineWidth" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span> <span class="parameter-name">lineWidth</span>, </span><span id="sdk-for-flutter-navigate-param-dashLength" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span> <span class="parameter-name">dashLength</span>, </span><span id="sdk-for-flutter-navigate-param-gapLength" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span> <span class="parameter-name">gapLength</span>, </span><span id="sdk-for-flutter-navigate-param-dashColor" class="parameter"><span class="type-annotation">Color</span> <span class="parameter-name">dashColor</span></span>)</span>  
Creates a representation for a dashed line.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolylinedashrepresentation-mappolylinedashrepresentation-withgapcolor">MapPolylineDashRepresentation.withGapColor</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withGapColor-param-lineWidth" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span> <span class="parameter-name">lineWidth</span>, </span><span id="sdk-for-flutter-navigate-withGapColor-param-dashLength" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span> <span class="parameter-name">dashLength</span>, </span><span id="sdk-for-flutter-navigate-withGapColor-param-gapLength" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span> <span class="parameter-name">gapLength</span>, </span><span id="sdk-for-flutter-navigate-withGapColor-param-dashColor" class="parameter"><span class="type-annotation">Color</span> <span class="parameter-name">dashColor</span>, </span><span id="sdk-for-flutter-navigate-withGapColor-param-gapColor" class="parameter"><span class="type-annotation">Color</span> <span class="parameter-name">gapColor</span></span>)</span>  
Creates a representation for a dashed line with both dash and the gap being colored.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolylinedashrepresentation-dashcolor">dashColor</a></span> <span class="signature">→ Color</span>  
The color of the dashes of the polyline. Gets the color of the dashes of the polyline.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolylinedashrepresentation-dashlength">dashLength</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span>  
The dash length of the polyline depending on the map measure. At map measures smaller than smallest map measure in the `dashLength` line width is constant and equal to the width given for the smallest map measure in the `dashLength`.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolylinedashrepresentation-gapcolor">gapColor</a></span> <span class="signature">→ Color?</span>  
The color for the gaps of the polyline. The default value is `null` and no color is used. Gets the color for the gaps of the polyline. Returns `null` if no color is used.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolylinedashrepresentation-gaplength">gapLength</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span>  
The gap length of the polyline depending on the map measure. At map measures smaller than smallest map measure in the `gapLength` line width is constant and equal to the width given for the smallest map measure in the `gapLength`.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapitemrepresentation-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolylinedashrepresentation-linewidth">lineWidth</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span>  
The width of the polyline depending on the map measure. At map measures smaller than smallest map measure in the `lineWidth` line width is constant and equal to the width given for the smallest map measure in the `lineWidth`.

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

