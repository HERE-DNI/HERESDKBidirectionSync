---
title: "SearchError enum - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-searcherror"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/SearchError-enum-sidebar.html">

<div>

# <span class="kind-enum">SearchError</span> enum

</div>

<div class="section desc markdown">

Specifies possible errors that may result from a search query.

</div>

## Values

<span class="name">authenticationFailed</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-searcherror">SearchError</a></span>  
Search operation is not authenticated. Check your credentials.

<span class="name">maxItemsOutOfRange</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-searcherror">SearchError</a></span>  
Should be in the range \[1, 100\].

<span class="name">parsingError</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-searcherror">SearchError</a></span>  
Error while parsing response data.

<span class="name">noResultsFound</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-searcherror">SearchError</a></span>  
No results found.

<span class="name">httpError</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-searcherror">SearchError</a></span>  
Network request error.

<span class="name">serverUnreachable</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-searcherror">SearchError</a></span>  
Server unreachable.

<span class="name">forbidden</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-searcherror">SearchError</a></span>  
The credentials given do not provide access to the resource requested.

<span class="name">exceededUsageLimit</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-searcherror">SearchError</a></span>  
Credentials exceeded the allowed requests limit.

<span class="name">operationFailed</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-searcherror">SearchError</a></span>  
Operation failed due to an internal error.

<span class="name">operationCancelled</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-searcherror">SearchError</a></span>  
Operation cancelled.

<span class="name">timedOut</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-searcherror">SearchError</a></span>  
The request timed out.

<span class="name">offline</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-searcherror">SearchError</a></span>  
The device does not have an internet connection.

<span class="name">queryTooLong</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-searcherror">SearchError</a></span>  
Query is too long, max. size is 300 characters.

<span class="name">filterTooLong</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-searcherror">SearchError</a></span>  
Filter is too long, max. size is 300 characters.

<span class="name">proxyAuthenticationFailed</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-searcherror">SearchError</a></span>  
Proxy is not authenticated. Check your proxy credentials.

<span class="name">proxyServerUnreachable</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-searcherror">SearchError</a></span>  
Proxy server unreachable.

<span class="name">queryEmpty</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-searcherror">SearchError</a></span>  
Empty query

<span class="name">invalidArea</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-searcherror">SearchError</a></span>  
Box or circle area of query is invalid

<span class="name">filterEmpty</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-searcherror">SearchError</a></span>  
Filter is empty

<span class="name">invalidCorridorPolyline</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-searcherror">SearchError</a></span>  
Corridor area polyline size is less than 2 points

<span class="name">invalidUrl</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-searcherror">SearchError</a></span>  
Url is invalid

<span class="name">invalidCustomOptionFormat</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-searcherror">SearchError</a></span>  
Custom options are set in an invalid format in the query

<span class="name">invalidTruckClass</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-searcherror">SearchError</a></span>  
Light truck class is passed in the filter

<span class="name">badRequest</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-searcherror">SearchError</a></span>  
Bad network request

<span class="name">mapNotReady</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-searcherror">SearchError</a></span>  
Offline map data is incomplete for the requested operation. Regions are not downloaded or are in the `Pending` state.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

<span class="name">layersNotDownloaded</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-search-searcherror">SearchError</a></span>  
Downloaded regions missing <a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.offlineSearchGlobal</a> feature. Update or redownload regions with enabled feature.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-search-searcherror-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-searcherror-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-searcherror-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-search-searcherror-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-searcherror-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-search-searcherror-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-navigate-search-searcherror-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-searcherror">SearchError</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

