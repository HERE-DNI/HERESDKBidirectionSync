---
title: "CarSpecifications constructor - CarSpecifications - transport library - Dart API"
slug: "sdk-for-flutter-explore-transport-carspecifications-carspecifications"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CarSpecifications.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="transport/CarSpecifications-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">CarSpecifications</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">CarSpecifications</span>(<wbr></wbr>\[

1.  <span id="sdk-for-flutter-explore-param-grossWeightInKilograms" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">grossWeightInKilograms</span> = <span class="default-value">null</span>, </span>
2.  <span id="sdk-for-flutter-explore-param-heightInCentimeters" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">heightInCentimeters</span> = <span class="default-value">null</span>, </span>
3.  <span id="sdk-for-flutter-explore-param-widthInCentimeters" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">widthInCentimeters</span> = <span class="default-value">null</span>, </span>
4.  <span id="sdk-for-flutter-explore-param-lengthInCentimeters" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">lengthInCentimeters</span> = <span class="default-value">null</span>, </span>
5.  <span id="sdk-for-flutter-explore-param-axleCount" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">axleCount</span> = <span class="default-value">null</span>, </span>
6.  <span id="sdk-for-flutter-explore-param-trailerCount" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">trailerCount</span> = <span class="default-value">null</span>, </span>
7.  <span id="sdk-for-flutter-explore-param-trailerAxleCount" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">trailerAxleCount</span> = <span class="default-value">null</span>, </span>

\])

</div>

<div class="section desc markdown">

Creates a new instance.

- `grossWeightInKilograms` Car weight including trailers and shipped goods in kilograms. The provided value must be greater than or equal to 0. By default, it is not set. **Note:** This parameter is limited to a maximum weight of 4250 kg without trailer and 7550 kg with trailer.
- `heightInCentimeters` Car height in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.
- `widthInCentimeters` Car width in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.
- `lengthInCentimeters` Car length in centimeters. The provided value must be in the range \[0, 30000\]. By default, it is not set.
- `axleCount` Defines total number of axles in the vehicle. The provided value must be greater than or equal to 2. By default, it is not set. Route calculation: When not set, possible axle count restrictions will not be taken into consideration. When specifying <a href="sdk-for-flutter-explore-transport-carspecifications-traileraxlecount">CarSpecifications.trailerAxleCount</a>, then <a href="sdk-for-flutter-explore-transport-carspecifications-axlecount">CarSpecifications.axleCount</a> is required and must be greater than <a href="sdk-for-flutter-explore-transport-carspecifications-traileraxlecount">CarSpecifications.trailerAxleCount</a>.
- `trailerCount` Defines number of trailers attached to the vehicle. The provided value must be in the range \[0, 1\]. By default, it is not set. When specifying <a href="sdk-for-flutter-explore-transport-carspecifications-traileraxlecount">CarSpecifications.trailerAxleCount</a>, then <a href="sdk-for-flutter-explore-transport-carspecifications-trailercount">CarSpecifications.trailerCount</a> is required and must be greater than 0.
- `trailerAxleCount` Defines total number of axles across all the trailers attached to the vehicle. This number is included in <a href="sdk-for-flutter-explore-transport-carspecifications-axlecount">CarSpecifications.axleCount</a>, hence <a href="sdk-for-flutter-explore-transport-carspecifications-traileraxlecount">CarSpecifications.trailerAxleCount</a> must be less than <a href="sdk-for-flutter-explore-transport-carspecifications-axlecount">CarSpecifications.axleCount</a> and greater than or equal to 1. <a href="sdk-for-flutter-explore-transport-carspecifications-axlecount">CarSpecifications.axleCount</a> and <a href="sdk-for-flutter-explore-transport-carspecifications-trailercount">CarSpecifications.trailerCount</a> are required to specify <a href="sdk-for-flutter-explore-transport-carspecifications-traileraxlecount">CarSpecifications.trailerAxleCount</a>. By default, it is not set.

</div>

## Implementation

``` dart
CarSpecifications([int? grossWeightInKilograms = null, int? heightInCentimeters = null, int? widthInCentimeters = null, int? lengthInCentimeters = null, int? axleCount = null, int? trailerCount = null, int? trailerAxleCount = null])
  : grossWeightInKilograms = grossWeightInKilograms, heightInCentimeters = heightInCentimeters, widthInCentimeters = widthInCentimeters, lengthInCentimeters = lengthInCentimeters, axleCount = axleCount, trailerCount = trailerCount, trailerAxleCount = trailerAxleCount;
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
