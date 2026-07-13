---
title: "PrivateBusOptions class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-privatebusoptions-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PrivateBusOptions-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/PrivateBusOptions-class-sidebar.html">

<div>

# <span class="kind-class">PrivateBusOptions</span> class

</div>

<div class="section desc markdown">

All the options to specify how a private bus route should be calculated.

</div>

<div class="section">

Annotations  
- @Deprecated("Will be removed in v4.28.0. Use \`RoutingOptions\` class instead.")

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-routing-privatebusoptions-privatebusoptions">PrivateBusOptions</a></span><span class="signature">()</span>  
Creates a new instance.

## Properties

<span class="name"><a href="sdk-for-flutter-explore-routing-privatebusoptions-allowoptions">allowOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-routing-allowoptions-class">AllowOptions</a></span>  
The options explicitly allowed by user for route calculations. By default no options are opt in.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-privatebusoptions-avoidanceoptions">avoidanceOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-routing-avoidanceoptions-class">AvoidanceOptions</a></span>  
Options to specify restrictions for route calculations. By default no restrictions are applied.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-privatebusoptions-busspecifications">busSpecifications</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-transport-busspecifications-class" class="deprecated">BusSpecifications</a></span>  
Detailed bus specifications such as dimensions and weight.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-privatebusoptions-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-privatebusoptions-lastcharacteroflicenseplate">lastCharacterOfLicensePlate</a></span> <span class="signature">↔ String?</span>  
Specifies the last character of a vehicle's license plate, typically used to evaluate traffic restrictions in certain environmental or low-emission zones. In cities like Bogotá, Mexico City, or Jakarta, specific license plate digits may be restricted on certain days or in certain areas to reduce congestion and emissions. When this value is provided, the HERE SDK considers it during route calculation to avoid roads or areas where your vehicle may be restricted based on local regulations. Example usage: "7", when the license plate of a vehicle looks like "B-ET-182487".

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-privatebusoptions-maxspeedonsegments">maxSpeedOnSegments</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-routing-maxspeedonsegment-class">MaxSpeedOnSegment</a></span>\></span></span>  
Segments with restriction on maximum baseSpeed.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-privatebusoptions-occupantsnumber">occupantsNumber</a></span> <span class="signature">↔ int</span>  
Specifies the number of occupants in the vehicle, including driver, can affect the vehicle's ability to use HOV/carpool restricted lanes. Shouldn't be less than 1 or greater than 255. Defaults to 1.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-privatebusoptions-routeoptions">routeOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-routing-routeoptions-class">RouteOptions</a></span>  
Specifies the common route calculation options.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-privatebusoptions-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-privatebusoptions-textoptions">textOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-routing-routetextoptions-class">RouteTextOptions</a></span>  
Customize textual content returned from the route calculation, such as localization, format, and unit system.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-privatebusoptions-tolloptions">tollOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-routing-tolloptions-class">TollOptions</a></span>  
Options to specify how the tolls should be calculated, such as transponders, vehicle category, and emission type.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-routing-privatebusoptions-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-privatebusoptions-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-routing-privatebusoptions-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
