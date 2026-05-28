---
title: "NavigatorInterface class abstract"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- NavigatorInterface-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="navigation/NavigatorInterface-class.html#constructors">Constructors</a></li>
<li><a href="navigation/NavigatorInterface/NavigatorInterface.html">NavigatorInterface</a></li>
<li class="section-title">
<a href="navigation/NavigatorInterface-class.html#instance-properties">Properties</a>
</li>
<li><a href="navigation/NavigatorInterface/borderCrossingWarningListener.html">borderCrossingWarningListener</a></li>
<li><a href="navigation/NavigatorInterface/borderCrossingWarningOptions.html">borderCrossingWarningOptions</a></li>
<li><a href="navigation/NavigatorInterface/currentSituationLaneAssistanceViewListener.html">currentSituationLaneAssistanceViewListener</a></li>
<li><a href="navigation/NavigatorInterface/dangerZoneWarningListener.html">dangerZoneWarningListener</a></li>
<li><a href="navigation/NavigatorInterface/destinationReachedListener.html">destinationReachedListener</a></li>
<li><a href="navigation/NavigatorInterface/environmentalZoneWarningListener.html">environmentalZoneWarningListener</a></li>
<li><a href="navigation/NavigatorInterface/eventTextListener.html">eventTextListener</a></li>
<li><a href="navigation/NavigatorInterface/eventTextOptions.html">eventTextOptions</a></li>
<li class="inherited"><a href="core/LocationListener/hashCode.html">hashCode</a></li>
<li><a href="navigation/NavigatorInterface/isEnableTunnelExtrapolation.html">isEnableTunnelExtrapolation</a></li>
<li><a href="navigation/NavigatorInterface/isPassthroughWaypointsHandlingEnabled.html">isPassthroughWaypointsHandlingEnabled</a></li>
<li><a href="navigation/NavigatorInterface/junctionViewLaneAssistanceListener.html">junctionViewLaneAssistanceListener</a></li>
<li><a href="navigation/NavigatorInterface/locationManager.html">locationManager</a></li>
<li><a href="navigation/NavigatorInterface/lowSpeedZoneWarningListener.html">lowSpeedZoneWarningListener</a></li>
<li><a href="navigation/NavigatorInterface/maneuverNotificationOptions.html">maneuverNotificationOptions</a></li>
<li><a href="navigation/NavigatorInterface/maneuverViewLaneAssistanceListener.html">maneuverViewLaneAssistanceListener</a></li>
<li><a href="navigation/NavigatorInterface/milestoneStatusListener.html">milestoneStatusListener</a></li>
<li><a href="navigation/NavigatorInterface/navigableLocationListener.html">navigableLocationListener</a></li>
<li><a href="navigation/NavigatorInterface/offRoadDestinationReachedListener.html">offRoadDestinationReachedListener</a></li>
<li><a href="navigation/NavigatorInterface/offRoadProgressListener.html">offRoadProgressListener</a></li>
<li><a href="navigation/NavigatorInterface/postActionListener.html">postActionListener</a></li>
<li><a href="navigation/NavigatorInterface/railwayCrossingWarningListener.html">railwayCrossingWarningListener</a></li>
<li><a href="navigation/NavigatorInterface/realisticViewWarningListener.html">realisticViewWarningListener</a></li>
<li><a href="navigation/NavigatorInterface/realisticViewWarningOptions.html">realisticViewWarningOptions</a></li>
<li><a href="navigation/NavigatorInterface/roadAttributesListener.html">roadAttributesListener</a></li>
<li><a href="navigation/NavigatorInterface/roadSignWarningListener.html">roadSignWarningListener</a></li>
<li><a href="navigation/NavigatorInterface/roadSignWarningOptions.html">roadSignWarningOptions</a></li>
<li><a href="navigation/NavigatorInterface/roadTextsListener.html">roadTextsListener</a></li>
<li><a href="navigation/NavigatorInterface/route.html">route</a></li>
<li><a href="navigation/NavigatorInterface/routeDeviationListener.html">routeDeviationListener</a></li>
<li><a href="navigation/NavigatorInterface/routeProgressListener.html">routeProgressListener</a></li>
<li class="inherited"><a href="core/LocationListener/runtimeType.html">runtimeType</a></li>
<li><a href="navigation/NavigatorInterface/safetyCameraWarningListener.html">safetyCameraWarningListener</a></li>
<li><a href="navigation/NavigatorInterface/safetyCameraWarningOptions.html">safetyCameraWarningOptions</a></li>
<li><a href="navigation/NavigatorInterface/schoolZoneWarningListener.html">schoolZoneWarningListener</a></li>
<li><a href="navigation/NavigatorInterface/schoolZoneWarningOptions.html">schoolZoneWarningOptions</a></li>
<li><a href="navigation/NavigatorInterface/speedLimitListener.html">speedLimitListener</a></li>
<li><a href="navigation/NavigatorInterface/speedWarningListener.html">speedWarningListener</a></li>
<li><a href="navigation/NavigatorInterface/speedWarningOptions.html">speedWarningOptions</a></li>
<li><a href="navigation/NavigatorInterface/tollStopWarningListener.html">tollStopWarningListener</a></li>
<li><a class="deprecated" href="navigation/NavigatorInterface/trackingTransportProfile.html">trackingTransportProfile</a></li>
<li><a href="navigation/NavigatorInterface/trackingTransportSpecification.html">trackingTransportSpecification</a></li>
<li><a href="navigation/NavigatorInterface/trafficMergeWarningListener.html">trafficMergeWarningListener</a></li>
<li><a href="navigation/NavigatorInterface/trafficMergeWarningOptions.html">trafficMergeWarningOptions</a></li>
<li><a href="navigation/NavigatorInterface/trafficOnRoute.html">trafficOnRoute</a></li>
<li><a href="navigation/NavigatorInterface/truckRestrictionsWarningListener.html">truckRestrictionsWarningListener</a></li>
<li><a href="navigation/NavigatorInterface/truckRestrictionsWarningOptions.html">truckRestrictionsWarningOptions</a></li>
<li><a href="navigation/NavigatorInterface/warnerEngine.html">warnerEngine</a></li>
<li class="section-title"><a href="navigation/NavigatorInterface-class.html#instance-methods">Methods</a></li>
<li><a href="navigation/NavigatorInterface/calculateRemainingDistanceInMeters.html">calculateRemainingDistanceInMeters</a></li>
<li><a href="navigation/NavigatorInterface/getManeuver.html">getManeuver</a></li>
<li><a href="navigation/NavigatorInterface/getManeuverNotificationTimingOptionsWithTimingProfile.html">getManeuverNotificationTimingOptionsWithTimingProfile</a></li>
<li><a href="navigation/NavigatorInterface/getWarningNotificationDistances.html">getWarningNotificationDistances</a></li>
<li class="inherited"><a href="core/LocationListener/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="core/LocationListener/onLocationUpdated.html">onLocationUpdated</a></li>
<li><a href="navigation/NavigatorInterface/repeatLastManeuverNotification.html">repeatLastManeuverNotification</a></li>
<li><a href="navigation/NavigatorInterface/setCustomOption.html">setCustomOption</a></li>
<li><a href="navigation/NavigatorInterface/setManeuverNotificationTimingOptionsWithTimingProfile.html">setManeuverNotificationTimingOptionsWithTimingProfile</a></li>
<li><a href="navigation/NavigatorInterface/setWarningNotificationDistances.html">setWarningNotificationDistances</a></li>
<li class="inherited"><a href="core/LocationListener/toString.html">toString</a></li>
<li class="section-title inherited"><a href="navigation/NavigatorInterface-class.html#operators">Operators</a></li>
<li class="inherited"><a href="core/LocationListener/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">NavigatorInterface class</li>
</ol>
<div class="self-name">NavigatorInterface</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/NavigatorInterface-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>NavigatorInterface class abstract</h1></div>
<section class="desc markdown">
<p>This abstract class provides the basic functionality needed to run a navigation session.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Implemented types</dt>
<dd>
<ul class="comma-separated clazz-relationships">
<li>/sdk-for-flutter-navigate-core-locationlistener-class</li>
</ul>
</dd>
<dt>Implementers</dt>
<dd><ul class="comma-separated clazz-relationships">
<li>/sdk-for-flutter-navigate-navigation-navigator-class</li>
<li>/sdk-for-flutter-navigate-navigation-visualnavigator-class</li>
</ul></dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="NavigatorInterface">
/sdk-for-flutter-navigate-navigation-navigatorinterface-navigatorinterface(void onLocationUpdatedLambda(/sdk-for-flutter-navigate-core-location-class), /sdk-for-flutter-navigate-routing-maneuver-class? getManeuverLambda(int), /sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-class getManeuverNotificationTimingOptionsWithTimingProfileLambda(/sdk-for-flutter-navigate-transport-transportmode, /sdk-for-flutter-navigate-navigation-timingprofile), bool setManeuverNotificationTimingOptionsWithTimingProfileLambda(/sdk-for-flutter-navigate-transport-transportmode, /sdk-for-flutter-navigate-navigation-timingprofile, /sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-class), /sdk-for-flutter-navigate-navigation-warningnotificationdistances-class getWarningNotificationDistancesLambda(/sdk-for-flutter-navigate-navigation-warningtype), bool setWarningNotificationDistancesLambda(/sdk-for-flutter-navigate-navigation-warningtype, /sdk-for-flutter-navigate-navigation-warningnotificationdistances-class), void repeatLastManeuverNotificationLambda(), int? calculateRemainingDistanceInMetersLambda(/sdk-for-flutter-navigate-core-geocoordinates-class), void setCustomOptionLambda(String, String), /sdk-for-flutter-navigate-routing-route-class? routeGetLambda(), void routeSetLambda(/sdk-for-flutter-navigate-routing-route-class?), /sdk-for-flutter-navigate-core-transportprofile-class? trackingTransportProfileGetLambda(), void trackingTransportProfileSetLambda(/sdk-for-flutter-navigate-core-transportprofile-class?), /sdk-for-flutter-navigate-transport-transportspecification-class? trackingTransportSpecificationGetLambda(), void trackingTransportSpecificationSetLambda(/sdk-for-flutter-navigate-transport-transportspecification-class?), /sdk-for-flutter-navigate-navigation-navigablelocationlistener-class? navigableLocationListenerGetLambda(), void navigableLocationListenerSetLambda(/sdk-for-flutter-navigate-navigation-navigablelocationlistener-class?), /sdk-for-flutter-navigate-navigation-routeprogresslistener-class? routeProgressListenerGetLambda(), void routeProgressListenerSetLambda(/sdk-for-flutter-navigate-navigation-routeprogresslistener-class?), /sdk-for-flutter-navigate-navigation-routedeviationlistener-class? routeDeviationListenerGetLambda(), void routeDeviationListenerSetLambda(/sdk-for-flutter-navigate-navigation-routedeviationlistener-class?), /sdk-for-flutter-navigate-navigation-eventtextlistener-class? eventTextListenerGetLambda(), void eventTextListenerSetLambda(/sdk-for-flutter-navigate-navigation-eventtextlistener-class?), /sdk-for-flutter-navigate-navigation-milestonestatuslistener-class? milestoneStatusListenerGetLambda(), void milestoneStatusListenerSetLambda(/sdk-for-flutter-navigate-navigation-milestonestatuslistener-class?), /sdk-for-flutter-navigate-navigation-destinationreachedlistener-class? destinationReachedListenerGetLambda(), void destinationReachedListenerSetLambda(/sdk-for-flutter-navigate-navigation-destinationreachedlistener-class?), /sdk-for-flutter-navigate-navigation-speedwarninglistener-class? speedWarningListenerGetLambda(), void speedWarningListenerSetLambda(/sdk-for-flutter-navigate-navigation-speedwarninglistener-class?), /sdk-for-flutter-navigate-navigation-maneuverviewlaneassistancelistener-class? maneuverViewLaneAssistanceListenerGetLambda(), void maneuverViewLaneAssistanceListenerSetLambda(/sdk-for-flutter-navigate-navigation-maneuverviewlaneassistancelistener-class?), /sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-class? currentSituationLaneAssistanceViewListenerGetLambda(), void currentSituationLaneAssistanceViewListenerSetLambda(/sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-class?), /sdk-for-flutter-navigate-navigation-environmentalzonewarninglistener-class? environmentalZoneWarningListenerGetLambda(), void environmentalZoneWarningListenerSetLambda(/sdk-for-flutter-navigate-navigation-environmentalzonewarninglistener-class?), /sdk-for-flutter-navigate-navigation-junctionviewlaneassistancelistener-class? junctionViewLaneAssistanceListenerGetLambda(), void junctionViewLaneAssistanceListenerSetLambda(/sdk-for-flutter-navigate-navigation-junctionviewlaneassistancelistener-class?), /sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-class? safetyCameraWarningListenerGetLambda(), void safetyCameraWarningListenerSetLambda(/sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-class?), /sdk-for-flutter-navigate-navigation-safetycamerawarningoptions-class safetyCameraWarningOptionsGetLambda(), void safetyCameraWarningOptionsSetLambda(/sdk-for-flutter-navigate-navigation-safetycamerawarningoptions-class), /sdk-for-flutter-navigate-navigation-dangerzonewarninglistener-class? dangerZoneWarningListenerGetLambda(), void dangerZoneWarningListenerSetLambda(/sdk-for-flutter-navigate-navigation-dangerzonewarninglistener-class?), /sdk-for-flutter-navigate-navigation-truckrestrictionswarninglistener-class? truckRestrictionsWarningListenerGetLambda(), void truckRestrictionsWarningListenerSetLambda(/sdk-for-flutter-navigate-navigation-truckrestrictionswarninglistener-class?), /sdk-for-flutter-navigate-warner-warnerengine-class warnerEngineGetLambda(), /sdk-for-flutter-navigate-navigation-truckrestrictionswarningoptions-class truckRestrictionsWarningOptionsGetLambda(), void truckRestrictionsWarningOptionsSetLambda(/sdk-for-flutter-navigate-navigation-truckrestrictionswarningoptions-class), /sdk-for-flutter-navigate-navigation-postactionlistener-class? postActionListenerGetLambda(), void postActionListenerSetLambda(/sdk-for-flutter-navigate-navigation-postactionlistener-class?), /sdk-for-flutter-navigate-navigation-speedlimitlistener-class? speedLimitListenerGetLambda(), void speedLimitListenerSetLambda(/sdk-for-flutter-navigate-navigation-speedlimitlistener-class?), /sdk-for-flutter-navigate-navigation-roadtextslistener-class? roadTextsListenerGetLambda(), void roadTextsListenerSetLambda(/sdk-for-flutter-navigate-navigation-roadtextslistener-class?), /sdk-for-flutter-navigate-navigation-roadattributeslistener-class? roadAttributesListenerGetLambda(), void roadAttributesListenerSetLambda(/sdk-for-flutter-navigate-navigation-roadattributeslistener-class?), /sdk-for-flutter-navigate-navigation-roadsignwarninglistener-class? roadSignWarningListenerGetLambda(), void roadSignWarningListenerSetLambda(/sdk-for-flutter-navigate-navigation-roadsignwarninglistener-class?), /sdk-for-flutter-navigate-navigation-roadsignwarningoptions-class roadSignWarningOptionsGetLambda(), void roadSignWarningOptionsSetLambda(/sdk-for-flutter-navigate-navigation-roadsignwarningoptions-class), /sdk-for-flutter-navigate-navigation-schoolzonewarninglistener-class? schoolZoneWarningListenerGetLambda(), void schoolZoneWarningListenerSetLambda(/sdk-for-flutter-navigate-navigation-schoolzonewarninglistener-class?), /sdk-for-flutter-navigate-navigation-schoolzonewarningoptions-class schoolZoneWarningOptionsGetLambda(), void schoolZoneWarningOptionsSetLambda(/sdk-for-flutter-navigate-navigation-schoolzonewarningoptions-class), /sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-class? realisticViewWarningListenerGetLambda(), void realisticViewWarningListenerSetLambda(/sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-class?), /sdk-for-flutter-navigate-navigation-realisticviewwarningoptions-class realisticViewWarningOptionsGetLambda(), void realisticViewWarningOptionsSetLambda(/sdk-for-flutter-navigate-navigation-realisticviewwarningoptions-class), /sdk-for-flutter-navigate-navigation-bordercrossingwarninglistener-class? borderCrossingWarningListenerGetLambda(), void borderCrossingWarningListenerSetLambda(/sdk-for-flutter-navigate-navigation-bordercrossingwarninglistener-class?), /sdk-for-flutter-navigate-navigation-bordercrossingwarningoptions-class borderCrossingWarningOptionsGetLambda(), void borderCrossingWarningOptionsSetLambda(/sdk-for-flutter-navigate-navigation-bordercrossingwarningoptions-class), /sdk-for-flutter-navigate-navigation-tollstopwarninglistener-class? tollStopWarningListenerGetLambda(), void tollStopWarningListenerSetLambda(/sdk-for-flutter-navigate-navigation-tollstopwarninglistener-class?), /sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-class? railwayCrossingWarningListenerGetLambda(), void railwayCrossingWarningListenerSetLambda(/sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-class?), /sdk-for-flutter-navigate-navigation-lowspeedzonewarninglistener-class? lowSpeedZoneWarningListenerGetLambda(), void lowSpeedZoneWarningListenerSetLambda(/sdk-for-flutter-navigate-navigation-lowspeedzonewarninglistener-class?), /sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-class? trafficMergeWarningListenerGetLambda(), void trafficMergeWarningListenerSetLambda(/sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-class?), /sdk-for-flutter-navigate-navigation-trafficmergewarningoptions-class trafficMergeWarningOptionsGetLambda(), void trafficMergeWarningOptionsSetLambda(/sdk-for-flutter-navigate-navigation-trafficmergewarningoptions-class), /sdk-for-flutter-navigate-navigation-offroaddestinationreachedlistener-class? offRoadDestinationReachedListenerGetLambda(), void offRoadDestinationReachedListenerSetLambda(/sdk-for-flutter-navigate-navigation-offroaddestinationreachedlistener-class?), /sdk-for-flutter-navigate-navigation-offroadprogresslistener-class? offRoadProgressListenerGetLambda(), void offRoadProgressListenerSetLambda(/sdk-for-flutter-navigate-navigation-offroadprogresslistener-class?), /sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-class maneuverNotificationOptionsGetLambda(), void maneuverNotificationOptionsSetLambda(/sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-class), /sdk-for-flutter-navigate-navigation-eventtextoptions-class eventTextOptionsGetLambda(), void eventTextOptionsSetLambda(/sdk-for-flutter-navigate-navigation-eventtextoptions-class), /sdk-for-flutter-navigate-navigation-speedwarningoptions-class speedWarningOptionsGetLambda(), void speedWarningOptionsSetLambda(/sdk-for-flutter-navigate-navigation-speedwarningoptions-class), bool isEnableTunnelExtrapolationGetLambda(), void isEnableTunnelExtrapolationSetLambda(bool), bool isPassthroughWaypointsHandlingEnabledGetLambda(), void isPassthroughWaypointsHandlingEnabledSetLambda(bool), /sdk-for-flutter-navigate-routing-trafficonroute-class? trafficOnRouteGetLambda(), void trafficOnRouteSetLambda(/sdk-for-flutter-navigate-routing-trafficonroute-class?), /sdk-for-flutter-navigate-mapmatcher-locationmanager-class locationManagerGetLambda())
</dt>
<dd>
          This abstract class provides the basic functionality needed to run a navigation session.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="borderCrossingWarningListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-bordercrossingwarninglistener
↔ /sdk-for-flutter-navigate-navigation-bordercrossingwarninglistener-class?
</dt>
<dd>
  Object to receive notifications about border crossings on the current road.
Border crossing notifications are given only if a route is present.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener to receive notifications about border crossings on the current road.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="borderCrossingWarningOptions">
/sdk-for-flutter-navigate-navigation-navigatorinterface-bordercrossingwarningoptions
↔ /sdk-for-flutter-navigate-navigation-bordercrossingwarningoptions-class
</dt>
<dd>
  Border crossing warning options to be passed to /sdk-for-flutter-navigate-navigation-bordercrossingwarninglistener-class. These options
allow the filtering of the border crossing warnings received and set the notification distances.
Gets border crossing warning options to be passed to /sdk-for-flutter-navigate-navigation-bordercrossingwarninglistener-class.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="currentSituationLaneAssistanceViewListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-currentsituationlaneassistanceviewlistener
↔ /sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-class?
</dt>
<dd>
  Object to receive current situation lane assistance view notifications.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener  to receive current situation lane assistance view notifications.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="dangerZoneWarningListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-dangerzonewarninglistener
↔ /sdk-for-flutter-navigate-navigation-dangerzonewarninglistener-class?
</dt>
<dd>
  Object to receive notification on approaching danger zones.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener to receive current danger zones notifications.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="destinationReachedListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-destinationreachedlistener
↔ /sdk-for-flutter-navigate-navigation-destinationreachedlistener-class?
</dt>
<dd>
  Object to receive the notification about the arrival at the destination.
Destination reached notifications only occurs if a route has been set.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener that notify when the destination has been reached.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="environmentalZoneWarningListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-environmentalzonewarninglistener
↔ /sdk-for-flutter-navigate-navigation-environmentalzonewarninglistener-class?
</dt>
<dd>
  Object to receive notification on approaching environmental zones.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener to receive current environmental zones notifications.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="eventTextListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-eventtextlistener
↔ /sdk-for-flutter-navigate-navigation-eventtextlistener-class?
</dt>
<dd>
  Object to receive text notifications when they are available.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
<strong>Note:</strong> In order to receive the text notification emitted for the traffic merge warner,
when <code>TrafficMergeWarningOptions.enable_text_notification</code> has been enabled, the <code>sdk.navigation.EventTextListener</code> must be enabled as well.
Gets the listener that notifies when a text notification is available.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="eventTextOptions">
/sdk-for-flutter-navigate-navigation-navigatorinterface-eventtextoptions
↔ /sdk-for-flutter-navigate-navigation-eventtextoptions-class
</dt>
<dd>
  Options used for text notifications.
Notifications are only available if a route is present.
Gets the text notification options.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-core-locationlistener-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="isEnableTunnelExtrapolation">
/sdk-for-flutter-navigate-navigation-navigatorinterface-isenabletunnelextrapolation
↔ bool
</dt>
<dd>
  Defines whether to enable or disable tunnel extrapolation.
By default the tunnel extrapolation is enabled.
Return <code>true</code> if tunnel extrapolation is enabled otherwise <code>false</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isPassthroughWaypointsHandlingEnabled">
/sdk-for-flutter-navigate-navigation-navigatorinterface-ispassthroughwaypointshandlingenabled
↔ bool
</dt>
<dd>
  Defines whether to enable or disable handling of passthrough waypoints.
By default the handling of passthrough waypoints is disabled.
Return <code>true</code> if handling of passthrough waypoints is enabled, otherwise - <code>false</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="junctionViewLaneAssistanceListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-junctionviewlaneassistancelistener
↔ /sdk-for-flutter-navigate-navigation-junctionviewlaneassistancelistener-class?
</dt>
<dd>
  Object to receive junction view lane assistance notifications.
Junction view lane assistance notifications only occurs if a route has been set.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener  to receive junction view lane assistance notifications.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="locationManager">
/sdk-for-flutter-navigate-navigation-navigatorinterface-locationmanager
→ /sdk-for-flutter-navigate-mapmatcher-locationmanager-class
</dt>
<dd>
  The location manager used by the navigator for map-matched location processing.
Gets the location manager instance used by the navigator.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="lowSpeedZoneWarningListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-lowspeedzonewarninglistener
↔ /sdk-for-flutter-navigate-navigation-lowspeedzonewarninglistener-class?
</dt>
<dd>
  Object to receive notifications about low speed zones on the current road.
Low speed zone notifications are given regardless if a route is set. This listener is currently
available <em>only</em> for Japan.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener to receive notifications about low speed zones on the current road.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maneuverNotificationOptions">
/sdk-for-flutter-navigate-navigation-navigatorinterface-maneuvernotificationoptions
↔ /sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-class
</dt>
<dd>
  Options used for maneuver notifications.
Notifications are only available if a route is present.
Gets the maneuver notification options.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maneuverViewLaneAssistanceListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-maneuverviewlaneassistancelistener
↔ /sdk-for-flutter-navigate-navigation-maneuverviewlaneassistancelistener-class?
</dt>
<dd>
  Object to receive maneuver view lane assistance notifications.
Maneuver view lane assistance notifications only occurs if a route has been set.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener  to receive maneuver view lane assistance notifications.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="milestoneStatusListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-milestonestatuslistener
↔ /sdk-for-flutter-navigate-navigation-milestonestatuslistener-class?
</dt>
<dd>
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
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="navigableLocationListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-navigablelocationlistener
↔ /sdk-for-flutter-navigate-navigation-navigablelocationlistener-class?
</dt>
<dd>
  Object to receive notifications about the current location.
It returns <code>null</code> when no listener is set by an user.
Gets the listener that notifies current location updates.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="offRoadDestinationReachedListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-offroaddestinationreachedlistener
↔ /sdk-for-flutter-navigate-navigation-offroaddestinationreachedlistener-class?
</dt>
<dd>
  Object to receive the notification about the arrival at the off-road destination.
Off-road destination reached notifications only occurs if a route has been set.
Setting <code>null</code> value to the listener will unset
the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener that notifies when the off-road destination has been reached.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="offRoadProgressListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-offroadprogresslistener
↔ /sdk-for-flutter-navigate-navigation-offroadprogresslistener-class?
</dt>
<dd>
  Object to receive the notification about the off-road progress.
Off-road progress notifications only occurs if a route has been set.
Setting <code>null</code> value to the listener will unset
the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener that notifies about off-road progress.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="postActionListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-postactionlistener
↔ /sdk-for-flutter-navigate-navigation-postactionlistener-class?
</dt>
<dd>
  Object to receive post action notifications, such as a charge action at a charging station.
Post actions notifications only occurs if a route has been set.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener  to receive post action notifications, such as a charge action at a charging station.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="railwayCrossingWarningListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-railwaycrossingwarninglistener
↔ /sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-class?
</dt>
<dd>
  Object to receive notifications about railway crossings on the current road.
Railway crossing notifications are given regardless if a route is set.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener to receive notifications about railway crossings on the current road.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="realisticViewWarningListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-realisticviewwarninglistener
↔ /sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-class?
</dt>
<dd>
  Object to receive notifications about junction views on the current road.
Setting <code>null</code> value to the listener will unset
the listener.
This feature requires a map version greater or equal to 67 in order to function properly.
It returns <code>null</code> when no listener is set by an user.
Gets the listener to receive notifications about junction views on the current road.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="realisticViewWarningOptions">
/sdk-for-flutter-navigate-navigation-navigatorinterface-realisticviewwarningoptions
↔ /sdk-for-flutter-navigate-navigation-realisticviewwarningoptions-class
</dt>
<dd>
  Realistic view warning options.
It allow to filter realistic views to be passed to /sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-class.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="roadAttributesListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-roadattributeslistener
↔ /sdk-for-flutter-navigate-navigation-roadattributeslistener-class?
</dt>
<dd>
  Object to receive notifications about attributes of the current road.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener  to receive notifications about attributes of the current road.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="roadSignWarningListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-roadsignwarninglistener
↔ /sdk-for-flutter-navigate-navigation-roadsignwarninglistener-class?
</dt>
<dd>
  Object to receive notifications about road signs on the current road.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener to receive notifications about road signs on the current road.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="roadSignWarningOptions">
/sdk-for-flutter-navigate-navigation-navigatorinterface-roadsignwarningoptions
↔ /sdk-for-flutter-navigate-navigation-roadsignwarningoptions-class
</dt>
<dd>
  Road sign warning options that allow to filter road sings to be passed to /sdk-for-flutter-navigate-navigation-roadsignwarninglistener-class.
Gets road sign warning options that allow to filter road signs to be passed to /sdk-for-flutter-navigate-navigation-roadsignwarninglistener-class.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="roadTextsListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-roadtextslistener
↔ /sdk-for-flutter-navigate-navigation-roadtextslistener-class?
</dt>
<dd>
  Object to receive notifications about the textual attributes of the current road.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener  to receive notifications about the textual attributes of the current road.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="route">
/sdk-for-flutter-navigate-navigation-navigatorinterface-route
↔ /sdk-for-flutter-navigate-routing-route-class?
</dt>
<dd>
  The route to navigate.
Gets and sets the route that is being navigated.
If not set, only the current location information will be
provided through /sdk-for-flutter-navigate-navigation-navigablelocationlistener-class.
If set, both route progress (/sdk-for-flutter-navigate-navigation-routeprogresslistener-class) and route deviation
(/sdk-for-flutter-navigate-navigation-routedeviationlistener-class) will receive notifications on updates.
A route may fail to be set if it is generated by an incompatible engine, in which case the operation has no effect.
Gets the route that is being navigated.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="routeDeviationListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-routedeviationlistener
↔ /sdk-for-flutter-navigate-navigation-routedeviationlistener-class?
</dt>
<dd>
  Object to receive notifications about deviations from the route if any occurs.
Route deviation notifications only occurs if a route has been set.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener that notifies when deviation from the route is observed.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="routeProgressListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-routeprogresslistener
↔ /sdk-for-flutter-navigate-navigation-routeprogresslistener-class?
</dt>
<dd>
  Object to receive notifications about navigation route progress.
Route progress notifications only occurs if the route has been set.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener that notifies when a route progress change occurs.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-core-locationlistener-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="safetyCameraWarningListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-safetycamerawarninglistener
↔ /sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-class?
</dt>
<dd>
  Object to receive safety camera warner notifications.
If a listener  is present, notifications about
safety speed cameras will be also sent via /sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-class.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener  to receive safety camera warning notifications.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="safetyCameraWarningOptions">
/sdk-for-flutter-navigate-navigation-navigatorinterface-safetycamerawarningoptions
↔ /sdk-for-flutter-navigate-navigation-safetycamerawarningoptions-class
</dt>
<dd>
  Safety camera warning options to be passed to /sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-class.
These options allow the enabling or disabling the text notification for the warner.
Gets safety camera warning options to be passed to /sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-class.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="schoolZoneWarningListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-schoolzonewarninglistener
↔ /sdk-for-flutter-navigate-navigation-schoolzonewarninglistener-class?
</dt>
<dd>
  Object to receive notifications about school zones on the current road.
Setting <code>null</code> value to the listener will unset the listener.
school zones on the current road.
It returns <code>null</code> when no listener is set by an user.
Gets the listener to receive notifications about school zones on the current road.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="schoolZoneWarningOptions">
/sdk-for-flutter-navigate-navigation-navigatorinterface-schoolzonewarningoptions
↔ /sdk-for-flutter-navigate-navigation-schoolzonewarningoptions-class
</dt>
<dd>
  School zone warning options
It allow to configure school zone notifications to be passed to
/sdk-for-flutter-navigate-navigation-schoolzonewarninglistener-class.
Gets school zone warning options that allow to configure school zone notifications to be
passed to /sdk-for-flutter-navigate-navigation-schoolzonewarninglistener-class.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="speedLimitListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-speedlimitlistener
↔ /sdk-for-flutter-navigate-navigation-speedlimitlistener-class?
</dt>
<dd>
  Object to receive notifications about the speed limit of the current road.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener  to receive notifications about the speed limit of the current road.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="speedWarningListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-speedwarninglistener
↔ /sdk-for-flutter-navigate-navigation-speedwarninglistener-class?
</dt>
<dd>
  Object to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener to receive notifications
when a speed limit on a road is exceeded or driving speed is restored back to normal.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="speedWarningOptions">
/sdk-for-flutter-navigate-navigation-navigatorinterface-speedwarningoptions
↔ /sdk-for-flutter-navigate-navigation-speedwarningoptions-class
</dt>
<dd>
  Options used for the speed warning feature.
Gets the speed warning options.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="tollStopWarningListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-tollstopwarninglistener
↔ /sdk-for-flutter-navigate-navigation-tollstopwarninglistener-class?
</dt>
<dd>
  Object to receive information on the upcoming toll stop.
Setting <code>null</code> value to the listener will unset
the listener.
This is a <strong>beta release</strong> of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.
Gets the listener to receive notifications about
the the upcoming toll stop.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="trackingTransportProfile">
/sdk-for-flutter-navigate-navigation-navigatorinterface-trackingtransportprofile
↔ /sdk-for-flutter-navigate-core-transportprofile-class?
</dt>
<dd>
  Defines the transport profile for the /sdk-for-flutter-navigate-navigation-navigator-class, when no route is present.
Properly setting the transport profile optimizes the navigation experience, and improves resource consumption.
For example, a /sdk-for-flutter-navigate-core-transportprofile-class can be defined with a /sdk-for-flutter-navigate-transport-vehicleprofile-class.
A vehicle profile can have several parameters such as /sdk-for-flutter-navigate-transport-vehicletype to set the
source of information describing the vehicle.
The default is a /sdk-for-flutter-navigate-transport-vehicletype profile.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="trackingTransportSpecification">
/sdk-for-flutter-navigate-navigation-navigatorinterface-trackingtransportspecification
↔ /sdk-for-flutter-navigate-transport-transportspecification-class?
</dt>
<dd>
  Defines the transport specification for the /sdk-for-flutter-navigate-navigation-navigator-class, when no route is present.
Properly setting the transport specification optimizes the navigation experience, and improves
resource consumption. An /sdk-for-flutter-navigate-transport-transportspecification-class must have the /sdk-for-flutter-navigate-transport-transportspecification-transportmode set.
A transport specification can have several parameters defined such as /sdk-for-flutter-navigate-transport-vehiclespecification-lengthincentimeters
defined in /sdk-for-flutter-navigate-transport-transportspecification-vehiclespecification to set the source of information describing the vehicle.
By default the /sdk-for-flutter-navigate-transport-transportspecification-class will have the transport mode set to /sdk-for-flutter-navigate-transport-transportmode.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="trafficMergeWarningListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-trafficmergewarninglistener
↔ /sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-class?
</dt>
<dd>
  Object to receive notifications about merging traffic to the current road.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener to receive notifications about
merging traffic to the current road.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="trafficMergeWarningOptions">
/sdk-for-flutter-navigate-navigation-navigatorinterface-trafficmergewarningoptions
↔ /sdk-for-flutter-navigate-navigation-trafficmergewarningoptions-class
</dt>
<dd>
  Merging traffic warning options that allow to configure merging traffic notifications to be passed to
/sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-class.
Gets merging traffic warning options that allow to configure merging traffic notifications to be
passed to /sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-class.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="trafficOnRoute">
/sdk-for-flutter-navigate-navigation-navigatorinterface-trafficonroute
↔ /sdk-for-flutter-navigate-routing-trafficonroute-class?
</dt>
<dd>
  Traffic information for the current route.
This impacts <code>RouteProgress</code> updates as the duration of the <code>SectionProgress</code> might change.
However, the remaining distance and the route geometry will remain unchanged.
Gets the traffic information for the current route.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="truckRestrictionsWarningListener">
/sdk-for-flutter-navigate-navigation-navigatorinterface-truckrestrictionswarninglistener
↔ /sdk-for-flutter-navigate-navigation-truckrestrictionswarninglistener-class?
</dt>
<dd>
  Object to receive notifications about truck restrictions on the current road.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
Gets the listener  to receive notifications about
truck restrictions on the current road.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="truckRestrictionsWarningOptions">
/sdk-for-flutter-navigate-navigation-navigatorinterface-truckrestrictionswarningoptions
↔ /sdk-for-flutter-navigate-navigation-truckrestrictionswarningoptions-class
</dt>
<dd>
  Truck restrictions warning options that allow to filter truck restrictions to be passed to /sdk-for-flutter-navigate-navigation-truckrestrictionswarninglistener-class.
Gets truck restrictions warning options that allow to filter truck restrictions to be
passed to /sdk-for-flutter-navigate-navigation-truckrestrictionswarninglistener-class.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="warnerEngine">
/sdk-for-flutter-navigate-navigation-navigatorinterface-warnerengine
→ /sdk-for-flutter-navigate-warner-warnerengine-class
</dt>
<dd>
  Warner engine used by the navigator.
This engine can be used to configure navigation warnings.
Gets the warner engine used by the navigator.
  <div class="features">no setter</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="calculateRemainingDistanceInMeters">
/sdk-for-flutter-navigate-navigation-navigatorinterface-calculateremainingdistanceinmeters(<wbr/>/sdk-for-flutter-navigate-core-geocoordinates-class coordinates)
    → int?

</dt>
<dd>
  This method calculates the distance between the current position and given coordinates.
  

</dd>
<dt class="callable" id="getManeuver">
/sdk-for-flutter-navigate-navigation-navigatorinterface-getmaneuver(<wbr/>int index)
    → /sdk-for-flutter-navigate-routing-maneuver-class?

</dt>
<dd>
  Returns maneuver at the given index.
  

</dd>
<dt class="callable" id="getManeuverNotificationTimingOptionsWithTimingProfile">
/sdk-for-flutter-navigate-navigation-navigatorinterface-getmaneuvernotificationtimingoptionswithtimingprofile(<wbr/>/sdk-for-flutter-navigate-transport-transportmode transportMode, /sdk-for-flutter-navigate-navigation-timingprofile timingProfile)
    → /sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-class

</dt>
<dd>
  Returns maneuver notification timing options with default values given the combination of transport mode and timing profile.
  

</dd>
<dt class="callable" id="getWarningNotificationDistances">
/sdk-for-flutter-navigate-navigation-navigatorinterface-getwarningnotificationdistances(<wbr/>/sdk-for-flutter-navigate-navigation-warningtype warningType)
    → /sdk-for-flutter-navigate-navigation-warningnotificationdistances-class

</dt>
<dd>
  Returns the warning notification distances for the requested warning type.
  

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
<dt class="callable" id="repeatLastManeuverNotification">
/sdk-for-flutter-navigate-navigation-navigatorinterface-repeatlastmaneuvernotification(<wbr/>)
    → void

</dt>
<dd>
  Call of this function is used to trigger the navigator to repeat the last maneuver notification based on the current position.
  

</dd>
<dt class="callable" id="setCustomOption">
/sdk-for-flutter-navigate-navigation-navigatorinterface-setcustomoption(<wbr/>String key, String value)
    → void

</dt>
<dd>
  This method sets custom options that controls navigator behavior.
  

</dd>
<dt class="callable" id="setManeuverNotificationTimingOptionsWithTimingProfile">
/sdk-for-flutter-navigate-navigation-navigatorinterface-setmaneuvernotificationtimingoptionswithtimingprofile(<wbr/>/sdk-for-flutter-navigate-transport-transportmode transportMode, /sdk-for-flutter-navigate-navigation-timingprofile timingProfile, /sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-class options)
    → bool

</dt>
<dd>
  Set timing option values for the combination of transport mode and timing profile.
  

</dd>
<dt class="callable" id="setWarningNotificationDistances">
/sdk-for-flutter-navigate-navigation-navigatorinterface-setwarningnotificationdistances(<wbr/>/sdk-for-flutter-navigate-navigation-warningtype warningType, /sdk-for-flutter-navigate-navigation-warningnotificationdistances-class warningNotificationDistances)
    → bool

</dt>
<dd>
  Set the warning notification distances for the specified warning types.
  

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
<li class="self-crumb">NavigatorInterface class</li>
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
