---
title: "RefreshRouteOptions class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-refreshrouteoptions-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/RefreshRouteOptions-class-sidebar.html">

<div>

# <span class="kind-class">RefreshRouteOptions</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

The options to specify how to refresh an already calculated route identified by a <a href="sdk-for-flutter-navigate-routing-routehandle-class">RouteHandle</a>.

All the options that may result in a new route shape are ignored as no new route is calculated. Instead, only the data that accompanies a route, such as traffic information, can be refreshed. Therefore, the following route options are ignored: <a href="sdk-for-flutter-navigate-routing-routeoptions-alternatives">RouteOptions.alternatives</a>, <a href="sdk-for-flutter-navigate-routing-routeoptions-arrivaltime">RouteOptions.arrivalTime</a>, and <a href="sdk-for-flutter-navigate-routing-routeoptions-optimizationmode">RouteOptions.optimizationMode</a>. If new <a href="sdk-for-flutter-navigate-routing-avoidanceoptions-class">AvoidanceOptions</a> are specified, they are ignored as well and instead new <a href="sdk-for-flutter-navigate-routing-sectionnotice-class">SectionNotice</a>'s are generated that indicate where the requested <a href="sdk-for-flutter-navigate-routing-avoidanceoptions-class">AvoidanceOptions</a> are violated. Note that when <a href="sdk-for-flutter-navigate-routing-evcaroptions-ensurereachability">EVCarOptions.ensureReachability</a> is set to true, the route refresh request will fail as this option is incompatible with a fixed route shape. If any of the ignored options are important, consider calculating a new route instead.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section">

Annotations  
- @Deprecated("Will be removed in v4.28.0. Use the \`RoutingOptions\` class instead.")

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-refreshrouteoptions-withbicycleoptions">RefreshRouteOptions.withBicycleOptions</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withBicycleOptions-param-bicycleOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-bicycleoptions-class" class="deprecated">BicycleOptions</a></span> <span class="parameter-name">bicycleOptions</span></span>)</span>  
Constructs a RefreshRouteOptions object with <a href="sdk-for-flutter-navigate-routing-bicycleoptions-class" class="deprecated">BicycleOptions</a>.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-refreshrouteoptions-withbusoptions">RefreshRouteOptions.withBusOptions</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withBusOptions-param-busOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-busoptions-class" class="deprecated">BusOptions</a></span> <span class="parameter-name">busOptions</span></span>)</span>  
Constructs a RefreshRouteOptions object with <a href="sdk-for-flutter-navigate-routing-busoptions-class" class="deprecated">BusOptions</a>.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-refreshrouteoptions-withcaroptions">RefreshRouteOptions.withCarOptions</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withCarOptions-param-carOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-caroptions-class" class="deprecated">CarOptions</a></span> <span class="parameter-name">carOptions</span></span>)</span>  
Constructs a RefreshRouteOptions object with <a href="sdk-for-flutter-navigate-routing-caroptions-class" class="deprecated">CarOptions</a>.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-refreshrouteoptions-withevcaroptions">RefreshRouteOptions.withEVCarOptions</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withEVCarOptions-param-evCarOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-evcaroptions-class" class="deprecated">EVCarOptions</a></span> <span class="parameter-name">evCarOptions</span></span>)</span>  
Constructs a RefreshRouteOptions object with <a href="sdk-for-flutter-navigate-routing-evcaroptions-class" class="deprecated">EVCarOptions</a>.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-refreshrouteoptions-withevtruckoptions">RefreshRouteOptions.withEVTruckOptions</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withEVTruckOptions-param-evTruckOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-evtruckoptions-class" class="deprecated">EVTruckOptions</a></span> <span class="parameter-name">evTruckOptions</span></span>)</span>  
Constructs a RefreshRouteOptions object with <a href="sdk-for-flutter-navigate-routing-evtruckoptions-class" class="deprecated">EVTruckOptions</a>.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-refreshrouteoptions-withpedestrianoptions">RefreshRouteOptions.withPedestrianOptions</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withPedestrianOptions-param-pedestrianOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-pedestrianoptions-class" class="deprecated">PedestrianOptions</a></span> <span class="parameter-name">pedestrianOptions</span></span>)</span>  
Constructs a RefreshRouteOptions object with <a href="sdk-for-flutter-navigate-routing-pedestrianoptions-class" class="deprecated">PedestrianOptions</a>.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-refreshrouteoptions-withprivatebusoptions">RefreshRouteOptions.withPrivateBusOptions</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withPrivateBusOptions-param-privateBusOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-privatebusoptions-class" class="deprecated">PrivateBusOptions</a></span> <span class="parameter-name">privateBusOptions</span></span>)</span>  
Constructs a RefreshRouteOptions object with <a href="sdk-for-flutter-navigate-routing-privatebusoptions-class" class="deprecated">PrivateBusOptions</a>.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-refreshrouteoptions-withscooteroptions">RefreshRouteOptions.withScooterOptions</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withScooterOptions-param-scooterOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-scooteroptions-class" class="deprecated">ScooterOptions</a></span> <span class="parameter-name">scooterOptions</span></span>)</span>  
Constructs a RefreshRouteOptions object with <a href="sdk-for-flutter-navigate-routing-scooteroptions-class" class="deprecated">ScooterOptions</a>.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-refreshrouteoptions-withtaxioptions">RefreshRouteOptions.withTaxiOptions</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withTaxiOptions-param-taxiOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-taxioptions-class" class="deprecated">TaxiOptions</a></span> <span class="parameter-name">taxiOptions</span></span>)</span>  
Constructs a RefreshRouteOptions object with <a href="sdk-for-flutter-navigate-routing-taxioptions-class" class="deprecated">TaxiOptions</a>.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-refreshrouteoptions-withtransportmode">RefreshRouteOptions.withTransportMode</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withTransportMode-param-transportMode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode</a></span> <span class="parameter-name">transportMode</span></span>)</span>  
Constructs a RefreshRouteOptions object with <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode</a>.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-refreshrouteoptions-withtruckoptions">RefreshRouteOptions.withTruckOptions</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withTruckOptions-param-truckOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-truckoptions-class" class="deprecated">TruckOptions</a></span> <span class="parameter-name">truckOptions</span></span>)</span>  
Constructs a RefreshRouteOptions object with <a href="sdk-for-flutter-navigate-routing-truckoptions-class" class="deprecated">TruckOptions</a>.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

