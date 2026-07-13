---
title: "fromString method - GeoCoordinates class - core library - Dart API"
slug: "sdk-for-flutter-navigate-core-geocoordinates-fromstring"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- fromString.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core/GeoCoordinates-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">fromString</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a>?</span> <span class="name">fromString</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-fromString-param-input" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">input</span></span>

)

</div>

<div class="section desc markdown">

Constructs GeoCoordinates from the provided string in specified format.

Corrects values of lat and long if they exceed the ranges. If the latitude value is out of range of \[-90.0, 90.0\] it's clamped to that range. If the longitude value is out of range of \[-180.0, 180.0\] it's replaced with a value within the range, representing effectively the same meridian. Examples: `53.43762,-13.65468`. `49°59'56.948"N, 15°48'22.989"E` `50d4m17.698N 14d24m2.826E` `49.9991522N, 150.8063858E` `40°26′47″N 79°58′36″W`

- `input` String representing GeoCoordinates in one of supported formats.

Returns <a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates?</a>. Created GeoCoordinates, or 'null' if string was not in appropriate format.

</div>

## Implementation

``` dart
static GeoCoordinates? fromString(String input) => $prototype.fromString(input);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
