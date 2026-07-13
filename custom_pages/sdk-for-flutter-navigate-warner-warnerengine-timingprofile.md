---
title: "timingProfile property - WarnerEngine class - warner library - Dart API"
slug: "sdk-for-flutter-navigate-warner-warnerengine-timingprofile"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- timingProfile.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="warner/WarnerEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">timingProfile</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile</a></span> <span class="name">timingProfile</span>

</div>

<div class="section desc markdown">

The timing profile that defines when navigation warnings should be triggered. Configures the base notification thresholds used for delivering navigation warnings. The effective thresholds depend on the selected <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile</a> and may adjust automatically according to the current speed limit:

- For <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.fastSpeed</a>, thresholds apply when the current speed limit is above 100 km/h (62 mph).
- For <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a>, thresholds apply when the current speed limit is above 60 km/h (37 mph).
- For <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a>, thresholds apply when the current speed limit is 60 km/h (37 mph) or below.

**Note:** Custom threshold values can be set, but these timing-profile rules will still apply. Gets the currently configured <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile</a>.

</div>

## Implementation

``` dart
TimingProfile get timingProfile;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">timingProfile=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-timingProfile-param-value" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile</a></span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

The timing profile that defines when navigation warnings should be triggered. Configures the base notification thresholds used for delivering navigation warnings. The effective thresholds depend on the selected <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile</a> and may adjust automatically according to the current speed limit:

- For <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.fastSpeed</a>, thresholds apply when the current speed limit is above 100 km/h (62 mph).
- For <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.regularSpeed</a>, thresholds apply when the current speed limit is above 60 km/h (37 mph).
- For <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile.slowSpeed</a>, thresholds apply when the current speed limit is 60 km/h (37 mph) or below.

**Note:** Custom threshold values can be set, but these timing-profile rules will still apply. Sets the <a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile</a> of the current position.

</div>

## Implementation

``` dart
set timingProfile(TimingProfile value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
