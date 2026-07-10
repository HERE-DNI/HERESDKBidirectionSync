---
title: "DynamicRoutingEngine (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengine"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-package-summary">com.here.sdk.trafficawarenavigation</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.trafficawarenavigation.DynamicRoutingEngine → com.here.NativeBase com.here.sdk.trafficawarenavigation.DynamicRoutingEngine → com.here.sdk.trafficawarenavigation.DynamicRoutingEngine

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">DynamicRoutingEngine</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

This class queries the HERE routing backend to find routes with less traffic and therefore an earlier remaining estimated time of arrival. DynamicRoutingEngine polls the HERE routing backend periodically to find the best new route out of a given initial route. For initial route calculation it is recommended to use the RoutingEngine as it already requests traffic-optimized routes. When a better route is found, it is recommended to follow these steps to set the new route: Stop the DynamicRoutingEngine . Update the currently active Navigator instance with the newly found route. Restart the DynamicRoutingEngine . This should be done outside of the onBetterRouteFound() callback. For both DynamicRoutingEngine and RoutingEngine , the resulting routes are optimized based on speed flow changes such as traffic jams, street closures or road accidents. To get the best result, it is recommended to not specify the RouteOptions.departureTime as then the current time is used by default. The poll interval is defined by DynamicRoutingEngineOptions.pollInterval and triggered by updateCurrentLocation(com.here.sdk.navigation.MapMatchedLocation, int) .

</div>

</div>

- <div id="sdk-for-android-navigate-nested-class-summary" class="section nested-class-summary">

  <div class="caption">

  Nested Classes

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Class

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  `static enum `

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengine-starterror" class="type-name-link" title="enum class in com.here.sdk.trafficawarenavigation"><code>DynamicRoutingEngine.StartError</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Start error

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final class `

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengine-startexception" class="type-name-link" title="class in com.here.sdk.trafficawarenavigation"><code>DynamicRoutingEngine.StartException</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Start exception

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-summary" class="section constructor-summary">

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

      DynamicRoutingEngine ( SDKNativeEngine sdkEngine, DynamicRoutingEngineOptions options)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance of this class.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      DynamicRoutingEngine ( DynamicRoutingEngineOptions options)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance of this class.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div id="sdk-for-android-navigate-method-summary-table">

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      start ( RouteHandle routeHandle, List < Waypoint > waypoints, RefreshRouteOptions refreshRouteOptions, DynamicRoutingListener listener)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      start ( RouteHandle routeHandle, List < Waypoint > waypoints, RoutingOptions routingOptions, DynamicRoutingListener listener)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Starts polling the HERE backend services to find a better route, as defined by the DynamicRoutingEngineOptions .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      start ( Route route, DynamicRoutingListener listener)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Starts polling the HERE backend services to find a better route, as defined by the DynamicRoutingEngineOptions.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      stop ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Stops polling the HERE backend services.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      updateCurrentLocation ( MapMatchedLocation mapMatchedLocation,
       int sectionIndex)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Updates the current location.

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

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-com-here-sdk-trafficawarenavigation-DynamicRoutingEngineOptions" class="section detail">

    ### DynamicRoutingEngine

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">DynamicRoutingEngine</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengineoptions" title="class in com.here.sdk.trafficawarenavigation">DynamicRoutingEngineOptions</a> options)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Creates a new instance of this class.

    </div>

    Parameters:  
    `options` -

    The options defining the behavior of the <a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengine" title="class in com.here.sdk.trafficawarenavigation">`DynamicRoutingEngine`</a>.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    when the engine was not initialized properly.

    </div>

  - <div id="sdk-for-android-navigate-init-com-here-sdk-core-engine-SDKNativeEngine-com-here-sdk-trafficawarenavigation-DynamicRoutingEngineOptions" class="section detail">

    ### DynamicRoutingEngine

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">DynamicRoutingEngine</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine, @Nullable <a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengineoptions" title="class in com.here.sdk.trafficawarenavigation">DynamicRoutingEngineOptions</a> options)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Creates a new instance of this class.

    </div>

    Parameters:  
    `sdkEngine` -

    Instance of an existing SDKEngine.

    `options` -

    The options defining the behavior of the <a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengine" title="class in com.here.sdk.trafficawarenavigation">`DynamicRoutingEngine`</a>.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    when the engine was not initialized properly.

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-start-com-here-sdk-routing-Route-com-here-sdk-trafficawarenavigation-DynamicRoutingListener" class="section detail">

    ### start

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">start</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing">Route</a> route, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutinglistener" title="interface in com.here.sdk.trafficawarenavigation">DynamicRoutingListener</a> listener)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengine-startexception" title="class in com.here.sdk.trafficawarenavigation">DynamicRoutingEngine.StartException</a></span>

    </div>

    <div class="block">

    Starts polling the HERE backend services to find a better route, as defined by the DynamicRoutingEngineOptions. Note: The engine will be internally stopped, if it was started before. Therefore, it is not necessary to stop the engine before starting it again.

    </div>

    Parameters:  
    `route` -

    The route to be refreshed. The route must contain a <a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing">`RouteHandle`</a>, therefore the route must have been requested with <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions#enableRouteHandle">`RouteOptions.enableRouteHandle`</a> set to `true`. The information to calculate new routes will be extracted from the provided route parameter. If more information from the original waypoints is important besides their location, consider to use one of the overloaded methods instead.

    `listener` -

    The listener to receive the events.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengine-startexception" title="class in com.here.sdk.trafficawarenavigation">`DynamicRoutingEngine.StartException`</a> -

    when the passed parameter are invalid.

    </div>

  - <div id="sdk-for-android-navigate-start-com-here-sdk-routing-RouteHandle-java-util-List-com-here-sdk-routing-RefreshRouteOptions-com-here-sdk-trafficawarenavigation-DynamicRoutingListener" class="section detail">

    ### start

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> </span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">start</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing">RouteHandle</a> routeHandle, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint" title="class in com.here.sdk.routing">Waypoint</a>\> waypoints, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-refreshrouteoptions" title="class in com.here.sdk.routing">RefreshRouteOptions</a> refreshRouteOptions, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutinglistener" title="interface in com.here.sdk.trafficawarenavigation">DynamicRoutingListener</a> listener)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengine-startexception" title="class in com.here.sdk.trafficawarenavigation">DynamicRoutingEngine.StartException</a></span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the

        start()

    method with RoutingOptions parameter instead.
    </p>

    </div>

    </div>

    <div class="block">

    Starts polling the HERE backend services to find a better route, as defined by the DynamicRoutingEngineOptions . Note: The engine will be internally stopped, if it was started before. Therefore, it is not necessary to stop the engine before starting it again.

    </div>

    Parameters:  
    `routeHandle` -

    The route handle from the HERE routing backend.

    `waypoints` -

    Allows to specify detailed information on the waypoints of the route. This parameter can be useful, when additional information needs to be specified besides the coordinates - as the coordinates can be retrieved from the contained <a href="sdk-for-android-navigate-com-here-sdk-routing-routeplace" title="class in com.here.sdk.routing">`RoutePlace`</a> that are already contained in the <a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing">`RouteHandle`</a> parameter.

    `refreshRouteOptions` -

    The options for the route calculation.

    `listener` -

    The listener to receive the events.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengine-startexception" title="class in com.here.sdk.trafficawarenavigation">`DynamicRoutingEngine.StartException`</a> -

    when the passed parameter are invalid.

    </div>

  - <div id="sdk-for-android-navigate-start-com-here-sdk-routing-RouteHandle-java-util-List-com-here-sdk-routing-RoutingOptions-com-here-sdk-trafficawarenavigation-DynamicRoutingListener" class="section detail">

    ### start

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">start</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing">RouteHandle</a> routeHandle, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint" title="class in com.here.sdk.routing">Waypoint</a>\> waypoints, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions" title="class in com.here.sdk.routing">RoutingOptions</a> routingOptions, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutinglistener" title="interface in com.here.sdk.trafficawarenavigation">DynamicRoutingListener</a> listener)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengine-startexception" title="class in com.here.sdk.trafficawarenavigation">DynamicRoutingEngine.StartException</a></span>

    </div>

    <div class="block">

    Starts polling the HERE backend services to find a better route, as defined by the DynamicRoutingEngineOptions . Note: The engine will be internally stopped, if it was started before. Therefore, it is not necessary to stop the engine before starting it again.

    </div>

    Parameters:  
    `routeHandle` -

    The route handle from the HERE routing backend.

    `waypoints` -

    Allows to specify detailed information on the waypoints of the route. This parameter can be useful, when additional information needs to be specified besides the coordinates - as the coordinates can be retrieved from the contained <a href="sdk-for-android-navigate-com-here-sdk-routing-routeplace" title="class in com.here.sdk.routing">`RoutePlace`</a> that are already contained in the <a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing">`RouteHandle`</a> parameter.

    `routingOptions` -

    The options for the route calculation.

    `listener` -

    The listener to receive the events.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengine-startexception" title="class in com.here.sdk.trafficawarenavigation">`DynamicRoutingEngine.StartException`</a> -

    when the passed parameter are invalid.

    </div>

  - <div id="sdk-for-android-navigate-stop" class="section detail">

    ### stop

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">stop</span>()

    </div>

    <div class="block">

    Stops polling the HERE backend services. Note: The engine is not automatically stopped when the destination is reached. Therefore, it is recommended to stop the engine when the destination was reached.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-updateCurrentLocation-com-here-sdk-navigation-MapMatchedLocation-int" class="section detail">

    ### updateCurrentLocation

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">updateCurrentLocation</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-mapmatchedlocation" title="class in com.here.sdk.navigation">MapMatchedLocation</a> mapMatchedLocation, int sectionIndex)</span>

    </div>

    <div class="block">

    Updates the current location. This location will be used as new starting point when the next DynamicRoutingEngineOptions.pollInterval is reached and a new route is requested. If an immediate route update is needed, consider to use the RoutingEngine instead. All subsequently calculated routes used for the ETA calculation will start from this location. The location needs to lie on the route or a RoutingError will be issued.

    </div>

    Parameters:  
    `mapMatchedLocation` -

    The last known location. It is recommended to use a <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigablelocation#mapMatchedLocation">`NavigableLocation.mapMatchedLocation`</a> as the driver is expected to be on a road.

    `sectionIndex` -

    The current section from <a href="sdk-for-android-navigate-com-here-sdk-navigation-routeprogress#sectionIndex">`RouteProgress.sectionIndex`</a>.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

