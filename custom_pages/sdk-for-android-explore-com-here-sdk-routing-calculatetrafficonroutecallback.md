---
title: "CalculateTrafficOnRouteCallback (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-calculatetrafficonroutecallback"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

Functional Interface:  
This is a functional interface and can therefore be used as the
assignment target for a lambda expression or method reference.

<div class="type-signature">

<span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" class="external-link" title="class or interface in java.lang">@FunctionalInterface</a>
</span><span class="modifiers">public interface
</span><span class="element-name type-name-label">CalculateTrafficOnRouteCallback</span>

</div>

<div class="block">

A function which is called by the RoutingEngine after route traffic
calculation has completed. It is always called on the main thread. The
first argument is the error in case of a failure. It is null for an
operation that succeeds. The second argument is the calculated route
traffic. It is null in case of an error.

</div>

</div>

<div class="section summary">
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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      onTrafficOnRouteCalculated(RoutingError routingError,
       TrafficOnRoute trafficOnRoute)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  A function which is called by the RoutingEngine after route traffic
  calculation has completed.

  </div>

  </div>

  </div>

  </div>

  </div>

</div>

<div class="section details">
<div id="sdk-for-android-explore-method-detail"
  class="section method-details">
<div id="sdk-for-android-explore-onTrafficOnRouteCalculated(com.here.sdk.routing.RoutingError,com.here.sdk.routing.TrafficOnRoute)"
    class="section detail">

    ### onTrafficOnRouteCalculated

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onTrafficOnRouteCalculated</span><span class="parameters">(@Nullable
    [RoutingError](sdk-for-android-explore-com-here-sdk-routing-routingerror "enum class in com.here.sdk.routing") routingError,
    @Nullable
    [TrafficOnRoute](sdk-for-android-explore-com-here-sdk-routing-trafficonroute "class in com.here.sdk.routing") trafficOnRoute)</span>

    </div>

    <div class="block">

    A function which is called by the RoutingEngine after route traffic
    calculation has completed. It is always called on the main thread.
    The first argument is the error in case of a failure. It is null for
    an operation that succeeds. The second argument is the calculated
    route traffic. It is null in case of an error.

    </div>

    Parameters:  
    `routingError` -

    The error in case of a failure. It is `null` for an operation that
    succeeds.

    `trafficOnRoute` -

    The calculated route traffic. It is `null` in case of an error.

    </div>

  </div>

</div>

