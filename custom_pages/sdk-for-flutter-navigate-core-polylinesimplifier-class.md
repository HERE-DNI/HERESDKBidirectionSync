---
title: "PolylineSimplifier class - core library - Dart API"
slug: "sdk-for-flutter-navigate-core-polylinesimplifier-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core/core-library-sidebar.html" data-below-sidebar="core/PolylineSimplifier-class-sidebar.html">

<div>

# <span class="kind-class">PolylineSimplifier</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

PolylineSimplifier helps to reduce the number of points in the polyline by removing redundant elements using Douglas–Peucker algorithm, so that result stays within <a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-class">PolylineSimplifierOptions</a>.

Typical use case is to perform input preparation step before invoking computationally heavy API. Such API have an upper limit on the input collection size and is subject to reduced performance when collection is huge. Examples of such API are:

- `TrafficEngine` methods which accept a `GeoCorridor`;
- `RoutePrefetcher.prefetchGeoCorridor`.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-core-polylinesimplifier-polylinesimplifier">PolylineSimplifier</a></span><span class="signature">()</span>  
Creates a new instance of <a href="sdk-for-flutter-navigate-core-polylinesimplifier-class">PolylineSimplifier</a>.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-core-polylinesimplifier-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-polylinesimplifier-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-core-polylinesimplifier-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-polylinesimplifier-simplify">simplify</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-simplify-param-polyline" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span>\></span></span> <span class="parameter-name">polyline</span>, </span><span id="sdk-for-flutter-navigate-simplify-param-simplificationParameters" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-class">PolylineSimplifierOptions</a></span> <span class="parameter-name">simplificationParameters</span>, </span><span id="sdk-for-flutter-navigate-simplify-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-polylinesimplificationcallback">PolylineSimplificationCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Reduces the number of points in the input polyline.

<span class="name"><a href="sdk-for-flutter-navigate-core-polylinesimplifier-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-core-polylinesimplifier-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

