---
title: "mapdata library"
slug: "sdk-for-flutter-navigate-mapdata-mapdata-library"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- mapdata-library.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapdata/mapdata-library.html#classes">Classes</a></li>
<li><a href="mapdata/AdminContextId-class.html">AdminContextId</a></li>
<li><a href="mapdata/AdministrativeCommercialVehicleRules-class.html">AdministrativeCommercialVehicleRules</a></li>
<li><a href="mapdata/AdministrativeRules-class.html">AdministrativeRules</a></li>
<li><a href="mapdata/AdministrativeRulesLoader-class.html">AdministrativeRulesLoader</a></li>
<li><a href="mapdata/AllowedTransportModes-class.html">AllowedTransportModes</a></li>
<li><a href="mapdata/BloodAlcoholContentLimit-class.html">BloodAlcoholContentLimit</a></li>
<li><a href="mapdata/Connectivity-class.html">Connectivity</a></li>
<li><a href="mapdata/DirectedOCMSegmentId-class.html">DirectedOCMSegmentId</a></li>
<li><a href="mapdata/DownloadingFileOptions-class.html">DownloadingFileOptions</a></li>
<li><a href="mapdata/DriveRestRegulation-class.html">DriveRestRegulation</a></li>
<li><a href="mapdata/FileReference-class.html">FileReference</a></li>
<li><a href="mapdata/LaneAttribute-class.html">LaneAttribute</a></li>
<li><a href="mapdata/OCMSegmentId-class.html">OCMSegmentId</a></li>
<li><a href="mapdata/PhysicalAttributes-class.html">PhysicalAttributes</a></li>
<li><a href="mapdata/PreTripPlanning-class.html">PreTripPlanning</a></li>
<li><a href="mapdata/RailwayCrossing-class.html">RailwayCrossing</a></li>
<li><a href="mapdata/RoadProfileCondition-class.html">RoadProfileCondition</a></li>
<li><a href="mapdata/RoadUsages-class.html">RoadUsages</a></li>
<li><a href="mapdata/SegmentConnectivities-class.html">SegmentConnectivities</a></li>
<li><a href="mapdata/SegmentData-class.html">SegmentData</a></li>
<li><a href="mapdata/SegmentDataLoader-class.html">SegmentDataLoader</a></li>
<li><a href="mapdata/SegmentDataLoaderOptions-class.html">SegmentDataLoaderOptions</a></li>
<li><a href="mapdata/SegmentReferenceConverter-class.html">SegmentReferenceConverter</a></li>
<li><a href="mapdata/SegmentSpanData-class.html">SegmentSpanData</a></li>
<li><a href="mapdata/SegmentSpecialSpeedSituation-class.html">SegmentSpecialSpeedSituation</a></li>
<li><a href="mapdata/SegmentSpeedLimit-class.html">SegmentSpeedLimit</a></li>
<li><a href="mapdata/TollCost-class.html">TollCost</a></li>
<li><a href="mapdata/TollPoint-class.html">TollPoint</a></li>
<li><a href="mapdata/TollStructure-class.html">TollStructure</a></li>
<li><a href="mapdata/TollStructureManeuver-class.html">TollStructureManeuver</a></li>
<li><a href="mapdata/TollSystem-class.html">TollSystem</a></li>
<li><a href="mapdata/TrafficSignal-class.html">TrafficSignal</a></li>
<li><a href="mapdata/VehicleProfileRestriction-class.html">VehicleProfileRestriction</a></li>
<li><a href="mapdata/VehicleRestrictionCondition-class.html">VehicleRestrictionCondition</a></li>
<li><a href="mapdata/VehicleSpecificAccess-class.html">VehicleSpecificAccess</a></li>
<li><a href="mapdata/VehicleSpecificSpeedLimit-class.html">VehicleSpecificSpeedLimit</a></li>
<li class="section-title"><a href="mapdata/mapdata-library.html#enums">Enums</a></li>
<li><a href="mapdata/CommercialVehicleRoadType.html">CommercialVehicleRoadType</a></li>
<li><a href="mapdata/DrivingSide.html">DrivingSide</a></li>
<li><a href="mapdata/FileReferenceType.html">FileReferenceType</a></li>
<li><a href="mapdata/HazardousMaterialType.html">HazardousMaterialType</a></li>
<li><a href="mapdata/HeadlightsRequirement.html">HeadlightsRequirement</a></li>
<li><a href="mapdata/LocalRoadCharacteristic.html">LocalRoadCharacteristic</a></li>
<li><a href="mapdata/MapDataLoaderErrorCode.html">MapDataLoaderErrorCode</a></li>
<li><a href="mapdata/ParkingSideRegulation.html">ParkingSideRegulation</a></li>
<li><a href="mapdata/PhysicalStructure.html">PhysicalStructure</a></li>
<li><a href="mapdata/RailwayCrossingType.html">RailwayCrossingType</a></li>
<li><a href="mapdata/RoadDivider.html">RoadDivider</a></li>
<li><a href="mapdata/SpecialSpeedType.html">SpecialSpeedType</a></li>
<li><a href="mapdata/TollStructureType.html">TollStructureType</a></li>
<li><a href="mapdata/TrafficSignalLocation.html">TrafficSignalLocation</a></li>
<li><a href="mapdata/TurnOnRedRegulation.html">TurnOnRedRegulation</a></li>
<li><a href="mapdata/VehicleTypeCondition.html">VehicleTypeCondition</a></li>
<li class="section-title"><a href="mapdata/mapdata-library.html#exceptions">Exceptions</a></li>
<li><a href="mapdata/MapDataLoaderExceptionException-class.html">MapDataLoaderExceptionException</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li class="self-crumb">mapdata.dart</li>
</ol>
<div class="self-name">mapdata</div>
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
<div class="main-content" data-above-sidebar="" data-below-sidebar="mapdata/mapdata-library-sidebar.html" id="dartdoc-main-content">
<div>
<h1>mapdata library</h1>
</div>
<section class="summary offset-anchor" id="classes">
<h2>Classes</h2>
<dl>
<dt id="AdminContextId">
/sdk-for-flutter-navigate-mapdata-admincontextid-class
</dt>
<dd>
  Represents a set of administrative rules for a country or a state.
</dd>
<dt id="AdministrativeCommercialVehicleRules">
/sdk-for-flutter-navigate-mapdata-administrativecommercialvehiclerules-class
</dt>
<dd>
  Commercial vehicle regulations for an administrative region (country or state).
</dd>
<dt id="AdministrativeRules">
/sdk-for-flutter-navigate-mapdata-administrativerules-class
</dt>
<dd>
  Represents a set of administrative rules for a country or a state.
</dd>
<dt id="AdministrativeRulesLoader">
/sdk-for-flutter-navigate-mapdata-administrativerulesloader-class
</dt>
<dd>
  Provides the abstract class for the access to the administrative rules available
for a country or a state in the local OCM map.
</dd>
<dt id="AllowedTransportModes">
/sdk-for-flutter-navigate-mapdata-allowedtransportmodes-class
</dt>
<dd>
  Specifies which transport modes are allowed in a particular direction.
</dd>
<dt id="BloodAlcoholContentLimit">
/sdk-for-flutter-navigate-mapdata-bloodalcoholcontentlimit-class
</dt>
<dd>
  Represents the rules regarding alcohol in blood content limit in a country or state for
all types of drivers.
</dd>
<dt id="Connectivity">
/sdk-for-flutter-navigate-mapdata-connectivity-class
</dt>
<dd>
  A class that provides information about link id and accessibility.
</dd>
<dt id="DirectedOCMSegmentId">
/sdk-for-flutter-navigate-mapdata-directedocmsegmentid-class
</dt>
<dd>
  OCM Segment ID with travel direction of segment.
</dd>
<dt id="DownloadingFileOptions">
/sdk-for-flutter-navigate-mapdata-downloadingfileoptions-class
</dt>
<dd>
  A class which identifies the configuration when downloading a file reference.
</dd>
<dt id="DriveRestRegulation">
/sdk-for-flutter-navigate-mapdata-driverestregulation-class
</dt>
<dd>
  Drive-rest regulation defining mandatory rest requirements for commercial vehicle drivers.
</dd>
<dt id="FileReference">
/sdk-for-flutter-navigate-mapdata-filereference-class
</dt>
<dd>
  A class that provides information for a file reference.
</dd>
<dt id="LaneAttribute">
/sdk-for-flutter-navigate-mapdata-laneattribute-class
</dt>
<dd>
  A class that describes attributes assigned to a specific section of a lane.
</dd>
<dt id="OCMSegmentId">
/sdk-for-flutter-navigate-mapdata-ocmsegmentid-class
</dt>
<dd>
  OCM Segment ID of particular matched /sdk-for-flutter-navigate-routing-segmentreference-class from OCM map,
represented in form: Tile + Local ID's .
</dd>
<dt id="PhysicalAttributes">
/sdk-for-flutter-navigate-mapdata-physicalattributes-class
</dt>
<dd>
  Physical attributes of the segment.
</dd>
<dt id="PreTripPlanning">
/sdk-for-flutter-navigate-mapdata-pretripplanning-class
</dt>
<dd>
  Represents the legal requirements to be considered before a trip for all vehicles types.
</dd>
<dt id="RailwayCrossing">
/sdk-for-flutter-navigate-mapdata-railwaycrossing-class
</dt>
<dd>
  Identifies the presence and the location of railway corssings.
</dd>
<dt id="RoadProfileCondition">
/sdk-for-flutter-navigate-mapdata-roadprofilecondition-class
</dt>
<dd>
  Road profile conditions that must be met for a regulation to apply.
</dd>
<dt id="RoadUsages">
/sdk-for-flutter-navigate-mapdata-roadusages-class
</dt>
<dd>
  Road Usages of the segment.
</dd>
<dt id="SegmentConnectivities">
/sdk-for-flutter-navigate-mapdata-segmentconnectivities-class
</dt>
<dd>
  A class that provides information about segment one direction source and target connectivities.
</dd>
<dt id="SegmentData">
/sdk-for-flutter-navigate-mapdata-segmentdata-class
</dt>
<dd>
  Contains the requested information for a segment
</dd>
<dt id="SegmentDataLoader">
/sdk-for-flutter-navigate-mapdata-segmentdataloader-class
</dt>
<dd>
  Provides the abstract class for the access to the
segments data available in the local OCM map.
</dd>
<dt id="SegmentDataLoaderOptions">
/sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-class
</dt>
<dd>
  Specifies which data should be loaded by the /sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddata or /sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddirectedsegmentdata function.
</dd>
<dt id="SegmentReferenceConverter">
/sdk-for-flutter-navigate-mapdata-segmentreferenceconverter-class
</dt>
<dd>
  A SegmentReferenceConverter provides possibility to convert mapmatched instances of
/sdk-for-flutter-navigate-routing-segmentreference-class to corresponding instances of /sdk-for-flutter-navigate-mapdata-directedocmsegmentid-class.
</dd>
<dt id="SegmentSpanData">
/sdk-for-flutter-navigate-mapdata-segmentspandata-class
</dt>
<dd>
  Contains attributes that are not necessarily constant on a full segment.
</dd>
<dt id="SegmentSpecialSpeedSituation">
/sdk-for-flutter-navigate-mapdata-segmentspecialspeedsituation-class
</dt>
<dd>
  A special speed situation indicates a speed that exists under special circumstances.
</dd>
<dt id="SegmentSpeedLimit">
/sdk-for-flutter-navigate-mapdata-segmentspeedlimit-class
</dt>
<dd>
  Describes the posted speed limit on the segment span.
</dd>
<dt id="TollCost">
/sdk-for-flutter-navigate-mapdata-tollcost-class
</dt>
<dd>
  Contains informations about the toll costs for a specific vehicle profile.
</dd>
<dt id="TollPoint">
/sdk-for-flutter-navigate-mapdata-tollpoint-class
</dt>
<dd>
  A class to represent the toll point attributes of a segment.
</dd>
<dt id="TollStructure">
/sdk-for-flutter-navigate-mapdata-tollstructure-class
</dt>
<dd>
  A class that defines tolling configuration for a lane.
</dd>
<dt id="TollStructureManeuver">
/sdk-for-flutter-navigate-mapdata-tollstructuremaneuver-class
</dt>
<dd>
  A class that provides information for a toll structure at a toll point.
</dd>
<dt id="TollSystem">
/sdk-for-flutter-navigate-mapdata-tollsystem-class
</dt>
<dd>
  Contains informations about a toll system.
</dd>
<dt id="TrafficSignal">
/sdk-for-flutter-navigate-mapdata-trafficsignal-class
</dt>
<dd>
  Identifies the presence and the location of traffic lights at an intersection
</dd>
<dt id="VehicleProfileRestriction">
/sdk-for-flutter-navigate-mapdata-vehicleprofilerestriction-class
</dt>
<dd>
  Physical and cargo profile of a vehicle that triggers a regulation.
</dd>
<dt id="VehicleRestrictionCondition">
/sdk-for-flutter-navigate-mapdata-vehiclerestrictioncondition-class
</dt>
<dd>
  Combined set of conditions that must all be satisfied for a regulation to apply.
</dd>
<dt id="VehicleSpecificAccess">
/sdk-for-flutter-navigate-mapdata-vehiclespecificaccess-class
</dt>
<dd>
  Access regulation for a specific vehicle type on a road segment.
</dd>
<dt id="VehicleSpecificSpeedLimit">
/sdk-for-flutter-navigate-mapdata-vehiclespecificspeedlimit-class
</dt>
<dd>
  Speed limit regulation specific to a vehicle type.
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="enums">
<h2>Enums</h2>
<dl>
<dt id="CommercialVehicleRoadType">
/sdk-for-flutter-navigate-mapdata-commercialvehicleroadtype
</dt>
<dd>
  Concise description of road type used in commercial vehicle regulations.
</dd>
<dt id="DrivingSide">
/sdk-for-flutter-navigate-mapdata-drivingside
</dt>
<dd>
  The side of the road on which the driving is done.
</dd>
<dt id="FileReferenceType">
/sdk-for-flutter-navigate-mapdata-filereferencetype
</dt>
<dd>
  Type of reference file.
</dd>
<dt id="HazardousMaterialType">
/sdk-for-flutter-navigate-mapdata-hazardousmaterialtype
</dt>
<dd>
  Hazardous material type as defined in the enum applicable for those that carry these
</dd>
<dt id="HeadlightsRequirement">
/sdk-for-flutter-navigate-mapdata-headlightsrequirement
</dt>
<dd>
  The situations in which headlights are required to be turned on.
</dd>
<dt id="LocalRoadCharacteristic">
/sdk-for-flutter-navigate-mapdata-localroadcharacteristic
</dt>
<dd>
  Specifies the local road characteristics: frontage, parking lot road, poi access.
</dd>
<dt id="MapDataLoaderErrorCode">
/sdk-for-flutter-navigate-mapdata-mapdataloadererrorcode
</dt>
<dd>
  Specifies possible errors from map data accessing.
</dd>
<dt id="ParkingSideRegulation">
/sdk-for-flutter-navigate-mapdata-parkingsideregulation
</dt>
<dd>
  The regulations for parking on the side of the road.
</dd>
<dt id="PhysicalStructure">
/sdk-for-flutter-navigate-mapdata-physicalstructure
</dt>
<dd>
  Physical structure of a road feature that causes an access restriction,
such as a bridge or tunnel that may limit vehicle dimensions or weight.
</dd>
<dt id="RailwayCrossingType">
/sdk-for-flutter-navigate-mapdata-railwaycrossingtype
</dt>
<dd>
  Type of railway crossing.
</dd>
<dt id="RoadDivider">
/sdk-for-flutter-navigate-mapdata-roaddivider
</dt>
<dd>
  A physical structure or painted road marking intended to legally prohibit
left turns in right-side driving countries, right turns in left-side driving countries,
and U-turns at divided intersections or in the middle of divided segments.
</dd>
<dt id="SpecialSpeedType">
/sdk-for-flutter-navigate-mapdata-specialspeedtype
</dt>
<dd>
  Represents the speed situation type.
</dd>
<dt id="TollStructureType">
/sdk-for-flutter-navigate-mapdata-tollstructuretype
</dt>
<dd>
  This enum defines the type of toll structure used on a road segment or lane.
</dd>
<dt id="TrafficSignalLocation">
/sdk-for-flutter-navigate-mapdata-trafficsignallocation
</dt>
<dd>
  Indicates the location of a traffic signal.
</dd>
<dt id="TurnOnRedRegulation">
/sdk-for-flutter-navigate-mapdata-turnonredregulation
</dt>
<dd>
  The regulations for turning on the red color of the traffic light.
</dd>
<dt id="VehicleTypeCondition">
/sdk-for-flutter-navigate-mapdata-vehicletypecondition
</dt>
<dd>
  Type of commercial vehicle to which a regulation applies.
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="exceptions">
<h2>Exceptions / Errors</h2>
<dl>
<dt id="MapDataLoaderExceptionException">
/sdk-for-flutter-navigate-mapdata-mapdataloaderexceptionexception-class
</dt>
<dd>
  Error occurred during obtaining data form the map.
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
<li class="self-crumb">mapdata.dart</li>
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
<h5>mapdata library</h5>
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
