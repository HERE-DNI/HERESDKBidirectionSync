---
title: "UsageStatsNetworkStats constructor - UsageStatsNetworkStats - core.engine library - Dart API"
slug: "sdk-for-flutter-navigate-core.engine-usagestatsnetworkstats-usagestatsnetworkstats"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/UsageStatsNetworkStats-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">UsageStatsNetworkStats</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">UsageStatsNetworkStats</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-sentBytes" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">sentBytes</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-receivedBytes" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">receivedBytes</span>, </span>
3.  <span id="sdk-for-flutter-navigate-param-methodCall" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">methodCall</span>, </span>
4.  <span id="sdk-for-flutter-navigate-param-requestCounter" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">requestCounter</span>, </span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `sentBytes` Number of bytes sent over the network.
- `receivedBytes` Number of bytes received from the network.
- `methodCall` Name or description of the method being called.
- `requestCounter` Amount of calls for particular family of methodCall. methodCall in this case is considered as base request, additional query params are ignored, all calculated as one request. e.g. <https://search.hereapi.com/someparams> and <https://search.hereapi.com/someparams2> will be considered as 1 methodCall, and requestCounter is 2.

</div>

## Implementation

``` dart
UsageStatsNetworkStats(this.sentBytes, this.receivedBytes, this.methodCall, this.requestCounter);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

