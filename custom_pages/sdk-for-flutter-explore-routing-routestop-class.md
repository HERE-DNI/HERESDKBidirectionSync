---
title: "RouteStop class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-routestop-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/RouteStop-class-sidebar.html">

<div>

# <span class="kind-class">RouteStop</span> class

</div>

<div class="section desc markdown">

Route stop that should be used together with import route functionality.

It specifies location index within provided route locations track. Route stop can have additional stop delay, which will be included in expected time to arrival. During navigation the stop will be treated as stopover and will be reported as milestone when passing-by. Only available for the Navigate licence.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-routing-routestop-routestop">RouteStop</a></span><span class="signature">(<span id="sdk-for-flutter-explore-param-locationIndex" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">locationIndex</span></span>)</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-explore-routing-routestop-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-routestop-locationindex">locationIndex</a></span> <span class="signature">↔ int</span>  
Index of location, used for route stop. Index should be \>= 1, which prevents user from using origin location as route stop.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-routestop-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-routestop-stopduration">stopDuration</a></span> <span class="signature">↔ Duration</span>  
Time that will be spent on route stop.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-routing-routestop-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-routestop-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-routing-routestop-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

