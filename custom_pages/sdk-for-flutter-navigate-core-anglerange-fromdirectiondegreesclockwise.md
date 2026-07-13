---
title: "fromDirectionDegreesClockwise method - AngleRange class - core library - Dart API"
slug: "sdk-for-flutter-navigate-core-anglerange-fromdirectiondegreesclockwise"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- fromDirectionDegreesClockwise.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core/AngleRange-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">fromDirectionDegreesClockwise</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-anglerange-class">AngleRange</a></span> <span class="name">fromDirectionDegreesClockwise</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-fromDirectionDegreesClockwise-param-center" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">center</span>, </span>
2.  <span id="sdk-for-flutter-navigate-fromDirectionDegreesClockwise-param-extent" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">extent</span></span>

)

</div>

<div class="section desc markdown">

Constructs an AngleRange from the provided center angle defining the direction and an angular width to extent the range by 50% clockwise and 50% counter-clockwise from its center angle.

Corrects values if they exceed the ranges. Example: direction = 90, extent = 10 means the circle sector is pointing east, with an extent of 5 degrees north-wards and 5 degrees south-wards.

- `center` Start angle, running clockwise, in degrees from north. The value will be normalized to \[0.0, 360.0).

- `extent` The range's extent, running clockwise, in degrees from start. The value will be clamped to the range of \[0, 360\] degrees.

Returns <a href="sdk-for-flutter-navigate-core-anglerange-class">AngleRange</a>. Created AngleRange from the provided center angle and the range's extent.

</div>

## Implementation

``` dart
static AngleRange fromDirectionDegreesClockwise(double center, double extent) => $prototype.fromDirectionDegreesClockwise(center, extent);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
