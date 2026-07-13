---
title: "DynamicRoutingListener class - trafficawarenavigation library - Dart API"
slug: "sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="trafficawarenavigation/trafficawarenavigation-library-sidebar.html" data-below-sidebar="trafficawarenavigation/DynamicRoutingListener-class-sidebar.html">

<div>

# <span class="kind-class">DynamicRoutingListener</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive notifications about the new route via the <a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-class">DynamicRoutingEngine</a>.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-dynamicroutinglistener">DynamicRoutingListener</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-onBetterRouteFoundLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onBetterRouteFoundLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-route-class">Route</a></span>, </span><span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">int</span>, </span><span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">int</span></span>), </span><span id="sdk-for-flutter-navigate-param-onRoutingErrorLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onRoutingErrorLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-routingerror">RoutingError</a></span></span>)</span>)</span>  
This abstract class should be implemented in order to receive notifications about the new route via the <a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-class">DynamicRoutingEngine</a>.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-onbetterroutefound">onBetterRouteFound</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-onBetterRouteFound-param-newRoute" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-route-class">Route</a></span> <span class="parameter-name">newRoute</span>, </span><span id="sdk-for-flutter-navigate-onBetterRouteFound-param-etaDifferenceInSeconds" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">etaDifferenceInSeconds</span>, </span><span id="sdk-for-flutter-navigate-onBetterRouteFound-param-distanceDifferenceInMeters" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">distanceDifferenceInMeters</span></span>) <span class="returntype parameter">→ void</span> </span>  
This event is issued when a better route could be found, as defined by <a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-class">DynamicRoutingEngineOptions</a>.

<span class="name"><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-onroutingerror">onRoutingError</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-onRoutingError-param-routingError" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-routingerror">RoutingError</a></span> <span class="parameter-name">routingError</span></span>) <span class="returntype parameter">→ void</span> </span>  
This event is issued when an error occurred.

<span class="name"><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

