---
title: "MapPolylineDashImageRepresentation class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mappolylinedashimagerepresentation-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapPolylineDashImageRepresentation-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapPolylineDashImageRepresentation-class-sidebar.html">

<div>

# <span class="kind-class">MapPolylineDashImageRepresentation</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Represents a dash pattern for the map polyline consisting of images rendered with certain gaps from each other.

This dash pattern representation consists only of images rendered at certain points along the polyline. For rendering them without any distortions, polyline gets sliced into series of straight segments that are multiple of sum of dash and gap lengths. For this reason, the new polyline geometry might not align fully with original geometry.

The <a href="sdk-for-flutter-navigate-mapview-mappolylinedashimagerepresentation-dashimage">MapPolylineDashImageRepresentation.dashImage</a> is stretched according to `MapPolylineDashImageRepresentation.dashLength` and `MapPolylineDashImageRepresentation.dashWidth`, with image's width matched to `dashLength` and image's height matched to `dashWidth`. The image is oriented so that its bottom is on the left-hand side between vertices `n` and `n+1`.

The spacing between images is specified by `MapPolylineDashImageRepresentation.gapLength`.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section">

Implemented types  
- <a href="sdk-for-flutter-navigate-mapview-mappolylinerepresentation-class">MapPolylineRepresentation</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolylinedashimagerepresentation-mappolylinedashimagerepresentation">MapPolylineDashImageRepresentation</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-dashLength" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span> <span class="parameter-name">dashLength</span>, </span><span id="sdk-for-flutter-navigate-param-gapLength" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span> <span class="parameter-name">gapLength</span>, </span><span id="sdk-for-flutter-navigate-param-dashWidth" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span> <span class="parameter-name">dashWidth</span>, </span><span id="sdk-for-flutter-navigate-param-image" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapimage-class">MapImage</a></span> <span class="parameter-name">image</span></span>)</span>  
Creates a simple dash pattern in which the lengths of a dash and gap can be different.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolylinedashimagerepresentation-mappolylinedashimagerepresentation-uniform">MapPolylineDashImageRepresentation.uniform</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-uniform-param-dashLength" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span> <span class="parameter-name">dashLength</span>, </span><span id="sdk-for-flutter-navigate-uniform-param-dashWidth" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span> <span class="parameter-name">dashWidth</span>, </span><span id="sdk-for-flutter-navigate-uniform-param-image" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapimage-class">MapImage</a></span> <span class="parameter-name">image</span></span>)</span>  
Creates a uniform dash pattern in which the length of a gap is the same as the length of a dash.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolylinedashimagerepresentation-dashimage">dashImage</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-mapview-mapimage-class">MapImage</a></span>  
Image to be rendered in place of dash space. It is stretched to fill whole polyline width and length of each dash. Gets the image that is rendered in place of dash space.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolylinedashimagerepresentation-dashlength">dashLength</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span>  
The map measure dependent length of a dash, to which image width is stretched. Gets the map measure dependent length of a dash, to which image width is stretched.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolylinedashimagerepresentation-dashwidth">dashWidth</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span>  
The map measure dependent width of a dash, to which image height is stretched. Gets the map measure dependent width of a dash, to which image height is stretched.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolylinedashimagerepresentation-gaplength">gapLength</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span>  
The map measure dependent length of a gap between dash images. Gets the map measure dependent length of a gap between dash images.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapitemrepresentation-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

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
