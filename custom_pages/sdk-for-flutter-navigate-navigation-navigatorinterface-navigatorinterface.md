---
title: "NavigatorInterface constructor"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-navigatorinterface"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- NavigatorInterface.html -->


<div>
<h1>NavigatorInterface constructor</h1></div>

NavigatorInterface(<ol class="parameter-list"> <li>void onLocationUpdatedLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-core-location-class">Location</a></li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-routing-maneuver-class">Maneuver</a>? getManeuverLambda(<ol class="parameter-list single-line"> <li>int</li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-class">ManeuverNotificationTimingOptions</a> getManeuverNotificationTimingOptionsWithTimingProfileLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode</a>, </li>
<li><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile</a></li>
</ol>), </li>
<li>bool setManeuverNotificationTimingOptionsWithTimingProfileLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode</a>, </li>
<li><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile</a>, </li>
<li><a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-class">ManeuverNotificationTimingOptions</a></li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-warningnotificationdistances-class">WarningNotificationDistances</a> getWarningNotificationDistancesLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType</a></li>
</ol>), </li>
<li>bool setWarningNotificationDistancesLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType</a>, </li>
<li><a href="sdk-for-flutter-navigate-navigation-warningnotificationdistances-class">WarningNotificationDistances</a></li>
</ol>), </li>
<li>void repeatLastManeuverNotificationLambda(), </li>
<li>int? calculateRemainingDistanceInMetersLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></li>
</ol>), </li>
<li>void setCustomOptionLambda(<ol class="parameter-list single-line"> <li>String, </li>
<li>String</li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-routing-route-class">Route</a>? routeGetLambda(), </li>
<li>void routeSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-routing-route-class">Route</a>?</li>
</ol>), </li>
<li><a class="deprecated" href="sdk-for-flutter-navigate-core-transportprofile-class">TransportProfile</a>? trackingTransportProfileGetLambda(), </li>
<li>void trackingTransportProfileSetLambda(<ol class="parameter-list single-line"> <li><a class="deprecated" href="sdk-for-flutter-navigate-core-transportprofile-class">TransportProfile</a>?</li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a>? trackingTransportSpecificationGetLambda(), </li>
<li>void trackingTransportSpecificationSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a>?</li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-navigablelocationlistener-class">NavigableLocationListener</a>? navigableLocationListenerGetLambda(), </li>
<li>void navigableLocationListenerSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-navigablelocationlistener-class">NavigableLocationListener</a>?</li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-routeprogresslistener-class">RouteProgressListener</a>? routeProgressListenerGetLambda(), </li>
<li>void routeProgressListenerSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-routeprogresslistener-class">RouteProgressListener</a>?</li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-routedeviationlistener-class">RouteDeviationListener</a>? routeDeviationListenerGetLambda(), </li>
<li>void routeDeviationListenerSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-routedeviationlistener-class">RouteDeviationListener</a>?</li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-eventtextlistener-class">EventTextListener</a>? eventTextListenerGetLambda(), </li>
<li>void eventTextListenerSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-eventtextlistener-class">EventTextListener</a>?</li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-milestonestatuslistener-class">MilestoneStatusListener</a>? milestoneStatusListenerGetLambda(), </li>
<li>void milestoneStatusListenerSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-milestonestatuslistener-class">MilestoneStatusListener</a>?</li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-destinationreachedlistener-class">DestinationReachedListener</a>? destinationReachedListenerGetLambda(), </li>
<li>void destinationReachedListenerSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-destinationreachedlistener-class">DestinationReachedListener</a>?</li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-speedwarninglistener-class">SpeedWarningListener</a>? speedWarningListenerGetLambda(), </li>
<li>void speedWarningListenerSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-speedwarninglistener-class">SpeedWarningListener</a>?</li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-maneuverviewlaneassistancelistener-class">ManeuverViewLaneAssistanceListener</a>? maneuverViewLaneAssistanceListenerGetLambda(), </li>
<li>void maneuverViewLaneAssistanceListenerSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-maneuverviewlaneassistancelistener-class">ManeuverViewLaneAssistanceListener</a>?</li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-class">CurrentSituationLaneAssistanceViewListener</a>? currentSituationLaneAssistanceViewListenerGetLambda(), </li>
<li>void currentSituationLaneAssistanceViewListenerSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-class">CurrentSituationLaneAssistanceViewListener</a>?</li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-environmentalzonewarninglistener-class">EnvironmentalZoneWarningListener</a>? environmentalZoneWarningListenerGetLambda(), </li>
<li>void environmentalZoneWarningListenerSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-environmentalzonewarninglistener-class">EnvironmentalZoneWarningListener</a>?</li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-junctionviewlaneassistancelistener-class">JunctionViewLaneAssistanceListener</a>? junctionViewLaneAssistanceListenerGetLambda(), </li>
<li>void junctionViewLaneAssistanceListenerSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-junctionviewlaneassistancelistener-class">JunctionViewLaneAssistanceListener</a>?</li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-class">SafetyCameraWarningListener</a>? safetyCameraWarningListenerGetLambda(), </li>
<li>void safetyCameraWarningListenerSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-class">SafetyCameraWarningListener</a>?</li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-safetycamerawarningoptions-class">SafetyCameraWarningOptions</a> safetyCameraWarningOptionsGetLambda(), </li>
<li>void safetyCameraWarningOptionsSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-safetycamerawarningoptions-class">SafetyCameraWarningOptions</a></li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-dangerzonewarninglistener-class">DangerZoneWarningListener</a>? dangerZoneWarningListenerGetLambda(), </li>
<li>void dangerZoneWarningListenerSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-dangerzonewarninglistener-class">DangerZoneWarningListener</a>?</li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-truckrestrictionswarninglistener-class">TruckRestrictionsWarningListener</a>? truckRestrictionsWarningListenerGetLambda(), </li>
<li>void truckRestrictionsWarningListenerSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-truckrestrictionswarninglistener-class">TruckRestrictionsWarningListener</a>?</li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-warner-warnerengine-class">WarnerEngine</a> warnerEngineGetLambda(), </li>
<li><a href="sdk-for-flutter-navigate-navigation-truckrestrictionswarningoptions-class">TruckRestrictionsWarningOptions</a> truckRestrictionsWarningOptionsGetLambda(), </li>
<li>void truckRestrictionsWarningOptionsSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-truckrestrictionswarningoptions-class">TruckRestrictionsWarningOptions</a></li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-postactionlistener-class">PostActionListener</a>? postActionListenerGetLambda(), </li>
<li>void postActionListenerSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-postactionlistener-class">PostActionListener</a>?</li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-speedlimitlistener-class">SpeedLimitListener</a>? speedLimitListenerGetLambda(), </li>
<li>void speedLimitListenerSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-speedlimitlistener-class">SpeedLimitListener</a>?</li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-roadtextslistener-class">RoadTextsListener</a>? roadTextsListenerGetLambda(), </li>
<li>void roadTextsListenerSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-roadtextslistener-class">RoadTextsListener</a>?</li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-roadattributeslistener-class">RoadAttributesListener</a>? roadAttributesListenerGetLambda(), </li>
<li>void roadAttributesListenerSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-roadattributeslistener-class">RoadAttributesListener</a>?</li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-roadsignwarninglistener-class">RoadSignWarningListener</a>? roadSignWarningListenerGetLambda(), </li>
<li>void roadSignWarningListenerSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-roadsignwarninglistener-class">RoadSignWarningListener</a>?</li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-roadsignwarningoptions-class">RoadSignWarningOptions</a> roadSignWarningOptionsGetLambda(), </li>
<li>void roadSignWarningOptionsSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-roadsignwarningoptions-class">RoadSignWarningOptions</a></li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-schoolzonewarninglistener-class">SchoolZoneWarningListener</a>? schoolZoneWarningListenerGetLambda(), </li>
<li>void schoolZoneWarningListenerSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-schoolzonewarninglistener-class">SchoolZoneWarningListener</a>?</li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-schoolzonewarningoptions-class">SchoolZoneWarningOptions</a> schoolZoneWarningOptionsGetLambda(), </li>
<li>void schoolZoneWarningOptionsSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-schoolzonewarningoptions-class">SchoolZoneWarningOptions</a></li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-class">RealisticViewWarningListener</a>? realisticViewWarningListenerGetLambda(), </li>
<li>void realisticViewWarningListenerSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-class">RealisticViewWarningListener</a>?</li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-realisticviewwarningoptions-class">RealisticViewWarningOptions</a> realisticViewWarningOptionsGetLambda(), </li>
<li>void realisticViewWarningOptionsSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-realisticviewwarningoptions-class">RealisticViewWarningOptions</a></li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-bordercrossingwarninglistener-class">BorderCrossingWarningListener</a>? borderCrossingWarningListenerGetLambda(), </li>
<li>void borderCrossingWarningListenerSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-bordercrossingwarninglistener-class">BorderCrossingWarningListener</a>?</li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-bordercrossingwarningoptions-class">BorderCrossingWarningOptions</a> borderCrossingWarningOptionsGetLambda(), </li>
<li>void borderCrossingWarningOptionsSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-bordercrossingwarningoptions-class">BorderCrossingWarningOptions</a></li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-tollstopwarninglistener-class">TollStopWarningListener</a>? tollStopWarningListenerGetLambda(), </li>
<li>void tollStopWarningListenerSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-tollstopwarninglistener-class">TollStopWarningListener</a>?</li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-class">RailwayCrossingWarningListener</a>? railwayCrossingWarningListenerGetLambda(), </li>
<li>void railwayCrossingWarningListenerSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-class">RailwayCrossingWarningListener</a>?</li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-lowspeedzonewarninglistener-class">LowSpeedZoneWarningListener</a>? lowSpeedZoneWarningListenerGetLambda(), </li>
<li>void lowSpeedZoneWarningListenerSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-lowspeedzonewarninglistener-class">LowSpeedZoneWarningListener</a>?</li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-class">TrafficMergeWarningListener</a>? trafficMergeWarningListenerGetLambda(), </li>
<li>void trafficMergeWarningListenerSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-class">TrafficMergeWarningListener</a>?</li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-trafficmergewarningoptions-class">TrafficMergeWarningOptions</a> trafficMergeWarningOptionsGetLambda(), </li>
<li>void trafficMergeWarningOptionsSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-trafficmergewarningoptions-class">TrafficMergeWarningOptions</a></li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-offroaddestinationreachedlistener-class">OffRoadDestinationReachedListener</a>? offRoadDestinationReachedListenerGetLambda(), </li>
<li>void offRoadDestinationReachedListenerSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-offroaddestinationreachedlistener-class">OffRoadDestinationReachedListener</a>?</li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-offroadprogresslistener-class">OffRoadProgressListener</a>? offRoadProgressListenerGetLambda(), </li>
<li>void offRoadProgressListenerSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-offroadprogresslistener-class">OffRoadProgressListener</a>?</li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-class">ManeuverNotificationOptions</a> maneuverNotificationOptionsGetLambda(), </li>
<li>void maneuverNotificationOptionsSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-class">ManeuverNotificationOptions</a></li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-eventtextoptions-class">EventTextOptions</a> eventTextOptionsGetLambda(), </li>
<li>void eventTextOptionsSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-eventtextoptions-class">EventTextOptions</a></li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-navigation-speedwarningoptions-class">SpeedWarningOptions</a> speedWarningOptionsGetLambda(), </li>
<li>void speedWarningOptionsSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-speedwarningoptions-class">SpeedWarningOptions</a></li>
</ol>), </li>
<li>bool isEnableTunnelExtrapolationGetLambda(), </li>
<li>void isEnableTunnelExtrapolationSetLambda(<ol class="parameter-list single-line"> <li>bool</li>
</ol>), </li>
<li>bool isPassthroughWaypointsHandlingEnabledGetLambda(), </li>
<li>void isPassthroughWaypointsHandlingEnabledSetLambda(<ol class="parameter-list single-line"> <li>bool</li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-routing-trafficonroute-class">TrafficOnRoute</a>? trafficOnRouteGetLambda(), </li>
<li>void trafficOnRouteSetLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-routing-trafficonroute-class">TrafficOnRoute</a>?</li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-mapmatcher-locationmanager-class">LocationManager</a> locationManagerGetLambda(), </li>
</ol>)
    

<p>This abstract class provides the basic functionality needed to run a navigation session.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory NavigatorInterface(
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
) =&gt; NavigatorInterface$Lambdas(
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
);</code></pre>

 



</div>
`
}</HTMLBlock>
