---
title: "allowHighway property - ScooterOptions class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-scooteroptions-allowhighway"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- allowHighway.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/ScooterOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">allowHighway</span> property

</div>

<div class="section multi-line-signature">

bool <span class="name">allowHighway</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Specifies whether scooter is allowed on highway or not. `True` means scooter is allowed to use highways and `false` means otherwise. By default it is set to `false`. Note that there is a similar parameter in <a href="sdk-for-flutter-navigate-routing-avoidanceoptions-class">AvoidanceOptions</a>, to disallow highway usage, see <a href="sdk-for-flutter-navigate-routing-roadfeatures">RoadFeatures.controlledAccessHighway</a>. As the avoidance options takes precedence, if this parameter is also used, then scooters are not allowed to use highways even if `allowHighway` is set to `true`. However, if no alternative route is possible, the calculated route may use highways. In such a case, a <a href="sdk-for-flutter-navigate-routing-sectionnotice-class">SectionNotice</a> will be provided in the related <a href="sdk-for-flutter-navigate-routing-section-class">Section</a> to indicate that the highway usage restriction is violated on this route. A few examples:

1 - If no avoidance option is set, and `allowHighway = false`, when no route is found without highway usage, a notice is received.

2 - If no avoidance option is set, and `allowHighway = true`, when no route is found without highway usage, no notice is received.

3 - If only `avoid[features] = controlledAccessHighway` is set, when no route is found without highway usage, a notice is received.

4 - If both `avoid[features] = controlledAccessHighway` and `allowHighway = true` are set, when no route is found without highway usage, a notice is received.

</div>

## Implementation

``` dart
bool allowHighway;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
