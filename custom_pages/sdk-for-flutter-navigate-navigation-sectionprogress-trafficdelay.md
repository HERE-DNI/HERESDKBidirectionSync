---
title: "trafficDelay property - SectionProgress class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-sectionprogress-trafficdelay"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/SectionProgress-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">trafficDelay</span> property

</div>

<div class="section multi-line-signature">

Duration <span class="name">trafficDelay</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

The estimated traffic delay in seconds from current location until the end of the <a href="sdk-for-flutter-navigate-routing-section-class">Section</a> is reached. Note that the value is accumulated per section, and that the last section contains the overall traffic delay until the destination is reached. The delay might be a negative value: Negative values indicate that the part of this section can be traversed faster than usual. Note that this is based on a delay value received at the moment of route calculation. Defaults to 0 seconds.

</div>

## Implementation

``` dart
Duration trafficDelay;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

