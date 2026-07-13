---
title: "NavigatorInterface constructor - NavigatorInterface - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-navigatorinterface"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/NavigatorInterface-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">NavigatorInterface</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">NavigatorInterface</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onLocationUpdatedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onLocationUpdatedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-location-class">Location</a></span></span>

    ), </span>
2.  <span id="sdk-for-flutter-navigate-param-getManeuverLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-maneuver-class">Maneuver</a>?</span> <span class="parameter-name">getManeuverLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">int</span></span>

    ), </span>
3.  <span id="sdk-for-flutter-navigate-param-getManeuverNotificationTimingOptionsWithTimingProfileLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-class">ManeuverNotificationTimingOptions</a></span> <span class="parameter-name">getManeuverNotificationTimingOptionsWithTimingProfileLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode</a></span>, </span>
    2.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile</a></span></span>

    ), </span>
4.  <span id="sdk-for-flutter-navigate-param-setManeuverNotificationTimingOptionsWithTimingProfileLambda" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">setManeuverNotificationTimingOptionsWithTimingProfileLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode</a></span>, </span>
    2.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile</a></span>, </span>
    3.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-class">ManeuverNotificationTimingOptions</a></span></span>

    ), </span>
5.  <span id="sdk-for-flutter-navigate-param-getWarningNotificationDistancesLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-warningnotificationdistances-class">WarningNotificationDistances</a></span> <span class="parameter-name">getWarningNotificationDistancesLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType</a></span></span>

    ), </span>
6.  <span id="sdk-for-flutter-navigate-param-setWarningNotificationDistancesLambda" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">setWarningNotificationDistancesLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType</a></span>, </span>
    2.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-warningnotificationdistances-class">WarningNotificationDistances</a></span></span>

    ), </span>
7.  <span id="sdk-for-flutter-navigate-param-repeatLastManeuverNotificationLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">repeatLastManeuverNotificationLambda</span>(), </span>
8.  <span id="sdk-for-flutter-navigate-param-calculateRemainingDistanceInMetersLambda" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">calculateRemainingDistanceInMetersLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span></span>

    ), </span>
9.  <span id="sdk-for-flutter-navigate-param-setCustomOptionLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">setCustomOptionLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">String</span>, </span>
    2.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">String</span></span>

    ), </span>
10. <span id="sdk-for-flutter-navigate-param-routeGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-route-class">Route</a>?</span> <span class="parameter-name">routeGetLambda</span>(), </span>
11. <span id="sdk-for-flutter-navigate-param-routeSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">routeSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-route-class">Route</a>?</span></span>

    ), </span>
12. <span id="sdk-for-flutter-navigate-param-trackingTransportProfileGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-transportprofile-class" class="deprecated">TransportProfile</a>?</span> <span class="parameter-name">trackingTransportProfileGetLambda</span>(), </span>
13. <span id="sdk-for-flutter-navigate-param-trackingTransportProfileSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">trackingTransportProfileSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-transportprofile-class" class="deprecated">TransportProfile</a>?</span></span>

    ), </span>
14. <span id="sdk-for-flutter-navigate-param-trackingTransportSpecificationGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a>?</span> <span class="parameter-name">trackingTransportSpecificationGetLambda</span>(), </span>
15. <span id="sdk-for-flutter-navigate-param-trackingTransportSpecificationSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">trackingTransportSpecificationSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a>?</span></span>

    ), </span>
16. <span id="sdk-for-flutter-navigate-param-navigableLocationListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-navigablelocationlistener-class">NavigableLocationListener</a>?</span> <span class="parameter-name">navigableLocationListenerGetLambda</span>(), </span>
17. <span id="sdk-for-flutter-navigate-param-navigableLocationListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">navigableLocationListenerSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-navigablelocationlistener-class">NavigableLocationListener</a>?</span></span>

    ), </span>
18. <span id="sdk-for-flutter-navigate-param-routeProgressListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-routeprogresslistener-class">RouteProgressListener</a>?</span> <span class="parameter-name">routeProgressListenerGetLambda</span>(), </span>
19. <span id="sdk-for-flutter-navigate-param-routeProgressListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">routeProgressListenerSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-routeprogresslistener-class">RouteProgressListener</a>?</span></span>

    ), </span>
20. <span id="sdk-for-flutter-navigate-param-routeDeviationListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-routedeviationlistener-class">RouteDeviationListener</a>?</span> <span class="parameter-name">routeDeviationListenerGetLambda</span>(), </span>
21. <span id="sdk-for-flutter-navigate-param-routeDeviationListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">routeDeviationListenerSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-routedeviationlistener-class">RouteDeviationListener</a>?</span></span>

    ), </span>
22. <span id="sdk-for-flutter-navigate-param-eventTextListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-eventtextlistener-class">EventTextListener</a>?</span> <span class="parameter-name">eventTextListenerGetLambda</span>(), </span>
23. <span id="sdk-for-flutter-navigate-param-eventTextListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">eventTextListenerSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-eventtextlistener-class">EventTextListener</a>?</span></span>

    ), </span>
24. <span id="sdk-for-flutter-navigate-param-milestoneStatusListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-milestonestatuslistener-class">MilestoneStatusListener</a>?</span> <span class="parameter-name">milestoneStatusListenerGetLambda</span>(), </span>
25. <span id="sdk-for-flutter-navigate-param-milestoneStatusListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">milestoneStatusListenerSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-milestonestatuslistener-class">MilestoneStatusListener</a>?</span></span>

    ), </span>
26. <span id="sdk-for-flutter-navigate-param-destinationReachedListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-destinationreachedlistener-class">DestinationReachedListener</a>?</span> <span class="parameter-name">destinationReachedListenerGetLambda</span>(), </span>
27. <span id="sdk-for-flutter-navigate-param-destinationReachedListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">destinationReachedListenerSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-destinationreachedlistener-class">DestinationReachedListener</a>?</span></span>

    ), </span>
28. <span id="sdk-for-flutter-navigate-param-speedWarningListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-speedwarninglistener-class">SpeedWarningListener</a>?</span> <span class="parameter-name">speedWarningListenerGetLambda</span>(), </span>
29. <span id="sdk-for-flutter-navigate-param-speedWarningListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">speedWarningListenerSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-speedwarninglistener-class">SpeedWarningListener</a>?</span></span>

    ), </span>
30. <span id="sdk-for-flutter-navigate-param-maneuverViewLaneAssistanceListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-maneuverviewlaneassistancelistener-class">ManeuverViewLaneAssistanceListener</a>?</span> <span class="parameter-name">maneuverViewLaneAssistanceListenerGetLambda</span>(), </span>
31. <span id="sdk-for-flutter-navigate-param-maneuverViewLaneAssistanceListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">maneuverViewLaneAssistanceListenerSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-maneuverviewlaneassistancelistener-class">ManeuverViewLaneAssistanceListener</a>?</span></span>

    ), </span>
32. <span id="sdk-for-flutter-navigate-param-currentSituationLaneAssistanceViewListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-class">CurrentSituationLaneAssistanceViewListener</a>?</span> <span class="parameter-name">currentSituationLaneAssistanceViewListenerGetLambda</span>(), </span>
33. <span id="sdk-for-flutter-navigate-param-currentSituationLaneAssistanceViewListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">currentSituationLaneAssistanceViewListenerSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-class">CurrentSituationLaneAssistanceViewListener</a>?</span></span>

    ), </span>
34. <span id="sdk-for-flutter-navigate-param-environmentalZoneWarningListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-environmentalzonewarninglistener-class">EnvironmentalZoneWarningListener</a>?</span> <span class="parameter-name">environmentalZoneWarningListenerGetLambda</span>(), </span>
35. <span id="sdk-for-flutter-navigate-param-environmentalZoneWarningListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">environmentalZoneWarningListenerSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-environmentalzonewarninglistener-class">EnvironmentalZoneWarningListener</a>?</span></span>

    ), </span>
36. <span id="sdk-for-flutter-navigate-param-junctionViewLaneAssistanceListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-junctionviewlaneassistancelistener-class">JunctionViewLaneAssistanceListener</a>?</span> <span class="parameter-name">junctionViewLaneAssistanceListenerGetLambda</span>(), </span>
37. <span id="sdk-for-flutter-navigate-param-junctionViewLaneAssistanceListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">junctionViewLaneAssistanceListenerSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-junctionviewlaneassistancelistener-class">JunctionViewLaneAssistanceListener</a>?</span></span>

    ), </span>
38. <span id="sdk-for-flutter-navigate-param-safetyCameraWarningListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-class">SafetyCameraWarningListener</a>?</span> <span class="parameter-name">safetyCameraWarningListenerGetLambda</span>(), </span>
39. <span id="sdk-for-flutter-navigate-param-safetyCameraWarningListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">safetyCameraWarningListenerSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-class">SafetyCameraWarningListener</a>?</span></span>

    ), </span>
40. <span id="sdk-for-flutter-navigate-param-safetyCameraWarningOptionsGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-safetycamerawarningoptions-class">SafetyCameraWarningOptions</a></span> <span class="parameter-name">safetyCameraWarningOptionsGetLambda</span>(), </span>
41. <span id="sdk-for-flutter-navigate-param-safetyCameraWarningOptionsSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">safetyCameraWarningOptionsSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-safetycamerawarningoptions-class">SafetyCameraWarningOptions</a></span></span>

    ), </span>
42. <span id="sdk-for-flutter-navigate-param-dangerZoneWarningListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-dangerzonewarninglistener-class">DangerZoneWarningListener</a>?</span> <span class="parameter-name">dangerZoneWarningListenerGetLambda</span>(), </span>
43. <span id="sdk-for-flutter-navigate-param-dangerZoneWarningListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">dangerZoneWarningListenerSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-dangerzonewarninglistener-class">DangerZoneWarningListener</a>?</span></span>

    ), </span>
44. <span id="sdk-for-flutter-navigate-param-truckRestrictionsWarningListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-truckrestrictionswarninglistener-class">TruckRestrictionsWarningListener</a>?</span> <span class="parameter-name">truckRestrictionsWarningListenerGetLambda</span>(), </span>
45. <span id="sdk-for-flutter-navigate-param-truckRestrictionsWarningListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">truckRestrictionsWarningListenerSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-truckrestrictionswarninglistener-class">TruckRestrictionsWarningListener</a>?</span></span>

    ), </span>
46. <span id="sdk-for-flutter-navigate-param-warnerEngineGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-warner-warnerengine-class">WarnerEngine</a></span> <span class="parameter-name">warnerEngineGetLambda</span>(), </span>
47. <span id="sdk-for-flutter-navigate-param-truckRestrictionsWarningOptionsGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-truckrestrictionswarningoptions-class">TruckRestrictionsWarningOptions</a></span> <span class="parameter-name">truckRestrictionsWarningOptionsGetLambda</span>(), </span>
48. <span id="sdk-for-flutter-navigate-param-truckRestrictionsWarningOptionsSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">truckRestrictionsWarningOptionsSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-truckrestrictionswarningoptions-class">TruckRestrictionsWarningOptions</a></span></span>

    ), </span>
49. <span id="sdk-for-flutter-navigate-param-postActionListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-postactionlistener-class">PostActionListener</a>?</span> <span class="parameter-name">postActionListenerGetLambda</span>(), </span>
50. <span id="sdk-for-flutter-navigate-param-postActionListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">postActionListenerSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-postactionlistener-class">PostActionListener</a>?</span></span>

    ), </span>
51. <span id="sdk-for-flutter-navigate-param-speedLimitListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-speedlimitlistener-class">SpeedLimitListener</a>?</span> <span class="parameter-name">speedLimitListenerGetLambda</span>(), </span>
52. <span id="sdk-for-flutter-navigate-param-speedLimitListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">speedLimitListenerSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-speedlimitlistener-class">SpeedLimitListener</a>?</span></span>

    ), </span>
53. <span id="sdk-for-flutter-navigate-param-roadTextsListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-roadtextslistener-class">RoadTextsListener</a>?</span> <span class="parameter-name">roadTextsListenerGetLambda</span>(), </span>
54. <span id="sdk-for-flutter-navigate-param-roadTextsListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">roadTextsListenerSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-roadtextslistener-class">RoadTextsListener</a>?</span></span>

    ), </span>
55. <span id="sdk-for-flutter-navigate-param-roadAttributesListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-roadattributeslistener-class">RoadAttributesListener</a>?</span> <span class="parameter-name">roadAttributesListenerGetLambda</span>(), </span>
56. <span id="sdk-for-flutter-navigate-param-roadAttributesListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">roadAttributesListenerSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-roadattributeslistener-class">RoadAttributesListener</a>?</span></span>

    ), </span>
57. <span id="sdk-for-flutter-navigate-param-roadSignWarningListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-roadsignwarninglistener-class">RoadSignWarningListener</a>?</span> <span class="parameter-name">roadSignWarningListenerGetLambda</span>(), </span>
58. <span id="sdk-for-flutter-navigate-param-roadSignWarningListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">roadSignWarningListenerSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-roadsignwarninglistener-class">RoadSignWarningListener</a>?</span></span>

    ), </span>
59. <span id="sdk-for-flutter-navigate-param-roadSignWarningOptionsGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-roadsignwarningoptions-class">RoadSignWarningOptions</a></span> <span class="parameter-name">roadSignWarningOptionsGetLambda</span>(), </span>
60. <span id="sdk-for-flutter-navigate-param-roadSignWarningOptionsSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">roadSignWarningOptionsSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-roadsignwarningoptions-class">RoadSignWarningOptions</a></span></span>

    ), </span>
61. <span id="sdk-for-flutter-navigate-param-schoolZoneWarningListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-schoolzonewarninglistener-class">SchoolZoneWarningListener</a>?</span> <span class="parameter-name">schoolZoneWarningListenerGetLambda</span>(), </span>
62. <span id="sdk-for-flutter-navigate-param-schoolZoneWarningListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">schoolZoneWarningListenerSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-schoolzonewarninglistener-class">SchoolZoneWarningListener</a>?</span></span>

    ), </span>
63. <span id="sdk-for-flutter-navigate-param-schoolZoneWarningOptionsGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-schoolzonewarningoptions-class">SchoolZoneWarningOptions</a></span> <span class="parameter-name">schoolZoneWarningOptionsGetLambda</span>(), </span>
64. <span id="sdk-for-flutter-navigate-param-schoolZoneWarningOptionsSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">schoolZoneWarningOptionsSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-schoolzonewarningoptions-class">SchoolZoneWarningOptions</a></span></span>

    ), </span>
65. <span id="sdk-for-flutter-navigate-param-realisticViewWarningListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-class">RealisticViewWarningListener</a>?</span> <span class="parameter-name">realisticViewWarningListenerGetLambda</span>(), </span>
66. <span id="sdk-for-flutter-navigate-param-realisticViewWarningListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">realisticViewWarningListenerSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-class">RealisticViewWarningListener</a>?</span></span>

    ), </span>
67. <span id="sdk-for-flutter-navigate-param-realisticViewWarningOptionsGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-realisticviewwarningoptions-class">RealisticViewWarningOptions</a></span> <span class="parameter-name">realisticViewWarningOptionsGetLambda</span>(), </span>
68. <span id="sdk-for-flutter-navigate-param-realisticViewWarningOptionsSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">realisticViewWarningOptionsSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-realisticviewwarningoptions-class">RealisticViewWarningOptions</a></span></span>

    ), </span>
69. <span id="sdk-for-flutter-navigate-param-borderCrossingWarningListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-bordercrossingwarninglistener-class">BorderCrossingWarningListener</a>?</span> <span class="parameter-name">borderCrossingWarningListenerGetLambda</span>(), </span>
70. <span id="sdk-for-flutter-navigate-param-borderCrossingWarningListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">borderCrossingWarningListenerSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-bordercrossingwarninglistener-class">BorderCrossingWarningListener</a>?</span></span>

    ), </span>
71. <span id="sdk-for-flutter-navigate-param-borderCrossingWarningOptionsGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-bordercrossingwarningoptions-class">BorderCrossingWarningOptions</a></span> <span class="parameter-name">borderCrossingWarningOptionsGetLambda</span>(), </span>
72. <span id="sdk-for-flutter-navigate-param-borderCrossingWarningOptionsSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">borderCrossingWarningOptionsSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-bordercrossingwarningoptions-class">BorderCrossingWarningOptions</a></span></span>

    ), </span>
73. <span id="sdk-for-flutter-navigate-param-tollStopWarningListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-tollstopwarninglistener-class">TollStopWarningListener</a>?</span> <span class="parameter-name">tollStopWarningListenerGetLambda</span>(), </span>
74. <span id="sdk-for-flutter-navigate-param-tollStopWarningListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">tollStopWarningListenerSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-tollstopwarninglistener-class">TollStopWarningListener</a>?</span></span>

    ), </span>
75. <span id="sdk-for-flutter-navigate-param-railwayCrossingWarningListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-class">RailwayCrossingWarningListener</a>?</span> <span class="parameter-name">railwayCrossingWarningListenerGetLambda</span>(), </span>
76. <span id="sdk-for-flutter-navigate-param-railwayCrossingWarningListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">railwayCrossingWarningListenerSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-class">RailwayCrossingWarningListener</a>?</span></span>

    ), </span>
77. <span id="sdk-for-flutter-navigate-param-lowSpeedZoneWarningListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-lowspeedzonewarninglistener-class">LowSpeedZoneWarningListener</a>?</span> <span class="parameter-name">lowSpeedZoneWarningListenerGetLambda</span>(), </span>
78. <span id="sdk-for-flutter-navigate-param-lowSpeedZoneWarningListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">lowSpeedZoneWarningListenerSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-lowspeedzonewarninglistener-class">LowSpeedZoneWarningListener</a>?</span></span>

    ), </span>
79. <span id="sdk-for-flutter-navigate-param-trafficMergeWarningListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-class">TrafficMergeWarningListener</a>?</span> <span class="parameter-name">trafficMergeWarningListenerGetLambda</span>(), </span>
80. <span id="sdk-for-flutter-navigate-param-trafficMergeWarningListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">trafficMergeWarningListenerSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-class">TrafficMergeWarningListener</a>?</span></span>

    ), </span>
81. <span id="sdk-for-flutter-navigate-param-trafficMergeWarningOptionsGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-trafficmergewarningoptions-class">TrafficMergeWarningOptions</a></span> <span class="parameter-name">trafficMergeWarningOptionsGetLambda</span>(), </span>
82. <span id="sdk-for-flutter-navigate-param-trafficMergeWarningOptionsSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">trafficMergeWarningOptionsSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-trafficmergewarningoptions-class">TrafficMergeWarningOptions</a></span></span>

    ), </span>
83. <span id="sdk-for-flutter-navigate-param-offRoadDestinationReachedListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-offroaddestinationreachedlistener-class">OffRoadDestinationReachedListener</a>?</span> <span class="parameter-name">offRoadDestinationReachedListenerGetLambda</span>(), </span>
84. <span id="sdk-for-flutter-navigate-param-offRoadDestinationReachedListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">offRoadDestinationReachedListenerSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-offroaddestinationreachedlistener-class">OffRoadDestinationReachedListener</a>?</span></span>

    ), </span>
85. <span id="sdk-for-flutter-navigate-param-offRoadProgressListenerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-offroadprogresslistener-class">OffRoadProgressListener</a>?</span> <span class="parameter-name">offRoadProgressListenerGetLambda</span>(), </span>
86. <span id="sdk-for-flutter-navigate-param-offRoadProgressListenerSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">offRoadProgressListenerSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-offroadprogresslistener-class">OffRoadProgressListener</a>?</span></span>

    ), </span>
87. <span id="sdk-for-flutter-navigate-param-maneuverNotificationOptionsGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-class">ManeuverNotificationOptions</a></span> <span class="parameter-name">maneuverNotificationOptionsGetLambda</span>(), </span>
88. <span id="sdk-for-flutter-navigate-param-maneuverNotificationOptionsSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">maneuverNotificationOptionsSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-class">ManeuverNotificationOptions</a></span></span>

    ), </span>
89. <span id="sdk-for-flutter-navigate-param-eventTextOptionsGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-eventtextoptions-class">EventTextOptions</a></span> <span class="parameter-name">eventTextOptionsGetLambda</span>(), </span>
90. <span id="sdk-for-flutter-navigate-param-eventTextOptionsSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">eventTextOptionsSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-eventtextoptions-class">EventTextOptions</a></span></span>

    ), </span>
91. <span id="sdk-for-flutter-navigate-param-speedWarningOptionsGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-speedwarningoptions-class">SpeedWarningOptions</a></span> <span class="parameter-name">speedWarningOptionsGetLambda</span>(), </span>
92. <span id="sdk-for-flutter-navigate-param-speedWarningOptionsSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">speedWarningOptionsSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-speedwarningoptions-class">SpeedWarningOptions</a></span></span>

    ), </span>
93. <span id="sdk-for-flutter-navigate-param-isEnableTunnelExtrapolationGetLambda" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isEnableTunnelExtrapolationGetLambda</span>(), </span>
94. <span id="sdk-for-flutter-navigate-param-isEnableTunnelExtrapolationSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">isEnableTunnelExtrapolationSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">bool</span></span>

    ), </span>
95. <span id="sdk-for-flutter-navigate-param-isPassthroughWaypointsHandlingEnabledGetLambda" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isPassthroughWaypointsHandlingEnabledGetLambda</span>(), </span>
96. <span id="sdk-for-flutter-navigate-param-isPassthroughWaypointsHandlingEnabledSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">isPassthroughWaypointsHandlingEnabledSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">bool</span></span>

    ), </span>
97. <span id="sdk-for-flutter-navigate-param-trafficOnRouteGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-trafficonroute-class">TrafficOnRoute</a>?</span> <span class="parameter-name">trafficOnRouteGetLambda</span>(), </span>
98. <span id="sdk-for-flutter-navigate-param-trafficOnRouteSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">trafficOnRouteSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-trafficonroute-class">TrafficOnRoute</a>?</span></span>

    ), </span>
99. <span id="sdk-for-flutter-navigate-param-locationManagerGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapmatcher-locationmanager-class">LocationManager</a></span> <span class="parameter-name">locationManagerGetLambda</span>(), </span>

)

</div>

<div class="section desc markdown">

This abstract class provides the basic functionality needed to run a navigation session.

</div>

## Implementation

``` dart
factory NavigatorInterface(
  void Function(Location) onLocationUpdatedLambda,
  Maneuver? Function(int) getManeuverLambda,
  ManeuverNotificationTimingOptions Function(TransportMode, TimingProfile) getManeuverNotificationTimingOptionsWithTimingProfileLambda,
  bool Function(TransportMode, TimingProfile, ManeuverNotificationTimingOptions) setManeuverNotificationTimingOptionsWithTimingProfileLambda,
  WarningNotificationDistances Function(WarningType) getWarningNotificationDistancesLambda,
  bool Function(WarningType, WarningNotificationDistances) setWarningNotificationDistancesLambda,
  void Function() repeatLastManeuverNotificationLambda,
  int? Function(GeoCoordinates) calculateRemainingDistanceInMetersLambda,
  void Function(String, String) setCustomOptionLambda,
  Route? Function() routeGetLambda,
  void Function(Route?) routeSetLambda,
  TransportProfile? Function() trackingTransportProfileGetLambda,
  void Function(TransportProfile?) trackingTransportProfileSetLambda,
  TransportSpecification? Function() trackingTransportSpecificationGetLambda,
  void Function(TransportSpecification?) trackingTransportSpecificationSetLambda,
  NavigableLocationListener? Function() navigableLocationListenerGetLambda,
  void Function(NavigableLocationListener?) navigableLocationListenerSetLambda,
  RouteProgressListener? Function() routeProgressListenerGetLambda,
  void Function(RouteProgressListener?) routeProgressListenerSetLambda,
  RouteDeviationListener? Function() routeDeviationListenerGetLambda,
  void Function(RouteDeviationListener?) routeDeviationListenerSetLambda,
  EventTextListener? Function() eventTextListenerGetLambda,
  void Function(EventTextListener?) eventTextListenerSetLambda,
  MilestoneStatusListener? Function() milestoneStatusListenerGetLambda,
  void Function(MilestoneStatusListener?) milestoneStatusListenerSetLambda,
  DestinationReachedListener? Function() destinationReachedListenerGetLambda,
  void Function(DestinationReachedListener?) destinationReachedListenerSetLambda,
  SpeedWarningListener? Function() speedWarningListenerGetLambda,
  void Function(SpeedWarningListener?) speedWarningListenerSetLambda,
  ManeuverViewLaneAssistanceListener? Function() maneuverViewLaneAssistanceListenerGetLambda,
  void Function(ManeuverViewLaneAssistanceListener?) maneuverViewLaneAssistanceListenerSetLambda,
  CurrentSituationLaneAssistanceViewListener? Function() currentSituationLaneAssistanceViewListenerGetLambda,
  void Function(CurrentSituationLaneAssistanceViewListener?) currentSituationLaneAssistanceViewListenerSetLambda,
  EnvironmentalZoneWarningListener? Function() environmentalZoneWarningListenerGetLambda,
  void Function(EnvironmentalZoneWarningListener?) environmentalZoneWarningListenerSetLambda,
  JunctionViewLaneAssistanceListener? Function() junctionViewLaneAssistanceListenerGetLambda,
  void Function(JunctionViewLaneAssistanceListener?) junctionViewLaneAssistanceListenerSetLambda,
  SafetyCameraWarningListener? Function() safetyCameraWarningListenerGetLambda,
  void Function(SafetyCameraWarningListener?) safetyCameraWarningListenerSetLambda,
  SafetyCameraWarningOptions Function() safetyCameraWarningOptionsGetLambda,
  void Function(SafetyCameraWarningOptions) safetyCameraWarningOptionsSetLambda,
  DangerZoneWarningListener? Function() dangerZoneWarningListenerGetLambda,
  void Function(DangerZoneWarningListener?) dangerZoneWarningListenerSetLambda,
  TruckRestrictionsWarningListener? Function() truckRestrictionsWarningListenerGetLambda,
  void Function(TruckRestrictionsWarningListener?) truckRestrictionsWarningListenerSetLambda,
  WarnerEngine Function() warnerEngineGetLambda,
  TruckRestrictionsWarningOptions Function() truckRestrictionsWarningOptionsGetLambda,
  void Function(TruckRestrictionsWarningOptions) truckRestrictionsWarningOptionsSetLambda,
  PostActionListener? Function() postActionListenerGetLambda,
  void Function(PostActionListener?) postActionListenerSetLambda,
  SpeedLimitListener? Function() speedLimitListenerGetLambda,
  void Function(SpeedLimitListener?) speedLimitListenerSetLambda,
  RoadTextsListener? Function() roadTextsListenerGetLambda,
  void Function(RoadTextsListener?) roadTextsListenerSetLambda,
  RoadAttributesListener? Function() roadAttributesListenerGetLambda,
  void Function(RoadAttributesListener?) roadAttributesListenerSetLambda,
  RoadSignWarningListener? Function() roadSignWarningListenerGetLambda,
  void Function(RoadSignWarningListener?) roadSignWarningListenerSetLambda,
  RoadSignWarningOptions Function() roadSignWarningOptionsGetLambda,
  void Function(RoadSignWarningOptions) roadSignWarningOptionsSetLambda,
  SchoolZoneWarningListener? Function() schoolZoneWarningListenerGetLambda,
  void Function(SchoolZoneWarningListener?) schoolZoneWarningListenerSetLambda,
  SchoolZoneWarningOptions Function() schoolZoneWarningOptionsGetLambda,
  void Function(SchoolZoneWarningOptions) schoolZoneWarningOptionsSetLambda,
  RealisticViewWarningListener? Function() realisticViewWarningListenerGetLambda,
  void Function(RealisticViewWarningListener?) realisticViewWarningListenerSetLambda,
  RealisticViewWarningOptions Function() realisticViewWarningOptionsGetLambda,
  void Function(RealisticViewWarningOptions) realisticViewWarningOptionsSetLambda,
  BorderCrossingWarningListener? Function() borderCrossingWarningListenerGetLambda,
  void Function(BorderCrossingWarningListener?) borderCrossingWarningListenerSetLambda,
  BorderCrossingWarningOptions Function() borderCrossingWarningOptionsGetLambda,
  void Function(BorderCrossingWarningOptions) borderCrossingWarningOptionsSetLambda,
  TollStopWarningListener? Function() tollStopWarningListenerGetLambda,
  void Function(TollStopWarningListener?) tollStopWarningListenerSetLambda,
  RailwayCrossingWarningListener? Function() railwayCrossingWarningListenerGetLambda,
  void Function(RailwayCrossingWarningListener?) railwayCrossingWarningListenerSetLambda,
  LowSpeedZoneWarningListener? Function() lowSpeedZoneWarningListenerGetLambda,
  void Function(LowSpeedZoneWarningListener?) lowSpeedZoneWarningListenerSetLambda,
  TrafficMergeWarningListener? Function() trafficMergeWarningListenerGetLambda,
  void Function(TrafficMergeWarningListener?) trafficMergeWarningListenerSetLambda,
  TrafficMergeWarningOptions Function() trafficMergeWarningOptionsGetLambda,
  void Function(TrafficMergeWarningOptions) trafficMergeWarningOptionsSetLambda,
  OffRoadDestinationReachedListener? Function() offRoadDestinationReachedListenerGetLambda,
  void Function(OffRoadDestinationReachedListener?) offRoadDestinationReachedListenerSetLambda,
  OffRoadProgressListener? Function() offRoadProgressListenerGetLambda,
  void Function(OffRoadProgressListener?) offRoadProgressListenerSetLambda,
  ManeuverNotificationOptions Function() maneuverNotificationOptionsGetLambda,
  void Function(ManeuverNotificationOptions) maneuverNotificationOptionsSetLambda,
  EventTextOptions Function() eventTextOptionsGetLambda,
  void Function(EventTextOptions) eventTextOptionsSetLambda,
  SpeedWarningOptions Function() speedWarningOptionsGetLambda,
  void Function(SpeedWarningOptions) speedWarningOptionsSetLambda,
  bool Function() isEnableTunnelExtrapolationGetLambda,
  void Function(bool) isEnableTunnelExtrapolationSetLambda,
  bool Function() isPassthroughWaypointsHandlingEnabledGetLambda,
  void Function(bool) isPassthroughWaypointsHandlingEnabledSetLambda,
  TrafficOnRoute? Function() trafficOnRouteGetLambda,
  void Function(TrafficOnRoute?) trafficOnRouteSetLambda,
  LocationManager Function() locationManagerGetLambda
) => NavigatorInterface$Lambdas(
  onLocationUpdatedLambda,
  getManeuverLambda,
  getManeuverNotificationTimingOptionsWithTimingProfileLambda,
  setManeuverNotificationTimingOptionsWithTimingProfileLambda,
  getWarningNotificationDistancesLambda,
  setWarningNotificationDistancesLambda,
  repeatLastManeuverNotificationLambda,
  calculateRemainingDistanceInMetersLambda,
  setCustomOptionLambda,
  routeGetLambda,
  routeSetLambda,
  trackingTransportProfileGetLambda,
  trackingTransportProfileSetLambda,
  trackingTransportSpecificationGetLambda,
  trackingTransportSpecificationSetLambda,
  navigableLocationListenerGetLambda,
  navigableLocationListenerSetLambda,
  routeProgressListenerGetLambda,
  routeProgressListenerSetLambda,
  routeDeviationListenerGetLambda,
  routeDeviationListenerSetLambda,
  eventTextListenerGetLambda,
  eventTextListenerSetLambda,
  milestoneStatusListenerGetLambda,
  milestoneStatusListenerSetLambda,
  destinationReachedListenerGetLambda,
  destinationReachedListenerSetLambda,
  speedWarningListenerGetLambda,
  speedWarningListenerSetLambda,
  maneuverViewLaneAssistanceListenerGetLambda,
  maneuverViewLaneAssistanceListenerSetLambda,
  currentSituationLaneAssistanceViewListenerGetLambda,
  currentSituationLaneAssistanceViewListenerSetLambda,
  environmentalZoneWarningListenerGetLambda,
  environmentalZoneWarningListenerSetLambda,
  junctionViewLaneAssistanceListenerGetLambda,
  junctionViewLaneAssistanceListenerSetLambda,
  safetyCameraWarningListenerGetLambda,
  safetyCameraWarningListenerSetLambda,
  safetyCameraWarningOptionsGetLambda,
  safetyCameraWarningOptionsSetLambda,
  dangerZoneWarningListenerGetLambda,
  dangerZoneWarningListenerSetLambda,
  truckRestrictionsWarningListenerGetLambda,
  truckRestrictionsWarningListenerSetLambda,
  warnerEngineGetLambda,
  truckRestrictionsWarningOptionsGetLambda,
  truckRestrictionsWarningOptionsSetLambda,
  postActionListenerGetLambda,
  postActionListenerSetLambda,
  speedLimitListenerGetLambda,
  speedLimitListenerSetLambda,
  roadTextsListenerGetLambda,
  roadTextsListenerSetLambda,
  roadAttributesListenerGetLambda,
  roadAttributesListenerSetLambda,
  roadSignWarningListenerGetLambda,
  roadSignWarningListenerSetLambda,
  roadSignWarningOptionsGetLambda,
  roadSignWarningOptionsSetLambda,
  schoolZoneWarningListenerGetLambda,
  schoolZoneWarningListenerSetLambda,
  schoolZoneWarningOptionsGetLambda,
  schoolZoneWarningOptionsSetLambda,
  realisticViewWarningListenerGetLambda,
  realisticViewWarningListenerSetLambda,
  realisticViewWarningOptionsGetLambda,
  realisticViewWarningOptionsSetLambda,
  borderCrossingWarningListenerGetLambda,
  borderCrossingWarningListenerSetLambda,
  borderCrossingWarningOptionsGetLambda,
  borderCrossingWarningOptionsSetLambda,
  tollStopWarningListenerGetLambda,
  tollStopWarningListenerSetLambda,
  railwayCrossingWarningListenerGetLambda,
  railwayCrossingWarningListenerSetLambda,
  lowSpeedZoneWarningListenerGetLambda,
  lowSpeedZoneWarningListenerSetLambda,
  trafficMergeWarningListenerGetLambda,
  trafficMergeWarningListenerSetLambda,
  trafficMergeWarningOptionsGetLambda,
  trafficMergeWarningOptionsSetLambda,
  offRoadDestinationReachedListenerGetLambda,
  offRoadDestinationReachedListenerSetLambda,
  offRoadProgressListenerGetLambda,
  offRoadProgressListenerSetLambda,
  maneuverNotificationOptionsGetLambda,
  maneuverNotificationOptionsSetLambda,
  eventTextOptionsGetLambda,
  eventTextOptionsSetLambda,
  speedWarningOptionsGetLambda,
  speedWarningOptionsSetLambda,
  isEnableTunnelExtrapolationGetLambda,
  isEnableTunnelExtrapolationSetLambda,
  isPassthroughWaypointsHandlingEnabledGetLambda,
  isPassthroughWaypointsHandlingEnabledSetLambda,
  trafficOnRouteGetLambda,
  trafficOnRouteSetLambda,
  locationManagerGetLambda
);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

