---
title: "flagFixedDurationForNextAnimation method - TrackingCameraBehavior class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-trackingcamerabehavior-flagfixeddurationfornextanimation"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/TrackingCameraBehavior-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">flagFixedDurationForNextAnimation</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">flagFixedDurationForNextAnimation</span>(<wbr></wbr>)

</div>

<div class="section desc markdown">

Enables fixed-duration animation mode for the next property change.

When called, the next setter call (e.g., tilt_in_degrees or bearing_in_degrees) will animate using a fast fixed-duration animation instead of the default speed-based animation. The flag is automatically reset after the next setter is called.

</div>

## Implementation

``` dart
void flagFixedDurationForNextAnimation();
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

