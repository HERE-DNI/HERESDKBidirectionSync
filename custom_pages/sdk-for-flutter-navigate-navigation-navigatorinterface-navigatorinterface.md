---
title: "NavigatorInterface constructor"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-navigatorinterface"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- NavigatorInterface.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-navigatorinterface-class</li>
<li class="self-crumb">NavigatorInterface factory constructor</li>
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
<div class="main-content" data-above-sidebar="navigation/NavigatorInterface-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>NavigatorInterface constructor</h1></div>
<section class="multi-line-signature">
NavigatorInterface(<wbr/><ol class="parameter-list"> <li>void onLocationUpdatedLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-location-class</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-routing-maneuver-class? getManeuverLambda(<ol class="parameter-list single-line"> <li>int</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-class getManeuverNotificationTimingOptionsWithTimingProfileLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-transport-transportmode, </li>
<li>/sdk-for-flutter-navigate-navigation-timingprofile</li>
</ol>), </li>
<li>bool setManeuverNotificationTimingOptionsWithTimingProfileLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-transport-transportmode, </li>
<li>/sdk-for-flutter-navigate-navigation-timingprofile, </li>
<li>/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-class</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-warningnotificationdistances-class getWarningNotificationDistancesLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-warningtype</li>
</ol>), </li>
<li>bool setWarningNotificationDistancesLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-warningtype, </li>
<li>/sdk-for-flutter-navigate-navigation-warningnotificationdistances-class</li>
</ol>), </li>
<li>void repeatLastManeuverNotificationLambda(), </li>
<li>int? calculateRemainingDistanceInMetersLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-geocoordinates-class</li>
</ol>), </li>
<li>void setCustomOptionLambda(<ol class="parameter-list single-line"> <li>String, </li>
<li>String</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-routing-route-class? routeGetLambda(), </li>
<li>void routeSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-routing-route-class?</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-core-transportprofile-class? trackingTransportProfileGetLambda(), </li>
<li>void trackingTransportProfileSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-transportprofile-class?</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-transport-transportspecification-class? trackingTransportSpecificationGetLambda(), </li>
<li>void trackingTransportSpecificationSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-transport-transportspecification-class?</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-navigablelocationlistener-class? navigableLocationListenerGetLambda(), </li>
<li>void navigableLocationListenerSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-navigablelocationlistener-class?</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-routeprogresslistener-class? routeProgressListenerGetLambda(), </li>
<li>void routeProgressListenerSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-routeprogresslistener-class?</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-routedeviationlistener-class? routeDeviationListenerGetLambda(), </li>
<li>void routeDeviationListenerSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-routedeviationlistener-class?</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-eventtextlistener-class? eventTextListenerGetLambda(), </li>
<li>void eventTextListenerSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-eventtextlistener-class?</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-milestonestatuslistener-class? milestoneStatusListenerGetLambda(), </li>
<li>void milestoneStatusListenerSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-milestonestatuslistener-class?</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-destinationreachedlistener-class? destinationReachedListenerGetLambda(), </li>
<li>void destinationReachedListenerSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-destinationreachedlistener-class?</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-speedwarninglistener-class? speedWarningListenerGetLambda(), </li>
<li>void speedWarningListenerSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-speedwarninglistener-class?</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-maneuverviewlaneassistancelistener-class? maneuverViewLaneAssistanceListenerGetLambda(), </li>
<li>void maneuverViewLaneAssistanceListenerSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-maneuverviewlaneassistancelistener-class?</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-class? currentSituationLaneAssistanceViewListenerGetLambda(), </li>
<li>void currentSituationLaneAssistanceViewListenerSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-class?</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-environmentalzonewarninglistener-class? environmentalZoneWarningListenerGetLambda(), </li>
<li>void environmentalZoneWarningListenerSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-environmentalzonewarninglistener-class?</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-junctionviewlaneassistancelistener-class? junctionViewLaneAssistanceListenerGetLambda(), </li>
<li>void junctionViewLaneAssistanceListenerSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-junctionviewlaneassistancelistener-class?</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-class? safetyCameraWarningListenerGetLambda(), </li>
<li>void safetyCameraWarningListenerSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-class?</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-safetycamerawarningoptions-class safetyCameraWarningOptionsGetLambda(), </li>
<li>void safetyCameraWarningOptionsSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-safetycamerawarningoptions-class</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-dangerzonewarninglistener-class? dangerZoneWarningListenerGetLambda(), </li>
<li>void dangerZoneWarningListenerSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-dangerzonewarninglistener-class?</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-truckrestrictionswarninglistener-class? truckRestrictionsWarningListenerGetLambda(), </li>
<li>void truckRestrictionsWarningListenerSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-truckrestrictionswarninglistener-class?</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-warner-warnerengine-class warnerEngineGetLambda(), </li>
<li>/sdk-for-flutter-navigate-navigation-truckrestrictionswarningoptions-class truckRestrictionsWarningOptionsGetLambda(), </li>
<li>void truckRestrictionsWarningOptionsSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-truckrestrictionswarningoptions-class</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-postactionlistener-class? postActionListenerGetLambda(), </li>
<li>void postActionListenerSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-postactionlistener-class?</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-speedlimitlistener-class? speedLimitListenerGetLambda(), </li>
<li>void speedLimitListenerSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-speedlimitlistener-class?</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-roadtextslistener-class? roadTextsListenerGetLambda(), </li>
<li>void roadTextsListenerSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-roadtextslistener-class?</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-roadattributeslistener-class? roadAttributesListenerGetLambda(), </li>
<li>void roadAttributesListenerSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-roadattributeslistener-class?</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-roadsignwarninglistener-class? roadSignWarningListenerGetLambda(), </li>
<li>void roadSignWarningListenerSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-roadsignwarninglistener-class?</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-roadsignwarningoptions-class roadSignWarningOptionsGetLambda(), </li>
<li>void roadSignWarningOptionsSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-roadsignwarningoptions-class</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-schoolzonewarninglistener-class? schoolZoneWarningListenerGetLambda(), </li>
<li>void schoolZoneWarningListenerSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-schoolzonewarninglistener-class?</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-schoolzonewarningoptions-class schoolZoneWarningOptionsGetLambda(), </li>
<li>void schoolZoneWarningOptionsSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-schoolzonewarningoptions-class</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-class? realisticViewWarningListenerGetLambda(), </li>
<li>void realisticViewWarningListenerSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-class?</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-realisticviewwarningoptions-class realisticViewWarningOptionsGetLambda(), </li>
<li>void realisticViewWarningOptionsSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-realisticviewwarningoptions-class</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-bordercrossingwarninglistener-class? borderCrossingWarningListenerGetLambda(), </li>
<li>void borderCrossingWarningListenerSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-bordercrossingwarninglistener-class?</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-bordercrossingwarningoptions-class borderCrossingWarningOptionsGetLambda(), </li>
<li>void borderCrossingWarningOptionsSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-bordercrossingwarningoptions-class</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-tollstopwarninglistener-class? tollStopWarningListenerGetLambda(), </li>
<li>void tollStopWarningListenerSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-tollstopwarninglistener-class?</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-class? railwayCrossingWarningListenerGetLambda(), </li>
<li>void railwayCrossingWarningListenerSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-class?</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-lowspeedzonewarninglistener-class? lowSpeedZoneWarningListenerGetLambda(), </li>
<li>void lowSpeedZoneWarningListenerSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-lowspeedzonewarninglistener-class?</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-class? trafficMergeWarningListenerGetLambda(), </li>
<li>void trafficMergeWarningListenerSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-class?</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-trafficmergewarningoptions-class trafficMergeWarningOptionsGetLambda(), </li>
<li>void trafficMergeWarningOptionsSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-trafficmergewarningoptions-class</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-offroaddestinationreachedlistener-class? offRoadDestinationReachedListenerGetLambda(), </li>
<li>void offRoadDestinationReachedListenerSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-offroaddestinationreachedlistener-class?</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-offroadprogresslistener-class? offRoadProgressListenerGetLambda(), </li>
<li>void offRoadProgressListenerSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-offroadprogresslistener-class?</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-class maneuverNotificationOptionsGetLambda(), </li>
<li>void maneuverNotificationOptionsSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-class</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-eventtextoptions-class eventTextOptionsGetLambda(), </li>
<li>void eventTextOptionsSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-eventtextoptions-class</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-navigation-speedwarningoptions-class speedWarningOptionsGetLambda(), </li>
<li>void speedWarningOptionsSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-speedwarningoptions-class</li>
</ol>), </li>
<li>bool isEnableTunnelExtrapolationGetLambda(), </li>
<li>void isEnableTunnelExtrapolationSetLambda(<ol class="parameter-list single-line"> <li>bool</li>
</ol>), </li>
<li>bool isPassthroughWaypointsHandlingEnabledGetLambda(), </li>
<li>void isPassthroughWaypointsHandlingEnabledSetLambda(<ol class="parameter-list single-line"> <li>bool</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-routing-trafficonroute-class? trafficOnRouteGetLambda(), </li>
<li>void trafficOnRouteSetLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-routing-trafficonroute-class?</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-mapmatcher-locationmanager-class locationManagerGetLambda(), </li>
</ol>)
    </section>
<section class="desc markdown">
<p>This abstract class provides the basic functionality needed to run a navigation session.</p>
</section>
<section class="summary source-code" id="source">
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
<li>/sdk-for-flutter-navigate-navigation-navigatorinterface-class</li>
<li class="self-crumb">NavigatorInterface factory constructor</li>
</ol>
<h5>NavigatorInterface class</h5>
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
