---
title: "RefreshRouteOptions class abstract"
slug: "sdk-for-flutter-navigate-routing-refreshrouteoptions-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RefreshRouteOptions-class.html -->


<div>
<h1>RefreshRouteOptions class abstract</h1></div>

<p>The options to specify how to refresh an already calculated route identified by a <a href="sdk-for-flutter-navigate-routing-routehandle-class">RouteHandle</a>.</p>
<p>All the
options that may result in a new route shape are ignored as no new route is calculated. Instead, only the data that
accompanies a route, such as traffic information, can be refreshed. Therefore, the following route options are ignored:
<a href="sdk-for-flutter-navigate-routing-routeoptions-alternatives">RouteOptions.alternatives</a>, <a href="sdk-for-flutter-navigate-routing-routeoptions-arrivaltime">RouteOptions.arrivalTime</a>, and <a href="sdk-for-flutter-navigate-routing-routeoptions-optimizationmode">RouteOptions.optimizationMode</a>.
If new <a href="sdk-for-flutter-navigate-routing-avoidanceoptions-class">AvoidanceOptions</a> are specified, they are ignored as well and instead new <a href="sdk-for-flutter-navigate-routing-sectionnotice-class">SectionNotice</a>'s
are generated that indicate where the requested <a href="sdk-for-flutter-navigate-routing-avoidanceoptions-class">AvoidanceOptions</a> are violated. Note that when
<a href="sdk-for-flutter-navigate-routing-evcaroptions-ensurereachability">EVCarOptions.ensureReachability</a> is set to true, the route refresh request will fail as this option
is incompatible with a fixed route shape.
If any of the ignored options are important, consider calculating a new route instead.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>


<ul><li>Annotations</li></ul>


<h2>Constructors</h2>
<ul><li><a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-refreshrouteoptions-withbicycleoptions">RefreshRouteOptions.withBicycleOptions</a></li><li><a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-refreshrouteoptions-withbusoptions">RefreshRouteOptions.withBusOptions</a></li><li><a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-refreshrouteoptions-withcaroptions">RefreshRouteOptions.withCarOptions</a></li><li><a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-refreshrouteoptions-withevcaroptions">RefreshRouteOptions.withEVCarOptions</a></li><li><a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-refreshrouteoptions-withevtruckoptions">RefreshRouteOptions.withEVTruckOptions</a></li><li><a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-refreshrouteoptions-withpedestrianoptions">RefreshRouteOptions.withPedestrianOptions</a></li><li><a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-refreshrouteoptions-withprivatebusoptions">RefreshRouteOptions.withPrivateBusOptions</a></li><li><a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-refreshrouteoptions-withscooteroptions">RefreshRouteOptions.withScooterOptions</a></li><li><a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-refreshrouteoptions-withtaxioptions">RefreshRouteOptions.withTaxiOptions</a></li><li><a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-refreshrouteoptions-withtransportmode">RefreshRouteOptions.withTransportMode</a></li><li><a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-refreshrouteoptions-withtruckoptions">RefreshRouteOptions.withTruckOptions</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-hashcode">hashCode</a></li><li><a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-nosuchmethod">noSuchMethod</a></li><li><a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
