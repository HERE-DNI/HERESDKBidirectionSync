---
title: "maxPoints property - IsolineOptionsCalculation class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-isolineoptionscalculation-maxpoints"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- maxPoints.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/IsolineOptionsCalculation-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">maxPoints</span> property

</div>

<div class="section multi-line-signature">

int? <span class="name">maxPoints</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Limits the number of points in the resulting isoline polygon. If the isoline consists of multiple polygons, the sum of points from all polygons is considered. Note that this parameter does not affect the calculation, but the shape of the polygon. Look at <a href="sdk-for-flutter-explore-routing-isolinecalculationmode">IsolineCalculationMode</a> parameter to optimize performance. A higher value will result in a more accurate polygon shape. Rendering a polygon with a high number of points can negatively impact rendering performance. The minimum allowed value is 30, lower values will be ignored.

</div>

## Implementation

``` dart
int? maxPoints;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
