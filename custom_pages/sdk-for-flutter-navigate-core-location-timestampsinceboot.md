---
title: "timestampSinceBoot property - Location class - core library - Dart API"
slug: "sdk-for-flutter-navigate-core-location-timestampsinceboot"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- timestampSinceBoot.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core/Location-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">timestampSinceBoot</span> property

</div>

<div class="section multi-line-signature">

Duration? <span class="name">timestampSinceBoot</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

The time at which the location was determined, relative to device boot time. This time is monotonic and not affected by leap time or other system time adjustments, so this is the recommended basis for general purpose interval timing between location updates. If it cannot be determined, the value is `null`.

</div>

## Implementation

``` dart
Duration? timestampSinceBoot;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
