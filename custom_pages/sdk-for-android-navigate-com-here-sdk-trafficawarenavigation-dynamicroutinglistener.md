---
title: "DynamicRoutingListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutinglistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-package-summary">com.here.sdk.trafficawarenavigation</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">DynamicRoutingListener</span>

</div>

<div class="block">

This interface should be implemented in order to receive notifications about the new route via the DynamicRoutingEngine .

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      onBetterRouteFound ( Route newRoute,
       int etaDifferenceInSeconds,
       int distanceDifferenceInMeters)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  This event is issued when a better route could be found, as defined by DynamicRoutingEngineOptions .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      onRoutingError ( RoutingError routingError)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  This event is issued when an error occurred.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onBetterRouteFound-com-here-sdk-routing-Route-int-int" class="section detail">

    ### onBetterRouteFound

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onBetterRouteFound</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing">Route</a> newRoute, int etaDifferenceInSeconds, int distanceDifferenceInMeters)</span>

    </div>

    <div class="block">

    This event is issued when a better route could be found, as defined by DynamicRoutingEngineOptions . To find a better route, two routes are calculated. The updated current route: A route that is calculated via the route specified. The dynamic route: A route that starts at the current position on the route specified and passes through the remaining waypoints.

    </div>

    Parameters:  
    `newRoute` -

    The newly calculated route with the remaining waypoints starting from the current location.

    `etaDifferenceInSeconds` -

    The difference in seconds: eta of the current updated route - eta of the dynamic route.

    `distanceDifferenceInMeters` -

    The difference in meters: distance of the current updated route - distance of the dynamic route. The value can be negative in case the current updated route has a shorter distance, but its now assumed to be longer than the dynamic route.

    </div>

  - <div id="sdk-for-android-navigate-onRoutingError-com-here-sdk-routing-RoutingError" class="section detail">

    ### onRoutingError

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onRoutingError</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a> routingError)</span>

    </div>

    <div class="block">

    This event is issued when an error occurred.

    </div>

    Parameters:  
    `routingError` -

    Routing error

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

