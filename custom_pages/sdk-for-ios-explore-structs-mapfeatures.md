---
title: "MapFeatures Structure Reference"
slug: "sdk-for-ios-explore-structs-mapfeatures"
---

# MapFeatures

<div class="declaration">

<div class="language">

``` highlight
public struct MapFeatures
```

</div>

</div>

Holds constants for map features, to be used with

    MapScene.enableFeatures(...)

and

    MapScene.disableFeatures(...)

.
</p>

See <a href="sdk-for-ios-explore-structs-mapfeaturemodes">`MapFeatureModes`</a> for constants representing feature modes.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk11MapFeaturesV17extrudedBuildingsSSvpZ"></span>` `<span id="//apple_ref/swift/Variable/extrudedBuildings" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-mapfeatures#/s:7heresdk11MapFeaturesV17extrudedBuildingsSSvpZ" class="token"><code>extrudedBuildings</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Simple 3D representation of buildings.

  Supports only one mode: <a href="sdk-for-ios-explore-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV20extrudedBuildingsAllSSvpZ">`MapFeatureModes.extrudedBuildingsAll`</a>.

  Not supported for <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO9satelliteyA2CmF">`MapScheme.satellite`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO14roadNetworkDayyA2CmF">`MapScheme.roadNetworkDay`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO16roadNetworkNightyA2CmF">`MapScheme.roadNetworkNight`</a> and all hybrid schemes: <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO9hybridDayyA2CmF">`MapScheme.hybridDay`</a> <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO11hybridNightyA2CmF">`MapScheme.hybridNight`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO13liteHybridDayyA2CmF">`MapScheme.liteHybridDay`</a> <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO15liteHybridNightyA2CmF">`MapScheme.liteHybridNight`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO18logisticsHybridDayyA2CmF">`MapScheme.logisticsHybridDay`</a> and <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO20logisticsHybridNightyA2CmF">`MapScheme.logisticsHybridNight`</a>.

  By default, extruded buildings are enabled on all compatible map schemes.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let extrudedBuildings: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11MapFeaturesV18buildingFootprintsSSvpZ"></span>` `<span id="//apple_ref/swift/Variable/buildingFootprints" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-mapfeatures#/s:7heresdk11MapFeaturesV18buildingFootprintsSSvpZ" class="token"><code>buildingFootprints</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The 2D footprint of buildings.

  Supports only one mode: <a href="sdk-for-ios-explore-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV21buildingFootprintsAllSSvpZ">`MapFeatureModes.buildingFootprintsAll`</a>.

  Not supported for <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO9satelliteyA2CmF">`MapScheme.satellite`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO14roadNetworkDayyA2CmF">`MapScheme.roadNetworkDay`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO16roadNetworkNightyA2CmF">`MapScheme.roadNetworkNight`</a> and all hybrid schemes: <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO9hybridDayyA2CmF">`MapScheme.hybridDay`</a> <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO11hybridNightyA2CmF">`MapScheme.hybridNight`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO13liteHybridDayyA2CmF">`MapScheme.liteHybridDay`</a> <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO15liteHybridNightyA2CmF">`MapScheme.liteHybridNight`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO18logisticsHybridDayyA2CmF">`MapScheme.logisticsHybridDay`</a> and <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO20logisticsHybridNightyA2CmF">`MapScheme.logisticsHybridNight`</a>.

  By default, building footprints are enabled on all compatible map schemes.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let buildingFootprints: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11MapFeaturesV11trafficFlowSSvpZ"></span>` `<span id="//apple_ref/swift/Variable/trafficFlow" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-mapfeatures#/s:7heresdk11MapFeaturesV11trafficFlowSSvpZ" class="token"><code>trafficFlow</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Traffic flow speed. An online connection is required for the traffic flow to be shown.

  If the offline-mode is enabled for offline maps usage, the live traffic flow can still be shown in offline mode by enabling pass-through feature for traffic flow on `sdk.core.engine.SDKNativeEngine`. See `sdk.core.engine.SDKNativeEngine.pass_through_features` for details.

  Supported modes:

  - <a href="sdk-for-ios-explore-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV027trafficFlowJapanWithoutFreeF0SSvpZ">`MapFeatureModes.trafficFlowJapanWithoutFreeFlow`</a>,
  - <a href="sdk-for-ios-explore-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV019trafficFlowWithFreeF0SSvpZ">`MapFeatureModes.trafficFlowWithFreeFlow`</a>,
  - <a href="sdk-for-ios-explore-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV022trafficFlowWithoutFreeF0SSvpZ">`MapFeatureModes.trafficFlowWithoutFreeFlow`</a>.

  Default mode is <a href="sdk-for-ios-explore-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV019trafficFlowWithFreeF0SSvpZ">`MapFeatureModes.trafficFlowWithFreeFlow`</a>.

  Not supported for <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO9satelliteyA2CmF">`MapScheme.satellite`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO14roadNetworkDayyA2CmF">`MapScheme.roadNetworkDay`</a> and <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO16roadNetworkNightyA2CmF">`MapScheme.roadNetworkNight`</a>. By default, this map feature is not enabled.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let trafficFlow: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11MapFeaturesV16trafficIncidentsSSvpZ"></span>` `<span id="//apple_ref/swift/Variable/trafficIncidents" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-mapfeatures#/s:7heresdk11MapFeaturesV16trafficIncidentsSSvpZ" class="token"><code>trafficIncidents</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Traffic incidents. An online connection is required for the traffic incidents to be shown.

  If the offline-mode is enabled for offline maps usage, the live traffic incidents can still be shown in offline mode by enabling pass-through feature for traffic incidents on `sdk.core.engine.SDKNativeEngine`. See `sdk.core.engine.SDKNativeEngine.pass_through_features` for details.

  Supports only one mode: <a href="sdk-for-ios-explore-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV19trafficIncidentsAllSSvpZ">`MapFeatureModes.trafficIncidentsAll`</a>.

  Not supported for <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO9satelliteyA2CmF">`MapScheme.satellite`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO14roadNetworkDayyA2CmF">`MapScheme.roadNetworkDay`</a> and <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO16roadNetworkNightyA2CmF">`MapScheme.roadNetworkNight`</a>. By default, this map feature is not enabled.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let trafficIncidents: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11MapFeaturesV13trafficLightsSSvpZ"></span>` `<span id="//apple_ref/swift/Variable/trafficLights" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-mapfeatures#/s:7heresdk11MapFeaturesV13trafficLightsSSvpZ" class="token"><code>trafficLights</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Traffic lights.

  Supports only one mode: <a href="sdk-for-ios-explore-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV16trafficLightsAllSSvpZ">`MapFeatureModes.trafficLightsAll`</a>

  Not supported for <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO9satelliteyA2CmF">`MapScheme.satellite`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO14roadNetworkDayyA2CmF">`MapScheme.roadNetworkDay`</a> and <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO16roadNetworkNightyA2CmF">`MapScheme.roadNetworkNight`</a>.

  By default, traffic lights are enabled on all compatible map schemes.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let trafficLights: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11MapFeaturesV19vehicleRestrictionsSSvpZ"></span>` `<span id="//apple_ref/swift/Variable/vehicleRestrictions" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-mapfeatures#/s:7heresdk11MapFeaturesV19vehicleRestrictionsSSvpZ" class="token"><code>vehicleRestrictions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Vehicle restrictions. Requires map version 25 as minimum. If old map data is stored on disk, it might require updating using <a href="sdk-for-ios-explore-classes-mapupdater">`MapUpdater`</a>.

  Supported modes: <a href="sdk-for-ios-explore-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV25vehicleRestrictionsActiveSSvpZ">`MapFeatureModes.vehicleRestrictionsActive`</a>, <a href="sdk-for-ios-explore-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV36vehicleRestrictionsActiveAndInactiveSSvpZ">`MapFeatureModes.vehicleRestrictionsActiveAndInactive`</a> and <a href="sdk-for-ios-explore-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV50vehicleRestrictionsActiveAndInactiveDifferentiatedSSvpZ">`MapFeatureModes.vehicleRestrictionsActiveAndInactiveDifferentiated`</a>.

  Default mode when enabled is <a href="sdk-for-ios-explore-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV36vehicleRestrictionsActiveAndInactiveSSvpZ">`MapFeatureModes.vehicleRestrictionsActiveAndInactive`</a>.

  Not supported for <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO9satelliteyA2CmF">`MapScheme.satellite`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO14roadNetworkDayyA2CmF">`MapScheme.roadNetworkDay`</a> and <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO16roadNetworkNightyA2CmF">`MapScheme.roadNetworkNight`</a>. By default, this map feature is not enabled.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let vehicleRestrictions: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11MapFeaturesV13safetyCamerasSSvpZ"></span>` `<span id="//apple_ref/swift/Variable/safetyCameras" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-mapfeatures#/s:7heresdk11MapFeaturesV13safetyCamerasSSvpZ" class="token"><code>safetyCameras</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Safety and speed cameras.

  Supports only one mode: <a href="sdk-for-ios-explore-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV16safetyCamerasAllSSvpZ">`MapFeatureModes.safetyCamerasAll`</a>.

  Not supported for <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO9satelliteyA2CmF">`MapScheme.satellite`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO14roadNetworkDayyA2CmF">`MapScheme.roadNetworkDay`</a> and <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO16roadNetworkNightyA2CmF">`MapScheme.roadNetworkNight`</a>. By default, this map feature is not enabled.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let safetyCameras: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11MapFeaturesV9landmarksSSvpZ"></span>` `<span id="//apple_ref/swift/Variable/landmarks" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-mapfeatures#/s:7heresdk11MapFeaturesV9landmarksSSvpZ" class="token"><code>landmarks</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Displays 3D landmarks on the map.

  Please note: Enabling 3D landmarks with 3D terrain may result in instances where landmarks sink into or float above the terrain.

  Supported modes: <a href="sdk-for-ios-explore-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV17landmarksTexturedSSvpZ">`MapFeatureModes.landmarksTextured`</a>, <a href="sdk-for-ios-explore-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV18landmarksGrayscaleSSvpZ">`MapFeatureModes.landmarksGrayscale`</a> and <a href="sdk-for-ios-explore-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV20landmarksTexturelessSSvpZ">`MapFeatureModes.landmarksTextureless`</a>.

  Default mode is <a href="sdk-for-ios-explore-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV18landmarksGrayscaleSSvpZ">`MapFeatureModes.landmarksGrayscale`</a>.

  By default, 3D landmarks are enabled on all compatible map schemes.

  Not supported for <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO9satelliteyA2CmF">`MapScheme.satellite`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO14roadNetworkDayyA2CmF">`MapScheme.roadNetworkDay`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO16roadNetworkNightyA2CmF">`MapScheme.roadNetworkNight`</a> and all hybrid schemes: <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO9hybridDayyA2CmF">`MapScheme.hybridDay`</a> <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO11hybridNightyA2CmF">`MapScheme.hybridNight`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO13liteHybridDayyA2CmF">`MapScheme.liteHybridDay`</a> <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO15liteHybridNightyA2CmF">`MapScheme.liteHybridNight`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO18logisticsHybridDayyA2CmF">`MapScheme.logisticsHybridDay`</a> and <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO20logisticsHybridNightyA2CmF">`MapScheme.logisticsHybridNight`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let landmarks: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11MapFeaturesV18environmentalZonesSSvpZ"></span>` `<span id="//apple_ref/swift/Variable/environmentalZones" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-mapfeatures#/s:7heresdk11MapFeaturesV18environmentalZonesSSvpZ" class="token"><code>environmentalZones</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  City areas designated as environmental zones, which empose limitations on the type of vehicles that are allowed to enter such areas.

  Supports only one mode: <a href="sdk-for-ios-explore-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV21environmentalZonesAllSSvpZ">`MapFeatureModes.environmentalZonesAll`</a>.

  Not supported for <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO9satelliteyA2CmF">`MapScheme.satellite`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO14roadNetworkDayyA2CmF">`MapScheme.roadNetworkDay`</a> and <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO16roadNetworkNightyA2CmF">`MapScheme.roadNetworkNight`</a>. By default, this map feature is not enabled.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let environmentalZones: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11MapFeaturesV15congestionZonesSSvpZ"></span>` `<span id="//apple_ref/swift/Variable/congestionZones" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-mapfeatures#/s:7heresdk11MapFeaturesV15congestionZonesSSvpZ" class="token"><code>congestionZones</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  City areas designated as congestion zones (or congestion charge zones), which impose fees on entering such areas.

  Supports only one mode: <a href="sdk-for-ios-explore-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV18congestionZonesAllSSvpZ">`MapFeatureModes.congestionZonesAll`</a>.

  Not supported for <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO9satelliteyA2CmF">`MapScheme.satellite`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO14roadNetworkDayyA2CmF">`MapScheme.roadNetworkDay`</a> and <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO16roadNetworkNightyA2CmF">`MapScheme.roadNetworkNight`</a>. By default, this map feature is not enabled.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let congestionZones: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11MapFeaturesV13lowSpeedZonesSSvpZ"></span>` `<span id="//apple_ref/swift/Variable/lowSpeedZones" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-mapfeatures#/s:7heresdk11MapFeaturesV13lowSpeedZonesSSvpZ" class="token"><code>lowSpeedZones</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  City areas designated as low speed zones. Only available when Japan map is used.

  Supports only one mode: <a href="sdk-for-ios-explore-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV16lowSpeedZonesAllSSvpZ">`MapFeatureModes.lowSpeedZonesAll`</a>.

  Not supported for <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO9satelliteyA2CmF">`MapScheme.satellite`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO14roadNetworkDayyA2CmF">`MapScheme.roadNetworkDay`</a> and <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO16roadNetworkNightyA2CmF">`MapScheme.roadNetworkNight`</a>. By default, this map feature is not enabled.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let lowSpeedZones: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11MapFeaturesV7terrainSSvpZ"></span>` `<span id="//apple_ref/swift/Variable/terrain" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-mapfeatures#/s:7heresdk11MapFeaturesV7terrainSSvpZ" class="token"><code>terrain</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Show elevation topography.

  Supported modes: <a href="sdk-for-ios-explore-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV16terrainHillshadeSSvpZ">`MapFeatureModes.terrainHillshade`</a>, <a href="sdk-for-ios-explore-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV9terrain3dSSvpZ">`MapFeatureModes.terrain3d`</a>.

  <a href="sdk-for-ios-explore-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV16terrainHillshadeSSvpZ">`MapFeatureModes.terrainHillshade`</a> is only supported for schemes <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO9normalDayyA2CmF">`MapScheme.normalDay`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO11normalNightyA2CmF">`MapScheme.normalNight`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO7liteDayyA2CmF">`MapScheme.liteDay`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO9liteNightyA2CmF">`MapScheme.liteNight`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO12logisticsDayyA2CmF">`MapScheme.logisticsDay`</a> and <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO14logisticsNightyA2CmF">`MapScheme.logisticsNight`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO7topoDayyA2CmF">`MapScheme.topoDay`</a> and <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO9topoNightyA2CmF">`MapScheme.topoNight`</a>.

  Default mode is <a href="sdk-for-ios-explore-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV16terrainHillshadeSSvpZ">`MapFeatureModes.terrainHillshade`</a> for the supporting schemes.

  By default, terrain is disabled, except for <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO7topoDayyA2CmF">`MapScheme.topoDay`</a> and <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO9topoNightyA2CmF">`MapScheme.topoNight`</a>.

  Note that this feature has performance implications, with extra data use and impact on frame rate. If performance is a concern, this feature can be disabled from the application side when loading the map scene.

  Not supported for <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO9satelliteyA2CmF">`MapScheme.satellite`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO14roadNetworkDayyA2CmF">`MapScheme.roadNetworkDay`</a> and <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO16roadNetworkNightyA2CmF">`MapScheme.roadNetworkNight`</a>.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let terrain: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11MapFeaturesV13publicTransitSSvpZ"></span>` `<span id="//apple_ref/swift/Variable/publicTransit" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-mapfeatures#/s:7heresdk11MapFeaturesV13publicTransitSSvpZ" class="token"><code>publicTransit</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Toggles the display of public transit lines for systems like subway, tram, train, monorail, and ferry, based on the selected mode.

  Supported modes: <a href="sdk-for-ios-explore-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV16publicTransitAllSSvpZ">`MapFeatureModes.publicTransitAll`</a>, <a href="sdk-for-ios-explore-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV17publicTransitAsiaSSvpZ">`MapFeatureModes.publicTransitAsia`</a>.

  <a href="sdk-for-ios-explore-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV17publicTransitAsiaSSvpZ">`MapFeatureModes.publicTransitAsia`</a> is supported only when credentials enabled for the enriched Japan map are used.

  Public transit is disabled by default for all map schemes when using Rest-of-World map data. When using enriched Japan map data, public transit is enabled by default with <a href="sdk-for-ios-explore-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV17publicTransitAsiaSSvpZ">`MapFeatureModes.publicTransitAsia`</a> on normal, lite and topo schemes (including their hybrid variants) and disabled by default on logistics schemes.

  Not supported for <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO9satelliteyA2CmF">`MapScheme.satellite`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO14roadNetworkDayyA2CmF">`MapScheme.roadNetworkDay`</a> and <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO16roadNetworkNightyA2CmF">`MapScheme.roadNetworkNight`</a>.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let publicTransit: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11MapFeaturesV14roadExitLabelsSSvpZ"></span>` `<span id="//apple_ref/swift/Variable/roadExitLabels" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-mapfeatures#/s:7heresdk11MapFeaturesV14roadExitLabelsSSvpZ" class="token"><code>roadExitLabels</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Show or hide road exit labels, if available.

  Supported modes: <a href="sdk-for-ios-explore-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV25roadExitLabelsNumbersOnlySSvpZ">`MapFeatureModes.roadExitLabelsNumbersOnly`</a>, <a href="sdk-for-ios-explore-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV17roadExitLabelsAllSSvpZ">`MapFeatureModes.roadExitLabelsAll`</a>

  Default mode is <a href="sdk-for-ios-explore-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV25roadExitLabelsNumbersOnlySSvpZ">`MapFeatureModes.roadExitLabelsNumbersOnly`</a>.

  Road exit labels are enabled by default with <a href="sdk-for-ios-explore-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV25roadExitLabelsNumbersOnlySSvpZ">`MapFeatureModes.roadExitLabelsNumbersOnly`</a> on normal, lite and topo schemes and with <a href="sdk-for-ios-explore-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV17roadExitLabelsAllSSvpZ">`MapFeatureModes.roadExitLabelsAll`</a> on logistics schemes. Note that topo schemes are only available in the HERE SDK Navigate variant.

  Not supported for <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO9satelliteyA2CmF">`MapScheme.satellite`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO14roadNetworkDayyA2CmF">`MapScheme.roadNetworkDay`</a> and <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO16roadNetworkNightyA2CmF">`MapScheme.roadNetworkNight`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let roadExitLabels: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11MapFeaturesV7shadowsSSvpZ"></span>` `<span id="//apple_ref/swift/Variable/shadows" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-mapfeatures#/s:7heresdk11MapFeaturesV7shadowsSSvpZ" class="token"><code>shadows</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Shadows for all building types (extruded buildings and landmarks).

  Supports only one mode: <a href="sdk-for-ios-explore-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV10shadowsAllSSvpZ">`MapFeatureModes.shadowsAll`</a>.

  A <a href="sdk-for-ios-explore-enums-shadowquality">`ShadowQuality`</a> must be set on the MapContext through a MapView or the feature has no effect.

  Shadows have a performance impact and should be considered only for devices with sufficient performance.

  Not supported for <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO9satelliteyA2CmF">`MapScheme.satellite`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO14roadNetworkDayyA2CmF">`MapScheme.roadNetworkDay`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO16roadNetworkNightyA2CmF">`MapScheme.roadNetworkNight`</a> and all hybrid schemes: <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO9hybridDayyA2CmF">`MapScheme.hybridDay`</a> <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO11hybridNightyA2CmF">`MapScheme.hybridNight`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO13liteHybridDayyA2CmF">`MapScheme.liteHybridDay`</a> <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO15liteHybridNightyA2CmF">`MapScheme.liteHybridNight`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO18logisticsHybridDayyA2CmF">`MapScheme.logisticsHybridDay`</a> and <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO20logisticsHybridNightyA2CmF">`MapScheme.logisticsHybridNight`</a>.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process. By default, this map feature is not enabled.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let shadows: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11MapFeaturesV16ambientOcclusionSSvpZ"></span>` `<span id="//apple_ref/swift/Variable/ambientOcclusion" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-mapfeatures#/s:7heresdk11MapFeaturesV16ambientOcclusionSSvpZ" class="token"><code>ambientOcclusion</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Ambient occlusion effect for 3D geometries (extruded buildings and landmarks).

  Supports only one mode: <a href="sdk-for-ios-explore-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV19ambientOcclusionAllSSvpZ">`MapFeatureModes.ambientOcclusionAll`</a>.

  This visual effect has a performance impact and should be considered only for devices with sufficient performance.

  Not supported for <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO9satelliteyA2CmF">`MapScheme.satellite`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO14roadNetworkDayyA2CmF">`MapScheme.roadNetworkDay`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO16roadNetworkNightyA2CmF">`MapScheme.roadNetworkNight`</a> and all hybrid schemes: <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO9hybridDayyA2CmF">`MapScheme.hybridDay`</a> <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO11hybridNightyA2CmF">`MapScheme.hybridNight`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO13liteHybridDayyA2CmF">`MapScheme.liteHybridDay`</a> <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO15liteHybridNightyA2CmF">`MapScheme.liteHybridNight`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO18logisticsHybridDayyA2CmF">`MapScheme.logisticsHybridDay`</a> and <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO20logisticsHybridNightyA2CmF">`MapScheme.logisticsHybridNight`</a>.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process. By default, this map feature is not enabled.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let ambientOcclusion: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11MapFeaturesV8contoursSSvpZ"></span>` `<span id="//apple_ref/swift/Variable/contours" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-mapfeatures#/s:7heresdk11MapFeaturesV8contoursSSvpZ" class="token"><code>contours</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Show or hide contour lines on the map to represent elevation changes.

  Supports only one mode: <a href="sdk-for-ios-explore-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV11contoursAllSSvpZ">`MapFeatureModes.contoursAll`</a>

  Not supported for <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO9satelliteyA2CmF">`MapScheme.satellite`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO14roadNetworkDayyA2CmF">`MapScheme.roadNetworkDay`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO16roadNetworkNightyA2CmF">`MapScheme.roadNetworkNight`</a> and all hybrid schemes: <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO9hybridDayyA2CmF">`MapScheme.hybridDay`</a> <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO11hybridNightyA2CmF">`MapScheme.hybridNight`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO13liteHybridDayyA2CmF">`MapScheme.liteHybridDay`</a> <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO15liteHybridNightyA2CmF">`MapScheme.liteHybridNight`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO18logisticsHybridDayyA2CmF">`MapScheme.logisticsHybridDay`</a> and <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO20logisticsHybridNightyA2CmF">`MapScheme.logisticsHybridNight`</a>.

  Contours are enabled by default on topo schemes and disabled by default on other schemes.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let contours: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11MapFeaturesV19truckPreferredRoadsSSvpZ"></span>` `<span id="//apple_ref/swift/Variable/truckPreferredRoads" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-mapfeatures#/s:7heresdk11MapFeaturesV19truckPreferredRoadsSSvpZ" class="token"><code>truckPreferredRoads</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Show or hide truck preferred road

  Supported modes: <a href="sdk-for-ios-explore-structs-mapfeaturemodes#/s:7heresdk15MapFeatureModesV22truckPreferredRoadsAllSSvpZ">`MapFeatureModes.truckPreferredRoadsAll`</a>

  Not supported for <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO9satelliteyA2CmF">`MapScheme.satellite`</a>, <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO14roadNetworkDayyA2CmF">`MapScheme.roadNetworkDay`</a> and <a href="sdk-for-ios-explore-enums-mapscheme#/s:7heresdk9MapSchemeO16roadNetworkNightyA2CmF">`MapScheme.roadNetworkNight`</a>. By default, this map feature is not enabled.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let truckPreferredRoads: String
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

