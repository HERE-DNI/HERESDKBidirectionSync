---
title: "TransitRoutingEngine class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-transitroutingengine-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TransitRoutingEngine-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/TransitRoutingEngine-class-sidebar.html">

<div>

# <span class="kind-class">TransitRoutingEngine</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Use the TransitRoutingEngine to calculate a public transit route from A to B with a number of waypoints in between.

Route calculation is done asynchronously and requires an online connection. The resulting route contains various information such as the polyline, route length in meters, estimated time to traverse along the route and maneuver data.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-routing-transitroutingengine-transitroutingengine">TransitRoutingEngine</a></span><span class="signature">()</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-transitroutingengine-transitroutingengine-withsdkengine">TransitRoutingEngine.withSdkEngine</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withSdkEngine-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span></span>)</span>  
Creates a new instance of TransitRoutingEngine.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-explore-routing-transitroutingengine-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-transitroutingengine-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-routing-transitroutingengine-calculateroute">calculateRoute</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-calculateRoute-param-startingPoint" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-transitwaypoint-class">TransitWaypoint</a></span> <span class="parameter-name">startingPoint</span>, </span><span id="sdk-for-flutter-explore-calculateRoute-param-destination" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-transitwaypoint-class">TransitWaypoint</a></span> <span class="parameter-name">destination</span>, </span><span id="sdk-for-flutter-explore-calculateRoute-param-routeOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-transitrouteoptions-class">TransitRouteOptions</a></span> <span class="parameter-name">routeOptions</span>, </span><span id="sdk-for-flutter-explore-calculateRoute-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-calculateroutecallback">CalculateRouteCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Asynchronously calculates a public transit route from the origin to the destination.

<span class="name"><a href="sdk-for-flutter-explore-routing-transitroutingengine-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-transitroutingengine-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-routing-transitroutingengine-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
