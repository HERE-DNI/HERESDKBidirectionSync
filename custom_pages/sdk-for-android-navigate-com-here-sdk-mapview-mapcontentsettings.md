---
title: "MapContentSettings (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapcontentsettings"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-mapview-package-summary">com.here.sdk.mapview</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.mapview.MapContentSettings → com.here.NativeBase com.here.sdk.mapview.MapContentSettings → com.here.sdk.mapview.MapContentSettings

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">MapContentSettings</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

Provides settings regarding map data which are applied globally to all map views. The settings can already be changed before a map view instance is created.

</div>

</div>

- <div id="sdk-for-android-navigate-nested-class-summary" class="section nested-class-summary">

  <div class="caption">

  Nested Classes

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Class

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  `static enum `

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontentsettings-trafficrefreshperioderrorcode" class="type-name-link" title="enum class in com.here.sdk.mapview"><code>MapContentSettings.TrafficRefreshPeriodErrorCode</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Traffic refresh period error code

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final class `

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontentsettings-trafficrefreshperiodexception" class="type-name-link" title="class in com.here.sdk.mapview"><code>MapContentSettings.TrafficRefreshPeriodException</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Traffic refresh period error exception

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div id="sdk-for-android-navigate-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">

  `static void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">

      configureVehicleRestrictionFilter ( TransportMode transportMode, TruckSpecifications truckSpecifications, List < HazardousMaterial > hazardousMaterials, TunnelCategory tunnelCategory)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0, use configureVehicleRestrictionFilter(TransportSpecification) instead.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      configureVehicleRestrictionFilter ( TransportSpecification transportSpecs)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Configures a filter for MapFeatures.VEHICLE_RESTRICTIONS to show only the restrictions matching the transport specifications when the feature is enabled.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      filterTrafficIncidents ( List < TrafficIncidentType > trafficIncidents)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Filters the displayed traffic incidents so that only the ones applicable to the specified criteria are shown when general display of traffic incidents is enabled.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      resetPoiCategoriesVisibility ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Resets POI categories visibility to their default state.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      resetTrafficIncidentFilter ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Removes all filters regarding Traffic Incidents so that all incidents will be displayed, when the display of Traffic Incidents is enabled using MapScene.enableFeatures(java.util.Map\<java.lang.String, java.lang.String\>) with MapFeatures.TRAFFIC_INCIDENTS .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      resetTrafficRefreshPeriod ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Resets the traffic data (both flow and incidents) refresh period so the default traffic information validity time and the refresh period derived from the refresh period of the traffic server is used.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      resetVehicleRestrictionFilter ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Removes all filters regarding vehicle restrictions so that all restrictions will be displayed, when the display of vehicle restrictions is enabled by enabling feature using MapScene.enableFeatures(java.util.Map\<java.lang.String, java.lang.String\>) with MapFeatures.VEHICLE_RESTRICTIONS and setting layer visibility using MapScene.setLayerVisibility(java.lang.String, com.here.sdk.mapview.VisibilityState) .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      setPoiCategoriesVisibility ( List < String > categoryIds, VisibilityState visibility)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Sets visibility for embedded carto POI categories (points of interest that are visible on the map, by default).

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      setTrafficRefreshPeriod ( Duration value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Sets the traffic data refresh period for both MapFeatures.TRAFFIC_FLOW and MapFeatures.TRAFFIC_INCIDENTS .

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-configureVehicleRestrictionFilter-com-here-sdk-transport-TransportMode-com-here-sdk-transport-TruckSpecifications-java-util-List-com-here-sdk-transport-TunnelCategory" class="section detail">

    ### configureVehicleRestrictionFilter

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> </span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">configureVehicleRestrictionFilter</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode" title="enum class in com.here.sdk.transport">TransportMode</a> transportMode, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-transport-truckspecifications" title="class in com.here.sdk.transport">TruckSpecifications</a> truckSpecifications, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-transport-hazardousmaterial" title="enum class in com.here.sdk.transport">HazardousMaterial</a>\> hazardousMaterials, @Nullable <a href="sdk-for-android-navigate-com-here-sdk-transport-tunnelcategory" title="enum class in com.here.sdk.transport">TunnelCategory</a> tunnelCategory)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0, use [](sdk-for-android-navigate-com-here-sdk-mapview-mapcontentsettings#configureVehicleRestrictionFilter(com.here.sdk.transport.TransportSpecification))

        configureVehicleRestrictionFilter(TransportSpecification)

    </a> instead.
    </p>

    </div>

    </div>

    <div class="block">

    Configure a filter for MapFeatures.VEHICLE_RESTRICTIONS to show only the restrictions matching the specified criteria when the feature is enabled. Filtering rules for truck specifications Only restrictions applicable to the supplied truck specifications will be shown. Examples: If the height in truckSpecifications is set to 200 cm, then height restrictions with a height greater than 200 cm will not be displayed. If the trailer count in truckSpecifications is set to 2, then trailer restrictions for a count greater than 2 will not be displayed. Filtering rules for hazardous materials Only restrictions applicable to specified hazardous materials will be shown. If at least one hazardous material of any type is present in the list, all available tunnel category restrictions will be displayed. In order to filter-out non-applicable tunnel categories, a tunnel category, that applies to the vehicle, can be specified additionally. Examples: If the hazardousMaterials contains HazardousMaterial.POISON and HazardousMaterial.GAS , then only material restrictions for poison and gas will be displayed. If the hazardousMaterials list is empty, then no material restrictions will be shown. If the hazardousMaterials list is not supplied at all (is null ), then no material restrictions will be shown. If the hazardousMaterials contains at least one hazardous material of any type and tunnelCategory is null , then only corresponding material restrictions will be displayed together with all available tunnel categories. Filtering rules for tunnel category Tunnel categories are labeled and rated based on the level of restriction they provide. The lowest level of restriction is TunnelCategory.B , the highest and most restrictive one is TunnelCategory.E . Specifying tunnel category means that: The truck carries goods which could cause only the additional dangerous effects described in specified tunnel category and other categories below it with lower level of restriction. The truck does not carry goods that could cause the dangerous effects described in tunnel categories above with higher restriction levels than the one specified. Tunnel categories are closely related to hazardous materials. Since the type of hazardous material alone does not define the exact level of danger, to ensure comprehensive coverage; the HERE SDK follows: If at least one hazardous material is specified but no tunnelCategory is provided, the SDK enables and displays all tunnel category restrictions to ensure that no relevant restrictions are omitted. If both hazardous materials and a tunnelCategory are specified, the SDK strictly follows the given tunnel category parameter and displays only the applicable restrictions. Example: If tunnelCategory is set to TunnelCategory.D , then restrictions for tunnel category TunnelCategory.E and TunnelCategory.D will be displayed, but not the categories TunnelCategory.B and TunnelCategory.C .

    </div>

    Parameters:  
    `transportMode` -

    Specifies the current transport type. Currently, it's used to distinguish between truck and other transport modes. This distinction ensures consistency between the routing logic and the information displayed on the map. At present, this is primarily used to suppress the generic truck restriction icon.

    `truckSpecifications` -

    The size, weight, type and trailer count specifications to filter for, so that only restrictions which are relevant for the given specifications are displayed.

    `hazardousMaterials` -

    The hazardous materials to filter for, so that only applicable restrictions are displayed. When the list is `null` or empty, then no material restrictions will be displayed.

    `tunnelCategory` -

    The tunnel category to filter for, so that only applicable restrictions are displayed. If `null`, then no tunnel category restrictions will be displayed.

    </div>

  - <div id="sdk-for-android-navigate-configureVehicleRestrictionFilter-com-here-sdk-transport-TransportSpecification" class="section detail">

    ### configureVehicleRestrictionFilter

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">configureVehicleRestrictionFilter</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-transport-transportspecification" title="class in com.here.sdk.transport">TransportSpecification</a> transportSpecs)</span>

    </div>

    <div class="block">

    Configures a filter for MapFeatures.VEHICLE_RESTRICTIONS to show only the restrictions matching the transport specifications when the feature is enabled. This method provides a unified way to configure vehicle restriction filters using a single TransportSpecification parameter. This allows you to use the same transport configuration for both routing and map rendering, ensuring consistency between route calculation and the restrictions displayed on the map. The method extracts the transport mode, vehicle specifications, hazardous materials, and tunnel category from the transportSpecs parameter and applies filtering according to the same rules described below. Filtering rules for transport mode The transport mode is used to distinguish between truck and other transport modes. This distinction ensures consistency between the routing logic and the information displayed on the map. At present, this is primarily used to suppress the generic truck restriction icon for non-truck modes. Currently, only vehicle-related restrictions are supported. For pedestrian, scooter, or taxi transport modes, the transport mode information is used, but no additional vehicle-specific restrictions are applied. Filtering rules for vehicle specifications Only restrictions applicable to the vehicle specifications will be shown. The vehicle specifications include dimensions (height, width, length), weights (gross weight, weight per axle), and trailer count. Examples: If the height in vehicle specifications is set to 200 cm, then height restrictions with a height greater than 200 cm will not be displayed. If the trailer count in vehicle specifications is set to 2, then trailer restrictions for a count greater than 2 will not be displayed. Filtering rules for hazardous materials Only restrictions applicable to specified hazardous materials will be shown. Hazardous materials are specified within the VehicleSpecification contained in the transportSpecs parameter. If at least one hazardous material of any type is present in the list, all available tunnel category restrictions will be displayed. In order to filter-out non-applicable tunnel categories, a tunnel category that applies to the vehicle can be specified additionally. Examples: If the hazardous materials list contains HazardousMaterial.POISON and HazardousMaterial.GAS , then only material restrictions for poison and gas will be displayed. If the hazardous materials list is empty, then no material restrictions will be shown. If the hazardous materials list is not supplied at all (is null ), then no material restrictions will be shown. If the hazardous materials list contains at least one hazardous material of any type and tunnel category is null , then only corresponding material restrictions will be displayed together with all available tunnel categories. Filtering rules for tunnel category Tunnel categories are labeled and rated based on the level of restriction they provide. The lowest level of restriction is TunnelCategory.B , the highest and most restrictive one is TunnelCategory.E . The tunnel category is specified within the VehicleSpecification contained in the transportSpecs parameter. Specifying tunnel category means that: The vehicle carries goods which could cause only the additional dangerous effects described in specified tunnel category and other categories below it with lower level of restriction. The vehicle does not carry goods that could cause the dangerous effects described in tunnel categories above with higher restriction levels than the one specified. Tunnel categories are closely related to hazardous materials. Since the type of hazardous material alone does not define the exact level of danger, to ensure comprehensive coverage; the HERE SDK follows: If at least one hazardous material is specified but no tunnel category is provided, the SDK enables and displays all tunnel category restrictions to ensure that no relevant restrictions are omitted. If both hazardous materials and a tunnel category are specified, the SDK strictly follows the given tunnel category parameter and displays only the applicable restrictions. Example: If tunnel category is set to TunnelCategory.D , then restrictions for tunnel category TunnelCategory.E and TunnelCategory.D will be displayed, but not the categories TunnelCategory.B and TunnelCategory.C .

    </div>

    Parameters:  
    `transportSpecs` -

    The transport specification containing the transport mode and vehicle specifications. For vehicle modes (car, truck, bus), the <a href="sdk-for-android-navigate-com-here-sdk-transport-vehiclespecification" title="class in com.here.sdk.transport">`VehicleSpecification`</a> within this parameter provides dimensions, weights, hazardous materials, and tunnel category information used for filtering. The same <a href="sdk-for-android-navigate-com-here-sdk-transport-transportspecification" title="class in com.here.sdk.transport">`TransportSpecification`</a> object can be used for both routing configuration and map rendering to ensure consistency.

    </div>

  - <div id="sdk-for-android-navigate-resetVehicleRestrictionFilter" class="section detail">

    ### resetVehicleRestrictionFilter

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">resetVehicleRestrictionFilter</span>()

    </div>

    <div class="block">

    Removes all filters regarding vehicle restrictions so that all restrictions will be displayed, when the display of vehicle restrictions is enabled by enabling feature using MapScene.enableFeatures(java.util.Map\<java.lang.String, java.lang.String\>) with MapFeatures.VEHICLE_RESTRICTIONS and setting layer visibility using MapScene.setLayerVisibility(java.lang.String, com.here.sdk.mapview.VisibilityState) .

    </div>

    </div>

  - <div id="sdk-for-android-navigate-setPoiCategoriesVisibility-java-util-List-com-here-sdk-mapview-VisibilityState" class="section detail">

    ### setPoiCategoriesVisibility

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setPoiCategoriesVisibility</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a>\> categoryIds, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapview-visibilitystate" title="enum class in com.here.sdk.mapview">VisibilityState</a> visibility)</span>

    </div>

    <div class="block">

    Sets visibility for embedded carto POI categories (points of interest that are visible on the map, by default). For HERE standard map schemes all available POI categories are visible by default for each selected map scheme. Note that not all POI categories are available for all map schemes. Based on the given list of categories the number of shown carto POIs can be reduced. To find all possible POI category strings look into here.sdk.search.PlaceCategory . Note that it is enough to hide a main category like "100" (eat-and-drink) to also affect sub categories such as "100-1000" (eat-and-drink-restaurant) and "100-1100" (eat-and-drink-coffee-tea). To enable a sub category, also the related main categories need have the VISIBLE state. The POI visibility is a property of the map data itself. Once set it will be applied to all HERE standard map schemes and the selected categories will remain even when switching a map scheme.

    </div>

    Parameters:  
    `categoryIds` -

    A list of POI categories that a visibility state is set for.

    `visibility` -

    A selected visibility for specified POI categories.

    </div>

  - <div id="sdk-for-android-navigate-resetPoiCategoriesVisibility" class="section detail">

    ### resetPoiCategoriesVisibility

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">resetPoiCategoriesVisibility</span>()

    </div>

    <div class="block">

    Resets POI categories visibility to their default state.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-filterTrafficIncidents-java-util-List" class="section detail">

    ### filterTrafficIncidents

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">filterTrafficIncidents</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincidenttype" title="enum class in com.here.sdk.traffic">TrafficIncidentType</a>\> trafficIncidents)</span>

    </div>

    <div class="block">

    Filters the displayed traffic incidents so that only the ones applicable to the specified criteria are shown when general display of traffic incidents is enabled. The display of traffic incidents can be enabled using MapScene.enableFeatures(java.util.Map\<java.lang.String, java.lang.String\>) with MapFeatures.TRAFFIC_INCIDENTS .

    </div>

    Parameters:  
    `trafficIncidents` -

    The traffic incidents to filter for, so that only applicable incidents are displayed. When the list is empty, then all traffic incidents will be displayed. If the `trafficIncidents` contains <a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincidenttype#UNKNOWN">`TrafficIncidentType.UNKNOWN`</a>, then the traffic filter will be applied ignoring this element.

    </div>

  - <div id="sdk-for-android-navigate-resetTrafficIncidentFilter" class="section detail">

    ### resetTrafficIncidentFilter

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">resetTrafficIncidentFilter</span>()

    </div>

    <div class="block">

    Removes all filters regarding Traffic Incidents so that all incidents will be displayed, when the display of Traffic Incidents is enabled using MapScene.enableFeatures(java.util.Map\<java.lang.String, java.lang.String\>) with MapFeatures.TRAFFIC_INCIDENTS .

    </div>

    </div>

  - <div id="sdk-for-android-navigate-setTrafficRefreshPeriod-com-here-time-Duration" class="section detail">

    ### setTrafficRefreshPeriod

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setTrafficRefreshPeriod</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a> value)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontentsettings-trafficrefreshperiodexception" title="class in com.here.sdk.mapview">MapContentSettings.TrafficRefreshPeriodException</a></span>

    </div>

    <div class="block">

    Sets the traffic data refresh period for both MapFeatures.TRAFFIC_FLOW and MapFeatures.TRAFFIC_INCIDENTS . By default, the traffic information validity time and the refresh period is derived from the refresh period of HERE's traffic server. The period set by this function will override the server's default setting for upcoming traffic data requests. Defaults to 60 seconds.

    </div>

    Parameters:  
    `value` -

    Traffic data refresh period in seconds. Valid range is \[60, 300\] seconds. The shortest refresh period that can be set is 60 seconds. This means that the traffic data shown on a map view will be refreshed every minute. The longest refresh period that can be set is 300 seconds. This means that the traffic data shown on the current map view will be refreshed every 5 minutes if the viewport does not change. Note that when a viewport change occurs, new traffic data may be requested regardless of the set refresh period. For example, during turn-by-turn navigation, frequent viewport changes can result in missing traffic data, causing new requests to be made more often.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontentsettings-trafficrefreshperiodexception" title="class in com.here.sdk.mapview">`MapContentSettings.TrafficRefreshPeriodException`</a> -

    <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontentsettings-trafficrefreshperiodexception" title="class in com.here.sdk.mapview">`MapContentSettings.TrafficRefreshPeriodException`</a> indicates what went wrong.

    </div>

  - <div id="sdk-for-android-navigate-resetTrafficRefreshPeriod" class="section detail">

    ### resetTrafficRefreshPeriod

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">resetTrafficRefreshPeriod</span>()

    </div>

    <div class="block">

    Resets the traffic data (both flow and incidents) refresh period so the default traffic information validity time and the refresh period derived from the refresh period of the traffic server is used.

    </div>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

