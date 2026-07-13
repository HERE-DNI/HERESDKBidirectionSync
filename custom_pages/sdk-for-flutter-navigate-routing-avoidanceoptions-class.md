---
title: "AvoidanceOptions class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-avoidanceoptions-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/AvoidanceOptions-class-sidebar.html">

<div>

# <span class="kind-class">AvoidanceOptions</span> class

</div>

<div class="section desc markdown">

The options to specify restrictions for route calculations.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-routing-avoidanceoptions-avoidanceoptions">AvoidanceOptions</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-routing-avoidanceoptions-avoidboundingboxareasoptions">avoidBoundingBoxAreasOptions</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-avoidboundingboxareaoptions-class">AvoidBoundingBoxAreaOptions</a></span>\></span></span>  
List of rectangular shapes which routes must not cross and additional options for this area.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-avoidanceoptions-avoidcorridorareasoptions">avoidCorridorAreasOptions</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-avoidcorridorareaoptions-class">AvoidCorridorAreaOptions</a></span>\></span></span>  
List of corridor shapes which routes must not cross and additional options for this area. **Note:** Currently, the maximum count of corridors is limited to 20.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-avoidanceoptions-avoidedtruckroadtypes">avoidedTruckRoadTypes</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-transport-truckroadtype">TruckRoadType</a></span>\></span></span>  
Specifies a list of avoided truck road types for vehicle. Refer to <a href="sdk-for-flutter-navigate-transport-truckroadtype">TruckRoadType</a> for the available options.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-avoidanceoptions-avoidpolygonareasoptions">avoidPolygonAreasOptions</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-avoidpolygonareaoptions-class">AvoidPolygonAreaOptions</a></span>\></span></span>  
List of polygon shapes which routes must not cross and additional options for this area. **Note:** Currently, the maximum count of polygons is limited to 20.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-avoidanceoptions-countries">countries</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-countrycode">CountryCode</a></span>\></span></span>  
Countries that the route must avoid. Strictly enforced. Violations are reported as <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode.violatedBlockedRoad</a>. **Note:** This avoidance option is not supported in `IsolineOptions` for isoline calculation.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-avoidanceoptions-exceptzoneids">exceptZoneIds</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span>  
Exception to `AvoidanceOptions.zone_categories`, which can be specified by list of zone identifiers. e.g. the format of ID is like `here:cm:envzone:2`. Information about the various routing zones originates from the respective catalogs of platform.here.com. For example, more information on zone IDs for Environmental Zones is available under "https://platform.here.com/data/hrn:here:data::olp-here:rib-2/environmental-zones/overview".

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-avoidanceoptions-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-avoidanceoptions-roadfeatures">roadFeatures</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-roadfeatures">RoadFeatures</a></span>\></span></span>  
Features which routes should avoid. Best effort only (not enforced).

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-avoidanceoptions-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-avoidanceoptions-segments">segments</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-segmentreference-class">SegmentReference</a></span>\></span></span>  
Segments that routes will avoid going through. Violations are reported as <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode.violatedBlockedRoad</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-avoidanceoptions-zonecategories">zoneCategories</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-zonecategory">ZoneCategory</a></span>\></span></span>  
Zone categories which routes must not cross. Strictly enforced. Violations are reported as <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode.violatedZoneRestriction</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-avoidanceoptions-zoneids">zoneIds</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span>  
List containing identifiers of zones that routes should avoid going through. e.g. the format of ID is like `here:cm:envzone:2`. Information about the various routing zones originates from the respective catalogs of platform.here.com. For example, more information on zone IDs for Environmental Zones is available under "https://platform.here.com/data/hrn:here:data::olp-here:rib-2/environmental-zones/overview".

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-routing-avoidanceoptions-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-avoidanceoptions-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-routing-avoidanceoptions-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

