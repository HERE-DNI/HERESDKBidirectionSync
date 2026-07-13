---
title: "roadSignWarningListener property - NavigatorInterface class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-roadsignwarninglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- roadSignWarningListener.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/NavigatorInterface-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">roadSignWarningListener</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-navigation-roadsignwarninglistener-class">RoadSignWarningListener</a>?</span> <span class="name">roadSignWarningListener</span>

</div>

<div class="section desc markdown">

Object to receive notifications about road signs on the current road. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive notifications about road signs on the current road.

</div>

## Implementation

``` dart
RoadSignWarningListener? get roadSignWarningListener;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">roadSignWarningListener=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-roadSignWarningListener-param-value" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-roadsignwarninglistener-class">RoadSignWarningListener</a>?</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

Object to receive notifications about road signs on the current road. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Sets the listener to receive notifications about road signs on the current road. **Note:** This `RoadSignWarningListener` will provide school zone warnings only in case the speed limit inside the school zone is different than the default speed limit applicable for cars outside the school zone. For warnings about school zones regardless of their speed limits, the `NavigatorInterface.road_sign_warning_listener` should be used and the `RoadSignWarning.type` should be checked for value `RoadSignType.SCHOOL_ZONE`. The school zone warner is a zone warner, which means that for a school zone there will *always* be 3 warnings emitted, with the `SchoolZoneWarning.distance_type` set to `DistanceType.AHEAD`, `DistanceType.REACHED`

</div>

## Implementation

``` dart
set roadSignWarningListener(RoadSignWarningListener? value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
