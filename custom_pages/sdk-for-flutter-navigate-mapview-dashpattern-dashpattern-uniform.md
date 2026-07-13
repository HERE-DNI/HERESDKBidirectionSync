---
title: "DashPattern.uniform constructor - DashPattern - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-dashpattern-dashpattern-uniform"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/DashPattern-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">DashPattern.uniform</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">DashPattern.uniform</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-uniform-param-dashLength" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">dashLength</span></span>

)

</div>

<div class="section desc markdown">

Creates a uniform dash pattern in which the length of a gap is the same as the length of a dash.

This allows for patterns like `' — — — —'` or `' ——— ——— ———'`.

- `dashLength` The length of a dash in pixels. The gap will have the same length. Clamped to the range of \[1, 500\].

</div>

## Implementation

``` dart
factory DashPattern.uniform(double dashLength) => $prototype.uniform(dashLength);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

