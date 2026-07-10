---
title: "RoutingOptions (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-routingoptions"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-routing-package-summary">com.here.sdk.routing</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.routing.RoutingOptions → com.here.sdk.routing.RoutingOptions

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">RoutingOptions</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

The options defines how a route should be calculated. The options are used for all transport modes and engines. \*\* Electric vehicle specific requirements \*\* Electric vehicle consumption are estimated when at least one consumption model is defined. Currently two models are supported: PhysicalConsumptionModel Aside from the values in PhysicalConsumptionModel additionally these values needs to be defined: VehicleSpecification.currentWeightInKilograms from TransportSpecification.vehicleSpecification from transportSpecification Additionally Waypoint.currentWeightChangeInKilograms can be defined. EmpiricalConsumptionModel By setting ElectricVehicleOptions.ensureReachability the RoutingEngine inserts additional charging stations to reach the waypoints. This feature requires setting the BatterySpecifications . By default a vehicle might not reach the waypoint, when the initial charge is not enough to reach all waypoints. See the parameter description below for more details.

</div>

</div>

- <div id="sdk-for-android-navigate-field-summary" class="section field-summary">

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

  <a href="sdk-for-android-navigate-com-here-sdk-routing-allowoptions" title="class in com.here.sdk.routing">`AllowOptions`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions#allowOptions" class="member-name-link"><code>allowOptions</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The options explicitly allowed by user for route calculations.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-avoidanceoptions" title="class in com.here.sdk.routing">`AvoidanceOptions`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions#avoidanceOptions" class="member-name-link"><code>avoidanceOptions</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Options to specify restrictions for route calculations.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-electricvehicleoptions" title="class in com.here.sdk.routing">`ElectricVehicleOptions`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions#evOptions" class="member-name-link"><code>evOptions</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Defines the electric vehicle (EV) related parameters to calculate the consumption and reachability.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-routing-maxspeedonsegment" title="class in com.here.sdk.routing">`MaxSpeedOnSegment`</a>`>`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions#maxSpeedOnSegments" class="member-name-link"><code>maxSpeedOnSegments</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Segments with restriction on maximum DynamicSpeedInfo.baseSpeedInMetersPerSecond .

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions" title="class in com.here.sdk.routing">`RouteOptions`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions#routeOptions" class="member-name-link"><code>routeOptions</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Specifies the common route calculation options.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-routetextoptions" title="class in com.here.sdk.routing">`RouteTextOptions`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions#textOptions" class="member-name-link"><code>textOptions</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Customize textual content returned from the route calculation, such as localization, format, and unit system.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-tolloptions" title="class in com.here.sdk.routing">`TollOptions`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions#tollOptions" class="member-name-link"><code>tollOptions</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Options to specify how the tolls should be calculated, such as transponders, vehicle category, and emission type.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-transport-transportspecification" title="class in com.here.sdk.transport">`TransportSpecification`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions#transportSpecification" class="member-name-link"><code>transportSpecification</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Defines the transport specification which contains the transport mode and the vehicle specifications for the transport mode chosen.

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

      RoutingOptions ()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      equals ( Object obj)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions" title="class in com.here.sdk.routing">`RoutingOptions`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      fromDefaultParameterConfiguration ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Returns the default configuration for the transport specification selected in ParameterConfiguration.transportSpecification from SDKNativeEngine.getParameterConfig() .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-field-detail" class="section field-details">

  - <div id="sdk-for-android-navigate-transportSpecification" class="section detail">

    ### transportSpecification

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-transport-transportspecification" title="class in com.here.sdk.transport">TransportSpecification</a></span> <span class="element-name">transportSpecification</span>

    </div>

    <div class="block">

    Defines the transport specification which contains the transport mode and the vehicle specifications for the transport mode chosen. Notes: The transport mode TransportMode.PUBLIC_TRANSIT is not supported. By default all vehicle specifications from transportSpecification are set to null and the TransportSpecification.transportMode from transportSpecification is set to TransportMode.CAR . A route can be calculated with only the TransportSpecification.transportMode from transportSpecification set. It is highly recommended to define the TruckCategory that is being used in VehicleSpecification.truckCategory from TransportSpecification.vehicleSpecification from transportSpecification , if the TransportSpecification.transportMode from transportSpecification is set to TransportMode.TRUCK . The VehicleSpecification.occupancy from TransportSpecification.vehicleSpecification won't have effect if HOV and/or HOT lane usage is not allowed using EVTruckOptions.allowOptions . The PedestrianSpecification.walkingSpeedInMetersPerSecond from TransportSpecification.pedestrianSpecification if present, will be used by the service as the walking speed for pedestrian routing. It influences the duration of walking along the route. The provided value must be in the range \[0.5, 2.0\]. When the value is outside this range, an invalid parameter error is raised. Refer to RoutingError for details. The default speed is 1 meter per second.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-routeOptions" class="section detail">

    ### routeOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions" title="class in com.here.sdk.routing">RouteOptions</a></span> <span class="element-name">routeOptions</span>

    </div>

    <div class="block">

    Specifies the common route calculation options.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-textOptions" class="section detail">

    ### textOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routetextoptions" title="class in com.here.sdk.routing">RouteTextOptions</a></span> <span class="element-name">textOptions</span>

    </div>

    <div class="block">

    Customize textual content returned from the route calculation, such as localization, format, and unit system.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-avoidanceOptions" class="section detail">

    ### avoidanceOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-avoidanceoptions" title="class in com.here.sdk.routing">AvoidanceOptions</a></span> <span class="element-name">avoidanceOptions</span>

    </div>

    <div class="block">

    Options to specify restrictions for route calculations. By default no restrictions are applied.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-allowOptions" class="section detail">

    ### allowOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-allowoptions" title="class in com.here.sdk.routing">AllowOptions</a></span> <span class="element-name">allowOptions</span>

    </div>

    <div class="block">

    The options explicitly allowed by user for route calculations. By default no options are opt in.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-tollOptions" class="section detail">

    ### tollOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-tolloptions" title="class in com.here.sdk.routing">TollOptions</a></span> <span class="element-name">tollOptions</span>

    </div>

    <div class="block">

    Options to specify how the tolls should be calculated, such as transponders, vehicle category, and emission type. Note Not used for offline calculations.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-maxSpeedOnSegments" class="section detail">

    ### maxSpeedOnSegments

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-routing-maxspeedonsegment" title="class in com.here.sdk.routing">MaxSpeedOnSegment</a>\></span> <span class="element-name">maxSpeedOnSegments</span>

    </div>

    <div class="block">

    Segments with restriction on maximum DynamicSpeedInfo.baseSpeedInMetersPerSecond . Note Not used for offline calculations.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-evOptions" class="section detail">

    ### evOptions

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-electricvehicleoptions" title="class in com.here.sdk.routing">ElectricVehicleOptions</a></span> <span class="element-name">evOptions</span>

    </div>

    <div class="block">

    Defines the electric vehicle (EV) related parameters to calculate the consumption and reachability. When no EV options are defined an internal combustion engine is assumed.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init" class="section detail">

    ### RoutingOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RoutingOptions</span>()

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-equals-java-lang-Object" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-navigate-hashCode" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-navigate-fromDefaultParameterConfiguration" class="section detail">

    ### fromDefaultParameterConfiguration

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions" title="class in com.here.sdk.routing">RoutingOptions</a></span> <span class="element-name">fromDefaultParameterConfiguration</span>()

    </div>

    <div class="block">

    Returns the default configuration for the transport specification selected in ParameterConfiguration.transportSpecification from SDKNativeEngine.getParameterConfig() . Note By default, the \[sdk.core.ParameterConfiguration.transport_specification\] from \[sdk.core.engine.SDKNativeEngine.parameter_config\] will return a valid TransportSpecification object with the \[sdk.transport.TransportSpecification.transport_mode\] set to TransportMode.CAR .

    </div>

    Returns:  
    The <a href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions" title="class in com.here.sdk.routing">`RoutingOptions`</a> object with the default configuration for the transport specification selected in <a href="sdk-for-android-navigate-com-here-sdk-core-parameterconfiguration#transportSpecification">`ParameterConfiguration.transportSpecification`</a> from [](sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine#getParameterConfig())

        SDKNativeEngine.getParameterConfig()

    </a>.

    </p>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

