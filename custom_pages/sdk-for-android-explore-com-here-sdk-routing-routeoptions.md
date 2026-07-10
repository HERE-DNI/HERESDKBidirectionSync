---
title: "RouteOptions (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-routeoptions"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-com-here-sdk-routing-package-summary">com.here.sdk.routing</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.routing.RouteOptions → com.here.sdk.routing.RouteOptions

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">RouteOptions</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

The options to specify how the route will be calculated.

</div>

</div>

- <div id="sdk-for-android-explore-field-summary" class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Field

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  `int`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#alternatives" class="member-name-link"><code>alternatives</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Maximum number of alternative routes that will be calculated, in addition to the best one.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util"><code>Date</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#arrivalTime" class="member-name-link"><code>arrivalTime</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Optional time when travel is expected to end.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util"><code>Date</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#departureTime" class="member-name-link"><code>departureTime</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Optional time when travel is expected to start.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#enableRouteHandle" class="member-name-link"><code>enableRouteHandle</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  A flag that indicates whether the resulting route should contain a RouteHandle .

  </div>

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#enableRouteLabels" class="member-name-link"><code>enableRouteLabels</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Specifies whether route labels should be included in the route response.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#enableTolls" class="member-name-link"><code>enableTolls</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  A flag that indicates whether the resulting route Section.getTolls() properties should contain tolls data.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">`OptimizationMode`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#optimizationMode" class="member-name-link"><code>optimizationMode</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The optimization mode to be used for route calculation.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#optimizeWaypointsOrder" class="member-name-link"><code>optimizeWaypointsOrder</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  A flag that indicates whether the order of waypoints that is passed to calculateRoute() should be optimized in the best order.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#speedCapInMetersPerSecond" class="member-name-link"><code>speedCapInMetersPerSecond</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Specifies the maximum speed in meters per second, which the user wishes not to exceed.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-trafficoptimizationmode" title="enum class in com.here.sdk.routing">`TrafficOptimizationMode`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#trafficOptimizationMode" class="member-name-link"><code>trafficOptimizationMode</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The traffic optimization mode to be used for route calculation.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-constructor-summary" class="section constructor-summary">

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

      RouteOptions ()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      RouteOptions ( OptimizationMode optimizationMode)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      RouteOptions ( OptimizationMode optimizationMode,
       int alternatives)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      RouteOptions ( OptimizationMode optimizationMode,
       int alternatives, Date departureTime)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      RouteOptions ( OptimizationMode optimizationMode,
       int alternatives, Date departureTime, Date arrivalTime)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      RouteOptions ( OptimizationMode optimizationMode,
       int alternatives, Date departureTime, Date arrivalTime, Double speedCapInMetersPerSecond)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      RouteOptions ( OptimizationMode optimizationMode,
       int alternatives, Date departureTime, Date arrivalTime, Double speedCapInMetersPerSecond,
       boolean enableRouteHandle)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      RouteOptions ( OptimizationMode optimizationMode,
       int alternatives, Date departureTime, Date arrivalTime, Double speedCapInMetersPerSecond,
       boolean enableRouteHandle, TrafficOptimizationMode trafficOptimizationMode)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      RouteOptions ( OptimizationMode optimizationMode,
       int alternatives, Date departureTime, Date arrivalTime, Double speedCapInMetersPerSecond,
       boolean enableRouteHandle, TrafficOptimizationMode trafficOptimizationMode,
       boolean enableTolls)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      RouteOptions ( OptimizationMode optimizationMode,
       int alternatives, Date departureTime, Date arrivalTime, Double speedCapInMetersPerSecond,
       boolean enableRouteHandle, TrafficOptimizationMode trafficOptimizationMode,
       boolean enableTolls,
       boolean optimizeWaypointsOrder)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      RouteOptions ( OptimizationMode optimizationMode,
       int alternatives, Date departureTime, Date arrivalTime, Double speedCapInMetersPerSecond,
       boolean enableRouteHandle, TrafficOptimizationMode trafficOptimizationMode,
       boolean enableTolls,
       boolean optimizeWaypointsOrder,
       boolean enableRouteLabels)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      equals ( Object obj)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-field-detail" class="section field-details">

  - <div id="sdk-for-android-explore-optimizationMode" class="section detail">

    ### optimizationMode

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a></span> <span class="element-name">optimizationMode</span>

    </div>

    <div class="block">

    The optimization mode to be used for route calculation. By default, it is OptimizationMode.FASTEST .

    </div>

    </div>

  - <div id="sdk-for-android-explore-alternatives" class="section detail">

    ### alternatives

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">alternatives</span>

    </div>

    <div class="block">

    Maximum number of alternative routes that will be calculated, in addition to the best one. The provided value must be in the range \[0, 6\]. Alternative routes can be unavailable, thus they are not guaranteed to be returned. The order of routes is from the best to the worst, as evaluated by the route calculation algorithm and according to the given input parameters. Defaults to 0, which means there are no alternatives, i.e. only the best route is returned. Must be 0 for isoline calculation.

    </div>

    </div>

  - <div id="sdk-for-android-explore-departureTime" class="section detail">

    ### departureTime

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util">Date</a></span> <span class="element-name">departureTime</span>

    </div>

    <div class="block">

    Optional time when travel is expected to start. Traffic speed and incidents shall be taken into account in the calculation of the route, per trafficOptimizationMode . By default, the time is not set. If the time is not set, the current time will be used internally, i.e. now. Therefore, by default, a time-aware route request is initiated including traffic. Note : Both departure time and arrivalTime cannot be set at the same time. This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

    </div>

    </div>

  - <div id="sdk-for-android-explore-arrivalTime" class="section detail">

    ### arrivalTime

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util">Date</a></span> <span class="element-name">arrivalTime</span>

    </div>

    <div class="block">

    Optional time when travel is expected to end. Traffic speed and incidents shall be taken into account in the calculation of the route, per trafficOptimizationMode . By default, the time is not set. If the time is not set, the current time will be used internally, to predict the arrival time. Therefore, by default, a time-aware route request is initiated including traffic. Note : Both departureTime and arrival time cannot be set at the same time. This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

    </div>

    </div>

  - <div id="sdk-for-android-explore-speedCapInMetersPerSecond" class="section detail">

    ### speedCapInMetersPerSecond

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">speedCapInMetersPerSecond</span>

    </div>

    <div class="block">

    Specifies the maximum speed in meters per second, which the user wishes not to exceed. The valid range is \[1, 70\] meters per second. Note that it is valid only for TransportMode.CAR , TransportMode.TRUCK and TransportMode.SCOOTER transport modes. For car, truck and scooter transport modes, it will affect Route.getDuration() of the route. Only for scooter transport mode, it may affect the route geometry. Defaults to null , which means that no speed cap is set.

    </div>

    </div>

  - <div id="sdk-for-android-explore-enableRouteHandle" class="section detail">

    ### enableRouteHandle

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">enableRouteHandle</span>

    </div>

    <div class="block">

    A flag that indicates whether the resulting route should contain a RouteHandle . Defaults to false . Note that a RouteHandle generated by the online RoutingEngine is not compatible with the OfflineRoutingEngine and vice versa.

    </div>

    </div>

  - <div id="sdk-for-android-explore-trafficOptimizationMode" class="section detail">

    ### trafficOptimizationMode

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-routing-trafficoptimizationmode" title="enum class in com.here.sdk.routing">TrafficOptimizationMode</a></span> <span class="element-name">trafficOptimizationMode</span>

    </div>

    <div class="block">

    The traffic optimization mode to be used for route calculation. By default, it is TrafficOptimizationMode.TIME_DEPENDENT , which enables traffic-aware routing.

    </div>

    </div>

  - <div id="sdk-for-android-explore-enableTolls" class="section detail">

    ### enableTolls

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">enableTolls</span>

    </div>

    <div class="block">

    A flag that indicates whether the resulting route Section.getTolls() properties should contain tolls data. Defaults to false . Note: When a route calculation request asks tolls, a pricing scheme with higher rates might be applied. Consult your HERE representative to get more information on the related pricing schemes. Note: For users of the OfflineRoutingEngine this is a beta release of this feature, so there could be a few bugs and unexpected behaviors. The OfflineRoutingEngine is only available for the Navigate license. For users of the RoutingEngine the feature is stable.

    </div>

    </div>

  - <div id="sdk-for-android-explore-optimizeWaypointsOrder" class="section detail">

    ### optimizeWaypointsOrder

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">optimizeWaypointsOrder</span>

    </div>

    <div class="block">

    A flag that indicates whether the order of waypoints that is passed to calculateRoute() should be optimized in the best order. The best order is calculated by the same metrics that are used during regular calculation, e.g. OptimizationMode . The starting and destination Waypoint are not reordered. If the whole number of waypoints is fewer than 4 - the flag doesn't affect the resulting route (nothing to optimize). The resulting order of waypoints can be identified by their waypoint indices in the route sections (see Route.getSections() , Section.getDeparturePlace() , Section.getArrivalPlace() , RoutePlace.waypointIndex ). Currently, the waypoints order optimization is available only when using the OfflineRoutingEngine (only available for the Navigate license). Defaults to false .

    </div>

    </div>

  - <div id="sdk-for-android-explore-enableRouteLabels" class="section detail">

    ### enableRouteLabels

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">enableRouteLabels</span>

    </div>

    <div class="block">

    Specifies whether route labels should be included in the route response. Route labels identify major highways or road names along the route. By default, this is set to false .

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-explore-init" class="section detail">

    ### RouteOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RouteOptions</span>()

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-routing-OptimizationMode" class="section detail">

    ### RouteOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RouteOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-explore-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `optimizationMode` -

    The optimization mode to be used for route calculation. By default, it is <a href="sdk-for-android-explore-com-here-sdk-routing-optimizationmode#FASTEST">`OptimizationMode.FASTEST`</a>.

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-routing-OptimizationMode-int" class="section detail">

    ### RouteOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RouteOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-explore-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode, int alternatives)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `optimizationMode` -

    The optimization mode to be used for route calculation. By default, it is <a href="sdk-for-android-explore-com-here-sdk-routing-optimizationmode#FASTEST">`OptimizationMode.FASTEST`</a>.

    `alternatives` -

    Maximum number of alternative routes that will be calculated, in addition to the best one. The provided value must be in the range \[0, 6\]. Alternative routes can be unavailable, thus they are not guaranteed to be returned. The order of routes is from the best to the worst, as evaluated by the route calculation algorithm and according to the given input parameters. Defaults to 0, which means there are no alternatives, i.e. only the best route is returned. Must be 0 for isoline calculation.

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-routing-OptimizationMode-int-java-util-Date" class="section detail">

    ### RouteOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RouteOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-explore-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode, int alternatives, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util">Date</a> departureTime)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `optimizationMode` -

    The optimization mode to be used for route calculation. By default, it is <a href="sdk-for-android-explore-com-here-sdk-routing-optimizationmode#FASTEST">`OptimizationMode.FASTEST`</a>.

    `alternatives` -

    Maximum number of alternative routes that will be calculated, in addition to the best one. The provided value must be in the range \[0, 6\]. Alternative routes can be unavailable, thus they are not guaranteed to be returned. The order of routes is from the best to the worst, as evaluated by the route calculation algorithm and according to the given input parameters. Defaults to 0, which means there are no alternatives, i.e. only the best route is returned. Must be 0 for isoline calculation.

    `departureTime` -

    Optional time when travel is expected to start. Traffic speed and incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#trafficOptimizationMode">`trafficOptimizationMode`</a>. By default, the time is not set. If the time is not set, the current time will be used internally, i.e. now. Therefore, by default, a time-aware route request is initiated including traffic. **Note**:

    - Both departure time and <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#arrivalTime">`arrivalTime`</a> cannot be set at the same time.
    - This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

    </p>

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-routing-OptimizationMode-int-java-util-Date-java-util-Date" class="section detail">

    ### RouteOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RouteOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-explore-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode, int alternatives, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util">Date</a> departureTime, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util">Date</a> arrivalTime)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `optimizationMode` -

    The optimization mode to be used for route calculation. By default, it is <a href="sdk-for-android-explore-com-here-sdk-routing-optimizationmode#FASTEST">`OptimizationMode.FASTEST`</a>.

    `alternatives` -

    Maximum number of alternative routes that will be calculated, in addition to the best one. The provided value must be in the range \[0, 6\]. Alternative routes can be unavailable, thus they are not guaranteed to be returned. The order of routes is from the best to the worst, as evaluated by the route calculation algorithm and according to the given input parameters. Defaults to 0, which means there are no alternatives, i.e. only the best route is returned. Must be 0 for isoline calculation.

    `departureTime` -

    Optional time when travel is expected to start. Traffic speed and incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#trafficOptimizationMode">`trafficOptimizationMode`</a>. By default, the time is not set. If the time is not set, the current time will be used internally, i.e. now. Therefore, by default, a time-aware route request is initiated including traffic. **Note**:

    - Both departure time and <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#arrivalTime">`arrivalTime`</a> cannot be set at the same time.
    - This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

    </p>

    `arrivalTime` -

    Optional time when travel is expected to end. Traffic speed and incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#trafficOptimizationMode">`trafficOptimizationMode`</a>. By default, the time is not set. If the time is not set, the current time will be used internally, to predict the arrival time. Therefore, by default, a time-aware route request is initiated including traffic. **Note**:

    - Both <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#departureTime">`departureTime`</a> and arrival time cannot be set at the same time.
    - This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

    </p>

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-routing-OptimizationMode-int-java-util-Date-java-util-Date-java-lang-Double" class="section detail">

    ### RouteOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RouteOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-explore-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode, int alternatives, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util">Date</a> departureTime, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util">Date</a> arrivalTime, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a> speedCapInMetersPerSecond)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `optimizationMode` -

    The optimization mode to be used for route calculation. By default, it is <a href="sdk-for-android-explore-com-here-sdk-routing-optimizationmode#FASTEST">`OptimizationMode.FASTEST`</a>.

    `alternatives` -

    Maximum number of alternative routes that will be calculated, in addition to the best one. The provided value must be in the range \[0, 6\]. Alternative routes can be unavailable, thus they are not guaranteed to be returned. The order of routes is from the best to the worst, as evaluated by the route calculation algorithm and according to the given input parameters. Defaults to 0, which means there are no alternatives, i.e. only the best route is returned. Must be 0 for isoline calculation.

    `departureTime` -

    Optional time when travel is expected to start. Traffic speed and incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#trafficOptimizationMode">`trafficOptimizationMode`</a>. By default, the time is not set. If the time is not set, the current time will be used internally, i.e. now. Therefore, by default, a time-aware route request is initiated including traffic. **Note**:

    - Both departure time and <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#arrivalTime">`arrivalTime`</a> cannot be set at the same time.
    - This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

    </p>

    `arrivalTime` -

    Optional time when travel is expected to end. Traffic speed and incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#trafficOptimizationMode">`trafficOptimizationMode`</a>. By default, the time is not set. If the time is not set, the current time will be used internally, to predict the arrival time. Therefore, by default, a time-aware route request is initiated including traffic. **Note**:

    - Both <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#departureTime">`departureTime`</a> and arrival time cannot be set at the same time.
    - This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

    </p>

    `speedCapInMetersPerSecond` -

    Specifies the maximum speed in meters per second, which the user wishes not to exceed. The valid range is \[1, 70\] meters per second. Note that it is valid only for <a href="sdk-for-android-explore-com-here-sdk-transport-transportmode#CAR">`TransportMode.CAR`</a>, <a href="sdk-for-android-explore-com-here-sdk-transport-transportmode#TRUCK">`TransportMode.TRUCK`</a> and <a href="sdk-for-android-explore-com-here-sdk-transport-transportmode#SCOOTER">`TransportMode.SCOOTER`</a> transport modes. For car, truck and scooter transport modes, it will affect [](sdk-for-android-explore-com-here-sdk-routing-route#getDuration())

        Route.getDuration()

    </a> of the route. Only for scooter transport mode, it may affect the route geometry. Defaults to `null`, which means that no speed cap is set.

    </p>

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-routing-OptimizationMode-int-java-util-Date-java-util-Date-java-lang-Double-boolean" class="section detail">

    ### RouteOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RouteOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-explore-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode, int alternatives, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util">Date</a> departureTime, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util">Date</a> arrivalTime, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a> speedCapInMetersPerSecond, boolean enableRouteHandle)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `optimizationMode` -

    The optimization mode to be used for route calculation. By default, it is <a href="sdk-for-android-explore-com-here-sdk-routing-optimizationmode#FASTEST">`OptimizationMode.FASTEST`</a>.

    `alternatives` -

    Maximum number of alternative routes that will be calculated, in addition to the best one. The provided value must be in the range \[0, 6\]. Alternative routes can be unavailable, thus they are not guaranteed to be returned. The order of routes is from the best to the worst, as evaluated by the route calculation algorithm and according to the given input parameters. Defaults to 0, which means there are no alternatives, i.e. only the best route is returned. Must be 0 for isoline calculation.

    `departureTime` -

    Optional time when travel is expected to start. Traffic speed and incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#trafficOptimizationMode">`trafficOptimizationMode`</a>. By default, the time is not set. If the time is not set, the current time will be used internally, i.e. now. Therefore, by default, a time-aware route request is initiated including traffic. **Note**:

    - Both departure time and <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#arrivalTime">`arrivalTime`</a> cannot be set at the same time.
    - This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

    </p>

    `arrivalTime` -

    Optional time when travel is expected to end. Traffic speed and incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#trafficOptimizationMode">`trafficOptimizationMode`</a>. By default, the time is not set. If the time is not set, the current time will be used internally, to predict the arrival time. Therefore, by default, a time-aware route request is initiated including traffic. **Note**:

    - Both <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#departureTime">`departureTime`</a> and arrival time cannot be set at the same time.
    - This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

    </p>

    `speedCapInMetersPerSecond` -

    Specifies the maximum speed in meters per second, which the user wishes not to exceed. The valid range is \[1, 70\] meters per second. Note that it is valid only for <a href="sdk-for-android-explore-com-here-sdk-transport-transportmode#CAR">`TransportMode.CAR`</a>, <a href="sdk-for-android-explore-com-here-sdk-transport-transportmode#TRUCK">`TransportMode.TRUCK`</a> and <a href="sdk-for-android-explore-com-here-sdk-transport-transportmode#SCOOTER">`TransportMode.SCOOTER`</a> transport modes. For car, truck and scooter transport modes, it will affect [](sdk-for-android-explore-com-here-sdk-routing-route#getDuration())

        Route.getDuration()

    </a> of the route. Only for scooter transport mode, it may affect the route geometry. Defaults to `null`, which means that no speed cap is set.

    </p>

    `enableRouteHandle` -

    A flag that indicates whether the resulting route should contain a <a href="sdk-for-android-explore-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing">`RouteHandle`</a>. Defaults to `false`. Note that a `RouteHandle` generated by the online `RoutingEngine` is not compatible with the `OfflineRoutingEngine` and vice versa.

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-routing-OptimizationMode-int-java-util-Date-java-util-Date-java-lang-Double-boolean-com-here-sdk-routing-TrafficOptimizationMode" class="section detail">

    ### RouteOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RouteOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-explore-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode, int alternatives, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util">Date</a> departureTime, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util">Date</a> arrivalTime, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a> speedCapInMetersPerSecond, boolean enableRouteHandle, @NonNull <a href="sdk-for-android-explore-com-here-sdk-routing-trafficoptimizationmode" title="enum class in com.here.sdk.routing">TrafficOptimizationMode</a> trafficOptimizationMode)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `optimizationMode` -

    The optimization mode to be used for route calculation. By default, it is <a href="sdk-for-android-explore-com-here-sdk-routing-optimizationmode#FASTEST">`OptimizationMode.FASTEST`</a>.

    `alternatives` -

    Maximum number of alternative routes that will be calculated, in addition to the best one. The provided value must be in the range \[0, 6\]. Alternative routes can be unavailable, thus they are not guaranteed to be returned. The order of routes is from the best to the worst, as evaluated by the route calculation algorithm and according to the given input parameters. Defaults to 0, which means there are no alternatives, i.e. only the best route is returned. Must be 0 for isoline calculation.

    `departureTime` -

    Optional time when travel is expected to start. Traffic speed and incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#trafficOptimizationMode">`trafficOptimizationMode`</a>. By default, the time is not set. If the time is not set, the current time will be used internally, i.e. now. Therefore, by default, a time-aware route request is initiated including traffic. **Note**:

    - Both departure time and <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#arrivalTime">`arrivalTime`</a> cannot be set at the same time.
    - This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

    </p>

    `arrivalTime` -

    Optional time when travel is expected to end. Traffic speed and incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#trafficOptimizationMode">`trafficOptimizationMode`</a>. By default, the time is not set. If the time is not set, the current time will be used internally, to predict the arrival time. Therefore, by default, a time-aware route request is initiated including traffic. **Note**:

    - Both <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#departureTime">`departureTime`</a> and arrival time cannot be set at the same time.
    - This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

    </p>

    `speedCapInMetersPerSecond` -

    Specifies the maximum speed in meters per second, which the user wishes not to exceed. The valid range is \[1, 70\] meters per second. Note that it is valid only for <a href="sdk-for-android-explore-com-here-sdk-transport-transportmode#CAR">`TransportMode.CAR`</a>, <a href="sdk-for-android-explore-com-here-sdk-transport-transportmode#TRUCK">`TransportMode.TRUCK`</a> and <a href="sdk-for-android-explore-com-here-sdk-transport-transportmode#SCOOTER">`TransportMode.SCOOTER`</a> transport modes. For car, truck and scooter transport modes, it will affect [](sdk-for-android-explore-com-here-sdk-routing-route#getDuration())

        Route.getDuration()

    </a> of the route. Only for scooter transport mode, it may affect the route geometry. Defaults to `null`, which means that no speed cap is set.

    </p>

    `enableRouteHandle` -

    A flag that indicates whether the resulting route should contain a <a href="sdk-for-android-explore-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing">`RouteHandle`</a>. Defaults to `false`. Note that a `RouteHandle` generated by the online `RoutingEngine` is not compatible with the `OfflineRoutingEngine` and vice versa.

    `trafficOptimizationMode` -

    The traffic optimization mode to be used for route calculation. By default, it is <a href="sdk-for-android-explore-com-here-sdk-routing-trafficoptimizationmode#TIME_DEPENDENT">`TrafficOptimizationMode.TIME_DEPENDENT`</a>, which enables traffic-aware routing.

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-routing-OptimizationMode-int-java-util-Date-java-util-Date-java-lang-Double-boolean-com-here-sdk-routing-TrafficOptimizationMode-boolean" class="section detail">

    ### RouteOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RouteOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-explore-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode, int alternatives, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util">Date</a> departureTime, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util">Date</a> arrivalTime, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a> speedCapInMetersPerSecond, boolean enableRouteHandle, @NonNull <a href="sdk-for-android-explore-com-here-sdk-routing-trafficoptimizationmode" title="enum class in com.here.sdk.routing">TrafficOptimizationMode</a> trafficOptimizationMode, boolean enableTolls)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `optimizationMode` -

    The optimization mode to be used for route calculation. By default, it is <a href="sdk-for-android-explore-com-here-sdk-routing-optimizationmode#FASTEST">`OptimizationMode.FASTEST`</a>.

    `alternatives` -

    Maximum number of alternative routes that will be calculated, in addition to the best one. The provided value must be in the range \[0, 6\]. Alternative routes can be unavailable, thus they are not guaranteed to be returned. The order of routes is from the best to the worst, as evaluated by the route calculation algorithm and according to the given input parameters. Defaults to 0, which means there are no alternatives, i.e. only the best route is returned. Must be 0 for isoline calculation.

    `departureTime` -

    Optional time when travel is expected to start. Traffic speed and incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#trafficOptimizationMode">`trafficOptimizationMode`</a>. By default, the time is not set. If the time is not set, the current time will be used internally, i.e. now. Therefore, by default, a time-aware route request is initiated including traffic. **Note**:

    - Both departure time and <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#arrivalTime">`arrivalTime`</a> cannot be set at the same time.
    - This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

    </p>

    `arrivalTime` -

    Optional time when travel is expected to end. Traffic speed and incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#trafficOptimizationMode">`trafficOptimizationMode`</a>. By default, the time is not set. If the time is not set, the current time will be used internally, to predict the arrival time. Therefore, by default, a time-aware route request is initiated including traffic. **Note**:

    - Both <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#departureTime">`departureTime`</a> and arrival time cannot be set at the same time.
    - This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

    </p>

    `speedCapInMetersPerSecond` -

    Specifies the maximum speed in meters per second, which the user wishes not to exceed. The valid range is \[1, 70\] meters per second. Note that it is valid only for <a href="sdk-for-android-explore-com-here-sdk-transport-transportmode#CAR">`TransportMode.CAR`</a>, <a href="sdk-for-android-explore-com-here-sdk-transport-transportmode#TRUCK">`TransportMode.TRUCK`</a> and <a href="sdk-for-android-explore-com-here-sdk-transport-transportmode#SCOOTER">`TransportMode.SCOOTER`</a> transport modes. For car, truck and scooter transport modes, it will affect [](sdk-for-android-explore-com-here-sdk-routing-route#getDuration())

        Route.getDuration()

    </a> of the route. Only for scooter transport mode, it may affect the route geometry. Defaults to `null`, which means that no speed cap is set.

    </p>

    `enableRouteHandle` -

    A flag that indicates whether the resulting route should contain a <a href="sdk-for-android-explore-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing">`RouteHandle`</a>. Defaults to `false`. Note that a `RouteHandle` generated by the online `RoutingEngine` is not compatible with the `OfflineRoutingEngine` and vice versa.

    `trafficOptimizationMode` -

    The traffic optimization mode to be used for route calculation. By default, it is <a href="sdk-for-android-explore-com-here-sdk-routing-trafficoptimizationmode#TIME_DEPENDENT">`TrafficOptimizationMode.TIME_DEPENDENT`</a>, which enables traffic-aware routing.

    `enableTolls` -

    A flag that indicates whether the resulting route [](sdk-for-android-explore-com-here-sdk-routing-section#getTolls())

        Section.getTolls()

    </a> properties should contain tolls data. Defaults to `false`. **Note:** When a route calculation request asks tolls, a pricing scheme with higher rates might be applied. Consult your HERE representative to get more information on the related pricing schemes. **Note:** For users of the `OfflineRoutingEngine` this is a beta release of this feature, so there could be a few bugs and unexpected behaviors. The `OfflineRoutingEngine` is only available for the Navigate license. For users of the `RoutingEngine` the feature is stable.

    </p>

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-routing-OptimizationMode-int-java-util-Date-java-util-Date-java-lang-Double-boolean-com-here-sdk-routing-TrafficOptimizationMode-boolean-boolean" class="section detail">

    ### RouteOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RouteOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-explore-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode, int alternatives, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util">Date</a> departureTime, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util">Date</a> arrivalTime, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a> speedCapInMetersPerSecond, boolean enableRouteHandle, @NonNull <a href="sdk-for-android-explore-com-here-sdk-routing-trafficoptimizationmode" title="enum class in com.here.sdk.routing">TrafficOptimizationMode</a> trafficOptimizationMode, boolean enableTolls, boolean optimizeWaypointsOrder)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `optimizationMode` -

    The optimization mode to be used for route calculation. By default, it is <a href="sdk-for-android-explore-com-here-sdk-routing-optimizationmode#FASTEST">`OptimizationMode.FASTEST`</a>.

    `alternatives` -

    Maximum number of alternative routes that will be calculated, in addition to the best one. The provided value must be in the range \[0, 6\]. Alternative routes can be unavailable, thus they are not guaranteed to be returned. The order of routes is from the best to the worst, as evaluated by the route calculation algorithm and according to the given input parameters. Defaults to 0, which means there are no alternatives, i.e. only the best route is returned. Must be 0 for isoline calculation.

    `departureTime` -

    Optional time when travel is expected to start. Traffic speed and incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#trafficOptimizationMode">`trafficOptimizationMode`</a>. By default, the time is not set. If the time is not set, the current time will be used internally, i.e. now. Therefore, by default, a time-aware route request is initiated including traffic. **Note**:

    - Both departure time and <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#arrivalTime">`arrivalTime`</a> cannot be set at the same time.
    - This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

    </p>

    `arrivalTime` -

    Optional time when travel is expected to end. Traffic speed and incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#trafficOptimizationMode">`trafficOptimizationMode`</a>. By default, the time is not set. If the time is not set, the current time will be used internally, to predict the arrival time. Therefore, by default, a time-aware route request is initiated including traffic. **Note**:

    - Both <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#departureTime">`departureTime`</a> and arrival time cannot be set at the same time.
    - This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

    </p>

    `speedCapInMetersPerSecond` -

    Specifies the maximum speed in meters per second, which the user wishes not to exceed. The valid range is \[1, 70\] meters per second. Note that it is valid only for <a href="sdk-for-android-explore-com-here-sdk-transport-transportmode#CAR">`TransportMode.CAR`</a>, <a href="sdk-for-android-explore-com-here-sdk-transport-transportmode#TRUCK">`TransportMode.TRUCK`</a> and <a href="sdk-for-android-explore-com-here-sdk-transport-transportmode#SCOOTER">`TransportMode.SCOOTER`</a> transport modes. For car, truck and scooter transport modes, it will affect [](sdk-for-android-explore-com-here-sdk-routing-route#getDuration())

        Route.getDuration()

    </a> of the route. Only for scooter transport mode, it may affect the route geometry. Defaults to `null`, which means that no speed cap is set.

    </p>

    `enableRouteHandle` -

    A flag that indicates whether the resulting route should contain a <a href="sdk-for-android-explore-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing">`RouteHandle`</a>. Defaults to `false`. Note that a `RouteHandle` generated by the online `RoutingEngine` is not compatible with the `OfflineRoutingEngine` and vice versa.

    `trafficOptimizationMode` -

    The traffic optimization mode to be used for route calculation. By default, it is <a href="sdk-for-android-explore-com-here-sdk-routing-trafficoptimizationmode#TIME_DEPENDENT">`TrafficOptimizationMode.TIME_DEPENDENT`</a>, which enables traffic-aware routing.

    `enableTolls` -

    A flag that indicates whether the resulting route [](sdk-for-android-explore-com-here-sdk-routing-section#getTolls())

        Section.getTolls()

    </a> properties should contain tolls data. Defaults to `false`. **Note:** When a route calculation request asks tolls, a pricing scheme with higher rates might be applied. Consult your HERE representative to get more information on the related pricing schemes. **Note:** For users of the `OfflineRoutingEngine` this is a beta release of this feature, so there could be a few bugs and unexpected behaviors. The `OfflineRoutingEngine` is only available for the Navigate license. For users of the `RoutingEngine` the feature is stable.

    </p>

    `optimizeWaypointsOrder` -

    A flag that indicates whether the order of waypoints that is passed to

        calculateRoute()

    should be optimized in the best order. The best order is calculated by the same metrics that are used during regular calculation, e.g. <a href="sdk-for-android-explore-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">`OptimizationMode`</a>. The starting and destination <a href="sdk-for-android-explore-com-here-sdk-routing-waypoint" title="class in com.here.sdk.routing">`Waypoint`</a> are not reordered. If the whole number of waypoints is fewer than 4 - the flag doesn't affect the resulting route (nothing to optimize). The resulting order of waypoints can be identified by their waypoint indices in the route sections (see [](sdk-for-android-explore-com-here-sdk-routing-route#getSections())

        Route.getSections()

    </a>, [](sdk-for-android-explore-com-here-sdk-routing-section#getDeparturePlace())

        Section.getDeparturePlace()

    </a>, [](sdk-for-android-explore-com-here-sdk-routing-section#getArrivalPlace())

        Section.getArrivalPlace()

    </a>, <a href="sdk-for-android-explore-com-here-sdk-routing-routeplace#waypointIndex">`RoutePlace.waypointIndex`</a>). Currently, the waypoints order optimization is available only when using the `OfflineRoutingEngine` (only available for the Navigate license). Defaults to `false`.

    </p>

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-routing-OptimizationMode-int-java-util-Date-java-util-Date-java-lang-Double-boolean-com-here-sdk-routing-TrafficOptimizationMode-boolean-boolean-boolean" class="section detail">

    ### RouteOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RouteOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-explore-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a> optimizationMode, int alternatives, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util">Date</a> departureTime, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" class="external-link" title="class or interface in java.util">Date</a> arrivalTime, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a> speedCapInMetersPerSecond, boolean enableRouteHandle, @NonNull <a href="sdk-for-android-explore-com-here-sdk-routing-trafficoptimizationmode" title="enum class in com.here.sdk.routing">TrafficOptimizationMode</a> trafficOptimizationMode, boolean enableTolls, boolean optimizeWaypointsOrder, boolean enableRouteLabels)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `optimizationMode` -

    The optimization mode to be used for route calculation. By default, it is <a href="sdk-for-android-explore-com-here-sdk-routing-optimizationmode#FASTEST">`OptimizationMode.FASTEST`</a>.

    `alternatives` -

    Maximum number of alternative routes that will be calculated, in addition to the best one. The provided value must be in the range \[0, 6\]. Alternative routes can be unavailable, thus they are not guaranteed to be returned. The order of routes is from the best to the worst, as evaluated by the route calculation algorithm and according to the given input parameters. Defaults to 0, which means there are no alternatives, i.e. only the best route is returned. Must be 0 for isoline calculation.

    `departureTime` -

    Optional time when travel is expected to start. Traffic speed and incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#trafficOptimizationMode">`trafficOptimizationMode`</a>. By default, the time is not set. If the time is not set, the current time will be used internally, i.e. now. Therefore, by default, a time-aware route request is initiated including traffic. **Note**:

    - Both departure time and <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#arrivalTime">`arrivalTime`</a> cannot be set at the same time.
    - This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

    </p>

    `arrivalTime` -

    Optional time when travel is expected to end. Traffic speed and incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#trafficOptimizationMode">`trafficOptimizationMode`</a>. By default, the time is not set. If the time is not set, the current time will be used internally, to predict the arrival time. Therefore, by default, a time-aware route request is initiated including traffic. **Note**:

    - Both <a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions#departureTime">`departureTime`</a> and arrival time cannot be set at the same time.
    - This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

    </p>

    `speedCapInMetersPerSecond` -

    Specifies the maximum speed in meters per second, which the user wishes not to exceed. The valid range is \[1, 70\] meters per second. Note that it is valid only for <a href="sdk-for-android-explore-com-here-sdk-transport-transportmode#CAR">`TransportMode.CAR`</a>, <a href="sdk-for-android-explore-com-here-sdk-transport-transportmode#TRUCK">`TransportMode.TRUCK`</a> and <a href="sdk-for-android-explore-com-here-sdk-transport-transportmode#SCOOTER">`TransportMode.SCOOTER`</a> transport modes. For car, truck and scooter transport modes, it will affect [](sdk-for-android-explore-com-here-sdk-routing-route#getDuration())

        Route.getDuration()

    </a> of the route. Only for scooter transport mode, it may affect the route geometry. Defaults to `null`, which means that no speed cap is set.

    </p>

    `enableRouteHandle` -

    A flag that indicates whether the resulting route should contain a <a href="sdk-for-android-explore-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing">`RouteHandle`</a>. Defaults to `false`. Note that a `RouteHandle` generated by the online `RoutingEngine` is not compatible with the `OfflineRoutingEngine` and vice versa.

    `trafficOptimizationMode` -

    The traffic optimization mode to be used for route calculation. By default, it is <a href="sdk-for-android-explore-com-here-sdk-routing-trafficoptimizationmode#TIME_DEPENDENT">`TrafficOptimizationMode.TIME_DEPENDENT`</a>, which enables traffic-aware routing.

    `enableTolls` -

    A flag that indicates whether the resulting route [](sdk-for-android-explore-com-here-sdk-routing-section#getTolls())

        Section.getTolls()

    </a> properties should contain tolls data. Defaults to `false`. **Note:** When a route calculation request asks tolls, a pricing scheme with higher rates might be applied. Consult your HERE representative to get more information on the related pricing schemes. **Note:** For users of the `OfflineRoutingEngine` this is a beta release of this feature, so there could be a few bugs and unexpected behaviors. The `OfflineRoutingEngine` is only available for the Navigate license. For users of the `RoutingEngine` the feature is stable.

    </p>

    `optimizeWaypointsOrder` -

    A flag that indicates whether the order of waypoints that is passed to

        calculateRoute()

    should be optimized in the best order. The best order is calculated by the same metrics that are used during regular calculation, e.g. <a href="sdk-for-android-explore-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">`OptimizationMode`</a>. The starting and destination <a href="sdk-for-android-explore-com-here-sdk-routing-waypoint" title="class in com.here.sdk.routing">`Waypoint`</a> are not reordered. If the whole number of waypoints is fewer than 4 - the flag doesn't affect the resulting route (nothing to optimize). The resulting order of waypoints can be identified by their waypoint indices in the route sections (see [](sdk-for-android-explore-com-here-sdk-routing-route#getSections())

        Route.getSections()

    </a>, [](sdk-for-android-explore-com-here-sdk-routing-section#getDeparturePlace())

        Section.getDeparturePlace()

    </a>, [](sdk-for-android-explore-com-here-sdk-routing-section#getArrivalPlace())

        Section.getArrivalPlace()

    </a>, <a href="sdk-for-android-explore-com-here-sdk-routing-routeplace#waypointIndex">`RoutePlace.waypointIndex`</a>). Currently, the waypoints order optimization is available only when using the `OfflineRoutingEngine` (only available for the Navigate license). Defaults to `false`.

    </p>

    `enableRouteLabels` -

    Specifies whether route labels should be included in the route response. Route labels identify major highways or road names along the route. By default, this is set to `false`.

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-equals-java-lang-Object" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-explore-hashCode" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

