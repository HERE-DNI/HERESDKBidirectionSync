---
title: "TrafficEngine class - traffic library - Dart API"
slug: "sdk-for-flutter-navigate-traffic-trafficengine-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrafficEngine-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="traffic/traffic-library-sidebar.html" data-below-sidebar="traffic/TrafficEngine-class-sidebar.html">

<div>

# <span class="kind-class">TrafficEngine</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Use the TrafficEngine to get information about current traffic flow and incidents in an area specified by <a href="sdk-for-flutter-navigate-core-geobox-class">GeoBox</a>, <a href="sdk-for-flutter-navigate-core-geocircle-class">GeoCircle</a>, or <a href="sdk-for-flutter-navigate-core-geocorridor-class">GeoCorridor</a>.

Provides optional parameters given in <a href="sdk-for-flutter-navigate-traffic-trafficincidentsqueryoptions-class">TrafficIncidentsQueryOptions</a> and <a href="sdk-for-flutter-navigate-traffic-trafficflowqueryoptions-class">TrafficFlowQueryOptions</a> to filter the result.

By default, incidents are localized based on their geographical location. You can override that behavior by specifying the desired language that should be used for the incidents description and summary.

The resulting traffic data contains information on incident types such as congestion, construction for road works, road hazard, road closure, weather updates for road condition, lane restriction and others.

Traffic data is fetched online to get the most precise and freshest data available. In offline mode, live traffic data can be fetched using the traffic pass-through features. See <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-passthroughfeatures">SDKNativeEngine.passThroughFeatures</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficengine-trafficengine">TrafficEngine</a></span><span class="signature">()</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficengine-trafficengine-withsdkengine">TrafficEngine.withSdkEngine</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withSdkEngine-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span></span>)</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficengine-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficengine-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficengine-lookupincident">lookupIncident</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-lookupIncident-param-originalId" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">originalId</span>, </span><span id="sdk-for-flutter-navigate-lookupIncident-param-lookupOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-traffic-trafficincidentlookupoptions-class">TrafficIncidentLookupOptions</a></span> <span class="parameter-name">lookupOptions</span>, </span><span id="sdk-for-flutter-navigate-lookupIncident-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-traffic-trafficincidentlookupcallback">TrafficIncidentLookupCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Asynchronously queries for traffic incident by the original id.

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficengine-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficengine-queryforflowinbox">queryForFlowInBox</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-queryForFlowInBox-param-boxArea" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geobox-class">GeoBox</a></span> <span class="parameter-name">boxArea</span>, </span><span id="sdk-for-flutter-navigate-queryForFlowInBox-param-queryOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-traffic-trafficflowqueryoptions-class">TrafficFlowQueryOptions</a></span> <span class="parameter-name">queryOptions</span>, </span><span id="sdk-for-flutter-navigate-queryForFlowInBox-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-traffic-trafficflowquerycallback">TrafficFlowQueryCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Asynchronously queries for traffic flow using a bounding box as a filter.

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficengine-queryforflowincircle">queryForFlowInCircle</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-queryForFlowInCircle-param-circleArea" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocircle-class">GeoCircle</a></span> <span class="parameter-name">circleArea</span>, </span><span id="sdk-for-flutter-navigate-queryForFlowInCircle-param-queryOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-traffic-trafficflowqueryoptions-class">TrafficFlowQueryOptions</a></span> <span class="parameter-name">queryOptions</span>, </span><span id="sdk-for-flutter-navigate-queryForFlowInCircle-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-traffic-trafficflowquerycallback">TrafficFlowQueryCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Asynchronously queries for traffic flow using a circle as a filter.

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficengine-queryforflowincorridor">queryForFlowInCorridor</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-queryForFlowInCorridor-param-corridorArea" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocorridor-class">GeoCorridor</a></span> <span class="parameter-name">corridorArea</span>, </span><span id="sdk-for-flutter-navigate-queryForFlowInCorridor-param-queryOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-traffic-trafficflowqueryoptions-class">TrafficFlowQueryOptions</a></span> <span class="parameter-name">queryOptions</span>, </span><span id="sdk-for-flutter-navigate-queryForFlowInCorridor-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-traffic-trafficflowquerycallback">TrafficFlowQueryCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Asynchronously queries for traffic flow by a corridor as a filter.

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficengine-queryforincidentsinbox">queryForIncidentsInBox</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-queryForIncidentsInBox-param-boxArea" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geobox-class">GeoBox</a></span> <span class="parameter-name">boxArea</span>, </span><span id="sdk-for-flutter-navigate-queryForIncidentsInBox-param-queryOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-traffic-trafficincidentsqueryoptions-class">TrafficIncidentsQueryOptions</a></span> <span class="parameter-name">queryOptions</span>, </span><span id="sdk-for-flutter-navigate-queryForIncidentsInBox-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-traffic-trafficincidentsquerycallback">TrafficIncidentsQueryCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Asynchronously queries for traffic incidents using a bounding box as a filter.

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficengine-queryforincidentsincircle">queryForIncidentsInCircle</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-queryForIncidentsInCircle-param-circleArea" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocircle-class">GeoCircle</a></span> <span class="parameter-name">circleArea</span>, </span><span id="sdk-for-flutter-navigate-queryForIncidentsInCircle-param-queryOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-traffic-trafficincidentsqueryoptions-class">TrafficIncidentsQueryOptions</a></span> <span class="parameter-name">queryOptions</span>, </span><span id="sdk-for-flutter-navigate-queryForIncidentsInCircle-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-traffic-trafficincidentsquerycallback">TrafficIncidentsQueryCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Asynchronously queries for traffic incidents using a circle as a filter.

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficengine-queryforincidentsincorridor">queryForIncidentsInCorridor</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-queryForIncidentsInCorridor-param-corridorArea" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocorridor-class">GeoCorridor</a></span> <span class="parameter-name">corridorArea</span>, </span><span id="sdk-for-flutter-navigate-queryForIncidentsInCorridor-param-queryOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-traffic-trafficincidentsqueryoptions-class">TrafficIncidentsQueryOptions</a></span> <span class="parameter-name">queryOptions</span>, </span><span id="sdk-for-flutter-navigate-queryForIncidentsInCorridor-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-traffic-trafficincidentsquerycallback">TrafficIncidentsQueryCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Asynchronously queries for traffic incidents by a corridor as a filter.

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficengine-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficengine-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
