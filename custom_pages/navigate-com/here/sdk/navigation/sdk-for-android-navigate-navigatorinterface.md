---
title: "NavigatorInterface (API Reference)"
slug: "sdk-for-android-navigate-navigatorinterface"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- NavigatorInterface.html -->
<!DOCTYPE HTML>






<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-navigate-index">Overview</a></li>
<li><a href="sdk-for-android-navigate-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-navigate-package-tree">Tree</a></li>
<li><a href="sdk-for-android-navigate-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-navigate-index-all">Index</a></li>
<li><a href="sdk-for-android-navigate-help-doc#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li>Nested | </li>
<li>Field | </li>
<li>Constr | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li>Field | </li>
<li>Constr | </li>
<li><a href="#method-detail">Method</a></li>
</ul>
</div>

</div>
<!-- ========= END OF TOP NAVBAR ========= -->
<span class="skip-nav" id="skip-navbar-top"></span></nav>
</header>
<div class="flex-content">
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="sdk-for-android-navigate-core-locationlistener" title="interface in com.here.sdk.core">LocationListener</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="sdk-for-android-navigate-navigator" title="class in com.here.sdk.navigation">Navigator</a></code>, <code><a href="sdk-for-android-navigate-visualnavigator" title="class in com.here.sdk.navigation">VisualNavigator</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">NavigatorInterface</span><span class="extends-implements">
extends <a href="sdk-for-android-navigate-core-locationlistener" title="interface in com.here.sdk.core">LocationListener</a></span></div>
<div class="block"><p>This interface provides the basic functionality needed to run a navigation session.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#calculateRemainingDistanceInMeters(com.here.sdk.core.GeoCoordinates)">calculateRemainingDistanceInMeters</a><wbr/>(<a href="sdk-for-android-navigate-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">This method calculates the distance between the current position and given coordinates.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-bordercrossingwarninglistener" title="interface in com.here.sdk.navigation">BorderCrossingWarningListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getBorderCrossingWarningListener()">getBorderCrossingWarningListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the listener to receive notifications about border crossings on the current road.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-bordercrossingwarningoptions" title="class in com.here.sdk.navigation">BorderCrossingWarningOptions</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getBorderCrossingWarningOptions()">getBorderCrossingWarningOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets border crossing warning options to be passed to <a href="sdk-for-android-navigate-bordercrossingwarninglistener" title="interface in com.here.sdk.navigation"><code>BorderCrossingWarningListener</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-currentsituationlaneassistanceviewlistener" title="interface in com.here.sdk.navigation">CurrentSituationLaneAssistanceViewListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getCurrentSituationLaneAssistanceViewListener()">getCurrentSituationLaneAssistanceViewListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the listener  to receive current situation lane assistance view notifications.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-dangerzonewarninglistener" title="interface in com.here.sdk.navigation">DangerZoneWarningListener</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDangerZoneWarningListener()">getDangerZoneWarningListener</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the listener to receive current danger zones notifications.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-destinationreachedlistener" title="interface in com.here.sdk.navigation">DestinationReachedListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getDestinationReachedListener()">getDestinationReachedListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the listener that notify when the destination has been reached.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-environmentalzonewarninglistener" title="interface in com.here.sdk.navigation">EnvironmentalZoneWarningListener</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getEnvironmentalZoneWarningListener()">getEnvironmentalZoneWarningListener</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the listener to receive current environmental zones notifications.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-eventtextlistener" title="interface in com.here.sdk.navigation">EventTextListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getEventTextListener()">getEventTextListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the listener that notifies when a text notification is available.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-eventtextoptions" title="class in com.here.sdk.navigation">EventTextOptions</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getEventTextOptions()">getEventTextOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the text notification options.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-junctionviewlaneassistancelistener" title="interface in com.here.sdk.navigation">JunctionViewLaneAssistanceListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getJunctionViewLaneAssistanceListener()">getJunctionViewLaneAssistanceListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the listener  to receive junction view lane assistance notifications.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-mapmatcher-locationmanager" title="class in com.here.sdk.mapmatcher">LocationManager</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getLocationManager()">getLocationManager</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the location manager instance used by the navigator.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-lowspeedzonewarninglistener" title="interface in com.here.sdk.navigation">LowSpeedZoneWarningListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getLowSpeedZoneWarningListener()">getLowSpeedZoneWarningListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the listener to receive notifications about low speed zones on the current road.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-routing-maneuver" title="class in com.here.sdk.routing">Maneuver</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getManeuver(int)">getManeuver</a><wbr/>(int index)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns maneuver at the given index.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-maneuvernotificationoptions" title="class in com.here.sdk.navigation">ManeuverNotificationOptions</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getManeuverNotificationOptions()">getManeuverNotificationOptions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the maneuver notification options.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-maneuvernotificationtimingoptions" title="class in com.here.sdk.navigation">ManeuverNotificationTimingOptions</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getManeuverNotificationTimingOptions(com.here.sdk.transport.TransportMode,com.here.sdk.navigation.TimingProfile)">getManeuverNotificationTimingOptions</a><wbr/>(<a href="sdk-for-android-navigate-transport-transportmode" title="enum class in com.here.sdk.transport">TransportMode</a> transportMode,
 <a href="sdk-for-android-navigate-timingprofile" title="enum class in com.here.sdk.navigation">TimingProfile</a> timingProfile)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns maneuver notification timing options with default values given the combination of transport mode and timing profile.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-maneuverviewlaneassistancelistener" title="interface in com.here.sdk.navigation">ManeuverViewLaneAssistanceListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getManeuverViewLaneAssistanceListener()">getManeuverViewLaneAssistanceListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the listener  to receive maneuver view lane assistance notifications.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-milestonestatuslistener" title="interface in com.here.sdk.navigation">MilestoneStatusListener</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getMilestoneStatusListener()">getMilestoneStatusListener</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the listener that notifies when a <a href="sdk-for-android-navigate-milestone" title="class in com.here.sdk.navigation"><code>Milestone</code></a> has been reached or missed.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-navigablelocationlistener" title="interface in com.here.sdk.navigation">NavigableLocationListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNavigableLocationListener()">getNavigableLocationListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the listener that notifies current location updates.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-offroaddestinationreachedlistener" title="interface in com.here.sdk.navigation">OffRoadDestinationReachedListener</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOffRoadDestinationReachedListener()">getOffRoadDestinationReachedListener</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the listener that notifies when the off-road destination has been reached.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-offroadprogresslistener" title="interface in com.here.sdk.navigation">OffRoadProgressListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getOffRoadProgressListener()">getOffRoadProgressListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the listener that notifies about off-road progress.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-postactionlistener" title="interface in com.here.sdk.navigation">PostActionListener</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getPostActionListener()">getPostActionListener</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the listener  to receive post action notifications, such as a charge action at a charging station.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-railwaycrossingwarninglistener" title="interface in com.here.sdk.navigation">RailwayCrossingWarningListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRailwayCrossingWarningListener()">getRailwayCrossingWarningListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the listener to receive notifications about railway crossings on the current road.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-realisticviewwarninglistener" title="interface in com.here.sdk.navigation">RealisticViewWarningListener</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRealisticViewWarningListener()">getRealisticViewWarningListener</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the listener to receive notifications about junction views on the current road.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-realisticviewwarningoptions" title="class in com.here.sdk.navigation">RealisticViewWarningOptions</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRealisticViewWarningOptions()">getRealisticViewWarningOptions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets realistic view warning options that allow to filter realistic views to be passed to
 <a href="sdk-for-android-navigate-realisticviewwarninglistener" title="interface in com.here.sdk.navigation"><code>RealisticViewWarningListener</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-roadattributeslistener" title="interface in com.here.sdk.navigation">RoadAttributesListener</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRoadAttributesListener()">getRoadAttributesListener</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the listener  to receive notifications about attributes of the current road.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-roadsignwarninglistener" title="interface in com.here.sdk.navigation">RoadSignWarningListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRoadSignWarningListener()">getRoadSignWarningListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the listener to receive notifications about road signs on the current road.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-roadsignwarningoptions" title="class in com.here.sdk.navigation">RoadSignWarningOptions</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRoadSignWarningOptions()">getRoadSignWarningOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets road sign warning options that allow to filter road signs to be passed to <a href="sdk-for-android-navigate-roadsignwarninglistener" title="interface in com.here.sdk.navigation"><code>RoadSignWarningListener</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-roadtextslistener" title="interface in com.here.sdk.navigation">RoadTextsListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRoadTextsListener()">getRoadTextsListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the listener  to receive notifications about the textual attributes of the current road.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-routing-route" title="class in com.here.sdk.routing">Route</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRoute()">getRoute</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the route that is being navigated.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-routedeviationlistener" title="interface in com.here.sdk.navigation">RouteDeviationListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRouteDeviationListener()">getRouteDeviationListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the listener that notifies when deviation from the route is observed.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-routeprogresslistener" title="interface in com.here.sdk.navigation">RouteProgressListener</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getRouteProgressListener()">getRouteProgressListener</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the listener that notifies when a route progress change occurs.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-safetycamerawarninglistener" title="interface in com.here.sdk.navigation">SafetyCameraWarningListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSafetyCameraWarningListener()">getSafetyCameraWarningListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the listener  to receive safety camera warning notifications.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-safetycamerawarningoptions" title="class in com.here.sdk.navigation">SafetyCameraWarningOptions</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSafetyCameraWarningOptions()">getSafetyCameraWarningOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets safety camera warning options to be passed to <a href="sdk-for-android-navigate-safetycamerawarninglistener" title="interface in com.here.sdk.navigation"><code>SafetyCameraWarningListener</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-schoolzonewarninglistener" title="interface in com.here.sdk.navigation">SchoolZoneWarningListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSchoolZoneWarningListener()">getSchoolZoneWarningListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the listener to receive notifications about school zones on the current road.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-schoolzonewarningoptions" title="class in com.here.sdk.navigation">SchoolZoneWarningOptions</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSchoolZoneWarningOptions()">getSchoolZoneWarningOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets school zone warning options that allow to configure school zone notifications to be
 passed to <a href="sdk-for-android-navigate-schoolzonewarninglistener" title="interface in com.here.sdk.navigation"><code>SchoolZoneWarningListener</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-speedlimitlistener" title="interface in com.here.sdk.navigation">SpeedLimitListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSpeedLimitListener()">getSpeedLimitListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the listener  to receive notifications about the speed limit of the current road.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-speedwarninglistener" title="interface in com.here.sdk.navigation">SpeedWarningListener</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSpeedWarningListener()">getSpeedWarningListener</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the listener to receive notifications
 when a speed limit on a road is exceeded or driving speed is restored back to normal.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-speedwarningoptions" title="class in com.here.sdk.navigation">SpeedWarningOptions</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getSpeedWarningOptions()">getSpeedWarningOptions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the speed warning options.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-tollstopwarninglistener" title="interface in com.here.sdk.navigation">TollStopWarningListener</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTollStopWarningListener()">getTollStopWarningListener</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the listener to receive notifications about
 the the upcoming toll stop.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code><a href="sdk-for-android-navigate-core-transportprofile" title="class in com.here.sdk.core">TransportProfile</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code><a class="member-name-link" href="#getTrackingTransportProfile()">getTrackingTransportProfile</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-transport-transportspecification" title="class in com.here.sdk.transport">TransportSpecification</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTrackingTransportSpecification()">getTrackingTransportSpecification</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the transport specification for the <a href="sdk-for-android-navigate-navigator" title="class in com.here.sdk.navigation"><code>Navigator</code></a>, when no route is present.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-trafficmergewarninglistener" title="interface in com.here.sdk.navigation">TrafficMergeWarningListener</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTrafficMergeWarningListener()">getTrafficMergeWarningListener</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the listener to receive notifications about
 merging traffic to the current road.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-trafficmergewarningoptions" title="class in com.here.sdk.navigation">TrafficMergeWarningOptions</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTrafficMergeWarningOptions()">getTrafficMergeWarningOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets merging traffic warning options that allow to configure merging traffic notifications to be
 passed to <a href="sdk-for-android-navigate-trafficmergewarninglistener" title="interface in com.here.sdk.navigation"><code>TrafficMergeWarningListener</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-routing-trafficonroute" title="class in com.here.sdk.routing">TrafficOnRoute</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTrafficOnRoute()">getTrafficOnRoute</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the traffic information for the current route.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-truckrestrictionswarninglistener" title="interface in com.here.sdk.navigation">TruckRestrictionsWarningListener</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTruckRestrictionsWarningListener()">getTruckRestrictionsWarningListener</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the listener  to receive notifications about
 truck restrictions on the current road.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-truckrestrictionswarningoptions" title="class in com.here.sdk.navigation">TruckRestrictionsWarningOptions</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getTruckRestrictionsWarningOptions()">getTruckRestrictionsWarningOptions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets truck restrictions warning options that allow to filter truck restrictions to be
 passed to <a href="sdk-for-android-navigate-truckrestrictionswarninglistener" title="interface in com.here.sdk.navigation"><code>TruckRestrictionsWarningListener</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-warner-warnerengine" title="class in com.here.sdk.warner">WarnerEngine</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getWarnerEngine()">getWarnerEngine</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the warner engine used by the navigator.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-warningnotificationdistances" title="class in com.here.sdk.navigation">WarningNotificationDistances</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getWarningNotificationDistances(com.here.sdk.navigation.WarningType)">getWarningNotificationDistances</a><wbr/>(<a href="sdk-for-android-navigate-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a> warningType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the warning notification distances for the requested warning type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isEnableTunnelExtrapolation()">isEnableTunnelExtrapolation</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return <code>true</code> if tunnel extrapolation is enabled otherwise <code>false</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#isPassthroughWaypointsHandlingEnabled()">isPassthroughWaypointsHandlingEnabled</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Return <code>true</code> if handling of passthrough waypoints is enabled, otherwise - <code>false</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#repeatLastManeuverNotification()">repeatLastManeuverNotification</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Call of this function is used to trigger the navigator to repeat the last maneuver notification based on the current position.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setBorderCrossingWarningListener(com.here.sdk.navigation.BorderCrossingWarningListener)">setBorderCrossingWarningListener</a><wbr/>(<a href="sdk-for-android-navigate-bordercrossingwarninglistener" title="interface in com.here.sdk.navigation">BorderCrossingWarningListener</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the listener to receive notifications about border crossings on the current road.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setBorderCrossingWarningOptions(com.here.sdk.navigation.BorderCrossingWarningOptions)">setBorderCrossingWarningOptions</a><wbr/>(<a href="sdk-for-android-navigate-bordercrossingwarningoptions" title="class in com.here.sdk.navigation">BorderCrossingWarningOptions</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets border crossing warning options to be passed to <a href="sdk-for-android-navigate-bordercrossingwarninglistener" title="interface in com.here.sdk.navigation"><code>BorderCrossingWarningListener</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setCurrentSituationLaneAssistanceViewListener(com.here.sdk.navigation.CurrentSituationLaneAssistanceViewListener)">setCurrentSituationLaneAssistanceViewListener</a><wbr/>(<a href="sdk-for-android-navigate-currentsituationlaneassistanceviewlistener" title="interface in com.here.sdk.navigation">CurrentSituationLaneAssistanceViewListener</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the listener  to receive current situation lane assistance view notifications.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setCustomOption(java.lang.String,java.lang.String)">setCustomOption</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">This method sets custom options that controls navigator behavior.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setDangerZoneWarningListener(com.here.sdk.navigation.DangerZoneWarningListener)">setDangerZoneWarningListener</a><wbr/>(<a href="sdk-for-android-navigate-dangerzonewarninglistener" title="interface in com.here.sdk.navigation">DangerZoneWarningListener</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the listener to receive current danger zones notifications.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setDestinationReachedListener(com.here.sdk.navigation.DestinationReachedListener)">setDestinationReachedListener</a><wbr/>(<a href="sdk-for-android-navigate-destinationreachedlistener" title="interface in com.here.sdk.navigation">DestinationReachedListener</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the listener that notify when the destination has been reached.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setEnableTunnelExtrapolation(boolean)">setEnableTunnelExtrapolation</a><wbr/>(boolean value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Set to <code>true</code> to enable tunnel extrapolation, set to <code>false</code> to disable tunnel extrapolation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setEnvironmentalZoneWarningListener(com.here.sdk.navigation.EnvironmentalZoneWarningListener)">setEnvironmentalZoneWarningListener</a><wbr/>(<a href="sdk-for-android-navigate-environmentalzonewarninglistener" title="interface in com.here.sdk.navigation">EnvironmentalZoneWarningListener</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the listener to receive current environmental zones notifications.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setEventTextListener(com.here.sdk.navigation.EventTextListener)">setEventTextListener</a><wbr/>(<a href="sdk-for-android-navigate-eventtextlistener" title="interface in com.here.sdk.navigation">EventTextListener</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the listener that notifies when a text notification is available.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setEventTextOptions(com.here.sdk.navigation.EventTextOptions)">setEventTextOptions</a><wbr/>(<a href="sdk-for-android-navigate-eventtextoptions" title="class in com.here.sdk.navigation">EventTextOptions</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the text notification options.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setJunctionViewLaneAssistanceListener(com.here.sdk.navigation.JunctionViewLaneAssistanceListener)">setJunctionViewLaneAssistanceListener</a><wbr/>(<a href="sdk-for-android-navigate-junctionviewlaneassistancelistener" title="interface in com.here.sdk.navigation">JunctionViewLaneAssistanceListener</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the listener  to receive junction view lane assistance notifications.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setLowSpeedZoneWarningListener(com.here.sdk.navigation.LowSpeedZoneWarningListener)">setLowSpeedZoneWarningListener</a><wbr/>(<a href="sdk-for-android-navigate-lowspeedzonewarninglistener" title="interface in com.here.sdk.navigation">LowSpeedZoneWarningListener</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the listener to receive notifications about low speed zones on the current road.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setManeuverNotificationOptions(com.here.sdk.navigation.ManeuverNotificationOptions)">setManeuverNotificationOptions</a><wbr/>(<a href="sdk-for-android-navigate-maneuvernotificationoptions" title="class in com.here.sdk.navigation">ManeuverNotificationOptions</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the maneuver notification options.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setManeuverNotificationTimingOptions(com.here.sdk.transport.TransportMode,com.here.sdk.navigation.TimingProfile,com.here.sdk.navigation.ManeuverNotificationTimingOptions)">setManeuverNotificationTimingOptions</a><wbr/>(<a href="sdk-for-android-navigate-transport-transportmode" title="enum class in com.here.sdk.transport">TransportMode</a> transportMode,
 <a href="sdk-for-android-navigate-timingprofile" title="enum class in com.here.sdk.navigation">TimingProfile</a> timingProfile,
 <a href="sdk-for-android-navigate-maneuvernotificationtimingoptions" title="class in com.here.sdk.navigation">ManeuverNotificationTimingOptions</a> options)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Set timing option values for the combination of transport mode and timing profile.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setManeuverViewLaneAssistanceListener(com.here.sdk.navigation.ManeuverViewLaneAssistanceListener)">setManeuverViewLaneAssistanceListener</a><wbr/>(<a href="sdk-for-android-navigate-maneuverviewlaneassistancelistener" title="interface in com.here.sdk.navigation">ManeuverViewLaneAssistanceListener</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the listener  to receive maneuver view lane assistance notifications.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setMilestoneStatusListener(com.here.sdk.navigation.MilestoneStatusListener)">setMilestoneStatusListener</a><wbr/>(<a href="sdk-for-android-navigate-milestonestatuslistener" title="interface in com.here.sdk.navigation">MilestoneStatusListener</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the listener that notifies when a <a href="sdk-for-android-navigate-milestone" title="class in com.here.sdk.navigation"><code>Milestone</code></a> has been reached or missed.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setNavigableLocationListener(com.here.sdk.navigation.NavigableLocationListener)">setNavigableLocationListener</a><wbr/>(<a href="sdk-for-android-navigate-navigablelocationlistener" title="interface in com.here.sdk.navigation">NavigableLocationListener</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the listener that notifies current location updates.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setOffRoadDestinationReachedListener(com.here.sdk.navigation.OffRoadDestinationReachedListener)">setOffRoadDestinationReachedListener</a><wbr/>(<a href="sdk-for-android-navigate-offroaddestinationreachedlistener" title="interface in com.here.sdk.navigation">OffRoadDestinationReachedListener</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the listener that notifies when the off-road destination has been reached.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setOffRoadProgressListener(com.here.sdk.navigation.OffRoadProgressListener)">setOffRoadProgressListener</a><wbr/>(<a href="sdk-for-android-navigate-offroadprogresslistener" title="interface in com.here.sdk.navigation">OffRoadProgressListener</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the listener that notifies about off-road progress.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setPassthroughWaypointsHandlingEnabled(boolean)">setPassthroughWaypointsHandlingEnabled</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Set to <code>true</code> enables handling of passthrough waypoints, set to <code>false</code> disables handling of passthrough waypoints.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setPostActionListener(com.here.sdk.navigation.PostActionListener)">setPostActionListener</a><wbr/>(<a href="sdk-for-android-navigate-postactionlistener" title="interface in com.here.sdk.navigation">PostActionListener</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the listener  to receive post action notifications, such as a charge action at a charging station.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setRailwayCrossingWarningListener(com.here.sdk.navigation.RailwayCrossingWarningListener)">setRailwayCrossingWarningListener</a><wbr/>(<a href="sdk-for-android-navigate-railwaycrossingwarninglistener" title="interface in com.here.sdk.navigation">RailwayCrossingWarningListener</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the listener to receive notifications about railway crossings on the current road.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setRealisticViewWarningListener(com.here.sdk.navigation.RealisticViewWarningListener)">setRealisticViewWarningListener</a><wbr/>(<a href="sdk-for-android-navigate-realisticviewwarninglistener" title="interface in com.here.sdk.navigation">RealisticViewWarningListener</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the listener to receive notifications about junction views on the current road.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setRealisticViewWarningOptions(com.here.sdk.navigation.RealisticViewWarningOptions)">setRealisticViewWarningOptions</a><wbr/>(<a href="sdk-for-android-navigate-realisticviewwarningoptions" title="class in com.here.sdk.navigation">RealisticViewWarningOptions</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets realistic view warning options that allow to filter realistic views to be passed to
 <a href="sdk-for-android-navigate-realisticviewwarninglistener" title="interface in com.here.sdk.navigation"><code>RealisticViewWarningListener</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setRoadAttributesListener(com.here.sdk.navigation.RoadAttributesListener)">setRoadAttributesListener</a><wbr/>(<a href="sdk-for-android-navigate-roadattributeslistener" title="interface in com.here.sdk.navigation">RoadAttributesListener</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the listener  to receive notifications about attributes of the current road.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setRoadSignWarningListener(com.here.sdk.navigation.RoadSignWarningListener)">setRoadSignWarningListener</a><wbr/>(<a href="sdk-for-android-navigate-roadsignwarninglistener" title="interface in com.here.sdk.navigation">RoadSignWarningListener</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the listener to receive notifications about road signs on the current road.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setRoadSignWarningOptions(com.here.sdk.navigation.RoadSignWarningOptions)">setRoadSignWarningOptions</a><wbr/>(<a href="sdk-for-android-navigate-roadsignwarningoptions" title="class in com.here.sdk.navigation">RoadSignWarningOptions</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets road sign warning options that allow to filter road signs to be passed to <a href="sdk-for-android-navigate-roadsignwarninglistener" title="interface in com.here.sdk.navigation"><code>RoadSignWarningListener</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setRoadTextsListener(com.here.sdk.navigation.RoadTextsListener)">setRoadTextsListener</a><wbr/>(<a href="sdk-for-android-navigate-roadtextslistener" title="interface in com.here.sdk.navigation">RoadTextsListener</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the listener  to receive notifications about the textual attributes of the current road.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setRoute(com.here.sdk.routing.Route)">setRoute</a><wbr/>(<a href="sdk-for-android-navigate-routing-route" title="class in com.here.sdk.routing">Route</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the route to navigate.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setRouteDeviationListener(com.here.sdk.navigation.RouteDeviationListener)">setRouteDeviationListener</a><wbr/>(<a href="sdk-for-android-navigate-routedeviationlistener" title="interface in com.here.sdk.navigation">RouteDeviationListener</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the listener that notifies when deviation from the route is observed.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setRouteProgressListener(com.here.sdk.navigation.RouteProgressListener)">setRouteProgressListener</a><wbr/>(<a href="sdk-for-android-navigate-routeprogresslistener" title="interface in com.here.sdk.navigation">RouteProgressListener</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the listener that notifies when a route progress change occurs.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setSafetyCameraWarningListener(com.here.sdk.navigation.SafetyCameraWarningListener)">setSafetyCameraWarningListener</a><wbr/>(<a href="sdk-for-android-navigate-safetycamerawarninglistener" title="interface in com.here.sdk.navigation">SafetyCameraWarningListener</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the listener  to receive safety camera warning notifications.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setSafetyCameraWarningOptions(com.here.sdk.navigation.SafetyCameraWarningOptions)">setSafetyCameraWarningOptions</a><wbr/>(<a href="sdk-for-android-navigate-safetycamerawarningoptions" title="class in com.here.sdk.navigation">SafetyCameraWarningOptions</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets safety camera warning options to be passed to <a href="sdk-for-android-navigate-safetycamerawarninglistener" title="interface in com.here.sdk.navigation"><code>SafetyCameraWarningListener</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setSchoolZoneWarningListener(com.here.sdk.navigation.SchoolZoneWarningListener)">setSchoolZoneWarningListener</a><wbr/>(<a href="sdk-for-android-navigate-schoolzonewarninglistener" title="interface in com.here.sdk.navigation">SchoolZoneWarningListener</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the listener to receive notifications about school zones on the current road.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setSchoolZoneWarningOptions(com.here.sdk.navigation.SchoolZoneWarningOptions)">setSchoolZoneWarningOptions</a><wbr/>(<a href="sdk-for-android-navigate-schoolzonewarningoptions" title="class in com.here.sdk.navigation">SchoolZoneWarningOptions</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets school zone warning options that allow to configure school zone notifications to be
 passed to <a href="sdk-for-android-navigate-schoolzonewarninglistener" title="interface in com.here.sdk.navigation"><code>SchoolZoneWarningListener</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setSpeedLimitListener(com.here.sdk.navigation.SpeedLimitListener)">setSpeedLimitListener</a><wbr/>(<a href="sdk-for-android-navigate-speedlimitlistener" title="interface in com.here.sdk.navigation">SpeedLimitListener</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the listener  to receive notifications about the speed limit of the current road.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setSpeedWarningListener(com.here.sdk.navigation.SpeedWarningListener)">setSpeedWarningListener</a><wbr/>(<a href="sdk-for-android-navigate-speedwarninglistener" title="interface in com.here.sdk.navigation">SpeedWarningListener</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the listener to receive notifications
 when a speed limit on a road is exceeded or driving speed is restored back to normal.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setSpeedWarningOptions(com.here.sdk.navigation.SpeedWarningOptions)">setSpeedWarningOptions</a><wbr/>(<a href="sdk-for-android-navigate-speedwarningoptions" title="class in com.here.sdk.navigation">SpeedWarningOptions</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the speed warning options.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setTollStopWarningListener(com.here.sdk.navigation.TollStopWarningListener)">setTollStopWarningListener</a><wbr/>(<a href="sdk-for-android-navigate-tollstopwarninglistener" title="interface in com.here.sdk.navigation">TollStopWarningListener</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the listener to receive notifications about
 the upcoming toll stop.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6"><code><a class="member-name-link" href="#setTrackingTransportProfile(com.here.sdk.core.TransportProfile)">setTrackingTransportProfile</a><wbr/>(<a href="sdk-for-android-navigate-core-transportprofile" title="class in com.here.sdk.core">TransportProfile</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setTrackingTransportSpecification(com.here.sdk.transport.TransportSpecification)">setTrackingTransportSpecification</a><wbr/>(<a href="sdk-for-android-navigate-transport-transportspecification" title="class in com.here.sdk.transport">TransportSpecification</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the transport specification for the <a href="sdk-for-android-navigate-navigator" title="class in com.here.sdk.navigation"><code>Navigator</code></a>, when no route is present.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setTrafficMergeWarningListener(com.here.sdk.navigation.TrafficMergeWarningListener)">setTrafficMergeWarningListener</a><wbr/>(<a href="sdk-for-android-navigate-trafficmergewarninglistener" title="interface in com.here.sdk.navigation">TrafficMergeWarningListener</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the listener to receive notifications about
 merging traffic to the current road.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setTrafficMergeWarningOptions(com.here.sdk.navigation.TrafficMergeWarningOptions)">setTrafficMergeWarningOptions</a><wbr/>(<a href="sdk-for-android-navigate-trafficmergewarningoptions" title="class in com.here.sdk.navigation">TrafficMergeWarningOptions</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets merging traffic warning options that allow to configure merging traffic notifications to be
 passed to <a href="sdk-for-android-navigate-trafficmergewarninglistener" title="interface in com.here.sdk.navigation"><code>TrafficMergeWarningListener</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setTrafficOnRoute(com.here.sdk.routing.TrafficOnRoute)">setTrafficOnRoute</a><wbr/>(<a href="sdk-for-android-navigate-routing-trafficonroute" title="class in com.here.sdk.routing">TrafficOnRoute</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the traffic information for the current route.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setTruckRestrictionsWarningListener(com.here.sdk.navigation.TruckRestrictionsWarningListener)">setTruckRestrictionsWarningListener</a><wbr/>(<a href="sdk-for-android-navigate-truckrestrictionswarninglistener" title="interface in com.here.sdk.navigation">TruckRestrictionsWarningListener</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets the listener  to receive notifications about
 truck restrictions on the current road.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setTruckRestrictionsWarningOptions(com.here.sdk.navigation.TruckRestrictionsWarningOptions)">setTruckRestrictionsWarningOptions</a><wbr/>(<a href="sdk-for-android-navigate-truckrestrictionswarningoptions" title="class in com.here.sdk.navigation">TruckRestrictionsWarningOptions</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets truck restrictions warning options that allow to filter truck restrictions to be
 passed to <a href="sdk-for-android-navigate-truckrestrictionswarninglistener" title="interface in com.here.sdk.navigation"><code>TruckRestrictionsWarningListener</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setWarningNotificationDistances(com.here.sdk.navigation.WarningType,com.here.sdk.navigation.WarningNotificationDistances)">setWarningNotificationDistances</a><wbr/>(<a href="sdk-for-android-navigate-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a> warningType,
 <a href="sdk-for-android-navigate-warningnotificationdistances" title="class in com.here.sdk.navigation">WarningNotificationDistances</a> warningNotificationDistances)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Set the warning notification distances for the specified warning types.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.here.sdk.core.LocationListener">Methods inherited from interface com.here.sdk.core.<a href="sdk-for-android-navigate-core-locationlistener" title="interface in com.here.sdk.core">LocationListener</a></h3>
<code><a href="sdk-for-android-navigate-core-locationlistener#onLocationUpdated(com.here.sdk.core.Location)">onLocationUpdated</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="getManeuver(int)">
<h3>getManeuver</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="sdk-for-android-navigate-routing-maneuver" title="class in com.here.sdk.routing">Maneuver</a></span> <span class="element-name">getManeuver</span><wbr/><span class="parameters">(int index)</span></div>
<div class="block"><p>Returns maneuver at the given index.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>index</code> - <p>The index of maneuver requested.</p></dd>
<dt>Returns:</dt>
<dd><p>The maneuver if it exists or otherwise <code>null</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getManeuverNotificationTimingOptions(com.here.sdk.transport.TransportMode,com.here.sdk.navigation.TimingProfile)">
<h3>getManeuverNotificationTimingOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-navigate-maneuvernotificationtimingoptions" title="class in com.here.sdk.navigation">ManeuverNotificationTimingOptions</a></span> <span class="element-name">getManeuverNotificationTimingOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-transport-transportmode" title="enum class in com.here.sdk.transport">TransportMode</a> transportMode,
 @NonNull
 <a href="sdk-for-android-navigate-timingprofile" title="enum class in com.here.sdk.navigation">TimingProfile</a> timingProfile)</span></div>
<div class="block"><p>Returns maneuver notification timing options with default values given the combination of transport mode and timing profile.
 The return value can be used as the base for configuring maneuver notification timings. Configure the relevant attributes
 of this object according to your preferences, and then set it by calling setManeuverNotificationTimingOptions function
 for the same combination of transport mode and timing profile.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transportMode</code> - <p>The transport mode of the timing options.</p></dd>
<dd><code>timingProfile</code> - <p>The timing profile of the timing options.</p></dd>
<dt>Returns:</dt>
<dd><p>The timing options with default values.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setManeuverNotificationTimingOptions(com.here.sdk.transport.TransportMode,com.here.sdk.navigation.TimingProfile,com.here.sdk.navigation.ManeuverNotificationTimingOptions)">
<h3>setManeuverNotificationTimingOptions</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">setManeuverNotificationTimingOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-transport-transportmode" title="enum class in com.here.sdk.transport">TransportMode</a> transportMode,
 @NonNull
 <a href="sdk-for-android-navigate-timingprofile" title="enum class in com.here.sdk.navigation">TimingProfile</a> timingProfile,
 @NonNull
 <a href="sdk-for-android-navigate-maneuvernotificationtimingoptions" title="class in com.here.sdk.navigation">ManeuverNotificationTimingOptions</a> options)</span></div>
<div class="block"><p>Set timing option values for the combination of transport mode and timing profile.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transportMode</code> - <p>The transport mode of the timing options.</p></dd>
<dd><code>timingProfile</code> - <p>The timing profile of the timing options.</p></dd>
<dd><code>options</code> - <p>The timing options.</p></dd>
<dt>Returns:</dt>
<dd><p><code>True</code> if set successfully, <code>false</code> when options has invalid value, see <a href="sdk-for-android-navigate-maneuvernotificationtimingoptions" title="class in com.here.sdk.navigation"><code>ManeuverNotificationTimingOptions</code></a> for
     more details about options.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getWarningNotificationDistances(com.here.sdk.navigation.WarningType)">
<h3>getWarningNotificationDistances</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-navigate-warningnotificationdistances" title="class in com.here.sdk.navigation">WarningNotificationDistances</a></span> <span class="element-name">getWarningNotificationDistances</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a> warningType)</span></div>
<div class="block"><p>Returns the warning notification distances for the requested warning type. The return value can be used as the
 base for configuring warning notification distances. Configure the relevant attributes of this object according
 to your preferences, and then set it by calling <code>setWarningNotificationDistances</code> function with the same
 warning type and the modified warning notification distances object.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>warningType</code> - <p>The warning type for which the notification distances will be returned.</p></dd>
<dt>Returns:</dt>
<dd><p>The notification distances for the given warning type.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setWarningNotificationDistances(com.here.sdk.navigation.WarningType,com.here.sdk.navigation.WarningNotificationDistances)">
<h3>setWarningNotificationDistances</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">setWarningNotificationDistances</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a> warningType,
 @NonNull
 <a href="sdk-for-android-navigate-warningnotificationdistances" title="class in com.here.sdk.navigation">WarningNotificationDistances</a> warningNotificationDistances)</span></div>
<div class="block"><p>Set the warning notification distances for the specified warning types.
 <strong>Note:</strong> The warning notification distances are set for most warners.
 This method can't be used to set the warning notification distance for the School Zone warning type because it is applicable regardless of the timing profile. Use <code>NavigatorInterface.school_zone_warning_options</code> instead.
 Attempting to set the warning notification distances for the school zone warner using the <code>NavigatorInterface.set_warning_notification_distances</code> method will fail and return <code>false</code>.
 Always use <code>SchoolZoneWarningOptions.warning_distance_in_meters</code> to set the warning notification distance for the school zone warner regardless of the <code>TimingProfile</code>.
 If <code>NavigatorInterface.set_warning_notification_distances</code> could be used, this would allow for different distances to be set for each timing profile, which is undesirable.
 Attempting to set the warning notification distances for the traffic merge warner using the <code>NavigatorInterface.set_warning_notification_distances</code> method will fail and return <code>false</code>.
 Always use <code>TrafficMergeWarningOptions.warning_distance_in_meters</code> to set the warning notification distance for the traffic merge warner regardless of the <code>TimingProfile</code>.
 Using the <code>NavigatorInterface.set_warning_notification_distances</code> method will fail and return <code>false</code> to avoid
 seting different distances on each timing profile since the traffic merge warning is only applicable on highways.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>warningType</code> - <p>The warning type for which the warning notification distances will be set.</p></dd>
<dd><code>warningNotificationDistances</code> - <p>The warning notification distances to be set for the specified warning types.</p></dd>
<dt>Returns:</dt>
<dd><p><code>True</code> if set successfully, <code>false</code> when the warning_type is [WarningType.SCHOOL_ZONE] or the options have invalid values,
     see <a href="sdk-for-android-navigate-warningnotificationdistances" title="class in com.here.sdk.navigation"><code>WarningNotificationDistances</code></a> for more details about warning notification distances.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="repeatLastManeuverNotification()">
<h3>repeatLastManeuverNotification</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">repeatLastManeuverNotification</span>()</div>
<div class="block"><p>Call of this function is used to trigger the navigator to repeat the last maneuver notification based on the current position.</p></div>
</section>
</li>
<li>
<section class="detail" id="calculateRemainingDistanceInMeters(com.here.sdk.core.GeoCoordinates)">
<h3>calculateRemainingDistanceInMeters</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">calculateRemainingDistanceInMeters</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates)</span></div>
<div class="block"><p>This method calculates the distance between the current position and given coordinates.
 The coordinates must be on the polyline.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>coordinates</code> - <p>The geographic coordinates of the location.</p></dd>
<dt>Returns:</dt>
<dd><p>distance in meters or null if given coordinates are not on route or given
     coordinates were already traversed.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCustomOption(java.lang.String,java.lang.String)">
<h3>setCustomOption</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setCustomOption</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block"><p>This method sets custom options that controls navigator behavior.
 Unsupported options are silently ignored.
 Undocumented options can change their meaning without going through deprecation process.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - <p>Option name</p></dd>
<dd><code>value</code> - <p>New option value</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRoute()">
<h3>getRoute</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="sdk-for-android-navigate-routing-route" title="class in com.here.sdk.routing">Route</a></span> <span class="element-name">getRoute</span>()</div>
<div class="block"><p>Gets the route that is being navigated.
 </p><p>Gets and sets the route that is being navigated.
 If not set, only the current location information will be
 provided through <a href="sdk-for-android-navigate-navigablelocationlistener" title="interface in com.here.sdk.navigation"><code>NavigableLocationListener</code></a>.
 If set, both route progress (<a href="sdk-for-android-navigate-routeprogresslistener" title="interface in com.here.sdk.navigation"><code>RouteProgressListener</code></a>) and route deviation
 (<a href="sdk-for-android-navigate-routedeviationlistener" title="interface in com.here.sdk.navigation"><code>RouteDeviationListener</code></a>) will receive notifications on updates.
 A route may fail to be set if it is generated by an incompatible engine, in which case the operation has no effect.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The route to navigate.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRoute(com.here.sdk.routing.Route)">
<h3>setRoute</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setRoute</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-routing-route" title="class in com.here.sdk.routing">Route</a> value)</span></div>
<div class="block"><p>Sets the route to navigate.
 </p><p>Gets and sets the route that is being navigated.
 If not set, only the current location information will be
 provided through <a href="sdk-for-android-navigate-navigablelocationlistener" title="interface in com.here.sdk.navigation"><code>NavigableLocationListener</code></a>.
 If set, both route progress (<a href="sdk-for-android-navigate-routeprogresslistener" title="interface in com.here.sdk.navigation"><code>RouteProgressListener</code></a>) and route deviation
 (<a href="sdk-for-android-navigate-routedeviationlistener" title="interface in com.here.sdk.navigation"><code>RouteDeviationListener</code></a>) will receive notifications on updates.
 A route may fail to be set if it is generated by an incompatible engine, in which case the operation has no effect.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The route to navigate.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTrackingTransportProfile()">
<h3>getTrackingTransportProfile</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@Nullable
</span><span class="return-type"><a href="sdk-for-android-navigate-core-transportprofile" title="class in com.here.sdk.core">TransportProfile</a></span> <span class="element-name">getTrackingTransportProfile</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use <code>NavigatorInterface.trackingTransportSpecification</code> instead.</p></div>
</div>
<div class="block"><p>Gets the transport profile for the <a href="sdk-for-android-navigate-navigator" title="class in com.here.sdk.navigation"><code>Navigator</code></a>, when no route is present.
 </p><p>Properly setting the transport profile optimizes the navigation experience, and improves resource consumption.
 For example, a <a href="sdk-for-android-navigate-core-transportprofile" title="class in com.here.sdk.core"><code>TransportProfile</code></a> can be defined with a <a href="sdk-for-android-navigate-transport-vehicleprofile" title="class in com.here.sdk.transport"><code>VehicleProfile</code></a>.
 A vehicle profile can have several parameters such as <a href="sdk-for-android-navigate-transport-vehicletype" title="enum class in com.here.sdk.transport"><code>VehicleType</code></a> to set the
 source of information describing the vehicle.
 The default is a <a href="sdk-for-android-navigate-transport-vehicletype#CAR"><code>VehicleType.CAR</code></a> profile.
 </p><p>Currently used members of <a href="sdk-for-android-navigate-core-transportprofile" title="class in com.here.sdk.core"><code>TransportProfile</code></a>
<ul>
<li><a href="sdk-for-android-navigate-transport-vehicletype" title="enum class in com.here.sdk.transport"><code>VehicleType</code></a>: Sets the transport mode.</li>
<li>From <code>vehicleProfile</code>:
 <ul>
<li><code>grossWeightInKilograms</code>: Required for truck related speed information.</li>
<li><code>heightInCentimeters</code>: Required for truck related speed information.</li>
<li><code>widthInCentimeters</code>: Additional truck definition for more specific truck speed information.</li>
<li><code>lengthInCentimeters</code>: Additional truck definition for more specific truck speed information.</li>
</ul>
</li>
</ul></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Defines the transport profile for the <a href="sdk-for-android-navigate-navigator" title="class in com.here.sdk.navigation"><code>Navigator</code></a>, when no route is present.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTrackingTransportProfile(com.here.sdk.core.TransportProfile)">
<h3>setTrackingTransportProfile</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="return-type">void</span> <span class="element-name">setTrackingTransportProfile</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-core-transportprofile" title="class in com.here.sdk.core">TransportProfile</a> value)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use <code>NavigatorInterface.trackingTransportSpecification</code> instead.</p></div>
</div>
<div class="block"><p>Sets the transport profile for the <a href="sdk-for-android-navigate-navigator" title="class in com.here.sdk.navigation"><code>Navigator</code></a>, when no route is present.
 </p><p>Properly setting the transport profile optimizes the navigation experience, and improves resource consumption.
 For example, a <a href="sdk-for-android-navigate-core-transportprofile" title="class in com.here.sdk.core"><code>TransportProfile</code></a> can be defined with a <a href="sdk-for-android-navigate-transport-vehicleprofile" title="class in com.here.sdk.transport"><code>VehicleProfile</code></a>.
 A vehicle profile can have several parameters such as <a href="sdk-for-android-navigate-transport-vehicletype" title="enum class in com.here.sdk.transport"><code>VehicleType</code></a> to set the
 source of information describing the vehicle.
 The default is a <a href="sdk-for-android-navigate-transport-vehicletype#CAR"><code>VehicleType.CAR</code></a> profile.
 </p><p>Currently used members of <a href="sdk-for-android-navigate-core-transportprofile" title="class in com.here.sdk.core"><code>TransportProfile</code></a>
<ul>
<li><a href="sdk-for-android-navigate-transport-vehicletype" title="enum class in com.here.sdk.transport"><code>VehicleType</code></a>: Sets the transport mode.</li>
<li>From <code>vehicleProfile</code>:
 <ul>
<li><code>grossWeightInKilograms</code>: Required for truck related speed information.</li>
<li><code>heightInCentimeters</code>: Required for truck related speed information.</li>
<li><code>widthInCentimeters</code>: Additional truck definition for more specific truck speed information.</li>
<li><code>lengthInCentimeters</code>: Additional truck definition for more specific truck speed information.</li>
</ul>
</li>
</ul></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Defines the transport profile for the <a href="sdk-for-android-navigate-navigator" title="class in com.here.sdk.navigation"><code>Navigator</code></a>, when no route is present.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTrackingTransportSpecification()">
<h3>getTrackingTransportSpecification</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="sdk-for-android-navigate-transport-transportspecification" title="class in com.here.sdk.transport">TransportSpecification</a></span> <span class="element-name">getTrackingTransportSpecification</span>()</div>
<div class="block"><p>Gets the transport specification for the <a href="sdk-for-android-navigate-navigator" title="class in com.here.sdk.navigation"><code>Navigator</code></a>, when no route is present.
 </p><p>Properly setting the transport specification optimizes the navigation experience, and improves
 resource consumption. An <a href="sdk-for-android-navigate-transport-transportspecification" title="class in com.here.sdk.transport"><code>TransportSpecification</code></a> must have the <a href="sdk-for-android-navigate-transport-transportspecification#transportMode"><code>TransportSpecification.transportMode</code></a> set.
 A transport specification can have several parameters defined such as <a href="sdk-for-android-navigate-transport-vehiclespecification#lengthInCentimeters"><code>VehicleSpecification.lengthInCentimeters</code></a>
 defined in <a href="sdk-for-android-navigate-transport-transportspecification#vehicleSpecification"><code>TransportSpecification.vehicleSpecification</code></a> to set the source of information describing the vehicle.
 By default the <a href="sdk-for-android-navigate-transport-transportspecification" title="class in com.here.sdk.transport"><code>TransportSpecification</code></a> will have the transport mode set to <a href="sdk-for-android-navigate-transport-transportmode#CAR"><code>TransportMode.CAR</code></a>.
 </p><p>Currently used members of <a href="sdk-for-android-navigate-transport-transportspecification" title="class in com.here.sdk.transport"><code>TransportSpecification</code></a>
<ul>
<li><a href="sdk-for-android-navigate-transport-transportspecification#transportMode"><code>TransportSpecification.transportMode</code></a>: Sets the transport mode.</li>
<li>From <a href="sdk-for-android-navigate-transport-transportspecification#vehicleSpecification"><code>TransportSpecification.vehicleSpecification</code></a>:
 <ul>
<li><a href="sdk-for-android-navigate-transport-vehiclespecification#grossWeightInKilograms"><code>VehicleSpecification.grossWeightInKilograms</code></a>: Required for truck related speed information.</li>
<li><a href="sdk-for-android-navigate-transport-vehiclespecification#heightInCentimeters"><code>VehicleSpecification.heightInCentimeters</code></a>: Required for truck related speed information.</li>
<li><a href="sdk-for-android-navigate-transport-vehiclespecification#widthInCentimeters"><code>VehicleSpecification.widthInCentimeters</code></a>: Additional truck definition for more specific truck speed information.</li>
<li><a href="sdk-for-android-navigate-transport-vehiclespecification#lengthInCentimeters"><code>VehicleSpecification.lengthInCentimeters</code></a>: Additional truck definition for more specific truck speed information.</li>
</ul>
</li>
</ul></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Defines the transport specification for the <a href="sdk-for-android-navigate-navigator" title="class in com.here.sdk.navigation"><code>Navigator</code></a>, when no route is present.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTrackingTransportSpecification(com.here.sdk.transport.TransportSpecification)">
<h3>setTrackingTransportSpecification</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setTrackingTransportSpecification</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-transport-transportspecification" title="class in com.here.sdk.transport">TransportSpecification</a> value)</span></div>
<div class="block"><p>Sets the transport specification for the <a href="sdk-for-android-navigate-navigator" title="class in com.here.sdk.navigation"><code>Navigator</code></a>, when no route is present.
 </p><p>Properly setting the transport specification optimizes the navigation experience, and improves
 resource consumption. An <a href="sdk-for-android-navigate-transport-transportspecification" title="class in com.here.sdk.transport"><code>TransportSpecification</code></a> must have the <a href="sdk-for-android-navigate-transport-transportspecification#transportMode"><code>TransportSpecification.transportMode</code></a> set.
 A transport specification can have several parameters defined such as <a href="sdk-for-android-navigate-transport-vehiclespecification#lengthInCentimeters"><code>VehicleSpecification.lengthInCentimeters</code></a>
 defined in <a href="sdk-for-android-navigate-transport-transportspecification#vehicleSpecification"><code>TransportSpecification.vehicleSpecification</code></a> to set the source of information describing the vehicle.
 By default the <a href="sdk-for-android-navigate-transport-transportspecification" title="class in com.here.sdk.transport"><code>TransportSpecification</code></a> will have the transport mode set to <a href="sdk-for-android-navigate-transport-transportmode#CAR"><code>TransportMode.CAR</code></a>.
 </p><p>Currently used members of <a href="sdk-for-android-navigate-transport-transportspecification" title="class in com.here.sdk.transport"><code>TransportSpecification</code></a>
<ul>
<li><a href="sdk-for-android-navigate-transport-transportspecification#transportMode"><code>TransportSpecification.transportMode</code></a>: Sets the transport mode.</li>
<li>From <a href="sdk-for-android-navigate-transport-transportspecification#vehicleSpecification"><code>TransportSpecification.vehicleSpecification</code></a>:
 <ul>
<li><a href="sdk-for-android-navigate-transport-vehiclespecification#grossWeightInKilograms"><code>VehicleSpecification.grossWeightInKilograms</code></a>: Required for truck related speed information.</li>
<li><a href="sdk-for-android-navigate-transport-vehiclespecification#heightInCentimeters"><code>VehicleSpecification.heightInCentimeters</code></a>: Required for truck related speed information.</li>
<li><a href="sdk-for-android-navigate-transport-vehiclespecification#widthInCentimeters"><code>VehicleSpecification.widthInCentimeters</code></a>: Additional truck definition for more specific truck speed information.</li>
<li><a href="sdk-for-android-navigate-transport-vehiclespecification#lengthInCentimeters"><code>VehicleSpecification.lengthInCentimeters</code></a>: Additional truck definition for more specific truck speed information.</li>
</ul>
</li>
</ul></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Defines the transport specification for the <a href="sdk-for-android-navigate-navigator" title="class in com.here.sdk.navigation"><code>Navigator</code></a>, when no route is present.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNavigableLocationListener()">
<h3>getNavigableLocationListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="sdk-for-android-navigate-navigablelocationlistener" title="interface in com.here.sdk.navigation">NavigableLocationListener</a></span> <span class="element-name">getNavigableLocationListener</span>()</div>
<div class="block"><p>Gets the listener that notifies current location updates.
 </p><p>It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Object to receive notifications about the current location.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setNavigableLocationListener(com.here.sdk.navigation.NavigableLocationListener)">
<h3>setNavigableLocationListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setNavigableLocationListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-navigablelocationlistener" title="interface in com.here.sdk.navigation">NavigableLocationListener</a> value)</span></div>
<div class="block"><p>Sets the listener that notifies current location updates.
 </p><p>It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about the current location.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRouteProgressListener()">
<h3>getRouteProgressListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="sdk-for-android-navigate-routeprogresslistener" title="interface in com.here.sdk.navigation">RouteProgressListener</a></span> <span class="element-name">getRouteProgressListener</span>()</div>
<div class="block"><p>Gets the listener that notifies when a route progress change occurs.
 </p><p>Route progress notifications only occurs if the route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Object to receive notifications about navigation route progress.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRouteProgressListener(com.here.sdk.navigation.RouteProgressListener)">
<h3>setRouteProgressListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setRouteProgressListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-routeprogresslistener" title="interface in com.here.sdk.navigation">RouteProgressListener</a> value)</span></div>
<div class="block"><p>Sets the listener that notifies when a route progress change occurs.
 </p><p>Route progress notifications only occurs if the route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about navigation route progress.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRouteDeviationListener()">
<h3>getRouteDeviationListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="sdk-for-android-navigate-routedeviationlistener" title="interface in com.here.sdk.navigation">RouteDeviationListener</a></span> <span class="element-name">getRouteDeviationListener</span>()</div>
<div class="block"><p>Gets the listener that notifies when deviation from the route is observed.
 </p><p>Route deviation notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Object to receive notifications about deviations from the route if any occurs.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRouteDeviationListener(com.here.sdk.navigation.RouteDeviationListener)">
<h3>setRouteDeviationListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setRouteDeviationListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-routedeviationlistener" title="interface in com.here.sdk.navigation">RouteDeviationListener</a> value)</span></div>
<div class="block"><p>Sets the listener that notifies when deviation from the route is observed.
 </p><p>Route deviation notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about deviations from the route if any occurs.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEventTextListener()">
<h3>getEventTextListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="sdk-for-android-navigate-eventtextlistener" title="interface in com.here.sdk.navigation">EventTextListener</a></span> <span class="element-name">getEventTextListener</span>()</div>
<div class="block"><p>Gets the listener that notifies when a text notification is available.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.
 <strong>Note:</strong> In order to receive the text notification emitted for the traffic merge warner,
 when <code>TrafficMergeWarningOptions.enable_text_notification</code> has been enabled, the <code>sdk.navigation.EventTextListener</code> must be enabled as well.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Object to receive text notifications when they are available.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setEventTextListener(com.here.sdk.navigation.EventTextListener)">
<h3>setEventTextListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setEventTextListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-eventtextlistener" title="interface in com.here.sdk.navigation">EventTextListener</a> value)</span></div>
<div class="block"><p>Sets the listener that notifies when a text notification is available.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.
 <strong>Note:</strong> In order to receive the text notification emitted for the traffic merge warner,
 when <code>TrafficMergeWarningOptions.enable_text_notification</code> has been enabled, the <code>sdk.navigation.EventTextListener</code> must be enabled as well.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive text notifications when they are available.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMilestoneStatusListener()">
<h3>getMilestoneStatusListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="sdk-for-android-navigate-milestonestatuslistener" title="interface in com.here.sdk.navigation">MilestoneStatusListener</a></span> <span class="element-name">getMilestoneStatusListener</span>()</div>
<div class="block"><p>Gets the listener that notifies when a <a href="sdk-for-android-navigate-milestone" title="class in com.here.sdk.navigation"><code>Milestone</code></a> has been reached or missed.
 </p><p>It informs on all waypoints (passed or missed) that
 are of type <a href="sdk-for-android-navigate-milestonetype#STOPOVER"><code>MilestoneType.STOPOVER</code></a> but excludes the
 starting waypoint.
 Waypoints of type <a href="sdk-for-android-navigate-milestonetype#PASSTHROUGH"><code>MilestoneType.PASSTHROUGH</code></a> are excluded, by default,
 but can be included via <a href="#isPassthroughWaypointsHandlingEnabled()"><code>isPassthroughWaypointsHandlingEnabled()</code></a>.
 Milestone status notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Object to receive notifications about the arrival at each <a href="sdk-for-android-navigate-milestone" title="class in com.here.sdk.navigation"><code>Milestone</code></a> or missing it.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMilestoneStatusListener(com.here.sdk.navigation.MilestoneStatusListener)">
<h3>setMilestoneStatusListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setMilestoneStatusListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-milestonestatuslistener" title="interface in com.here.sdk.navigation">MilestoneStatusListener</a> value)</span></div>
<div class="block"><p>Sets the listener that notifies when a <a href="sdk-for-android-navigate-milestone" title="class in com.here.sdk.navigation"><code>Milestone</code></a> has been reached or missed.
 </p><p>It informs on all waypoints (passed or missed) that
 are of type <a href="sdk-for-android-navigate-milestonetype#STOPOVER"><code>MilestoneType.STOPOVER</code></a> but excludes the
 starting waypoint.
 Waypoints of type <a href="sdk-for-android-navigate-milestonetype#PASSTHROUGH"><code>MilestoneType.PASSTHROUGH</code></a> are excluded, by default,
 but can be included via <a href="#isPassthroughWaypointsHandlingEnabled()"><code>isPassthroughWaypointsHandlingEnabled()</code></a>.
 Milestone status notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about the arrival at each <a href="sdk-for-android-navigate-milestone" title="class in com.here.sdk.navigation"><code>Milestone</code></a> or missing it.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDestinationReachedListener()">
<h3>getDestinationReachedListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="sdk-for-android-navigate-destinationreachedlistener" title="interface in com.here.sdk.navigation">DestinationReachedListener</a></span> <span class="element-name">getDestinationReachedListener</span>()</div>
<div class="block"><p>Gets the listener that notify when the destination has been reached.
 </p><p>Destination reached notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Object to receive the notification about the arrival at the destination.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDestinationReachedListener(com.here.sdk.navigation.DestinationReachedListener)">
<h3>setDestinationReachedListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setDestinationReachedListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-destinationreachedlistener" title="interface in com.here.sdk.navigation">DestinationReachedListener</a> value)</span></div>
<div class="block"><p>Sets the listener that notify when the destination has been reached.
 </p><p>Destination reached notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive the notification about the arrival at the destination.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSpeedWarningListener()">
<h3>getSpeedWarningListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="sdk-for-android-navigate-speedwarninglistener" title="interface in com.here.sdk.navigation">SpeedWarningListener</a></span> <span class="element-name">getSpeedWarningListener</span>()</div>
<div class="block"><p>Gets the listener to receive notifications
 when a speed limit on a road is exceeded or driving speed is restored back to normal.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Object to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSpeedWarningListener(com.here.sdk.navigation.SpeedWarningListener)">
<h3>setSpeedWarningListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setSpeedWarningListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-speedwarninglistener" title="interface in com.here.sdk.navigation">SpeedWarningListener</a> value)</span></div>
<div class="block"><p>Sets the listener to receive notifications
 when a speed limit on a road is exceeded or driving speed is restored back to normal.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getManeuverViewLaneAssistanceListener()">
<h3>getManeuverViewLaneAssistanceListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="sdk-for-android-navigate-maneuverviewlaneassistancelistener" title="interface in com.here.sdk.navigation">ManeuverViewLaneAssistanceListener</a></span> <span class="element-name">getManeuverViewLaneAssistanceListener</span>()</div>
<div class="block"><p>Gets the listener  to receive maneuver view lane assistance notifications.
 </p><p>Maneuver view lane assistance notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Object to receive maneuver view lane assistance notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setManeuverViewLaneAssistanceListener(com.here.sdk.navigation.ManeuverViewLaneAssistanceListener)">
<h3>setManeuverViewLaneAssistanceListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setManeuverViewLaneAssistanceListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-maneuverviewlaneassistancelistener" title="interface in com.here.sdk.navigation">ManeuverViewLaneAssistanceListener</a> value)</span></div>
<div class="block"><p>Sets the listener  to receive maneuver view lane assistance notifications.
 </p><p>Maneuver view lane assistance notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive maneuver view lane assistance notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCurrentSituationLaneAssistanceViewListener()">
<h3>getCurrentSituationLaneAssistanceViewListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="sdk-for-android-navigate-currentsituationlaneassistanceviewlistener" title="interface in com.here.sdk.navigation">CurrentSituationLaneAssistanceViewListener</a></span> <span class="element-name">getCurrentSituationLaneAssistanceViewListener</span>()</div>
<div class="block"><p>Gets the listener  to receive current situation lane assistance view notifications.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Object to receive current situation lane assistance view notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCurrentSituationLaneAssistanceViewListener(com.here.sdk.navigation.CurrentSituationLaneAssistanceViewListener)">
<h3>setCurrentSituationLaneAssistanceViewListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setCurrentSituationLaneAssistanceViewListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-currentsituationlaneassistanceviewlistener" title="interface in com.here.sdk.navigation">CurrentSituationLaneAssistanceViewListener</a> value)</span></div>
<div class="block"><p>Sets the listener  to receive current situation lane assistance view notifications.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive current situation lane assistance view notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEnvironmentalZoneWarningListener()">
<h3>getEnvironmentalZoneWarningListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="sdk-for-android-navigate-environmentalzonewarninglistener" title="interface in com.here.sdk.navigation">EnvironmentalZoneWarningListener</a></span> <span class="element-name">getEnvironmentalZoneWarningListener</span>()</div>
<div class="block"><p>Gets the listener to receive current environmental zones notifications.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Object to receive notification on approaching environmental zones.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setEnvironmentalZoneWarningListener(com.here.sdk.navigation.EnvironmentalZoneWarningListener)">
<h3>setEnvironmentalZoneWarningListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setEnvironmentalZoneWarningListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-environmentalzonewarninglistener" title="interface in com.here.sdk.navigation">EnvironmentalZoneWarningListener</a> value)</span></div>
<div class="block"><p>Sets the listener to receive current environmental zones notifications.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notification on approaching environmental zones.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getJunctionViewLaneAssistanceListener()">
<h3>getJunctionViewLaneAssistanceListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="sdk-for-android-navigate-junctionviewlaneassistancelistener" title="interface in com.here.sdk.navigation">JunctionViewLaneAssistanceListener</a></span> <span class="element-name">getJunctionViewLaneAssistanceListener</span>()</div>
<div class="block"><p>Gets the listener  to receive junction view lane assistance notifications.
 </p><p>Junction view lane assistance notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Object to receive junction view lane assistance notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setJunctionViewLaneAssistanceListener(com.here.sdk.navigation.JunctionViewLaneAssistanceListener)">
<h3>setJunctionViewLaneAssistanceListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setJunctionViewLaneAssistanceListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-junctionviewlaneassistancelistener" title="interface in com.here.sdk.navigation">JunctionViewLaneAssistanceListener</a> value)</span></div>
<div class="block"><p>Sets the listener  to receive junction view lane assistance notifications.
 </p><p>Junction view lane assistance notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive junction view lane assistance notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSafetyCameraWarningListener()">
<h3>getSafetyCameraWarningListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="sdk-for-android-navigate-safetycamerawarninglistener" title="interface in com.here.sdk.navigation">SafetyCameraWarningListener</a></span> <span class="element-name">getSafetyCameraWarningListener</span>()</div>
<div class="block"><p>Gets the listener  to receive safety camera warning notifications.
 </p><p>If a listener  is present, notifications about
 safety speed cameras will be also sent via <a href="sdk-for-android-navigate-safetycamerawarninglistener" title="interface in com.here.sdk.navigation"><code>SafetyCameraWarningListener</code></a>.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Object to receive safety camera warner notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSafetyCameraWarningListener(com.here.sdk.navigation.SafetyCameraWarningListener)">
<h3>setSafetyCameraWarningListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setSafetyCameraWarningListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-safetycamerawarninglistener" title="interface in com.here.sdk.navigation">SafetyCameraWarningListener</a> value)</span></div>
<div class="block"><p>Sets the listener  to receive safety camera warning notifications.
 </p><p>If a listener  is present, notifications about
 safety speed cameras will be also sent via <a href="sdk-for-android-navigate-safetycamerawarninglistener" title="interface in com.here.sdk.navigation"><code>SafetyCameraWarningListener</code></a>.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive safety camera warner notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSafetyCameraWarningOptions()">
<h3>getSafetyCameraWarningOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-navigate-safetycamerawarningoptions" title="class in com.here.sdk.navigation">SafetyCameraWarningOptions</a></span> <span class="element-name">getSafetyCameraWarningOptions</span>()</div>
<div class="block"><p>Gets safety camera warning options to be passed to <a href="sdk-for-android-navigate-safetycamerawarninglistener" title="interface in com.here.sdk.navigation"><code>SafetyCameraWarningListener</code></a>.
 </p><p>These options allow the enabling or disabling the text notification for the warner.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Safety camera warning options to be passed to <a href="sdk-for-android-navigate-safetycamerawarninglistener" title="interface in com.here.sdk.navigation"><code>SafetyCameraWarningListener</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSafetyCameraWarningOptions(com.here.sdk.navigation.SafetyCameraWarningOptions)">
<h3>setSafetyCameraWarningOptions</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setSafetyCameraWarningOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-safetycamerawarningoptions" title="class in com.here.sdk.navigation">SafetyCameraWarningOptions</a> value)</span></div>
<div class="block"><p>Sets safety camera warning options to be passed to <a href="sdk-for-android-navigate-safetycamerawarninglistener" title="interface in com.here.sdk.navigation"><code>SafetyCameraWarningListener</code></a>.
 </p><p>These options allow the enabling or disabling the text notification for the warner.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Safety camera warning options to be passed to <a href="sdk-for-android-navigate-safetycamerawarninglistener" title="interface in com.here.sdk.navigation"><code>SafetyCameraWarningListener</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDangerZoneWarningListener()">
<h3>getDangerZoneWarningListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="sdk-for-android-navigate-dangerzonewarninglistener" title="interface in com.here.sdk.navigation">DangerZoneWarningListener</a></span> <span class="element-name">getDangerZoneWarningListener</span>()</div>
<div class="block"><p>Gets the listener to receive current danger zones notifications.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Object to receive notification on approaching danger zones.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDangerZoneWarningListener(com.here.sdk.navigation.DangerZoneWarningListener)">
<h3>setDangerZoneWarningListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setDangerZoneWarningListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-dangerzonewarninglistener" title="interface in com.here.sdk.navigation">DangerZoneWarningListener</a> value)</span></div>
<div class="block"><p>Sets the listener to receive current danger zones notifications.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notification on approaching danger zones.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTruckRestrictionsWarningListener()">
<h3>getTruckRestrictionsWarningListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="sdk-for-android-navigate-truckrestrictionswarninglistener" title="interface in com.here.sdk.navigation">TruckRestrictionsWarningListener</a></span> <span class="element-name">getTruckRestrictionsWarningListener</span>()</div>
<div class="block"><p>Gets the listener  to receive notifications about
 truck restrictions on the current road.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Object to receive notifications about truck restrictions on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTruckRestrictionsWarningListener(com.here.sdk.navigation.TruckRestrictionsWarningListener)">
<h3>setTruckRestrictionsWarningListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setTruckRestrictionsWarningListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-truckrestrictionswarninglistener" title="interface in com.here.sdk.navigation">TruckRestrictionsWarningListener</a> value)</span></div>
<div class="block"><p>Sets the listener  to receive notifications about
 truck restrictions on the current road.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about truck restrictions on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getWarnerEngine()">
<h3>getWarnerEngine</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-navigate-warner-warnerengine" title="class in com.here.sdk.warner">WarnerEngine</a></span> <span class="element-name">getWarnerEngine</span>()</div>
<div class="block"><p>Gets the warner engine used by the navigator.
 </p><p>This engine can be used to configure navigation warnings.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Warner engine used by the navigator.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTruckRestrictionsWarningOptions()">
<h3>getTruckRestrictionsWarningOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-navigate-truckrestrictionswarningoptions" title="class in com.here.sdk.navigation">TruckRestrictionsWarningOptions</a></span> <span class="element-name">getTruckRestrictionsWarningOptions</span>()</div>
<div class="block"><p>Gets truck restrictions warning options that allow to filter truck restrictions to be
 passed to <a href="sdk-for-android-navigate-truckrestrictionswarninglistener" title="interface in com.here.sdk.navigation"><code>TruckRestrictionsWarningListener</code></a>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Truck restrictions warning options that allow to filter truck restrictions to be passed to <a href="sdk-for-android-navigate-truckrestrictionswarninglistener" title="interface in com.here.sdk.navigation"><code>TruckRestrictionsWarningListener</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTruckRestrictionsWarningOptions(com.here.sdk.navigation.TruckRestrictionsWarningOptions)">
<h3>setTruckRestrictionsWarningOptions</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setTruckRestrictionsWarningOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-truckrestrictionswarningoptions" title="class in com.here.sdk.navigation">TruckRestrictionsWarningOptions</a> value)</span></div>
<div class="block"><p>Sets truck restrictions warning options that allow to filter truck restrictions to be
 passed to <a href="sdk-for-android-navigate-truckrestrictionswarninglistener" title="interface in com.here.sdk.navigation"><code>TruckRestrictionsWarningListener</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Truck restrictions warning options that allow to filter truck restrictions to be passed to <a href="sdk-for-android-navigate-truckrestrictionswarninglistener" title="interface in com.here.sdk.navigation"><code>TruckRestrictionsWarningListener</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPostActionListener()">
<h3>getPostActionListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="sdk-for-android-navigate-postactionlistener" title="interface in com.here.sdk.navigation">PostActionListener</a></span> <span class="element-name">getPostActionListener</span>()</div>
<div class="block"><p>Gets the listener  to receive post action notifications, such as a charge action at a charging station.
 </p><p>Post actions notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Object to receive post action notifications, such as a charge action at a charging station.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPostActionListener(com.here.sdk.navigation.PostActionListener)">
<h3>setPostActionListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setPostActionListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-postactionlistener" title="interface in com.here.sdk.navigation">PostActionListener</a> value)</span></div>
<div class="block"><p>Sets the listener  to receive post action notifications, such as a charge action at a charging station.
 </p><p>Post actions notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive post action notifications, such as a charge action at a charging station.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSpeedLimitListener()">
<h3>getSpeedLimitListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="sdk-for-android-navigate-speedlimitlistener" title="interface in com.here.sdk.navigation">SpeedLimitListener</a></span> <span class="element-name">getSpeedLimitListener</span>()</div>
<div class="block"><p>Gets the listener  to receive notifications about the speed limit of the current road.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Object to receive notifications about the speed limit of the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSpeedLimitListener(com.here.sdk.navigation.SpeedLimitListener)">
<h3>setSpeedLimitListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setSpeedLimitListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-speedlimitlistener" title="interface in com.here.sdk.navigation">SpeedLimitListener</a> value)</span></div>
<div class="block"><p>Sets the listener  to receive notifications about the speed limit of the current road.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about the speed limit of the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRoadTextsListener()">
<h3>getRoadTextsListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="sdk-for-android-navigate-roadtextslistener" title="interface in com.here.sdk.navigation">RoadTextsListener</a></span> <span class="element-name">getRoadTextsListener</span>()</div>
<div class="block"><p>Gets the listener  to receive notifications about the textual attributes of the current road.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Object to receive notifications about the textual attributes of the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRoadTextsListener(com.here.sdk.navigation.RoadTextsListener)">
<h3>setRoadTextsListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setRoadTextsListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-roadtextslistener" title="interface in com.here.sdk.navigation">RoadTextsListener</a> value)</span></div>
<div class="block"><p>Sets the listener  to receive notifications about the textual attributes of the current road.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about the textual attributes of the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRoadAttributesListener()">
<h3>getRoadAttributesListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="sdk-for-android-navigate-roadattributeslistener" title="interface in com.here.sdk.navigation">RoadAttributesListener</a></span> <span class="element-name">getRoadAttributesListener</span>()</div>
<div class="block"><p>Gets the listener  to receive notifications about attributes of the current road.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Object to receive notifications about attributes of the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRoadAttributesListener(com.here.sdk.navigation.RoadAttributesListener)">
<h3>setRoadAttributesListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setRoadAttributesListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-roadattributeslistener" title="interface in com.here.sdk.navigation">RoadAttributesListener</a> value)</span></div>
<div class="block"><p>Sets the listener  to receive notifications about attributes of the current road.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about attributes of the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRoadSignWarningListener()">
<h3>getRoadSignWarningListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="sdk-for-android-navigate-roadsignwarninglistener" title="interface in com.here.sdk.navigation">RoadSignWarningListener</a></span> <span class="element-name">getRoadSignWarningListener</span>()</div>
<div class="block"><p>Gets the listener to receive notifications about road signs on the current road.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Object to receive notifications about road signs on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRoadSignWarningListener(com.here.sdk.navigation.RoadSignWarningListener)">
<h3>setRoadSignWarningListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setRoadSignWarningListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-roadsignwarninglistener" title="interface in com.here.sdk.navigation">RoadSignWarningListener</a> value)</span></div>
<div class="block"><p>Sets the listener to receive notifications about road signs on the current road.
 <strong>Note:</strong> This <code>RoadSignWarningListener</code> will provide
 school zone warnings only in case the speed limit inside the school zone is different than the
 default speed limit applicable for cars outside the school zone. For warnings about school zones
 regardless of their speed limits, the <code>NavigatorInterface.road_sign_warning_listener</code> should be
 used and the <code>RoadSignWarning.type</code> should be checked for value <code>RoadSignType.SCHOOL_ZONE</code>.
 The school zone warner is a zone warner, which means that for a school zone there will <em>always</em> be
 3 warnings emitted, with the <code>SchoolZoneWarning.distance_type</code> set to <code>DistanceType.AHEAD</code>, <code>DistanceType.REACHED</code>
</p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about road signs on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRoadSignWarningOptions()">
<h3>getRoadSignWarningOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-navigate-roadsignwarningoptions" title="class in com.here.sdk.navigation">RoadSignWarningOptions</a></span> <span class="element-name">getRoadSignWarningOptions</span>()</div>
<div class="block"><p>Gets road sign warning options that allow to filter road signs to be passed to <a href="sdk-for-android-navigate-roadsignwarninglistener" title="interface in com.here.sdk.navigation"><code>RoadSignWarningListener</code></a>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Road sign warning options that allow to filter road sings to be passed to <a href="sdk-for-android-navigate-roadsignwarninglistener" title="interface in com.here.sdk.navigation"><code>RoadSignWarningListener</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRoadSignWarningOptions(com.here.sdk.navigation.RoadSignWarningOptions)">
<h3>setRoadSignWarningOptions</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setRoadSignWarningOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-roadsignwarningoptions" title="class in com.here.sdk.navigation">RoadSignWarningOptions</a> value)</span></div>
<div class="block"><p>Sets road sign warning options that allow to filter road signs to be passed to <a href="sdk-for-android-navigate-roadsignwarninglistener" title="interface in com.here.sdk.navigation"><code>RoadSignWarningListener</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Road sign warning options that allow to filter road sings to be passed to <a href="sdk-for-android-navigate-roadsignwarninglistener" title="interface in com.here.sdk.navigation"><code>RoadSignWarningListener</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSchoolZoneWarningListener()">
<h3>getSchoolZoneWarningListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="sdk-for-android-navigate-schoolzonewarninglistener" title="interface in com.here.sdk.navigation">SchoolZoneWarningListener</a></span> <span class="element-name">getSchoolZoneWarningListener</span>()</div>
<div class="block"><p>Gets the listener to receive notifications about school zones on the current road.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 school zones on the current road.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Object to receive notifications about school zones on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSchoolZoneWarningListener(com.here.sdk.navigation.SchoolZoneWarningListener)">
<h3>setSchoolZoneWarningListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setSchoolZoneWarningListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-schoolzonewarninglistener" title="interface in com.here.sdk.navigation">SchoolZoneWarningListener</a> value)</span></div>
<div class="block"><p>Sets the listener to receive notifications about school zones on the current road.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 school zones on the current road.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about school zones on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSchoolZoneWarningOptions()">
<h3>getSchoolZoneWarningOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-navigate-schoolzonewarningoptions" title="class in com.here.sdk.navigation">SchoolZoneWarningOptions</a></span> <span class="element-name">getSchoolZoneWarningOptions</span>()</div>
<div class="block"><p>Gets school zone warning options that allow to configure school zone notifications to be
 passed to <a href="sdk-for-android-navigate-schoolzonewarninglistener" title="interface in com.here.sdk.navigation"><code>SchoolZoneWarningListener</code></a>.
 </p><p>It allow to configure school zone notifications to be passed to
 <a href="sdk-for-android-navigate-schoolzonewarninglistener" title="interface in com.here.sdk.navigation"><code>SchoolZoneWarningListener</code></a>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>School zone warning options</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSchoolZoneWarningOptions(com.here.sdk.navigation.SchoolZoneWarningOptions)">
<h3>setSchoolZoneWarningOptions</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setSchoolZoneWarningOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-schoolzonewarningoptions" title="class in com.here.sdk.navigation">SchoolZoneWarningOptions</a> value)</span></div>
<div class="block"><p>Sets school zone warning options that allow to configure school zone notifications to be
 passed to <a href="sdk-for-android-navigate-schoolzonewarninglistener" title="interface in com.here.sdk.navigation"><code>SchoolZoneWarningListener</code></a>.
 </p><p>It allow to configure school zone notifications to be passed to
 <a href="sdk-for-android-navigate-schoolzonewarninglistener" title="interface in com.here.sdk.navigation"><code>SchoolZoneWarningListener</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>School zone warning options</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRealisticViewWarningListener()">
<h3>getRealisticViewWarningListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="sdk-for-android-navigate-realisticviewwarninglistener" title="interface in com.here.sdk.navigation">RealisticViewWarningListener</a></span> <span class="element-name">getRealisticViewWarningListener</span>()</div>
<div class="block"><p>Gets the listener to receive notifications about junction views on the current road.
 </p><p>Setting <code>null</code> value to the listener will unset
 the listener.
 This feature requires a map version greater or equal to 67 in order to function properly.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Object to receive notifications about junction views on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRealisticViewWarningListener(com.here.sdk.navigation.RealisticViewWarningListener)">
<h3>setRealisticViewWarningListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setRealisticViewWarningListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-realisticviewwarninglistener" title="interface in com.here.sdk.navigation">RealisticViewWarningListener</a> value)</span></div>
<div class="block"><p>Sets the listener to receive notifications about junction views on the current road.
 </p><p>Setting <code>null</code> value to the listener will unset
 the listener.
 This feature requires a map version greater or equal to 67 in order to function properly.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about junction views on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRealisticViewWarningOptions()">
<h3>getRealisticViewWarningOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-navigate-realisticviewwarningoptions" title="class in com.here.sdk.navigation">RealisticViewWarningOptions</a></span> <span class="element-name">getRealisticViewWarningOptions</span>()</div>
<div class="block"><p>Gets realistic view warning options that allow to filter realistic views to be passed to
 <a href="sdk-for-android-navigate-realisticviewwarninglistener" title="interface in com.here.sdk.navigation"><code>RealisticViewWarningListener</code></a>.
 </p><p>It allow to filter realistic views to be passed to <a href="sdk-for-android-navigate-realisticviewwarninglistener" title="interface in com.here.sdk.navigation"><code>RealisticViewWarningListener</code></a>.
 <ul>
<li>This feature requires a map version greater or equal to 67 in order to function properly.</li>
</ul></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Realistic view warning options.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRealisticViewWarningOptions(com.here.sdk.navigation.RealisticViewWarningOptions)">
<h3>setRealisticViewWarningOptions</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setRealisticViewWarningOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-realisticviewwarningoptions" title="class in com.here.sdk.navigation">RealisticViewWarningOptions</a> value)</span></div>
<div class="block"><p>Sets realistic view warning options that allow to filter realistic views to be passed to
 <a href="sdk-for-android-navigate-realisticviewwarninglistener" title="interface in com.here.sdk.navigation"><code>RealisticViewWarningListener</code></a>.
 </p><p>It allow to filter realistic views to be passed to <a href="sdk-for-android-navigate-realisticviewwarninglistener" title="interface in com.here.sdk.navigation"><code>RealisticViewWarningListener</code></a>.
 <ul>
<li>This feature requires a map version greater or equal to 67 in order to function properly.</li>
</ul></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Realistic view warning options.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBorderCrossingWarningListener()">
<h3>getBorderCrossingWarningListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="sdk-for-android-navigate-bordercrossingwarninglistener" title="interface in com.here.sdk.navigation">BorderCrossingWarningListener</a></span> <span class="element-name">getBorderCrossingWarningListener</span>()</div>
<div class="block"><p>Gets the listener to receive notifications about border crossings on the current road.
 </p><p>Border crossing notifications are given only if a route is present.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Object to receive notifications about border crossings on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setBorderCrossingWarningListener(com.here.sdk.navigation.BorderCrossingWarningListener)">
<h3>setBorderCrossingWarningListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setBorderCrossingWarningListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-bordercrossingwarninglistener" title="interface in com.here.sdk.navigation">BorderCrossingWarningListener</a> value)</span></div>
<div class="block"><p>Sets the listener to receive notifications about border crossings on the current road.
 </p><p>Border crossing notifications are given only if a route is present.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about border crossings on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBorderCrossingWarningOptions()">
<h3>getBorderCrossingWarningOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-navigate-bordercrossingwarningoptions" title="class in com.here.sdk.navigation">BorderCrossingWarningOptions</a></span> <span class="element-name">getBorderCrossingWarningOptions</span>()</div>
<div class="block"><p>Gets border crossing warning options to be passed to <a href="sdk-for-android-navigate-bordercrossingwarninglistener" title="interface in com.here.sdk.navigation"><code>BorderCrossingWarningListener</code></a>.
 </p><p>allow the filtering of the border crossing warnings received and set the notification distances.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Border crossing warning options to be passed to <a href="sdk-for-android-navigate-bordercrossingwarninglistener" title="interface in com.here.sdk.navigation"><code>BorderCrossingWarningListener</code></a>. These options</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setBorderCrossingWarningOptions(com.here.sdk.navigation.BorderCrossingWarningOptions)">
<h3>setBorderCrossingWarningOptions</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setBorderCrossingWarningOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-bordercrossingwarningoptions" title="class in com.here.sdk.navigation">BorderCrossingWarningOptions</a> value)</span></div>
<div class="block"><p>Sets border crossing warning options to be passed to <a href="sdk-for-android-navigate-bordercrossingwarninglistener" title="interface in com.here.sdk.navigation"><code>BorderCrossingWarningListener</code></a>.
 </p><p>allow the filtering of the border crossing warnings received and set the notification distances.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Border crossing warning options to be passed to <a href="sdk-for-android-navigate-bordercrossingwarninglistener" title="interface in com.here.sdk.navigation"><code>BorderCrossingWarningListener</code></a>. These options</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTollStopWarningListener()">
<h3>getTollStopWarningListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="sdk-for-android-navigate-tollstopwarninglistener" title="interface in com.here.sdk.navigation">TollStopWarningListener</a></span> <span class="element-name">getTollStopWarningListener</span>()</div>
<div class="block"><p>Gets the listener to receive notifications about
 the the upcoming toll stop.
 </p><p>Setting <code>null</code> value to the listener will unset
 the listener.
 This is a <strong>beta release</strong> of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Object to receive information on the upcoming toll stop.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTollStopWarningListener(com.here.sdk.navigation.TollStopWarningListener)">
<h3>setTollStopWarningListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setTollStopWarningListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-tollstopwarninglistener" title="interface in com.here.sdk.navigation">TollStopWarningListener</a> value)</span></div>
<div class="block"><p>Sets the listener to receive notifications about
 the upcoming toll stop.
 </p><p>Setting <code>null</code> value to the listener will unset
 the listener.
 This is a <strong>beta release</strong> of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive information on the upcoming toll stop.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRailwayCrossingWarningListener()">
<h3>getRailwayCrossingWarningListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="sdk-for-android-navigate-railwaycrossingwarninglistener" title="interface in com.here.sdk.navigation">RailwayCrossingWarningListener</a></span> <span class="element-name">getRailwayCrossingWarningListener</span>()</div>
<div class="block"><p>Gets the listener to receive notifications about railway crossings on the current road.
 </p><p>Railway crossing notifications are given regardless if a route is set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Object to receive notifications about railway crossings on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setRailwayCrossingWarningListener(com.here.sdk.navigation.RailwayCrossingWarningListener)">
<h3>setRailwayCrossingWarningListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setRailwayCrossingWarningListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-railwaycrossingwarninglistener" title="interface in com.here.sdk.navigation">RailwayCrossingWarningListener</a> value)</span></div>
<div class="block"><p>Sets the listener to receive notifications about railway crossings on the current road.
 </p><p>Railway crossing notifications are given regardless if a route is set.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about railway crossings on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLowSpeedZoneWarningListener()">
<h3>getLowSpeedZoneWarningListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="sdk-for-android-navigate-lowspeedzonewarninglistener" title="interface in com.here.sdk.navigation">LowSpeedZoneWarningListener</a></span> <span class="element-name">getLowSpeedZoneWarningListener</span>()</div>
<div class="block"><p>Gets the listener to receive notifications about low speed zones on the current road.
 </p><p>Low speed zone notifications are given regardless if a route is set. This listener is currently
 available <em>only</em> for Japan.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Object to receive notifications about low speed zones on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLowSpeedZoneWarningListener(com.here.sdk.navigation.LowSpeedZoneWarningListener)">
<h3>setLowSpeedZoneWarningListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setLowSpeedZoneWarningListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-lowspeedzonewarninglistener" title="interface in com.here.sdk.navigation">LowSpeedZoneWarningListener</a> value)</span></div>
<div class="block"><p>Sets the listener to receive notifications about low speed zones on the current road.
 </p><p>Low speed zone notifications are given regardless if a route is set. This listener is currently
 available <em>only</em> for Japan.
 Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about low speed zones on the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTrafficMergeWarningListener()">
<h3>getTrafficMergeWarningListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="sdk-for-android-navigate-trafficmergewarninglistener" title="interface in com.here.sdk.navigation">TrafficMergeWarningListener</a></span> <span class="element-name">getTrafficMergeWarningListener</span>()</div>
<div class="block"><p>Gets the listener to receive notifications about
 merging traffic to the current road.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Object to receive notifications about merging traffic to the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTrafficMergeWarningListener(com.here.sdk.navigation.TrafficMergeWarningListener)">
<h3>setTrafficMergeWarningListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setTrafficMergeWarningListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-trafficmergewarninglistener" title="interface in com.here.sdk.navigation">TrafficMergeWarningListener</a> value)</span></div>
<div class="block"><p>Sets the listener to receive notifications about
 merging traffic to the current road.
 </p><p>Setting <code>null</code> value to the listener will unset the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive notifications about merging traffic to the current road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTrafficMergeWarningOptions()">
<h3>getTrafficMergeWarningOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-navigate-trafficmergewarningoptions" title="class in com.here.sdk.navigation">TrafficMergeWarningOptions</a></span> <span class="element-name">getTrafficMergeWarningOptions</span>()</div>
<div class="block"><p>Gets merging traffic warning options that allow to configure merging traffic notifications to be
 passed to <a href="sdk-for-android-navigate-trafficmergewarninglistener" title="interface in com.here.sdk.navigation"><code>TrafficMergeWarningListener</code></a>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Merging traffic warning options that allow to configure merging traffic notifications to be passed to
     <a href="sdk-for-android-navigate-trafficmergewarninglistener" title="interface in com.here.sdk.navigation"><code>TrafficMergeWarningListener</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTrafficMergeWarningOptions(com.here.sdk.navigation.TrafficMergeWarningOptions)">
<h3>setTrafficMergeWarningOptions</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setTrafficMergeWarningOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-trafficmergewarningoptions" title="class in com.here.sdk.navigation">TrafficMergeWarningOptions</a> value)</span></div>
<div class="block"><p>Sets merging traffic warning options that allow to configure merging traffic notifications to be
 passed to <a href="sdk-for-android-navigate-trafficmergewarninglistener" title="interface in com.here.sdk.navigation"><code>TrafficMergeWarningListener</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Merging traffic warning options that allow to configure merging traffic notifications to be passed to
     <a href="sdk-for-android-navigate-trafficmergewarninglistener" title="interface in com.here.sdk.navigation"><code>TrafficMergeWarningListener</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOffRoadDestinationReachedListener()">
<h3>getOffRoadDestinationReachedListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="sdk-for-android-navigate-offroaddestinationreachedlistener" title="interface in com.here.sdk.navigation">OffRoadDestinationReachedListener</a></span> <span class="element-name">getOffRoadDestinationReachedListener</span>()</div>
<div class="block"><p>Gets the listener that notifies when the off-road destination has been reached.
 </p><p>Off-road destination reached notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset
 the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Object to receive the notification about the arrival at the off-road destination.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOffRoadDestinationReachedListener(com.here.sdk.navigation.OffRoadDestinationReachedListener)">
<h3>setOffRoadDestinationReachedListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setOffRoadDestinationReachedListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-offroaddestinationreachedlistener" title="interface in com.here.sdk.navigation">OffRoadDestinationReachedListener</a> value)</span></div>
<div class="block"><p>Sets the listener that notifies when the off-road destination has been reached.
 </p><p>Off-road destination reached notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset
 the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive the notification about the arrival at the off-road destination.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOffRoadProgressListener()">
<h3>getOffRoadProgressListener</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="sdk-for-android-navigate-offroadprogresslistener" title="interface in com.here.sdk.navigation">OffRoadProgressListener</a></span> <span class="element-name">getOffRoadProgressListener</span>()</div>
<div class="block"><p>Gets the listener that notifies about off-road progress.
 </p><p>Off-road progress notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset
 the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Object to receive the notification about the off-road progress.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOffRoadProgressListener(com.here.sdk.navigation.OffRoadProgressListener)">
<h3>setOffRoadProgressListener</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setOffRoadProgressListener</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-offroadprogresslistener" title="interface in com.here.sdk.navigation">OffRoadProgressListener</a> value)</span></div>
<div class="block"><p>Sets the listener that notifies about off-road progress.
 </p><p>Off-road progress notifications only occurs if a route has been set.
 Setting <code>null</code> value to the listener will unset
 the listener.
 It returns <code>null</code> when no listener is set by an user.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Object to receive the notification about the off-road progress.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getManeuverNotificationOptions()">
<h3>getManeuverNotificationOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-navigate-maneuvernotificationoptions" title="class in com.here.sdk.navigation">ManeuverNotificationOptions</a></span> <span class="element-name">getManeuverNotificationOptions</span>()</div>
<div class="block"><p>Gets the maneuver notification options.
 </p><p>Notifications are only available if a route is present.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Options used for maneuver notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setManeuverNotificationOptions(com.here.sdk.navigation.ManeuverNotificationOptions)">
<h3>setManeuverNotificationOptions</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setManeuverNotificationOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-maneuvernotificationoptions" title="class in com.here.sdk.navigation">ManeuverNotificationOptions</a> value)</span></div>
<div class="block"><p>Sets the maneuver notification options.
 </p><p>Notifications are only available if a route is present.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Options used for maneuver notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getEventTextOptions()">
<h3>getEventTextOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-navigate-eventtextoptions" title="class in com.here.sdk.navigation">EventTextOptions</a></span> <span class="element-name">getEventTextOptions</span>()</div>
<div class="block"><p>Gets the text notification options.
 </p><p>Notifications are only available if a route is present.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Options used for text notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setEventTextOptions(com.here.sdk.navigation.EventTextOptions)">
<h3>setEventTextOptions</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setEventTextOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-eventtextoptions" title="class in com.here.sdk.navigation">EventTextOptions</a> value)</span></div>
<div class="block"><p>Sets the text notification options.
 </p><p>Notifications are only available if a route is present.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Options used for text notifications.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSpeedWarningOptions()">
<h3>getSpeedWarningOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-navigate-speedwarningoptions" title="class in com.here.sdk.navigation">SpeedWarningOptions</a></span> <span class="element-name">getSpeedWarningOptions</span>()</div>
<div class="block"><p>Gets the speed warning options.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Options used for the speed warning feature.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setSpeedWarningOptions(com.here.sdk.navigation.SpeedWarningOptions)">
<h3>setSpeedWarningOptions</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setSpeedWarningOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-speedwarningoptions" title="class in com.here.sdk.navigation">SpeedWarningOptions</a> value)</span></div>
<div class="block"><p>Sets the speed warning options.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Options used for the speed warning feature.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isEnableTunnelExtrapolation()">
<h3>isEnableTunnelExtrapolation</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isEnableTunnelExtrapolation</span>()</div>
<div class="block"><p>Return <code>true</code> if tunnel extrapolation is enabled otherwise <code>false</code>.
 </p><p>By default the tunnel extrapolation is enabled.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Defines whether to enable or disable tunnel extrapolation.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setEnableTunnelExtrapolation(boolean)">
<h3>setEnableTunnelExtrapolation</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setEnableTunnelExtrapolation</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Set to <code>true</code> to enable tunnel extrapolation, set to <code>false</code> to disable tunnel extrapolation.
 </p><p>By default the tunnel extrapolation is enabled.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Defines whether to enable or disable tunnel extrapolation.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isPassthroughWaypointsHandlingEnabled()">
<h3>isPassthroughWaypointsHandlingEnabled</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isPassthroughWaypointsHandlingEnabled</span>()</div>
<div class="block"><p>Return <code>true</code> if handling of passthrough waypoints is enabled, otherwise - <code>false</code>.
 </p><p>By default the handling of passthrough waypoints is disabled.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Defines whether to enable or disable handling of passthrough waypoints.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPassthroughWaypointsHandlingEnabled(boolean)">
<h3>setPassthroughWaypointsHandlingEnabled</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setPassthroughWaypointsHandlingEnabled</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Set to <code>true</code> enables handling of passthrough waypoints, set to <code>false</code> disables handling of passthrough waypoints.
 </p><p>By default the handling of passthrough waypoints is disabled.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Defines whether to enable or disable handling of passthrough waypoints.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTrafficOnRoute()">
<h3>getTrafficOnRoute</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="return-type"><a href="sdk-for-android-navigate-routing-trafficonroute" title="class in com.here.sdk.routing">TrafficOnRoute</a></span> <span class="element-name">getTrafficOnRoute</span>()</div>
<div class="block"><p>Gets the traffic information for the current route.
 </p><p>This impacts <code>RouteProgress</code> updates as the duration of the <code>SectionProgress</code> might change.
 However, the remaining distance and the route geometry will remain unchanged.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Traffic information for the current route.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTrafficOnRoute(com.here.sdk.routing.TrafficOnRoute)">
<h3>setTrafficOnRoute</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setTrafficOnRoute</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-routing-trafficonroute" title="class in com.here.sdk.routing">TrafficOnRoute</a> value)</span></div>
<div class="block"><p>Sets the traffic information for the current route.
 </p><p>This impacts <code>RouteProgress</code> updates as the duration of the <code>SectionProgress</code> might change.
 However, the remaining distance and the route geometry will remain unchanged.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Traffic information for the current route.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLocationManager()">
<h3>getLocationManager</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-navigate-mapmatcher-locationmanager" title="class in com.here.sdk.mapmatcher">LocationManager</a></span> <span class="element-name">getLocationManager</span>()</div>
<div class="block"><p>Gets the location manager instance used by the navigator.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The location manager used by the navigator for map-matched location processing.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
</div>
</div>



</div>
`
}</HTMLBlock>
