---
title: "TollOptions class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-tolloptions-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TollOptions-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/TollOptions-class-sidebar.html">

<div>

# <span class="kind-class">TollOptions</span> class

</div>

<div class="section desc markdown">

The option to specify how the tolls should be calculated.

**Note** Not used for offline calculations.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-routing-tolloptions-tolloptions">TollOptions</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-explore-routing-tolloptions-co2class">co2Class</a></span> <span class="signature">↔ int?</span>  
Defines the CO2 class of the vehicle as defined by the toll operator. CO2 class is used with `emissionType`. Allowed values for CO2 class are 1, 2, 3, 4, or 5, where a lower value generally indicates lower CO2 emissions.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-tolloptions-emissiontype">emissionType</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-routing-tolloptionsemissiontype">TollOptionsEmissionType</a>?</span>  
Defines the emission type as defined by the toll operator for toll calculation based on vehicle emissions class. The emission type is based on the European emission standards (Euro 1 to Euro 6, and Euro EEV).

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-tolloptions-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-tolloptions-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-tolloptions-transponders">transponders</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span>  
Specifies the toll collection systems for which the user has valid transponders. Note: currently, the only valid value is "all". This means the user has a transponder that is accepted by all toll systems.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-tolloptions-vehiclecategory">vehicleCategory</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-routing-tolloptionsvehiclecategory">TollOptionsVehicleCategory</a>?</span>  
Defines special vehicle category for toll calculation. Usual types like car or truck are determined from transport mode.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-routing-tolloptions-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-tolloptions-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-routing-tolloptions-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
