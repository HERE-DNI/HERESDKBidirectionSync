---
title: "lookAheadDistancesInMeters property - ElectronicHorizonOptions class - electronic_horizon library - Dart API"
slug: "sdk-for-flutter-navigate-electronic_horizon-electronichorizonoptions-lookaheaddistancesinmeters"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="electronic_horizon/ElectronicHorizonOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">lookAheadDistancesInMeters</span> property

</div>

<div class="section multi-line-signature">

List<span class="signature">\<<wbr></wbr><span class="type-parameter">double</span>\></span> <span class="name">lookAheadDistancesInMeters</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

The ordered list of distances that define how far to look ahead in meters when calculating electronic horizon paths. The first entry of the list is for the most preferred path, the second is for the side paths of the first level, the third is for the side paths of the second level, and so on. Each entry defines how far ahead the path should be provided. The valid number of values is from one to ten. Values beyond the tenth entry are removed from the list. If the list is empty, a single default distance value is used instead.

</div>

## Implementation

``` dart
List<double> lookAheadDistancesInMeters;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

