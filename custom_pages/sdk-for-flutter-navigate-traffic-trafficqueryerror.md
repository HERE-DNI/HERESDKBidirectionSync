---
title: "TrafficQueryError enum - traffic library - Dart API"
slug: "sdk-for-flutter-navigate-traffic-trafficqueryerror"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrafficQueryError.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="traffic/traffic-library-sidebar.html" data-below-sidebar="traffic/TrafficQueryError-enum-sidebar.html">

<div>

# <span class="kind-enum">TrafficQueryError</span> enum

</div>

<div class="section desc markdown">

Represents various errors that could occur from a traffic queries.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Values

<span class="name">failedToRetrieveResult</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-traffic-trafficqueryerror">TrafficQueryError</a></span>  
Failed to retrieve result since the server has returned an error or invalid result that couldn't be processed correctly.

<span class="name">authenticationFailed</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-traffic-trafficqueryerror">TrafficQueryError</a></span>  
Incident query/flow operation is not authenticated. Check your credentials.

<span class="name">forbidden</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-traffic-trafficqueryerror">TrafficQueryError</a></span>  
The provided credentials don't give access to the requested resource.

<span class="name">serverUnreachable</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-traffic-trafficqueryerror">TrafficQueryError</a></span>  
Server unreachable.

<span class="name">timedOut</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-traffic-trafficqueryerror">TrafficQueryError</a></span>  
The request timed out.

<span class="name">offline</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-traffic-trafficqueryerror">TrafficQueryError</a></span>  
The device has no internet connection.

<span class="name">httpError</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-traffic-trafficqueryerror">TrafficQueryError</a></span>  
Network request error.

<span class="name">invalidIn</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-traffic-trafficqueryerror">TrafficQueryError</a></span>  
Invalid "in" parameter: wrong type, missing or invalid "in".

<span class="name">invalidGeometry</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-traffic-trafficqueryerror">TrafficQueryError</a></span>  
Invalid geometry: bounding box, circle, or corridor.

<span class="name">invalidIncident</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-traffic-trafficqueryerror">TrafficQueryError</a></span>  
Invalid incident ID, type, earliestStartTime or latestEndTime.

<span class="name">incidentIdNotFound</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-traffic-trafficqueryerror">TrafficQueryError</a></span>  
Incident ID is not found in the system.

<span class="name">invalidFilterOptions</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-traffic-trafficqueryerror">TrafficQueryError</a></span>  
One or several filter options are invalid.

<span class="name">invalidParameter</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-traffic-trafficqueryerror">TrafficQueryError</a></span>  
One or more input parameters in the query is not valid.

<span class="name">internalError</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-traffic-trafficqueryerror">TrafficQueryError</a></span>  
Internal error.

<span class="name">operationCancelled</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-traffic-trafficqueryerror">TrafficQueryError</a></span>  
Operation cancelled.

<span class="name">proxyAuthenticationFailed</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-traffic-trafficqueryerror">TrafficQueryError</a></span>  
Proxy is not authenticated. Check your proxy credentials.

<span class="name">proxyServerUnreachable</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-traffic-trafficqueryerror">TrafficQueryError</a></span>  
Proxy server unreachable. Error indicates a problem with a proxy server's accessibility or connectivity.

<span class="name">badRequest</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-traffic-trafficqueryerror">TrafficQueryError</a></span>  
Bad request. Error indicates server could not understand or process the request made by the client because the request itself was malformed or incorrect.

<span class="name">tooManyRequests</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-traffic-trafficqueryerror">TrafficQueryError</a></span>  
Server has received an excessive number of requests from client within a specific timeframe and client should slow down or wait before sending more requests.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficqueryerror-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficqueryerror-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficqueryerror-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficqueryerror-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficqueryerror-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficqueryerror-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficqueryerror-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-traffic-trafficqueryerror">TrafficQueryError</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
