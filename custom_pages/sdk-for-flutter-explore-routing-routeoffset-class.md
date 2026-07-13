---
title: "RouteOffset class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-routeoffset-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RouteOffset-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/RouteOffset-class-sidebar.html">

<div>

# <span class="kind-class">RouteOffset</span> class

</div>

<div class="section desc markdown">

Represents a specific location along the route.

A `RouteOffset` is a location on the route defined by the section index and the distance in meters from the start of that section to the specified location on the route. An offset in meters indicates the distance that needs to be traveled to reach a specific location along the route, such as a railway crossing. For the latter case, the location of a railway crossing can be retrieved from `RouteRailwayCrossing.coordinates`.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-routing-routeoffset-routeoffset">RouteOffset</a></span><span class="signature">(<span id="sdk-for-flutter-explore-param-sectionIndex" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">sectionIndex</span>, </span><span id="sdk-for-flutter-explore-param-offsetInMeters" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">offsetInMeters</span></span>)</span>  
Creates a new instance.

## Properties

<span class="name"><a href="sdk-for-flutter-explore-routing-routeoffset-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-routeoffset-offsetinmeters">offsetInMeters</a></span> <span class="signature">↔ double</span>  
Offset from the start of the indexed <a href="sdk-for-flutter-explore-routing-section-class">Section</a> to the specified location along the route. The maximum possible offset is limited by the length of the section and cannot exceed it.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-routeoffset-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-routeoffset-sectionindex">sectionIndex</a></span> <span class="signature">↔ int</span>  
Index of the corresponding route <a href="sdk-for-flutter-explore-routing-section-class">Section</a>. The start of the section indicates the start of the offset.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-routing-routeoffset-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-routeoffset-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-routing-routeoffset-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
