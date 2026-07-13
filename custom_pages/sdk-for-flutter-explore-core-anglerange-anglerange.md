---
title: "AngleRange constructor - AngleRange - core library - Dart API"
slug: "sdk-for-flutter-explore-core-anglerange-anglerange"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core/AngleRange-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">AngleRange</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">AngleRange</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-param-start" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">start</span>, </span>
2.  <span id="sdk-for-flutter-explore-param-extent" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">extent</span></span>

)

</div>

<div class="section desc markdown">

Constructs an AngleRange from the provided start and extent angles.

Corrects values if they exceed the ranges.

- `start` Start angle, running clockwise, in degrees from north. The value will be normalized to \[0.0, 360.0).

- `extent` The range's extent, running clockwise, in degrees from start. The value will be clamped to the range of \[0, 360\] degrees.

</div>

## Implementation

``` dart
factory AngleRange(double start, double extent) => $prototype.$init(start, extent);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

