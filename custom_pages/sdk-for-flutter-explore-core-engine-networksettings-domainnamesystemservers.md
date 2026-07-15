---
title: "domainNameSystemServers property - NetworkSettings class - core.engine library - Dart API"
slug: "sdk-for-flutter-explore-core-engine-networksettings-domainnamesystemservers"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/NetworkSettings-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">domainNameSystemServers</span> property

</div>

<div class="section multi-line-signature">

List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-core-networkendpoint-class">NetworkEndpoint</a></span>\></span> <span class="name">domainNameSystemServers</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Domain Name Server list. This list fully replaces embedded mechanism to detect DNS. The order is important. To reduce response time make sure that most probably servers are at the beginning. Currently only IPv4 is supported.

</div>

## Implementation

``` dart
List<NetworkEndpoint> domainNameSystemServers;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

