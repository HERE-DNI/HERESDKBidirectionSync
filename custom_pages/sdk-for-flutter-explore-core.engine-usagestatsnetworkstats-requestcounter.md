---
title: "requestCounter property - UsageStatsNetworkStats class - core.engine library - Dart API"
slug: "sdk-for-flutter-explore-core.engine-usagestatsnetworkstats-requestcounter"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- requestCounter.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/UsageStatsNetworkStats-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">requestCounter</span> property

</div>

<div class="section multi-line-signature">

int <span class="name">requestCounter</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Amount of calls for particular family of methodCall. methodCall in this case is considered as base request, additional query params are ignored, all calculated as one request. e.g. <https://search.hereapi.com/someparams> and <https://search.hereapi.com/someparams2> will be considered as 1 methodCall, and requestCounter is 2.

</div>

## Implementation

``` dart
int requestCounter;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
