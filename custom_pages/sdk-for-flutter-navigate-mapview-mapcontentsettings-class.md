---
title: "MapContentSettings class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapcontentsettings-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapContentSettings-class-sidebar.html">

<div>

# <span class="kind-class">MapContentSettings</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Provides settings regarding map data which are applied globally to all map views.

The settings can already be changed before a map view instance is created.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontentsettings-mapcontentsettings">MapContentSettings</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontentsettings-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontentsettings-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontentsettings-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontentsettings-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontentsettings-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Static Methods

<span class="name deprecated"><a href="sdk-for-flutter-navigate-mapview-mapcontentsettings-configurevehiclerestrictionfilter" class="deprecated">configureVehicleRestrictionFilter</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-configureVehicleRestrictionFilter-param-transportMode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode</a></span> <span class="parameter-name">transportMode</span>, </span><span id="sdk-for-flutter-navigate-configureVehicleRestrictionFilter-param-truckSpecifications" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-transport-truckspecifications-class" class="deprecated">TruckSpecifications</a></span> <span class="parameter-name">truckSpecifications</span>, </span><span id="sdk-for-flutter-navigate-configureVehicleRestrictionFilter-param-hazardousMaterials" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-transport-hazardousmaterial">HazardousMaterial</a></span>\></span>?</span> <span class="parameter-name">hazardousMaterials</span>, </span><span id="sdk-for-flutter-navigate-configureVehicleRestrictionFilter-param-tunnelCategory" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-transport-tunnelcategory">TunnelCategory</a>?</span> <span class="parameter-name">tunnelCategory</span></span>) <span class="returntype parameter">→ void</span> </span>  
Configure a filter for <a href="sdk-for-flutter-navigate-mapview-mapfeatures-vehiclerestrictions">MapFeatures.vehicleRestrictions</a> to show only the restrictions matching the specified criteria when the feature is enabled.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontentsettings-configurevehiclerestrictionfilterwithtransportspecification">configureVehicleRestrictionFilterWithTransportSpecification</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-configureVehicleRestrictionFilterWithTransportSpecification-param-transportSpecs" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a></span> <span class="parameter-name">transportSpecs</span></span>) <span class="returntype parameter">→ void</span> </span>  
Configures a filter for <a href="sdk-for-flutter-navigate-mapview-mapfeatures-vehiclerestrictions">MapFeatures.vehicleRestrictions</a> to show only the restrictions matching the transport specifications when the feature is enabled.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontentsettings-filtertrafficincidents">filterTrafficIncidents</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-filterTrafficIncidents-param-trafficIncidents" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-traffic-trafficincidenttype">TrafficIncidentType</a></span>\></span></span> <span class="parameter-name">trafficIncidents</span></span>) <span class="returntype parameter">→ void</span> </span>  
Filters the displayed traffic incidents so that only the ones applicable to the specified criteria are shown when general display of traffic incidents is enabled.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontentsettings-resetpoicategoriesvisibility">resetPoiCategoriesVisibility</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Resets POI categories visibility to their default state.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontentsettings-resettrafficincidentfilter">resetTrafficIncidentFilter</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Removes all filters regarding Traffic Incidents so that all incidents will be displayed, when the display of Traffic Incidents is enabled using <a href="sdk-for-flutter-navigate-mapview-mapscene-enablefeatures">MapScene.enableFeatures</a> with <a href="sdk-for-flutter-navigate-mapview-mapfeatures-trafficincidents">MapFeatures.trafficIncidents</a>.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontentsettings-resettrafficrefreshperiod">resetTrafficRefreshPeriod</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Resets the traffic data (both flow and incidents) refresh period so the default traffic information validity time and the refresh period derived from the refresh period of the traffic server is used.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontentsettings-resetvehiclerestrictionfilter">resetVehicleRestrictionFilter</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Removes all filters regarding vehicle restrictions so that all restrictions will be displayed, when the display of vehicle restrictions is enabled by enabling feature using <a href="sdk-for-flutter-navigate-mapview-mapscene-enablefeatures">MapScene.enableFeatures</a> with <a href="sdk-for-flutter-navigate-mapview-mapfeatures-vehiclerestrictions">MapFeatures.vehicleRestrictions</a> and setting layer visibility using <a href="sdk-for-flutter-navigate-mapview-mapscene-setlayervisibility">MapScene.setLayerVisibility</a>.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontentsettings-setpoicategoriesvisibility">setPoiCategoriesVisibility</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setPoiCategoriesVisibility-param-categoryIds" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span> <span class="parameter-name">categoryIds</span>, </span><span id="sdk-for-flutter-navigate-setPoiCategoriesVisibility-param-visibility" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-visibilitystate">VisibilityState</a></span> <span class="parameter-name">visibility</span></span>) <span class="returntype parameter">→ void</span> </span>  
Sets visibility for embedded carto POI categories (points of interest that are visible on the map, by default).

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontentsettings-settrafficrefreshperiod">setTrafficRefreshPeriod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setTrafficRefreshPeriod-param-value" class="parameter"><span class="type-annotation">Duration</span> <span class="parameter-name">value</span></span>) <span class="returntype parameter">→ void</span> </span>  
Sets the traffic data refresh period for both <a href="sdk-for-flutter-navigate-mapview-mapfeatures-trafficflow">MapFeatures.trafficFlow</a> and <a href="sdk-for-flutter-navigate-mapview-mapfeatures-trafficincidents">MapFeatures.trafficIncidents</a>.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

