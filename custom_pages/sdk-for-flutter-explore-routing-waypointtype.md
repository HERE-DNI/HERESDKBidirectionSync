---
title: "WaypointType enum - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-waypointtype"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- WaypointType.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/WaypointType-enum-sidebar.html">

<div>

# <span class="kind-enum">WaypointType</span> enum

</div>

<div class="section desc markdown">

Defines if the waypoint is a stop over, or a hint for a desired polyline of a route.

</div>

## Values

<span class="name">stopover</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-waypointtype">WaypointType</a></span>  
Stopover mode will cause the route to exactly pass through this point, generating maneuvers and splitting the route into sections. Turns of 180 degrees are generated if necessary.

<span class="name">passThrough</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-waypointtype">WaypointType</a></span>  
Acts as a rough position hint for route calculation on how the route should look like. Does not generate 180 degree turns, nor does it appear in the list of maneuvers. Imprecise inputs such as a map touch location should be represented as a pass through.

## Properties

<span class="name"><a href="sdk-for-flutter-explore-routing-waypointtype-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-waypointtype-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-waypointtype-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-routing-waypointtype-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-waypointtype-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-routing-waypointtype-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-explore-routing-waypointtype-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-routing-waypointtype">WaypointType</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
