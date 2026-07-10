---
title: "NavigatorInterface (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

All Superinterfaces:  
<a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener" title="interface in com.here.sdk.core">`LocationListener`</a>

<!-- -->

All Known Implementing Classes:  
<a href="sdk-for-android-navigate-com-here-sdk-navigation-navigator" title="class in com.here.sdk.navigation">`Navigator`</a>, <a href="sdk-for-android-navigate-com-here-sdk-navigation-visualnavigator" title="class in com.here.sdk.navigation">`VisualNavigator`</a>

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">NavigatorInterface</span><span class="extends-implements"> extends <a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener" title="interface in com.here.sdk.core">LocationListener</a></span>

</div>

<div class="block">

This interface provides the basic functionality needed to run a navigation session.

</div>

</div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div id="sdk-for-android-navigate-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang"><code>Integer</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      calculateRemainingDistanceInMeters ( GeoCoordinates coordinates)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  This method calculates the distance between the current position and given coordinates.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarninglistener" title="interface in com.here.sdk.navigation">`BorderCrossingWarningListener`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getBorderCrossingWarningListener ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the listener to receive notifications about border crossings on the current road.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarningoptions" title="class in com.here.sdk.navigation">`BorderCrossingWarningOptions`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getBorderCrossingWarningOptions ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets border crossing warning options to be passed to BorderCrossingWarningListener .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-currentsituationlaneassistanceviewlistener" title="interface in com.here.sdk.navigation">`CurrentSituationLaneAssistanceViewListener`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getCurrentSituationLaneAssistanceViewListener ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the listener to receive current situation lane assistance view notifications.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-dangerzonewarninglistener" title="interface in com.here.sdk.navigation">`DangerZoneWarningListener`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getDangerZoneWarningListener ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the listener to receive current danger zones notifications.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-destinationreachedlistener" title="interface in com.here.sdk.navigation">`DestinationReachedListener`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getDestinationReachedListener ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the listener that notify when the destination has been reached.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-environmentalzonewarninglistener" title="interface in com.here.sdk.navigation">`EnvironmentalZoneWarningListener`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getEnvironmentalZoneWarningListener ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the listener to receive current environmental zones notifications.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-eventtextlistener" title="interface in com.here.sdk.navigation">`EventTextListener`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getEventTextListener ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the listener that notifies when a text notification is available.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-eventtextoptions" title="class in com.here.sdk.navigation">`EventTextOptions`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getEventTextOptions ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the text notification options.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-junctionviewlaneassistancelistener" title="interface in com.here.sdk.navigation">`JunctionViewLaneAssistanceListener`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getJunctionViewLaneAssistanceListener ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the listener to receive junction view lane assistance notifications.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-locationmanager" title="class in com.here.sdk.mapmatcher">`LocationManager`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getLocationManager ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the location manager instance used by the navigator.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-lowspeedzonewarninglistener" title="interface in com.here.sdk.navigation">`LowSpeedZoneWarningListener`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getLowSpeedZoneWarningListener ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the listener to receive notifications about low speed zones on the current road.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-maneuver" title="class in com.here.sdk.routing">`Maneuver`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getManeuver (int index)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Returns maneuver at the given index.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions" title="class in com.here.sdk.navigation">`ManeuverNotificationOptions`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getManeuverNotificationOptions ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the maneuver notification options.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions" title="class in com.here.sdk.navigation">`ManeuverNotificationTimingOptions`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getManeuverNotificationTimingOptions ( TransportMode transportMode, TimingProfile timingProfile)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Returns maneuver notification timing options with default values given the combination of transport mode and timing profile.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverviewlaneassistancelistener" title="interface in com.here.sdk.navigation">`ManeuverViewLaneAssistanceListener`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getManeuverViewLaneAssistanceListener ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the listener to receive maneuver view lane assistance notifications.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-milestonestatuslistener" title="interface in com.here.sdk.navigation">`MilestoneStatusListener`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getMilestoneStatusListener ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the listener that notifies when a Milestone has been reached or missed.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigablelocationlistener" title="interface in com.here.sdk.navigation">`NavigableLocationListener`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getNavigableLocationListener ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the listener that notifies current location updates.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-offroaddestinationreachedlistener" title="interface in com.here.sdk.navigation">`OffRoadDestinationReachedListener`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getOffRoadDestinationReachedListener ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the listener that notifies when the off-road destination has been reached.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-offroadprogresslistener" title="interface in com.here.sdk.navigation">`OffRoadProgressListener`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getOffRoadProgressListener ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the listener that notifies about off-road progress.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-postactionlistener" title="interface in com.here.sdk.navigation">`PostActionListener`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getPostActionListener ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the listener to receive post action notifications, such as a charge action at a charging station.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-railwaycrossingwarninglistener" title="interface in com.here.sdk.navigation">`RailwayCrossingWarningListener`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getRailwayCrossingWarningListener ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the listener to receive notifications about railway crossings on the current road.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarninglistener" title="interface in com.here.sdk.navigation">`RealisticViewWarningListener`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getRealisticViewWarningListener ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the listener to receive notifications about junction views on the current road.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarningoptions" title="class in com.here.sdk.navigation">`RealisticViewWarningOptions`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getRealisticViewWarningOptions ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets realistic view warning options that allow to filter realistic views to be passed to RealisticViewWarningListener .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadattributeslistener" title="interface in com.here.sdk.navigation">`RoadAttributesListener`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getRoadAttributesListener ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the listener to receive notifications about attributes of the current road.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarninglistener" title="interface in com.here.sdk.navigation">`RoadSignWarningListener`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getRoadSignWarningListener ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the listener to receive notifications about road signs on the current road.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarningoptions" title="class in com.here.sdk.navigation">`RoadSignWarningOptions`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getRoadSignWarningOptions ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets road sign warning options that allow to filter road signs to be passed to RoadSignWarningListener .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadtextslistener" title="interface in com.here.sdk.navigation">`RoadTextsListener`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getRoadTextsListener ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the listener to receive notifications about the textual attributes of the current road.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing">`Route`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getRoute ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the route that is being navigated.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-routedeviationlistener" title="interface in com.here.sdk.navigation">`RouteDeviationListener`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getRouteDeviationListener ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the listener that notifies when deviation from the route is observed.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-routeprogresslistener" title="interface in com.here.sdk.navigation">`RouteProgressListener`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getRouteProgressListener ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the listener that notifies when a route progress change occurs.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-safetycamerawarninglistener" title="interface in com.here.sdk.navigation">`SafetyCameraWarningListener`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getSafetyCameraWarningListener ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the listener to receive safety camera warning notifications.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-safetycamerawarningoptions" title="class in com.here.sdk.navigation">`SafetyCameraWarningOptions`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getSafetyCameraWarningOptions ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets safety camera warning options to be passed to SafetyCameraWarningListener .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-schoolzonewarninglistener" title="interface in com.here.sdk.navigation">`SchoolZoneWarningListener`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getSchoolZoneWarningListener ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the listener to receive notifications about school zones on the current road.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-schoolzonewarningoptions" title="class in com.here.sdk.navigation">`SchoolZoneWarningOptions`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getSchoolZoneWarningOptions ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets school zone warning options that allow to configure school zone notifications to be passed to SchoolZoneWarningListener .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimitlistener" title="interface in com.here.sdk.navigation">`SpeedLimitListener`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getSpeedLimitListener ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the listener to receive notifications about the speed limit of the current road.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedwarninglistener" title="interface in com.here.sdk.navigation">`SpeedWarningListener`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getSpeedWarningListener ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the listener to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedwarningoptions" title="class in com.here.sdk.navigation">`SpeedWarningOptions`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getSpeedWarningOptions ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the speed warning options.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-tollstopwarninglistener" title="interface in com.here.sdk.navigation">`TollStopWarningListener`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getTollStopWarningListener ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the listener to receive notifications about the the upcoming toll stop.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">

  <a href="sdk-for-android-navigate-com-here-sdk-core-transportprofile" title="class in com.here.sdk.core">`TransportProfile`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">

      getTrackingTransportProfile ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-transport-transportspecification" title="class in com.here.sdk.transport">`TransportSpecification`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getTrackingTransportSpecification ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the transport specification for the Navigator , when no route is present.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarninglistener" title="interface in com.here.sdk.navigation">`TrafficMergeWarningListener`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getTrafficMergeWarningListener ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the listener to receive notifications about merging traffic to the current road.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarningoptions" title="class in com.here.sdk.navigation">`TrafficMergeWarningOptions`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getTrafficMergeWarningOptions ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets merging traffic warning options that allow to configure merging traffic notifications to be passed to TrafficMergeWarningListener .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-trafficonroute" title="class in com.here.sdk.routing">`TrafficOnRoute`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getTrafficOnRoute ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the traffic information for the current route.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionswarninglistener" title="interface in com.here.sdk.navigation">`TruckRestrictionsWarningListener`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getTruckRestrictionsWarningListener ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the listener to receive notifications about truck restrictions on the current road.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionswarningoptions" title="class in com.here.sdk.navigation">`TruckRestrictionsWarningOptions`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getTruckRestrictionsWarningOptions ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets truck restrictions warning options that allow to filter truck restrictions to be passed to TruckRestrictionsWarningListener .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-warner-warnerengine" title="class in com.here.sdk.warner">`WarnerEngine`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getWarnerEngine ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Gets the warner engine used by the navigator.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-warningnotificationdistances" title="class in com.here.sdk.navigation">`WarningNotificationDistances`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getWarningNotificationDistances ( WarningType warningType)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Returns the warning notification distances for the requested warning type.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      isEnableTunnelExtrapolation ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Return true if tunnel extrapolation is enabled otherwise false .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `boolean`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      isPassthroughWaypointsHandlingEnabled ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Return true if handling of passthrough waypoints is enabled, otherwise - false .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      repeatLastManeuverNotification ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Call of this function is used to trigger the navigator to repeat the last maneuver notification based on the current position.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setBorderCrossingWarningListener ( BorderCrossingWarningListener value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets the listener to receive notifications about border crossings on the current road.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setBorderCrossingWarningOptions ( BorderCrossingWarningOptions value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets border crossing warning options to be passed to BorderCrossingWarningListener .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setCurrentSituationLaneAssistanceViewListener ( CurrentSituationLaneAssistanceViewListener value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets the listener to receive current situation lane assistance view notifications.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setCustomOption ( String key, String value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  This method sets custom options that controls navigator behavior.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setDangerZoneWarningListener ( DangerZoneWarningListener value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets the listener to receive current danger zones notifications.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setDestinationReachedListener ( DestinationReachedListener value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets the listener that notify when the destination has been reached.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setEnableTunnelExtrapolation (boolean value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Set to true to enable tunnel extrapolation, set to false to disable tunnel extrapolation.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setEnvironmentalZoneWarningListener ( EnvironmentalZoneWarningListener value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets the listener to receive current environmental zones notifications.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setEventTextListener ( EventTextListener value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets the listener that notifies when a text notification is available.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setEventTextOptions ( EventTextOptions value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets the text notification options.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setJunctionViewLaneAssistanceListener ( JunctionViewLaneAssistanceListener value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets the listener to receive junction view lane assistance notifications.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setLowSpeedZoneWarningListener ( LowSpeedZoneWarningListener value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets the listener to receive notifications about low speed zones on the current road.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setManeuverNotificationOptions ( ManeuverNotificationOptions value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets the maneuver notification options.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setManeuverNotificationTimingOptions ( TransportMode transportMode, TimingProfile timingProfile, ManeuverNotificationTimingOptions options)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Set timing option values for the combination of transport mode and timing profile.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setManeuverViewLaneAssistanceListener ( ManeuverViewLaneAssistanceListener value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets the listener to receive maneuver view lane assistance notifications.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setMilestoneStatusListener ( MilestoneStatusListener value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets the listener that notifies when a Milestone has been reached or missed.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setNavigableLocationListener ( NavigableLocationListener value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets the listener that notifies current location updates.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setOffRoadDestinationReachedListener ( OffRoadDestinationReachedListener value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets the listener that notifies when the off-road destination has been reached.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setOffRoadProgressListener ( OffRoadProgressListener value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets the listener that notifies about off-road progress.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setPassthroughWaypointsHandlingEnabled (boolean value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Set to true enables handling of passthrough waypoints, set to false disables handling of passthrough waypoints.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setPostActionListener ( PostActionListener value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets the listener to receive post action notifications, such as a charge action at a charging station.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setRailwayCrossingWarningListener ( RailwayCrossingWarningListener value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets the listener to receive notifications about railway crossings on the current road.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setRealisticViewWarningListener ( RealisticViewWarningListener value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets the listener to receive notifications about junction views on the current road.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setRealisticViewWarningOptions ( RealisticViewWarningOptions value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets realistic view warning options that allow to filter realistic views to be passed to RealisticViewWarningListener .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setRoadAttributesListener ( RoadAttributesListener value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets the listener to receive notifications about attributes of the current road.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setRoadSignWarningListener ( RoadSignWarningListener value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets the listener to receive notifications about road signs on the current road.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setRoadSignWarningOptions ( RoadSignWarningOptions value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets road sign warning options that allow to filter road signs to be passed to RoadSignWarningListener .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setRoadTextsListener ( RoadTextsListener value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets the listener to receive notifications about the textual attributes of the current road.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setRoute ( Route value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets the route to navigate.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setRouteDeviationListener ( RouteDeviationListener value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets the listener that notifies when deviation from the route is observed.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setRouteProgressListener ( RouteProgressListener value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets the listener that notifies when a route progress change occurs.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setSafetyCameraWarningListener ( SafetyCameraWarningListener value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets the listener to receive safety camera warning notifications.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setSafetyCameraWarningOptions ( SafetyCameraWarningOptions value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets safety camera warning options to be passed to SafetyCameraWarningListener .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setSchoolZoneWarningListener ( SchoolZoneWarningListener value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets the listener to receive notifications about school zones on the current road.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setSchoolZoneWarningOptions ( SchoolZoneWarningOptions value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets school zone warning options that allow to configure school zone notifications to be passed to SchoolZoneWarningListener .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setSpeedLimitListener ( SpeedLimitListener value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets the listener to receive notifications about the speed limit of the current road.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setSpeedWarningListener ( SpeedWarningListener value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets the listener to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setSpeedWarningOptions ( SpeedWarningOptions value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets the speed warning options.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setTollStopWarningListener ( TollStopWarningListener value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets the listener to receive notifications about the upcoming toll stop.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">

      setTrackingTransportProfile ( TransportProfile value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setTrackingTransportSpecification ( TransportSpecification value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets the transport specification for the Navigator , when no route is present.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setTrafficMergeWarningListener ( TrafficMergeWarningListener value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets the listener to receive notifications about merging traffic to the current road.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setTrafficMergeWarningOptions ( TrafficMergeWarningOptions value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets merging traffic warning options that allow to configure merging traffic notifications to be passed to TrafficMergeWarningListener .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setTrafficOnRoute ( TrafficOnRoute value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets the traffic information for the current route.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setTruckRestrictionsWarningListener ( TruckRestrictionsWarningListener value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets the listener to receive notifications about truck restrictions on the current road.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setTruckRestrictionsWarningOptions ( TruckRestrictionsWarningOptions value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Sets truck restrictions warning options that allow to filter truck restrictions to be passed to TruckRestrictionsWarningListener .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `boolean`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      setWarningNotificationDistances ( WarningType warningType, WarningNotificationDistances warningNotificationDistances)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Set the warning notification distances for the specified warning types.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from interface com.here.sdk.core.<a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener" title="interface in com.here.sdk.core">LocationListener</a>

  <a href="sdk-for-android-navigate-com-here-sdk-core-locationlistener#onLocationUpdated(com.here.sdk.core.Location">`onLocationUpdated`</a>)

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-getManeuver-int" class="section detail">

    ### getManeuver

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-maneuver" title="class in com.here.sdk.routing">Maneuver</a></span> <span class="element-name">getManeuver</span><wbr></wbr><span class="parameters">(int index)</span>

    </div>

    <div class="block">

    Returns maneuver at the given index.

    </div>

    Parameters:  
    `index` -

    The index of maneuver requested.

    Returns:  
    The maneuver if it exists or otherwise `null`.

    </div>

  - <div id="sdk-for-android-navigate-getManeuverNotificationTimingOptions-com-here-sdk-transport-TransportMode-com-here-sdk-navigation-TimingProfile" class="section detail">

    ### getManeuverNotificationTimingOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions" title="class in com.here.sdk.navigation">ManeuverNotificationTimingOptions</a></span> <span class="element-name">getManeuverNotificationTimingOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode" title="enum class in com.here.sdk.transport">TransportMode</a> transportMode, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile" title="enum class in com.here.sdk.navigation">TimingProfile</a> timingProfile)</span>

    </div>

    <div class="block">

    Returns maneuver notification timing options with default values given the combination of transport mode and timing profile. The return value can be used as the base for configuring maneuver notification timings. Configure the relevant attributes of this object according to your preferences, and then set it by calling setManeuverNotificationTimingOptions function for the same combination of transport mode and timing profile.

    </div>

    Parameters:  
    `transportMode` -

    The transport mode of the timing options.

    `timingProfile` -

    The timing profile of the timing options.

    Returns:  
    The timing options with default values.

    </div>

  - <div id="sdk-for-android-navigate-setManeuverNotificationTimingOptions-com-here-sdk-transport-TransportMode-com-here-sdk-navigation-TimingProfile-com-here-sdk-navigation-ManeuverNotificationTimingOptions" class="section detail">

    ### setManeuverNotificationTimingOptions

    <div class="member-signature">

    <span class="return-type">boolean</span> <span class="element-name">setManeuverNotificationTimingOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode" title="enum class in com.here.sdk.transport">TransportMode</a> transportMode, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-timingprofile" title="enum class in com.here.sdk.navigation">TimingProfile</a> timingProfile, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions" title="class in com.here.sdk.navigation">ManeuverNotificationTimingOptions</a> options)</span>

    </div>

    <div class="block">

    Set timing option values for the combination of transport mode and timing profile.

    </div>

    Parameters:  
    `transportMode` -

    The transport mode of the timing options.

    `timingProfile` -

    The timing profile of the timing options.

    `options` -

    The timing options.

    Returns:  
    `True` if set successfully, `false` when options has invalid value, see <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationtimingoptions" title="class in com.here.sdk.navigation">`ManeuverNotificationTimingOptions`</a> for more details about options.

    </div>

  - <div id="sdk-for-android-navigate-getWarningNotificationDistances-com-here-sdk-navigation-WarningType" class="section detail">

    ### getWarningNotificationDistances

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-warningnotificationdistances" title="class in com.here.sdk.navigation">WarningNotificationDistances</a></span> <span class="element-name">getWarningNotificationDistances</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a> warningType)</span>

    </div>

    <div class="block">

    Returns the warning notification distances for the requested warning type. The return value can be used as the base for configuring warning notification distances. Configure the relevant attributes of this object according to your preferences, and then set it by calling setWarningNotificationDistances function with the same warning type and the modified warning notification distances object.

    </div>

    Parameters:  
    `warningType` -

    The warning type for which the notification distances will be returned.

    Returns:  
    The notification distances for the given warning type.

    </div>

  - <div id="sdk-for-android-navigate-setWarningNotificationDistances-com-here-sdk-navigation-WarningType-com-here-sdk-navigation-WarningNotificationDistances" class="section detail">

    ### setWarningNotificationDistances

    <div class="member-signature">

    <span class="return-type">boolean</span> <span class="element-name">setWarningNotificationDistances</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-warningtype" title="enum class in com.here.sdk.navigation">WarningType</a> warningType, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-warningnotificationdistances" title="class in com.here.sdk.navigation">WarningNotificationDistances</a> warningNotificationDistances)</span>

    </div>

    <div class="block">

    Set the warning notification distances for the specified warning types. Note: The warning notification distances are set for most warners. This method can't be used to set the warning notification distance for the School Zone warning type because it is applicable regardless of the timing profile. Use NavigatorInterface.school_zone_warning_options instead. Attempting to set the warning notification distances for the school zone warner using the NavigatorInterface.set_warning_notification_distances method will fail and return false . Always use SchoolZoneWarningOptions.warning_distance_in_meters to set the warning notification distance for the school zone warner regardless of the TimingProfile . If NavigatorInterface.set_warning_notification_distances could be used, this would allow for different distances to be set for each timing profile, which is undesirable. Attempting to set the warning notification distances for the traffic merge warner using the NavigatorInterface.set_warning_notification_distances method will fail and return false . Always use TrafficMergeWarningOptions.warning_distance_in_meters to set the warning notification distance for the traffic merge warner regardless of the TimingProfile . Using the NavigatorInterface.set_warning_notification_distances method will fail and return false to avoid seting different distances on each timing profile since the traffic merge warning is only applicable on highways.

    </div>

    Parameters:  
    `warningType` -

    The warning type for which the warning notification distances will be set.

    `warningNotificationDistances` -

    The warning notification distances to be set for the specified warning types.

    Returns:  
    `True` if set successfully, `false` when the warning_type is \[WarningType.SCHOOL_ZONE\] or the options have invalid values, see <a href="sdk-for-android-navigate-com-here-sdk-navigation-warningnotificationdistances" title="class in com.here.sdk.navigation">`WarningNotificationDistances`</a> for more details about warning notification distances.

    </div>

  - <div id="sdk-for-android-navigate-repeatLastManeuverNotification" class="section detail">

    ### repeatLastManeuverNotification

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">repeatLastManeuverNotification</span>()

    </div>

    <div class="block">

    Call of this function is used to trigger the navigator to repeat the last maneuver notification based on the current position.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-calculateRemainingDistanceInMeters-com-here-sdk-core-GeoCoordinates" class="section detail">

    ### calculateRemainingDistanceInMeters

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a></span> <span class="element-name">calculateRemainingDistanceInMeters</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates)</span>

    </div>

    <div class="block">

    This method calculates the distance between the current position and given coordinates. The coordinates must be on the polyline.

    </div>

    Parameters:  
    `coordinates` -

    The geographic coordinates of the location.

    Returns:  
    distance in meters or null if given coordinates are not on route or given coordinates were already traversed.

    </div>

  - <div id="sdk-for-android-navigate-setCustomOption-java-lang-String-java-lang-String" class="section detail">

    ### setCustomOption

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setCustomOption</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> key, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> value)</span>

    </div>

    <div class="block">

    This method sets custom options that controls navigator behavior. Unsupported options are silently ignored. Undocumented options can change their meaning without going through deprecation process.

    </div>

    Parameters:  
    `key` -

    Option name

    `value` -

    New option value

    </div>

  - <div id="sdk-for-android-navigate-getRoute" class="section detail">

    ### getRoute

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing">Route</a></span> <span class="element-name">getRoute</span>()

    </div>

    <div class="block">

    Gets the route that is being navigated. Gets and sets the route that is being navigated. If not set, only the current location information will be provided through NavigableLocationListener . If set, both route progress ( RouteProgressListener ) and route deviation ( RouteDeviationListener ) will receive notifications on updates. A route may fail to be set if it is generated by an incompatible engine, in which case the operation has no effect.

    </div>

    Returns:  
    The route to navigate.

    </div>

  - <div id="sdk-for-android-navigate-setRoute-com-here-sdk-routing-Route" class="section detail">

    ### setRoute

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setRoute</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing">Route</a> value)</span>

    </div>

    <div class="block">

    Sets the route to navigate. Gets and sets the route that is being navigated. If not set, only the current location information will be provided through NavigableLocationListener . If set, both route progress ( RouteProgressListener ) and route deviation ( RouteDeviationListener ) will receive notifications on updates. A route may fail to be set if it is generated by an incompatible engine, in which case the operation has no effect.

    </div>

    Parameters:  
    `value` -

    The route to navigate.

    </div>

  - <div id="sdk-for-android-navigate-getTrackingTransportProfile" class="section detail">

    ### getTrackingTransportProfile

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @Nullable </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-transportprofile" title="class in com.here.sdk.core">TransportProfile</a></span> <span class="element-name">getTrackingTransportProfile</span>()

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use `NavigatorInterface.trackingTransportSpecification` instead.

    </div>

    </div>

    <div class="block">

    Gets the transport profile for the Navigator , when no route is present. Properly setting the transport profile optimizes the navigation experience, and improves resource consumption. For example, a TransportProfile can be defined with a VehicleProfile . A vehicle profile can have several parameters such as VehicleType to set the source of information describing the vehicle. The default is a VehicleType.CAR profile. Currently used members of TransportProfile VehicleType : Sets the transport mode. From vehicleProfile : grossWeightInKilograms : Required for truck related speed information. heightInCentimeters : Required for truck related speed information. widthInCentimeters : Additional truck definition for more specific truck speed information. lengthInCentimeters : Additional truck definition for more specific truck speed information.

    </div>

    Returns:  
    Defines the transport profile for the <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigator" title="class in com.here.sdk.navigation">`Navigator`</a>, when no route is present.

    </div>

  - <div id="sdk-for-android-navigate-setTrackingTransportProfile-com-here-sdk-core-TransportProfile" class="section detail">

    ### setTrackingTransportProfile

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> </span><span class="return-type">void</span> <span class="element-name">setTrackingTransportProfile</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-core-transportprofile" title="class in com.here.sdk.core">TransportProfile</a> value)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use `NavigatorInterface.trackingTransportSpecification` instead.

    </div>

    </div>

    <div class="block">

    Sets the transport profile for the Navigator , when no route is present. Properly setting the transport profile optimizes the navigation experience, and improves resource consumption. For example, a TransportProfile can be defined with a VehicleProfile . A vehicle profile can have several parameters such as VehicleType to set the source of information describing the vehicle. The default is a VehicleType.CAR profile. Currently used members of TransportProfile VehicleType : Sets the transport mode. From vehicleProfile : grossWeightInKilograms : Required for truck related speed information. heightInCentimeters : Required for truck related speed information. widthInCentimeters : Additional truck definition for more specific truck speed information. lengthInCentimeters : Additional truck definition for more specific truck speed information.

    </div>

    Parameters:  
    `value` -

    Defines the transport profile for the <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigator" title="class in com.here.sdk.navigation">`Navigator`</a>, when no route is present.

    </div>

  - <div id="sdk-for-android-navigate-getTrackingTransportSpecification" class="section detail">

    ### getTrackingTransportSpecification

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-transport-transportspecification" title="class in com.here.sdk.transport">TransportSpecification</a></span> <span class="element-name">getTrackingTransportSpecification</span>()

    </div>

    <div class="block">

    Gets the transport specification for the Navigator , when no route is present. Properly setting the transport specification optimizes the navigation experience, and improves resource consumption. An TransportSpecification must have the TransportSpecification.transportMode set. A transport specification can have several parameters defined such as VehicleSpecification.lengthInCentimeters defined in TransportSpecification.vehicleSpecification to set the source of information describing the vehicle. By default the TransportSpecification will have the transport mode set to TransportMode.CAR . Currently used members of TransportSpecification TransportSpecification.transportMode : Sets the transport mode. From TransportSpecification.vehicleSpecification : VehicleSpecification.grossWeightInKilograms : Required for truck related speed information. VehicleSpecification.heightInCentimeters : Required for truck related speed information. VehicleSpecification.widthInCentimeters : Additional truck definition for more specific truck speed information. VehicleSpecification.lengthInCentimeters : Additional truck definition for more specific truck speed information.

    </div>

    Returns:  
    Defines the transport specification for the <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigator" title="class in com.here.sdk.navigation">`Navigator`</a>, when no route is present.

    </div>

  - <div id="sdk-for-android-navigate-setTrackingTransportSpecification-com-here-sdk-transport-TransportSpecification" class="section detail">

    ### setTrackingTransportSpecification

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setTrackingTransportSpecification</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-transport-transportspecification" title="class in com.here.sdk.transport">TransportSpecification</a> value)</span>

    </div>

    <div class="block">

    Sets the transport specification for the Navigator , when no route is present. Properly setting the transport specification optimizes the navigation experience, and improves resource consumption. An TransportSpecification must have the TransportSpecification.transportMode set. A transport specification can have several parameters defined such as VehicleSpecification.lengthInCentimeters defined in TransportSpecification.vehicleSpecification to set the source of information describing the vehicle. By default the TransportSpecification will have the transport mode set to TransportMode.CAR . Currently used members of TransportSpecification TransportSpecification.transportMode : Sets the transport mode. From TransportSpecification.vehicleSpecification : VehicleSpecification.grossWeightInKilograms : Required for truck related speed information. VehicleSpecification.heightInCentimeters : Required for truck related speed information. VehicleSpecification.widthInCentimeters : Additional truck definition for more specific truck speed information. VehicleSpecification.lengthInCentimeters : Additional truck definition for more specific truck speed information.

    </div>

    Parameters:  
    `value` -

    Defines the transport specification for the <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigator" title="class in com.here.sdk.navigation">`Navigator`</a>, when no route is present.

    </div>

  - <div id="sdk-for-android-navigate-getNavigableLocationListener" class="section detail">

    ### getNavigableLocationListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigablelocationlistener" title="interface in com.here.sdk.navigation">NavigableLocationListener</a></span> <span class="element-name">getNavigableLocationListener</span>()

    </div>

    <div class="block">

    Gets the listener that notifies current location updates. It returns null when no listener is set by an user.

    </div>

    Returns:  
    Object to receive notifications about the current location.

    </div>

  - <div id="sdk-for-android-navigate-setNavigableLocationListener-com-here-sdk-navigation-NavigableLocationListener" class="section detail">

    ### setNavigableLocationListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setNavigableLocationListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigablelocationlistener" title="interface in com.here.sdk.navigation">NavigableLocationListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener that notifies current location updates. It returns null when no listener is set by an user.

    </div>

    Parameters:  
    `value` -

    Object to receive notifications about the current location.

    </div>

  - <div id="sdk-for-android-navigate-getRouteProgressListener" class="section detail">

    ### getRouteProgressListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-routeprogresslistener" title="interface in com.here.sdk.navigation">RouteProgressListener</a></span> <span class="element-name">getRouteProgressListener</span>()

    </div>

    <div class="block">

    Gets the listener that notifies when a route progress change occurs. Route progress notifications only occurs if the route has been set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Returns:  
    Object to receive notifications about navigation route progress.

    </div>

  - <div id="sdk-for-android-navigate-setRouteProgressListener-com-here-sdk-navigation-RouteProgressListener" class="section detail">

    ### setRouteProgressListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setRouteProgressListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-routeprogresslistener" title="interface in com.here.sdk.navigation">RouteProgressListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener that notifies when a route progress change occurs. Route progress notifications only occurs if the route has been set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Parameters:  
    `value` -

    Object to receive notifications about navigation route progress.

    </div>

  - <div id="sdk-for-android-navigate-getRouteDeviationListener" class="section detail">

    ### getRouteDeviationListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-routedeviationlistener" title="interface in com.here.sdk.navigation">RouteDeviationListener</a></span> <span class="element-name">getRouteDeviationListener</span>()

    </div>

    <div class="block">

    Gets the listener that notifies when deviation from the route is observed. Route deviation notifications only occurs if a route has been set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Returns:  
    Object to receive notifications about deviations from the route if any occurs.

    </div>

  - <div id="sdk-for-android-navigate-setRouteDeviationListener-com-here-sdk-navigation-RouteDeviationListener" class="section detail">

    ### setRouteDeviationListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setRouteDeviationListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-routedeviationlistener" title="interface in com.here.sdk.navigation">RouteDeviationListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener that notifies when deviation from the route is observed. Route deviation notifications only occurs if a route has been set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Parameters:  
    `value` -

    Object to receive notifications about deviations from the route if any occurs.

    </div>

  - <div id="sdk-for-android-navigate-getEventTextListener" class="section detail">

    ### getEventTextListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-eventtextlistener" title="interface in com.here.sdk.navigation">EventTextListener</a></span> <span class="element-name">getEventTextListener</span>()

    </div>

    <div class="block">

    Gets the listener that notifies when a text notification is available. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user. Note: In order to receive the text notification emitted for the traffic merge warner, when TrafficMergeWarningOptions.enable_text_notification has been enabled, the sdk.navigation.EventTextListener must be enabled as well.

    </div>

    Returns:  
    Object to receive text notifications when they are available.

    </div>

  - <div id="sdk-for-android-navigate-setEventTextListener-com-here-sdk-navigation-EventTextListener" class="section detail">

    ### setEventTextListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setEventTextListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-eventtextlistener" title="interface in com.here.sdk.navigation">EventTextListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener that notifies when a text notification is available. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user. Note: In order to receive the text notification emitted for the traffic merge warner, when TrafficMergeWarningOptions.enable_text_notification has been enabled, the sdk.navigation.EventTextListener must be enabled as well.

    </div>

    Parameters:  
    `value` -

    Object to receive text notifications when they are available.

    </div>

  - <div id="sdk-for-android-navigate-getMilestoneStatusListener" class="section detail">

    ### getMilestoneStatusListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-milestonestatuslistener" title="interface in com.here.sdk.navigation">MilestoneStatusListener</a></span> <span class="element-name">getMilestoneStatusListener</span>()

    </div>

    <div class="block">

    Gets the listener that notifies when a Milestone has been reached or missed. It informs on all waypoints (passed or missed) that are of type MilestoneType.STOPOVER but excludes the starting waypoint. Waypoints of type MilestoneType.PASSTHROUGH are excluded, by default, but can be included via isPassthroughWaypointsHandlingEnabled() . Milestone status notifications only occurs if a route has been set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Returns:  
    Object to receive notifications about the arrival at each <a href="sdk-for-android-navigate-com-here-sdk-navigation-milestone" title="class in com.here.sdk.navigation">`Milestone`</a> or missing it.

    </div>

  - <div id="sdk-for-android-navigate-setMilestoneStatusListener-com-here-sdk-navigation-MilestoneStatusListener" class="section detail">

    ### setMilestoneStatusListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setMilestoneStatusListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-milestonestatuslistener" title="interface in com.here.sdk.navigation">MilestoneStatusListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener that notifies when a Milestone has been reached or missed. It informs on all waypoints (passed or missed) that are of type MilestoneType.STOPOVER but excludes the starting waypoint. Waypoints of type MilestoneType.PASSTHROUGH are excluded, by default, but can be included via isPassthroughWaypointsHandlingEnabled() . Milestone status notifications only occurs if a route has been set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Parameters:  
    `value` -

    Object to receive notifications about the arrival at each <a href="sdk-for-android-navigate-com-here-sdk-navigation-milestone" title="class in com.here.sdk.navigation">`Milestone`</a> or missing it.

    </div>

  - <div id="sdk-for-android-navigate-getDestinationReachedListener" class="section detail">

    ### getDestinationReachedListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-destinationreachedlistener" title="interface in com.here.sdk.navigation">DestinationReachedListener</a></span> <span class="element-name">getDestinationReachedListener</span>()

    </div>

    <div class="block">

    Gets the listener that notify when the destination has been reached. Destination reached notifications only occurs if a route has been set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Returns:  
    Object to receive the notification about the arrival at the destination.

    </div>

  - <div id="sdk-for-android-navigate-setDestinationReachedListener-com-here-sdk-navigation-DestinationReachedListener" class="section detail">

    ### setDestinationReachedListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setDestinationReachedListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-destinationreachedlistener" title="interface in com.here.sdk.navigation">DestinationReachedListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener that notify when the destination has been reached. Destination reached notifications only occurs if a route has been set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Parameters:  
    `value` -

    Object to receive the notification about the arrival at the destination.

    </div>

  - <div id="sdk-for-android-navigate-getSpeedWarningListener" class="section detail">

    ### getSpeedWarningListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-speedwarninglistener" title="interface in com.here.sdk.navigation">SpeedWarningListener</a></span> <span class="element-name">getSpeedWarningListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Returns:  
    Object to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal.

    </div>

  - <div id="sdk-for-android-navigate-setSpeedWarningListener-com-here-sdk-navigation-SpeedWarningListener" class="section detail">

    ### setSpeedWarningListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setSpeedWarningListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedwarninglistener" title="interface in com.here.sdk.navigation">SpeedWarningListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Parameters:  
    `value` -

    Object to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal.

    </div>

  - <div id="sdk-for-android-navigate-getManeuverViewLaneAssistanceListener" class="section detail">

    ### getManeuverViewLaneAssistanceListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverviewlaneassistancelistener" title="interface in com.here.sdk.navigation">ManeuverViewLaneAssistanceListener</a></span> <span class="element-name">getManeuverViewLaneAssistanceListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive maneuver view lane assistance notifications. Maneuver view lane assistance notifications only occurs if a route has been set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Returns:  
    Object to receive maneuver view lane assistance notifications.

    </div>

  - <div id="sdk-for-android-navigate-setManeuverViewLaneAssistanceListener-com-here-sdk-navigation-ManeuverViewLaneAssistanceListener" class="section detail">

    ### setManeuverViewLaneAssistanceListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setManeuverViewLaneAssistanceListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuverviewlaneassistancelistener" title="interface in com.here.sdk.navigation">ManeuverViewLaneAssistanceListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive maneuver view lane assistance notifications. Maneuver view lane assistance notifications only occurs if a route has been set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Parameters:  
    `value` -

    Object to receive maneuver view lane assistance notifications.

    </div>

  - <div id="sdk-for-android-navigate-getCurrentSituationLaneAssistanceViewListener" class="section detail">

    ### getCurrentSituationLaneAssistanceViewListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-currentsituationlaneassistanceviewlistener" title="interface in com.here.sdk.navigation">CurrentSituationLaneAssistanceViewListener</a></span> <span class="element-name">getCurrentSituationLaneAssistanceViewListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive current situation lane assistance view notifications. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Returns:  
    Object to receive current situation lane assistance view notifications.

    </div>

  - <div id="sdk-for-android-navigate-setCurrentSituationLaneAssistanceViewListener-com-here-sdk-navigation-CurrentSituationLaneAssistanceViewListener" class="section detail">

    ### setCurrentSituationLaneAssistanceViewListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setCurrentSituationLaneAssistanceViewListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-currentsituationlaneassistanceviewlistener" title="interface in com.here.sdk.navigation">CurrentSituationLaneAssistanceViewListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive current situation lane assistance view notifications. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Parameters:  
    `value` -

    Object to receive current situation lane assistance view notifications.

    </div>

  - <div id="sdk-for-android-navigate-getEnvironmentalZoneWarningListener" class="section detail">

    ### getEnvironmentalZoneWarningListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-environmentalzonewarninglistener" title="interface in com.here.sdk.navigation">EnvironmentalZoneWarningListener</a></span> <span class="element-name">getEnvironmentalZoneWarningListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive current environmental zones notifications. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Returns:  
    Object to receive notification on approaching environmental zones.

    </div>

  - <div id="sdk-for-android-navigate-setEnvironmentalZoneWarningListener-com-here-sdk-navigation-EnvironmentalZoneWarningListener" class="section detail">

    ### setEnvironmentalZoneWarningListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setEnvironmentalZoneWarningListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-environmentalzonewarninglistener" title="interface in com.here.sdk.navigation">EnvironmentalZoneWarningListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive current environmental zones notifications. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Parameters:  
    `value` -

    Object to receive notification on approaching environmental zones.

    </div>

  - <div id="sdk-for-android-navigate-getJunctionViewLaneAssistanceListener" class="section detail">

    ### getJunctionViewLaneAssistanceListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-junctionviewlaneassistancelistener" title="interface in com.here.sdk.navigation">JunctionViewLaneAssistanceListener</a></span> <span class="element-name">getJunctionViewLaneAssistanceListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive junction view lane assistance notifications. Junction view lane assistance notifications only occurs if a route has been set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Returns:  
    Object to receive junction view lane assistance notifications.

    </div>

  - <div id="sdk-for-android-navigate-setJunctionViewLaneAssistanceListener-com-here-sdk-navigation-JunctionViewLaneAssistanceListener" class="section detail">

    ### setJunctionViewLaneAssistanceListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setJunctionViewLaneAssistanceListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-junctionviewlaneassistancelistener" title="interface in com.here.sdk.navigation">JunctionViewLaneAssistanceListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive junction view lane assistance notifications. Junction view lane assistance notifications only occurs if a route has been set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Parameters:  
    `value` -

    Object to receive junction view lane assistance notifications.

    </div>

  - <div id="sdk-for-android-navigate-getSafetyCameraWarningListener" class="section detail">

    ### getSafetyCameraWarningListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-safetycamerawarninglistener" title="interface in com.here.sdk.navigation">SafetyCameraWarningListener</a></span> <span class="element-name">getSafetyCameraWarningListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive safety camera warning notifications. If a listener is present, notifications about safety speed cameras will be also sent via SafetyCameraWarningListener . Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Returns:  
    Object to receive safety camera warner notifications.

    </div>

  - <div id="sdk-for-android-navigate-setSafetyCameraWarningListener-com-here-sdk-navigation-SafetyCameraWarningListener" class="section detail">

    ### setSafetyCameraWarningListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setSafetyCameraWarningListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-safetycamerawarninglistener" title="interface in com.here.sdk.navigation">SafetyCameraWarningListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive safety camera warning notifications. If a listener is present, notifications about safety speed cameras will be also sent via SafetyCameraWarningListener . Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Parameters:  
    `value` -

    Object to receive safety camera warner notifications.

    </div>

  - <div id="sdk-for-android-navigate-getSafetyCameraWarningOptions" class="section detail">

    ### getSafetyCameraWarningOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-safetycamerawarningoptions" title="class in com.here.sdk.navigation">SafetyCameraWarningOptions</a></span> <span class="element-name">getSafetyCameraWarningOptions</span>()

    </div>

    <div class="block">

    Gets safety camera warning options to be passed to SafetyCameraWarningListener . These options allow the enabling or disabling the text notification for the warner.

    </div>

    Returns:  
    Safety camera warning options to be passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-safetycamerawarninglistener" title="interface in com.here.sdk.navigation">`SafetyCameraWarningListener`</a>.

    </div>

  - <div id="sdk-for-android-navigate-setSafetyCameraWarningOptions-com-here-sdk-navigation-SafetyCameraWarningOptions" class="section detail">

    ### setSafetyCameraWarningOptions

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setSafetyCameraWarningOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-safetycamerawarningoptions" title="class in com.here.sdk.navigation">SafetyCameraWarningOptions</a> value)</span>

    </div>

    <div class="block">

    Sets safety camera warning options to be passed to SafetyCameraWarningListener . These options allow the enabling or disabling the text notification for the warner.

    </div>

    Parameters:  
    `value` -

    Safety camera warning options to be passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-safetycamerawarninglistener" title="interface in com.here.sdk.navigation">`SafetyCameraWarningListener`</a>.

    </div>

  - <div id="sdk-for-android-navigate-getDangerZoneWarningListener" class="section detail">

    ### getDangerZoneWarningListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-dangerzonewarninglistener" title="interface in com.here.sdk.navigation">DangerZoneWarningListener</a></span> <span class="element-name">getDangerZoneWarningListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive current danger zones notifications. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Returns:  
    Object to receive notification on approaching danger zones.

    </div>

  - <div id="sdk-for-android-navigate-setDangerZoneWarningListener-com-here-sdk-navigation-DangerZoneWarningListener" class="section detail">

    ### setDangerZoneWarningListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setDangerZoneWarningListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-dangerzonewarninglistener" title="interface in com.here.sdk.navigation">DangerZoneWarningListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive current danger zones notifications. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Parameters:  
    `value` -

    Object to receive notification on approaching danger zones.

    </div>

  - <div id="sdk-for-android-navigate-getTruckRestrictionsWarningListener" class="section detail">

    ### getTruckRestrictionsWarningListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionswarninglistener" title="interface in com.here.sdk.navigation">TruckRestrictionsWarningListener</a></span> <span class="element-name">getTruckRestrictionsWarningListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive notifications about truck restrictions on the current road. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Returns:  
    Object to receive notifications about truck restrictions on the current road.

    </div>

  - <div id="sdk-for-android-navigate-setTruckRestrictionsWarningListener-com-here-sdk-navigation-TruckRestrictionsWarningListener" class="section detail">

    ### setTruckRestrictionsWarningListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setTruckRestrictionsWarningListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionswarninglistener" title="interface in com.here.sdk.navigation">TruckRestrictionsWarningListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive notifications about truck restrictions on the current road. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Parameters:  
    `value` -

    Object to receive notifications about truck restrictions on the current road.

    </div>

  - <div id="sdk-for-android-navigate-getWarnerEngine" class="section detail">

    ### getWarnerEngine

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-warner-warnerengine" title="class in com.here.sdk.warner">WarnerEngine</a></span> <span class="element-name">getWarnerEngine</span>()

    </div>

    <div class="block">

    Gets the warner engine used by the navigator. This engine can be used to configure navigation warnings.

    </div>

    Returns:  
    Warner engine used by the navigator.

    </div>

  - <div id="sdk-for-android-navigate-getTruckRestrictionsWarningOptions" class="section detail">

    ### getTruckRestrictionsWarningOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionswarningoptions" title="class in com.here.sdk.navigation">TruckRestrictionsWarningOptions</a></span> <span class="element-name">getTruckRestrictionsWarningOptions</span>()

    </div>

    <div class="block">

    Gets truck restrictions warning options that allow to filter truck restrictions to be passed to TruckRestrictionsWarningListener .

    </div>

    Returns:  
    Truck restrictions warning options that allow to filter truck restrictions to be passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionswarninglistener" title="interface in com.here.sdk.navigation">`TruckRestrictionsWarningListener`</a>.

    </div>

  - <div id="sdk-for-android-navigate-setTruckRestrictionsWarningOptions-com-here-sdk-navigation-TruckRestrictionsWarningOptions" class="section detail">

    ### setTruckRestrictionsWarningOptions

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setTruckRestrictionsWarningOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionswarningoptions" title="class in com.here.sdk.navigation">TruckRestrictionsWarningOptions</a> value)</span>

    </div>

    <div class="block">

    Sets truck restrictions warning options that allow to filter truck restrictions to be passed to TruckRestrictionsWarningListener .

    </div>

    Parameters:  
    `value` -

    Truck restrictions warning options that allow to filter truck restrictions to be passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionswarninglistener" title="interface in com.here.sdk.navigation">`TruckRestrictionsWarningListener`</a>.

    </div>

  - <div id="sdk-for-android-navigate-getPostActionListener" class="section detail">

    ### getPostActionListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-postactionlistener" title="interface in com.here.sdk.navigation">PostActionListener</a></span> <span class="element-name">getPostActionListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive post action notifications, such as a charge action at a charging station. Post actions notifications only occurs if a route has been set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Returns:  
    Object to receive post action notifications, such as a charge action at a charging station.

    </div>

  - <div id="sdk-for-android-navigate-setPostActionListener-com-here-sdk-navigation-PostActionListener" class="section detail">

    ### setPostActionListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setPostActionListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-postactionlistener" title="interface in com.here.sdk.navigation">PostActionListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive post action notifications, such as a charge action at a charging station. Post actions notifications only occurs if a route has been set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Parameters:  
    `value` -

    Object to receive post action notifications, such as a charge action at a charging station.

    </div>

  - <div id="sdk-for-android-navigate-getSpeedLimitListener" class="section detail">

    ### getSpeedLimitListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimitlistener" title="interface in com.here.sdk.navigation">SpeedLimitListener</a></span> <span class="element-name">getSpeedLimitListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive notifications about the speed limit of the current road. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Returns:  
    Object to receive notifications about the speed limit of the current road.

    </div>

  - <div id="sdk-for-android-navigate-setSpeedLimitListener-com-here-sdk-navigation-SpeedLimitListener" class="section detail">

    ### setSpeedLimitListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setSpeedLimitListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimitlistener" title="interface in com.here.sdk.navigation">SpeedLimitListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive notifications about the speed limit of the current road. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Parameters:  
    `value` -

    Object to receive notifications about the speed limit of the current road.

    </div>

  - <div id="sdk-for-android-navigate-getRoadTextsListener" class="section detail">

    ### getRoadTextsListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-roadtextslistener" title="interface in com.here.sdk.navigation">RoadTextsListener</a></span> <span class="element-name">getRoadTextsListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive notifications about the textual attributes of the current road. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Returns:  
    Object to receive notifications about the textual attributes of the current road.

    </div>

  - <div id="sdk-for-android-navigate-setRoadTextsListener-com-here-sdk-navigation-RoadTextsListener" class="section detail">

    ### setRoadTextsListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setRoadTextsListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadtextslistener" title="interface in com.here.sdk.navigation">RoadTextsListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive notifications about the textual attributes of the current road. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Parameters:  
    `value` -

    Object to receive notifications about the textual attributes of the current road.

    </div>

  - <div id="sdk-for-android-navigate-getRoadAttributesListener" class="section detail">

    ### getRoadAttributesListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-roadattributeslistener" title="interface in com.here.sdk.navigation">RoadAttributesListener</a></span> <span class="element-name">getRoadAttributesListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive notifications about attributes of the current road. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Returns:  
    Object to receive notifications about attributes of the current road.

    </div>

  - <div id="sdk-for-android-navigate-setRoadAttributesListener-com-here-sdk-navigation-RoadAttributesListener" class="section detail">

    ### setRoadAttributesListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setRoadAttributesListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadattributeslistener" title="interface in com.here.sdk.navigation">RoadAttributesListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive notifications about attributes of the current road. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Parameters:  
    `value` -

    Object to receive notifications about attributes of the current road.

    </div>

  - <div id="sdk-for-android-navigate-getRoadSignWarningListener" class="section detail">

    ### getRoadSignWarningListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarninglistener" title="interface in com.here.sdk.navigation">RoadSignWarningListener</a></span> <span class="element-name">getRoadSignWarningListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive notifications about road signs on the current road. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Returns:  
    Object to receive notifications about road signs on the current road.

    </div>

  - <div id="sdk-for-android-navigate-setRoadSignWarningListener-com-here-sdk-navigation-RoadSignWarningListener" class="section detail">

    ### setRoadSignWarningListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setRoadSignWarningListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarninglistener" title="interface in com.here.sdk.navigation">RoadSignWarningListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive notifications about road signs on the current road. Note: This RoadSignWarningListener will provide school zone warnings only in case the speed limit inside the school zone is different than the default speed limit applicable for cars outside the school zone. For warnings about school zones regardless of their speed limits, the NavigatorInterface.road_sign_warning_listener should be used and the RoadSignWarning.type should be checked for value RoadSignType.SCHOOL_ZONE . The school zone warner is a zone warner, which means that for a school zone there will always be 3 warnings emitted, with the SchoolZoneWarning.distance_type set to DistanceType.AHEAD , DistanceType.REACHED Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Parameters:  
    `value` -

    Object to receive notifications about road signs on the current road.

    </div>

  - <div id="sdk-for-android-navigate-getRoadSignWarningOptions" class="section detail">

    ### getRoadSignWarningOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarningoptions" title="class in com.here.sdk.navigation">RoadSignWarningOptions</a></span> <span class="element-name">getRoadSignWarningOptions</span>()

    </div>

    <div class="block">

    Gets road sign warning options that allow to filter road signs to be passed to RoadSignWarningListener .

    </div>

    Returns:  
    Road sign warning options that allow to filter road sings to be passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarninglistener" title="interface in com.here.sdk.navigation">`RoadSignWarningListener`</a>.

    </div>

  - <div id="sdk-for-android-navigate-setRoadSignWarningOptions-com-here-sdk-navigation-RoadSignWarningOptions" class="section detail">

    ### setRoadSignWarningOptions

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setRoadSignWarningOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarningoptions" title="class in com.here.sdk.navigation">RoadSignWarningOptions</a> value)</span>

    </div>

    <div class="block">

    Sets road sign warning options that allow to filter road signs to be passed to RoadSignWarningListener .

    </div>

    Parameters:  
    `value` -

    Road sign warning options that allow to filter road sings to be passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarninglistener" title="interface in com.here.sdk.navigation">`RoadSignWarningListener`</a>.

    </div>

  - <div id="sdk-for-android-navigate-getSchoolZoneWarningListener" class="section detail">

    ### getSchoolZoneWarningListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-schoolzonewarninglistener" title="interface in com.here.sdk.navigation">SchoolZoneWarningListener</a></span> <span class="element-name">getSchoolZoneWarningListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive notifications about school zones on the current road. Setting null value to the listener will unset the listener. school zones on the current road. It returns null when no listener is set by an user.

    </div>

    Returns:  
    Object to receive notifications about school zones on the current road.

    </div>

  - <div id="sdk-for-android-navigate-setSchoolZoneWarningListener-com-here-sdk-navigation-SchoolZoneWarningListener" class="section detail">

    ### setSchoolZoneWarningListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setSchoolZoneWarningListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-schoolzonewarninglistener" title="interface in com.here.sdk.navigation">SchoolZoneWarningListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive notifications about school zones on the current road. Setting null value to the listener will unset the listener. school zones on the current road. It returns null when no listener is set by an user.

    </div>

    Parameters:  
    `value` -

    Object to receive notifications about school zones on the current road.

    </div>

  - <div id="sdk-for-android-navigate-getSchoolZoneWarningOptions" class="section detail">

    ### getSchoolZoneWarningOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-schoolzonewarningoptions" title="class in com.here.sdk.navigation">SchoolZoneWarningOptions</a></span> <span class="element-name">getSchoolZoneWarningOptions</span>()

    </div>

    <div class="block">

    Gets school zone warning options that allow to configure school zone notifications to be passed to SchoolZoneWarningListener . It allow to configure school zone notifications to be passed to SchoolZoneWarningListener .

    </div>

    Returns:  
    School zone warning options

    </div>

  - <div id="sdk-for-android-navigate-setSchoolZoneWarningOptions-com-here-sdk-navigation-SchoolZoneWarningOptions" class="section detail">

    ### setSchoolZoneWarningOptions

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setSchoolZoneWarningOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-schoolzonewarningoptions" title="class in com.here.sdk.navigation">SchoolZoneWarningOptions</a> value)</span>

    </div>

    <div class="block">

    Sets school zone warning options that allow to configure school zone notifications to be passed to SchoolZoneWarningListener . It allow to configure school zone notifications to be passed to SchoolZoneWarningListener .

    </div>

    Parameters:  
    `value` -

    School zone warning options

    </div>

  - <div id="sdk-for-android-navigate-getRealisticViewWarningListener" class="section detail">

    ### getRealisticViewWarningListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarninglistener" title="interface in com.here.sdk.navigation">RealisticViewWarningListener</a></span> <span class="element-name">getRealisticViewWarningListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive notifications about junction views on the current road. Setting null value to the listener will unset the listener. This feature requires a map version greater or equal to 67 in order to function properly. It returns null when no listener is set by an user.

    </div>

    Returns:  
    Object to receive notifications about junction views on the current road.

    </div>

  - <div id="sdk-for-android-navigate-setRealisticViewWarningListener-com-here-sdk-navigation-RealisticViewWarningListener" class="section detail">

    ### setRealisticViewWarningListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setRealisticViewWarningListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarninglistener" title="interface in com.here.sdk.navigation">RealisticViewWarningListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive notifications about junction views on the current road. Setting null value to the listener will unset the listener. This feature requires a map version greater or equal to 67 in order to function properly. It returns null when no listener is set by an user.

    </div>

    Parameters:  
    `value` -

    Object to receive notifications about junction views on the current road.

    </div>

  - <div id="sdk-for-android-navigate-getRealisticViewWarningOptions" class="section detail">

    ### getRealisticViewWarningOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarningoptions" title="class in com.here.sdk.navigation">RealisticViewWarningOptions</a></span> <span class="element-name">getRealisticViewWarningOptions</span>()

    </div>

    <div class="block">

    Gets realistic view warning options that allow to filter realistic views to be passed to RealisticViewWarningListener . It allow to filter realistic views to be passed to RealisticViewWarningListener . This feature requires a map version greater or equal to 67 in order to function properly.

    </div>

    Returns:  
    Realistic view warning options.

    </div>

  - <div id="sdk-for-android-navigate-setRealisticViewWarningOptions-com-here-sdk-navigation-RealisticViewWarningOptions" class="section detail">

    ### setRealisticViewWarningOptions

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setRealisticViewWarningOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarningoptions" title="class in com.here.sdk.navigation">RealisticViewWarningOptions</a> value)</span>

    </div>

    <div class="block">

    Sets realistic view warning options that allow to filter realistic views to be passed to RealisticViewWarningListener . It allow to filter realistic views to be passed to RealisticViewWarningListener . This feature requires a map version greater or equal to 67 in order to function properly.

    </div>

    Parameters:  
    `value` -

    Realistic view warning options.

    </div>

  - <div id="sdk-for-android-navigate-getBorderCrossingWarningListener" class="section detail">

    ### getBorderCrossingWarningListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarninglistener" title="interface in com.here.sdk.navigation">BorderCrossingWarningListener</a></span> <span class="element-name">getBorderCrossingWarningListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive notifications about border crossings on the current road. Border crossing notifications are given only if a route is present. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Returns:  
    Object to receive notifications about border crossings on the current road.

    </div>

  - <div id="sdk-for-android-navigate-setBorderCrossingWarningListener-com-here-sdk-navigation-BorderCrossingWarningListener" class="section detail">

    ### setBorderCrossingWarningListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setBorderCrossingWarningListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarninglistener" title="interface in com.here.sdk.navigation">BorderCrossingWarningListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive notifications about border crossings on the current road. Border crossing notifications are given only if a route is present. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Parameters:  
    `value` -

    Object to receive notifications about border crossings on the current road.

    </div>

  - <div id="sdk-for-android-navigate-getBorderCrossingWarningOptions" class="section detail">

    ### getBorderCrossingWarningOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarningoptions" title="class in com.here.sdk.navigation">BorderCrossingWarningOptions</a></span> <span class="element-name">getBorderCrossingWarningOptions</span>()

    </div>

    <div class="block">

    Gets border crossing warning options to be passed to BorderCrossingWarningListener . allow the filtering of the border crossing warnings received and set the notification distances.

    </div>

    Returns:  
    Border crossing warning options to be passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarninglistener" title="interface in com.here.sdk.navigation">`BorderCrossingWarningListener`</a>. These options

    </div>

  - <div id="sdk-for-android-navigate-setBorderCrossingWarningOptions-com-here-sdk-navigation-BorderCrossingWarningOptions" class="section detail">

    ### setBorderCrossingWarningOptions

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setBorderCrossingWarningOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarningoptions" title="class in com.here.sdk.navigation">BorderCrossingWarningOptions</a> value)</span>

    </div>

    <div class="block">

    Sets border crossing warning options to be passed to BorderCrossingWarningListener . allow the filtering of the border crossing warnings received and set the notification distances.

    </div>

    Parameters:  
    `value` -

    Border crossing warning options to be passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarninglistener" title="interface in com.here.sdk.navigation">`BorderCrossingWarningListener`</a>. These options

    </div>

  - <div id="sdk-for-android-navigate-getTollStopWarningListener" class="section detail">

    ### getTollStopWarningListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-tollstopwarninglistener" title="interface in com.here.sdk.navigation">TollStopWarningListener</a></span> <span class="element-name">getTollStopWarningListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive notifications about the the upcoming toll stop. Setting null value to the listener will unset the listener. This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    </div>

    Returns:  
    Object to receive information on the upcoming toll stop.

    </div>

  - <div id="sdk-for-android-navigate-setTollStopWarningListener-com-here-sdk-navigation-TollStopWarningListener" class="section detail">

    ### setTollStopWarningListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setTollStopWarningListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-tollstopwarninglistener" title="interface in com.here.sdk.navigation">TollStopWarningListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive notifications about the upcoming toll stop. Setting null value to the listener will unset the listener. This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    </div>

    Parameters:  
    `value` -

    Object to receive information on the upcoming toll stop.

    </div>

  - <div id="sdk-for-android-navigate-getRailwayCrossingWarningListener" class="section detail">

    ### getRailwayCrossingWarningListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-railwaycrossingwarninglistener" title="interface in com.here.sdk.navigation">RailwayCrossingWarningListener</a></span> <span class="element-name">getRailwayCrossingWarningListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive notifications about railway crossings on the current road. Railway crossing notifications are given regardless if a route is set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Returns:  
    Object to receive notifications about railway crossings on the current road.

    </div>

  - <div id="sdk-for-android-navigate-setRailwayCrossingWarningListener-com-here-sdk-navigation-RailwayCrossingWarningListener" class="section detail">

    ### setRailwayCrossingWarningListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setRailwayCrossingWarningListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-railwaycrossingwarninglistener" title="interface in com.here.sdk.navigation">RailwayCrossingWarningListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive notifications about railway crossings on the current road. Railway crossing notifications are given regardless if a route is set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Parameters:  
    `value` -

    Object to receive notifications about railway crossings on the current road.

    </div>

  - <div id="sdk-for-android-navigate-getLowSpeedZoneWarningListener" class="section detail">

    ### getLowSpeedZoneWarningListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-lowspeedzonewarninglistener" title="interface in com.here.sdk.navigation">LowSpeedZoneWarningListener</a></span> <span class="element-name">getLowSpeedZoneWarningListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive notifications about low speed zones on the current road. Low speed zone notifications are given regardless if a route is set. This listener is currently available only for Japan. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Returns:  
    Object to receive notifications about low speed zones on the current road.

    </div>

  - <div id="sdk-for-android-navigate-setLowSpeedZoneWarningListener-com-here-sdk-navigation-LowSpeedZoneWarningListener" class="section detail">

    ### setLowSpeedZoneWarningListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setLowSpeedZoneWarningListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-lowspeedzonewarninglistener" title="interface in com.here.sdk.navigation">LowSpeedZoneWarningListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive notifications about low speed zones on the current road. Low speed zone notifications are given regardless if a route is set. This listener is currently available only for Japan. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Parameters:  
    `value` -

    Object to receive notifications about low speed zones on the current road.

    </div>

  - <div id="sdk-for-android-navigate-getTrafficMergeWarningListener" class="section detail">

    ### getTrafficMergeWarningListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarninglistener" title="interface in com.here.sdk.navigation">TrafficMergeWarningListener</a></span> <span class="element-name">getTrafficMergeWarningListener</span>()

    </div>

    <div class="block">

    Gets the listener to receive notifications about merging traffic to the current road. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Returns:  
    Object to receive notifications about merging traffic to the current road.

    </div>

  - <div id="sdk-for-android-navigate-setTrafficMergeWarningListener-com-here-sdk-navigation-TrafficMergeWarningListener" class="section detail">

    ### setTrafficMergeWarningListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setTrafficMergeWarningListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarninglistener" title="interface in com.here.sdk.navigation">TrafficMergeWarningListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener to receive notifications about merging traffic to the current road. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Parameters:  
    `value` -

    Object to receive notifications about merging traffic to the current road.

    </div>

  - <div id="sdk-for-android-navigate-getTrafficMergeWarningOptions" class="section detail">

    ### getTrafficMergeWarningOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarningoptions" title="class in com.here.sdk.navigation">TrafficMergeWarningOptions</a></span> <span class="element-name">getTrafficMergeWarningOptions</span>()

    </div>

    <div class="block">

    Gets merging traffic warning options that allow to configure merging traffic notifications to be passed to TrafficMergeWarningListener .

    </div>

    Returns:  
    Merging traffic warning options that allow to configure merging traffic notifications to be passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarninglistener" title="interface in com.here.sdk.navigation">`TrafficMergeWarningListener`</a>.

    </div>

  - <div id="sdk-for-android-navigate-setTrafficMergeWarningOptions-com-here-sdk-navigation-TrafficMergeWarningOptions" class="section detail">

    ### setTrafficMergeWarningOptions

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setTrafficMergeWarningOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarningoptions" title="class in com.here.sdk.navigation">TrafficMergeWarningOptions</a> value)</span>

    </div>

    <div class="block">

    Sets merging traffic warning options that allow to configure merging traffic notifications to be passed to TrafficMergeWarningListener .

    </div>

    Parameters:  
    `value` -

    Merging traffic warning options that allow to configure merging traffic notifications to be passed to <a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarninglistener" title="interface in com.here.sdk.navigation">`TrafficMergeWarningListener`</a>.

    </div>

  - <div id="sdk-for-android-navigate-getOffRoadDestinationReachedListener" class="section detail">

    ### getOffRoadDestinationReachedListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-offroaddestinationreachedlistener" title="interface in com.here.sdk.navigation">OffRoadDestinationReachedListener</a></span> <span class="element-name">getOffRoadDestinationReachedListener</span>()

    </div>

    <div class="block">

    Gets the listener that notifies when the off-road destination has been reached. Off-road destination reached notifications only occurs if a route has been set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Returns:  
    Object to receive the notification about the arrival at the off-road destination.

    </div>

  - <div id="sdk-for-android-navigate-setOffRoadDestinationReachedListener-com-here-sdk-navigation-OffRoadDestinationReachedListener" class="section detail">

    ### setOffRoadDestinationReachedListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setOffRoadDestinationReachedListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-offroaddestinationreachedlistener" title="interface in com.here.sdk.navigation">OffRoadDestinationReachedListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener that notifies when the off-road destination has been reached. Off-road destination reached notifications only occurs if a route has been set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Parameters:  
    `value` -

    Object to receive the notification about the arrival at the off-road destination.

    </div>

  - <div id="sdk-for-android-navigate-getOffRoadProgressListener" class="section detail">

    ### getOffRoadProgressListener

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-offroadprogresslistener" title="interface in com.here.sdk.navigation">OffRoadProgressListener</a></span> <span class="element-name">getOffRoadProgressListener</span>()

    </div>

    <div class="block">

    Gets the listener that notifies about off-road progress. Off-road progress notifications only occurs if a route has been set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Returns:  
    Object to receive the notification about the off-road progress.

    </div>

  - <div id="sdk-for-android-navigate-setOffRoadProgressListener-com-here-sdk-navigation-OffRoadProgressListener" class="section detail">

    ### setOffRoadProgressListener

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setOffRoadProgressListener</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-navigation-offroadprogresslistener" title="interface in com.here.sdk.navigation">OffRoadProgressListener</a> value)</span>

    </div>

    <div class="block">

    Sets the listener that notifies about off-road progress. Off-road progress notifications only occurs if a route has been set. Setting null value to the listener will unset the listener. It returns null when no listener is set by an user.

    </div>

    Parameters:  
    `value` -

    Object to receive the notification about the off-road progress.

    </div>

  - <div id="sdk-for-android-navigate-getManeuverNotificationOptions" class="section detail">

    ### getManeuverNotificationOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions" title="class in com.here.sdk.navigation">ManeuverNotificationOptions</a></span> <span class="element-name">getManeuverNotificationOptions</span>()

    </div>

    <div class="block">

    Gets the maneuver notification options. Notifications are only available if a route is present.

    </div>

    Returns:  
    Options used for maneuver notifications.

    </div>

  - <div id="sdk-for-android-navigate-setManeuverNotificationOptions-com-here-sdk-navigation-ManeuverNotificationOptions" class="section detail">

    ### setManeuverNotificationOptions

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setManeuverNotificationOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationoptions" title="class in com.here.sdk.navigation">ManeuverNotificationOptions</a> value)</span>

    </div>

    <div class="block">

    Sets the maneuver notification options. Notifications are only available if a route is present.

    </div>

    Parameters:  
    `value` -

    Options used for maneuver notifications.

    </div>

  - <div id="sdk-for-android-navigate-getEventTextOptions" class="section detail">

    ### getEventTextOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-eventtextoptions" title="class in com.here.sdk.navigation">EventTextOptions</a></span> <span class="element-name">getEventTextOptions</span>()

    </div>

    <div class="block">

    Gets the text notification options. Notifications are only available if a route is present.

    </div>

    Returns:  
    Options used for text notifications.

    </div>

  - <div id="sdk-for-android-navigate-setEventTextOptions-com-here-sdk-navigation-EventTextOptions" class="section detail">

    ### setEventTextOptions

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setEventTextOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-eventtextoptions" title="class in com.here.sdk.navigation">EventTextOptions</a> value)</span>

    </div>

    <div class="block">

    Sets the text notification options. Notifications are only available if a route is present.

    </div>

    Parameters:  
    `value` -

    Options used for text notifications.

    </div>

  - <div id="sdk-for-android-navigate-getSpeedWarningOptions" class="section detail">

    ### getSpeedWarningOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-speedwarningoptions" title="class in com.here.sdk.navigation">SpeedWarningOptions</a></span> <span class="element-name">getSpeedWarningOptions</span>()

    </div>

    <div class="block">

    Gets the speed warning options.

    </div>

    Returns:  
    Options used for the speed warning feature.

    </div>

  - <div id="sdk-for-android-navigate-setSpeedWarningOptions-com-here-sdk-navigation-SpeedWarningOptions" class="section detail">

    ### setSpeedWarningOptions

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setSpeedWarningOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedwarningoptions" title="class in com.here.sdk.navigation">SpeedWarningOptions</a> value)</span>

    </div>

    <div class="block">

    Sets the speed warning options.

    </div>

    Parameters:  
    `value` -

    Options used for the speed warning feature.

    </div>

  - <div id="sdk-for-android-navigate-isEnableTunnelExtrapolation" class="section detail">

    ### isEnableTunnelExtrapolation

    <div class="member-signature">

    <span class="return-type">boolean</span> <span class="element-name">isEnableTunnelExtrapolation</span>()

    </div>

    <div class="block">

    Return true if tunnel extrapolation is enabled otherwise false . By default the tunnel extrapolation is enabled.

    </div>

    Returns:  
    Defines whether to enable or disable tunnel extrapolation.

    </div>

  - <div id="sdk-for-android-navigate-setEnableTunnelExtrapolation-boolean" class="section detail">

    ### setEnableTunnelExtrapolation

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setEnableTunnelExtrapolation</span><wbr></wbr><span class="parameters">(boolean value)</span>

    </div>

    <div class="block">

    Set to true to enable tunnel extrapolation, set to false to disable tunnel extrapolation. By default the tunnel extrapolation is enabled.

    </div>

    Parameters:  
    `value` -

    Defines whether to enable or disable tunnel extrapolation.

    </div>

  - <div id="sdk-for-android-navigate-isPassthroughWaypointsHandlingEnabled" class="section detail">

    ### isPassthroughWaypointsHandlingEnabled

    <div class="member-signature">

    <span class="return-type">boolean</span> <span class="element-name">isPassthroughWaypointsHandlingEnabled</span>()

    </div>

    <div class="block">

    Return true if handling of passthrough waypoints is enabled, otherwise - false . By default the handling of passthrough waypoints is disabled.

    </div>

    Returns:  
    Defines whether to enable or disable handling of passthrough waypoints.

    </div>

  - <div id="sdk-for-android-navigate-setPassthroughWaypointsHandlingEnabled-boolean" class="section detail">

    ### setPassthroughWaypointsHandlingEnabled

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setPassthroughWaypointsHandlingEnabled</span><wbr></wbr><span class="parameters">(boolean value)</span>

    </div>

    <div class="block">

    Set to true enables handling of passthrough waypoints, set to false disables handling of passthrough waypoints. By default the handling of passthrough waypoints is disabled.

    </div>

    Parameters:  
    `value` -

    Defines whether to enable or disable handling of passthrough waypoints.

    </div>

  - <div id="sdk-for-android-navigate-getTrafficOnRoute" class="section detail">

    ### getTrafficOnRoute

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-trafficonroute" title="class in com.here.sdk.routing">TrafficOnRoute</a></span> <span class="element-name">getTrafficOnRoute</span>()

    </div>

    <div class="block">

    Gets the traffic information for the current route. This impacts RouteProgress updates as the duration of the SectionProgress might change. However, the remaining distance and the route geometry will remain unchanged.

    </div>

    Returns:  
    Traffic information for the current route.

    </div>

  - <div id="sdk-for-android-navigate-setTrafficOnRoute-com-here-sdk-routing-TrafficOnRoute" class="section detail">

    ### setTrafficOnRoute

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">setTrafficOnRoute</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-routing-trafficonroute" title="class in com.here.sdk.routing">TrafficOnRoute</a> value)</span>

    </div>

    <div class="block">

    Sets the traffic information for the current route. This impacts RouteProgress updates as the duration of the SectionProgress might change. However, the remaining distance and the route geometry will remain unchanged.

    </div>

    Parameters:  
    `value` -

    Traffic information for the current route.

    </div>

  - <div id="sdk-for-android-navigate-getLocationManager" class="section detail">

    ### getLocationManager

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapmatcher-locationmanager" title="class in com.here.sdk.mapmatcher">LocationManager</a></span> <span class="element-name">getLocationManager</span>()

    </div>

    <div class="block">

    Gets the location manager instance used by the navigator.

    </div>

    Returns:  
    The location manager used by the navigator for map-matched location processing.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

