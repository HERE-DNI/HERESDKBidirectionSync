---
title: "Toll constructor - Toll - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-toll-toll"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Toll.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/Toll-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">Toll</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">Toll</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-param-countryCode" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">countryCode</span>, </span>
2.  <span id="sdk-for-flutter-explore-param-tollSystems" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span> <span class="parameter-name">tollSystems</span>, </span>
3.  <span id="sdk-for-flutter-explore-param-fares" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-routing-tollfare-class">TollFare</a></span>\></span></span> <span class="parameter-name">fares</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `countryCode` The country in which the toll is to be paid in ISO-3166-1 alpha-3 format, e.g. "USA".
- `tollSystems` Names of the multiple toll systems which are associated with the toll, e.g. \["ATLANDES“, "ASF", "COFIROUTE"\]. When the toll information covers several toll roads and the toll system of the each road is different, all toll system names are listed here and the last element will be one of the exit toll booth.
- `fares` The list of toll fares possible for the toll which may depend on time of day, payment method, vehicle characteristics, etc. If there are multiple toll fares that the router cannot disambiguate, then the list will contain more than one toll fare. Note that this list contains at least one element, i.e. it is never empty.

</div>

## Implementation

``` dart
Toll(this.countryCode, this.tollSystems, this.fares);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
