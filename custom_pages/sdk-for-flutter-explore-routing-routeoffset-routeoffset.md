---
title: "RouteOffset constructor - RouteOffset - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-routeoffset-routeoffset"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RouteOffset.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/RouteOffset-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">RouteOffset</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">RouteOffset</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-param-sectionIndex" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">sectionIndex</span>, </span>
2.  <span id="sdk-for-flutter-explore-param-offsetInMeters" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">offsetInMeters</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `sectionIndex` Index of the corresponding route <a href="sdk-for-flutter-explore-routing-section-class">Section</a>. The start of the section indicates the start of the offset.
- `offsetInMeters` Offset from the start of the indexed <a href="sdk-for-flutter-explore-routing-section-class">Section</a> to the specified location along the route. The maximum possible offset is limited by the length of the section and cannot exceed it.

</div>

## Implementation

``` dart
RouteOffset(this.sectionIndex, this.offsetInMeters);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
