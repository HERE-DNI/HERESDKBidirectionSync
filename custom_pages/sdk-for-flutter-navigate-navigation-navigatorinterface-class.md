---
title: "NavigatorInterface class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/NavigatorInterface-class-sidebar.html">

<div>

# <span class="kind-class">NavigatorInterface</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

This abstract class provides the basic functionality needed to run a navigation session.

</div>

<div class="section">

Implemented types  
- <a href="sdk-for-flutter-navigate-core-locationlistener-class">LocationListener</a>

Implementers  
- <a href="sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>
- <a href="sdk-for-flutter-navigate-navigation-visualnavigator-class">VisualNavigator</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-navigatorinterface">NavigatorInterface</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-onLocationUpdatedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onLocationUpdatedLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-location-class">Location</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-getManeuverLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-maneuver-class">Maneuver</a>?</span> <span class="parameter-name">getManeuverLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">int</span></span>), </span><span id="sdk-for-flutter-navigate-param-getManeuverNotificationTimingOptionsWithTimingProfileLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-class">ManeuverNotificationTimingOptions</a></span> <span class="parameter-name">getManeuverNotificationTimingOptionsWithTimingProfileLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode</a></span>, </span><span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-setManeuverNotificationTimingOptionsWithTimingProfileLambda" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">setManeuverNotificationTimingOptionsWithTimingProfileLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode</a></span>, </span><span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile</a></span>, </span><span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-class">ManeuverNotificationTimingOptions</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-getWarningNotificationDistancesLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-warningnotificationdistances-class">WarningNotificationDistances</a></span> <span class="parameter-name">getWarningNotificationDistancesLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-setWarningNotificationDistancesLambda" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">setWarningNotificationDistancesLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType</a></span>, </span><span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-warningnotificationdistances-class">WarningNotificationDistances</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-repeatLastManeuverNotificationLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">repeatLastManeuverNotificationLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-calculateRemainingDistanceInMetersLambda" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">calculateRemainingDistanceInMetersLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-setCustomOptionLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">setCustomOptionLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">String</span>, </span><span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">String</span></span>), </span><span id="sdk-for-flutter-navigate-param-routeGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-route-class">Route</a>?</span> <span class="parameter-name">routeGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-routeSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">routeSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-route-class">Route</a>?</span></span>), </span><span id="sdk-for-flutter-navigate-param-trackingTransportProfileGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-transportprofile-class" class="deprecated">TransportProfile</a>?</span> <span class="parameter-name">trackingTransportProfileGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-trackingTransportProfileSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">trackingTransportProfileSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-transportprofile-class" class="deprecated">TransportProfile</a>?</span></span>), </span><span id="sdk-for-flutter-navigate-param-trackingTransportSpecificationGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a>?</span> <span class="parameter-name">trackingTransportSpecificationGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-trackingTransportSpecificationSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">trackingTransportSpecificationSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a>?</span></span>), </span><span id="sdk-for-flutter-navigate-param-navigableLocationListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-navigablelocationlistener-class">NavigableLocationListener</a>?</span> <span class="parameter-name">navigableLocationListenerGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-navigableLocationListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">navigableLocationListenerSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-navigablelocationlistener-class">NavigableLocationListener</a>?</span></span>), </span><span id="sdk-for-flutter-navigate-param-routeProgressListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-routeprogresslistener-class">RouteProgressListener</a>?</span> <span class="parameter-name">routeProgressListenerGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-routeProgressListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">routeProgressListenerSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-routeprogresslistener-class">RouteProgressListener</a>?</span></span>), </span><span id="sdk-for-flutter-navigate-param-routeDeviationListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-routedeviationlistener-class">RouteDeviationListener</a>?</span> <span class="parameter-name">routeDeviationListenerGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-routeDeviationListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">routeDeviationListenerSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-routedeviationlistener-class">RouteDeviationListener</a>?</span></span>), </span><span id="sdk-for-flutter-navigate-param-eventTextListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-eventtextlistener-class">EventTextListener</a>?</span> <span class="parameter-name">eventTextListenerGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-eventTextListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">eventTextListenerSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-eventtextlistener-class">EventTextListener</a>?</span></span>), </span><span id="sdk-for-flutter-navigate-param-milestoneStatusListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-milestonestatuslistener-class">MilestoneStatusListener</a>?</span> <span class="parameter-name">milestoneStatusListenerGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-milestoneStatusListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">milestoneStatusListenerSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-milestonestatuslistener-class">MilestoneStatusListener</a>?</span></span>), </span><span id="sdk-for-flutter-navigate-param-destinationReachedListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-destinationreachedlistener-class">DestinationReachedListener</a>?</span> <span class="parameter-name">destinationReachedListenerGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-destinationReachedListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">destinationReachedListenerSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-destinationreachedlistener-class">DestinationReachedListener</a>?</span></span>), </span><span id="sdk-for-flutter-navigate-param-speedWarningListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-speedwarninglistener-class">SpeedWarningListener</a>?</span> <span class="parameter-name">speedWarningListenerGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-speedWarningListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">speedWarningListenerSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-speedwarninglistener-class">SpeedWarningListener</a>?</span></span>), </span><span id="sdk-for-flutter-navigate-param-maneuverViewLaneAssistanceListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-maneuverviewlaneassistancelistener-class">ManeuverViewLaneAssistanceListener</a>?</span> <span class="parameter-name">maneuverViewLaneAssistanceListenerGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-maneuverViewLaneAssistanceListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">maneuverViewLaneAssistanceListenerSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-maneuverviewlaneassistancelistener-class">ManeuverViewLaneAssistanceListener</a>?</span></span>), </span><span id="sdk-for-flutter-navigate-param-currentSituationLaneAssistanceViewListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-class">CurrentSituationLaneAssistanceViewListener</a>?</span> <span class="parameter-name">currentSituationLaneAssistanceViewListenerGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-currentSituationLaneAssistanceViewListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">currentSituationLaneAssistanceViewListenerSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-class">CurrentSituationLaneAssistanceViewListener</a>?</span></span>), </span><span id="sdk-for-flutter-navigate-param-environmentalZoneWarningListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-environmentalzonewarninglistener-class">EnvironmentalZoneWarningListener</a>?</span> <span class="parameter-name">environmentalZoneWarningListenerGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-environmentalZoneWarningListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">environmentalZoneWarningListenerSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-environmentalzonewarninglistener-class">EnvironmentalZoneWarningListener</a>?</span></span>), </span><span id="sdk-for-flutter-navigate-param-junctionViewLaneAssistanceListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-junctionviewlaneassistancelistener-class">JunctionViewLaneAssistanceListener</a>?</span> <span class="parameter-name">junctionViewLaneAssistanceListenerGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-junctionViewLaneAssistanceListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">junctionViewLaneAssistanceListenerSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-junctionviewlaneassistancelistener-class">JunctionViewLaneAssistanceListener</a>?</span></span>), </span><span id="sdk-for-flutter-navigate-param-safetyCameraWarningListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-class">SafetyCameraWarningListener</a>?</span> <span class="parameter-name">safetyCameraWarningListenerGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-safetyCameraWarningListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">safetyCameraWarningListenerSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-class">SafetyCameraWarningListener</a>?</span></span>), </span><span id="sdk-for-flutter-navigate-param-safetyCameraWarningOptionsGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-safetycamerawarningoptions-class">SafetyCameraWarningOptions</a></span> <span class="parameter-name">safetyCameraWarningOptionsGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-safetyCameraWarningOptionsSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">safetyCameraWarningOptionsSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-safetycamerawarningoptions-class">SafetyCameraWarningOptions</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-dangerZoneWarningListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-dangerzonewarninglistener-class">DangerZoneWarningListener</a>?</span> <span class="parameter-name">dangerZoneWarningListenerGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-dangerZoneWarningListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">dangerZoneWarningListenerSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-dangerzonewarninglistener-class">DangerZoneWarningListener</a>?</span></span>), </span><span id="sdk-for-flutter-navigate-param-truckRestrictionsWarningListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-truckrestrictionswarninglistener-class">TruckRestrictionsWarningListener</a>?</span> <span class="parameter-name">truckRestrictionsWarningListenerGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-truckRestrictionsWarningListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">truckRestrictionsWarningListenerSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-truckrestrictionswarninglistener-class">TruckRestrictionsWarningListener</a>?</span></span>), </span><span id="sdk-for-flutter-navigate-param-warnerEngineGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-warner-warnerengine-class">WarnerEngine</a></span> <span class="parameter-name">warnerEngineGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-truckRestrictionsWarningOptionsGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-truckrestrictionswarningoptions-class">TruckRestrictionsWarningOptions</a></span> <span class="parameter-name">truckRestrictionsWarningOptionsGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-truckRestrictionsWarningOptionsSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">truckRestrictionsWarningOptionsSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-truckrestrictionswarningoptions-class">TruckRestrictionsWarningOptions</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-postActionListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-postactionlistener-class">PostActionListener</a>?</span> <span class="parameter-name">postActionListenerGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-postActionListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">postActionListenerSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-postactionlistener-class">PostActionListener</a>?</span></span>), </span><span id="sdk-for-flutter-navigate-param-speedLimitListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-speedlimitlistener-class">SpeedLimitListener</a>?</span> <span class="parameter-name">speedLimitListenerGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-speedLimitListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">speedLimitListenerSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-speedlimitlistener-class">SpeedLimitListener</a>?</span></span>), </span><span id="sdk-for-flutter-navigate-param-roadTextsListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-roadtextslistener-class">RoadTextsListener</a>?</span> <span class="parameter-name">roadTextsListenerGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-roadTextsListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">roadTextsListenerSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-roadtextslistener-class">RoadTextsListener</a>?</span></span>), </span><span id="sdk-for-flutter-navigate-param-roadAttributesListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-roadattributeslistener-class">RoadAttributesListener</a>?</span> <span class="parameter-name">roadAttributesListenerGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-roadAttributesListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">roadAttributesListenerSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-roadattributeslistener-class">RoadAttributesListener</a>?</span></span>), </span><span id="sdk-for-flutter-navigate-param-roadSignWarningListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-roadsignwarninglistener-class">RoadSignWarningListener</a>?</span> <span class="parameter-name">roadSignWarningListenerGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-roadSignWarningListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">roadSignWarningListenerSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-roadsignwarninglistener-class">RoadSignWarningListener</a>?</span></span>), </span><span id="sdk-for-flutter-navigate-param-roadSignWarningOptionsGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-roadsignwarningoptions-class">RoadSignWarningOptions</a></span> <span class="parameter-name">roadSignWarningOptionsGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-roadSignWarningOptionsSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">roadSignWarningOptionsSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-roadsignwarningoptions-class">RoadSignWarningOptions</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-schoolZoneWarningListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-schoolzonewarninglistener-class">SchoolZoneWarningListener</a>?</span> <span class="parameter-name">schoolZoneWarningListenerGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-schoolZoneWarningListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">schoolZoneWarningListenerSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-schoolzonewarninglistener-class">SchoolZoneWarningListener</a>?</span></span>), </span><span id="sdk-for-flutter-navigate-param-schoolZoneWarningOptionsGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-schoolzonewarningoptions-class">SchoolZoneWarningOptions</a></span> <span class="parameter-name">schoolZoneWarningOptionsGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-schoolZoneWarningOptionsSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">schoolZoneWarningOptionsSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-schoolzonewarningoptions-class">SchoolZoneWarningOptions</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-realisticViewWarningListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-class">RealisticViewWarningListener</a>?</span> <span class="parameter-name">realisticViewWarningListenerGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-realisticViewWarningListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">realisticViewWarningListenerSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-class">RealisticViewWarningListener</a>?</span></span>), </span><span id="sdk-for-flutter-navigate-param-realisticViewWarningOptionsGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-realisticviewwarningoptions-class">RealisticViewWarningOptions</a></span> <span class="parameter-name">realisticViewWarningOptionsGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-realisticViewWarningOptionsSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">realisticViewWarningOptionsSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-realisticviewwarningoptions-class">RealisticViewWarningOptions</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-borderCrossingWarningListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-bordercrossingwarninglistener-class">BorderCrossingWarningListener</a>?</span> <span class="parameter-name">borderCrossingWarningListenerGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-borderCrossingWarningListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">borderCrossingWarningListenerSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-bordercrossingwarninglistener-class">BorderCrossingWarningListener</a>?</span></span>), </span><span id="sdk-for-flutter-navigate-param-borderCrossingWarningOptionsGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-bordercrossingwarningoptions-class">BorderCrossingWarningOptions</a></span> <span class="parameter-name">borderCrossingWarningOptionsGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-borderCrossingWarningOptionsSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">borderCrossingWarningOptionsSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-bordercrossingwarningoptions-class">BorderCrossingWarningOptions</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-tollStopWarningListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-tollstopwarninglistener-class">TollStopWarningListener</a>?</span> <span class="parameter-name">tollStopWarningListenerGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-tollStopWarningListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">tollStopWarningListenerSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-tollstopwarninglistener-class">TollStopWarningListener</a>?</span></span>), </span><span id="sdk-for-flutter-navigate-param-railwayCrossingWarningListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-class">RailwayCrossingWarningListener</a>?</span> <span class="parameter-name">railwayCrossingWarningListenerGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-railwayCrossingWarningListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">railwayCrossingWarningListenerSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-class">RailwayCrossingWarningListener</a>?</span></span>), </span><span id="sdk-for-flutter-navigate-param-lowSpeedZoneWarningListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-lowspeedzonewarninglistener-class">LowSpeedZoneWarningListener</a>?</span> <span class="parameter-name">lowSpeedZoneWarningListenerGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-lowSpeedZoneWarningListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">lowSpeedZoneWarningListenerSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-lowspeedzonewarninglistener-class">LowSpeedZoneWarningListener</a>?</span></span>), </span><span id="sdk-for-flutter-navigate-param-trafficMergeWarningListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-class">TrafficMergeWarningListener</a>?</span> <span class="parameter-name">trafficMergeWarningListenerGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-trafficMergeWarningListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">trafficMergeWarningListenerSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-class">TrafficMergeWarningListener</a>?</span></span>), </span><span id="sdk-for-flutter-navigate-param-trafficMergeWarningOptionsGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-trafficmergewarningoptions-class">TrafficMergeWarningOptions</a></span> <span class="parameter-name">trafficMergeWarningOptionsGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-trafficMergeWarningOptionsSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">trafficMergeWarningOptionsSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-trafficmergewarningoptions-class">TrafficMergeWarningOptions</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-offRoadDestinationReachedListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-offroaddestinationreachedlistener-class">OffRoadDestinationReachedListener</a>?</span> <span class="parameter-name">offRoadDestinationReachedListenerGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-offRoadDestinationReachedListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">offRoadDestinationReachedListenerSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-offroaddestinationreachedlistener-class">OffRoadDestinationReachedListener</a>?</span></span>), </span><span id="sdk-for-flutter-navigate-param-offRoadProgressListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-offroadprogresslistener-class">OffRoadProgressListener</a>?</span> <span class="parameter-name">offRoadProgressListenerGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-offRoadProgressListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">offRoadProgressListenerSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-offroadprogresslistener-class">OffRoadProgressListener</a>?</span></span>), </span><span id="sdk-for-flutter-navigate-param-maneuverNotificationOptionsGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-class">ManeuverNotificationOptions</a></span> <span class="parameter-name">maneuverNotificationOptionsGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-maneuverNotificationOptionsSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">maneuverNotificationOptionsSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-class">ManeuverNotificationOptions</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-eventTextOptionsGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-eventtextoptions-class">EventTextOptions</a></span> <span class="parameter-name">eventTextOptionsGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-eventTextOptionsSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">eventTextOptionsSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-eventtextoptions-class">EventTextOptions</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-speedWarningOptionsGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-speedwarningoptions-class">SpeedWarningOptions</a></span> <span class="parameter-name">speedWarningOptionsGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-speedWarningOptionsSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">speedWarningOptionsSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-speedwarningoptions-class">SpeedWarningOptions</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-isEnableTunnelExtrapolationGetLambda" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isEnableTunnelExtrapolationGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-isEnableTunnelExtrapolationSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">isEnableTunnelExtrapolationSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">bool</span></span>), </span><span id="sdk-for-flutter-navigate-param-isPassthroughWaypointsHandlingEnabledGetLambda" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isPassthroughWaypointsHandlingEnabledGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-isPassthroughWaypointsHandlingEnabledSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">isPassthroughWaypointsHandlingEnabledSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">bool</span></span>), </span><span id="sdk-for-flutter-navigate-param-trafficOnRouteGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-trafficonroute-class">TrafficOnRoute</a>?</span> <span class="parameter-name">trafficOnRouteGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-trafficOnRouteSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">trafficOnRouteSetLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-trafficonroute-class">TrafficOnRoute</a>?</span></span>), </span><span id="sdk-for-flutter-navigate-param-locationManagerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapmatcher-locationmanager-class">LocationManager</a></span> <span class="parameter-name">locationManagerGetLambda</span>()</span>)</span>  
This abstract class provides the basic functionality needed to run a navigation session.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-bordercrossingwarninglistener">borderCrossingWarningListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-bordercrossingwarninglistener-class">BorderCrossingWarningListener</a>?</span>  
Object to receive notifications about border crossings on the current road. Border crossing notifications are given only if a route is present. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive notifications about border crossings on the current road.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-bordercrossingwarningoptions">borderCrossingWarningOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-bordercrossingwarningoptions-class">BorderCrossingWarningOptions</a></span>  
Border crossing warning options to be passed to <a href="sdk-for-flutter-navigate-navigation-bordercrossingwarninglistener-class">BorderCrossingWarningListener</a>. These options allow the filtering of the border crossing warnings received and set the notification distances. Gets border crossing warning options to be passed to <a href="sdk-for-flutter-navigate-navigation-bordercrossingwarninglistener-class">BorderCrossingWarningListener</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-currentsituationlaneassistanceviewlistener">currentSituationLaneAssistanceViewListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-class">CurrentSituationLaneAssistanceViewListener</a>?</span>  
Object to receive current situation lane assistance view notifications. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive current situation lane assistance view notifications.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-dangerzonewarninglistener">dangerZoneWarningListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-dangerzonewarninglistener-class">DangerZoneWarningListener</a>?</span>  
Object to receive notification on approaching danger zones. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive current danger zones notifications.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-destinationreachedlistener">destinationReachedListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-destinationreachedlistener-class">DestinationReachedListener</a>?</span>  
Object to receive the notification about the arrival at the destination. Destination reached notifications only occurs if a route has been set. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener that notify when the destination has been reached.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-environmentalzonewarninglistener">environmentalZoneWarningListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-environmentalzonewarninglistener-class">EnvironmentalZoneWarningListener</a>?</span>  
Object to receive notification on approaching environmental zones. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive current environmental zones notifications.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-eventtextlistener">eventTextListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-eventtextlistener-class">EventTextListener</a>?</span>  
Object to receive text notifications when they are available. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. **Note:** In order to receive the text notification emitted for the traffic merge warner, when `TrafficMergeWarningOptions.enable_text_notification` has been enabled, the `sdk.navigation.EventTextListener` must be enabled as well. Gets the listener that notifies when a text notification is available.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-eventtextoptions">eventTextOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-eventtextoptions-class">EventTextOptions</a></span>  
Options used for text notifications. Notifications are only available if a route is present. Gets the text notification options.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-locationlistener-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-isenabletunnelextrapolation">isEnableTunnelExtrapolation</a></span> <span class="signature">↔ bool</span>  
Defines whether to enable or disable tunnel extrapolation. By default the tunnel extrapolation is enabled. Return `true` if tunnel extrapolation is enabled otherwise `false`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-ispassthroughwaypointshandlingenabled">isPassthroughWaypointsHandlingEnabled</a></span> <span class="signature">↔ bool</span>  
Defines whether to enable or disable handling of passthrough waypoints. By default the handling of passthrough waypoints is disabled. Return `true` if handling of passthrough waypoints is enabled, otherwise - `false`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-junctionviewlaneassistancelistener">junctionViewLaneAssistanceListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-junctionviewlaneassistancelistener-class">JunctionViewLaneAssistanceListener</a>?</span>  
Object to receive junction view lane assistance notifications. Junction view lane assistance notifications only occurs if a route has been set. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive junction view lane assistance notifications.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-locationmanager">locationManager</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-mapmatcher-locationmanager-class">LocationManager</a></span>  
The location manager used by the navigator for map-matched location processing. Gets the location manager instance used by the navigator.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-lowspeedzonewarninglistener">lowSpeedZoneWarningListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-lowspeedzonewarninglistener-class">LowSpeedZoneWarningListener</a>?</span>  
Object to receive notifications about low speed zones on the current road. Low speed zone notifications are given regardless if a route is set. This listener is currently available *only* for Japan. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive notifications about low speed zones on the current road.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-maneuvernotificationoptions">maneuverNotificationOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-class">ManeuverNotificationOptions</a></span>  
Options used for maneuver notifications. Notifications are only available if a route is present. Gets the maneuver notification options.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-maneuverviewlaneassistancelistener">maneuverViewLaneAssistanceListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-maneuverviewlaneassistancelistener-class">ManeuverViewLaneAssistanceListener</a>?</span>  
Object to receive maneuver view lane assistance notifications. Maneuver view lane assistance notifications only occurs if a route has been set. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive maneuver view lane assistance notifications.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-milestonestatuslistener">milestoneStatusListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-milestonestatuslistener-class">MilestoneStatusListener</a>?</span>  
Object to receive notifications about the arrival at each <a href="sdk-for-flutter-navigate-navigation-milestone-class">Milestone</a> or missing it. It informs on all waypoints (passed or missed) that are of type <a href="sdk-for-flutter-navigate-navigation-milestonetype">MilestoneType.stopover</a> but excludes the starting waypoint. Waypoints of type <a href="sdk-for-flutter-navigate-navigation-milestonetype">MilestoneType.passthrough</a> are excluded, by default, but can be included via <a href="sdk-for-flutter-navigate-navigation-navigatorinterface-ispassthroughwaypointshandlingenabled">NavigatorInterface.isPassthroughWaypointsHandlingEnabled</a>. Milestone status notifications only occurs if a route has been set. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener that notifies when a <a href="sdk-for-flutter-navigate-navigation-milestone-class">Milestone</a> has been reached or missed.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-navigablelocationlistener">navigableLocationListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-navigablelocationlistener-class">NavigableLocationListener</a>?</span>  
Object to receive notifications about the current location. It returns `null` when no listener is set by an user. Gets the listener that notifies current location updates.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-offroaddestinationreachedlistener">offRoadDestinationReachedListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-offroaddestinationreachedlistener-class">OffRoadDestinationReachedListener</a>?</span>  
Object to receive the notification about the arrival at the off-road destination. Off-road destination reached notifications only occurs if a route has been set. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener that notifies when the off-road destination has been reached.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-offroadprogresslistener">offRoadProgressListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-offroadprogresslistener-class">OffRoadProgressListener</a>?</span>  
Object to receive the notification about the off-road progress. Off-road progress notifications only occurs if a route has been set. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener that notifies about off-road progress.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-postactionlistener">postActionListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-postactionlistener-class">PostActionListener</a>?</span>  
Object to receive post action notifications, such as a charge action at a charging station. Post actions notifications only occurs if a route has been set. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive post action notifications, such as a charge action at a charging station.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-railwaycrossingwarninglistener">railwayCrossingWarningListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-class">RailwayCrossingWarningListener</a>?</span>  
Object to receive notifications about railway crossings on the current road. Railway crossing notifications are given regardless if a route is set. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive notifications about railway crossings on the current road.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-realisticviewwarninglistener">realisticViewWarningListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-class">RealisticViewWarningListener</a>?</span>  
Object to receive notifications about junction views on the current road. Setting `null` value to the listener will unset the listener. This feature requires a map version greater or equal to 67 in order to function properly. It returns `null` when no listener is set by an user. Gets the listener to receive notifications about junction views on the current road.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-realisticviewwarningoptions">realisticViewWarningOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-realisticviewwarningoptions-class">RealisticViewWarningOptions</a></span>  
Realistic view warning options. It allow to filter realistic views to be passed to <a href="sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-class">RealisticViewWarningListener</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-roadattributeslistener">roadAttributesListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-roadattributeslistener-class">RoadAttributesListener</a>?</span>  
Object to receive notifications about attributes of the current road. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive notifications about attributes of the current road.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-roadsignwarninglistener">roadSignWarningListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-roadsignwarninglistener-class">RoadSignWarningListener</a>?</span>  
Object to receive notifications about road signs on the current road. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive notifications about road signs on the current road.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-roadsignwarningoptions">roadSignWarningOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-roadsignwarningoptions-class">RoadSignWarningOptions</a></span>  
Road sign warning options that allow to filter road sings to be passed to <a href="sdk-for-flutter-navigate-navigation-roadsignwarninglistener-class">RoadSignWarningListener</a>. Gets road sign warning options that allow to filter road signs to be passed to <a href="sdk-for-flutter-navigate-navigation-roadsignwarninglistener-class">RoadSignWarningListener</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-roadtextslistener">roadTextsListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-roadtextslistener-class">RoadTextsListener</a>?</span>  
Object to receive notifications about the textual attributes of the current road. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive notifications about the textual attributes of the current road.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-route">route</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-route-class">Route</a>?</span>  
The route to navigate. Gets and sets the route that is being navigated. If not set, only the current location information will be provided through <a href="sdk-for-flutter-navigate-navigation-navigablelocationlistener-class">NavigableLocationListener</a>. If set, both route progress (<a href="sdk-for-flutter-navigate-navigation-routeprogresslistener-class">RouteProgressListener</a>) and route deviation (<a href="sdk-for-flutter-navigate-navigation-routedeviationlistener-class">RouteDeviationListener</a>) will receive notifications on updates. A route may fail to be set if it is generated by an incompatible engine, in which case the operation has no effect. Gets the route that is being navigated.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-routedeviationlistener">routeDeviationListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-routedeviationlistener-class">RouteDeviationListener</a>?</span>  
Object to receive notifications about deviations from the route if any occurs. Route deviation notifications only occurs if a route has been set. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener that notifies when deviation from the route is observed.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-routeprogresslistener">routeProgressListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-routeprogresslistener-class">RouteProgressListener</a>?</span>  
Object to receive notifications about navigation route progress. Route progress notifications only occurs if the route has been set. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener that notifies when a route progress change occurs.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-locationlistener-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-safetycamerawarninglistener">safetyCameraWarningListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-class">SafetyCameraWarningListener</a>?</span>  
Object to receive safety camera warner notifications. If a listener is present, notifications about safety speed cameras will be also sent via <a href="sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-class">SafetyCameraWarningListener</a>. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive safety camera warning notifications.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-safetycamerawarningoptions">safetyCameraWarningOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-safetycamerawarningoptions-class">SafetyCameraWarningOptions</a></span>  
Safety camera warning options to be passed to <a href="sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-class">SafetyCameraWarningListener</a>. These options allow the enabling or disabling the text notification for the warner. Gets safety camera warning options to be passed to <a href="sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-class">SafetyCameraWarningListener</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-schoolzonewarninglistener">schoolZoneWarningListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-schoolzonewarninglistener-class">SchoolZoneWarningListener</a>?</span>  
Object to receive notifications about school zones on the current road. Setting `null` value to the listener will unset the listener. school zones on the current road. It returns `null` when no listener is set by an user. Gets the listener to receive notifications about school zones on the current road.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-schoolzonewarningoptions">schoolZoneWarningOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-schoolzonewarningoptions-class">SchoolZoneWarningOptions</a></span>  
School zone warning options It allow to configure school zone notifications to be passed to <a href="sdk-for-flutter-navigate-navigation-schoolzonewarninglistener-class">SchoolZoneWarningListener</a>. Gets school zone warning options that allow to configure school zone notifications to be passed to <a href="sdk-for-flutter-navigate-navigation-schoolzonewarninglistener-class">SchoolZoneWarningListener</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-speedlimitlistener">speedLimitListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-speedlimitlistener-class">SpeedLimitListener</a>?</span>  
Object to receive notifications about the speed limit of the current road. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive notifications about the speed limit of the current road.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-speedwarninglistener">speedWarningListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-speedwarninglistener-class">SpeedWarningListener</a>?</span>  
Object to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-speedwarningoptions">speedWarningOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-speedwarningoptions-class">SpeedWarningOptions</a></span>  
Options used for the speed warning feature. Gets the speed warning options.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-tollstopwarninglistener">tollStopWarningListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-tollstopwarninglistener-class">TollStopWarningListener</a>?</span>  
Object to receive information on the upcoming toll stop. Setting `null` value to the listener will unset the listener. This is a **beta release** of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process. Gets the listener to receive notifications about the the upcoming toll stop.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-trackingtransportprofile" class="deprecated">trackingTransportProfile</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-transportprofile-class" class="deprecated">TransportProfile</a>?</span>  
Defines the transport profile for the <a href="sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>, when no route is present. Properly setting the transport profile optimizes the navigation experience, and improves resource consumption. For example, a <a href="sdk-for-flutter-navigate-core-transportprofile-class" class="deprecated">TransportProfile</a> can be defined with a <a href="sdk-for-flutter-navigate-transport-vehicleprofile-class" class="deprecated">VehicleProfile</a>. A vehicle profile can have several parameters such as <a href="sdk-for-flutter-navigate-transport-vehicletype" class="deprecated">VehicleType</a> to set the source of information describing the vehicle. The default is a <a href="sdk-for-flutter-navigate-transport-vehicletype">VehicleType.car</a> profile.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-trackingtransportspecification">trackingTransportSpecification</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a>?</span>  
Defines the transport specification for the <a href="sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>, when no route is present. Properly setting the transport specification optimizes the navigation experience, and improves resource consumption. An <a href="sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a> must have the <a href="sdk-for-flutter-navigate-transport-transportspecification-transportmode">TransportSpecification.transportMode</a> set. A transport specification can have several parameters defined such as <a href="sdk-for-flutter-navigate-transport-vehiclespecification-lengthincentimeters">VehicleSpecification.lengthInCentimeters</a> defined in <a href="sdk-for-flutter-navigate-transport-transportspecification-vehiclespecification">TransportSpecification.vehicleSpecification</a> to set the source of information describing the vehicle. By default the <a href="sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a> will have the transport mode set to <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.car</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-trafficmergewarninglistener">trafficMergeWarningListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-class">TrafficMergeWarningListener</a>?</span>  
Object to receive notifications about merging traffic to the current road. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive notifications about merging traffic to the current road.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-trafficmergewarningoptions">trafficMergeWarningOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-trafficmergewarningoptions-class">TrafficMergeWarningOptions</a></span>  
Merging traffic warning options that allow to configure merging traffic notifications to be passed to <a href="sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-class">TrafficMergeWarningListener</a>. Gets merging traffic warning options that allow to configure merging traffic notifications to be passed to <a href="sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-class">TrafficMergeWarningListener</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-trafficonroute">trafficOnRoute</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-trafficonroute-class">TrafficOnRoute</a>?</span>  
Traffic information for the current route. This impacts `RouteProgress` updates as the duration of the `SectionProgress` might change. However, the remaining distance and the route geometry will remain unchanged. Gets the traffic information for the current route.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-truckrestrictionswarninglistener">truckRestrictionsWarningListener</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-truckrestrictionswarninglistener-class">TruckRestrictionsWarningListener</a>?</span>  
Object to receive notifications about truck restrictions on the current road. Setting `null` value to the listener will unset the listener. It returns `null` when no listener is set by an user. Gets the listener to receive notifications about truck restrictions on the current road.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-truckrestrictionswarningoptions">truckRestrictionsWarningOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-truckrestrictionswarningoptions-class">TruckRestrictionsWarningOptions</a></span>  
Truck restrictions warning options that allow to filter truck restrictions to be passed to <a href="sdk-for-flutter-navigate-navigation-truckrestrictionswarninglistener-class">TruckRestrictionsWarningListener</a>. Gets truck restrictions warning options that allow to filter truck restrictions to be passed to <a href="sdk-for-flutter-navigate-navigation-truckrestrictionswarninglistener-class">TruckRestrictionsWarningListener</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-warnerengine">warnerEngine</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-warner-warnerengine-class">WarnerEngine</a></span>  
Warner engine used by the navigator. This engine can be used to configure navigation warnings. Gets the warner engine used by the navigator.

<div class="features">

<span class="feature">no setter</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-calculateremainingdistanceinmeters">calculateRemainingDistanceInMeters</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-calculateRemainingDistanceInMeters-param-coordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">coordinates</span></span>) <span class="returntype parameter">→ int?</span> </span>  
This method calculates the distance between the current position and given coordinates.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-getmaneuver">getManeuver</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getManeuver-param-index" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">index</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-routing-maneuver-class">Maneuver</a>?</span> </span>  
Returns maneuver at the given index.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-getmaneuvernotificationtimingoptionswithtimingprofile">getManeuverNotificationTimingOptionsWithTimingProfile</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getManeuverNotificationTimingOptionsWithTimingProfile-param-transportMode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode</a></span> <span class="parameter-name">transportMode</span>, </span><span id="sdk-for-flutter-navigate-getManeuverNotificationTimingOptionsWithTimingProfile-param-timingProfile" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile</a></span> <span class="parameter-name">timingProfile</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-class">ManeuverNotificationTimingOptions</a></span> </span>  
Returns maneuver notification timing options with default values given the combination of transport mode and timing profile.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-getwarningnotificationdistances">getWarningNotificationDistances</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getWarningNotificationDistances-param-warningType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType</a></span> <span class="parameter-name">warningType</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-navigation-warningnotificationdistances-class">WarningNotificationDistances</a></span> </span>  
Returns the warning notification distances for the requested warning type.

<span class="name"><a href="sdk-for-flutter-navigate-core-locationlistener-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-locationlistener-onlocationupdated">onLocationUpdated</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-onLocationUpdated-param-location" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-location-class">Location</a></span> <span class="parameter-name">location</span></span>) <span class="returntype parameter">→ void</span> </span>  
Called each time a new location is available.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-repeatlastmaneuvernotification">repeatLastManeuverNotification</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Call of this function is used to trigger the navigator to repeat the last maneuver notification based on the current position.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-setcustomoption">setCustomOption</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setCustomOption-param-key" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">key</span>, </span><span id="sdk-for-flutter-navigate-setCustomOption-param-value" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">value</span></span>) <span class="returntype parameter">→ void</span> </span>  
This method sets custom options that controls navigator behavior.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-setmaneuvernotificationtimingoptionswithtimingprofile">setManeuverNotificationTimingOptionsWithTimingProfile</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setManeuverNotificationTimingOptionsWithTimingProfile-param-transportMode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode</a></span> <span class="parameter-name">transportMode</span>, </span><span id="sdk-for-flutter-navigate-setManeuverNotificationTimingOptionsWithTimingProfile-param-timingProfile" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile</a></span> <span class="parameter-name">timingProfile</span>, </span><span id="sdk-for-flutter-navigate-setManeuverNotificationTimingOptionsWithTimingProfile-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-class">ManeuverNotificationTimingOptions</a></span> <span class="parameter-name">options</span></span>) <span class="returntype parameter">→ bool</span> </span>  
Set timing option values for the combination of transport mode and timing profile.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-setwarningnotificationdistances">setWarningNotificationDistances</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setWarningNotificationDistances-param-warningType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType</a></span> <span class="parameter-name">warningType</span>, </span><span id="sdk-for-flutter-navigate-setWarningNotificationDistances-param-warningNotificationDistances" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-warningnotificationdistances-class">WarningNotificationDistances</a></span> <span class="parameter-name">warningNotificationDistances</span></span>) <span class="returntype parameter">→ bool</span> </span>  
Set the warning notification distances for the specified warning types.

<span class="name"><a href="sdk-for-flutter-navigate-core-locationlistener-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-core-locationlistener-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

