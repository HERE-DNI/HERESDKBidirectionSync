---
title: "ScooterOptions class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-scooteroptions-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/ScooterOptions-class-sidebar.html">

<div>

# <span class="kind-class">ScooterOptions</span> class

</div>

<div class="section desc markdown">

All the options to specify how a scooter route should be calculated.

</div>

<div class="section">

Annotations  
- @Deprecated("Will be removed in v4.28.0. Use \`RoutingOptions\` class instead.")

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-routing-scooteroptions-scooteroptions">ScooterOptions</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-explore-routing-scooteroptions-allowhighway">allowHighway</a></span> <span class="signature">↔ bool</span>  
Specifies whether scooter is allowed on highway or not. `True` means scooter is allowed to use highways and `false` means otherwise. By default it is set to `false`. Note that there is a similar parameter in <a href="sdk-for-flutter-explore-routing-avoidanceoptions-class">AvoidanceOptions</a>, to disallow highway usage, see <a href="sdk-for-flutter-explore-routing-roadfeatures">RoadFeatures.controlledAccessHighway</a>. As the avoidance options takes precedence, if this parameter is also used, then scooters are not allowed to use highways even if `allowHighway` is set to `true`. However, if no alternative route is possible, the calculated route may use highways. In such a case, a <a href="sdk-for-flutter-explore-routing-sectionnotice-class">SectionNotice</a> will be provided in the related <a href="sdk-for-flutter-explore-routing-section-class">Section</a> to indicate that the highway usage restriction is violated on this route. A few examples:

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-scooteroptions-avoidanceoptions">avoidanceOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-routing-avoidanceoptions-class">AvoidanceOptions</a></span>  
Options to specify restrictions for route calculations. By default no restrictions are applied.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-scooteroptions-enginesizeincubiccentimeters">engineSizeInCubicCentimeters</a></span> <span class="signature">↔ int?</span>  
Engine size of the scooter in cubic centimeters. Shouldn't be less than 1 or greater than 65535. Default value is `null`, which means the scooter route calculation ignores all engine size limits on the road.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-scooteroptions-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-scooteroptions-lastcharacteroflicenseplate">lastCharacterOfLicensePlate</a></span> <span class="signature">↔ String?</span>  
Specifies the last character of a vehicle's license plate, typically used to evaluate traffic restrictions in certain environmental or low-emission zones. In cities like Bogotá, Mexico City, or Jakarta, specific license plate digits may be restricted on certain days or in certain areas to reduce congestion and emissions. When this value is provided, the HERE SDK considers it during route calculation to avoid roads or areas where your vehicle may be restricted based on local regulations. Example usage: "7", when the license plate of a vehicle looks like "B-ET-182487".

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-scooteroptions-maxspeedonsegments">maxSpeedOnSegments</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-routing-maxspeedonsegment-class">MaxSpeedOnSegment</a></span>\></span></span>  
Segments with restriction on maximum <a href="sdk-for-flutter-explore-routing-dynamicspeedinfo-basespeedinmeterspersecond">DynamicSpeedInfo.baseSpeedInMetersPerSecond</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-scooteroptions-occupantsnumber">occupantsNumber</a></span> <span class="signature">↔ int</span>  
Specifies the number of occupants in the vehicle, including driver. Shouldn't be less than 1 or greater than 255. Defaults to 1. This option is only relevant for Japan and will be ignored for other countries.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-scooteroptions-routeoptions">routeOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-routing-routeoptions-class">RouteOptions</a></span>  
Specifies the common route calculation options.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-scooteroptions-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-scooteroptions-textoptions">textOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-routing-routetextoptions-class">RouteTextOptions</a></span>  
Customize textual content returned from the route calculation, such as localization, format, and unit system.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-scooteroptions-tolloptions">tollOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-routing-tolloptions-class">TollOptions</a></span>  
Options to specify how the tolls should be calculated, such as transponders, vehicle category, and emission type.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-routing-scooteroptions-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-scooteroptions-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-routing-scooteroptions-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

