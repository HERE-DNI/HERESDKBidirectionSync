---
title: "Route (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-route"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.routing.Route → com.here.NativeBase com.here.sdk.routing.Route → com.here.sdk.routing.Route

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">Route</span> <span class="extends-implements">extends [NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

A route is a path through a road network over which someone travels. Note: Each Section of a route contains a list of SectionNotice objects that describe potential issues after the route was calculated. If the list is non-empty, it is recommended to evaluate possible violations against the requested route options and reject the route if deemed necessary.

</div>

</div>

- <div id="sdk-for-android-explore-method-summary" class="section method-summary">

  <div id="sdk-for-android-explore-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `[`Route`](sdk-for-android-explore-com-here-sdk-routing-route "class in com.here.sdk.routing")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      deserialize (byte[] routeData)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Creates route from the given binary data.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`GeoBox`](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getBoundingBox ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the closest rectangular area where this route fits in.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getConsumptionInKilowattHours ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets estimated net energy consumption (in kWh) if the transportation mode used for this route is an electric vehicle.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`Duration`](sdk-for-android-explore-com-here-time-duration "class in com.here.time")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getDuration ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the estimated time in seconds needed to travel along this route, including real-time traffic delays if available.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`GeoPolyline`](sdk-for-android-explore-com-here-sdk-core-geopolyline "class in com.here.sdk.core")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getGeometry ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the GeoPolyline object representing the polyline of this route.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`LanguageCode`](sdk-for-android-explore-com-here-sdk-core-languagecode "enum class in com.here.sdk.core")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getLanguage ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the language requested for all textual information related to this route.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getLengthInMeters ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the length of this route in meters.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`OptimizationMode`](sdk-for-android-explore-com-here-sdk-routing-optimizationmode "enum class in com.here.sdk.routing")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getOptimizationMode ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the optimization mode requested for route calculation.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`[`RouteRailwayCrossing`](sdk-for-android-explore-com-here-sdk-routing-routerailwaycrossing "class in com.here.sdk.routing")`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getRailwayCrossings ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets railway crossings.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TransportMode`](sdk-for-android-explore-com-here-sdk-transport-transportmode "enum class in com.here.sdk.transport")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getRequestedTransportMode ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the transport mode requested for route calculation.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`RouteHandle`](sdk-for-android-explore-com-here-sdk-routing-routehandle "class in com.here.sdk.routing")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getRouteHandle ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the route handle of this route.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`[`RouteLabel`](sdk-for-android-explore-com-here-sdk-routing-routelabel "class in com.here.sdk.routing")`>`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getRouteLabels ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets route labels.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`RoutingOptions`](sdk-for-android-explore-com-here-sdk-routing-routingoptions "class in com.here.sdk.routing")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getRoutingOptions ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the options used to calculate this route.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`[`Section`](sdk-for-android-explore-com-here-sdk-routing-section "class in com.here.sdk.routing")`>`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getSections ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the sections that make up this route.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`Duration`](sdk-for-android-explore-com-here-time-duration "class in com.here.time")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTrafficDelay ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the estimated time in seconds spent in traffic along this route.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static byte[]`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      serialize ( Route route)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Serializes given route to a binary data.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-serialize-com-here-sdk-routing-Route" class="section detail">

    ### serialize

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public static</span> <span class="return-type">byte\[\]</span> <span class="element-name">serialize</span><wbr></wbr><span class="parameters">(@NonNull [Route](sdk-for-android-explore-com-here-sdk-routing-route "class in com.here.sdk.routing") route)</span>

    </div>

    <div class="block">

    Serializes given route to a binary data. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    </div>

    Parameters:  
    `route` -

    The route which should be serialized.

    Returns:  
    The binary data of the route.

    </div>

  - <div id="sdk-for-android-explore-deserialize-byte" class="section detail">

    ### deserialize

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public static</span> <span class="return-type">[Route](sdk-for-android-explore-com-here-sdk-routing-route "class in com.here.sdk.routing")</span> <span class="element-name">deserialize</span><wbr></wbr><span class="parameters">(@NonNull byte\[\] routeData)</span>

    </div>

    <div class="block">

    Creates route from the given binary data. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    </div>

    Parameters:  
    `routeData` -

    The binary of a serialized route.

    Returns:  
    The route object restored from the binary data.

    </div>

  - <div id="sdk-for-android-explore-getSections" class="section detail">

    ### getSections

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Section](sdk-for-android-explore-com-here-sdk-routing-section "class in com.here.sdk.routing")\></span> <span class="element-name">getSections</span>()

    </div>

    <div class="block">

    Gets the sections that make up this route.

    </div>

    Returns:  
    The sections that make up this route.

    </div>

  - <div id="sdk-for-android-explore-getGeometry" class="section detail">

    ### getGeometry

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[GeoPolyline](sdk-for-android-explore-com-here-sdk-core-geopolyline "class in com.here.sdk.core")</span> <span class="element-name">getGeometry</span>()

    </div>

    <div class="block">

    Gets the GeoPolyline object representing the polyline of this route. It may not contain the original coordinates specified in the request for a route.

    </div>

    Returns:  
    The [`GeoPolyline`](sdk-for-android-explore-com-here-sdk-core-geopolyline "class in com.here.sdk.core") object representing the polyline of this route. It may not contain the original coordinates specified in the request for a route.

    </div>

  - <div id="sdk-for-android-explore-getBoundingBox" class="section detail">

    ### getBoundingBox

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[GeoBox](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core")</span> <span class="element-name">getBoundingBox</span>()

    </div>

    <div class="block">

    Gets the closest rectangular area where this route fits in.

    </div>

    Returns:  
    The closest rectangular area where this route fits in.

    </div>

  - <div id="sdk-for-android-explore-getLengthInMeters" class="section detail">

    ### getLengthInMeters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getLengthInMeters</span>()

    </div>

    <div class="block">

    Gets the length of this route in meters.

    </div>

    Returns:  
    The length of this route in meters.

    </div>

  - <div id="sdk-for-android-explore-getLanguage" class="section detail">

    ### getLanguage

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[LanguageCode](sdk-for-android-explore-com-here-sdk-core-languagecode "enum class in com.here.sdk.core")</span> <span class="element-name">getLanguage</span>()

    </div>

    <div class="block">

    Gets the language requested for all textual information related to this route.

    </div>

    Returns:  
    Indicates the language requested for all textual information related to this route.

    </div>

  - <div id="sdk-for-android-explore-getOptimizationMode" class="section detail">

    ### getOptimizationMode

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[OptimizationMode](sdk-for-android-explore-com-here-sdk-routing-optimizationmode "enum class in com.here.sdk.routing")</span> <span class="element-name">getOptimizationMode</span>()

    </div>

    <div class="block">

    Gets the optimization mode requested for route calculation.

    </div>

    Returns:  
    The optimization mode requested for route calculation.

    </div>

  - <div id="sdk-for-android-explore-getRequestedTransportMode" class="section detail">

    ### getRequestedTransportMode

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[TransportMode](sdk-for-android-explore-com-here-sdk-transport-transportmode "enum class in com.here.sdk.transport")</span> <span class="element-name">getRequestedTransportMode</span>()

    </div>

    <div class="block">

    Gets the transport mode requested for route calculation.

    </div>

    Returns:  
    The transport mode requested for route calculation.

    </div>

  - <div id="sdk-for-android-explore-getConsumptionInKilowattHours" class="section detail">

    ### getConsumptionInKilowattHours

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">getConsumptionInKilowattHours</span>()

    </div>

    <div class="block">

    Gets estimated net energy consumption (in kWh) if the transportation mode used for this route is an electric vehicle. Note that it can be negative due to energy recuperation.

    </div>

    Returns:  
    Estimated net energy consumption (in kWh) if the transportation mode used for this route is an electric vehicle. Note that it can be negative due to energy recuperation.

    </div>

  - <div id="sdk-for-android-explore-getRouteHandle" class="section detail">

    ### getRouteHandle

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type">[RouteHandle](sdk-for-android-explore-com-here-sdk-routing-routehandle "class in com.here.sdk.routing")</span> <span class="element-name">getRouteHandle</span>()

    </div>

    <div class="block">

    Gets the route handle of this route. Note that it is provided only if RouteOptions.enableRouteHandle is set before route calculation.

    </div>

    Returns:  
    The route handle of this route. Note that it is provided only if [`RouteOptions.enableRouteHandle`](sdk-for-android-explore-com-here-sdk-routing-routeoptions#enableRouteHandle) is set before route calculation.

    </div>

  - <div id="sdk-for-android-explore-getDuration" class="section detail">

    ### getDuration

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time")</span> <span class="element-name">getDuration</span>()

    </div>

    <div class="block">

    Gets the estimated time in seconds needed to travel along this route, including real-time traffic delays if available.

    </div>

    Returns:  
    The estimated time in seconds needed to travel along this route, including real-time traffic delays if available.

    </div>

  - <div id="sdk-for-android-explore-getTrafficDelay" class="section detail">

    ### getTrafficDelay

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[Duration](sdk-for-android-explore-com-here-time-duration "class in com.here.time")</span> <span class="element-name">getTrafficDelay</span>()

    </div>

    <div class="block">

    Gets the estimated time in seconds spent in traffic along this route. Negative values indicate that the route can be traversed faster than usual.

    </div>

    Returns:  
    The estimated time in seconds spent in traffic along this route. Negative values indicate that the route can be traversed faster than usual.

    </div>

  - <div id="sdk-for-android-explore-getRoutingOptions" class="section detail">

    ### getRoutingOptions

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type">[RoutingOptions](sdk-for-android-explore-com-here-sdk-routing-routingoptions "class in com.here.sdk.routing")</span> <span class="element-name">getRoutingOptions</span>()

    </div>

    <div class="block">

    Gets the options used to calculate this route.

    </div>

    Returns:  
    The set of options used to calculate the route.

    </div>

  - <div id="sdk-for-android-explore-getRailwayCrossings" class="section detail">

    ### getRailwayCrossings

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[RouteRailwayCrossing](sdk-for-android-explore-com-here-sdk-routing-routerailwaycrossing "class in com.here.sdk.routing")\></span> <span class="element-name">getRailwayCrossings</span>()

    </div>

    <div class="block">

    Gets railway crossings. Railway crossing information is only available for routes created with the online RoutingEngine .

    </div>

    Returns:  
    Collection of railway crossings along the route.

    </div>

  - <div id="sdk-for-android-explore-getRouteLabels" class="section detail">

    ### getRouteLabels

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[RouteLabel](sdk-for-android-explore-com-here-sdk-routing-routelabel "class in com.here.sdk.routing")\></span> <span class="element-name">getRouteLabels</span>()

    </div>

    <div class="block">

    Gets route labels. The main street names or route numbers through which the route is going to pass that differentiate it from other alternatives routes. The labels are ordered by importance based on how much time the route spends on each road segment, not by traversal sequence. This helps users quickly identify and distinguish between different route alternatives when alternative routes have been quested via RouteOptions .

    </div>

    Returns:  
    A collection containing a maximum of 2 `RouteLabel` instances for the route. It will return an empty list if no labels are available.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

