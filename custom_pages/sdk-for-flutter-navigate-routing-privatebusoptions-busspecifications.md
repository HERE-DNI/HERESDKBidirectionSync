---
title: "busSpecifications property - PrivateBusOptions class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-privatebusoptions-busspecifications"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- busSpecifications.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/PrivateBusOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">busSpecifications</span> property

</div>

<div class="section multi-line-signature">

<a href="sdk-for-flutter-navigate-transport-busspecifications-class" class="deprecated">BusSpecifications</a> <span class="name">busSpecifications</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Detailed bus specifications such as dimensions and weight.

**Note:** Some members of `bus_specifications` have limited value range.

- <a href="sdk-for-flutter-navigate-transport-busspecifications-grossweightinkilograms">BusSpecifications.grossWeightInKilograms</a> must not be negative.
- <a href="sdk-for-flutter-navigate-transport-busspecifications-heightincentimeters">BusSpecifications.heightInCentimeters</a> must be in the range \[0, 5000\].
- <a href="sdk-for-flutter-navigate-transport-busspecifications-widthincentimeters">BusSpecifications.widthInCentimeters</a> must be in the range \[0, 5000\].
- <a href="sdk-for-flutter-navigate-transport-busspecifications-lengthincentimeters">BusSpecifications.lengthInCentimeters</a> must be in the range \[0, 30000\]. The validation of the range is done in the method that takes `PrivateBusOptions` as parameter.

</div>

## Implementation

``` dart
BusSpecifications busSpecifications;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
