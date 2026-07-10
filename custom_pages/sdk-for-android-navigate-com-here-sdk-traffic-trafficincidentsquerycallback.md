---
title: "TrafficIncidentsQueryCallback (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-traffic-trafficincidentsquerycallback"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-traffic-package-summary">com.here.sdk.traffic</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

Functional Interface:  
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

<div class="type-signature">

<span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" class="external-link" title="class or interface in java.lang">@FunctionalInterface</a> </span><span class="modifiers">public interface </span><span class="element-name type-name-label">TrafficIncidentsQueryCallback</span>

</div>

<div class="block">

Callback passed to TrafficEngine.queryForIncidents(GeoCorridor, TrafficIncidentsQueryOptions, TrafficIncidentsQueryCallback) . The method will be called on the main thread when a search call has been completed. The first argument is the error in the case of the failure. It is null for an operation that succeeds. The second argument is the list of incidents in the case of the success. It is null in case of an error.

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

      onTrafficIncidentsFetched ( TrafficQueryError queryError, List < TrafficIncident > result)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Callback passed to TrafficEngine.queryForIncidents(GeoCorridor, TrafficIncidentsQueryOptions, TrafficIncidentsQueryCallback) .

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onTrafficIncidentsFetched-com-here-sdk-traffic-TrafficQueryError-java-util-List" class="section detail">

    ### onTrafficIncidentsFetched

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onTrafficIncidentsFetched</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a> queryError, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident" title="class in com.here.sdk.traffic">TrafficIncident</a>\> result)</span>

    </div>

    <div class="block">

    Callback passed to TrafficEngine.queryForIncidents(GeoCorridor, TrafficIncidentsQueryOptions, TrafficIncidentsQueryCallback) . The method will be called on the main thread when a search call has been completed. The first argument is the error in the case of the failure. It is null for an operation that succeeds. The second argument is the list of incidents in the case of the success. It is null in case of an error.

    </div>

    Parameters:  
    `queryError` -

    The error in the case of the failure. It is `null` for an operation that succeeds.

    `result` -

    The list of incidents in the case of the success. It is `null` in case of an error.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

