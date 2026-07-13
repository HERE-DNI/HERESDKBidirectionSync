---
title: "Toll class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-toll-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Toll-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/Toll-class-sidebar.html">

<div>

# <span class="kind-class">Toll</span> class

</div>

<div class="section desc markdown">

This struct presents all the data for a toll.

**Note**: If you're using the `OfflineRoutingEngine`, be aware that this feature is currently in **beta**. As a result, there may be some bugs or unexpected behaviors. Additionally, this feature and related APIs may be updated in future releases without going through the deprecation process. Note that the `OfflineRoutingEngine` is only available for the Navigate license. If you're using the `RoutingEngine`, this feature is considered to be stable.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-routing-toll-toll">Toll</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-countryCode" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">countryCode</span>, </span><span id="sdk-for-flutter-navigate-param-tollSystems" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span> <span class="parameter-name">tollSystems</span>, </span><span id="sdk-for-flutter-navigate-param-fares" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-tollfare-class">TollFare</a></span>\></span></span> <span class="parameter-name">fares</span></span>)</span>  
Creates a new instance.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-routing-toll-countrycode">countryCode</a></span> <span class="signature">↔ String</span>  
The country in which the toll is to be paid in ISO-3166-1 alpha-3 format, e.g. "USA".

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-toll-fares">fares</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-tollfare-class">TollFare</a></span>\></span></span>  
The list of toll fares possible for the toll which may depend on time of day, payment method, vehicle characteristics, etc. If there are multiple toll fares that the router cannot disambiguate, then the list will contain more than one toll fare. Note that this list contains at least one element, i.e. it is never empty.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-toll-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-toll-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-toll-tollsystems">tollSystems</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span>  
Names of the multiple toll systems which are associated with the toll, e.g. \["ATLANDES“, "ASF", "COFIROUTE"\]. When the toll information covers several toll roads and the toll system of the each road is different, all toll system names are listed here and the last element will be one of the exit toll booth.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-routing-toll-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-toll-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-routing-toll-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
