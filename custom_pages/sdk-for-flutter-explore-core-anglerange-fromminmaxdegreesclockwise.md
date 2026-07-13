---
title: "fromMinMaxDegreesClockwise method - AngleRange class - core library - Dart API"
slug: "sdk-for-flutter-explore-core-anglerange-fromminmaxdegreesclockwise"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core/AngleRange-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">fromMinMaxDegreesClockwise</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-core-anglerange-class">AngleRange</a></span> <span class="name">fromMinMaxDegreesClockwise</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-fromMinMaxDegreesClockwise-param-min" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">min</span>, </span>
2.  <span id="sdk-for-flutter-explore-fromMinMaxDegreesClockwise-param-max" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">max</span></span>

)

</div>

<div class="section desc markdown">

Constructs an AngleRange from the provided minimum and maximum angles.

Corrects values if they exceed the ranges. The angles are always interpreted in clockwise orientation.

- `min` Angle where to start the circular sector, running clockwise, in degrees from north. The value will be normalized to \<a href="sdk-for-flutter-explore-core-anglerange-class">0.0, 360.0).

- `max` Angle where the circular sector ends, running clockwise, in degrees from north. The value will be normalized to \[0.0, 360.0).

Returns [AngleRange</a>. Created AngleRange from the provided minimum and maximum angles.

</div>

## Implementation

``` dart
static AngleRange fromMinMaxDegreesClockwise(double min, double max) => $prototype.fromMinMaxDegreesClockwise(min, max);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

