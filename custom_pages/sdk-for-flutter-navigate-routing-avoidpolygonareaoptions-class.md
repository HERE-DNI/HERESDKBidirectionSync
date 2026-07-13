---
title: "AvoidPolygonAreaOptions class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-avoidpolygonareaoptions-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- AvoidPolygonAreaOptions-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/AvoidPolygonAreaOptions-class-sidebar.html">

<div>

# <span class="kind-class">AvoidPolygonAreaOptions</span> class

</div>

<div class="section desc markdown">

The options to specify polygon shape which routes must not cross.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-routing-avoidpolygonareaoptions-avoidpolygonareaoptions">AvoidPolygonAreaOptions</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-avoidPolygonArea" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geopolygon-class">GeoPolygon</a></span> <span class="parameter-name">avoidPolygonArea</span></span>)</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-routing-avoidpolygonareaoptions-avoidpolygonarea">avoidPolygonArea</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-geopolygon-class">GeoPolygon</a></span>  
Area of polygon shape which routes must not cross. Strictly enforced. Violations are reported as <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode.violatedBlockedRoad</a>. **Note:** This avoidance option is not supported for `IsolineOptions`. If it is defined for isoline calculation then an `sdk.routing.RoutingError.INVALID_PARAMETER` error is generated.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-avoidpolygonareaoptions-boundingboxexceptionareas">boundingBoxExceptionAreas</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-geobox-class">GeoBox</a></span>\></span></span>  
Areas of rectangular shape to exclude from avoidance.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-avoidpolygonareaoptions-corridorexceptionareas">corridorExceptionAreas</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-geocorridor-class">GeoCorridor</a></span>\></span></span>  
Areas of corridor shape to exclude from avoidance. **Note:** Even though `GeoCorridor.half_width_in_meters` is an optional property in case of exception areas it is mandatory. Otherwise route calculation will fail with an `sdk.routing.RoutingError.INVALID_PARAMETER` error.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-avoidpolygonareaoptions-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-avoidpolygonareaoptions-polygonexceptionareas">polygonExceptionAreas</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-geopolygon-class">GeoPolygon</a></span>\></span></span>  
Areas of polygon shape to exclude from avoidance.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-avoidpolygonareaoptions-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-routing-avoidpolygonareaoptions-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-avoidpolygonareaoptions-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-routing-avoidpolygonareaoptions-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
