---
title: "TrafficIncidentLookupCallback (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-traffic-trafficincidentlookupcallback"
---

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.traffic](sdk-for-android-explore-com-here-sdk-traffic-package-summary)

</div>

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

Functional Interface:  
This is a functional interface and can therefore be used as the
assignment target for a lambda expression or method reference.

<div class="type-signature">

<span class="annotations"><a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html"
class="external-link"
title="class or interface in java.lang">@FunctionalInterface</a>
</span><span class="modifiers">public interface
</span><span class="element-name type-name-label">TrafficIncidentLookupCallback</span>

</div>

<div class="block">

Callback passed to TrafficEngine.lookupIncident(java.lang.String,
com.here.sdk.traffic.TrafficIncidentLookupOptions,
com.here.sdk.traffic.TrafficIncidentLookupCallback) . The method will be
called on the main thread when a search call has been completed. The
first argument is the error in the case of the failure. It is null for
an operation that succeeds. The second argument is the incident in the
case of the success. It is null in case of an error.

</div>

</div>

- <div id="sdk-for-android-explore-method-summary"
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

      onTrafficIncidentFetched ( TrafficQueryError queryError, TrafficIncident result)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Callback passed to TrafficEngine.lookupIncident(java.lang.String,
  com.here.sdk.traffic.TrafficIncidentLookupOptions,
  com.here.sdk.traffic.TrafficIncidentLookupCallback) .

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-onTrafficIncidentFetched-com-here-sdk-traffic-TrafficQueryError-com-here-sdk-traffic-TrafficIncident"
    class="section detail">

    ### onTrafficIncidentFetched

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onTrafficIncidentFetched</span><span class="parameters">(@Nullable
    [TrafficQueryError](sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror "enum class in com.here.sdk.traffic") queryError,
    @Nullable
    [TrafficIncident](sdk-for-android-explore-com-here-sdk-traffic-trafficincident "class in com.here.sdk.traffic") result)</span>

    </div>

    <div class="block">

    Callback passed to TrafficEngine.lookupIncident(java.lang.String,
    com.here.sdk.traffic.TrafficIncidentLookupOptions,
    com.here.sdk.traffic.TrafficIncidentLookupCallback) . The method
    will be called on the main thread when a search call has been
    completed. The first argument is the error in the case of the
    failure. It is null for an operation that succeeds. The second
    argument is the incident in the case of the success. It is null in
    case of an error.

    </div>

    Parameters:  
    `queryError` -

    The error in the case of the failure. It is `null` for an operation
    that succeeds.

    `result` -

    The incident in the case of the success. It is `null` in case of an
    error.

    </div>

  </div>

