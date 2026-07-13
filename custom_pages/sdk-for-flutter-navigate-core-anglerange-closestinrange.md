---
title: "closestInRange method - AngleRange class - core library - Dart API"
slug: "sdk-for-flutter-navigate-core-anglerange-closestinrange"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- closestInRange.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core/AngleRange-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">closestInRange</span> method

</div>

<div class="section multi-line-signature">

<span class="returntype">double</span> <span class="name">closestInRange</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-closestInRange-param-angleClockwiseInDegreesFromNorth" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">angleClockwiseInDegreesFromNorth</span></span>

)

</div>

<div class="section desc markdown">

Get the angle that is closest to the given one and in range.

If the angle to both ends of the range is the same, the value in the clockwise direction is returned. If the given angle is in range already, it will be returned as normalized angle.

- `angleClockwiseInDegreesFromNorth` An angle in degrees from north. Will be normalized.

Returns `double`. The closest, normalized in-range angle in degrees, clockwise from north.

If the given angle is in range already, the given angle will be returned as normalized angle in degree, clockwise from north.

</div>

## Implementation

``` dart
double closestInRange(double angleClockwiseInDegreesFromNorth) => $prototype.closestInRange(this, angleClockwiseInDegreesFromNorth);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
