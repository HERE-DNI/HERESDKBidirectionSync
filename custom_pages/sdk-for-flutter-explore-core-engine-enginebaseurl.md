---
title: "EngineBaseURL enum - core.engine library - Dart API"
slug: "sdk-for-flutter-explore-core-engine-enginebaseurl"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/core.engine-library-sidebar.html" data-below-sidebar="core.engine/EngineBaseURL-enum-sidebar.html">

<div>

# <span class="kind-enum">EngineBaseURL</span> enum

</div>

<div class="section desc markdown">

Lists the available HERE SDK endpoints that can be customized with a custom backend base URL.

</div>

## Values

<span class="name">searchEngine</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-core-engine-enginebaseurl">EngineBaseURL</a></span>  
Indicates a `SearchEngine` endpoint. Note that the provided string value will replace the base URL. The endpoint names for this engine are "v1/discover", "v1/geocode", "v1/revgeocode", "v1/autosuggest", "v1/lookup" and "v1/browse". A valid base string value could look like "www.my-company.com". An example of the resulting URL for the first endpoint looks like this: "https://www.my-company.com/v1/discover" appended with query data. You need to ensure that the provided base URL supports all required endpoints.

<span class="name">routingEngine</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-core-engine-enginebaseurl">EngineBaseURL</a></span>  
Indicates a `RoutingEngine` endpoint. Note that the provided string value will replace the base URL. The endpoint names for this engine are "v8/routes", "v8/import". A valid base string value could look like "www.my-company.com". An example of the resulting URL for the first endpoint looks like this: "https://www.my-company.com/v8/routes" appended with query data. You need to ensure that the provided base URL supports all required endpoints.

<span class="name">authentication</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-core-engine-enginebaseurl">EngineBaseURL</a></span>  
Indicates base url for `Authentication`. Note that the provided string value will replace the base URL. The endpoint name for this base url is "oauth2/token". A valid base string value could look like "www.my-company.com". An example of the resulting URL for the endpoint looks like this: "https://www.my-company.com/oauth2/token" appended with query data. You need to ensure that the provided base URL supports required endpoint.

<span class="name">dsProxy</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-core-engine-enginebaseurl">EngineBaseURL</a></span>  
Specifies the endpoint URL for a map catalog. This is only relevant for the Navigate license that uses OCM based map data when a custom catalog configuration should be loaded. By default, the data Service proxy, in short <a href="sdk-for-flutter-explore-core-engine-enginebaseurl">EngineBaseURL.dsProxy</a>, is set to "https://direct.data.api.platform.here.com/direct/v1". When a custom catalog should be used, then the HERE SDK will internally do a lookup request to find out which URL to use to access catalog. In order to bypass this extra request, we recommend to set the URL upfront when initializing the HERE SDK. For example, a valid <a href="sdk-for-flutter-explore-core-engine-enginebaseurl">EngineBaseURL.dsProxy</a> for a custom catalog may look like this: "https://data.api.platform.yourcompany.com/direct/v1". Note that this is not a network proxy setting. If you do not load a custom catalog configuration, you can ignore this setting.

<span class="name">trafficData</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-core-engine-enginebaseurl">EngineBaseURL</a></span>  
Indicates a `Traffic Data` endpoint. Note that the provided string value will replace the base URL. This is only relevant for TrafficEngine. For traffic incident and flow presented in the map view, please use <a href="sdk-for-flutter-explore-core-engine-enginebaseurl">EngineBaseURL.trafficVectorTileService</a>.

<span class="name">trafficVectorTileService</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-core-engine-enginebaseurl">EngineBaseURL</a></span>  
Indicates a `Traffic Vector Tile API` endpoint. Note that the provided string value will replace the base URL. This is only relevant for traffic presented in the map view. For the TrafficEngine, please use <a href="sdk-for-flutter-explore-core-engine-enginebaseurl">EngineBaseURL.trafficData</a>.

The service needs to comply with <https://www.here.com/docs/bundle/traffic-vector-tile-api-v2-api-reference/page/index.html> The endpoint name for this engine is "v2/traffictiles". A valid base string value could look like "www.my-company.com". The resulting URL looks like this: "https://www.my-company.com/v2/traffictiles/{layer}/mc/{z}/{x}/{y}/omv", with concrete tile IDs in {x}, {y}, {z} and {layers} in (flow, incidents). You need to ensure that the provided base URL supports all required endpoints.

<span class="name">rasterTileService</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-core-engine-enginebaseurl">EngineBaseURL</a></span>  
Indicates a `Raster Tile API` endpoint. Note that the provided string value will replace the URL template. A valid URL template value could look like: "https://www.my-company.com/satellite.day/{z}/{x}/{y}/512/jpg"

<span class="name">isolineRoutingEngine</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-core-engine-enginebaseurl">EngineBaseURL</a></span>  
Indicates a `IsolineRoutingEngine` endpoint. Note that the provided string value will replace the base URL. The endpoint names for this engine are "v8/isolines". A valid base string value could look like "www.my-company.com". An example of the resulting URL for the first endpoint looks like this: "https://www.my-company.com/v8/isolines" appended with query data. You need to ensure that the provided base URL supports all required endpoints.

## Properties

<span class="name"><a href="sdk-for-flutter-explore-core-engine-enginebaseurl-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-enginebaseurl-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-enginebaseurl-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-core-engine-enginebaseurl-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-enginebaseurl-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-core-engine-enginebaseurl-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-explore-core-engine-enginebaseurl-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-core-engine-enginebaseurl">EngineBaseURL</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

