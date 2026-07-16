---
title: "MapContentSettings Class Reference"
slug: "sdk-for-ios-explore-classes-mapcontentsettings"
---

# MapContentSettings

<div class="declaration">

<div class="language">

``` highlight
public class MapContentSettings
```

``` highlight
extension MapContentSettings: NativeBase
```

``` highlight
extension MapContentSettings: Hashable
```

</div>

</div>

Provides settings regarding map data which are applied globally to all map views. The settings can already be changed before a map view instance is created.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18MapContentSettingsC25TrafficRefreshPeriodErrora"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Alias-TrafficRefreshPeriodError" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcontentsettings#sdk-for-ios-explore-s-7heresdk18MapContentSettingsC25TrafficRefreshPeriodErrora" class="token"><code>TrafficRefreshPeriodError</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Traffic refresh period error exception

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias TrafficRefreshPeriodError = TrafficRefreshPeriodErrorCode
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapcontentsettings-trafficrefreshperioderrorcode">TrafficRefreshPeriodErrorCode</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18MapContentSettingsC29TrafficRefreshPeriodErrorCodeO"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Enum-TrafficRefreshPeriodErrorCode" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcontentsettings#sdk-for-ios-explore-s-7heresdk18MapContentSettingsC29TrafficRefreshPeriodErrorCodeO" class="token"><code>TrafficRefreshPeriodErrorCode</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Traffic refresh period error code

  <a href="sdk-for-ios-explore-classes-mapcontentsettings-trafficrefreshperioderrorcode" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum TrafficRefreshPeriodErrorCode : UInt32, CaseIterable, Codable
  ```

  ``` highlight
  extension MapContentSettings.TrafficRefreshPeriodErrorCode : Error
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapcontentsettings">MapContentSettings</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18MapContentSettingsC33configureVehicleRestrictionFilter13transportMode19truckSpecifications18hazardousMaterials14tunnelCategoryyAA09TransportJ0O_AA05TruckL0VSayAA17HazardousMaterialOGSgAA06TunnelP0OSgtFZ"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-configureVehicleRestrictionFilter-transportMode-truckSpecifications-hazardousMaterials-tunnelCategory" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcontentsettings#sdk-for-ios-explore-s-7heresdk18MapContentSettingsC33configureVehicleRestrictionFilter13transportMode19truckSpecifications18hazardousMaterials14tunnelCategoryyAA09TransportJ0O_AA05TruckL0VSayAA17HazardousMaterialOGSgAA06TunnelP0OSgtFZ" class="token"><code>configureVehicleRestrictionFilter(transportMode:</code><wbr></wbr><code>truckSpecifications:</code><wbr></wbr><code>hazardousMaterials:</code><wbr></wbr><code>tunnelCategory:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configure a filter for <a href="sdk-for-ios-explore-structs-mapfeatures#sdk-for-ios-explore-s-7heresdk11MapFeaturesV19vehicleRestrictionsSSvpZ">`MapFeatures.vehicleRestrictions`</a> to show only the restrictions matching the specified criteria when the feature is enabled.

  # Filtering rules for truck specifications

  Only restrictions applicable to the supplied truck specifications will be shown.

  Examples:

  - If the height in

        MapContentSettings.configureVehicleRestrictionFilter(TransportMode, TruckSpecifications, [HazardousMaterial]?, TunnelCategory?).truckSpecifications

    is set to 200 cm, then height restrictions with a height greater than 200 cm will not be displayed.

  - If the trailer count in

        MapContentSettings.configureVehicleRestrictionFilter(TransportMode, TruckSpecifications, [HazardousMaterial]?, TunnelCategory?).truckSpecifications

    is set to 2, then trailer restrictions for a count greater than 2 will not be displayed.

  # Filtering rules for hazardous materials

  Only restrictions applicable to specified hazardous materials will be shown. If at least one hazardous material of any type is present in the list, all available tunnel category restrictions will be displayed. In order to filter-out non-applicable tunnel categories, a tunnel category, that applies to the vehicle, can be specified additionally.

  Examples:

  - If the

        MapContentSettings.configureVehicleRestrictionFilter(TransportMode, TruckSpecifications, [HazardousMaterial]?, TunnelCategory?).hazardousMaterials

    contains <a href="sdk-for-ios-explore-enums-hazardousmaterial#sdk-for-ios-explore-s-7heresdk17HazardousMaterialO6poisonyA2CmF">`HazardousMaterial.poison`</a> and <a href="sdk-for-ios-explore-enums-hazardousmaterial#sdk-for-ios-explore-s-7heresdk17HazardousMaterialO3gasyA2CmF">`HazardousMaterial.gas`</a>, then only material restrictions for poison and gas will be displayed.

  - If the

        MapContentSettings.configureVehicleRestrictionFilter(TransportMode, TruckSpecifications, [HazardousMaterial]?, TunnelCategory?).hazardousMaterials

    list is empty, then no material restrictions will be shown.

  - If the

        MapContentSettings.configureVehicleRestrictionFilter(TransportMode, TruckSpecifications, [HazardousMaterial]?, TunnelCategory?).hazardousMaterials

    list is not supplied at all (is `nil`), then no material restrictions will be shown.

  - If the

        MapContentSettings.configureVehicleRestrictionFilter(TransportMode, TruckSpecifications, [HazardousMaterial]?, TunnelCategory?).hazardousMaterials

    contains at least one hazardous material of any type and

        MapContentSettings.configureVehicleRestrictionFilter(TransportMode, TruckSpecifications, [HazardousMaterial]?, TunnelCategory?).tunnelCategory

    is `nil`, then only corresponding material restrictions will be displayed together with all available tunnel categories.

  # Filtering rules for tunnel category

  Tunnel categories are labeled and rated based on the level of restriction they provide. The lowest level of restriction is <a href="sdk-for-ios-explore-enums-tunnelcategory#sdk-for-ios-explore-s-7heresdk14TunnelCategoryO1byA2CmF">`TunnelCategory.b`</a>, the highest and most restrictive one is <a href="sdk-for-ios-explore-enums-tunnelcategory#sdk-for-ios-explore-s-7heresdk14TunnelCategoryO1eyA2CmF">`TunnelCategory.e`</a>.

  Specifying tunnel category means that:

  - The truck carries goods which could cause only the additional dangerous effects described in specified tunnel category and other categories below it with lower level of restriction.
  - The truck does not carry goods that could cause the dangerous effects described in tunnel categories above with higher restriction levels than the one specified.

  Tunnel categories are closely related to hazardous materials.

  Since the type of hazardous material alone does not define the exact level of danger, to ensure comprehensive coverage; the HERE SDK follows:

  - If at least one hazardous material is specified but no

        MapContentSettings.configureVehicleRestrictionFilter(TransportMode, TruckSpecifications, [HazardousMaterial]?, TunnelCategory?).tunnelCategory

    is provided, the SDK enables and displays **all tunnel category restrictions** to ensure that no relevant restrictions are omitted.

  - If both hazardous materials and a

        MapContentSettings.configureVehicleRestrictionFilter(TransportMode, TruckSpecifications, [HazardousMaterial]?, TunnelCategory?).tunnelCategory

    are specified, the SDK **strictly follows the given tunnel category parameter** and displays only the applicable restrictions.

  Example: If

      MapContentSettings.configureVehicleRestrictionFilter(TransportMode, TruckSpecifications, [HazardousMaterial]?, TunnelCategory?).tunnelCategory

  is set to <a href="sdk-for-ios-explore-enums-tunnelcategory#sdk-for-ios-explore-s-7heresdk14TunnelCategoryO1dyA2CmF">`TunnelCategory.d`</a>, then restrictions for tunnel category <a href="sdk-for-ios-explore-enums-tunnelcategory#sdk-for-ios-explore-s-7heresdk14TunnelCategoryO1eyA2CmF">`TunnelCategory.e`</a> and <a href="sdk-for-ios-explore-enums-tunnelcategory#sdk-for-ios-explore-s-7heresdk14TunnelCategoryO1dyA2CmF">`TunnelCategory.d`</a> will be displayed, but not the categories <a href="sdk-for-ios-explore-enums-tunnelcategory#sdk-for-ios-explore-s-7heresdk14TunnelCategoryO1byA2CmF">`TunnelCategory.b`</a> and <a href="sdk-for-ios-explore-enums-tunnelcategory#sdk-for-ios-explore-s-7heresdk14TunnelCategoryO1cyA2CmF">`TunnelCategory.c`</a>.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @available(*, deprecated, message: "Will be removed in v4.28.0, use `MapContentSettings.configureVehicleRestrictionFilter(TransportSpecification﹚` instead.")
  public static func configureVehicleRestrictionFilter(transportMode: TransportMode, truckSpecifications: TruckSpecifications, hazardousMaterials: [HazardousMaterial]?, tunnelCategory: TunnelCategory?)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-transportmode">TransportMode</a>
  - <a href="sdk-for-ios-explore-structs-truckspecifications">TruckSpecifications</a>
  - <a href="sdk-for-ios-explore-enums-hazardousmaterial">HazardousMaterial</a>
  - <a href="sdk-for-ios-explore-enums-tunnelcategory">TunnelCategory</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>transportMode</code></em><code> </code></td>
  <td><div>
  <p>Specifies the current transport type. Currently, it’s used to distinguish between truck and other transport modes. This distinction ensures consistency between the routing logic and the information displayed on the map. At present, this is primarily used to suppress the generic truck restriction icon.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>truckSpecifications</code></em><code> </code></td>
  <td><div>
  <p>The size, weight, type and trailer count specifications to filter for, so that only restrictions which are relevant for the given specifications are displayed.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>hazardousMaterials</code></em><code> </code></td>
  <td><div>
  <p>The hazardous materials to filter for, so that only applicable restrictions are displayed. When the list is <code>nil</code> or empty, then no material restrictions will be displayed.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>tunnelCategory</code></em><code> </code></td>
  <td><div>
  <p>The tunnel category to filter for, so that only applicable restrictions are displayed. If <code>nil</code>, then no tunnel category restrictions will be displayed.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18MapContentSettingsC33configureVehicleRestrictionFilter14transportSpecsyAA22TransportSpecificationV_tFZ"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-configureVehicleRestrictionFilter-transportSpecs" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcontentsettings#sdk-for-ios-explore-s-7heresdk18MapContentSettingsC33configureVehicleRestrictionFilter14transportSpecsyAA22TransportSpecificationV_tFZ" class="token"><code>configureVehicleRestrictionFilter(transportSpecs:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configures a filter for <a href="sdk-for-ios-explore-structs-mapfeatures#sdk-for-ios-explore-s-7heresdk11MapFeaturesV19vehicleRestrictionsSSvpZ">`MapFeatures.vehicleRestrictions`</a> to show only the restrictions matching the transport specifications when the feature is enabled.

  This method provides a unified way to configure vehicle restriction filters using a single <a href="sdk-for-ios-explore-structs-transportspecification">`TransportSpecification`</a> parameter. This allows you to use the same transport configuration for both routing and map rendering, ensuring consistency between route calculation and the restrictions displayed on the map.

  The method extracts the transport mode, vehicle specifications, hazardous materials, and tunnel category from the

      MapContentSettings.configureVehicleRestrictionFilter(TransportSpecification).transportSpecs

  parameter and applies filtering according to the same rules described below.
  </p>

  # Filtering rules for transport mode

  The transport mode is used to distinguish between truck and other transport modes. This distinction ensures consistency between the routing logic and the information displayed on the map. At present, this is primarily used to suppress the generic truck restriction icon for non-truck modes.

  Currently, only vehicle-related restrictions are supported. For pedestrian, scooter, or taxi transport modes, the transport mode information is used, but no additional vehicle-specific restrictions are applied.

  # Filtering rules for vehicle specifications

  Only restrictions applicable to the vehicle specifications will be shown. The vehicle specifications include dimensions (height, width, length), weights (gross weight, weight per axle), and trailer count.

  Examples:

  - If the height in vehicle specifications is set to 200 cm, then height restrictions with a height greater than 200 cm will not be displayed.
  - If the trailer count in vehicle specifications is set to 2, then trailer restrictions for a count greater than 2 will not be displayed.

  # Filtering rules for hazardous materials

  Only restrictions applicable to specified hazardous materials will be shown. Hazardous materials are specified within the <a href="sdk-for-ios-explore-structs-vehiclespecification">`VehicleSpecification`</a> contained in the

      MapContentSettings.configureVehicleRestrictionFilter(TransportSpecification).transportSpecs

  parameter.
  </p>

  If at least one hazardous material of any type is present in the list, all available tunnel category restrictions will be displayed. In order to filter-out non-applicable tunnel categories, a tunnel category that applies to the vehicle can be specified additionally.

  Examples:

  - If the hazardous materials list contains <a href="sdk-for-ios-explore-enums-hazardousmaterial#sdk-for-ios-explore-s-7heresdk17HazardousMaterialO6poisonyA2CmF">`HazardousMaterial.poison`</a> and <a href="sdk-for-ios-explore-enums-hazardousmaterial#sdk-for-ios-explore-s-7heresdk17HazardousMaterialO3gasyA2CmF">`HazardousMaterial.gas`</a>, then only material restrictions for poison and gas will be displayed.
  - If the hazardous materials list is empty, then no material restrictions will be shown.
  - If the hazardous materials list is not supplied at all (is `nil`), then no material restrictions will be shown.
  - If the hazardous materials list contains at least one hazardous material of any type and tunnel category is `nil`, then only corresponding material restrictions will be displayed together with all available tunnel categories.

  # Filtering rules for tunnel category

  Tunnel categories are labeled and rated based on the level of restriction they provide. The lowest level of restriction is <a href="sdk-for-ios-explore-enums-tunnelcategory#sdk-for-ios-explore-s-7heresdk14TunnelCategoryO1byA2CmF">`TunnelCategory.b`</a>, the highest and most restrictive one is <a href="sdk-for-ios-explore-enums-tunnelcategory#sdk-for-ios-explore-s-7heresdk14TunnelCategoryO1eyA2CmF">`TunnelCategory.e`</a>.

  The tunnel category is specified within the <a href="sdk-for-ios-explore-structs-vehiclespecification">`VehicleSpecification`</a> contained in the

      MapContentSettings.configureVehicleRestrictionFilter(TransportSpecification).transportSpecs

  parameter.
  </p>

  Specifying tunnel category means that:

  - The vehicle carries goods which could cause only the additional dangerous effects described in specified tunnel category and other categories below it with lower level of restriction.
  - The vehicle does not carry goods that could cause the dangerous effects described in tunnel categories above with higher restriction levels than the one specified.

  Tunnel categories are closely related to hazardous materials.

  Since the type of hazardous material alone does not define the exact level of danger, to ensure comprehensive coverage; the HERE SDK follows:

  - If at least one hazardous material is specified but no tunnel category is provided, the SDK enables and displays **all tunnel category restrictions** to ensure that no relevant restrictions are omitted.
  - If both hazardous materials and a tunnel category are specified, the SDK **strictly follows the given tunnel category parameter** and displays only the applicable restrictions.

  Example: If tunnel category is set to <a href="sdk-for-ios-explore-enums-tunnelcategory#sdk-for-ios-explore-s-7heresdk14TunnelCategoryO1dyA2CmF">`TunnelCategory.d`</a>, then restrictions for tunnel category <a href="sdk-for-ios-explore-enums-tunnelcategory#sdk-for-ios-explore-s-7heresdk14TunnelCategoryO1eyA2CmF">`TunnelCategory.e`</a> and <a href="sdk-for-ios-explore-enums-tunnelcategory#sdk-for-ios-explore-s-7heresdk14TunnelCategoryO1dyA2CmF">`TunnelCategory.d`</a> will be displayed, but not the categories <a href="sdk-for-ios-explore-enums-tunnelcategory#sdk-for-ios-explore-s-7heresdk14TunnelCategoryO1byA2CmF">`TunnelCategory.b`</a> and <a href="sdk-for-ios-explore-enums-tunnelcategory#sdk-for-ios-explore-s-7heresdk14TunnelCategoryO1cyA2CmF">`TunnelCategory.c`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func configureVehicleRestrictionFilter(transportSpecs: TransportSpecification)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-transportspecification">TransportSpecification</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>transportSpecs</code></em><code> </code></td>
  <td><div>
  <p>The transport specification containing the transport mode and vehicle specifications. For vehicle modes (car, truck, bus), the <a href="sdk-for-ios-explore-structs-vehiclespecification"><code>VehicleSpecification</code></a> within this parameter provides dimensions, weights, hazardous materials, and tunnel category information used for filtering. The same <a href="sdk-for-ios-explore-structs-transportspecification"><code>TransportSpecification</code></a> object can be used for both routing configuration and map rendering to ensure consistency.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18MapContentSettingsC29resetVehicleRestrictionFilteryyFZ"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-resetVehicleRestrictionFilter" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcontentsettings#sdk-for-ios-explore-s-7heresdk18MapContentSettingsC29resetVehicleRestrictionFilteryyFZ" class="token"><code>resetVehicleRestrictionFilter()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes all filters regarding vehicle restrictions so that all restrictions will be displayed, when the display of vehicle restrictions is enabled by enabling feature using <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC14enableFeaturesyySDyS2SGF">`MapScene.enableFeatures(...)`</a> with <a href="sdk-for-ios-explore-structs-mapfeatures#sdk-for-ios-explore-s-7heresdk11MapFeaturesV19vehicleRestrictionsSSvpZ">`MapFeatures.vehicleRestrictions`</a> and setting layer visibility using <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC18setLayerVisibility9layerName10visibilityySS_AA0F5StateOtF">`MapScene.setLayerVisibility(...)`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func resetVehicleRestrictionFilter()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18MapContentSettingsC26setPoiCategoriesVisibility11categoryIds10visibilityySaySSG_AA0H5StateOtFZ"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-setPoiCategoriesVisibility-categoryIds-visibility" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcontentsettings#sdk-for-ios-explore-s-7heresdk18MapContentSettingsC26setPoiCategoriesVisibility11categoryIds10visibilityySaySSG_AA0H5StateOtFZ" class="token"><code>setPoiCategoriesVisibility(categoryIds:</code><wbr></wbr><code>visibility:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets visibility for embedded carto POI categories (points of interest that are visible on the map, by default). For HERE standard map schemes all available POI categories are visible by default for each selected map scheme. Note that not all POI categories are available for all map schemes.

  Based on the given list of categories the number of shown carto POIs can be reduced. To find all possible POI category strings look into `here.sdk.search.PlaceCategory`. Note that it is enough to hide a main category like “100” (eat-and-drink) to also affect sub categories such as “100-1000” (eat-and-drink-restaurant) and “100-1100” (eat-and-drink-coffee-tea). To enable a sub category, also the related main categories need have the `VISIBLE` state.

  The POI visibility is a property of the map data itself. Once set it will be applied to all HERE standard map schemes and the selected categories will remain even when switching a map scheme.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func setPoiCategoriesVisibility(categoryIds: [String], visibility: VisibilityState)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-visibilitystate">VisibilityState</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>categoryIds</code></em><code> </code></td>
  <td><div>
  <p>A list of POI categories that a visibility state is set for.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>visibility</code></em><code> </code></td>
  <td><div>
  <p>A selected visibility for specified POI categories.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18MapContentSettingsC28resetPoiCategoriesVisibilityyyFZ"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-resetPoiCategoriesVisibility" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcontentsettings#sdk-for-ios-explore-s-7heresdk18MapContentSettingsC28resetPoiCategoriesVisibilityyyFZ" class="token"><code>resetPoiCategoriesVisibility()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Resets POI categories visibility to their default state.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func resetPoiCategoriesVisibility()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18MapContentSettingsC22filterTrafficIncidents07trafficG0ySayAA0F12IncidentTypeOG_tFZ"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-filterTrafficIncidents-trafficIncidents" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcontentsettings#sdk-for-ios-explore-s-7heresdk18MapContentSettingsC22filterTrafficIncidents07trafficG0ySayAA0F12IncidentTypeOG_tFZ" class="token"><code>filterTrafficIncidents(trafficIncidents:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Filters the displayed traffic incidents so that only the ones applicable to the specified criteria are shown when general display of traffic incidents is enabled. The display of traffic incidents can be enabled using <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC14enableFeaturesyySDyS2SGF">`MapScene.enableFeatures(...)`</a> with <a href="sdk-for-ios-explore-structs-mapfeatures#sdk-for-ios-explore-s-7heresdk11MapFeaturesV16trafficIncidentsSSvpZ">`MapFeatures.trafficIncidents`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func filterTrafficIncidents(trafficIncidents: [TrafficIncidentType])
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-trafficincidenttype">TrafficIncidentType</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>trafficIncidents</code></em><code> </code></td>
  <td><div>
  <p>The traffic incidents to filter for, so that only applicable incidents are displayed. When the list is empty, then all traffic incidents will be displayed. If the</p>
  <pre><code>MapContentSettings.filterTrafficIncidents(...).trafficIncidents</code></pre>
  contains <a href="sdk-for-ios-explore-enums-trafficincidenttype#sdk-for-ios-explore-s-7heresdk19TrafficIncidentTypeO7unknownyA2CmF"><code>TrafficIncidentType.unknown</code></a>, then the traffic filter will be applied ignoring this element.
  </p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18MapContentSettingsC26resetTrafficIncidentFilteryyFZ"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-resetTrafficIncidentFilter" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcontentsettings#sdk-for-ios-explore-s-7heresdk18MapContentSettingsC26resetTrafficIncidentFilteryyFZ" class="token"><code>resetTrafficIncidentFilter()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes all filters regarding Traffic Incidents so that all incidents will be displayed, when the display of Traffic Incidents is enabled using <a href="sdk-for-ios-explore-classes-mapscene#sdk-for-ios-explore-s-7heresdk8MapSceneC14enableFeaturesyySDyS2SGF">`MapScene.enableFeatures(...)`</a> with <a href="sdk-for-ios-explore-structs-mapfeatures#sdk-for-ios-explore-s-7heresdk11MapFeaturesV16trafficIncidentsSSvpZ">`MapFeatures.trafficIncidents`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func resetTrafficIncidentFilter()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18MapContentSettingsC23setTrafficRefreshPeriodyySdKFZ"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-setTrafficRefreshPeriod-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcontentsettings#sdk-for-ios-explore-s-7heresdk18MapContentSettingsC23setTrafficRefreshPeriodyySdKFZ" class="token"><code>setTrafficRefreshPeriod(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the traffic data refresh period for both <a href="sdk-for-ios-explore-structs-mapfeatures#sdk-for-ios-explore-s-7heresdk11MapFeaturesV11trafficFlowSSvpZ">`MapFeatures.trafficFlow`</a> and <a href="sdk-for-ios-explore-structs-mapfeatures#sdk-for-ios-explore-s-7heresdk11MapFeaturesV16trafficIncidentsSSvpZ">`MapFeatures.trafficIncidents`</a>. By default, the traffic information validity time and the refresh period is derived from the refresh period of HERE’s traffic server. The period set by this function will override the server’s default setting for upcoming traffic data requests. Defaults to 60 seconds.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-explore-classes-mapcontentsettings#sdk-for-ios-explore-s-7heresdk18MapContentSettingsC25TrafficRefreshPeriodErrora">`MapContentSettings.TrafficRefreshPeriodError`</a> <a href="sdk-for-ios-explore-classes-mapcontentsettings#sdk-for-ios-explore-s-7heresdk18MapContentSettingsC25TrafficRefreshPeriodErrora">`MapContentSettings.TrafficRefreshPeriodError`</a> indicates what went wrong.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func setTrafficRefreshPeriod(_ value: TimeInterval) throws
  ```

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>value</code></em><code> </code></td>
  <td><div>
  <p>Traffic data refresh period in seconds. Valid range is [60, 300] seconds. The shortest refresh period that can be set is 60 seconds. This means that the traffic data shown on a map view will be refreshed every minute. The longest refresh period that can be set is 300 seconds. This means that the traffic data shown on the current map view will be refreshed every 5 minutes if the viewport does not change. Note that when a viewport change occurs, new traffic data may be requested regardless of the set refresh period. For example, during turn-by-turn navigation, frequent viewport changes can result in missing traffic data, causing new requests to be made more often.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18MapContentSettingsC25resetTrafficRefreshPeriodyyFZ"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-resetTrafficRefreshPeriod" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcontentsettings#sdk-for-ios-explore-s-7heresdk18MapContentSettingsC25resetTrafficRefreshPeriodyyFZ" class="token"><code>resetTrafficRefreshPeriod()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Resets the traffic data (both flow and incidents) refresh period so the default traffic information validity time and the refresh period derived from the refresh period of the traffic server is used.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func resetTrafficRefreshPeriod()
  ```

  </div>

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

