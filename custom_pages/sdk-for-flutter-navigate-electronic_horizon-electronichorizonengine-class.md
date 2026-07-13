---
title: "ElectronicHorizonEngine class - electronic_horizon library - Dart API"
slug: "sdk-for-flutter-navigate-electronic_horizon-electronichorizonengine-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ElectronicHorizonEngine-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="electronic_horizon/electronic_horizon-library-sidebar.html" data-below-sidebar="electronic_horizon/ElectronicHorizonEngine-class-sidebar.html">

<div>

# <span class="kind-class">ElectronicHorizonEngine</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Provides an electronic horizon engine that continuously predicts the road network ahead of the vehicle by using detailed map data, including road topography that is currently out of sight.

You can subscribe to electronic horizon updates based on position updates by using <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonlistener-class">ElectronicHorizonListener</a>. For more information about sub path levels, see <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonoptions-lookaheaddistancesinmeters">ElectronicHorizonOptions.lookAheadDistancesInMeters</a>.

The electronic horizon engine uses map-matched locations and can optionally use a <a href="sdk-for-flutter-navigate-routing-route-class">Route</a> to improve the most-preferred path (MPP).

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonengine-electronichorizonengine-withoptionsandroutepathevaluator">ElectronicHorizonEngine.WithOptionsAndRoutePathEvaluator</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-WithOptionsAndRoutePathEvaluator-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span>, </span><span id="sdk-for-flutter-navigate-WithOptionsAndRoutePathEvaluator-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonoptions-class">ElectronicHorizonOptions</a></span> <span class="parameter-name">options</span>, </span><span id="sdk-for-flutter-navigate-WithOptionsAndRoutePathEvaluator-param-transportMode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode</a></span> <span class="parameter-name">transportMode</span>, </span><span id="sdk-for-flutter-navigate-WithOptionsAndRoutePathEvaluator-param-route" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-route-class">Route</a>?</span> <span class="parameter-name">route</span></span>)</span>  
Creates a new instance of <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonengine-class">ElectronicHorizonEngine</a>.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonengine-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonengine-route">route</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-route-class">Route</a>?</span>  
The instance of <a href="sdk-for-flutter-navigate-routing-route-class">Route</a> that is being used by <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonengine-class">ElectronicHorizonEngine</a>. You can override this property to rebuild the electronic horizon based on a different route. Gets the instance of <a href="sdk-for-flutter-navigate-routing-route-class">Route</a> or `null` if <a href="sdk-for-flutter-navigate-routing-route-class">Route</a> is not set.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonengine-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonengine-addelectronichorizonlistener">addElectronicHorizonListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-addElectronicHorizonListener-param-electronicHorizonListener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonlistener-class">ElectronicHorizonListener</a></span> <span class="parameter-name">electronicHorizonListener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds an <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonlistener-class">ElectronicHorizonListener</a> to the subscription list.

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonengine-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonengine-removeelectronichorizonlistener">removeElectronicHorizonListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-removeElectronicHorizonListener-param-electronicHorizonListener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonlistener-class">ElectronicHorizonListener</a></span> <span class="parameter-name">electronicHorizonListener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes an <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonlistener-class">ElectronicHorizonListener</a> from the subscription list.

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonengine-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonengine-update">update</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-update-param-mapMatchedLocation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-mapmatchedlocation-class">MapMatchedLocation</a></span> <span class="parameter-name">mapMatchedLocation</span></span>) <span class="returntype parameter">→ void</span> </span>  
Updates the electronic horizon paths based on the provided map-matched location.

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonengine-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
