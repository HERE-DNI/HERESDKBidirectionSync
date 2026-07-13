---
title: "SectionTransportMode enum - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-sectiontransportmode"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/SectionTransportMode-enum-sidebar.html">

<div>

# <span class="kind-enum">SectionTransportMode</span> enum

</div>

<div class="section desc markdown">

Specifies the <a href="sdk-for-flutter-explore-routing-section-class">Section</a> mode of transport.

A <a href="sdk-for-flutter-explore-routing-section-class">Section</a> may have a different transport mode than the one specified for route calculation. For example, a car route may have a section having ferry transport mode.

</div>

## Values

<span class="name">car</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-sectiontransportmode">SectionTransportMode</a></span>  
Car mode of transport.

<span class="name">truck</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-sectiontransportmode">SectionTransportMode</a></span>  
Truck mode of transport.

<span class="name">pedestrian</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-sectiontransportmode">SectionTransportMode</a></span>  
Pedestrian mode of transport.

<span class="name">ferry</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-sectiontransportmode">SectionTransportMode</a></span>  
Ferry mode of transport.

<span class="name">carShuttleTrain</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-sectiontransportmode">SectionTransportMode</a></span>  
Mode of transport representing a shuttle train for cars.

<span class="name">scooter</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-sectiontransportmode">SectionTransportMode</a></span>  
Scooter mode of transport.

<span class="name">bicycle</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-sectiontransportmode">SectionTransportMode</a></span>  
Bicycle mode of transport.

<span class="name">publicTransit</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-sectiontransportmode">SectionTransportMode</a></span>  
A section with this mode is part of a public transit route. The actual transport mode can be obtained from <a href="sdk-for-flutter-explore-routing-section-transitdetails">Section.transitDetails</a>.

<span class="name">taxi</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-sectiontransportmode">SectionTransportMode</a></span>  
Taxi mode of transport.

<span class="name">bus</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-sectiontransportmode">SectionTransportMode</a></span>  
Bus mode of transport. Denotes those vehicles operated by public transport provider. This transport mode has the access to the bus-only lane/road.

<span class="name">privateBus</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-sectiontransportmode">SectionTransportMode</a></span>  
Private bus mode of transport. Denotes those vehicles operated by private transport company. This transport mode does not have the access to the bus-only lane/road.

## Properties

<span class="name"><a href="sdk-for-flutter-explore-routing-sectiontransportmode-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-sectiontransportmode-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-sectiontransportmode-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-routing-sectiontransportmode-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-sectiontransportmode-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-routing-sectiontransportmode-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-explore-routing-sectiontransportmode-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-routing-sectiontransportmode">SectionTransportMode</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

