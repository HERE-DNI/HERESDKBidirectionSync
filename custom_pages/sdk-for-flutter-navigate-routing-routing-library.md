---
title: "routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-routing-library"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- routing-library.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="" data-below-sidebar="routing/routing-library-sidebar.html">

<div>

# <span class="kind-library">routing</span> library

</div>

## Classes

<span class="name"><a href="sdk-for-flutter-navigate-routing-agency-class">Agency</a></span>  
Holds all the agency information.

<span class="name"><a href="sdk-for-flutter-navigate-routing-allowoptions-class">AllowOptions</a></span>  
The options explicitly allowed by user for route calculations.

<span class="name"><a href="sdk-for-flutter-navigate-routing-attribution-class">Attribution</a></span>  
Holds all the data on a URL address to an external resource.

<span class="name"><a href="sdk-for-flutter-navigate-routing-avoidanceoptions-class">AvoidanceOptions</a></span>  
The options to specify restrictions for route calculations.

<span class="name"><a href="sdk-for-flutter-navigate-routing-avoidboundingboxareaoptions-class">AvoidBoundingBoxAreaOptions</a></span>  
The options to specify rectangular shape which routes must not cross.

<span class="name"><a href="sdk-for-flutter-navigate-routing-avoidcorridorareaoptions-class">AvoidCorridorAreaOptions</a></span>  
Area of corridor shape which routes must not cross and exceptions for this area.

<span class="name"><a href="sdk-for-flutter-navigate-routing-avoidpolygonareaoptions-class">AvoidPolygonAreaOptions</a></span>  
The options to specify polygon shape which routes must not cross.

<span class="name"><a href="sdk-for-flutter-navigate-routing-batteryspecifications-class">BatterySpecifications</a></span>  
Parameters related to the electric vehicle's battery.

<span class="name deprecated"><a href="sdk-for-flutter-navigate-routing-bicycleoptions-class" class="deprecated">BicycleOptions</a></span>  
All the options to specify how a bicycle route should be calculated.

<span class="name deprecated"><a href="sdk-for-flutter-navigate-routing-busoptions-class" class="deprecated">BusOptions</a></span>  
All the options to specify how a bus route should be calculated.

<span class="name deprecated"><a href="sdk-for-flutter-navigate-routing-caroptions-class" class="deprecated">CarOptions</a></span>  
All the options to specify how a car route should be calculated.

<span class="name"><a href="sdk-for-flutter-navigate-routing-chargingactiondetails-class">ChargingActionDetails</a></span>  
Parameters related to the electric vehicle's charging action.

<span class="name"><a href="sdk-for-flutter-navigate-routing-chargingconnectorattributes-class">ChargingConnectorAttributes</a></span>  
Details of the connector that is suggested to be used in the section's <a href="sdk-for-flutter-navigate-routing-postaction-class">PostAction</a>'s for charging.

<span class="name"><a href="sdk-for-flutter-navigate-routing-chargingstation-class">ChargingStation</a></span>  
Data for an electric vehicle charging station.

<span class="name"><a href="sdk-for-flutter-navigate-routing-chargingstop-class">ChargingStop</a></span>  
The options to specify a user-planned charging stop.

<span class="name"><a href="sdk-for-flutter-navigate-routing-dynamicspeedinfo-class">DynamicSpeedInfo</a></span>  
Provides estimated speed information.

<span class="name"><a href="sdk-for-flutter-navigate-routing-electricvehicleoptions-class">ElectricVehicleOptions</a></span>  
These options define the parameters of the electric vehicle.

<span class="name"><a href="sdk-for-flutter-navigate-routing-empiricalconsumptionmodel-class">EmpiricalConsumptionModel</a></span>  
This model defines a data-driven energy consumption model for electric vehicles.

<span class="name deprecated"><a href="sdk-for-flutter-navigate-routing-evcaroptions-class" class="deprecated">EVCarOptions</a></span>  
All the options to specify how a route for an electric car should be calculated.

<span class="name"><a href="sdk-for-flutter-navigate-routing-evconsumptionmodel-class">EVConsumptionModel</a></span>  
Parameters specific for the electric vehicle, which are then used to calculate energy consumption on a given route.

<span class="name"><a href="sdk-for-flutter-navigate-routing-evmobilityserviceproviderpreferences-class">EVMobilityServiceProviderPreferences</a></span>  
Defines preference level per known E-Mobility Service Provider.

<span class="name deprecated"><a href="sdk-for-flutter-navigate-routing-evtruckoptions-class" class="deprecated">EVTruckOptions</a></span>  
All the options to specify how a route for an electric truck should be calculated.

<span class="name"><a href="sdk-for-flutter-navigate-routing-fare-class">Fare</a></span>  
Holds all the fare data.

<span class="name"><a href="sdk-for-flutter-navigate-routing-farepassvalidityperiod-class">FarePassValidityPeriod</a></span>  
Specifies a temporal validity period for a pass

<span class="name"><a href="sdk-for-flutter-navigate-routing-fareprice-class">FarePrice</a></span>  
Price of a fare.

<span class="name"><a href="sdk-for-flutter-navigate-routing-indoorlevelchangedata-class">IndoorLevelChangeData</a></span>  
Represents the level change data for an indoor maneuver.

<span class="name"><a href="sdk-for-flutter-navigate-routing-indoormaneuver-class">IndoorManeuver</a></span>  
Represents a maneuver within an indoor section.

<span class="name"><a href="sdk-for-flutter-navigate-routing-indoorrouteplace-class">IndoorRoutePlace</a></span>  
Represents a place within an indoor route.

<span class="name"><a href="sdk-for-flutter-navigate-routing-indoorsectiondetails-class">IndoorSectionDetails</a></span>  
Provides additional details for an indoor <a href="sdk-for-flutter-navigate-routing-section-class">Section</a>.

<span class="name"><a href="sdk-for-flutter-navigate-routing-indoorspacedata-class">IndoorSpaceData</a></span>  
Represents the space data for an indoor maneuver.

<span class="name"><a href="sdk-for-flutter-navigate-routing-isoline-class">Isoline</a></span>  
Represents an isoline polygon around a center point.

<span class="name"><a href="sdk-for-flutter-navigate-routing-isolineoptions-class">IsolineOptions</a></span>  
Specifies options for isolines calculation.

<span class="name"><a href="sdk-for-flutter-navigate-routing-isolineoptionscalculation-class">IsolineOptionsCalculation</a></span>  
Specifies isoline parameters.

<span class="name"><a href="sdk-for-flutter-navigate-routing-isolineroutingengine-class">IsolineRoutingEngine</a></span>  
Use the IsolineRoutingEngine to calculate a reachable area from a center point.

<span class="name"><a href="sdk-for-flutter-navigate-routing-localizedroadnumber-class">LocalizedRoadNumber</a></span>  
Used to represent road number localized to specific language with optional direction and route type information.

<span class="name"><a href="sdk-for-flutter-navigate-routing-localizedroadnumbers-class">LocalizedRoadNumbers</a></span>  
The list of multiple names or titles for the same entity, possibly in different languages.

<span class="name"><a href="sdk-for-flutter-navigate-routing-maneuver-class">Maneuver</a></span>  
This class provides all the information for a maneuver.

<span class="name"><a href="sdk-for-flutter-navigate-routing-mapmatchedcoordinates-class">MapMatchedCoordinates</a></span>  
Information about the user defined coordinates and where they match to the map.

<span class="name"><a href="sdk-for-flutter-navigate-routing-maxaxlegroupweight-class">MaxAxleGroupWeight</a></span>  
`MaxAxleGroupWeight` contains all the restriction details violated by an axle group weight.

<span class="name"><a href="sdk-for-flutter-navigate-routing-maxspeedonsegment-class">MaxSpeedOnSegment</a></span>  
New base speed for a segment.

<span class="name"><a href="sdk-for-flutter-navigate-routing-offlineroutingengine-class">OfflineRoutingEngine</a></span>  
Use this class to calculate a route offline from A to B with a number of waypoints in between.

<span class="name"><a href="sdk-for-flutter-navigate-routing-offlineroutingengineoptions-class">OfflineRoutingEngineOptions</a></span>  
Options to configure offline routing engine.

<span class="name"><a href="sdk-for-flutter-navigate-routing-passthroughwaypoint-class">PassThroughWaypoint</a></span>  
This structure provides all the information for a passthrough waypoint.

<span class="name deprecated"><a href="sdk-for-flutter-navigate-routing-pedestrianoptions-class" class="deprecated">PedestrianOptions</a></span>  
All the options to specify how a pedestrian route should be calculated.

<span class="name"><a href="sdk-for-flutter-navigate-routing-physicalconsumptionmodel-class">PhysicalConsumptionModel</a></span>  
Defines the physical consumption model for electric vehicles, using vehicle-specific parameters to calculate energy consumption along a route.

<span class="name"><a href="sdk-for-flutter-navigate-routing-postaction-class">PostAction</a></span>  
An action that must be done after arrival, i.e.

<span class="name"><a href="sdk-for-flutter-navigate-routing-preaction-class">PreAction</a></span>  
An action that must be done prior to the section, i.e.

<span class="name deprecated"><a href="sdk-for-flutter-navigate-routing-privatebusoptions-class" class="deprecated">PrivateBusOptions</a></span>  
All the options to specify how a private bus route should be calculated.

<span class="name deprecated"><a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-class" class="deprecated">RefreshRouteOptions</a></span>  
The options to specify how to refresh an already calculated route identified by a <a href="sdk-for-flutter-navigate-routing-routehandle-class">RouteHandle</a>.

<span class="name"><a href="sdk-for-flutter-navigate-routing-refreshrouteparameters-class">RefreshRouteParameters</a></span>  
This class provides the necessary information for refreshing a route from a specific location on it.

<span class="name"><a href="sdk-for-flutter-navigate-routing-roadtexts-class">RoadTexts</a></span>  
Textual attributes of road.

<span class="name"><a href="sdk-for-flutter-navigate-routing-route-class">Route</a></span>  
A route is a path through a road network over which someone travels.

<span class="name"><a href="sdk-for-flutter-navigate-routing-routehandle-class">RouteHandle</a></span>  
Provides an opaque handle to the calculated <a href="sdk-for-flutter-navigate-routing-route-class">Route</a>.

<span class="name"><a href="sdk-for-flutter-navigate-routing-routelabel-class">RouteLabel</a></span>  
The main street name or road number for a route.

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeoffset-class">RouteOffset</a></span>  
Represents a specific location along the route.

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeoptions-class">RouteOptions</a></span>  
The options to specify how the route will be calculated.

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeplace-class">RoutePlace</a></span>  
The location information.

<span class="name"><a href="sdk-for-flutter-navigate-routing-routerailwaycrossing-class">RouteRailwayCrossing</a></span>  
Contains information about railway crossing.

<span class="name"><a href="sdk-for-flutter-navigate-routing-routestop-class">RouteStop</a></span>  
Route stop that should be used together with import route functionality.

<span class="name"><a href="sdk-for-flutter-navigate-routing-routetextoptions-class">RouteTextOptions</a></span>  
Specify how textual output should be provided.

<span class="name"><a href="sdk-for-flutter-navigate-routing-routingconnectionsettings-class">RoutingConnectionSettings</a></span>  
Defines the settings for the retry logic when connecting to the HERE routing backend.

<span class="name"><a href="sdk-for-flutter-navigate-routing-routingengine-class">RoutingEngine</a></span>  
Use the RoutingEngine to calculate a route from A to B with a number of waypoints in between.

<span class="name"><a href="sdk-for-flutter-navigate-routing-routinginterface-class">RoutingInterface</a></span>  
Provides the abstract class for the online and offline routing engines.

<span class="name"><a href="sdk-for-flutter-navigate-routing-routingoptions-class">RoutingOptions</a></span>  
The options defines how a route should be calculated.

<span class="name deprecated"><a href="sdk-for-flutter-navigate-routing-scooteroptions-class" class="deprecated">ScooterOptions</a></span>  
All the options to specify how a scooter route should be calculated.

<span class="name"><a href="sdk-for-flutter-navigate-routing-section-class">Section</a></span>  
A section is a part of the route between two stopovers.

<span class="name"><a href="sdk-for-flutter-navigate-routing-sectionnotice-class">SectionNotice</a></span>  
Explains an issue encountered in a <a href="sdk-for-flutter-navigate-routing-section-class">Section</a>.

<span class="name"><a href="sdk-for-flutter-navigate-routing-segmentreference-class">SegmentReference</a></span>  
Reference to a segment id with a travel direction.

<span class="name"><a href="sdk-for-flutter-navigate-routing-signpost-class">Signpost</a></span>  
Signpost information.

<span class="name"><a href="sdk-for-flutter-navigate-routing-signpostlabel-class">SignpostLabel</a></span>  
Details of a signpost representing a particular direction or destination.

<span class="name"><a href="sdk-for-flutter-navigate-routing-span-class">Span</a></span>  
A span is a part of the <a href="sdk-for-flutter-navigate-routing-section-class">Section</a> which is traversable or navigable.

<span class="name deprecated"><a href="sdk-for-flutter-navigate-routing-taxioptions-class" class="deprecated">TaxiOptions</a></span>  
All the options to specify how a taxi route should be calculated.

<span class="name"><a href="sdk-for-flutter-navigate-routing-textusageoptions-class">TextUsageOptions</a></span>  
Specify whether the text should be used when generating notification.

<span class="name"><a href="sdk-for-flutter-navigate-routing-toll-class">Toll</a></span>  
This struct presents all the data for a toll.

<span class="name"><a href="sdk-for-flutter-navigate-routing-tollfare-class">TollFare</a></span>  
This struct presents all the fare data for a toll.

<span class="name"><a href="sdk-for-flutter-navigate-routing-tollfarepass-class">TollFarePass</a></span>  
<a href="sdk-for-flutter-navigate-routing-tollfare-class">TollFare</a> multi-travel pass characteristics.

<span class="name"><a href="sdk-for-flutter-navigate-routing-tolloptions-class">TollOptions</a></span>  
The option to specify how the tolls should be calculated.

<span class="name"><a href="sdk-for-flutter-navigate-routing-trafficincidentonroute-class">TrafficIncidentOnRoute</a></span>  
Traffic incidents on a route.

<span class="name"><a href="sdk-for-flutter-navigate-routing-trafficonroute-class">TrafficOnRoute</a></span>  
Traffic information on a route.

<span class="name"><a href="sdk-for-flutter-navigate-routing-trafficonsection-class">TrafficOnSection</a></span>  
Traffic information on a section.

<span class="name"><a href="sdk-for-flutter-navigate-routing-trafficonspan-class">TrafficOnSpan</a></span>  
Traffic information of a span along a route.

<span class="name"><a href="sdk-for-flutter-navigate-routing-transitdeparture-class">TransitDeparture</a></span>  
This struct holds the transit departure or arrival information.

<span class="name"><a href="sdk-for-flutter-navigate-routing-transitincident-class">TransitIncident</a></span>  
A transit incident describes disruptions on the transit network.

<span class="name"><a href="sdk-for-flutter-navigate-routing-transitrouteoptions-class">TransitRouteOptions</a></span>  
All the options to specify how a public transit route should be calculated.

<span class="name"><a href="sdk-for-flutter-navigate-routing-transitroutingengine-class">TransitRoutingEngine</a></span>  
Use the TransitRoutingEngine to calculate a public transit route from A to B with a number of waypoints in between.

<span class="name"><a href="sdk-for-flutter-navigate-routing-transitsectiondetails-class">TransitSectionDetails</a></span>  
Gives the details of a transit section.

<span class="name"><a href="sdk-for-flutter-navigate-routing-transitstop-class">TransitStop</a></span>  
A transit stop between the departure and destination of a transit section.

<span class="name"><a href="sdk-for-flutter-navigate-routing-transittransport-class">TransitTransport</a></span>  
Holds all the transit transport information.

<span class="name"><a href="sdk-for-flutter-navigate-routing-transitwaypoint-class">TransitWaypoint</a></span>  
Represents a transit waypoint, used as input for transit route calculation.

<span class="name deprecated"><a href="sdk-for-flutter-navigate-routing-truckoptions-class" class="deprecated">TruckOptions</a></span>  
All the options to specify how a truck route should be calculated.

<span class="name"><a href="sdk-for-flutter-navigate-routing-vehiclerestrictionmaxweight-class">VehicleRestrictionMaxWeight</a></span>  
`VehicleRestrictionMaxWeight` contains max permitted weight during the trip, in kilograms, along with the specific type of maximum permitted weight restriction.

<span class="name"><a href="sdk-for-flutter-navigate-routing-violatedrestriction-class">ViolatedRestriction</a></span>  
`ViolatedRestriction` contains all the violated restriction details for the planned trip.

<span class="name"><a href="sdk-for-flutter-navigate-routing-violatedrestrictiondetails-class">ViolatedRestrictionDetails</a></span>  
Optional restriction details, contains additional information depending on the specific violation, zero or more member might be set.

<span class="name"><a href="sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a></span>  
Represents a waypoint, used as input for route calculation.

## Enums

<span class="name"><a href="sdk-for-flutter-navigate-routing-accessattributes">AccessAttributes</a></span>  
Types of access attributes.

<span class="name"><a href="sdk-for-flutter-navigate-routing-attributiontype">AttributionType</a></span>  
Attribution link type.

<span class="name"><a href="sdk-for-flutter-navigate-routing-chargingconnectortype">ChargingConnectorType</a></span>  
Available charging connector types.

<span class="name"><a href="sdk-for-flutter-navigate-routing-chargingsupplytype">ChargingSupplyType</a></span>  
Available charging supply types.

<span class="name"><a href="sdk-for-flutter-navigate-routing-farepassvalidityperiodtype">FarePassValidityPeriodType</a></span>  
Specifies validity periods.

<span class="name"><a href="sdk-for-flutter-navigate-routing-farepricetype">FarePriceType</a></span>  
Type of price represented by a <a href="sdk-for-flutter-navigate-routing-fareprice-class">FarePrice</a> object.

<span class="name"><a href="sdk-for-flutter-navigate-routing-farereason">FareReason</a></span>  
Reason for the cost.

<span class="name"><a href="sdk-for-flutter-navigate-routing-functionalroadclass">FunctionalRoadClass</a></span>  
Types of function road class.

<span class="name"><a href="sdk-for-flutter-navigate-routing-indoorlevelchangefeatures">IndoorLevelChangeFeatures</a></span>  
Indoor route features.

<span class="name"><a href="sdk-for-flutter-navigate-routing-indoormaneuveractions">IndoorManeuverActions</a></span>  
Defines the types of actions for indoor maneuvers.

<span class="name"><a href="sdk-for-flutter-navigate-routing-isolinecalculationmode">IsolineCalculationMode</a></span>  
Specifies how isoline calculation is optimized.

<span class="name"><a href="sdk-for-flutter-navigate-routing-isolinerangetype">IsolineRangeType</a></span>  
Specifies the type of one or more range values to be included in the isoline.

<span class="name"><a href="sdk-for-flutter-navigate-routing-localizedtextpreference">LocalizedTextPreference</a></span>  
Indicates the option of localized text usage.

<span class="name"><a href="sdk-for-flutter-navigate-routing-maneuveraction">ManeuverAction</a></span>  
Maneuver action type.

<span class="name"><a href="sdk-for-flutter-navigate-routing-matchsideofstreet">MatchSideOfStreet</a></span>  
Specifies how the location set by <a href="sdk-for-flutter-navigate-routing-waypoint-sideofstreethint">Waypoint.sideOfStreetHint</a> should be handled.

<span class="name"><a href="sdk-for-flutter-navigate-routing-noticeseverity">NoticeSeverity</a></span>  
Describes the impact a notice has on the resource to which the notice is attached.

<span class="name"><a href="sdk-for-flutter-navigate-routing-optimizationmode">OptimizationMode</a></span>  
Identifiers for different optimizations that can be used during the route calculation while trying to keep the quality of the route being calculated high.

<span class="name"><a href="sdk-for-flutter-navigate-routing-paymentmethod">PaymentMethod</a></span>  
Available payment methods.

<span class="name"><a href="sdk-for-flutter-navigate-routing-postactiontype">PostActionType</a></span>  
Identifies the action type.

<span class="name"><a href="sdk-for-flutter-navigate-routing-preactiontype">PreActionType</a></span>  
Identifies the action type.

<span class="name"><a href="sdk-for-flutter-navigate-routing-roadfeatures">RoadFeatures</a></span>  
Road features or states.

<span class="name"><a href="sdk-for-flutter-navigate-routing-routelabeltype">RouteLabelType</a></span>  
Identifies the type of the route label.

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeplacedirection">RoutePlaceDirection</a></span>  
Specifies the direction to make distinction between departure and arrival cases.

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeplacetype">RoutePlaceType</a></span>  
Identifies the route place type.

<span class="name"><a href="sdk-for-flutter-navigate-routing-routerailwaycrossingtype">RouteRailwayCrossingType</a></span>  
Identify possible type of route railway crossing.

<span class="name"><a href="sdk-for-flutter-navigate-routing-routingerror">RoutingError</a></span>  
Specifies possible errors that may result from the calculation of a route.

<span class="name"><a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
Notice codes which point the issues encountered during processing of a <a href="sdk-for-flutter-navigate-routing-section-class">Section</a>.

<span class="name"><a href="sdk-for-flutter-navigate-routing-sectiontransportmode">SectionTransportMode</a></span>  
Specifies the <a href="sdk-for-flutter-navigate-routing-section-class">Section</a> mode of transport.

<span class="name"><a href="sdk-for-flutter-navigate-routing-sideofdestination">SideOfDestination</a></span>  
Specifies the side of street on which the destination is located.

<span class="name"><a href="sdk-for-flutter-navigate-routing-streetattributes">StreetAttributes</a></span>  
Types of street attributes.

<span class="name"><a href="sdk-for-flutter-navigate-routing-tolloptionsemissiontype">TollOptionsEmissionType</a></span>  
Supported options of emission type

<span class="name"><a href="sdk-for-flutter-navigate-routing-tolloptionsvehiclecategory">TollOptionsVehicleCategory</a></span>  
Supported options of vehicle category for toll calculation.

<span class="name"><a href="sdk-for-flutter-navigate-routing-trafficoptimizationmode">TrafficOptimizationMode</a></span>  
Traffic optimization mode that defines whether and what kind of traffic information should be considered during route calculation.

<span class="name"><a href="sdk-for-flutter-navigate-routing-transitdeparturestatus">TransitDepartureStatus</a></span>  
Status of a departure.

<span class="name"><a href="sdk-for-flutter-navigate-routing-transitincidenteffect">TransitIncidentEffect</a></span>  
Transit incident effect.

<span class="name"><a href="sdk-for-flutter-navigate-routing-transitincidenttype">TransitIncidentType</a></span>  
Transit incident type.

<span class="name"><a href="sdk-for-flutter-navigate-routing-transitmode">TransitMode</a></span>  
Public transit mode

<span class="name"><a href="sdk-for-flutter-navigate-routing-transitmodefilter">TransitModeFilter</a></span>  
Filtering mode for public transit.

<span class="name"><a href="sdk-for-flutter-navigate-routing-traveldirection">TravelDirection</a></span>  
Travel direction.

<span class="name"><a href="sdk-for-flutter-navigate-routing-vehiclerestrictionmaxweighttype">VehicleRestrictionMaxWeightType</a></span>  
This enum represents the specific type of the maximum permitted weight restriction.

<span class="name"><a href="sdk-for-flutter-navigate-routing-walkattributes">WalkAttributes</a></span>  
Types of walk attributes.

<span class="name"><a href="sdk-for-flutter-navigate-routing-waypointtype">WaypointType</a></span>  
Defines if the waypoint is a stop over, or a hint for a desired polyline of a route.

<span class="name"><a href="sdk-for-flutter-navigate-routing-zonecategory">ZoneCategory</a></span>  
Identifies categories of zones which routes avoid going through when used in <a href="sdk-for-flutter-navigate-routing-avoidanceoptions-class">AvoidanceOptions</a>.

## Typedefs

<span class="name"><a href="sdk-for-flutter-navigate-routing-calculateisolinecallback">CalculateIsolineCallback</a></span><span class="signature"> <span class="returntype parameter">= void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-routingError" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-routingerror">RoutingError</a>?</span> <span class="parameter-name">routingError</span>, </span><span id="sdk-for-flutter-navigate-param-isolines" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-isoline-class">Isoline</a></span>\></span>?</span> <span class="parameter-name">isolines</span></span>)</span></span> </span>  
A function which is called by the RoutingEngine after isoline calculation has completed.

<span class="name"><a href="sdk-for-flutter-navigate-routing-calculateroutecallback">CalculateRouteCallback</a></span><span class="signature"> <span class="returntype parameter">= void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-routingError" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-routingerror">RoutingError</a>?</span> <span class="parameter-name">routingError</span>, </span><span id="sdk-for-flutter-navigate-param-routeList" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-route-class">Route</a></span>\></span>?</span> <span class="parameter-name">routeList</span></span>)</span></span> </span>  
A function which is called by the RoutingEngine after route calculation has completed.

<span class="name"><a href="sdk-for-flutter-navigate-routing-calculatetrafficonroutecallback">CalculateTrafficOnRouteCallback</a></span><span class="signature"> <span class="returntype parameter">= void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-routingError" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-routingerror">RoutingError</a>?</span> <span class="parameter-name">routingError</span>, </span><span id="sdk-for-flutter-navigate-param-trafficOnRoute" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-trafficonroute-class">TrafficOnRoute</a>?</span> <span class="parameter-name">trafficOnRoute</span></span>)</span></span> </span>  
A function which is called by the RoutingEngine after route traffic calculation has completed.

</div>

<!-- /.main-content --> <!--/sidebar-offcanvas-right--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
