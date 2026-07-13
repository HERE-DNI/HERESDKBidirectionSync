---
title: "ElectronicHorizonOptions constructor - ElectronicHorizonOptions - electronic_horizon library - Dart API"
slug: "sdk-for-flutter-navigate-electronic_horizon-electronichorizonoptions-electronichorizonoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ElectronicHorizonOptions.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="electronic_horizon/ElectronicHorizonOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">ElectronicHorizonOptions</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">ElectronicHorizonOptions</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-lookAheadDistancesInMeters" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">double</span>\></span></span> <span class="parameter-name">lookAheadDistancesInMeters</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-trailingDistanceInMeters" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">trailingDistanceInMeters</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

Offline availability: This property is available online and offline.

- `lookAheadDistancesInMeters` The ordered list of distances that define how far to look ahead in meters when calculating electronic horizon paths. The first entry of the list is for the most preferred path, the second is for the side paths of the first level, the third is for the side paths of the second level, and so on. Each entry defines how far ahead the path should be provided. The valid number of values is from one to ten. Values beyond the tenth entry are removed from the list. If the list is empty, a single default distance value is used instead.
- `trailingDistanceInMeters` The trailing distance of the electronic horizon path in meters. Segments are removed from the path once they are passed and the distance to them exceeds this value.

</div>

## Implementation

``` dart
ElectronicHorizonOptions(this.lookAheadDistancesInMeters, this.trailingDistanceInMeters);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
