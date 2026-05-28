---
title: "Navigator class abstract"
slug: "sdk-for-flutter-navigate-navigation-navigator-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Navigator-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="navigation/Navigator-class.html#constructors">Constructors</a></li>
<li><a href="navigation/Navigator/Navigator.html">Navigator</a></li>
<li><a href="navigation/Navigator/Navigator.withEngine.html">withEngine</a></li>
<li class="section-title inherited">
<a href="navigation/Navigator-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="navigation/NavigatorInterface/borderCrossingWarningListener.html">borderCrossingWarningListener</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/borderCrossingWarningOptions.html">borderCrossingWarningOptions</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/currentSituationLaneAssistanceViewListener.html">currentSituationLaneAssistanceViewListener</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/dangerZoneWarningListener.html">dangerZoneWarningListener</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/destinationReachedListener.html">destinationReachedListener</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/environmentalZoneWarningListener.html">environmentalZoneWarningListener</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/eventTextListener.html">eventTextListener</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/eventTextOptions.html">eventTextOptions</a></li>
<li class="inherited"><a href="core/LocationListener/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/isEnableTunnelExtrapolation.html">isEnableTunnelExtrapolation</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/isPassthroughWaypointsHandlingEnabled.html">isPassthroughWaypointsHandlingEnabled</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/junctionViewLaneAssistanceListener.html">junctionViewLaneAssistanceListener</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/locationManager.html">locationManager</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/lowSpeedZoneWarningListener.html">lowSpeedZoneWarningListener</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/maneuverNotificationOptions.html">maneuverNotificationOptions</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/maneuverViewLaneAssistanceListener.html">maneuverViewLaneAssistanceListener</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/milestoneStatusListener.html">milestoneStatusListener</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/navigableLocationListener.html">navigableLocationListener</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/offRoadDestinationReachedListener.html">offRoadDestinationReachedListener</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/offRoadProgressListener.html">offRoadProgressListener</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/postActionListener.html">postActionListener</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/railwayCrossingWarningListener.html">railwayCrossingWarningListener</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/realisticViewWarningListener.html">realisticViewWarningListener</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/realisticViewWarningOptions.html">realisticViewWarningOptions</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/roadAttributesListener.html">roadAttributesListener</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/roadSignWarningListener.html">roadSignWarningListener</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/roadSignWarningOptions.html">roadSignWarningOptions</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/roadTextsListener.html">roadTextsListener</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/route.html">route</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/routeDeviationListener.html">routeDeviationListener</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/routeProgressListener.html">routeProgressListener</a></li>
<li class="inherited"><a href="core/LocationListener/runtimeType.html">runtimeType</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/safetyCameraWarningListener.html">safetyCameraWarningListener</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/safetyCameraWarningOptions.html">safetyCameraWarningOptions</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/schoolZoneWarningListener.html">schoolZoneWarningListener</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/schoolZoneWarningOptions.html">schoolZoneWarningOptions</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/speedLimitListener.html">speedLimitListener</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/speedWarningListener.html">speedWarningListener</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/speedWarningOptions.html">speedWarningOptions</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/tollStopWarningListener.html">tollStopWarningListener</a></li>
<li class="inherited"><a class="deprecated" href="navigation/NavigatorInterface/trackingTransportProfile.html">trackingTransportProfile</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/trackingTransportSpecification.html">trackingTransportSpecification</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/trafficMergeWarningListener.html">trafficMergeWarningListener</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/trafficMergeWarningOptions.html">trafficMergeWarningOptions</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/trafficOnRoute.html">trafficOnRoute</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/truckRestrictionsWarningListener.html">truckRestrictionsWarningListener</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/truckRestrictionsWarningOptions.html">truckRestrictionsWarningOptions</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/warnerEngine.html">warnerEngine</a></li>
<li class="section-title inherited"><a href="navigation/Navigator-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/calculateRemainingDistanceInMeters.html">calculateRemainingDistanceInMeters</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/getManeuver.html">getManeuver</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/getManeuverNotificationTimingOptionsWithTimingProfile.html">getManeuverNotificationTimingOptionsWithTimingProfile</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/getWarningNotificationDistances.html">getWarningNotificationDistances</a></li>
<li class="inherited"><a href="core/LocationListener/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="core/LocationListener/onLocationUpdated.html">onLocationUpdated</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/repeatLastManeuverNotification.html">repeatLastManeuverNotification</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/setCustomOption.html">setCustomOption</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/setManeuverNotificationTimingOptionsWithTimingProfile.html">setManeuverNotificationTimingOptionsWithTimingProfile</a></li>
<li class="inherited"><a href="navigation/NavigatorInterface/setWarningNotificationDistances.html">setWarningNotificationDistances</a></li>
<li class="inherited"><a href="core/LocationListener/toString.html">toString</a></li>
<li class="section-title inherited"><a href="navigation/Navigator-class.html#operators">Operators</a></li>
<li class="inherited"><a href="core/LocationListener/operator_equals.html">operator ==</a></li>
<li class="section-title"><a href="navigation/Navigator-class.html#static-methods">Static methods</a></li>
<li><a href="navigation/Navigator/getAvailableLanguagesForManeuverNotifications.html">getAvailableLanguagesForManeuverNotifications</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">Navigator class</li>
</ol>
<div class="self-name">Navigator</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/Navigator-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>Navigator class abstract</h1></div>
<section class="desc markdown">
<p>This class provides the basic navigation functionality.</p>
<p>It provides
notifications about current map-matched location updates (see /sdk-for-flutter-navigate-navigation-navigablelocation-class).
And, if a route has been set, about the route progress (see /sdk-for-flutter-navigate-navigation-routeprogress-class),
route deviations (see /sdk-for-flutter-navigate-navigation-routedeviation-class) and maneuver notifications (see
/sdk-for-flutter-navigate-navigation-eventtextlistener-class).</p>
<p>All transport modes are supported for turn-by-turn navigation, except for public transit.
Public transit routes may lead to unsafe and unexpected results.</p>
<p>Navigation support for bus routes can be sometimes a bit limited and bus lane assistance and
turn-by-turn bus instructions may not be as appropriate as expected.</p>
<p>The /sdk-for-flutter-navigate-transport-transportmode is determined from the provided /sdk-for-flutter-navigate-routing-route-class instance,
but the actual /sdk-for-flutter-navigate-routing-sectiontransportmode can vary along a route, for example, when a
ferry must be taken. When no route is set, the /sdk-for-flutter-navigate-navigation-navigablelocation-class assumes a drive
scenario.</p>
<p>This class continuously reacts to new locations provided from a location source and acts as a
/sdk-for-flutter-navigate-core-locationlistener-class.
The accuracy of the positioning increases with the update frequency. At least one update per second
should be provided. More information can be found at <code>LocationAccuracy.NAVIGATION</code>.</p>
<p><strong>Note:</strong>
Even without provided locations, for example, while driving through a tunnel, this class
can interpolate missing location events and still send /sdk-for-flutter-navigate-navigation-navigablelocation-class,
/sdk-for-flutter-navigate-navigation-routeprogress-class and maneuver notifications.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Implemented types</dt>
<dd>
<ul class="comma-separated clazz-relationships">
<li>/sdk-for-flutter-navigate-navigation-navigatorinterface-class</li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="Navigator">
/sdk-for-flutter-navigate-navigation-navigator-navigator()
</dt>
<dd>
          Creates a new instance of this class.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="Navigator.withEngine">
/sdk-for-flutter-navigate-navigation-navigator-navigator-withengine(/sdk-for-flutter-navigate-core-engine-sdknativeengine-class sdkEngine)
</dt>
<dd>
          Creates a new instance of this class.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="borderCrossingWarningListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-bordercrossingwarninglistener
↔ /sdk-for-flutter-navigate-navigation-bordercrossingwarninglistener-class?
</dt>
<dd class="inherited">
  Object to receive notifications about border crossings on the current road.
Border crossing notifications are given only if a route is present.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener to receive notifications about border crossings on the current road.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="borderCrossingWarningOptions">
/sdk-for-flutter-navigate-navigation-navigatorinterface-bordercrossingwarningoptions
↔ /sdk-for-flutter-navigate-navigation-bordercrossingwarningoptions-class
</dt>
<dd class="inherited">
  Border crossing warning options to be passed to /sdk-for-flutter-navigate-navigation-bordercrossingwarninglistener-class. These options
allow the filtering of the border crossing warnings received and set the notification distances.
Gets border crossing warning options to be passed to /sdk-for-flutter-navigate-navigation-bordercrossingwarninglistener-class.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="currentSituationLaneAssistanceViewListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-currentsituationlaneassistanceviewlistener
↔ /sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-class?
</dt>
<dd class="inherited">
  Object to receive current situation lane assistance view notifications.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener  to receive current situation lane assistance view notifications.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="dangerZoneWarningListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-dangerzonewarninglistener
↔ /sdk-for-flutter-navigate-navigation-dangerzonewarninglistener-class?
</dt>
<dd class="inherited">
  Object to receive notification on approaching danger zones.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener to receive current danger zones notifications.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="destinationReachedListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-destinationreachedlistener
↔ /sdk-for-flutter-navigate-navigation-destinationreachedlistener-class?
</dt>
<dd class="inherited">
  Object to receive the notification about the arrival at the destination.
Destination reached notifications only occurs if a route has been set.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener that notify when the destination has been reached.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="environmentalZoneWarningListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-environmentalzonewarninglistener
↔ /sdk-for-flutter-navigate-navigation-environmentalzonewarninglistener-class?
</dt>
<dd class="inherited">
  Object to receive notification on approaching environmental zones.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener to receive current environmental zones notifications.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="eventTextListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-eventtextlistener
↔ /sdk-for-flutter-navigate-navigation-eventtextlistener-class?
</dt>
<dd class="inherited">
  Object to receive text notifications when they are available.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
<strong>Note:</strong> In order to receive the text notification emitted for the traffic merge warner,
when <code>TrafficMergeWarningOptions.enable_text_notification</code> has been enabled, the <code>sdk.navigation.EventTextListener</code> must be enabled as well.
Gets the listener that notifies when a text notification is available.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="eventTextOptions">
/sdk-for-flutter-navigate-navigation-navigatorinterface-eventtextoptions
↔ /sdk-for-flutter-navigate-navigation-eventtextoptions-class
</dt>
<dd class="inherited">
  Options used for text notifications.
Notifications are only available if a route is present.
Gets the text notification options.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-core-locationlistener-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="isEnableTunnelExtrapolation">
/sdk-for-flutter-navigate-navigation-navigatorinterface-isenabletunnelextrapolation
↔ bool
</dt>
<dd class="inherited">
  Defines whether to enable or disable tunnel extrapolation.
By default the tunnel extrapolation is enabled.
Return <code>true</code> if tunnel extrapolation is enabled otherwise <code>false</code>.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="isPassthroughWaypointsHandlingEnabled">
/sdk-for-flutter-navigate-navigation-navigatorinterface-ispassthroughwaypointshandlingenabled
↔ bool
</dt>
<dd class="inherited">
  Defines whether to enable or disable handling of passthrough waypoints.
By default the handling of passthrough waypoints is disabled.
Return <code>true</code> if handling of passthrough waypoints is enabled, otherwise - <code>false</code>.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="junctionViewLaneAssistanceListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-junctionviewlaneassistancelistener
↔ /sdk-for-flutter-navigate-navigation-junctionviewlaneassistancelistener-class?
</dt>
<dd class="inherited">
  Object to receive junction view lane assistance notifications.
Junction view lane assistance notifications only occurs if a route has been set.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener  to receive junction view lane assistance notifications.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="locationManager">
/sdk-for-flutter-navigate-navigation-navigatorinterface-locationmanager
→ /sdk-for-flutter-navigate-mapmatcher-locationmanager-class
</dt>
<dd class="inherited">
  The location manager used by the navigator for map-matched location processing.
Gets the location manager instance used by the navigator.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="lowSpeedZoneWarningListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-lowspeedzonewarninglistener
↔ /sdk-for-flutter-navigate-navigation-lowspeedzonewarninglistener-class?
</dt>
<dd class="inherited">
  Object to receive notifications about low speed zones on the current road.
Low speed zone notifications are given regardless if a route is set. This listener is currently
available <em>only</em> for Japan.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener to receive notifications about low speed zones on the current road.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="maneuverNotificationOptions">
/sdk-for-flutter-navigate-navigation-navigatorinterface-maneuvernotificationoptions
↔ /sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-class
</dt>
<dd class="inherited">
  Options used for maneuver notifications.
Notifications are only available if a route is present.
Gets the maneuver notification options.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="maneuverViewLaneAssistanceListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-maneuverviewlaneassistancelistener
↔ /sdk-for-flutter-navigate-navigation-maneuverviewlaneassistancelistener-class?
</dt>
<dd class="inherited">
  Object to receive maneuver view lane assistance notifications.
Maneuver view lane assistance notifications only occurs if a route has been set.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener  to receive maneuver view lane assistance notifications.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="milestoneStatusListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-milestonestatuslistener
↔ /sdk-for-flutter-navigate-navigation-milestonestatuslistener-class?
</dt>
<dd class="inherited">
  Object to receive notifications about the arrival at each /sdk-for-flutter-navigate-navigation-milestone-class or missing it.
It informs on all waypoints (passed or missed) that
are of type /sdk-for-flutter-navigate-navigation-milestonetype but excludes the
starting waypoint.
Waypoints of type /sdk-for-flutter-navigate-navigation-milestonetype are excluded, by default,
but can be included via /sdk-for-flutter-navigate-navigation-navigatorinterface-ispassthroughwaypointshandlingenabled.
Milestone status notifications only occurs if a route has been set.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener that notifies when a /sdk-for-flutter-navigate-navigation-milestone-class has been reached or missed.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="navigableLocationListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-navigablelocationlistener
↔ /sdk-for-flutter-navigate-navigation-navigablelocationlistener-class?
</dt>
<dd class="inherited">
  Object to receive notifications about the current location.
It returns <code>null</code> when no listener is set by an user.
Gets the listener that notifies current location updates.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="offRoadDestinationReachedListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-offroaddestinationreachedlistener
↔ /sdk-for-flutter-navigate-navigation-offroaddestinationreachedlistener-class?
</dt>
<dd class="inherited">
  Object to receive the notification about the arrival at the off-road destination.
Off-road destination reached notifications only occurs if a route has been set.
Setting <code>null</code> value to the listener will unset
the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener that notifies when the off-road destination has been reached.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="offRoadProgressListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-offroadprogresslistener
↔ /sdk-for-flutter-navigate-navigation-offroadprogresslistener-class?
</dt>
<dd class="inherited">
  Object to receive the notification about the off-road progress.
Off-road progress notifications only occurs if a route has been set.
Setting <code>null</code> value to the listener will unset
the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener that notifies about off-road progress.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="postActionListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-postactionlistener
↔ /sdk-for-flutter-navigate-navigation-postactionlistener-class?
</dt>
<dd class="inherited">
  Object to receive post action notifications, such as a charge action at a charging station.
Post actions notifications only occurs if a route has been set.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener  to receive post action notifications, such as a charge action at a charging station.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="railwayCrossingWarningListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-railwaycrossingwarninglistener
↔ /sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-class?
</dt>
<dd class="inherited">
  Object to receive notifications about railway crossings on the current road.
Railway crossing notifications are given regardless if a route is set.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener to receive notifications about railway crossings on the current road.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="realisticViewWarningListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-realisticviewwarninglistener
↔ /sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-class?
</dt>
<dd class="inherited">
  Object to receive notifications about junction views on the current road.
Setting <code>null</code> value to the listener will unset
the listener.
This feature requires a map version greater or equal to 67 in order to function properly.
It returns <code>null</code> when no listener is set by an user.
Gets the listener to receive notifications about junction views on the current road.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="realisticViewWarningOptions">
/sdk-for-flutter-navigate-navigation-navigatorinterface-realisticviewwarningoptions
↔ /sdk-for-flutter-navigate-navigation-realisticviewwarningoptions-class
</dt>
<dd class="inherited">
  Realistic view warning options.
It allow to filter realistic views to be passed to /sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-class.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="roadAttributesListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-roadattributeslistener
↔ /sdk-for-flutter-navigate-navigation-roadattributeslistener-class?
</dt>
<dd class="inherited">
  Object to receive notifications about attributes of the current road.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener  to receive notifications about attributes of the current road.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="roadSignWarningListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-roadsignwarninglistener
↔ /sdk-for-flutter-navigate-navigation-roadsignwarninglistener-class?
</dt>
<dd class="inherited">
  Object to receive notifications about road signs on the current road.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener to receive notifications about road signs on the current road.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="roadSignWarningOptions">
/sdk-for-flutter-navigate-navigation-navigatorinterface-roadsignwarningoptions
↔ /sdk-for-flutter-navigate-navigation-roadsignwarningoptions-class
</dt>
<dd class="inherited">
  Road sign warning options that allow to filter road sings to be passed to /sdk-for-flutter-navigate-navigation-roadsignwarninglistener-class.
Gets road sign warning options that allow to filter road signs to be passed to /sdk-for-flutter-navigate-navigation-roadsignwarninglistener-class.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="roadTextsListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-roadtextslistener
↔ /sdk-for-flutter-navigate-navigation-roadtextslistener-class?
</dt>
<dd class="inherited">
  Object to receive notifications about the textual attributes of the current road.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener  to receive notifications about the textual attributes of the current road.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="route">
/sdk-for-flutter-navigate-navigation-navigatorinterface-route
↔ /sdk-for-flutter-navigate-routing-route-class?
</dt>
<dd class="inherited">
  The route to navigate.
Gets and sets the route that is being navigated.
If not set, only the current location information will be
provided through /sdk-for-flutter-navigate-navigation-navigablelocationlistener-class.
If set, both route progress (/sdk-for-flutter-navigate-navigation-routeprogresslistener-class) and route deviation
(/sdk-for-flutter-navigate-navigation-routedeviationlistener-class) will receive notifications on updates.
A route may fail to be set if it is generated by an incompatible engine, in which case the operation has no effect.
Gets the route that is being navigated.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="routeDeviationListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-routedeviationlistener
↔ /sdk-for-flutter-navigate-navigation-routedeviationlistener-class?
</dt>
<dd class="inherited">
  Object to receive notifications about deviations from the route if any occurs.
Route deviation notifications only occurs if a route has been set.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener that notifies when deviation from the route is observed.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="routeProgressListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-routeprogresslistener
↔ /sdk-for-flutter-navigate-navigation-routeprogresslistener-class?
</dt>
<dd class="inherited">
  Object to receive notifications about navigation route progress.
Route progress notifications only occurs if the route has been set.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener that notifies when a route progress change occurs.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-core-locationlistener-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="safetyCameraWarningListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-safetycamerawarninglistener
↔ /sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-class?
</dt>
<dd class="inherited">
  Object to receive safety camera warner notifications.
If a listener  is present, notifications about
safety speed cameras will be also sent via /sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-class.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener  to receive safety camera warning notifications.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="safetyCameraWarningOptions">
/sdk-for-flutter-navigate-navigation-navigatorinterface-safetycamerawarningoptions
↔ /sdk-for-flutter-navigate-navigation-safetycamerawarningoptions-class
</dt>
<dd class="inherited">
  Safety camera warning options to be passed to /sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-class.
These options allow the enabling or disabling the text notification for the warner.
Gets safety camera warning options to be passed to /sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-class.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="schoolZoneWarningListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-schoolzonewarninglistener
↔ /sdk-for-flutter-navigate-navigation-schoolzonewarninglistener-class?
</dt>
<dd class="inherited">
  Object to receive notifications about school zones on the current road.
Setting <code>null</code> value to the listener will unset the listener.
school zones on the current road.
It returns <code>null</code> when no listener is set by an user.
Gets the listener to receive notifications about school zones on the current road.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="schoolZoneWarningOptions">
/sdk-for-flutter-navigate-navigation-navigatorinterface-schoolzonewarningoptions
↔ /sdk-for-flutter-navigate-navigation-schoolzonewarningoptions-class
</dt>
<dd class="inherited">
  School zone warning options
It allow to configure school zone notifications to be passed to
/sdk-for-flutter-navigate-navigation-schoolzonewarninglistener-class.
Gets school zone warning options that allow to configure school zone notifications to be
passed to /sdk-for-flutter-navigate-navigation-schoolzonewarninglistener-class.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="speedLimitListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-speedlimitlistener
↔ /sdk-for-flutter-navigate-navigation-speedlimitlistener-class?
</dt>
<dd class="inherited">
  Object to receive notifications about the speed limit of the current road.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener  to receive notifications about the speed limit of the current road.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="speedWarningListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-speedwarninglistener
↔ /sdk-for-flutter-navigate-navigation-speedwarninglistener-class?
</dt>
<dd class="inherited">
  Object to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener to receive notifications
when a speed limit on a road is exceeded or driving speed is restored back to normal.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="speedWarningOptions">
/sdk-for-flutter-navigate-navigation-navigatorinterface-speedwarningoptions
↔ /sdk-for-flutter-navigate-navigation-speedwarningoptions-class
</dt>
<dd class="inherited">
  Options used for the speed warning feature.
Gets the speed warning options.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="tollStopWarningListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-tollstopwarninglistener
↔ /sdk-for-flutter-navigate-navigation-tollstopwarninglistener-class?
</dt>
<dd class="inherited">
  Object to receive information on the upcoming toll stop.
Setting <code>null</code> value to the listener will unset
the listener.
This is a <strong>beta release</strong> of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.
Gets the listener to receive notifications about
the the upcoming toll stop.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="trackingTransportProfile">
/sdk-for-flutter-navigate-navigation-navigatorinterface-trackingtransportprofile
↔ /sdk-for-flutter-navigate-core-transportprofile-class?
</dt>
<dd class="inherited">
  Defines the transport profile for the /sdk-for-flutter-navigate-navigation-navigator-class, when no route is present.
Properly setting the transport profile optimizes the navigation experience, and improves resource consumption.
For example, a /sdk-for-flutter-navigate-core-transportprofile-class can be defined with a /sdk-for-flutter-navigate-transport-vehicleprofile-class.
A vehicle profile can have several parameters such as /sdk-for-flutter-navigate-transport-vehicletype to set the
source of information describing the vehicle.
The default is a /sdk-for-flutter-navigate-transport-vehicletype profile.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="trackingTransportSpecification">
/sdk-for-flutter-navigate-navigation-navigatorinterface-trackingtransportspecification
↔ /sdk-for-flutter-navigate-transport-transportspecification-class?
</dt>
<dd class="inherited">
  Defines the transport specification for the /sdk-for-flutter-navigate-navigation-navigator-class, when no route is present.
Properly setting the transport specification optimizes the navigation experience, and improves
resource consumption. An /sdk-for-flutter-navigate-transport-transportspecification-class must have the /sdk-for-flutter-navigate-transport-transportspecification-transportmode set.
A transport specification can have several parameters defined such as /sdk-for-flutter-navigate-transport-vehiclespecification-lengthincentimeters
defined in /sdk-for-flutter-navigate-transport-transportspecification-vehiclespecification to set the source of information describing the vehicle.
By default the /sdk-for-flutter-navigate-transport-transportspecification-class will have the transport mode set to /sdk-for-flutter-navigate-transport-transportmode.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="trafficMergeWarningListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-trafficmergewarninglistener
↔ /sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-class?
</dt>
<dd class="inherited">
  Object to receive notifications about merging traffic to the current road.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener to receive notifications about
merging traffic to the current road.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="trafficMergeWarningOptions">
/sdk-for-flutter-navigate-navigation-navigatorinterface-trafficmergewarningoptions
↔ /sdk-for-flutter-navigate-navigation-trafficmergewarningoptions-class
</dt>
<dd class="inherited">
  Merging traffic warning options that allow to configure merging traffic notifications to be passed to
/sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-class.
Gets merging traffic warning options that allow to configure merging traffic notifications to be
passed to /sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-class.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="trafficOnRoute">
/sdk-for-flutter-navigate-navigation-navigatorinterface-trafficonroute
↔ /sdk-for-flutter-navigate-routing-trafficonroute-class?
</dt>
<dd class="inherited">
  Traffic information for the current route.
This impacts <code>RouteProgress</code> updates as the duration of the <code>SectionProgress</code> might change.
However, the remaining distance and the route geometry will remain unchanged.
Gets the traffic information for the current route.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="truckRestrictionsWarningListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-truckrestrictionswarninglistener
↔ /sdk-for-flutter-navigate-navigation-truckrestrictionswarninglistener-class?
</dt>
<dd class="inherited">
  Object to receive notifications about truck restrictions on the current road.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener  to receive notifications about
truck restrictions on the current road.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="truckRestrictionsWarningOptions">
/sdk-for-flutter-navigate-navigation-navigatorinterface-truckrestrictionswarningoptions
↔ /sdk-for-flutter-navigate-navigation-truckrestrictionswarningoptions-class
</dt>
<dd class="inherited">
  Truck restrictions warning options that allow to filter truck restrictions to be passed to /sdk-for-flutter-navigate-navigation-truckrestrictionswarninglistener-class.
Gets truck restrictions warning options that allow to filter truck restrictions to be
passed to /sdk-for-flutter-navigate-navigation-truckrestrictionswarninglistener-class.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property inherited" id="warnerEngine">
/sdk-for-flutter-navigate-navigation-navigatorinterface-warnerengine
→ /sdk-for-flutter-navigate-warner-warnerengine-class
</dt>
<dd class="inherited">
  Warner engine used by the navigator.
This engine can be used to configure navigation warnings.
Gets the warner engine used by the navigator.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="calculateRemainingDistanceInMeters">
/sdk-for-flutter-navigate-navigation-navigatorinterface-calculateremainingdistanceinmeters(<wbr/>/sdk-for-flutter-navigate-core-geocoordinates-class coordinates)
    → int?

</dt>
<dd class="inherited">
  This method calculates the distance between the current position and given coordinates.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="getManeuver">
/sdk-for-flutter-navigate-navigation-navigatorinterface-getmaneuver(<wbr/>int index)
    → /sdk-for-flutter-navigate-routing-maneuver-class?

</dt>
<dd class="inherited">
  Returns maneuver at the given index.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="getManeuverNotificationTimingOptionsWithTimingProfile">
/sdk-for-flutter-navigate-navigation-navigatorinterface-getmaneuvernotificationtimingoptionswithtimingprofile(<wbr/>/sdk-for-flutter-navigate-transport-transportmode transportMode, /sdk-for-flutter-navigate-navigation-timingprofile timingProfile)
    → /sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-class

</dt>
<dd class="inherited">
  Returns maneuver notification timing options with default values given the combination of transport mode and timing profile.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="getWarningNotificationDistances">
/sdk-for-flutter-navigate-navigation-navigatorinterface-getwarningnotificationdistances(<wbr/>/sdk-for-flutter-navigate-navigation-warningtype warningType)
    → /sdk-for-flutter-navigate-navigation-warningnotificationdistances-class

</dt>
<dd class="inherited">
  Returns the warning notification distances for the requested warning type.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-core-locationlistener-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="onLocationUpdated">
/sdk-for-flutter-navigate-core-locationlistener-onlocationupdated(<wbr/>/sdk-for-flutter-navigate-core-location-class location)
    → void

</dt>
<dd class="inherited">
  Called each time a new location is available.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="repeatLastManeuverNotification">
/sdk-for-flutter-navigate-navigation-navigatorinterface-repeatlastmaneuvernotification(<wbr/>)
    → void

</dt>
<dd class="inherited">
  Call of this function is used to trigger the navigator to repeat the last maneuver notification based on the current position.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="setCustomOption">
/sdk-for-flutter-navigate-navigation-navigatorinterface-setcustomoption(<wbr/>String key, String value)
    → void

</dt>
<dd class="inherited">
  This method sets custom options that controls navigator behavior.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="setManeuverNotificationTimingOptionsWithTimingProfile">
/sdk-for-flutter-navigate-navigation-navigatorinterface-setmaneuvernotificationtimingoptionswithtimingprofile(<wbr/>/sdk-for-flutter-navigate-transport-transportmode transportMode, /sdk-for-flutter-navigate-navigation-timingprofile timingProfile, /sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-class options)
    → bool

</dt>
<dd class="inherited">
  Set timing option values for the combination of transport mode and timing profile.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="setWarningNotificationDistances">
/sdk-for-flutter-navigate-navigation-navigatorinterface-setwarningnotificationdistances(<wbr/>/sdk-for-flutter-navigate-navigation-warningtype warningType, /sdk-for-flutter-navigate-navigation-warningnotificationdistances-class warningNotificationDistances)
    → bool

</dt>
<dd class="inherited">
  Set the warning notification distances for the specified warning types.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-core-locationlistener-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
/sdk-for-flutter-navigate-core-locationlistener-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="static-methods">
<h2>Static Methods</h2>
<dl class="callables">
<dt class="callable" id="getAvailableLanguagesForManeuverNotifications">
/sdk-for-flutter-navigate-navigation-navigator-getavailablelanguagesformaneuvernotifications(<wbr/>)
    → List&lt;<wbr/>/sdk-for-flutter-navigate-core-languagecode&gt;

</dt>
<dd>
  Returns the list of languages for maneuver notification currently available in the SDK.
  

</dd>
</dl>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">Navigator class</li>
</ol>
<h5>navigation library</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
`
}</HTMLBlock>
