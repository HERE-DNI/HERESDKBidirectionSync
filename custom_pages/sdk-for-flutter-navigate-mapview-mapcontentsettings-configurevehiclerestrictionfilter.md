---
title: "configureVehicleRestrictionFilter method - MapContentSettings class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapcontentsettings-configurevehiclerestrictionfilter"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- configureVehicleRestrictionFilter.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapContentSettings-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">configureVehicleRestrictionFilter</span> static method

</div>

<div class="section multi-line-signature">

<div>

1.  @Deprecated("Will be removed in v4.28.0, use \[MapContentSettings.configureVehicleRestrictionFilterWithTransportSpecification\] instead.")

</div>

<span class="returntype">void</span> <span class="name deprecated">configureVehicleRestrictionFilter</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-configureVehicleRestrictionFilter-param-transportMode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode</a></span> <span class="parameter-name">transportMode</span>, </span>
2.  <span id="sdk-for-flutter-navigate-configureVehicleRestrictionFilter-param-truckSpecifications" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-transport-truckspecifications-class" class="deprecated">TruckSpecifications</a></span> <span class="parameter-name">truckSpecifications</span>, </span>
3.  <span id="sdk-for-flutter-navigate-configureVehicleRestrictionFilter-param-hazardousMaterials" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-transport-hazardousmaterial">HazardousMaterial</a></span>\></span>?</span> <span class="parameter-name">hazardousMaterials</span>, </span>
4.  <span id="sdk-for-flutter-navigate-configureVehicleRestrictionFilter-param-tunnelCategory" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-transport-tunnelcategory">TunnelCategory</a>?</span> <span class="parameter-name">tunnelCategory</span>, </span>

)

</div>

<div class="section desc markdown">

Configure a filter for <a href="sdk-for-flutter-navigate-mapview-mapfeatures-vehiclerestrictions">MapFeatures.vehicleRestrictions</a> to show only the restrictions matching the specified criteria when the feature is enabled.

# Filtering rules for truck specifications

Only restrictions applicable to the supplied truck specifications will be shown.

Examples:

- If the height in `MapContentSettings.configureVehicleRestrictionFilter.truckSpecifications` is set to 200 cm, then height restrictions with a height greater than 200 cm will not be displayed.
- If the trailer count in `MapContentSettings.configureVehicleRestrictionFilter.truckSpecifications` is set to 2, then trailer restrictions for a count greater than 2 will not be displayed.

# Filtering rules for hazardous materials

Only restrictions applicable to specified hazardous materials will be shown. If at least one hazardous material of any type is present in the list, all available tunnel category restrictions will be displayed. In order to filter-out non-applicable tunnel categories, a tunnel category, that applies to the vehicle, can be specified additionally.

Examples:

- If the `MapContentSettings.configureVehicleRestrictionFilter.hazardousMaterials` contains <a href="sdk-for-flutter-navigate-transport-hazardousmaterial">HazardousMaterial.poison</a> and <a href="sdk-for-flutter-navigate-transport-hazardousmaterial">HazardousMaterial.gas</a>, then only material restrictions for poison and gas will be displayed.
- If the `MapContentSettings.configureVehicleRestrictionFilter.hazardousMaterials` list is empty, then no material restrictions will be shown.
- If the `MapContentSettings.configureVehicleRestrictionFilter.hazardousMaterials` list is not supplied at all (is `null`), then no material restrictions will be shown.
- If the `MapContentSettings.configureVehicleRestrictionFilter.hazardousMaterials` contains at least one hazardous material of any type and `MapContentSettings.configureVehicleRestrictionFilter.tunnelCategory` is `null`, then only corresponding material restrictions will be displayed together with all available tunnel categories.

# Filtering rules for tunnel category

Tunnel categories are labeled and rated based on the level of restriction they provide. The lowest level of restriction is <a href="sdk-for-flutter-navigate-transport-tunnelcategory">TunnelCategory.b</a>, the highest and most restrictive one is <a href="sdk-for-flutter-navigate-transport-tunnelcategory">TunnelCategory.e</a>.

Specifying tunnel category means that:

- The truck carries goods which could cause only the additional dangerous effects described in specified tunnel category and other categories below it with lower level of restriction.
- The truck does not carry goods that could cause the dangerous effects described in tunnel categories above with higher restriction levels than the one specified.

Tunnel categories are closely related to hazardous materials.

Since the type of hazardous material alone does not define the exact level of danger, to ensure comprehensive coverage; the HERE SDK follows:

- If at least one hazardous material is specified but no `MapContentSettings.configureVehicleRestrictionFilter.tunnelCategory` is provided, the SDK enables and displays **all tunnel category restrictions** to ensure that no relevant restrictions are omitted.
- If both hazardous materials and a `MapContentSettings.configureVehicleRestrictionFilter.tunnelCategory` are specified, the SDK **strictly follows the given tunnel category parameter** and displays only the applicable restrictions.

Example: If `MapContentSettings.configureVehicleRestrictionFilter.tunnelCategory` is set to <a href="sdk-for-flutter-navigate-transport-tunnelcategory">TunnelCategory.d</a>, then restrictions for tunnel category <a href="sdk-for-flutter-navigate-transport-tunnelcategory">TunnelCategory.e</a> and <a href="sdk-for-flutter-navigate-transport-tunnelcategory">TunnelCategory.d</a> will be displayed, but not the categories <a href="sdk-for-flutter-navigate-transport-tunnelcategory">TunnelCategory.b</a> and <a href="sdk-for-flutter-navigate-transport-tunnelcategory">TunnelCategory.c</a>.

- `transportMode` Specifies the current transport type. Currently, it's used to distinguish between truck and other transport modes. This distinction ensures consistency between the routing logic and the information displayed on the map. At present, this is primarily used to suppress the generic truck restriction icon.

- `truckSpecifications` The size, weight, type and trailer count specifications to filter for, so that only restrictions which are relevant for the given specifications are displayed.

- `hazardousMaterials` The hazardous materials to filter for, so that only applicable restrictions are displayed. When the list is `null` or empty, then no material restrictions will be displayed.

- `tunnelCategory` The tunnel category to filter for, so that only applicable restrictions are displayed. If `null`, then no tunnel category restrictions will be displayed.

</div>

## Implementation

``` dart
@Deprecated("Will be removed in v4.28.0, use [MapContentSettings.configureVehicleRestrictionFilterWithTransportSpecification] instead.")

static void configureVehicleRestrictionFilter(TransportMode transportMode, TruckSpecifications truckSpecifications, List<HazardousMaterial>? hazardousMaterials, TunnelCategory? tunnelCategory) => $prototype.configureVehicleRestrictionFilter(transportMode, truckSpecifications, hazardousMaterials, tunnelCategory);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
