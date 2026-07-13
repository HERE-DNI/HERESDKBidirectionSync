---
title: "TrafficFlowQueryCallback typedef - traffic library - Dart API"
slug: "sdk-for-flutter-navigate-traffic-trafficflowquerycallback"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="traffic/traffic-library-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-typedef">TrafficFlowQueryCallback</span> typedef

</div>

<div class="section multi-line-signature">

<span class="name">TrafficFlowQueryCallback</span> = <span class="returntype">void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-queryError" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-traffic-trafficqueryerror">TrafficQueryError</a>?</span> <span class="parameter-name">queryError</span>, </span><span id="sdk-for-flutter-navigate-param-result" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-traffic-trafficflow-class">TrafficFlow</a></span>\></span>?</span> <span class="parameter-name">result</span></span>)</span></span>

</div>

<div class="section desc markdown">

Callback passed to following functions: <a href="sdk-for-flutter-navigate-traffic-trafficengine-queryforflowinbox">TrafficEngine.queryForFlowInBox</a> <a href="sdk-for-flutter-navigate-traffic-trafficengine-queryforflowincircle">TrafficEngine.queryForFlowInCircle</a> <a href="sdk-for-flutter-navigate-traffic-trafficengine-queryforflowincorridor">TrafficEngine.queryForFlowInCorridor</a> The method will be called on the main thread when a search call has been completed.

The first argument is the error in the case of the failure. It is `null` for an operation that succeeds. The second argument is the list of flow items in the case of the success. It is `null` in case of an error.

- `queryError` The error in the case of the failure. It is `null` for an operation that succeeds.

- `result` The list of incidents in the case of the success. It is `null` in case of an error.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Implementation

``` dart
typedef TrafficFlowQueryCallback = void Function(TrafficQueryError? queryError, List<TrafficFlow>? result);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

