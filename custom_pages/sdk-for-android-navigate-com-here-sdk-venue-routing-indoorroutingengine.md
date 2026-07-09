---
title: "IndoorRoutingEngine (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-routing-indoorroutingengine"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-venue-routing-package-summary">com.here.sdk.venue.routing</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.venue.routing.IndoorRoutingEngine → com.here.NativeBase com.here.sdk.venue.routing.IndoorRoutingEngine → com.here.sdk.venue.routing.IndoorRoutingEngine

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">IndoorRoutingEngine</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

Use the IndoorRoutingEngine to calculate a route inside a venue. Route calculation is done asynchronously and requires an internet connection. The resulting route contains various information such as the polyline, route length in meters, estimated time to traverse along the route and maneuver data. Note: This feature is in BETA state and thus there can be bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process. Currently, the indoor route calculation may not be accurate so that e.g. a pedestrian end user might be routed via a vehicle access and route or similar. Therefore end users must use this feature with caution and always be aware of the surroundings. The signs and instructions given at the premises must be observed. You are required to inform the end user about this in an appropriate manner, whether in the UI of your application, your end user terms or similar.

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

      IndoorRoutingEngine ( VenueService venueService)

  </div>

  <div class="col-last even-row-color">

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      calculateRoute ( IndoorWaypoint from, IndoorWaypoint to, IndoorRouteOptions routeOptions, CalculateIndoorRouteCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Asynchronously calculates a route inside a venue.

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

  - <div id="sdk-for-android-navigate-init-com-here-sdk-venue-service-VenueService" class="section detail">

    ### IndoorRoutingEngine

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">IndoorRoutingEngine</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-service-venueservice" title="class in com.here.sdk.venue.service">VenueService</a> venueService)</span>

    </div>

    <div class="block">

    Creates a new instance of this class.

    </div>

    Parameters:  
    `venueService` -

    A venue service instance.

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-calculateRoute-com-here-sdk-venue-routing-IndoorWaypoint-com-here-sdk-venue-routing-IndoorWaypoint-com-here-sdk-venue-routing-IndoorRouteOptions-com-here-sdk-venue-routing-CalculateIndoorRouteCallback" class="section detail">

    ### calculateRoute

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">calculateRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-routing-indoorwaypoint" title="class in com.here.sdk.venue.routing">IndoorWaypoint</a> from, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-routing-indoorwaypoint" title="class in com.here.sdk.venue.routing">IndoorWaypoint</a> to, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-routing-indoorrouteoptions" title="class in com.here.sdk.venue.routing">IndoorRouteOptions</a> routeOptions, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-venue-routing-calculateindoorroutecallback" title="interface in com.here.sdk.venue.routing">CalculateIndoorRouteCallback</a> callback)</span>

    </div>

    <div class="block">

    Asynchronously calculates a route inside a venue.

    </div>

    Parameters:  
    `from` -

    A starting position of the route to calculate.

    `to` -

    A destination position of the route to calculate.

    `routeOptions` -

    Options specific for indoor route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

