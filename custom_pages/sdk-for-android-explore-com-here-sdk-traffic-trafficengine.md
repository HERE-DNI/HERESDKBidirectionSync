---
title: "TrafficEngine (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-traffic-trafficengine"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.traffic](sdk-for-android-explore-com-here-sdk-traffic-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.NativeBasecom.here.sdk.traffic.TrafficEngine
→ com.here.NativeBase → com.here.sdk.traffic.TrafficEngine

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">TrafficEngine</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Use the TrafficEngine to get information about current traffic flow and
incidents in an area specified by GeoBox , GeoCircle , or GeoCorridor .
Provides optional parameters given in TrafficIncidentsQueryOptions and
TrafficFlowQueryOptions to filter the result. By default, incidents are
localized based on their geographical location. You can override that
behavior by specifying the desired language that should be used for the
incidents description and summary. The resulting traffic data contains
information on incident types such as congestion, construction for road
works, road hazard, road closure, weather updates for road condition,
lane restriction and others. Traffic data is fetched online to get the
most precise and freshest data available. In offline mode, live traffic
data can be fetched using the traffic pass-through features. See
SDKNativeEngine.getPassThroughFeatures()

</div>

</div>

<div class="section summary">
<div id="sdk-for-android-explore-constructor-summary"
  class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Constructor

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-constructor-name even-row-color">

      TrafficEngine()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance of this class.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      TrafficEngine(SDKNativeEngine sdkEngine)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance of this class.

  </div>

  </div>

  </div>

  </div>
<div id="sdk-for-android-explore-method-summary"
  class="section method-summary">

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      lookupIncident(String originalId,
       TrafficIncidentLookupOptions lookupOptions,
       TrafficIncidentLookupCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Asynchronously queries for traffic incident by the original id.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      queryForFlow(GeoBox boxArea,
       TrafficFlowQueryOptions queryOptions,
       TrafficFlowQueryCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Asynchronously queries for traffic flow using a bounding box as a
  filter.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      queryForFlow(GeoCircle circleArea,
       TrafficFlowQueryOptions queryOptions,
       TrafficFlowQueryCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Asynchronously queries for traffic flow using a circle as a filter.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      queryForFlow(GeoCorridor corridorArea,
       TrafficFlowQueryOptions queryOptions,
       TrafficFlowQueryCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Asynchronously queries for traffic flow by a corridor as a filter.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      queryForIncidents(GeoBox boxArea,
       TrafficIncidentsQueryOptions queryOptions,
       TrafficIncidentsQueryCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Asynchronously queries for traffic incidents using a bounding box as a
  filter.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      queryForIncidents(GeoCircle circleArea,
       TrafficIncidentsQueryOptions queryOptions,
       TrafficIncidentsQueryCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Asynchronously queries for traffic incidents using a circle as a
  filter.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      queryForIncidents(GeoCorridor corridorArea,
       TrafficIncidentsQueryOptions queryOptions,
       TrafficIncidentsQueryCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Asynchronously queries for traffic incidents by a corridor as a
  filter.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">
<div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">
<div id="sdk-for-android-explore-<init>()" class="section detail">

    ### TrafficEngine

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">TrafficEngine</span>()
    throws
    <span class="exceptions">[InstantiationErrorException](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")</span>

    </div>

    <div class="block">

    Creates a new instance of this class.

    </div>

    Throws:  
    [`InstantiationErrorException`](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")

    Indicates what went wrong when the instantiation was attempted.

    </div>
<div id="sdk-for-android-explore-<init>(com.here.sdk.core.engine.SDKNativeEngine)"
    class="section detail">

    ### TrafficEngine

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">TrafficEngine</span><span class="parameters">(@NonNull
    [SDKNativeEngine](sdk-for-android-explore-com-here-sdk-core-engine-sdknativeengine "class in com.here.sdk.core.engine") sdkEngine)</span>
    throws
    <span class="exceptions">[InstantiationErrorException](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")</span>

    </div>

    <div class="block">

    Creates a new instance of this class.

    </div>

    Parameters:  
    `sdkEngine` -

    An SDKEngine instance.

    Throws:  
    [`InstantiationErrorException`](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")

    Indicates what went wrong when the instantiation was attempted.

    </div>

  </div>
<div id="sdk-for-android-explore-method-detail"
  class="section method-details">
<div id="sdk-for-android-explore-queryForIncidents(com.here.sdk.core.GeoBox,com.here.sdk.traffic.TrafficIncidentsQueryOptions,com.here.sdk.traffic.TrafficIncidentsQueryCallback)"
    class="section detail">

    ### queryForIncidents

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">queryForIncidents</span><span class="parameters">(@NonNull
    [GeoBox](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core") boxArea,
    @NonNull
    [TrafficIncidentsQueryOptions](sdk-for-android-explore-com-here-sdk-traffic-trafficincidentsqueryoptions "class in com.here.sdk.traffic") queryOptions,
    @NonNull
    [TrafficIncidentsQueryCallback](sdk-for-android-explore-com-here-sdk-traffic-trafficincidentsquerycallback "interface in com.here.sdk.traffic") callback)</span>

    </div>

    <div class="block">

    Asynchronously queries for traffic incidents using a bounding box as
    a filter.

    </div>

    Parameters:  
    `boxArea` -

    The bounding box area to search for traffic incidents. The maximum
    width and height for a bounding box filter is 1 degree.

    `queryOptions` -

    The options which are specific for incidents query.

    `callback` -

    It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>
<div id="sdk-for-android-explore-queryForIncidents(com.here.sdk.core.GeoCircle,com.here.sdk.traffic.TrafficIncidentsQueryOptions,com.here.sdk.traffic.TrafficIncidentsQueryCallback)"
    class="section detail">

    ### queryForIncidents

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">queryForIncidents</span><span class="parameters">(@NonNull
    [GeoCircle](sdk-for-android-explore-com-here-sdk-core-geocircle "class in com.here.sdk.core") circleArea,
    @NonNull
    [TrafficIncidentsQueryOptions](sdk-for-android-explore-com-here-sdk-traffic-trafficincidentsqueryoptions "class in com.here.sdk.traffic") queryOptions,
    @NonNull
    [TrafficIncidentsQueryCallback](sdk-for-android-explore-com-here-sdk-traffic-trafficincidentsquerycallback "interface in com.here.sdk.traffic") callback)</span>

    </div>

    <div class="block">

    Asynchronously queries for traffic incidents using a circle as a
    filter.

    </div>

    Parameters:  
    `circleArea` -

    The circle area to search for traffic incidents. The maximum radius
    of the circle filter is 50000 meters.

    `queryOptions` -

    The options which are specific for incidents query.

    `callback` -

    It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>
<div id="sdk-for-android-explore-queryForIncidents(com.here.sdk.core.GeoCorridor,com.here.sdk.traffic.TrafficIncidentsQueryOptions,com.here.sdk.traffic.TrafficIncidentsQueryCallback)"
    class="section detail">

    ### queryForIncidents

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">queryForIncidents</span><span class="parameters">(@NonNull
    [GeoCorridor](sdk-for-android-explore-com-here-sdk-core-geocorridor "class in com.here.sdk.core") corridorArea,
    @NonNull
    [TrafficIncidentsQueryOptions](sdk-for-android-explore-com-here-sdk-traffic-trafficincidentsqueryoptions "class in com.here.sdk.traffic") queryOptions,
    @NonNull
    [TrafficIncidentsQueryCallback](sdk-for-android-explore-com-here-sdk-traffic-trafficincidentsquerycallback "interface in com.here.sdk.traffic") callback)</span>

    </div>

    <div class="block">

    Asynchronously queries for traffic incidents by a corridor as a
    filter.

    </div>

    Parameters:  
    `corridorArea` -

    The corridor box to search for traffic incidents. The maximum length
    for the corridor is 500000 meters and the maximum
    `GeoCorridor.half_width_in_meters` is 5000 meters. If the number of
    points in corridor is greater than 300 then request is split into
    smaller ones and results are aggregated into single response, this
    will result in multiple requests to the backend. This process does
    not change a shape of the corridor. To reduce number of points in
    the corridor use
    [`PolylineSimplifier`](sdk-for-android-explore-com-here-sdk-core-polylinesimplifier "class in com.here.sdk.core").
    If no `GeoCorridor.half_width_in_meters` is specified, the default
    value is used. The default value is 30 meters.

    `queryOptions` -

    The options which are specific for incidents query.

    `callback` -

    It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>
<div id="sdk-for-android-explore-lookupIncident(java.lang.String,com.here.sdk.traffic.TrafficIncidentLookupOptions,com.here.sdk.traffic.TrafficIncidentLookupCallback)"
    class="section detail">

    ### lookupIncident

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">lookupIncident</span><span class="parameters">(@NonNull
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> originalId,
    @NonNull
    [TrafficIncidentLookupOptions](sdk-for-android-explore-com-here-sdk-traffic-trafficincidentlookupoptions "class in com.here.sdk.traffic") lookupOptions,
    @NonNull
    [TrafficIncidentLookupCallback](sdk-for-android-explore-com-here-sdk-traffic-trafficincidentlookupcallback "interface in com.here.sdk.traffic") callback)</span>

    </div>

    <div class="block">

    Asynchronously queries for traffic incident by the original id. See
    TrafficIncident.getOriginalId() for more information.

    </div>

    Parameters:  
    `originalId` -

    The requested incident original id.

    `lookupOptions` -

    The options which are specific for the incident lookup query.

    `callback` -

    The callback object that will be invoked after the incident lookup
    query. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>
<div id="sdk-for-android-explore-queryForFlow(com.here.sdk.core.GeoBox,com.here.sdk.traffic.TrafficFlowQueryOptions,com.here.sdk.traffic.TrafficFlowQueryCallback)"
    class="section detail">

    ### queryForFlow

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">queryForFlow</span><span class="parameters">(@NonNull
    [GeoBox](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core") boxArea,
    @NonNull
    [TrafficFlowQueryOptions](sdk-for-android-explore-com-here-sdk-traffic-trafficflowqueryoptions "class in com.here.sdk.traffic") queryOptions,
    @NonNull
    [TrafficFlowQueryCallback](sdk-for-android-explore-com-here-sdk-traffic-trafficflowquerycallback "interface in com.here.sdk.traffic") callback)</span>

    </div>

    <div class="block">

    Asynchronously queries for traffic flow using a bounding box as a
    filter. Note: This is a beta release of this feature, so there could
    be a few bugs and unexpected behaviors. Related APIs may change for
    new releases without a deprecation process.

    </div>

    Parameters:  
    `boxArea` -

    The bounding box area to search for traffic flow.

    `queryOptions` -

    The options which are specific for flow query.

    `callback` -

    It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>
<div id="sdk-for-android-explore-queryForFlow(com.here.sdk.core.GeoCircle,com.here.sdk.traffic.TrafficFlowQueryOptions,com.here.sdk.traffic.TrafficFlowQueryCallback)"
    class="section detail">

    ### queryForFlow

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">queryForFlow</span><span class="parameters">(@NonNull
    [GeoCircle](sdk-for-android-explore-com-here-sdk-core-geocircle "class in com.here.sdk.core") circleArea,
    @NonNull
    [TrafficFlowQueryOptions](sdk-for-android-explore-com-here-sdk-traffic-trafficflowqueryoptions "class in com.here.sdk.traffic") queryOptions,
    @NonNull
    [TrafficFlowQueryCallback](sdk-for-android-explore-com-here-sdk-traffic-trafficflowquerycallback "interface in com.here.sdk.traffic") callback)</span>

    </div>

    <div class="block">

    Asynchronously queries for traffic flow using a circle as a filter.
    Note: This is a beta release of this feature, so there could be a
    few bugs and unexpected behaviors. Related APIs may change for new
    releases without a deprecation process.

    </div>

    Parameters:  
    `circleArea` -

    The circle area to search for traffic flow. The maximum radius of
    the circle filter is 50000 meters.

    `queryOptions` -

    The options which are specific for flow query.

    `callback` -

    It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>
<div id="sdk-for-android-explore-queryForFlow(com.here.sdk.core.GeoCorridor,com.here.sdk.traffic.TrafficFlowQueryOptions,com.here.sdk.traffic.TrafficFlowQueryCallback)"
    class="section detail">

    ### queryForFlow

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">queryForFlow</span><span class="parameters">(@NonNull
    [GeoCorridor](sdk-for-android-explore-com-here-sdk-core-geocorridor "class in com.here.sdk.core") corridorArea,
    @NonNull
    [TrafficFlowQueryOptions](sdk-for-android-explore-com-here-sdk-traffic-trafficflowqueryoptions "class in com.here.sdk.traffic") queryOptions,
    @NonNull
    [TrafficFlowQueryCallback](sdk-for-android-explore-com-here-sdk-traffic-trafficflowquerycallback "interface in com.here.sdk.traffic") callback)</span>

    </div>

    <div class="block">

    Asynchronously queries for traffic flow by a corridor as a filter.
    Note: This is a beta release of this feature, so there could be a
    few bugs and unexpected behaviors. Related APIs may change for new
    releases without a deprecation process.

    </div>

    Parameters:  
    `corridorArea` -

    The corridor box to search for traffic flow. The maximum length for
    the corridor is 500000 meters and the maximum
    `GeoCorridor.half_width_in_meters` is 5000 meters. Maximum number of
    points in the corridor is 300. To reduce number of points in the
    corridor use
    [`PolylineSimplifier`](sdk-for-android-explore-com-here-sdk-core-polylinesimplifier "class in com.here.sdk.core").
    If no `GeoCorridor.half_width_in_meters` is specified, the default
    value is used. The default value is 30 meters.

    `queryOptions` -

    The options which are specific for flow query.

    `callback` -

    It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  </div>

</div>

