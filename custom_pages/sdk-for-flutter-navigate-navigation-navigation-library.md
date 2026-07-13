---
title: "navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-navigation-library"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- navigation-library.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="" data-below-sidebar="navigation/navigation-library-sidebar.html">

<div>

# <span class="kind-library">navigation</span> library

</div>

## Classes

<span class="name"><a href="sdk-for-flutter-navigate-navigation-areacamerabehavior-class">AreaCameraBehavior</a></span>  
Use this class to show an overview of geo points.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-automotivecamerabehavior-class">AutomotiveCameraBehavior</a></span>  
Provides a high-level camera controller for automotive navigation that manages both tracking and area camera behaviors.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-bordercrossingwarning-class">BorderCrossingWarning</a></span>  
A border crossing.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-bordercrossingwarninglistener-class">BorderCrossingWarningListener</a></span>  
This abstract class should be implemented in order to receive border crossing warnings for country and state borders.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-bordercrossingwarningoptions-class">BorderCrossingWarningOptions</a></span>  
Border crossing warning options.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-camerabehavior-class">CameraBehavior</a></span>  
Abstract class used to change implement different camera behaviors.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceview-class">CurrentSituationLaneAssistanceView</a></span>  
A class that provides current situation lane assistance view information for the street at the current location.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceviewlistener-class">CurrentSituationLaneAssistanceViewListener</a></span>  
This abstract class should be implemented in order to receive notifications on <a href="sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceview-class">CurrentSituationLaneAssistanceView</a>.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-currentsituationlaneview-class">CurrentSituationLaneView</a></span>  
A class that provides current situation lane assistance view information for the street at the current position of a single lane.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-custompanningdata-class">CustomPanningData</a></span>  
This class contains all the information regarding the next angular panning element, including a new estimated audio cue duration, and a new set of initial and sweep angular angle, allowing the customization of the spatial audio trajectories for any type of notification, such as speed or merge warners, maneuvers or even roundabouts notifications.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-dangerzonewarning-class">DangerZoneWarning</a></span>  
Represents danger zones.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-dangerzonewarninglistener-class">DangerZoneWarningListener</a></span>  
This abstract class should be implemented in order to receive notifications about the Danger zones.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-destinationreachedlistener-class">DestinationReachedListener</a></span>  
This abstract class should be implemented in order to receive notifications from this class about the arrival at the destination.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-dimensionrestriction-class">DimensionRestriction</a></span>  
Defines a dimension restriction.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-dynamiccamerabehavior-class">DynamicCameraBehavior</a></span>  
Use this class to follow the current location of the user: The camera will look at the target location that was fed into the navigator instance, gradually zooming in as the user approaches each maneuver and zooming out after the user passes them.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-environmentalzonewarning-class">EnvironmentalZoneWarning</a></span>  
Represents Environmental zones.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-environmentalzonewarninglistener-class">EnvironmentalZoneWarningListener</a></span>  
This abstract class should be implemented in order to receive notifications about the environmental zones.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-eventtext-class">EventText</a></span>  
Contains all the information regarding the next text announcement.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-eventtextlistener-class">EventTextListener</a></span>  
This abstract class should be implemented in order to receive notifications when text notifications are available from <a href="sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-eventtextoptions-class">EventTextOptions</a></span>  
Text notifications options.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-fixedcamerabehavior-class">FixedCameraBehavior</a></span>  
Use this class to follow the current location of the user: The camera will permanently look at the target location that was fed into the navigator instance.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-gpxdocument-class">GPXDocument</a></span>  
Use the GPXDocument to load the GPX file.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-gpxoptions-class">GPXOptions</a></span>  
Options used when reading the GPX file.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-gpxtrack-class">GPXTrack</a></span>  
Single track from the <a href="sdk-for-flutter-navigate-navigation-gpxdocument-class">GPXDocument</a>.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-gpxtrackwriter-class">GPXTrackWriter</a></span>  
Writes GPX track points to <a href="sdk-for-flutter-navigate-navigation-gpxtrack-class">GPXTrack</a>.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-interpolatedlocationlistener-class">InterpolatedLocationListener</a></span>  
This abstract class should be implemented in order to receive interpolated locations.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-class">JunctionViewLaneAssistance</a></span>  
A class that provides lane assistance information for the next complex junction in order to keep following the route.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-junctionviewlaneassistancelistener-class">JunctionViewLaneAssistanceListener</a></span>  
This abstract class should be implemented in order to receive notifications on <a href="sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-class">JunctionViewLaneAssistance</a>.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lane-class">Lane</a></span>  
A class that provides information for a lane.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-laneaccess-class">LaneAccess</a></span>  
A class which identifies the vehicle type(s) allowed to access a lane.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lanedirectioncategory-class">LaneDirectionCategory</a></span>  
Indicates the directions of a lane.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lanemarkings-class">LaneMarkings</a></span>  
A class that provides information for the lane markings.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lanetype-class">LaneType</a></span>  
A class that provides information on the available lane properties.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-locationsimulator-class">LocationSimulator</a></span>  
Use the `LocationSimulator` to generate locations along a route or a GPX document.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-locationsimulatoroptions-class">LocationSimulatorOptions</a></span>  
Options to specify how the location simulator will behave.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lowspeedzonewarning-class">LowSpeedZoneWarning</a></span>  
A class that provides low speed zone.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lowspeedzonewarninglistener-class">LowSpeedZoneWarningListener</a></span>  
This abstract class should be implemented in order to receive low speed zone warnings.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-maneuvernotificationdetails-class">ManeuverNotificationDetails</a></span>  
This class provides the information regarding the next maneuver to be triggered

<span class="name"><a href="sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-class">ManeuverNotificationOptions</a></span>  
A class containing all options to be used when generating maneuver notifications.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtimingoptions-class">ManeuverNotificationTimingOptions</a></span>  
A class defining timing and distance thresholds for maneuver notifications.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-maneuverprogress-class">ManeuverProgress</a></span>  
Indicates a user's progress to a <a href="sdk-for-flutter-navigate-routing-maneuver-class">Maneuver</a>.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-class">ManeuverViewLaneAssistance</a></span>  
A class that provides lane assistance information for the next maneuver(s).

<span class="name"><a href="sdk-for-flutter-navigate-navigation-maneuverviewlaneassistancelistener-class">ManeuverViewLaneAssistanceListener</a></span>  
This abstract class should be implemented in order to receive notifications on <a href="sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-class">ManeuverViewLaneAssistance</a>.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-mapmatchedlocation-class">MapMatchedLocation</a></span>  
Describes a map-matched location in the world at a given time.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-milestone-class">Milestone</a></span>  
Represents information about the waypoints along the route.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-milestonestatuslistener-class">MilestoneStatusListener</a></span>  
This abstract class should be implemented in order to receive notifications from this class about the arrival at each <a href="sdk-for-flutter-navigate-navigation-milestone-class">Milestone</a> or missing it.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigablelocation-class">NavigableLocation</a></span>  
Contains all the relevant information on the current location.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigablelocationlistener-class">NavigableLocationListener</a></span>  
This abstract class should be implemented in order to receive notifications about the current location from <a href="sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a></span>  
This class provides the basic navigation functionality.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-class">NavigatorInterface</a></span>  
This abstract class provides the basic functionality needed to run a navigation session.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-offroaddestinationreachedlistener-class">OffRoadDestinationReachedListener</a></span>  
This abstract class should be implemented in order to receive notifications from this class about the arrival at the off-road destination.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-offroadprogress-class">OffRoadProgress</a></span>  
Represents the information needed to help the users to reach their off-road destination.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-offroadprogresslistener-class">OffRoadProgressListener</a></span>  
This abstract class should be implemented in order to receive notifications about the current off-road location from <a href="sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-postactionlistener-class">PostActionListener</a></span>  
This abstract class should be implemented in order to receive post action notifications.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-railwaycrossingwarning-class">RailwayCrossingWarning</a></span>  
A class that provides railway crossing.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-class">RailwayCrossingWarningListener</a></span>  
This abstract class should be implemented in order to receive railway crossing warnings.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-realisticviewrasterimage-class">RealisticViewRasterImage</a></span>  
A realistic view.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-realisticviewvectorimage-class">RealisticViewVectorImage</a></span>  
A realistic view of a junction.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-class">RealisticViewWarning</a></span>  
A realistic view notification.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-class">RealisticViewWarningListener</a></span>  
This abstract class should be implemented in order to receive realistic view warnings.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-realisticviewwarningoptions-class">RealisticViewWarningOptions</a></span>  
Realistic view warning options.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadattributes-class">RoadAttributes</a></span>  
Road attributes, including usage and physical characteristics.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadattributeslistener-class">RoadAttributesListener</a></span>  
This abstract class should be implemented in order to receive attributes of the current road.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadsign-class">RoadSign</a></span>  
Describes a road sign.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadsignwarning-class">RoadSignWarning</a></span>  
A road sign.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadsignwarninglistener-class">RoadSignWarningListener</a></span>  
This abstract class should be implemented in order to receive road sign warnings.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadsignwarningoptions-class">RoadSignWarningOptions</a></span>  
A class that provides road sign warning options.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadtextslistener-class">RoadTextsListener</a></span>  
This abstract class should be implemented in order to receive textual attributes of the current road.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-routedeviation-class">RouteDeviation</a></span>  
Contains all the relevant information on a deviation from the route.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-routedeviationlistener-class">RouteDeviationListener</a></span>  
This abstract class should be implemented in order to receive notifications about route deviations from <a href="sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-routematchedlocation-class">RouteMatchedLocation</a></span>  
Represents a location matched to a specific position on a navigation route.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-routeprogress-class">RouteProgress</a></span>  
Contains all the relevant information on the user's progress along a route.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-routeprogresscolors-class">RouteProgressColors</a></span>  
This struct contains colors for the route progress visualization.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-routeprogresslistener-class">RouteProgressListener</a></span>  
This abstract class should be implemented in order to receive notifications about the route progress from <a href="sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-safetycamerawarning-class">SafetyCameraWarning</a></span>  
A class that provides safety camera warning information.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-class">SafetyCameraWarningListener</a></span>  
This abstract class should be implemented in order to receive notifications on safety cameras.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-safetycamerawarningoptions-class">SafetyCameraWarningOptions</a></span>  
Safety camera warning options.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-schoolzonewarning-class">SchoolZoneWarning</a></span>  
A school zone warning which notifies about a school zone presence on road with a speed limit different than the default speed limit applicable for cars.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-schoolzonewarninglistener-class">SchoolZoneWarningListener</a></span>  
This abstract class should be implemented in order to receive school zone warnings.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-schoolzonewarningoptions-class">SchoolZoneWarningOptions</a></span>  
School zone warning options.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-sectionprogress-class">SectionProgress</a></span>  
Indicates a user's progress along a <a href="sdk-for-flutter-navigate-routing-section-class">Section</a>.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-spatialaudiocuepanning-class">SpatialAudioCuePanning</a></span>  
Use the <a href="sdk-for-flutter-navigate-navigation-spatialaudiocuepanning-class">SpatialAudioCuePanning</a> to notify each of the azimuths which compose a spatial audio trajectory along the audio cue.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-spatialnotificationdetails-class">SpatialNotificationDetails</a></span>  
This class provides all the information for a spatial text notification, including the maneuver data and extra data which is required to set the direction of spatialization of the audio cue.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-spatialtrajectorydata-class">SpatialTrajectoryData</a></span>  
This struct provides all the information regarding an angular panning element, including the panning angle and whether or not it is the last element on the spatial audio trajectory.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-speedbasedcamerabehavior-class">SpeedBasedCameraBehavior</a></span>  
Use this class to follow the current location of the user, zooming in and out and changing camera tilt according to the current speed.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-speedbasedcamerabehaviorprofilevalue-class">SpeedBasedCameraBehaviorProfileValue</a></span>  
A single profile value which indicates the speed range in which it applies to its zoom and tilt configuration.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-speedlimit-class">SpeedLimit</a></span>  
Represents the speed limit of the current road.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-speedlimitlistener-class">SpeedLimitListener</a></span>  
This abstract class should be implemented in order to receive the speed limit of the current road.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-speedlimitoffset-class">SpeedLimitOffset</a></span>  
A class that represents two separate speed limit offsets for higher and lower speed limits.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-speedwarninglistener-class">SpeedWarningListener</a></span>  
This abstract class should be implemented in order to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-speedwarningoptions-class">SpeedWarningOptions</a></span>  
A class that contains all options to be used for the speed limit warnings.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-tollbooth-class">TollBooth</a></span>  
A class that provides information of a toll stop.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-tollboothlane-class">TollBoothLane</a></span>  
A class that provides information for a toll booth.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-tollstop-class">TollStop</a></span>  
A class that provides information for a toll stop with multiple toll booths.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-tollstopwarninglistener-class">TollStopWarningListener</a></span>  
This abstract class should be implemented in order to receive information on the upcoming toll booth structure.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehavior-class">TrackingCameraBehavior</a></span>  
Use this class to follow a moving target.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviorfunctionalroadclasszoompolicyoptions-class">TrackingCameraBehaviorFunctionalRoadClassZoomPolicyOptions</a></span>  
Configuration for mapping functional road classes to zoom levels.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-class">TrackingCameraBehaviorManeuverModeConfiguration</a></span>  
Configuration that defines how <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehavior-class">TrackingCameraBehavior</a> reacts to nearby maneuvers.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverrule-class">TrackingCameraBehaviorManeuverRule</a></span>  
Defines a single rule that determines how <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehavior-class">TrackingCameraBehavior</a> reacts to nearby maneuvers when the current position matches this rule.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverruleoptions-class">TrackingCameraBehaviorManeuverRuleOptions</a></span>  
Defines a set of configurations specific to a <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverrule-class">TrackingCameraBehaviorManeuverRule</a>.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverzoomrange-class">TrackingCameraBehaviorManeuverZoomRange</a></span>  
Defines the bounds within which the zoom level is constrained when approaching a maneuver.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviorspeedbasedzoompolicyoptions-class">TrackingCameraBehaviorSpeedBasedZoomPolicyOptions</a></span>  
Configuration for computing zoom levels from speed thresholds defined per road classification.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviorspeedthreshold-class">TrackingCameraBehaviorSpeedThreshold</a></span>  
Defines a zoom level triggered when the vehicle reaches a specific speed.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviorzoompolicy-class">TrackingCameraBehaviorZoomPolicy</a></span>  
Defines zoom behavior in different policy settings.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trafficmergewarning-class">TrafficMergeWarning</a></span>  
A class that provides warning for merging traffic.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-class">TrafficMergeWarningListener</a></span>  
This abstract class should be implemented in order to receive traffic merge warnings.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trafficmergewarningoptions-class">TrafficMergeWarningOptions</a></span>  
A class that provides traffic merge warning options.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trafficonroutecolors-class">TrafficOnRouteColors</a></span>  
This type contains colors used for the traffic with jam factor greater or equal to 4.0 on route ahead of the current location visualization.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-truckrestrictionswarninglistener-class">TruckRestrictionsWarningListener</a></span>  
This abstract class should be implemented in order to receive truck restriction warnings.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-truckrestrictionswarningoptions-class">TruckRestrictionsWarningOptions</a></span>  
Truck restrictions warning options.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-truckrestrictionwarning-class">TruckRestrictionWarning</a></span>  
Represents truck restrictions.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigator-class">VisualNavigator</a></span>  
This class provides all functionality of <a href="sdk-for-flutter-navigate-navigation-navigatorinterface-class">NavigatorInterface</a>.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-visualnavigatorcolors-class">VisualNavigatorColors</a></span>  
This class contains colors used by <a href="sdk-for-flutter-navigate-navigation-visualnavigator-class">VisualNavigator</a> to render the route and the maneuver arrow visualization.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-warningnotificationdistances-class">WarningNotificationDistances</a></span>  
Distances for emitting warnings according to the timing profile.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-weightrestriction-class">WeightRestriction</a></span>  
Defines a weight restriction.

## Enums

<span class="name"><a href="sdk-for-flutter-navigate-navigation-arrivalnotificationoption">ArrivalNotificationOption</a></span>  
Indicates arrival point type to announce in maneuver notification.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-aspectratio">AspectRatio</a></span>  
The aspect ratio of the image.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-automotivecamerabehavioractivecameratype">AutomotiveCameraBehaviorActiveCameraType</a></span>  
Defines the type of camera currently handling camera updates.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-automotivecamerabehaviororientationmode">AutomotiveCameraBehaviorOrientationMode</a></span>  
Defines the visual presentation modes for the camera orientation.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-bordercrossingtype">BorderCrossingType</a></span>  
Type of a border crossing given in a <a href="sdk-for-flutter-navigate-navigation-bordercrossingwarning-class">BorderCrossingWarning</a>.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-dimensionrestrictiontype">DimensionRestrictionType</a></span>  
Defines the type of a dimension restriction.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-directioninformationusageoption">DirectionInformationUsageOption</a></span>  
Indicates the option of direction information included in the notification.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType</a></span>  
**Note:** The distance types are being given for warnings at distances which can be configured via options specific for each warner.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-dividermarker">DividerMarker</a></span>  
Indicates the divider between the lanes.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-generalwarningroadsigntype">GeneralWarningRoadSignType</a></span>  
Type of a general warning that a road sign represents.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lanedirection">LaneDirection</a></span>  
This enum defines the lane direction.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lanerecommendationstate">LaneRecommendationState</a></span>  
Indicates whether this lane leads to the next maneuvers or not.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType</a></span>  
Indicates the type of the maneuver notification.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-milestonestatus">MilestoneStatus</a></span>  
This enum represents the status of the <a href="sdk-for-flutter-navigate-navigation-milestone-class">Milestone</a>.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-milestonetype">MilestoneType</a></span>  
This enum represents the type of the <a href="sdk-for-flutter-navigate-navigation-milestone-class">Milestone</a>.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-naturalguidancetype">NaturalGuidanceType</a></span>  
Indicates the type of the natural guidance element.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-notificationformatoption">NotificationFormatOption</a></span>  
Indicates the formatting option of phoneme included in the notification.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadclassification">RoadClassification</a></span>  
Classification of the surrounding road environment.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadsigncategory">RoadSignCategory</a></span>  
Road sign category defining a general purpose of the sign.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadsigntype">RoadSignType</a></span>  
A road sign type classifying road signs that can appear along a road.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadsignvehicletype">RoadSignVehicleType</a></span>  
Vehicle type for which a road sign is applicable.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-safetycameratype">SafetyCameraType</a></span>  
Indicates the type of the safety camera.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-speedwarningstatus">SpeedWarningStatus</a></span>  
This enum represents the status of the speed warning feature.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-textnotificationtype">TextNotificationType</a></span>  
Different types of text notifications.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-timingprofile">TimingProfile</a></span>  
Identifies the timing profile used for emitting notifications and warnings.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-tollcollectionmethod">TollCollectionMethod</a></span>  
Available payment methods.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trafficmergeroadtype">TrafficMergeRoadType</a></span>  
The type of road which is merging onto the current road.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trafficmergeside">TrafficMergeSide</a></span>  
The side from where the merging traffic is joining with the current highway.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType</a></span>  
Identifies the warning type.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-weathertype">WeatherType</a></span>  
Weather type attached to `RoadSignWarning` or `VehicleRestriction.Condition` which limits the conditions for which the sign is applicable.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-weightrestrictiontype">WeightRestrictionType</a></span>  
Defines the type of a weight restriction.

## Typedefs

<span class="name"><a href="sdk-for-flutter-navigate-navigation-spatialaudiocuepanningspatialazimuthstarted">SpatialAudioCuePanningspatialAzimuthStarted</a></span><span class="signature"> <span class="returntype parameter">= void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-spatialTrajectoryData" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-spatialtrajectorydata-class">SpatialTrajectoryData</a></span> <span class="parameter-name">spatialTrajectoryData</span></span>)</span></span> </span>  
Called once

    startAngularPanning()

starts.

</div>

<!-- /.main-content --> <!--/sidebar-offcanvas-right--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
