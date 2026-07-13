---
title: "Isoline class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-isoline-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Isoline-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/Isoline-class-sidebar.html">

<div>

# <span class="kind-class">Isoline</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Represents an isoline polygon around a center point.

Any possible route between the center and any point on the edges of the polygon can be travelled within the given range restriction. The edges of the polygon are not guaranteed to be on the road as all reachable road endpoints are smoothened to fit into one polygon shape. This process can be influenced by setting <a href="sdk-for-flutter-explore-routing-isolineoptionscalculation-maxpoints">IsolineOptionsCalculation.maxPoints</a>.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-routing-isoline-isoline">Isoline</a></span><span class="signature">(<span id="sdk-for-flutter-explore-param-rangeType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-isolinerangetype">IsolineRangeType</a></span> <span class="parameter-name">rangeType</span>, </span><span id="sdk-for-flutter-explore-param-rangeValue" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">rangeValue</span>, </span><span id="sdk-for-flutter-explore-param-center" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-mapmatchedcoordinates-class">MapMatchedCoordinates</a></span> <span class="parameter-name">center</span>, </span><span id="sdk-for-flutter-explore-param-polygons" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-core-geopolygon-class">GeoPolygon</a></span>\></span></span> <span class="parameter-name">polygons</span></span>)</span>  
Constructs an isoline instance.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-explore-routing-isoline-center">center</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-routing-mapmatchedcoordinates-class">MapMatchedCoordinates</a></span>  
The center point that was used to calculate this isoline. Specifies the center point that was used to calculate this isoline. This includes the original center that was passed to the RoutingEngine. Gets the center point that was used to calculate this isoline.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-isoline-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-isoline-polygons">polygons</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-core-geopolygon-class">GeoPolygon</a></span>\></span></span>  
A list of polygons that belong to this isoline. An isoline can consist of multiple polygons. For example, islands that can be reached by a ferry are included. Each island is then represented as a separate polygon. However, in most cases only a single polygon is included. Gets a list of polygons that belong to this isoline. An isoline can consist of multiple polygons. For example, islands that can be reached by a ferry are included. Each island is then represented as a separate polygon. However, in most cases only a single polygon is included.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-isoline-rangetype">rangeType</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-routing-isolinerangetype">IsolineRangeType</a></span>  
Specifies the type of the restriction that was used to calculate this isoline. Gets the type of the restriction that was used to calculate this isoline.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-isoline-rangevalue">rangeValue</a></span> <span class="signature">→ double</span>  
Specifies the numerical value of the restriction that was used to calculate this isoline. Gets the numerical value of the restriction that was used to calculate this isoline.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-isoline-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-routing-isoline-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-isoline-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-routing-isoline-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
