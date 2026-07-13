---
title: "milestoneStatusListener property - NavigatorInterface class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-milestonestatuslistener"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/NavigatorInterface-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">milestoneStatusListener</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-navigation-milestonestatuslistener-class">MilestoneStatusListener</a>?</span> <span class="name">milestoneStatusListener</span>

</div>

<div class="section desc markdown">

Object to receive notifications about the arrival at each <a href="sdk-for-flutter-navigate-navigation-milestone-class">Milestone</a> or missing it. It informs on all waypoints (passed or missed) that are of type <a href="sdk-for-flutter-navigate-navigation-milestonetype">MilestoneType.stopover</a> but excludes the starting waypoint. Waypoints of type <a href="sdk-for-flutter-navigate-navigation-milestonetype">MilestoneType.passthrough</a> are excluded, by default, but can be included via <a href="sdk-for-flutter-navigate-navigation-navigatorinterface-ispassthroughwaypointshandlingenabled">NavigatorInterface.isPassthroughWaypointsHandlingEnabled</a>. Milestone status notifications only occurs if a route has been set. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener that notifies when a <a href="sdk-for-flutter-navigate-navigation-milestone-class">Milestone</a> has been reached or missed.

</div>

## Implementation

``` dart
MilestoneStatusListener? get milestoneStatusListener;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">milestoneStatusListener=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-milestoneStatusListener-param-value" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-milestonestatuslistener-class">MilestoneStatusListener</a>?</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

Object to receive notifications about the arrival at each <a href="sdk-for-flutter-navigate-navigation-milestone-class">Milestone</a> or missing it. It informs on all waypoints (passed or missed) that are of type <a href="sdk-for-flutter-navigate-navigation-milestonetype">MilestoneType.stopover</a> but excludes the starting waypoint. Waypoints of type <a href="sdk-for-flutter-navigate-navigation-milestonetype">MilestoneType.passthrough</a> are excluded, by default, but can be included via <a href="sdk-for-flutter-navigate-navigation-navigatorinterface-ispassthroughwaypointshandlingenabled">NavigatorInterface.isPassthroughWaypointsHandlingEnabled</a>. Milestone status notifications only occurs if a route has been set. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Sets the listener that notifies when a <a href="sdk-for-flutter-navigate-navigation-milestone-class">Milestone</a> has been reached or missed.

</div>

## Implementation

``` dart
set milestoneStatusListener(MilestoneStatusListener? value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

