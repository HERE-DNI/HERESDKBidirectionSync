---
title: "EVCarOptions class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-evcaroptions-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- EVCarOptions-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/EVCarOptions-class-sidebar.html">

<div>

# <span class="kind-class">EVCarOptions</span> class

</div>

<div class="section desc markdown">

All the options to specify how a route for an electric car should be calculated.

At minimum, a valid <a href="sdk-for-flutter-navigate-routing-evconsumptionmodel-class">EVConsumptionModel</a> must be set or the route calculation will fail.\
Note: <a href="sdk-for-flutter-navigate-routing-evcaroptions-ensurereachability">EVCarOptions.ensureReachability</a> must be `true` to make sure that all stopovers are reachable. For this, charging stations may be added to the route. If <a href="sdk-for-flutter-navigate-routing-evcaroptions-ensurereachability">EVCarOptions.ensureReachability</a> is true, you need to specify the required route options and battery specifications that include the current charge level of the battery (<a href="sdk-for-flutter-navigate-routing-batteryspecifications-initialchargeinkilowatthours">BatterySpecifications.initialChargeInKilowattHours</a>). See the parameter description below for more details.

</div>

<div class="section">

Annotations  
- @Deprecated("Will be removed in v4.28.0. Use \`RoutingOptions\` class instead.")

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-routing-evcaroptions-evcaroptions">EVCarOptions</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-routing-evcaroptions-allowoptions">allowOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-allowoptions-class">AllowOptions</a></span>  
The options explicitly allowed by user for route calculations. By default no options are opt in.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-evcaroptions-avoidanceoptions">avoidanceOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-avoidanceoptions-class">AvoidanceOptions</a></span>  
Options to specify restrictions for route calculations. By default no restrictions are applied.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-evcaroptions-batteryspecifications">batterySpecifications</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-batteryspecifications-class">BatterySpecifications</a></span>  
Parameters that describe the electric vehicle's battery.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-evcaroptions-carspecifications">carSpecifications</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-transport-carspecifications-class" class="deprecated">CarSpecifications</a></span>  
Detailed car specifications such as dimensions and weight.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-evcaroptions-consumptionmodel">consumptionModel</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-evconsumptionmodel-class">EVConsumptionModel</a></span>  
Vehicle specific parameters, which are then used to calculate energy consumption for the vehicle on a given route.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-evcaroptions-ensurereachability">ensureReachability</a></span> <span class="signature">↔ bool</span>  
Ensure that the vehicle does not run out of energy along the way. Requires valid <a href="sdk-for-flutter-navigate-routing-evcaroptions-batteryspecifications">EVCarOptions.batterySpecifications</a>. It also requires that <a href="sdk-for-flutter-navigate-routing-routeoptions-optimizationmode">RouteOptions.optimizationMode</a> = <a href="sdk-for-flutter-navigate-routing-optimizationmode">OptimizationMode.fastest</a>, <a href="sdk-for-flutter-navigate-routing-routeoptions-speedcapinmeterspersecond">RouteOptions.speedCapInMetersPerSecond</a> is not set, and <a href="sdk-for-flutter-navigate-routing-avoidanceoptions-class">AvoidanceOptions</a> is empty. Otherwise, this object is considered invalid. Setting this flag enables calculation of a route optimized for electric vehicles. Charging stations may be added along the route to ensure that the vehicle does not run out of energy along the way. It is especially useful for longer routes, because after all, charging stations are much less common than petrol stations. **Note** An `sdk.routing.RoutingError.INVALID_PARAMETER` is generated when the `sdk.routing.EVCarOptions.ensure_reachability` is set to `true` in case `sdk.routing.RoutingEngine.import_route` is called. Defaults to `false`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-evcaroptions-evmobilityserviceproviderpreferences">evMobilityServiceProviderPreferences</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-evmobilityserviceproviderpreferences-class">EVMobilityServiceProviderPreferences</a></span>  
Defines the preferred E-Mobility Service Providers. The The E-Mobility Service Provider Partner Ids can be received from <https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-roamings.html> An alternative way to get `partnerId` is the `eMobilityServiceProviders.partnerId` as part of `HERE SDK Search`. Maximum number of E-Mobility Service Providers is limited to 10. By default, all providers are used.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-evcaroptions-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-evcaroptions-lastcharacteroflicenseplate">lastCharacterOfLicensePlate</a></span> <span class="signature">↔ String?</span>  
Specifies the last character of a vehicle's license plate, typically used to evaluate traffic restrictions in certain environmental or low-emission zones. In cities like Bogotá, Mexico City, or Jakarta, specific license plate digits may be restricted on certain days or in certain areas to reduce congestion and emissions. When this value is provided, the HERE SDK considers it during route calculation to avoid roads or areas where your vehicle may be restricted based on local regulations. Example usage: "7", when the license plate of a vehicle looks like "B-ET-182487".

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-evcaroptions-maxspeedonsegments">maxSpeedOnSegments</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-maxspeedonsegment-class">MaxSpeedOnSegment</a></span>\></span></span>  
Segments with restriction on maximum <a href="sdk-for-flutter-navigate-routing-dynamicspeedinfo-basespeedinmeterspersecond">DynamicSpeedInfo.baseSpeedInMetersPerSecond</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-evcaroptions-occupantsnumber">occupantsNumber</a></span> <span class="signature">↔ int</span>  
Specifies the number of occupants in the vehicle, including driver, can affect the vehicle's ability to use HOV/carpool restricted lanes. Shouldn't be less than 1 or greater than 255. Defaults to 1.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-evcaroptions-routeoptions">routeOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-routeoptions-class">RouteOptions</a></span>  
Specifies the common route calculation options.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-evcaroptions-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-evcaroptions-textoptions">textOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-routetextoptions-class">RouteTextOptions</a></span>  
Customize textual content returned from the route calculation, such as localization, format, and unit system.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-evcaroptions-tolloptions">tollOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-tolloptions-class">TollOptions</a></span>  
Options to specify how the tolls should be calculated, such as transponders, vehicle category, and emission type.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-routing-evcaroptions-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-evcaroptions-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-routing-evcaroptions-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
