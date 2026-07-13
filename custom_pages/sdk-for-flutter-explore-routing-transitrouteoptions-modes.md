---
title: "modes property - TransitRouteOptions class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-transitrouteoptions-modes"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/TransitRouteOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">modes</span> property

</div>

<div class="section multi-line-signature">

List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-routing-transitmode">TransitMode</a></span>\></span> <span class="name">modes</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

This list is used to determine which transit modes should be used for route calculation, <a href="sdk-for-flutter-explore-routing-transitrouteoptions-modefilter">TransitRouteOptions.modeFilter</a> specifies whether this list is an inclusion or an exclusion. For example, specifying subway and bus transit modes with the include filter, returns only subway and bus transit modes, and with the exclude filter, returns all the transit modes except subway and bus. When not set, all the supported transit modes are permitted. By default, this list is empty.

</div>

## Implementation

``` dart
List<TransitMode> modes;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

