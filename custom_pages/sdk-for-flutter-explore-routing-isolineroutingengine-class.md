---
title: "IsolineRoutingEngine class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-isolineroutingengine-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/IsolineRoutingEngine-class-sidebar.html">

<div>

# <span class="kind-class">IsolineRoutingEngine</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Use the IsolineRoutingEngine to calculate a reachable area from a center point.

The calculation is done asynchronously and requires an online connection.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineroutingengine-isolineroutingengine">IsolineRoutingEngine</a></span><span class="signature">()</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineroutingengine-isolineroutingengine-withconnectionsettings">IsolineRoutingEngine.withConnectionSettings</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withConnectionSettings-param-connectionSettings" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-routingconnectionsettings-class">RoutingConnectionSettings</a></span> <span class="parameter-name">connectionSettings</span></span>)</span>  
Creates a new instance of RoutingEngine.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineroutingengine-isolineroutingengine-withsdkengine">IsolineRoutingEngine.withSdkEngine</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withSdkEngine-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span></span>)</span>  
Creates a new instance of IsolineRoutingEngine.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineroutingengine-isolineroutingengine-withsdkengineandconnectionsettings">IsolineRoutingEngine.withSdkEngineAndConnectionSettings</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withSdkEngineAndConnectionSettings-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span>, </span><span id="sdk-for-flutter-explore-withSdkEngineAndConnectionSettings-param-connectionSettings" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-routingconnectionsettings-class">RoutingConnectionSettings</a></span> <span class="parameter-name">connectionSettings</span></span>)</span>  
Creates a new instance of RoutingEngine.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineroutingengine-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineroutingengine-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineroutingengine-calculateisoline">calculateIsoline</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-calculateIsoline-param-center" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-waypoint-class">Waypoint</a></span> <span class="parameter-name">center</span>, </span><span id="sdk-for-flutter-explore-calculateIsoline-param-isolineOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-isolineoptions-class">IsolineOptions</a></span> <span class="parameter-name">isolineOptions</span>, </span><span id="sdk-for-flutter-explore-calculateIsoline-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-calculateisolinecallback">CalculateIsolineCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Asynchronously calculates isolines to indicate the reachable area from a center point.

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineroutingengine-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineroutingengine-setcustomoption">setCustomOption</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-setCustomOption-param-name" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">name</span>, </span><span id="sdk-for-flutter-explore-setCustomOption-param-value" class="parameter"><span class="type-annotation">String?</span> <span class="parameter-name">value</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError</a>?</span> </span>  
Sets a custom option for routing backend queries.

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineroutingengine-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-routing-isolineroutingengine-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

