---
title: "enableDoubleNotification property - ManeuverNotificationOptions class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-enabledoublenotification"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- enableDoubleNotification.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/ManeuverNotificationOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">enableDoubleNotification</span> property

</div>

<div class="section multi-line-signature">

bool <span class="name">enableDoubleNotification</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

A flag that indicates whether combined maneuver notifications should be generated. Such double notifications can be useful when maneuvers are very close. **Example:** A combined message: 'After 300 meters turn left and then turn right.'. This way a user can better anticipate the next-next maneuver. Note that setting to `true` will make the notification longer as two maneuvers will be merged into one. When the next-next maneuver action takes place, the notification will be given as usual. **Example:** 'Now turn left and then then turn right.' will be followed by 'Now turn right.'. Defaults to `true`.

</div>

## Implementation

``` dart
bool enableDoubleNotification;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
