---
title: "gestureRecognizers property - HereMap class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-heremap-gesturerecognizers"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- gestureRecognizers.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/HereMap-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">gestureRecognizers</span> property

</div>

<div class="section multi-line-signature">

Set<span class="signature">\<<wbr></wbr><span class="type-parameter">Factory<span class="signature">\<<wbr></wbr><span class="type-parameter">OneSequenceGestureRecognizer</span>\></span></span>\></span>? <span class="name">gestureRecognizers</span>

<div class="features">

<span class="feature">final</span>

</div>

</div>

<div class="section desc markdown">

Which gestures should be consumed by the map.

It is possible for other gesture recognizers to be competing with the map on pointer events, e.g if the map is inside a `ListView` the `ListView` will want to handle vertical drags. The map will claim gestures that are recognized by any of the recognizers on this list.

When this set is empty or null, the map will only handle pointer events for gestures that were not claimed by any other gesture recognizer.

</div>

## Implementation

``` dart
final Set<Factory<OneSequenceGestureRecognizer>>? gestureRecognizers;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
