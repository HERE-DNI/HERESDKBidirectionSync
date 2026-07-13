---
title: "onOffRoadProgressUpdated method - OffRoadProgressListener class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-offroadprogresslistener-onoffroadprogressupdated"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onOffRoadProgressUpdated.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/OffRoadProgressListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">onOffRoadProgressUpdated</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">onOffRoadProgressUpdated</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-onOffRoadProgressUpdated-param-offRoadProgress" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-offroadprogress-class">OffRoadProgress</a></span> <span class="parameter-name">offRoadProgress</span></span>

)

</div>

<div class="section desc markdown">

Called whenever the current location has been updated and the user is off-road.

Off-road progress events starts after the user has reached the map-matched destination and the current location is not map-matched.

- `offRoadProgress` The current off-road progress update.

</div>

## Implementation

``` dart
void onOffRoadProgressUpdated(OffRoadProgress offRoadProgress);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
