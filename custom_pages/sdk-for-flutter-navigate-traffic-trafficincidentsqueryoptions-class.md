---
title: "TrafficIncidentsQueryOptions class - traffic library - Dart API"
slug: "sdk-for-flutter-navigate-traffic-trafficincidentsqueryoptions-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrafficIncidentsQueryOptions-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="traffic/traffic-library-sidebar.html" data-below-sidebar="traffic/TrafficIncidentsQueryOptions-class-sidebar.html">

<div>

# <span class="kind-class">TrafficIncidentsQueryOptions</span> class

</div>

<div class="section desc markdown">

The options to specify how incidents should be queried.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficincidentsqueryoptions-trafficincidentsqueryoptions">TrafficIncidentsQueryOptions</a></span><span class="signature">()</span>  
Creates a new instance with default values.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficincidentsqueryoptions-earlieststarttime">earliestStartTime</a></span> <span class="signature">↔ DateTime?</span>  
The earliest start time of incidents to be queried. If the value is null filtering by the earliest start time is not applied.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficincidentsqueryoptions-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficincidentsqueryoptions-impactfilter">impactFilter</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-traffic-trafficincidentimpact">TrafficIncidentImpact</a></span>\></span></span>  
The list of incident impacts to be queried. If the list is empty, all incident impacts will be queried.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficincidentsqueryoptions-languagecode">languageCode</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-languagecode">LanguageCode</a>?</span>  
The language code of the query. It's the expected language of fields <a href="sdk-for-flutter-navigate-traffic-trafficincidentbase-description">TrafficIncidentBase.description</a> and <a href="sdk-for-flutter-navigate-traffic-trafficincident-summary">TrafficIncident.summary</a> in the relevant response. However, the language code doesn't impact on <a href="sdk-for-flutter-navigate-traffic-trafficlocation-description">TrafficLocation.description</a>. If the language code is null or not supported then response fields are expected in the original language of the country that the incident belongs to.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficincidentsqueryoptions-latestendtime">latestEndTime</a></span> <span class="signature">↔ DateTime?</span>  
The latest end time of incidents to be queried. If the value is null filtering by the latest end time is not applied.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficincidentsqueryoptions-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficincidentsqueryoptions-typefilter">typeFilter</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-traffic-trafficincidenttype">TrafficIncidentType</a></span>\></span></span>  
The list of incident types to be queried. If the list is empty, all types will be queried.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficincidentsqueryoptions-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficincidentsqueryoptions-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficincidentsqueryoptions-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
