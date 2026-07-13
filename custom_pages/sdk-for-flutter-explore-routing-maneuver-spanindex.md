---
title: "spanIndex property - Maneuver class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-maneuver-spanindex"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- spanIndex.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/Maneuver-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">spanIndex</span> property

</div>

<div id="sdk-for-flutter-explore-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">int</span> <span class="name">spanIndex</span>

</div>

<div class="section desc markdown">

Index over <a href="sdk-for-flutter-explore-routing-section-spans">Section.spans</a> indicating the first span after the maneuver point. **Note:** The span index for the last maneuvers (those maneuvers with maneuver action set to <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction.arrive</a>) cannot be used, since these maneuvers are placed after the last span of the route and the span index for them would be greater than the span list size. Gets the index over <a href="sdk-for-flutter-explore-routing-section-spans">Section.spans</a> indicating the first span after the maneuver point.

</div>

## Implementation

``` dart
int get spanIndex;
```

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
