---
title: "DashPattern constructor - DashPattern - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-dashpattern-dashpattern"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/DashPattern-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">DashPattern</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">DashPattern</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-param-gapLength" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">gapLength</span>, </span>
2.  <span id="sdk-for-flutter-explore-param-dashLength" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">dashLength</span></span>

)

</div>

<div class="section desc markdown">

Creates a simple dash pattern in which the lengths of a dash and gap can be different.

This allows for patterns like `' — — — —'` or `' ——— ——— ———'`.

- `gapLength` The length of a gap in pixels. Clamped to the range of \[1, 500\].

- `dashLength` The length of a dash in pixels. Clamped to the range of \[1, 500\].

</div>

## Implementation

``` dart
factory DashPattern(double gapLength, double dashLength) => $prototype.$init(gapLength, dashLength);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

