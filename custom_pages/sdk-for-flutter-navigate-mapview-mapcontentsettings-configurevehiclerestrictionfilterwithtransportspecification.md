---
title: "configureVehicleRestrictionFilterWithTransportSpecification method - MapContentSettings class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapcontentsettings-configurevehiclerestrictionfilterwithtransportspecification"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapContentSettings-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">configureVehicleRestrictionFilterWithTransportSpecification</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">configureVehicleRestrictionFilterWithTransportSpecification</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-configureVehicleRestrictionFilterWithTransportSpecification-param-transportSpecs" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a></span> <span class="parameter-name">transportSpecs</span></span>

)

</div>

<div class="section desc markdown">

Configures a filter for <a href="sdk-for-flutter-navigate-mapview-mapfeatures-vehiclerestrictions">MapFeatures.vehicleRestrictions</a> to show only the restrictions matching the transport specifications when the feature is enabled.

This method provides a unified way to configure vehicle restriction filters using a single <a href="sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a> parameter. This allows you to use the same transport configuration for both routing and map rendering, ensuring consistency between route calculation and the restrictions displayed on the map.

The method extracts the transport mode, vehicle specifications, hazardous materials, and tunnel category from the `MapContentSettings.configureVehicleRestrictionFilterWithTransportSpecification.transportSpecs` parameter and applies filtering according to the same rules described below.

# Filtering rules for transport mode

The transport mode is used to distinguish between truck and other transport modes. This distinction ensures consistency between the routing logic and the information displayed on the map. At present, this is primarily used to suppress the generic truck restriction icon for non-truck modes.

Currently, only vehicle-related restrictions are supported. For pedestrian, scooter, or taxi transport modes, the transport mode information is used, but no additional vehicle-specific restrictions are applied.

# Filtering rules for vehicle specifications

Only restrictions applicable to the vehicle specifications will be shown. The vehicle specifications include dimensions (height, width, length), weights (gross weight, weight per axle), and trailer count.

Examples:

- If the height in vehicle specifications is set to 200 cm, then height restrictions with a height greater than 200 cm will not be displayed.
- If the trailer count in vehicle specifications is set to 2, then trailer restrictions for a count greater than 2 will not be displayed.

# Filtering rules for hazardous materials

Only restrictions applicable to specified hazardous materials will be shown. Hazardous materials are specified within the <a href="sdk-for-flutter-navigate-transport-vehiclespecification-class">VehicleSpecification</a> contained in the `MapContentSettings.configureVehicleRestrictionFilterWithTransportSpecification.transportSpecs` parameter.

If at least one hazardous material of any type is present in the list, all available tunnel category restrictions will be displayed. In order to filter-out non-applicable tunnel categories, a tunnel category that applies to the vehicle can be specified additionally.

Examples:

- If the hazardous materials list contains <a href="sdk-for-flutter-navigate-transport-hazardousmaterial">HazardousMaterial.poison</a> and <a href="sdk-for-flutter-navigate-transport-hazardousmaterial">HazardousMaterial.gas</a>, then only material restrictions for poison and gas will be displayed.
- If the hazardous materials list is empty, then no material restrictions will be shown.
- If the hazardous materials list is not supplied at all (is `null`), then no material restrictions will be shown.
- If the hazardous materials list contains at least one hazardous material of any type and tunnel category is `null`, then only corresponding material restrictions will be displayed together with all available tunnel categories.

# Filtering rules for tunnel category

Tunnel categories are labeled and rated based on the level of restriction they provide. The lowest level of restriction is <a href="sdk-for-flutter-navigate-transport-tunnelcategory">TunnelCategory.b</a>, the highest and most restrictive one is <a href="sdk-for-flutter-navigate-transport-tunnelcategory">TunnelCategory.e</a>.

The tunnel category is specified within the <a href="sdk-for-flutter-navigate-transport-vehiclespecification-class">VehicleSpecification</a> contained in the `MapContentSettings.configureVehicleRestrictionFilterWithTransportSpecification.transportSpecs` parameter.

Specifying tunnel category means that:

- The vehicle carries goods which could cause only the additional dangerous effects described in specified tunnel category and other categories below it with lower level of restriction.
- The vehicle does not carry goods that could cause the dangerous effects described in tunnel categories above with higher restriction levels than the one specified.

Tunnel categories are closely related to hazardous materials.

Since the type of hazardous material alone does not define the exact level of danger, to ensure comprehensive coverage; the HERE SDK follows:

- If at least one hazardous material is specified but no tunnel category is provided, the SDK enables and displays **all tunnel category restrictions** to ensure that no relevant restrictions are omitted.
- If both hazardous materials and a tunnel category are specified, the SDK **strictly follows the given tunnel category parameter** and displays only the applicable restrictions.

Example: If tunnel category is set to <a href="sdk-for-flutter-navigate-transport-tunnelcategory">TunnelCategory.d</a>, then restrictions for tunnel category <a href="sdk-for-flutter-navigate-transport-tunnelcategory">TunnelCategory.e</a> and <a href="sdk-for-flutter-navigate-transport-tunnelcategory">TunnelCategory.d</a> will be displayed, but not the categories <a href="sdk-for-flutter-navigate-transport-tunnelcategory">TunnelCategory.b</a> and <a href="sdk-for-flutter-navigate-transport-tunnelcategory">TunnelCategory.c</a>.

- `transportSpecs` The transport specification containing the transport mode and vehicle specifications. For vehicle modes (car, truck, bus), the <a href="sdk-for-flutter-navigate-transport-vehiclespecification-class">VehicleSpecification</a> within this parameter provides dimensions, weights, hazardous materials, and tunnel category information used for filtering. The same <a href="sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a> object can be used for both routing configuration and map rendering to ensure consistency.

</div>

## Implementation

``` dart
static void configureVehicleRestrictionFilterWithTransportSpecification(TransportSpecification transportSpecs) => $prototype.configureVehicleRestrictionFilterWithTransportSpecification(transportSpecs);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

