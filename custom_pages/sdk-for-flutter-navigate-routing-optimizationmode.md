---
title: "OptimizationMode enum - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-optimizationmode"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- OptimizationMode.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/OptimizationMode-enum-sidebar.html">

<div>

# <span class="kind-enum">OptimizationMode</span> enum

</div>

<div class="section desc markdown">

Identifiers for different optimizations that can be used during the route calculation while trying to keep the quality of the route being calculated high.

The route is considered to be of low quality if it gives the traveler an unpleasant experience, such as having difficult turns or having a lot of turns in general. For example, if there are two possible routes from A to B, one with a length of 1000m and 10 turns, and another with a length of 1050m and only one turn, the second one will be returned as the shortest, although it is 50m longer. Yet, it contains only one turn and it is therefore considered to provide a better traveler experience.

</div>

## Values

<span class="name">fastest</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-optimizationmode">OptimizationMode</a></span>  
The routing algorithm will attempt to find the fastest route possible, i.e. to optimize travel time while at the same time keeping the quality of the route high. For example, the algorithm may favor a route that remains on a highway, even if a shorter route can be achieved by taking a shortcut through side roads.

<span class="name">shortest</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-optimizationmode">OptimizationMode</a></span>  
The routing algorithm will attempt to find the shortest route possible, i.e. to optimize the length of the route while at the same time keeping the quality of the route high. For example, the algorithm may favor taking a shortcut that ignores speed information, even if a faster route can be achieved by staying on the highway.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-routing-optimizationmode-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-optimizationmode-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-optimizationmode-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-routing-optimizationmode-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-optimizationmode-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-routing-optimizationmode-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-navigate-routing-optimizationmode-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-optimizationmode">OptimizationMode</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
