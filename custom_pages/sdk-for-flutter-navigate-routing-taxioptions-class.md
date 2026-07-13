---
title: "TaxiOptions class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-taxioptions-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/TaxiOptions-class-sidebar.html">

<div>

# <span class="kind-class">TaxiOptions</span> class

</div>

<div class="section desc markdown">

All the options to specify how a taxi route should be calculated.

See, <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.taxi</a>.

**Note:** Specify the optional <a href="sdk-for-flutter-navigate-routing-waypoint-sideofstreethint">Waypoint.sideOfStreetHint</a> to indicate at which side of the street a passenger wants to leave the taxi.

</div>

<div class="section">

Annotations  
- @Deprecated("Will be removed in v4.28.0. Use \`RoutingOptions\` class instead.")

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-routing-taxioptions-taxioptions">TaxiOptions</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-routeOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-routeoptions-class">RouteOptions</a></span> <span class="parameter-name">routeOptions</span>, </span><span id="sdk-for-flutter-navigate-param-textOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-routetextoptions-class">RouteTextOptions</a></span> <span class="parameter-name">textOptions</span>, </span><span id="sdk-for-flutter-navigate-param-avoidanceOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-avoidanceoptions-class">AvoidanceOptions</a></span> <span class="parameter-name">avoidanceOptions</span></span>)</span>  
Creates a new instance.

<span class="name"><a href="sdk-for-flutter-navigate-routing-taxioptions-taxioptions-withdefaults">TaxiOptions.withDefaults</a></span><span class="signature">()</span>  
Creates a new instance.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-routing-taxioptions-allowdrivethroughtaxiroads">allowDriveThroughTaxiRoads</a></span> <span class="signature">↔ bool</span>  
Specifies if a vehicle is allowed to drive through the taxi-only roads and lanes. When set to `false`, it is still allowed on taxi roads after the route start and before the route destination.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-taxioptions-avoidanceoptions">avoidanceOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-avoidanceoptions-class">AvoidanceOptions</a></span>  
Options to specify restrictions for route calculations. By default no restrictions are applied.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-taxioptions-carspecifications">carSpecifications</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-transport-carspecifications-class" class="deprecated">CarSpecifications</a></span>  
Detailed car specifications such as dimensions and weight.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-taxioptions-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-taxioptions-lastcharacteroflicenseplate">lastCharacterOfLicensePlate</a></span> <span class="signature">↔ String?</span>  
Specifies the last character of a vehicle's license plate, typically used to evaluate traffic restrictions in certain environmental or low-emission zones. In cities like Bogotá, Mexico City, or Jakarta, specific license plate digits may be restricted on certain days or in certain areas to reduce congestion and emissions. When this value is provided, the HERE SDK considers it during route calculation to avoid roads or areas where your vehicle may be restricted based on local regulations. Example usage: "7", when the license plate of a vehicle looks like "B-ET-182487".

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-taxioptions-maxspeedonsegments">maxSpeedOnSegments</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-maxspeedonsegment-class">MaxSpeedOnSegment</a></span>\></span></span>  
Segments with restriction on maximum <a href="sdk-for-flutter-navigate-routing-dynamicspeedinfo-basespeedinmeterspersecond">DynamicSpeedInfo.baseSpeedInMetersPerSecond</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-taxioptions-routeoptions">routeOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-routeoptions-class">RouteOptions</a></span>  
Specifies the common route calculation options.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-taxioptions-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-taxioptions-textoptions">textOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-routetextoptions-class">RouteTextOptions</a></span>  
Customize textual content returned from the route calculation, such as localization, format, and unit system.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-taxioptions-tolloptions">tollOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-tolloptions-class">TollOptions</a></span>  
Options to specify how the tolls should be calculated, such as transponders, vehicle category, and emission type.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-routing-taxioptions-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-taxioptions-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-routing-taxioptions-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

