---
title: "Easing.withSampledPoints constructor - Easing - animation library - Dart API"
slug: "sdk-for-flutter-explore-animation-easing-easing-withsampledpoints"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="animation/Easing-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">Easing.withSampledPoints</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">Easing.withSampledPoints</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-withSampledPoints-param-points" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-core-point2d-class">Point2D</a></span>\></span></span> <span class="parameter-name">points</span></span>

)

</div>

<div class="section desc markdown">

Creates an instance of customized <a href="sdk-for-flutter-explore-animation-easing-class">Easing</a> using a specified number of points describing an easing function.

- `points` List of sampled data points that define an easing function. X describes normalized time values in the range \[0, 1\]. Y describes normalized animated value changes. Values can fall outside of the range \[0, 1\]. During an animation run animated target value is multiplied with Y value. In case resulting animated target value falls outside of its own supported range it will be clamped to its range (e.g. when negative values used for color animation). X values must increase monotonically. There must be at least 2 data points specified. The first point's X value must be 0, the last point's X value must be 1. During an animation run for any given time value X' from the animation engine that satisfies the relation X(i) \< X' \< X(i+1) for the given X data points the corresponding Y' value will be calculated by linearly interpolating between Y(i) and Y(i+1) data points. The higher the sampling rate of the easing curve used for the data points the more precise the results. In order to achieve the same animation precision for animations with different durations (shorter vs longer) it is recommended to use a higher sampling rate for longer animation duration.

Throws <a href="sdk-for-flutter-explore-animation-easinginstantiationexception-class">EasingInstantiationException</a>. Instantiation error in case of invalid input parameters.

</div>

## Implementation

``` dart
factory Easing.withSampledPoints(List<Point2D> points) => $prototype.withSampledPoints(points);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

