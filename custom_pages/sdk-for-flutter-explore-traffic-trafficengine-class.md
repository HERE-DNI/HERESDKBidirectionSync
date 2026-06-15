---
title: "TrafficEngine class abstract"
slug: "sdk-for-flutter-explore-traffic-trafficengine-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrafficEngine-class.html -->


<div>
<h1>TrafficEngine class abstract</h1></div>

<p>Use the TrafficEngine to get information about current traffic flow and incidents in an area
specified by <a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a>, <a href="sdk-for-flutter-explore-core-geocircle-class">GeoCircle</a>, or <a href="sdk-for-flutter-explore-core-geocorridor-class">GeoCorridor</a>.</p>
<p>Provides optional parameters given in <a href="sdk-for-flutter-explore-traffic-trafficincidentsqueryoptions-class">TrafficIncidentsQueryOptions</a> and <a href="sdk-for-flutter-explore-traffic-trafficflowqueryoptions-class">TrafficFlowQueryOptions</a> to filter the result.</p>
<p>By default, incidents are localized based on their geographical
location. You can override that behavior by specifying the
desired language that should be used for the incidents description and summary.</p>
<p>The resulting traffic data contains information on incident
types such as congestion, construction for road works, road hazard,
road closure, weather updates for road condition, lane restriction
and others.</p>
<p>Traffic data is fetched online to get the most precise and freshest data available.
In offline mode, live traffic data can be fetched using the traffic pass-through features.
See <a href="sdk-for-flutter-explore-core-engine-sdknativeengine-passthroughfeatures">SDKNativeEngine.passThroughFeatures</a></p>


<h2>Constructors</h2>
<ul><li><a href="sdk-for-flutter-explore-traffic-trafficengine-trafficengine">TrafficEngine</a></li><li><a href="sdk-for-flutter-explore-traffic-trafficengine-trafficengine-withsdkengine">TrafficEngine.withSdkEngine</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="sdk-for-flutter-explore-traffic-trafficengine-hashcode">hashCode</a></li><li><a href="sdk-for-flutter-explore-traffic-trafficengine-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="sdk-for-flutter-explore-traffic-trafficengine-lookupincident">lookupIncident</a></li><li><a href="sdk-for-flutter-explore-traffic-trafficengine-nosuchmethod">noSuchMethod</a></li><li><a href="sdk-for-flutter-explore-traffic-trafficengine-queryforflowinbox">queryForFlowInBox</a></li><li><a href="sdk-for-flutter-explore-traffic-trafficengine-queryforflowincircle">queryForFlowInCircle</a></li><li><a href="sdk-for-flutter-explore-traffic-trafficengine-queryforflowincorridor">queryForFlowInCorridor</a></li><li><a href="sdk-for-flutter-explore-traffic-trafficengine-queryforincidentsinbox">queryForIncidentsInBox</a></li><li><a href="sdk-for-flutter-explore-traffic-trafficengine-queryforincidentsincircle">queryForIncidentsInCircle</a></li><li><a href="sdk-for-flutter-explore-traffic-trafficengine-queryforincidentsincorridor">queryForIncidentsInCorridor</a></li><li><a href="sdk-for-flutter-explore-traffic-trafficengine-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="sdk-for-flutter-explore-traffic-trafficengine-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
