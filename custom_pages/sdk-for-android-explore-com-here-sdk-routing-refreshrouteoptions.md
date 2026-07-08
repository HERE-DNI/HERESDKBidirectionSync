---
title: "RefreshRouteOptions (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-refreshrouteoptions"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.routing.RefreshRouteOptions → com.here.NativeBase com.here.sdk.routing.RefreshRouteOptions → com.here.sdk.routing.RefreshRouteOptions

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

<div class="type-signature">

<span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> </span><span class="modifiers">public final class </span><span class="element-name type-name-label">RefreshRouteOptions</span> <span class="extends-implements">extends [NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="deprecation-block">

<span class="deprecated-label">Deprecated.</span>

<div class="deprecation-comment">

Will be removed in v4.28.0. Use the `RoutingOptions` class instead.

</div>

</div>

<div class="block">

The options to specify how to refresh an already calculated route identified by a RouteHandle . All the options that may result in a new route shape are ignored as no new route is calculated. Instead, only the data that accompanies a route, such as traffic information, can be refreshed. Therefore, the following route options are ignored: RouteOptions.alternatives , RouteOptions.arrivalTime , and RouteOptions.optimizationMode . If new AvoidanceOptions are specified, they are ignored as well and instead new SectionNotice 's are generated that indicate where the requested AvoidanceOptions are violated. Note that when EVCarOptions.ensureReachability is set to true, the route refresh request will fail as this option is incompatible with a fixed route shape. If any of the ignored options are important, consider calculating a new route instead. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

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

      RefreshRouteOptions ( BicycleOptions bicycleOptions)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Deprecated.

  </div>

  <div class="block">

  Constructs a RefreshRouteOptions object with BicycleOptions .

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      RefreshRouteOptions ( BusOptions busOptions)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Deprecated.

  </div>

  <div class="block">

  Constructs a RefreshRouteOptions object with BusOptions .

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      RefreshRouteOptions ( CarOptions carOptions)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Deprecated.

  </div>

  <div class="block">

  Constructs a RefreshRouteOptions object with CarOptions .

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      RefreshRouteOptions ( EVCarOptions evCarOptions)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Deprecated.

  </div>

  <div class="block">

  Constructs a RefreshRouteOptions object with EVCarOptions .

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      RefreshRouteOptions ( EVTruckOptions evTruckOptions)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Deprecated.

  </div>

  <div class="block">

  Constructs a RefreshRouteOptions object with EVTruckOptions .

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      RefreshRouteOptions ( PedestrianOptions pedestrianOptions)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Deprecated.

  </div>

  <div class="block">

  Constructs a RefreshRouteOptions object with PedestrianOptions .

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      RefreshRouteOptions ( PrivateBusOptions privateBusOptions)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Deprecated.

  </div>

  <div class="block">

  Constructs a RefreshRouteOptions object with PrivateBusOptions .

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      RefreshRouteOptions ( ScooterOptions scooterOptions)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Deprecated.

  </div>

  <div class="block">

  Constructs a RefreshRouteOptions object with ScooterOptions .

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      RefreshRouteOptions ( TaxiOptions taxiOptions)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Deprecated.

  </div>

  <div class="block">

  Constructs a RefreshRouteOptions object with TaxiOptions .

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      RefreshRouteOptions ( TruckOptions truckOptions)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Deprecated.

  </div>

  <div class="block">

  Constructs a RefreshRouteOptions object with TruckOptions .

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      RefreshRouteOptions ( TransportMode transportMode)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Deprecated.

  </div>

  <div class="block">

  Constructs a RefreshRouteOptions object with TransportMode .

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary" class="section method-summary">

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-explore-init-com-here-sdk-transport-TransportMode" class="section detail">

    ### RefreshRouteOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RefreshRouteOptions</span><wbr></wbr><span class="parameters">(@NonNull [TransportMode](sdk-for-android-explore-com-here-sdk-transport-transportmode "enum class in com.here.sdk.transport") transportMode)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Constructs a RefreshRouteOptions object with TransportMode .

    </div>

    Parameters:  
    `transportMode` -

    Updates the transport mode for the route.

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-routing-CarOptions" class="section detail">

    ### RefreshRouteOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RefreshRouteOptions</span><wbr></wbr><span class="parameters">(@NonNull [CarOptions](sdk-for-android-explore-com-here-sdk-routing-caroptions "class in com.here.sdk.routing") carOptions)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Constructs a RefreshRouteOptions object with CarOptions .

    </div>

    Parameters:  
    `carOptions` -

    Converts the route to a car route, if a different transport mode was used for the [`RouteHandle`](sdk-for-android-explore-com-here-sdk-routing-routehandle "class in com.here.sdk.routing"). Note that in case this is not possible, an [`RoutingError.NO_ROUTE_FOUND`](sdk-for-android-explore-com-here-sdk-routing-routingerror#NO_ROUTE_FOUND) error will be triggered.

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-routing-TruckOptions" class="section detail">

    ### RefreshRouteOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RefreshRouteOptions</span><wbr></wbr><span class="parameters">(@NonNull [TruckOptions](sdk-for-android-explore-com-here-sdk-routing-truckoptions "class in com.here.sdk.routing") truckOptions)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Constructs a RefreshRouteOptions object with TruckOptions .

    </div>

    Parameters:  
    `truckOptions` -

    Converts the route to a truck route, if a different transport mode was used for the [`RouteHandle`](sdk-for-android-explore-com-here-sdk-routing-routehandle "class in com.here.sdk.routing"). Note that in case this is not possible, an [`RoutingError.NO_ROUTE_FOUND`](sdk-for-android-explore-com-here-sdk-routing-routingerror#NO_ROUTE_FOUND) error will be triggered.

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-routing-PedestrianOptions" class="section detail">

    ### RefreshRouteOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RefreshRouteOptions</span><wbr></wbr><span class="parameters">(@NonNull [PedestrianOptions](sdk-for-android-explore-com-here-sdk-routing-pedestrianoptions "class in com.here.sdk.routing") pedestrianOptions)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Constructs a RefreshRouteOptions object with PedestrianOptions .

    </div>

    Parameters:  
    `pedestrianOptions` -

    Converts the route to a pedestrian route, if a different transport mode was used for the [`RouteHandle`](sdk-for-android-explore-com-here-sdk-routing-routehandle "class in com.here.sdk.routing"). Note that in case this is not possible, an [`RoutingError.NO_ROUTE_FOUND`](sdk-for-android-explore-com-here-sdk-routing-routingerror#NO_ROUTE_FOUND) error will be triggered.

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-routing-ScooterOptions" class="section detail">

    ### RefreshRouteOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RefreshRouteOptions</span><wbr></wbr><span class="parameters">(@NonNull [ScooterOptions](sdk-for-android-explore-com-here-sdk-routing-scooteroptions "class in com.here.sdk.routing") scooterOptions)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Constructs a RefreshRouteOptions object with ScooterOptions .

    </div>

    Parameters:  
    `scooterOptions` -

    Converts the route to a scooter route, if a different transport mode was used for the [`RouteHandle`](sdk-for-android-explore-com-here-sdk-routing-routehandle "class in com.here.sdk.routing"). Note that in case this is not possible, an [`RoutingError.NO_ROUTE_FOUND`](sdk-for-android-explore-com-here-sdk-routing-routingerror#NO_ROUTE_FOUND) error will be triggered.

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-routing-TaxiOptions" class="section detail">

    ### RefreshRouteOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RefreshRouteOptions</span><wbr></wbr><span class="parameters">(@NonNull [TaxiOptions](sdk-for-android-explore-com-here-sdk-routing-taxioptions "class in com.here.sdk.routing") taxiOptions)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Constructs a RefreshRouteOptions object with TaxiOptions .

    </div>

    Parameters:  
    `taxiOptions` -

    Converts the route to a taxi route, if a different transport mode was used for the [`RouteHandle`](sdk-for-android-explore-com-here-sdk-routing-routehandle "class in com.here.sdk.routing"). Note that in case this is not possible, an [`RoutingError.NO_ROUTE_FOUND`](sdk-for-android-explore-com-here-sdk-routing-routingerror#NO_ROUTE_FOUND) error will be triggered.

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-routing-EVCarOptions" class="section detail">

    ### RefreshRouteOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RefreshRouteOptions</span><wbr></wbr><span class="parameters">(@NonNull [EVCarOptions](sdk-for-android-explore-com-here-sdk-routing-evcaroptions "class in com.here.sdk.routing") evCarOptions)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Constructs a RefreshRouteOptions object with EVCarOptions .

    </div>

    Parameters:  
    `evCarOptions` -

    Converts the route to an electric car route, if a different transport mode was used for the [`RouteHandle`](sdk-for-android-explore-com-here-sdk-routing-routehandle "class in com.here.sdk.routing"). Note that in case this is not possible, an [`RoutingError.NO_ROUTE_FOUND`](sdk-for-android-explore-com-here-sdk-routing-routingerror#NO_ROUTE_FOUND) error will be triggered.

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-routing-EVTruckOptions" class="section detail">

    ### RefreshRouteOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RefreshRouteOptions</span><wbr></wbr><span class="parameters">(@NonNull [EVTruckOptions](sdk-for-android-explore-com-here-sdk-routing-evtruckoptions "class in com.here.sdk.routing") evTruckOptions)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Constructs a RefreshRouteOptions object with EVTruckOptions .

    </div>

    Parameters:  
    `evTruckOptions` -

    Converts the route to an electric truck route, if a different transport mode was used for the [`RouteHandle`](sdk-for-android-explore-com-here-sdk-routing-routehandle "class in com.here.sdk.routing"). Note that in case this is not possible, an [`RoutingError.NO_ROUTE_FOUND`](sdk-for-android-explore-com-here-sdk-routing-routingerror#NO_ROUTE_FOUND) error will be triggered.

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-routing-BicycleOptions" class="section detail">

    ### RefreshRouteOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RefreshRouteOptions</span><wbr></wbr><span class="parameters">(@NonNull [BicycleOptions](sdk-for-android-explore-com-here-sdk-routing-bicycleoptions "class in com.here.sdk.routing") bicycleOptions)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Constructs a RefreshRouteOptions object with BicycleOptions .

    </div>

    Parameters:  
    `bicycleOptions` -

    Converts the route to a bicycle route, if a different transport mode was used for the [`RouteHandle`](sdk-for-android-explore-com-here-sdk-routing-routehandle "class in com.here.sdk.routing"). Note that in case this is not possible, an [`RoutingError.NO_ROUTE_FOUND`](sdk-for-android-explore-com-here-sdk-routing-routingerror#NO_ROUTE_FOUND) error will be triggered.

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-routing-BusOptions" class="section detail">

    ### RefreshRouteOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RefreshRouteOptions</span><wbr></wbr><span class="parameters">(@NonNull [BusOptions](sdk-for-android-explore-com-here-sdk-routing-busoptions "class in com.here.sdk.routing") busOptions)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Constructs a RefreshRouteOptions object with BusOptions .

    </div>

    Parameters:  
    `busOptions` -

    Converts the route to a bus route, if a different transport mode was used for the [`RouteHandle`](sdk-for-android-explore-com-here-sdk-routing-routehandle "class in com.here.sdk.routing"). Note that in case this is not possible, an [`RoutingError.NO_ROUTE_FOUND`](sdk-for-android-explore-com-here-sdk-routing-routingerror#NO_ROUTE_FOUND) error will be triggered.

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-routing-PrivateBusOptions" class="section detail">

    ### RefreshRouteOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RefreshRouteOptions</span><wbr></wbr><span class="parameters">(@NonNull [PrivateBusOptions](sdk-for-android-explore-com-here-sdk-routing-privatebusoptions "class in com.here.sdk.routing") privateBusOptions)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>

    </div>

    <div class="block">

    Constructs a RefreshRouteOptions object with PrivateBusOptions .

    </div>

    Parameters:  
    `privateBusOptions` -

    Converts the route to a private bus route, if a different transport mode was used for the [`RouteHandle`](sdk-for-android-explore-com-here-sdk-routing-routehandle "class in com.here.sdk.routing"). Note that in case this is not possible, an [`RoutingError.NO_ROUTE_FOUND`](sdk-for-android-explore-com-here-sdk-routing-routingerror#NO_ROUTE_FOUND) error will be triggered.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

