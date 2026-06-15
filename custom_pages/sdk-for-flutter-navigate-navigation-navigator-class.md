---
title: "Navigator class abstract"
slug: "sdk-for-flutter-navigate-navigation-navigator-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Navigator-class.html -->


<div>
<h1>Navigator class abstract</h1></div>

<p>This class provides the basic navigation functionality.</p>
<p>It provides
notifications about current map-matched location updates (see <a href="sdk-for-flutter-navigate-navigation-navigablelocation-class">NavigableLocation</a>).
And, if a route has been set, about the route progress (see <a href="sdk-for-flutter-navigate-navigation-routeprogress-class">RouteProgress</a>),
route deviations (see <a href="sdk-for-flutter-navigate-navigation-routedeviation-class">RouteDeviation</a>) and maneuver notifications (see
<a href="sdk-for-flutter-navigate-navigation-eventtextlistener-class">EventTextListener</a>).</p>
<p>All transport modes are supported for turn-by-turn navigation, except for public transit.
Public transit routes may lead to unsafe and unexpected results.</p>
<p>Navigation support for bus routes can be sometimes a bit limited and bus lane assistance and
turn-by-turn bus instructions may not be as appropriate as expected.</p>
<p>The <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode</a> is determined from the provided <a href="sdk-for-flutter-navigate-routing-route-class">Route</a> instance,
but the actual <a href="sdk-for-flutter-navigate-routing-sectiontransportmode">SectionTransportMode</a> can vary along a route, for example, when a
ferry must be taken. When no route is set, the <a href="sdk-for-flutter-navigate-navigation-navigablelocation-class">NavigableLocation</a> assumes a drive
scenario.</p>
<p>This class continuously reacts to new locations provided from a location source and acts as a
<a href="sdk-for-flutter-navigate-core-locationlistener-class">LocationListener</a>.
The accuracy of the positioning increases with the update frequency. At least one update per second
should be provided. More information can be found at <code>LocationAccuracy.NAVIGATION</code>.</p>
<p><strong>Note:</strong>
Even without provided locations, for example, while driving through a tunnel, this class
can interpolate missing location events and still send <a href="sdk-for-flutter-navigate-navigation-navigablelocation-class">NavigableLocation</a>,
<a href="sdk-for-flutter-navigate-navigation-routeprogress-class">RouteProgress</a> and maneuver notifications.</p>


<ul><li>Implemented types</li></ul>


<h2>Constructors</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-navigator-navigator">Navigator</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigator-navigator-withengine">Navigator.withEngine</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-bordercrossingwarninglistener">borderCrossingWarningListener</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-bordercrossingwarningoptions">borderCrossingWarningOptions</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-currentsituationlaneassistanceviewlistener">currentSituationLaneAssistanceViewListener</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-dangerzonewarninglistener">dangerZoneWarningListener</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-destinationreachedlistener">destinationReachedListener</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-environmentalzonewarninglistener">environmentalZoneWarningListener</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-eventtextlistener">eventTextListener</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-eventtextoptions">eventTextOptions</a></li><li><a href="sdk-for-flutter-navigate-core-locationlistener-hashcode">hashCode</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-isenabletunnelextrapolation">isEnableTunnelExtrapolation</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-ispassthroughwaypointshandlingenabled">isPassthroughWaypointsHandlingEnabled</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-junctionviewlaneassistancelistener">junctionViewLaneAssistanceListener</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-locationmanager">locationManager</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-lowspeedzonewarninglistener">lowSpeedZoneWarningListener</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-maneuvernotificationoptions">maneuverNotificationOptions</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-maneuverviewlaneassistancelistener">maneuverViewLaneAssistanceListener</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-milestonestatuslistener">milestoneStatusListener</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-navigablelocationlistener">navigableLocationListener</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-offroaddestinationreachedlistener">offRoadDestinationReachedListener</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-offroadprogresslistener">offRoadProgressListener</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-postactionlistener">postActionListener</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-railwaycrossingwarninglistener">railwayCrossingWarningListener</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-realisticviewwarninglistener">realisticViewWarningListener</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-realisticviewwarningoptions">realisticViewWarningOptions</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-roadattributeslistener">roadAttributesListener</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-roadsignwarninglistener">roadSignWarningListener</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-roadsignwarningoptions">roadSignWarningOptions</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-roadtextslistener">roadTextsListener</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-route">route</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-routedeviationlistener">routeDeviationListener</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-routeprogresslistener">routeProgressListener</a></li><li><a href="sdk-for-flutter-navigate-core-locationlistener-runtimetype">runtimeType</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-safetycamerawarninglistener">safetyCameraWarningListener</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-safetycamerawarningoptions">safetyCameraWarningOptions</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-schoolzonewarninglistener">schoolZoneWarningListener</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-schoolzonewarningoptions">schoolZoneWarningOptions</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-speedlimitlistener">speedLimitListener</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-speedwarninglistener">speedWarningListener</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-speedwarningoptions">speedWarningOptions</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-tollstopwarninglistener">tollStopWarningListener</a></li><li><a class="deprecated" href="sdk-for-flutter-navigate-navigation-navigatorinterface-trackingtransportprofile">trackingTransportProfile</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-trackingtransportspecification">trackingTransportSpecification</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-trafficmergewarninglistener">trafficMergeWarningListener</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-trafficmergewarningoptions">trafficMergeWarningOptions</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-trafficonroute">trafficOnRoute</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-truckrestrictionswarninglistener">truckRestrictionsWarningListener</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-truckrestrictionswarningoptions">truckRestrictionsWarningOptions</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-warnerengine">warnerEngine</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-calculateremainingdistanceinmeters">calculateRemainingDistanceInMeters</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-getmaneuver">getManeuver</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-getmaneuvernotificationtimingoptionswithtimingprofile">getManeuverNotificationTimingOptionsWithTimingProfile</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-getwarningnotificationdistances">getWarningNotificationDistances</a></li><li><a href="sdk-for-flutter-navigate-core-locationlistener-nosuchmethod">noSuchMethod</a></li><li><a href="sdk-for-flutter-navigate-core-locationlistener-onlocationupdated">onLocationUpdated</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-repeatlastmaneuvernotification">repeatLastManeuverNotification</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-setcustomoption">setCustomOption</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-setmaneuvernotificationtimingoptionswithtimingprofile">setManeuverNotificationTimingOptionsWithTimingProfile</a></li><li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-setwarningnotificationdistances">setWarningNotificationDistances</a></li><li><a href="sdk-for-flutter-navigate-core-locationlistener-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="sdk-for-flutter-navigate-core-locationlistener-operator-equals">operator ==</a></li></ul>


<h2>Static Methods</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-navigator-getavailablelanguagesformaneuvernotifications">getAvailableLanguagesForManeuverNotifications</a></li></ul>

 



</div>
`
}</HTMLBlock>
