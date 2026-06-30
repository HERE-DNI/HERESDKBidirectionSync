---
title: "com.here.sdk.routing (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-package-summary"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- package-summary.html -->












<div class="package-signature">package <span class="element-name">com.here.sdk.routing</span></div>
<section class="summary">
<ul class="summary-list">
<li>
<div id="class-summary">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="class-summary.tabpanel" aria-selected="true" class="active-table-tab" id="class-summary-tab0" onclick="show('class-summary', 'class-summary', 2)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Classes and Interfaces</button><button aria-controls="class-summary.tabpanel" aria-selected="false" class="table-tab" id="class-summary-tab1" onclick="show('class-summary', 'class-summary-tab1', 2)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Interfaces</button><button aria-controls="class-summary.tabpanel" aria-selected="false" class="table-tab" id="class-summary-tab2" onclick="show('class-summary', 'class-summary-tab2', 2)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Classes</button><button aria-controls="class-summary.tabpanel" aria-selected="false" class="table-tab" id="class-summary-tab3" onclick="show('class-summary', 'class-summary-tab3', 2)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Enum Classes</button></div>
<div aria-labelledby="class-summary-tab0" id="class-summary.tabpanel" role="tabpanel">
<div class="summary-table two-column-summary">
<div class="table-header col-first">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-accessattributes" title="enum class in com.here.sdk.routing">AccessAttributes</a></div>
<div class="col-last even-row-color class-summary class-summary-tab3">
<div class="block">Types of access attributes.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-agency" title="class in com.here.sdk.routing">Agency</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Holds all the agency information.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-allowoptions" title="class in com.here.sdk.routing">AllowOptions</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">The options explicitly allowed by user for route calculations.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-attribution" title="class in com.here.sdk.routing">Attribution</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Holds all the data on a URL address to an external resource.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-attributiontype" title="enum class in com.here.sdk.routing">AttributionType</a></div>
<div class="col-last even-row-color class-summary class-summary-tab3">
<div class="block">Attribution link type.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-avoidanceoptions" title="class in com.here.sdk.routing">AvoidanceOptions</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">The options to specify restrictions for route calculations.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-avoidboundingboxareaoptions" title="class in com.here.sdk.routing">AvoidBoundingBoxAreaOptions</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">The options to specify rectangular shape which routes must not cross.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-avoidcorridorareaoptions" title="class in com.here.sdk.routing">AvoidCorridorAreaOptions</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Area of corridor shape which routes must not cross and exceptions for this area.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-avoidpolygonareaoptions" title="class in com.here.sdk.routing">AvoidPolygonAreaOptions</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">The options to specify polygon shape which routes must not cross.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-batteryspecifications" title="class in com.here.sdk.routing">BatterySpecifications</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Parameters related to the electric vehicle's battery.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-bicycleoptions" title="class in com.here.sdk.routing">BicycleOptions</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">Deprecated.
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-busoptions" title="class in com.here.sdk.routing">BusOptions</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">Deprecated.
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab1"><a href="sdk-for-android-explore-com-here-sdk-routing-calculateisolinecallback" title="interface in com.here.sdk.routing">CalculateIsolineCallback</a></div>
<div class="col-last even-row-color class-summary class-summary-tab1">
<div class="block">A function which is called by the RoutingEngine after isoline calculation has completed.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab1"><a href="sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab1">
<div class="block">A function which is called by the RoutingEngine after route calculation has completed.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab1"><a href="sdk-for-android-explore-com-here-sdk-routing-calculatetrafficonroutecallback" title="interface in com.here.sdk.routing">CalculateTrafficOnRouteCallback</a></div>
<div class="col-last even-row-color class-summary class-summary-tab1">
<div class="block">A function which is called by the RoutingEngine after route traffic calculation has completed.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-caroptions" title="class in com.here.sdk.routing">CarOptions</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">Deprecated.
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-chargingactiondetails" title="class in com.here.sdk.routing">ChargingActionDetails</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Parameters related to the electric vehicle's charging action.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-chargingconnectorattributes" title="class in com.here.sdk.routing">ChargingConnectorAttributes</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Details of the connector that is suggested to be used in the section's
 <a href="sdk-for-android-explore-com-here-sdk-routing-postaction" title="class in com.here.sdk.routing"><code>PostAction</code></a>'s for charging.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-chargingconnectortype" title="enum class in com.here.sdk.routing">ChargingConnectorType</a></div>
<div class="col-last even-row-color class-summary class-summary-tab3">
<div class="block">Available charging connector types.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-chargingstation" title="class in com.here.sdk.routing">ChargingStation</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Data for an electric vehicle charging station.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-chargingstop" title="class in com.here.sdk.routing">ChargingStop</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">The options to specify a user-planned charging stop.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-chargingsupplytype" title="enum class in com.here.sdk.routing">ChargingSupplyType</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Available charging supply types.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-dynamicspeedinfo" title="class in com.here.sdk.routing">DynamicSpeedInfo</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Provides estimated speed information.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-electricvehicleoptions" title="class in com.here.sdk.routing">ElectricVehicleOptions</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">These options define the parameters of the electric vehicle.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-empiricalconsumptionmodel" title="class in com.here.sdk.routing">EmpiricalConsumptionModel</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">This model defines a data-driven energy consumption model for electric vehicles.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-evcaroptions" title="class in com.here.sdk.routing">EVCarOptions</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">Deprecated.
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-evconsumptionmodel" title="class in com.here.sdk.routing">EVConsumptionModel</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Parameters specific for the electric vehicle, which are then used to calculate
 energy consumption on a given route.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-evmobilityserviceproviderpreferences" title="class in com.here.sdk.routing">EVMobilityServiceProviderPreferences</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Defines preference level per known E-Mobility Service Provider.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-evtruckoptions" title="class in com.here.sdk.routing">EVTruckOptions</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">Deprecated.
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-fare" title="class in com.here.sdk.routing">Fare</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Holds all the fare data.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-farepassvalidityperiod" title="class in com.here.sdk.routing">FarePassValidityPeriod</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Specifies a temporal validity period for a pass</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-farepassvalidityperiodtype" title="enum class in com.here.sdk.routing">FarePassValidityPeriodType</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Specifies validity periods.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-fareprice" title="class in com.here.sdk.routing">FarePrice</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Price of a fare.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-farepricetype" title="enum class in com.here.sdk.routing">FarePriceType</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Type of price represented by a <a href="sdk-for-android-explore-com-here-sdk-routing-fareprice" title="class in com.here.sdk.routing"><code>FarePrice</code></a> object.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-farereason" title="enum class in com.here.sdk.routing">FareReason</a></div>
<div class="col-last even-row-color class-summary class-summary-tab3">
<div class="block">Reason for the cost.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-functionalroadclass" title="enum class in com.here.sdk.routing">FunctionalRoadClass</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Types of function road class.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-indoorlevelchangedata" title="class in com.here.sdk.routing">IndoorLevelChangeData</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Represents the level change data for an indoor maneuver.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-indoorlevelchangefeatures" title="enum class in com.here.sdk.routing">IndoorLevelChangeFeatures</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Indoor route features.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-indoormaneuver" title="class in com.here.sdk.routing">IndoorManeuver</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Represents a maneuver within an indoor section.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-indoormaneuveractions" title="enum class in com.here.sdk.routing">IndoorManeuverActions</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Defines the types of actions for indoor maneuvers.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-indoorrouteplace" title="class in com.here.sdk.routing">IndoorRoutePlace</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Represents a place within an indoor route.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-indoorsectiondetails" title="class in com.here.sdk.routing">IndoorSectionDetails</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Provides additional details for an indoor <a href="sdk-for-android-explore-com-here-sdk-routing-section" title="class in com.here.sdk.routing"><code>Section</code></a>.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-indoorspacedata" title="class in com.here.sdk.routing">IndoorSpaceData</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Represents the space data for an indoor maneuver.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-isoline" title="class in com.here.sdk.routing">Isoline</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Represents an isoline polygon around a center point.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-isolinecalculationmode" title="enum class in com.here.sdk.routing">IsolineCalculationMode</a></div>
<div class="col-last even-row-color class-summary class-summary-tab3">
<div class="block">Specifies how isoline calculation is optimized.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-isolineoptions" title="class in com.here.sdk.routing">IsolineOptions</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Specifies options for isolines calculation.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-isolineoptions-calculation" title="class in com.here.sdk.routing">IsolineOptions.Calculation</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Specifies isoline parameters.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-isolinerangetype" title="enum class in com.here.sdk.routing">IsolineRangeType</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Specifies the type of one or more range values to be included in the isoline.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-isolineroutingengine" title="class in com.here.sdk.routing">IsolineRoutingEngine</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Use the IsolineRoutingEngine to calculate a reachable area from a center point.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-localizedroadnumber" title="class in com.here.sdk.routing">LocalizedRoadNumber</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Used to represent road number localized to specific language with optional direction and route type information.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-localizedroadnumbers" title="class in com.here.sdk.routing">LocalizedRoadNumbers</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">The list of multiple names or titles for the same entity, possibly in different languages.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-localizedtextpreference" title="enum class in com.here.sdk.routing">LocalizedTextPreference</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Indicates the option of localized text usage.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-maneuver" title="class in com.here.sdk.routing">Maneuver</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">This class provides all the information for a maneuver.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Maneuver action type.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-mapmatchedcoordinates" title="class in com.here.sdk.routing">MapMatchedCoordinates</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Information about the user defined coordinates and where they match to the map.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-matchsideofstreet" title="enum class in com.here.sdk.routing">MatchSideOfStreet</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Specifies how the location set by <a href="sdk-for-android-explore-waypoint#sideOfStreetHint"><code>Waypoint.sideOfStreetHint</code></a> should be handled.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-maxaxlegroupweight" title="class in com.here.sdk.routing">MaxAxleGroupWeight</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block"><code>MaxAxleGroupWeight</code> contains all the restriction details violated by an axle group weight.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-maxspeedonsegment" title="class in com.here.sdk.routing">MaxSpeedOnSegment</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">New base speed for a segment.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-noticeseverity" title="enum class in com.here.sdk.routing">NoticeSeverity</a></div>
<div class="col-last even-row-color class-summary class-summary-tab3">
<div class="block">Describes the impact a notice has on the resource to which the notice is attached.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Identifiers for different optimizations that can be used during the
 route calculation while trying to keep the quality of the route being calculated high.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-passthroughwaypoint" title="class in com.here.sdk.routing">PassThroughWaypoint</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">This structure provides all the information for a passthrough waypoint.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-paymentmethod" title="enum class in com.here.sdk.routing">PaymentMethod</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Available payment methods.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-pedestrianoptions" title="class in com.here.sdk.routing">PedestrianOptions</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">Deprecated.
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-physicalconsumptionmodel" title="class in com.here.sdk.routing">PhysicalConsumptionModel</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Defines the physical consumption model for electric vehicles,
 using vehicle-specific parameters to calculate energy consumption along a route.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-postaction" title="class in com.here.sdk.routing">PostAction</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">An action that must be done after arrival, i.e.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-postactiontype" title="enum class in com.here.sdk.routing">PostActionType</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Identifies the action type.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-preaction" title="class in com.here.sdk.routing">PreAction</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">An action that must be done prior to the section, i.e.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-preactiontype" title="enum class in com.here.sdk.routing">PreActionType</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Identifies the action type.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-privatebusoptions" title="class in com.here.sdk.routing">PrivateBusOptions</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">Deprecated.
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-refreshrouteoptions" title="class in com.here.sdk.routing">RefreshRouteOptions</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">Deprecated.
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-refreshrouteparameters" title="class in com.here.sdk.routing">RefreshRouteParameters</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">This class provides the necessary information for refreshing a route from a
 specific location on it.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-roadfeatures" title="enum class in com.here.sdk.routing">RoadFeatures</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Road features or states.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-roadtexts" title="class in com.here.sdk.routing">RoadTexts</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Textual attributes of road.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-route" title="class in com.here.sdk.routing">Route</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">A route is a path through a road network over which someone travels.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing">RouteHandle</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Provides an opaque handle to the calculated <a href="sdk-for-android-explore-com-here-sdk-routing-route" title="class in com.here.sdk.routing"><code>Route</code></a>.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-routelabel" title="class in com.here.sdk.routing">RouteLabel</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">The main street name or road number for a route.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-routelabeltype" title="enum class in com.here.sdk.routing">RouteLabelType</a></div>
<div class="col-last even-row-color class-summary class-summary-tab3">
<div class="block">Identifies the type of the route label.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-routeoffset" title="class in com.here.sdk.routing">RouteOffset</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Represents a specific location along the route.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-routeoptions" title="class in com.here.sdk.routing">RouteOptions</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">The options to specify how the route will be calculated.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-routeplace" title="class in com.here.sdk.routing">RoutePlace</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">The location information.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-routeplacedirection" title="enum class in com.here.sdk.routing">RoutePlaceDirection</a></div>
<div class="col-last even-row-color class-summary class-summary-tab3">
<div class="block">Specifies the direction to make distinction between departure and arrival cases.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-routeplacetype" title="enum class in com.here.sdk.routing">RoutePlaceType</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Identifies the route place type.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-routerailwaycrossing" title="class in com.here.sdk.routing">RouteRailwayCrossing</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Contains information about railway crossing.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-routerailwaycrossingtype" title="enum class in com.here.sdk.routing">RouteRailwayCrossingType</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Identify possible type of route railway crossing.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-routestop" title="class in com.here.sdk.routing">RouteStop</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Route stop that should be used together with import route functionality.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-routetextoptions" title="class in com.here.sdk.routing">RouteTextOptions</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Specify how textual output should be provided.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-routingconnectionsettings" title="class in com.here.sdk.routing">RoutingConnectionSettings</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Defines the settings for the retry logic when connecting to the HERE routing backend.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-routingengine" title="class in com.here.sdk.routing">RoutingEngine</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Use the RoutingEngine to calculate a route from A to B with
 a number of waypoints in between.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a></div>
<div class="col-last even-row-color class-summary class-summary-tab3">
<div class="block">Specifies possible errors that may result from the calculation of a route.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab1"><a href="sdk-for-android-explore-com-here-sdk-routing-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab1">
<div class="block">Provides the interface for the online and offline
 routing engines.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-routingoptions" title="class in com.here.sdk.routing">RoutingOptions</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">The options defines how a route should be calculated.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-scooteroptions" title="class in com.here.sdk.routing">ScooterOptions</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">Deprecated.
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-section" title="class in com.here.sdk.routing">Section</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">A section is a part of the route between two stopovers.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-sectionnotice" title="class in com.here.sdk.routing">SectionNotice</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Explains an issue encountered in a <a href="sdk-for-android-explore-com-here-sdk-routing-section" title="class in com.here.sdk.routing"><code>Section</code></a>.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></div>
<div class="col-last even-row-color class-summary class-summary-tab3">
<div class="block">Notice codes which point the issues encountered during processing of a <a href="sdk-for-android-explore-com-here-sdk-routing-section" title="class in com.here.sdk.routing"><code>Section</code></a>.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-sectiontransportmode" title="enum class in com.here.sdk.routing">SectionTransportMode</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Specifies the <a href="sdk-for-android-explore-com-here-sdk-routing-section" title="class in com.here.sdk.routing"><code>Section</code></a> mode of transport.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-segmentreference" title="class in com.here.sdk.routing">SegmentReference</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Reference to a segment id with a travel direction.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-sideofdestination" title="enum class in com.here.sdk.routing">SideOfDestination</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Specifies the side of street on which the destination is located.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-signpost" title="class in com.here.sdk.routing">Signpost</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Signpost information.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-signpostlabel" title="class in com.here.sdk.routing">SignpostLabel</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Details of a signpost representing a particular direction or destination.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-span" title="class in com.here.sdk.routing">Span</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">A span is a part of the <a href="sdk-for-android-explore-com-here-sdk-routing-section" title="class in com.here.sdk.routing"><code>Section</code></a> which is traversable or navigable.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-streetattributes" title="enum class in com.here.sdk.routing">StreetAttributes</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Types of street attributes.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-taxioptions" title="class in com.here.sdk.routing">TaxiOptions</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">Deprecated.
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-textusageoptions" title="class in com.here.sdk.routing">TextUsageOptions</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Specify whether the text should be used when generating notification.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-toll" title="class in com.here.sdk.routing">Toll</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">This struct presents all the data for a toll.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-tollfare" title="class in com.here.sdk.routing">TollFare</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">This struct presents all the fare data for a toll.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-tollfarepass" title="class in com.here.sdk.routing">TollFarePass</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block"><a href="sdk-for-android-explore-com-here-sdk-routing-tollfare" title="class in com.here.sdk.routing"><code>TollFare</code></a> multi-travel pass characteristics.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-tolloptions" title="class in com.here.sdk.routing">TollOptions</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">The option to specify how the tolls should be calculated.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-tolloptions-emissiontype" title="enum class in com.here.sdk.routing">TollOptions.EmissionType</a></div>
<div class="col-last even-row-color class-summary class-summary-tab3">
<div class="block">Supported options of emission type</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-tolloptions-vehiclecategory" title="enum class in com.here.sdk.routing">TollOptions.VehicleCategory</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Supported options of vehicle category for toll calculation.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-trafficincidentonroute" title="class in com.here.sdk.routing">TrafficIncidentOnRoute</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Traffic incidents on a route.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-trafficonroute" title="class in com.here.sdk.routing">TrafficOnRoute</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Traffic information on a route.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-trafficonsection" title="class in com.here.sdk.routing">TrafficOnSection</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Traffic information on a section.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-trafficonspan" title="class in com.here.sdk.routing">TrafficOnSpan</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Traffic information of a span along a route.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-trafficoptimizationmode" title="enum class in com.here.sdk.routing">TrafficOptimizationMode</a></div>
<div class="col-last even-row-color class-summary class-summary-tab3">
<div class="block">Traffic optimization mode that defines whether and what kind of traffic information should be considered during route calculation.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-transitdeparture" title="class in com.here.sdk.routing">TransitDeparture</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">This struct holds the transit departure or arrival information.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-transitdeparturestatus" title="enum class in com.here.sdk.routing">TransitDepartureStatus</a></div>
<div class="col-last even-row-color class-summary class-summary-tab3">
<div class="block">Status of a departure.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-transitincident" title="class in com.here.sdk.routing">TransitIncident</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">A transit incident describes disruptions on the transit network.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-transitincidenteffect" title="enum class in com.here.sdk.routing">TransitIncidentEffect</a></div>
<div class="col-last even-row-color class-summary class-summary-tab3">
<div class="block">Transit incident effect.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-transitincidenttype" title="enum class in com.here.sdk.routing">TransitIncidentType</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Transit incident type.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-transitmode" title="enum class in com.here.sdk.routing">TransitMode</a></div>
<div class="col-last even-row-color class-summary class-summary-tab3">
<div class="block">Public transit mode</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-transitmodefilter" title="enum class in com.here.sdk.routing">TransitModeFilter</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Filtering mode for public transit.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-transitrouteoptions" title="class in com.here.sdk.routing">TransitRouteOptions</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">All the options to specify how a public transit route should be calculated.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-transitroutingengine" title="class in com.here.sdk.routing">TransitRoutingEngine</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Use the TransitRoutingEngine to calculate a public transit route from A to B with
 a number of waypoints in between.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-transitsectiondetails" title="class in com.here.sdk.routing">TransitSectionDetails</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Gives the details of a transit section.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-transitstop" title="class in com.here.sdk.routing">TransitStop</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">A transit stop between the departure and destination of a transit section.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-transittransport" title="class in com.here.sdk.routing">TransitTransport</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Holds all the transit transport information.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-transitwaypoint" title="class in com.here.sdk.routing">TransitWaypoint</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Represents a transit waypoint, used as input for transit route calculation.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-traveldirection" title="enum class in com.here.sdk.routing">TravelDirection</a></div>
<div class="col-last even-row-color class-summary class-summary-tab3">
<div class="block">Travel direction.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-truckoptions" title="class in com.here.sdk.routing">TruckOptions</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">Deprecated.
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-vehiclerestrictionmaxweight" title="class in com.here.sdk.routing">VehicleRestrictionMaxWeight</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block"><code>VehicleRestrictionMaxWeight</code> contains max permitted weight during the trip, in kilograms,
 along with the specific type of maximum permitted weight restriction.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-vehiclerestrictionmaxweighttype" title="enum class in com.here.sdk.routing">VehicleRestrictionMaxWeightType</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">This enum represents the specific type of the maximum permitted weight restriction.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-violatedrestriction" title="class in com.here.sdk.routing">ViolatedRestriction</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block"><code>ViolatedRestriction</code> contains all the violated restriction details for the planned trip.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-violatedrestriction-details" title="class in com.here.sdk.routing">ViolatedRestriction.Details</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Optional restriction details, contains additional information depending on the specific violation, zero or more member might be set.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-walkattributes" title="enum class in com.here.sdk.routing">WalkAttributes</a></div>
<div class="col-last even-row-color class-summary class-summary-tab3">
<div class="block">Types of walk attributes.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-explore-com-here-sdk-routing-waypoint" title="class in com.here.sdk.routing">Waypoint</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Represents a waypoint, used as input for route calculation.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-waypointtype" title="enum class in com.here.sdk.routing">WaypointType</a></div>
<div class="col-last even-row-color class-summary class-summary-tab3">
<div class="block">Defines if the waypoint is a stop over, or a hint for a desired polyline of a
 route.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="sdk-for-android-explore-com-here-sdk-routing-zonecategory" title="enum class in com.here.sdk.routing">ZoneCategory</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Identifies categories of zones which routes avoid going through when used in
 <a href="sdk-for-android-explore-com-here-sdk-routing-avoidanceoptions" title="class in com.here.sdk.routing"><code>AvoidanceOptions</code></a>.</div>
</div>
</div>
</div>
</div>
</li>
</ul>
</section>






</div>
`
}</HTMLBlock>
