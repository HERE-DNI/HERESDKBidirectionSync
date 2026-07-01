---
title: "TrafficIncidentsQueryCallback (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-traffic-trafficincidentsquerycallback"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.traffic](sdk-for-android-explore-com-here-sdk-traffic-package-summary)

</div>

<div id="class-description" class="section class-description">

Functional Interface:  
This is a functional interface and can therefore be used as the
assignment target for a lambda expression or method reference.

<div class="type-signature">

<span class="annotations"><a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html"
class="external-link"
title="class or interface in java.lang">@FunctionalInterface</a>
</span><span class="modifiers">public interface
</span><span class="element-name type-name-label">TrafficIncidentsQueryCallback</span>

</div>

<div class="block">

Callback passed to TrafficEngine.queryForIncidents(GeoCorridor,
TrafficIncidentsQueryOptions, TrafficIncidentsQueryCallback) . The
method will be called on the main thread when a search call has been
completed. The first argument is the error in the case of the failure.
It is null for an operation that succeeds. The second argument is the
list of incidents in the case of the success. It is null in case of an
error.

</div>

</div>

<div class="section summary">

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Instance Methods
  Abstract Methods

  </div>

  <div id="method-summary-table.tabpanel"
  aria-labelledby="method-summary-table-tab0" role="tabpanel">

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Method</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>onTrafficIncidentsFetched(TrafficQueryError queryError,
   List&lt;TrafficIncident&gt; result)</code></pre></td>
  <td><div class="block">
  Callback passed to TrafficEngine.queryForIncidents(GeoCorridor,
  TrafficIncidentsQueryOptions, TrafficIncidentsQueryCallback) .
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

</div>

<div class="section details">

- <div id="method-detail" class="section method-details">

  - <div id="onTrafficIncidentsFetched(com.here.sdk.traffic.TrafficQueryError,java.util.List)"
    class="section detail">

    ### onTrafficIncidentsFetched

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onTrafficIncidentsFetched</span><span class="parameters">(@Nullable
    [TrafficQueryError](sdk-for-android-explore-com-here-sdk-traffic-trafficqueryerror "enum class in com.here.sdk.traffic") queryError,
    @Nullable <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[TrafficIncident](sdk-for-android-explore-com-here-sdk-traffic-trafficincident "class in com.here.sdk.traffic")> result)</span>

    </div>

    <div class="block">

    Callback passed to TrafficEngine.queryForIncidents(GeoCorridor,
    TrafficIncidentsQueryOptions, TrafficIncidentsQueryCallback) . The
    method will be called on the main thread when a search call has been
    completed. The first argument is the error in the case of the
    failure. It is null for an operation that succeeds. The second
    argument is the list of incidents in the case of the success. It is
    null in case of an error.

    </div>

    Parameters:  
    `queryError` -

    The error in the case of the failure. It is `null` for an operation
    that succeeds.

    `result` -

    The list of incidents in the case of the success. It is `null` in
    case of an error.

    </div>

  </div>

</div>

