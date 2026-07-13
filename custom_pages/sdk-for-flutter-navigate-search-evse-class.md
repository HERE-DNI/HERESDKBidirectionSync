---
title: "Evse class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-evse-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/Evse-class-sidebar.html">

<div>

# <span class="kind-class">Evse</span> class

</div>

<div class="section desc markdown">

Charge Point Operator (CPO) ID uses the Electric Vehicle Supply Equipment ID (EVSE ID) for an exact identification of the charging infrastructure and charging point.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-search-evse-evse">Evse</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-search-evse-connectors">connectors</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-evseconnector-class">EVSEConnector</a></span>\></span></span>  
List of connectors of this EVSE.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evse-cpoevseemi3id">cpoEvseEmi3Id</a></span> <span class="signature">↔ String?</span>  
Identifier in Emi3 format of the EVSE within the Charge Point Operator (CPO) platform. This id is not always present. Example of ID format: `DE*ICT*E0001897`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evse-cpoid">cpoId</a></span> <span class="signature">↔ String?</span>  
The unique ID of an EVSE in the system of the CPO. This ID is unique in the system of the CPO but not necessarily globally unique. The format will differ between different CPOs. This ID is always provided.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evse-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evse-id">id</a></span> <span class="signature">↔ String?</span>  
HERE ID of the EVSE.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evse-lastupdated">lastUpdated</a></span> <span class="signature">↔ DateTime?</span>  
Last update of the dynamic connector availability information.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evse-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evse-status">status</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-search-evsestatus">EVSEStatus</a>?</span>  
EVSE status.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-search-evse-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evse-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-search-evse-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

