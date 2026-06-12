---
title: "NavigatorInterface class abstract"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- NavigatorInterface-class.html -->


<div>
<h1>NavigatorInterface class abstract</h1></div>

<p>This abstract class provides the basic functionality needed to run a navigation session.</p>


<ul><li>Implemented types</li><li>Implementers</li></ul>


<h2>Constructors</h2>
<ul><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-navigatorinterface">NavigatorInterface</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-bordercrossingwarninglistener">borderCrossingWarningListener</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-bordercrossingwarningoptions">borderCrossingWarningOptions</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-currentsituationlaneassistanceviewlistener">currentSituationLaneAssistanceViewListener</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-dangerzonewarninglistener">dangerZoneWarningListener</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-destinationreachedlistener">destinationReachedListener</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-environmentalzonewarninglistener">environmentalZoneWarningListener</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-eventtextlistener">eventTextListener</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-eventtextoptions">eventTextOptions</a></li><li><a href="/sdk-for-flutter-navigate-core-locationlistener-hashcode">hashCode</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-isenabletunnelextrapolation">isEnableTunnelExtrapolation</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-ispassthroughwaypointshandlingenabled">isPassthroughWaypointsHandlingEnabled</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-junctionviewlaneassistancelistener">junctionViewLaneAssistanceListener</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-locationmanager">locationManager</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-lowspeedzonewarninglistener">lowSpeedZoneWarningListener</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-maneuvernotificationoptions">maneuverNotificationOptions</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-maneuverviewlaneassistancelistener">maneuverViewLaneAssistanceListener</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-milestonestatuslistener">milestoneStatusListener</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-navigablelocationlistener">navigableLocationListener</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-offroaddestinationreachedlistener">offRoadDestinationReachedListener</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-offroadprogresslistener">offRoadProgressListener</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-postactionlistener">postActionListener</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-railwaycrossingwarninglistener">railwayCrossingWarningListener</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-realisticviewwarninglistener">realisticViewWarningListener</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-realisticviewwarningoptions">realisticViewWarningOptions</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-roadattributeslistener">roadAttributesListener</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-roadsignwarninglistener">roadSignWarningListener</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-roadsignwarningoptions">roadSignWarningOptions</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-roadtextslistener">roadTextsListener</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-route">route</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-routedeviationlistener">routeDeviationListener</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-routeprogresslistener">routeProgressListener</a></li><li><a href="/sdk-for-flutter-navigate-core-locationlistener-runtimetype">runtimeType</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-safetycamerawarninglistener">safetyCameraWarningListener</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-safetycamerawarningoptions">safetyCameraWarningOptions</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-schoolzonewarninglistener">schoolZoneWarningListener</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-schoolzonewarningoptions">schoolZoneWarningOptions</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-speedlimitlistener">speedLimitListener</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-speedwarninglistener">speedWarningListener</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-speedwarningoptions">speedWarningOptions</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-tollstopwarninglistener">tollStopWarningListener</a></li><li><a class="deprecated" href="/sdk-for-flutter-navigate-navigation-navigatorinterface-trackingtransportprofile">trackingTransportProfile</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-trackingtransportspecification">trackingTransportSpecification</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-trafficmergewarninglistener">trafficMergeWarningListener</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-trafficmergewarningoptions">trafficMergeWarningOptions</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-trafficonroute">trafficOnRoute</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-truckrestrictionswarninglistener">truckRestrictionsWarningListener</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-truckrestrictionswarningoptions">truckRestrictionsWarningOptions</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-warnerengine">warnerEngine</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-calculateremainingdistanceinmeters">calculateRemainingDistanceInMeters</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-getmaneuver">getManeuver</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-getmaneuvernotificationtimingoptionswithtimingprofile">getManeuverNotificationTimingOptionsWithTimingProfile</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-getwarningnotificationdistances">getWarningNotificationDistances</a></li><li><a href="/sdk-for-flutter-navigate-core-locationlistener-nosuchmethod">noSuchMethod</a></li><li><a href="/sdk-for-flutter-navigate-core-locationlistener-onlocationupdated">onLocationUpdated</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-repeatlastmaneuvernotification">repeatLastManeuverNotification</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-setcustomoption">setCustomOption</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-setmaneuvernotificationtimingoptionswithtimingprofile">setManeuverNotificationTimingOptionsWithTimingProfile</a></li><li><a href="/sdk-for-flutter-navigate-navigation-navigatorinterface-setwarningnotificationdistances">setWarningNotificationDistances</a></li><li><a href="/sdk-for-flutter-navigate-core-locationlistener-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="/sdk-for-flutter-navigate-core-locationlistener-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
