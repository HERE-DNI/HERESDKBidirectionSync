---
title: "diffBetweenVideoMemoryLimitAndRequirementInKiB property - MapContextMemoryManagementResult class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementresult-diffbetweenvideomemorylimitandrequirementinkib"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- diffBetweenVideoMemoryLimitAndRequirementInKiB.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapContextMemoryManagementResult-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">diffBetweenVideoMemoryLimitAndRequirementInKiB</span> property

</div>

<div class="section multi-line-signature">

int? <span class="name">diffBetweenVideoMemoryLimitAndRequirementInKiB</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

The difference in kibibytes between the limit and the video-memory requirement for only the currently visible data. If positive, the returned value is the surplus value over the currently required bare minimum. Even when positive, if the limit set is low, the application could later breach the limit and delete even visible data. A non positive value means the limit cannot fit the existing visible data and there could be data disappearing or flickering. If for some reason the callback is ignored or correct memory limit cannot be calculated, `null` value is returned.

</div>

## Implementation

``` dart
int? diffBetweenVideoMemoryLimitAndRequirementInKiB;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
