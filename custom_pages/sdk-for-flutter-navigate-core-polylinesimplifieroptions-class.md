---
title: "PolylineSimplifierOptions class - core library - Dart API"
slug: "sdk-for-flutter-navigate-core-polylinesimplifieroptions-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PolylineSimplifierOptions-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core/core-library-sidebar.html" data-below-sidebar="core/PolylineSimplifierOptions-class-sidebar.html">

<div>

# <span class="kind-class">PolylineSimplifierOptions</span> class

</div>

<div class="section desc markdown">

Controls the strategy of <a href="sdk-for-flutter-navigate-core-polylinesimplifier-simplify">PolylineSimplifier.simplify</a> when reducing a size of polyline.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-polylinesimplifieroptions">PolylineSimplifierOptions</a></span><span class="signature">()</span>  
Creates default options with <a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-maxpoints">PolylineSimplifierOptions.maxPoints</a> equal to 0 and <a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-simplificationtoleranceinmeters">PolylineSimplifierOptions.simplificationToleranceInMeters</a> equal to <a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-simplificationinmeters14zoomlevel">PolylineSimplifierOptions.simplificationInMeters14ZoomLevel</a>.

<span class="name"><a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-polylinesimplifieroptions-withmaxpointsandtolerance">PolylineSimplifierOptions.withMaxPointsAndTolerance</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withMaxPointsAndTolerance-param-maxPoints" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">maxPoints</span>, </span><span id="sdk-for-flutter-navigate-withMaxPointsAndTolerance-param-simplificationToleranceInMeters" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">simplificationToleranceInMeters</span></span>)</span>  
Creates options with explicitly specified <a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-maxpoints">PolylineSimplifierOptions.maxPoints</a> and <a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-simplificationtoleranceinmeters">PolylineSimplifierOptions.simplificationToleranceInMeters</a>.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-maxpoints">maxPoints</a></span> <span class="signature">↔ int</span>  
Sets the upper limit on the resulting collection for the <a href="sdk-for-flutter-navigate-core-polylinesimplifier-simplify">PolylineSimplifier.simplify</a>. Lower value results in the lower accuracy of the resulting polyline. If `maxPoints` is less than `2` then resulting polyline will not have an upper limit on the size and only <a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-simplificationtoleranceinmeters">PolylineSimplifierOptions.simplificationToleranceInMeters</a> will be considered. When `maxPoints` is greater than size of the passed polyline then simplification algorithm will take into account only <a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-simplificationtoleranceinmeters">PolylineSimplifierOptions.simplificationToleranceInMeters</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-simplificationtoleranceinmeters">simplificationToleranceInMeters</a></span> <span class="signature">↔ int</span>  
Sets the accuracy limit for the <a href="sdk-for-flutter-navigate-core-polylinesimplifier-simplify">PolylineSimplifier.simplify</a>:

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Static Properties

<span class="name"><a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-simplificationinmeters14zoomlevel">simplificationInMeters14ZoomLevel</a></span> <span class="signature">→ int</span>  
Value for simplification tolerance for 14 zoom level without significant artifacts.

<div class="features">

<span class="feature">final</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
