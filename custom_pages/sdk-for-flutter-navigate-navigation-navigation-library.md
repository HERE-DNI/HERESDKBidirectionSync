---
title: "Untitled"
slug: "sdk-for-flutter-navigate-navigation-navigation-library"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- navigation-library.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li class="self-crumb">navigation.dart</li>
</ol>
<div class="self-name">navigation</div>
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
<div class="main-content" data-above-sidebar="" data-below-sidebar="navigation/navigation-library-sidebar.html" id="dartdoc-main-content">
<div>
<h1>navigation library</h1>
</div>
<section class="summary offset-anchor" id="classes">
<h2>Classes</h2>
<dl>
<dt id="AreaCameraBehavior">
/sdk-for-flutter-navigate-navigation-areacamerabehavior-class
</dt>
<dd>
  Use this class to show an overview of geo points.
</dd>
<dt id="AutomotiveCameraBehavior">
/sdk-for-flutter-navigate-navigation-automotivecamerabehavior-class
</dt>
<dd>
  Provides a high-level camera controller for automotive navigation that manages both tracking
and area camera behaviors.
</dd>
<dt id="BorderCrossingWarning">
/sdk-for-flutter-navigate-navigation-bordercrossingwarning-class
</dt>
<dd>
  A border crossing.
</dd>
<dt id="BorderCrossingWarningListener">
/sdk-for-flutter-navigate-navigation-bordercrossingwarninglistener-class
</dt>
<dd>
  This abstract class
should be implemented in order to receive border crossing warnings for country and state borders.
</dd>
<dt id="BorderCrossingWarningOptions">
/sdk-for-flutter-navigate-navigation-bordercrossingwarningoptions-class
</dt>
<dd>
  Border crossing warning options.
</dd>
<dt id="CameraBehavior">
/sdk-for-flutter-navigate-navigation-camerabehavior-class
</dt>
<dd>
  Abstract class used to change implement different
camera behaviors.
</dd>
<dt id="CurrentSituationLaneAssistanceView">
/sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceview-class
</dt>
<dd>
  A class that provides current situation lane assistance view
information for the street at the current location.
</dd>
<dt id="CurrentSituationLaneAssistanceViewListener">
/sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-class
</dt>
<dd>
  This abstract class should be
implemented in order to receive notifications on /sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceview-class.
</dd>
<dt id="CurrentSituationLaneView">
/sdk-for-flutter-navigate-navigation-currentsituationlaneview-class
</dt>
<dd>
  A class that provides current situation lane assistance view
information for the street at the current position of a single lane.
</dd>
<dt id="CustomPanningData">
/sdk-for-flutter-navigate-navigation-custompanningdata-class
</dt>
<dd>
  This class contains all the information regarding the next angular panning element, including
a new estimated audio cue duration, and a new set of initial and sweep angular angle,
allowing the customization of the spatial audio trajectories for any type of notification,
such as speed or merge warners, maneuvers or even roundabouts notifications.
</dd>
<dt id="DangerZoneWarning">
/sdk-for-flutter-navigate-navigation-dangerzonewarning-class
</dt>
<dd>
  Represents danger zones.
</dd>
<dt id="DangerZoneWarningListener">
/sdk-for-flutter-navigate-navigation-dangerzonewarninglistener-class
</dt>
<dd>
  This abstract class should be implemented in order to receive notifications about the Danger zones.
</dd>
<dt id="DestinationReachedListener">
/sdk-for-flutter-navigate-navigation-destinationreachedlistener-class
</dt>
<dd>
  This abstract class should be
implemented in order to receive notifications from this class about the
arrival at the destination.
</dd>
<dt id="DimensionRestriction">
/sdk-for-flutter-navigate-navigation-dimensionrestriction-class
</dt>
<dd>
  Defines a dimension restriction.
</dd>
<dt id="DynamicCameraBehavior">
/sdk-for-flutter-navigate-navigation-dynamiccamerabehavior-class
</dt>
<dd>
  Use this class to follow the current location of the user: The camera will look at
the target location that was fed into the navigator instance, gradually zooming in as the user
approaches each maneuver and zooming out after the user passes them.
</dd>
<dt id="EnvironmentalZoneWarning">
/sdk-for-flutter-navigate-navigation-environmentalzonewarning-class
</dt>
<dd>
  Represents Environmental zones.
</dd>
<dt id="EnvironmentalZoneWarningListener">
/sdk-for-flutter-navigate-navigation-environmentalzonewarninglistener-class
</dt>
<dd>
  This abstract class should be implemented in order to receive notifications about the environmental zones.
</dd>
<dt id="EventText">
/sdk-for-flutter-navigate-navigation-eventtext-class
</dt>
<dd>
  Contains all the information regarding the next text announcement.
</dd>
<dt id="EventTextListener">
/sdk-for-flutter-navigate-navigation-eventtextlistener-class
</dt>
<dd>
  This abstract class should be implemented in order to receive notifications
when text notifications are available from /sdk-for-flutter-navigate-navigation-navigator-class.
</dd>
<dt id="EventTextOptions">
/sdk-for-flutter-navigate-navigation-eventtextoptions-class
</dt>
<dd>
  Text notifications options.
</dd>
<dt id="FixedCameraBehavior">
/sdk-for-flutter-navigate-navigation-fixedcamerabehavior-class
</dt>
<dd>
  Use this class to follow the current location of the user: The camera will permanently look at
the target location that was fed into the navigator instance.
</dd>
<dt id="GPXDocument">
/sdk-for-flutter-navigate-navigation-gpxdocument-class
</dt>
<dd>
  Use the GPXDocument to load the GPX file.
</dd>
<dt id="GPXOptions">
/sdk-for-flutter-navigate-navigation-gpxoptions-class
</dt>
<dd>
  Options used when reading the GPX file.
</dd>
<dt id="GPXTrack">
/sdk-for-flutter-navigate-navigation-gpxtrack-class
</dt>
<dd>
  Single track from the /sdk-for-flutter-navigate-navigation-gpxdocument-class.
</dd>
<dt id="GPXTrackWriter">
/sdk-for-flutter-navigate-navigation-gpxtrackwriter-class
</dt>
<dd>
  Writes GPX track points to /sdk-for-flutter-navigate-navigation-gpxtrack-class.
</dd>
<dt id="InterpolatedLocationListener">
/sdk-for-flutter-navigate-navigation-interpolatedlocationlistener-class
</dt>
<dd>
  This abstract class should be implemented
in order to receive interpolated locations.
</dd>
<dt id="JunctionViewLaneAssistance">
/sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-class
</dt>
<dd>
  A class that provides lane assistance information for the next complex junction
in order to keep following the route.
</dd>
<dt id="JunctionViewLaneAssistanceListener">
/sdk-for-flutter-navigate-navigation-junctionviewlaneassistancelistener-class
</dt>
<dd>
  This abstract class should be
implemented in order to receive notifications on /sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-class.
</dd>
<dt id="Lane">
/sdk-for-flutter-navigate-navigation-lane-class
</dt>
<dd>
  A class that provides information for a lane.
</dd>
<dt id="LaneAccess">
/sdk-for-flutter-navigate-navigation-laneaccess-class
</dt>
<dd>
  A class which identifies the vehicle type(s) allowed to
access a lane.
</dd>
<dt id="LaneDirectionCategory">
/sdk-for-flutter-navigate-navigation-lanedirectioncategory-class
</dt>
<dd>
  Indicates the directions of a lane.
</dd>
<dt id="LaneMarkings">
/sdk-for-flutter-navigate-navigation-lanemarkings-class
</dt>
<dd>
  A class that provides information for the lane markings.
</dd>
<dt id="LaneType">
/sdk-for-flutter-navigate-navigation-lanetype-class
</dt>
<dd>
  A class that provides information on the available lane properties.
</dd>
<dt id="LocationSimulator">
/sdk-for-flutter-navigate-navigation-locationsimulator-class
</dt>
<dd>
  Use the <code>LocationSimulator</code> to generate locations along a route or a GPX document.
</dd>
<dt id="LocationSimulatorOptions">
/sdk-for-flutter-navigate-navigation-locationsimulatoroptions-class
</dt>
<dd>
  Options to specify how the location simulator will behave.
</dd>
<dt id="LowSpeedZoneWarning">
/sdk-for-flutter-navigate-navigation-lowspeedzonewarning-class
</dt>
<dd>
  A class that provides low speed zone.
</dd>
<dt id="LowSpeedZoneWarningListener">
/sdk-for-flutter-navigate-navigation-lowspeedzonewarninglistener-class
</dt>
<dd>
  This abstract class should be implemented in order to receive low speed zone warnings.
</dd>
<dt id="ManeuverNotificationDetails">
/sdk-for-flutter-navigate-navigation-maneuvernotificationdetails-class
</dt>
<dd>
  This class provides the information regarding the next maneuver to be triggered
</dd>
<dt id="ManeuverNotificationOptions">
/sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-class
</dt>
<dd>
  A class containing all options to be used when generating maneuver notifications.
</dd>
<dt id="ManeuverNotificationTimingOptions">
/sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-class
</dt>
<dd>
  A class defining timing and distance thresholds for maneuver notifications.
</dd>
<dt id="ManeuverProgress">
/sdk-for-flutter-navigate-navigation-maneuverprogress-class
</dt>
<dd>
  Indicates a user's progress to a /sdk-for-flutter-navigate-routing-maneuver-class.
</dd>
<dt id="ManeuverViewLaneAssistance">
/sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-class
</dt>
<dd>
  A class that provides lane assistance information for the next maneuver(s).
</dd>
<dt id="ManeuverViewLaneAssistanceListener">
/sdk-for-flutter-navigate-navigation-maneuverviewlaneassistancelistener-class
</dt>
<dd>
  This abstract class should be
implemented in order to receive notifications on /sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-class.
</dd>
<dt id="MapMatchedLocation">
/sdk-for-flutter-navigate-navigation-mapmatchedlocation-class
</dt>
<dd>
  Describes a map-matched location in the world at a given time.
</dd>
<dt id="Milestone">
/sdk-for-flutter-navigate-navigation-milestone-class
</dt>
<dd>
  Represents information about the waypoints along the route.
</dd>
<dt id="MilestoneStatusListener">
/sdk-for-flutter-navigate-navigation-milestonestatuslistener-class
</dt>
<dd>
  This abstract class should be
implemented in order to receive notifications from this class about the
arrival at each /sdk-for-flutter-navigate-navigation-milestone-class or missing it.
</dd>
<dt id="NavigableLocation">
/sdk-for-flutter-navigate-navigation-navigablelocation-class
</dt>
<dd>
  Contains all the relevant information on the current location.
</dd>
<dt id="NavigableLocationListener">
/sdk-for-flutter-navigate-navigation-navigablelocationlistener-class
</dt>
<dd>
  This abstract class should be implemented in order to receive notifications
about the current location from /sdk-for-flutter-navigate-navigation-navigator-class.
</dd>
<dt id="Navigator">
/sdk-for-flutter-navigate-navigation-navigator-class
</dt>
<dd>
  This class provides the basic navigation functionality.
</dd>
<dt id="NavigatorInterface">
/sdk-for-flutter-navigate-navigation-navigatorinterface-class
</dt>
<dd>
  This abstract class provides the basic functionality needed to run a navigation session.
</dd>
<dt id="OffRoadDestinationReachedListener">
/sdk-for-flutter-navigate-navigation-offroaddestinationreachedlistener-class
</dt>
<dd>
  This abstract class should be
implemented in order to receive notifications from this class about the
arrival at the off-road destination.
</dd>
<dt id="OffRoadProgress">
/sdk-for-flutter-navigate-navigation-offroadprogress-class
</dt>
<dd>
  Represents the information needed to help the users to reach their off-road destination.
</dd>
<dt id="OffRoadProgressListener">
/sdk-for-flutter-navigate-navigation-offroadprogresslistener-class
</dt>
<dd>
  This abstract class should be implemented in order to
receive notifications about the current off-road location from /sdk-for-flutter-navigate-navigation-navigator-class.
</dd>
<dt id="PostActionListener">
/sdk-for-flutter-navigate-navigation-postactionlistener-class
</dt>
<dd>
  This abstract class should be implemented in order to
receive post action notifications.
</dd>
<dt id="RailwayCrossingWarning">
/sdk-for-flutter-navigate-navigation-railwaycrossingwarning-class
</dt>
<dd>
  A class that provides railway crossing.
</dd>
<dt id="RailwayCrossingWarningListener">
/sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-class
</dt>
<dd>
  This abstract class
should be implemented in order to receive railway crossing warnings.
</dd>
<dt id="RealisticViewRasterImage">
/sdk-for-flutter-navigate-navigation-realisticviewrasterimage-class
</dt>
<dd>
  A realistic view.
</dd>
<dt id="RealisticViewVectorImage">
/sdk-for-flutter-navigate-navigation-realisticviewvectorimage-class
</dt>
<dd>
  A realistic view of a junction.
</dd>
<dt id="RealisticViewWarning">
/sdk-for-flutter-navigate-navigation-realisticviewwarning-class
</dt>
<dd>
  A realistic view notification.
</dd>
<dt id="RealisticViewWarningListener">
/sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-class
</dt>
<dd>
  This abstract class
should be implemented in order to receive realistic view warnings.
</dd>
<dt id="RealisticViewWarningOptions">
/sdk-for-flutter-navigate-navigation-realisticviewwarningoptions-class
</dt>
<dd>
  Realistic view warning options.
</dd>
<dt id="RoadAttributes">
/sdk-for-flutter-navigate-navigation-roadattributes-class
</dt>
<dd>
  Road attributes, including usage and physical characteristics.
</dd>
<dt id="RoadAttributesListener">
/sdk-for-flutter-navigate-navigation-roadattributeslistener-class
</dt>
<dd>
  This abstract class
should be implemented in order to receive attributes of the current road.
</dd>
<dt id="RoadSign">
/sdk-for-flutter-navigate-navigation-roadsign-class
</dt>
<dd>
  Describes a road sign.
</dd>
<dt id="RoadSignWarning">
/sdk-for-flutter-navigate-navigation-roadsignwarning-class
</dt>
<dd>
  A road sign.
</dd>
<dt id="RoadSignWarningListener">
/sdk-for-flutter-navigate-navigation-roadsignwarninglistener-class
</dt>
<dd>
  This abstract class
should be implemented in order to receive road sign warnings.
</dd>
<dt id="RoadSignWarningOptions">
/sdk-for-flutter-navigate-navigation-roadsignwarningoptions-class
</dt>
<dd>
  A class that provides road sign warning options.
</dd>
<dt id="RoadTextsListener">
/sdk-for-flutter-navigate-navigation-roadtextslistener-class
</dt>
<dd>
  This abstract class
should be implemented in order to receive textual attributes of the current road.
</dd>
<dt id="RouteDeviation">
/sdk-for-flutter-navigate-navigation-routedeviation-class
</dt>
<dd>
  Contains all the relevant information on a deviation from the route.
</dd>
<dt id="RouteDeviationListener">
/sdk-for-flutter-navigate-navigation-routedeviationlistener-class
</dt>
<dd>
  This abstract class should be implemented in order to
receive notifications
about route deviations from /sdk-for-flutter-navigate-navigation-navigator-class.
</dd>
<dt id="RouteMatchedLocation">
/sdk-for-flutter-navigate-navigation-routematchedlocation-class
</dt>
<dd>
  Represents a location matched to a specific position on a navigation route.
</dd>
<dt id="RouteProgress">
/sdk-for-flutter-navigate-navigation-routeprogress-class
</dt>
<dd>
  Contains all the relevant information on the user's progress along a route.
</dd>
<dt id="RouteProgressColors">
/sdk-for-flutter-navigate-navigation-routeprogresscolors-class
</dt>
<dd>
  This struct contains colors for the route progress visualization.
</dd>
<dt id="RouteProgressListener">
/sdk-for-flutter-navigate-navigation-routeprogresslistener-class
</dt>
<dd>
  This abstract class should be implemented in order to receive notifications
about the route progress from /sdk-for-flutter-navigate-navigation-navigator-class.
</dd>
<dt id="SafetyCameraWarning">
/sdk-for-flutter-navigate-navigation-safetycamerawarning-class
</dt>
<dd>
  A class that provides safety camera warning information.
</dd>
<dt id="SafetyCameraWarningListener">
/sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-class
</dt>
<dd>
  This abstract class
should be implemented in order to receive notifications on safety cameras.
</dd>
<dt id="SafetyCameraWarningOptions">
/sdk-for-flutter-navigate-navigation-safetycamerawarningoptions-class
</dt>
<dd>
  Safety camera warning options.
</dd>
<dt id="SchoolZoneWarning">
/sdk-for-flutter-navigate-navigation-schoolzonewarning-class
</dt>
<dd>
  A school zone warning which notifies about a school zone presence on road with a speed limit
different than the default speed limit applicable for cars.
</dd>
<dt id="SchoolZoneWarningListener">
/sdk-for-flutter-navigate-navigation-schoolzonewarninglistener-class
</dt>
<dd>
  This abstract class should be implemented in order to receive school zone warnings.
</dd>
<dt id="SchoolZoneWarningOptions">
/sdk-for-flutter-navigate-navigation-schoolzonewarningoptions-class
</dt>
<dd>
  School zone warning options.
</dd>
<dt id="SectionProgress">
/sdk-for-flutter-navigate-navigation-sectionprogress-class
</dt>
<dd>
  Indicates a user's progress along a /sdk-for-flutter-navigate-routing-section-class.
</dd>
<dt id="SpatialAudioCuePanning">
/sdk-for-flutter-navigate-navigation-spatialaudiocuepanning-class
</dt>
<dd>
  Use the /sdk-for-flutter-navigate-navigation-spatialaudiocuepanning-class to notify each of the azimuths which compose a spatial audio
trajectory along the audio cue.
</dd>
<dt id="SpatialNotificationDetails">
/sdk-for-flutter-navigate-navigation-spatialnotificationdetails-class
</dt>
<dd>
  This class provides all the information for a spatial text notification, including the
maneuver data and extra data which is required to set the direction of spatialization
of the audio cue.
</dd>
<dt id="SpatialTrajectoryData">
/sdk-for-flutter-navigate-navigation-spatialtrajectorydata-class
</dt>
<dd>
  This struct provides all the information regarding an angular panning element, including the panning angle
and whether or not it is the last element on the spatial audio trajectory.
</dd>
<dt id="SpeedBasedCameraBehavior">
/sdk-for-flutter-navigate-navigation-speedbasedcamerabehavior-class
</dt>
<dd>
  Use this class to follow the current location of the user, zooming in and out and changing
camera tilt according to the current speed.
</dd>
<dt id="SpeedBasedCameraBehaviorProfileValue">
/sdk-for-flutter-navigate-navigation-speedbasedcamerabehaviorprofilevalue-class
</dt>
<dd>
  A single profile value which indicates the speed range in which it applies to its zoom and
tilt configuration.
</dd>
<dt id="SpeedLimit">
/sdk-for-flutter-navigate-navigation-speedlimit-class
</dt>
<dd>
  Represents the speed limit of the current road.
</dd>
<dt id="SpeedLimitListener">
/sdk-for-flutter-navigate-navigation-speedlimitlistener-class
</dt>
<dd>
  This abstract class
should be implemented in order to receive the speed limit of the current road.
</dd>
<dt id="SpeedLimitOffset">
/sdk-for-flutter-navigate-navigation-speedlimitoffset-class
</dt>
<dd>
  A class that represents two separate speed limit offsets for higher and lower speed limits.
</dd>
<dt id="SpeedWarningListener">
/sdk-for-flutter-navigate-navigation-speedwarninglistener-class
</dt>
<dd>
  This abstract class should be implemented in order to receive notifications
when a speed limit on a road is exceeded or driving speed is restored back to normal.
</dd>
<dt id="SpeedWarningOptions">
/sdk-for-flutter-navigate-navigation-speedwarningoptions-class
</dt>
<dd>
  A class that contains all options to be used for the speed limit warnings.
</dd>
<dt id="TollBooth">
/sdk-for-flutter-navigate-navigation-tollbooth-class
</dt>
<dd>
  A class that provides information of a toll stop.
</dd>
<dt id="TollBoothLane">
/sdk-for-flutter-navigate-navigation-tollboothlane-class
</dt>
<dd>
  A class that provides information for a toll booth.
</dd>
<dt id="TollStop">
/sdk-for-flutter-navigate-navigation-tollstop-class
</dt>
<dd>
  A class that provides information for a toll stop with multiple toll booths.
</dd>
<dt id="TollStopWarningListener">
/sdk-for-flutter-navigate-navigation-tollstopwarninglistener-class
</dt>
<dd>
  This abstract class
should be implemented in order to receive information on the upcoming toll booth structure.
</dd>
<dt id="TrackingCameraBehavior">
/sdk-for-flutter-navigate-navigation-trackingcamerabehavior-class
</dt>
<dd>
  Use this class to follow a moving target.
</dd>
<dt id="TrackingCameraBehaviorFunctionalRoadClassZoomPolicyOptions">
/sdk-for-flutter-navigate-navigation-trackingcamerabehaviorfunctionalroadclasszoompolicyoptions-class
</dt>
<dd>
  Configuration for mapping functional road classes to zoom levels.
</dd>
<dt id="TrackingCameraBehaviorManeuverModeConfiguration">
/sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-class
</dt>
<dd>
  Configuration that defines how /sdk-for-flutter-navigate-navigation-trackingcamerabehavior-class reacts to nearby maneuvers.
</dd>
<dt id="TrackingCameraBehaviorManeuverRule">
/sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverrule-class
</dt>
<dd>
  Defines a single rule that determines how /sdk-for-flutter-navigate-navigation-trackingcamerabehavior-class reacts to nearby
maneuvers when the current position matches this rule.
</dd>
<dt id="TrackingCameraBehaviorManeuverRuleOptions">
/sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverruleoptions-class
</dt>
<dd>
  Defines a set of configurations specific to a /sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverrule-class.
</dd>
<dt id="TrackingCameraBehaviorManeuverZoomRange">
/sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverzoomrange-class
</dt>
<dd>
  Defines the bounds within which the zoom level is constrained when approaching a maneuver.
</dd>
<dt id="TrackingCameraBehaviorSpeedBasedZoomPolicyOptions">
/sdk-for-flutter-navigate-navigation-trackingcamerabehaviorspeedbasedzoompolicyoptions-class
</dt>
<dd>
  Configuration for computing zoom levels from speed thresholds defined per road classification.
</dd>
<dt id="TrackingCameraBehaviorSpeedThreshold">
/sdk-for-flutter-navigate-navigation-trackingcamerabehaviorspeedthreshold-class
</dt>
<dd>
  Defines a zoom level triggered when the vehicle reaches a specific speed.
</dd>
<dt id="TrackingCameraBehaviorZoomPolicy">
/sdk-for-flutter-navigate-navigation-trackingcamerabehaviorzoompolicy-class
</dt>
<dd>
  Defines zoom behavior in different policy settings.
</dd>
<dt id="TrafficMergeWarning">
/sdk-for-flutter-navigate-navigation-trafficmergewarning-class
</dt>
<dd>
  A class that provides warning for merging traffic.
</dd>
<dt id="TrafficMergeWarningListener">
/sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-class
</dt>
<dd>
  This abstract class
should be implemented in order to receive traffic merge warnings.
</dd>
<dt id="TrafficMergeWarningOptions">
/sdk-for-flutter-navigate-navigation-trafficmergewarningoptions-class
</dt>
<dd>
  A class that provides traffic merge warning options.
</dd>
<dt id="TrafficOnRouteColors">
/sdk-for-flutter-navigate-navigation-trafficonroutecolors-class
</dt>
<dd>
  This type contains colors used for the traffic with jam factor greater or equal to 4.0 on route
ahead of the current location visualization.
</dd>
<dt id="TruckRestrictionsWarningListener">
/sdk-for-flutter-navigate-navigation-truckrestrictionswarninglistener-class
</dt>
<dd>
  This abstract class
should be implemented in order to receive truck restriction warnings.
</dd>
<dt id="TruckRestrictionsWarningOptions">
/sdk-for-flutter-navigate-navigation-truckrestrictionswarningoptions-class
</dt>
<dd>
  Truck restrictions warning options.
</dd>
<dt id="TruckRestrictionWarning">
/sdk-for-flutter-navigate-navigation-truckrestrictionwarning-class
</dt>
<dd>
  Represents truck restrictions.
</dd>
<dt id="VisualNavigator">
/sdk-for-flutter-navigate-navigation-visualnavigator-class
</dt>
<dd>
  This class provides all functionality of /sdk-for-flutter-navigate-navigation-navigatorinterface-class.
</dd>
<dt id="VisualNavigatorColors">
/sdk-for-flutter-navigate-navigation-visualnavigatorcolors-class
</dt>
<dd>
  This class contains colors used by /sdk-for-flutter-navigate-navigation-visualnavigator-class to render
the route and the maneuver arrow visualization.
</dd>
<dt id="WarningNotificationDistances">
/sdk-for-flutter-navigate-navigation-warningnotificationdistances-class
</dt>
<dd>
  Distances for emitting warnings according to the timing profile.
</dd>
<dt id="WeightRestriction">
/sdk-for-flutter-navigate-navigation-weightrestriction-class
</dt>
<dd>
  Defines a weight restriction.
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="enums">
<h2>Enums</h2>
<dl>
<dt id="ArrivalNotificationOption">
/sdk-for-flutter-navigate-navigation-arrivalnotificationoption
</dt>
<dd>
  Indicates arrival point type to announce in maneuver notification.
</dd>
<dt id="AspectRatio">
/sdk-for-flutter-navigate-navigation-aspectratio
</dt>
<dd>
  The aspect ratio of the image.
</dd>
<dt id="AutomotiveCameraBehaviorActiveCameraType">
/sdk-for-flutter-navigate-navigation-automotivecamerabehavioractivecameratype
</dt>
<dd>
  Defines the type of camera currently handling camera updates.
</dd>
<dt id="AutomotiveCameraBehaviorOrientationMode">
/sdk-for-flutter-navigate-navigation-automotivecamerabehaviororientationmode
</dt>
<dd>
  Defines the visual presentation modes for the camera orientation.
</dd>
<dt id="BorderCrossingType">
/sdk-for-flutter-navigate-navigation-bordercrossingtype
</dt>
<dd>
  Type of a border crossing given in a /sdk-for-flutter-navigate-navigation-bordercrossingwarning-class.
</dd>
<dt id="DimensionRestrictionType">
/sdk-for-flutter-navigate-navigation-dimensionrestrictiontype
</dt>
<dd>
  Defines the type of a dimension restriction.
</dd>
<dt id="DirectionInformationUsageOption">
/sdk-for-flutter-navigate-navigation-directioninformationusageoption
</dt>
<dd>
  Indicates the option of direction information included in the notification.
</dd>
<dt id="DistanceType">
/sdk-for-flutter-navigate-navigation-distancetype
</dt>
<dd>
<strong>Note:</strong> The distance types are being given for warnings at distances which can be configured
via options specific for each warner.
</dd>
<dt id="DividerMarker">
/sdk-for-flutter-navigate-navigation-dividermarker
</dt>
<dd>
  Indicates the divider between the lanes.
</dd>
<dt id="GeneralWarningRoadSignType">
/sdk-for-flutter-navigate-navigation-generalwarningroadsigntype
</dt>
<dd>
  Type of a general warning that a road sign represents.
</dd>
<dt id="LaneDirection">
/sdk-for-flutter-navigate-navigation-lanedirection
</dt>
<dd>
  This enum defines the lane direction.
</dd>
<dt id="LaneRecommendationState">
/sdk-for-flutter-navigate-navigation-lanerecommendationstate
</dt>
<dd>
  Indicates whether this lane leads to the next maneuvers or not.
</dd>
<dt id="ManeuverNotificationType">
/sdk-for-flutter-navigate-navigation-maneuvernotificationtype
</dt>
<dd>
  Indicates the type of the maneuver notification.
</dd>
<dt id="MilestoneStatus">
/sdk-for-flutter-navigate-navigation-milestonestatus
</dt>
<dd>
  This enum represents the status of the /sdk-for-flutter-navigate-navigation-milestone-class.
</dd>
<dt id="MilestoneType">
/sdk-for-flutter-navigate-navigation-milestonetype
</dt>
<dd>
  This enum represents the type of the /sdk-for-flutter-navigate-navigation-milestone-class.
</dd>
<dt id="NaturalGuidanceType">
/sdk-for-flutter-navigate-navigation-naturalguidancetype
</dt>
<dd>
  Indicates the type of the natural guidance element.
</dd>
<dt id="NotificationFormatOption">
/sdk-for-flutter-navigate-navigation-notificationformatoption
</dt>
<dd>
  Indicates the formatting option of phoneme included in the notification.
</dd>
<dt id="RoadClassification">
/sdk-for-flutter-navigate-navigation-roadclassification
</dt>
<dd>
  Classification of the surrounding road environment.
</dd>
<dt id="RoadSignCategory">
/sdk-for-flutter-navigate-navigation-roadsigncategory
</dt>
<dd>
  Road sign category defining a general purpose of the sign.
</dd>
<dt id="RoadSignType">
/sdk-for-flutter-navigate-navigation-roadsigntype
</dt>
<dd>
  A road sign type classifying road signs that can appear along a road.
</dd>
<dt id="RoadSignVehicleType">
/sdk-for-flutter-navigate-navigation-roadsignvehicletype
</dt>
<dd>
  Vehicle type for which a road sign is applicable.
</dd>
<dt id="SafetyCameraType">
/sdk-for-flutter-navigate-navigation-safetycameratype
</dt>
<dd>
  Indicates the type of the safety camera.
</dd>
<dt id="SpeedWarningStatus">
/sdk-for-flutter-navigate-navigation-speedwarningstatus
</dt>
<dd>
  This enum represents the status of the speed warning feature.
</dd>
<dt id="TextNotificationType">
/sdk-for-flutter-navigate-navigation-textnotificationtype
</dt>
<dd>
  Different types of text notifications.
</dd>
<dt id="TimingProfile">
/sdk-for-flutter-navigate-navigation-timingprofile
</dt>
<dd>
  Identifies the timing profile used for emitting notifications and warnings.
</dd>
<dt id="TollCollectionMethod">
/sdk-for-flutter-navigate-navigation-tollcollectionmethod
</dt>
<dd>
  Available payment methods.
</dd>
<dt id="TrafficMergeRoadType">
/sdk-for-flutter-navigate-navigation-trafficmergeroadtype
</dt>
<dd>
  The type of road which is merging onto the current road.
</dd>
<dt id="TrafficMergeSide">
/sdk-for-flutter-navigate-navigation-trafficmergeside
</dt>
<dd>
  The side from where the merging traffic is joining with the current highway.
</dd>
<dt id="WarningType">
/sdk-for-flutter-navigate-navigation-warningtype
</dt>
<dd>
  Identifies the warning type.
</dd>
<dt id="WeatherType">
/sdk-for-flutter-navigate-navigation-weathertype
</dt>
<dd>
  Weather type attached to <code>RoadSignWarning</code> or <code>VehicleRestriction.Condition</code> which limits the conditions for which the sign is applicable.
</dd>
<dt id="WeightRestrictionType">
/sdk-for-flutter-navigate-navigation-weightrestrictiontype
</dt>
<dd>
  Defines the type of a weight restriction.
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="typedefs">
<h2>Typedefs</h2>
<dl>
<dt class="callable" id="SpatialAudioCuePanningspatialAzimuthStarted">
/sdk-for-flutter-navigate-navigation-spatialaudiocuepanningspatialazimuthstarted
= void Function(/sdk-for-flutter-navigate-navigation-spatialtrajectorydata-class spatialTrajectoryData)

</dt>
<dd>
    Called once <code>startAngularPanning()</code> starts.
    

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
<li class="self-crumb">navigation.dart</li>
</ol>
<h5>here_sdk package</h5>
<ol>
<li class="section-title">Libraries</li>
<li>/sdk-for-flutter-navigate-animation-animation-library</li>
<li>/sdk-for-flutter-navigate-core-core-library</li>
<li>/sdk-for-flutter-navigate-core-engine-core-engine-library</li>
<li>/sdk-for-flutter-navigate-core-errors-core-errors-library</li>
<li>/sdk-for-flutter-navigate-core-threading-core-threading-library</li>
<li>/sdk-for-flutter-navigate-electronic-horizon-electronic-horizon-library</li>
<li>/sdk-for-flutter-navigate-ev-ev-library</li>
<li>/sdk-for-flutter-navigate-gestures-gestures-library</li>
<li>/sdk-for-flutter-navigate-location-location-library</li>
<li>/sdk-for-flutter-navigate-mapdata-mapdata-library</li>
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li>/sdk-for-flutter-navigate-maploader-remote-connection-maploader-remote-connection-library</li>
<li>/sdk-for-flutter-navigate-mapmatcher-mapmatcher-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-datasource-mapview-datasource-library</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-prefetcher-prefetcher-library</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li>/sdk-for-flutter-navigate-traffic-traffic-library</li>
<li>/sdk-for-flutter-navigate-trafficawarenavigation-trafficawarenavigation-library</li>
<li>/sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-library</li>
<li>/sdk-for-flutter-navigate-transport-transport-library</li>
<li>/sdk-for-flutter-navigate-venue-venue-library</li>
<li>/sdk-for-flutter-navigate-venue-control-venue-control-library</li>
<li>/sdk-for-flutter-navigate-venue-data-venue-data-library</li>
<li>/sdk-for-flutter-navigate-venue-routing-venue-routing-library</li>
<li>/sdk-for-flutter-navigate-venue-service-venue-service-library</li>
<li>/sdk-for-flutter-navigate-venue-style-venue-style-library</li>
<li>/sdk-for-flutter-navigate-warner-warner-library</li>
</ol>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
<h5>navigation library</h5>
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>



</div>
`
}</HTMLBlock>
