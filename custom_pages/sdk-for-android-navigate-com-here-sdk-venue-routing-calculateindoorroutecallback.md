---
title: "CalculateIndoorRouteCallback (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-routing-calculateindoorroutecallback"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-venue-routing-package-summary">com.here.sdk.venue.routing</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

Functional Interface:  
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

<div class="type-signature">

<span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" class="external-link" title="class or interface in java.lang">@FunctionalInterface</a> </span><span class="modifiers">public interface </span><span class="element-name type-name-label">CalculateIndoorRouteCallback</span>

</div>

<div class="block">

A function which is called by the IndoorRoutingEngine after route calculation has completed. It is always called on the main thread. The first argument is the error in case of a failure. It is null for an operation that succeeds. The second argument is the calculated routes. It is null in case of an error.

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

      onIndoorRouteCalculated ( IndoorRoutingError indoorRoutingError, List < Route > routeList)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  A function which is called by the IndoorRoutingEngine after route calculation has completed.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onIndoorRouteCalculated-com-here-sdk-venue-routing-IndoorRoutingError-java-util-List" class="section detail">

    ### onIndoorRouteCalculated

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onIndoorRouteCalculated</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-venue-routing-indoorroutingerror" title="enum class in com.here.sdk.venue.routing">IndoorRoutingError</a> indoorRoutingError, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing">Route</a>\> routeList)</span>

    </div>

    <div class="block">

    A function which is called by the IndoorRoutingEngine after route calculation has completed. It is always called on the main thread. The first argument is the error in case of a failure. It is null for an operation that succeeds. The second argument is the calculated routes. It is null in case of an error.

    </div>

    Parameters:  
    `indoorRoutingError` -

    The error in case of a failure. It is `null` for an operation that succeeds.

    `routeList` -

    The calculated routes. It is `null` in case of an error.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

