---
title: "TrafficIncidentLookupCallback typedef - traffic library - Dart API"
slug: "sdk-for-flutter-explore-traffic-trafficincidentlookupcallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrafficIncidentLookupCallback.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="traffic/traffic-library-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-typedef">TrafficIncidentLookupCallback</span> typedef

</div>

<div class="section multi-line-signature">

<span class="name">TrafficIncidentLookupCallback</span> = <span class="returntype">void Function<span class="signature">(<span id="sdk-for-flutter-explore-param-queryError" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-traffic-trafficqueryerror">TrafficQueryError</a>?</span> <span class="parameter-name">queryError</span>, </span><span id="sdk-for-flutter-explore-param-result" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-traffic-trafficincident-class">TrafficIncident</a>?</span> <span class="parameter-name">result</span></span>)</span></span>

</div>

<div class="section desc markdown">

Callback passed to <a href="sdk-for-flutter-explore-traffic-trafficengine-lookupincident">TrafficEngine.lookupIncident</a>.

The method will be called on the main thread when a search call has been completed. The first argument is the error in the case of the failure. It is `null` for an operation that succeeds. The second argument is the incident in the case of the success. It is `null` in case of an error.

- `queryError` The error in the case of the failure. It is `null` for an operation that succeeds.

- `result` The incident in the case of the success. It is `null` in case of an error.

</div>

## Implementation

``` dart
typedef TrafficIncidentLookupCallback = void Function(TrafficQueryError? queryError, TrafficIncident? result);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
