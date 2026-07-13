---
title: "EVTruckOptions class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-evtruckoptions-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/EVTruckOptions-class-sidebar.html">

<div>

# <span class="kind-class">EVTruckOptions</span> class

</div>

<div class="section desc markdown">

All the options to specify how a route for an electric truck should be calculated.

</div>

<div class="section">

Annotations  
- @Deprecated("Will be removed in v4.28.0. Use \`RoutingOptions\` class instead.")

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-routing-evtruckoptions-evtruckoptions">EVTruckOptions</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-routing-evtruckoptions-allowoptions">allowOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-allowoptions-class">AllowOptions</a></span>  
The options explicitly allowed by user for route calculations. By default no options are opt in.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-evtruckoptions-avoidanceoptions">avoidanceOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-avoidanceoptions-class">AvoidanceOptions</a></span>  
Options to specify restrictions for route calculations. By default no restrictions are applied.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-evtruckoptions-avoidedtruckroadtypes">avoidedTruckRoadTypes</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-transport-truckroadtype">TruckRoadType</a></span>\></span></span>  
Specifies a list of avoided truck road types for vehicle. Refer to <a href="sdk-for-flutter-navigate-transport-truckroadtype">TruckRoadType</a> for the available options.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-evtruckoptions-consumptionmodel">consumptionModel</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-evconsumptionmodel-class">EVConsumptionModel</a></span>  
Vehicle specific parameters, which are then used to calculate energy consumption for the vehicle on a given route.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-evtruckoptions-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-evtruckoptions-hazardousmaterials">hazardousMaterials</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-transport-hazardousmaterial">HazardousMaterial</a></span>\></span></span>  
Specifies a list of hazardous materials shipped in the vehicle. Refer to <a href="sdk-for-flutter-navigate-transport-hazardousmaterial">HazardousMaterial</a> for the available options.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-evtruckoptions-lastcharacteroflicenseplate">lastCharacterOfLicensePlate</a></span> <span class="signature">↔ String?</span>  
Specifies the last character of a vehicle's license plate, typically used to evaluate traffic restrictions in certain environmental or low-emission zones. In cities like Bogotá, Mexico City, or Jakarta, specific license plate digits may be restricted on certain days or in certain areas to reduce congestion and emissions. When this value is provided, the HERE SDK considers it during route calculation to avoid roads or areas where your vehicle may be restricted based on local regulations. Example usage: "7", when the license plate of a vehicle looks like "B-ET-182487".

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-evtruckoptions-linktunnelcategory">linkTunnelCategory</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-transport-tunnelcategory">TunnelCategory</a>?</span>  
Specifies the tunnel categories to restrict certain route links. The route will pass only through tunnels of a less strict category. Refer to <a href="sdk-for-flutter-navigate-transport-tunnelcategory">TunnelCategory</a> for the available options.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-evtruckoptions-maxspeedonsegments">maxSpeedOnSegments</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-maxspeedonsegment-class">MaxSpeedOnSegment</a></span>\></span></span>  
Segments with restriction on maximum <a href="sdk-for-flutter-navigate-routing-dynamicspeedinfo-basespeedinmeterspersecond">DynamicSpeedInfo.baseSpeedInMetersPerSecond</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-evtruckoptions-occupantsnumber">occupantsNumber</a></span> <span class="signature">↔ int</span>  
Specifies the number of occupants in the vehicle, including driver, can affect the vehicle's ability to use HOV/carpool restricted lanes. Shouldn't be less than 1 or greater than 255. Defaults to 1.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-evtruckoptions-routeoptions">routeOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-routeoptions-class">RouteOptions</a></span>  
Specifies the common route calculation options.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-evtruckoptions-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-evtruckoptions-textoptions">textOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-routetextoptions-class">RouteTextOptions</a></span>  
Customize textual content returned from the route calculation, such as localization, format, and unit system.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-evtruckoptions-tolloptions">tollOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-tolloptions-class">TollOptions</a></span>  
Options to specify how the tolls should be calculated, such as transponders, vehicle category, and emission type.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-evtruckoptions-truckspecifications">truckSpecifications</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-transport-truckspecifications-class" class="deprecated">TruckSpecifications</a></span>  
Detailed truck specifications such as dimensions and weight.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-routing-evtruckoptions-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-evtruckoptions-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-routing-evtruckoptions-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

