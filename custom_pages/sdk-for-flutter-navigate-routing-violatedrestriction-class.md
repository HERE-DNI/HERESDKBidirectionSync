---
title: "ViolatedRestriction class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-violatedrestriction-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/ViolatedRestriction-class-sidebar.html">

<div>

# <span class="kind-class">ViolatedRestriction</span> class

</div>

<div class="section desc markdown">

`ViolatedRestriction` contains all the violated restriction details for the planned trip.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-routing-violatedrestriction-violatedrestriction">ViolatedRestriction</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-cause" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">cause</span>, </span><span id="sdk-for-flutter-navigate-param-timeDependent" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">timeDependent</span></span>)</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-routing-violatedrestriction-cause">cause</a></span> <span class="signature">↔ String</span>  
Cause of the notice. Human readable description of the notice, for example "Route violates vehicle restriction". It will be EN-US text only.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-violatedrestriction-details">details</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-violatedrestrictiondetails-class">ViolatedRestrictionDetails</a>?</span>  
The detailed information of restriction depending on the specific violation. For time dependent restriction or transport mode restriction, this property will be null. For vehicle restriction, the corresponding member will be set, for example, if the vehicle violates the maximum allowed gross weight for a specific route, the max_gross_weight_in_kilograms will be set with the maximum allowed gross weight for this route.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-violatedrestriction-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-violatedrestriction-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-violatedrestriction-timedependent">timeDependent</a></span> <span class="signature">↔ bool</span>  
Indicates that restriction depends on time.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-routing-violatedrestriction-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-violatedrestriction-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-routing-violatedrestriction-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

