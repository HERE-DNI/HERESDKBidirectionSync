---
title: "notificationInterval property - LocationSimulatorOptions class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-locationsimulatoroptions-notificationinterval"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/LocationSimulatorOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">notificationInterval</span> property

</div>

<div class="section multi-line-signature">

Duration <span class="name">notificationInterval</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Interval between notifications. Defaults to 1 second.

Values less than 1 ms are not acceptable and the interval is raised to this minimum in object constructors.

Note: This value does not affect `LocationSimulator` when created with a `GPXTrack`.

</div>

## Implementation

``` dart
Duration notificationInterval;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

