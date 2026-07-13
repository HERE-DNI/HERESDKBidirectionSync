---
title: "MapMeasureDependentRenderSize class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapMeasureDependentRenderSize-class-sidebar.html">

<div>

# <span class="kind-class">MapMeasureDependentRenderSize</span> class

</div>

<div class="section desc markdown">

Represents a render size, described as map measure dependent values.

</div>

<div class="section">

Annotations  
- @<a href="https://pub.dev/documentation/meta/1.17.0/meta/immutable-constant.html">immutable</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-measureKind" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmeasurekind">MapMeasureKind</a></span> <span class="parameter-name">measureKind</span>, </span><span id="sdk-for-flutter-navigate-param-sizeUnit" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-rendersizeunit">RenderSizeUnit</a></span> <span class="parameter-name">sizeUnit</span>, </span><span id="sdk-for-flutter-navigate-param-sizes" class="parameter"><span class="type-annotation">Map<span class="signature">\<<wbr></wbr><span class="type-parameter">double</span>, <span class="type-parameter">double</span>\></span></span> <span class="parameter-name">sizes</span></span>)</span>  
Constructs a `MapMeasureDependentRenderSize` from given parameters.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-mapmeasuredependentrendersize-withsinglesize">MapMeasureDependentRenderSize.withSingleSize</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withSingleSize-param-sizeUnit" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-rendersizeunit">RenderSizeUnit</a></span> <span class="parameter-name">sizeUnit</span>, </span><span id="sdk-for-flutter-navigate-withSingleSize-param-size" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">size</span></span>)</span>  
Constructs a `MapMeasureDependentRenderSize` from single size value which is constant across all map measures.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-measurekind">measureKind</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-mapview-mapmeasurekind">MapMeasureKind</a></span>  
The unit used for the key in <a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-sizes">MapMeasureDependentRenderSize.sizes</a>.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-sizes">sizes</a></span> <span class="signature">→ Map<span class="signature">\<<wbr></wbr><span class="type-parameter">double</span>, <span class="type-parameter">double</span>\></span></span>  
The dictionary describing the size (value) per map measure (key).

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-sizeunit">sizeUnit</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-mapview-rendersizeunit">RenderSizeUnit</a></span>  
The unit used for the value in <a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-sizes">MapMeasureDependentRenderSize.sizes</a>.

<div class="features">

<span class="feature">final</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

