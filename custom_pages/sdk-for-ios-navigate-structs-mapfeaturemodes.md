---
title: "MapFeatureModes Structure Reference"
slug: "sdk-for-ios-navigate-structs-mapfeaturemodes"
---

# MapFeatureModes

<div class="declaration">

<div class="language">

``` highlight
public struct MapFeatureModes
```

</div>

</div>

Holds constants for map feature modes, to be used with <a href="sdk-for-ios-navigate-classes-mapscene#sdk-for-ios-navigate-s-7heresdk8MapSceneC14enableFeaturesyySDyS2SGF">`MapScene.enableFeatures(...)`</a>.

Use <a href="sdk-for-ios-navigate-structs-mapfeaturemodes#sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV11defaultModeSSvpZ">`MapFeatureModes.defaultMode`</a> to enable a feature with its default mode.

Note: The default mode is defined by the currently loaded map scene configuration and may vary per <a href="sdk-for-ios-navigate-enums-mapscheme">`MapScheme`</a>. The currently active features and modes can be inspected using <a href="sdk-for-ios-navigate-classes-mapscene#sdk-for-ios-navigate-s-7heresdk8MapSceneC17getActiveFeaturesSDyS2SGyF">`MapScene.getActiveFeatures(...)`</a> after the scene is loaded.

See <a href="sdk-for-ios-navigate-structs-mapfeatures">`MapFeatures`</a> for constants representing the feature names.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV11defaultModeSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-defaultMode" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-mapfeaturemodes#sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV11defaultModeSSvpZ" class="token"><code>defaultMode</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Enables the default mode of a map feature. Can be used with any map feature.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let defaultMode: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV21buildingFootprintsAllSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-buildingFootprintsAll" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-mapfeaturemodes#sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV21buildingFootprintsAllSSvpZ" class="token"><code>buildingFootprintsAll</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  All building footprints are shown.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let buildingFootprintsAll: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV18congestionZonesAllSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-congestionZonesAll" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-mapfeaturemodes#sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV18congestionZonesAllSSvpZ" class="token"><code>congestionZonesAll</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  All congestion zones are shown.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let congestionZonesAll: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV20extrudedBuildingsAllSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-extrudedBuildingsAll" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-mapfeaturemodes#sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV20extrudedBuildingsAllSSvpZ" class="token"><code>extrudedBuildingsAll</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  All extruded buildings are shown.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let extrudedBuildingsAll: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV21environmentalZonesAllSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-environmentalZonesAll" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-mapfeaturemodes#sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV21environmentalZonesAllSSvpZ" class="token"><code>environmentalZonesAll</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  All environmental zones are shown.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let environmentalZonesAll: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV16lowSpeedZonesAllSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-lowSpeedZonesAll" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-mapfeaturemodes#sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV16lowSpeedZonesAllSSvpZ" class="token"><code>lowSpeedZonesAll</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  All low speed zones are shown.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let lowSpeedZonesAll: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV027trafficFlowJapanWithoutFreeF0SSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-trafficFlowJapanWithoutFreeFlow" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-mapfeaturemodes#sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV027trafficFlowJapanWithoutFreeF0SSvpZ" class="token"><code>trafficFlowJapanWithoutFreeFlow</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Only available when Japan map is used.

  Traffic flow shows green lines depending on the region.

  In Japan green lines will not be shown, as if the <a href="sdk-for-ios-navigate-structs-mapfeaturemodes#sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV022trafficFlowWithoutFreeF0SSvpZ">`MapFeatureModes.trafficFlowWithoutFreeFlow`</a> were used.

  In rest of the world, green lines will be shown, as if the <a href="sdk-for-ios-navigate-structs-mapfeaturemodes#sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV019trafficFlowWithFreeF0SSvpZ">`MapFeatureModes.trafficFlowWithFreeFlow`</a> were used.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let trafficFlowJapanWithoutFreeFlow: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV019trafficFlowWithFreeF0SSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-trafficFlowWithFreeFlow" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-mapfeaturemodes#sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV019trafficFlowWithFreeF0SSvpZ" class="token"><code>trafficFlowWithFreeFlow</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Traffic flow shows green lines when there is no traffic congestion.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let trafficFlowWithFreeFlow: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV022trafficFlowWithoutFreeF0SSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-trafficFlowWithoutFreeFlow" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-mapfeaturemodes#sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV022trafficFlowWithoutFreeF0SSvpZ" class="token"><code>trafficFlowWithoutFreeFlow</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Traffic flow does not show green lines when there is no traffic congestion.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let trafficFlowWithoutFreeFlow: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV19trafficIncidentsAllSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-trafficIncidentsAll" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-mapfeaturemodes#sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV19trafficIncidentsAllSSvpZ" class="token"><code>trafficIncidentsAll</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  All available traffic incidents are shown.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let trafficIncidentsAll: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV16trafficLightsAllSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-trafficLightsAll" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-mapfeaturemodes#sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV16trafficLightsAllSSvpZ" class="token"><code>trafficLightsAll</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  All available traffic lights are shown.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let trafficLightsAll: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV17landmarksTexturedSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-landmarksTextured" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-mapfeaturemodes#sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV17landmarksTexturedSSvpZ" class="token"><code>landmarksTextured</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  3D landmarks are textured.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let landmarksTextured: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV18landmarksGrayscaleSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-landmarksGrayscale" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-mapfeaturemodes#sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV18landmarksGrayscaleSSvpZ" class="token"><code>landmarksGrayscale</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  3D landmarks are textured with grayscale filter.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let landmarksGrayscale: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV20landmarksTexturelessSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-landmarksTextureless" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-mapfeaturemodes#sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV20landmarksTexturelessSSvpZ" class="token"><code>landmarksTextureless</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  3D landmarks have solid color.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let landmarksTextureless: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV36vehicleRestrictionsActiveAndInactiveSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-vehicleRestrictionsActiveAndInactive" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-mapfeaturemodes#sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV36vehicleRestrictionsActiveAndInactiveSSvpZ" class="token"><code>vehicleRestrictionsActiveAndInactive</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Both active and inactive time-based restrictions are shown.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let vehicleRestrictionsActiveAndInactive: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV50vehicleRestrictionsActiveAndInactiveDifferentiatedSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-vehicleRestrictionsActiveAndInactiveDifferentiated" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-mapfeaturemodes#sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV50vehicleRestrictionsActiveAndInactiveDifferentiatedSSvpZ" class="token"><code>vehicleRestrictionsActiveAndInactiveDifferentiated</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Both active and inactive restrictions are shown, but inactive time-based restrictions are shown as faded.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let vehicleRestrictionsActiveAndInactiveDifferentiated: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV25vehicleRestrictionsActiveSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-vehicleRestrictionsActive" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-mapfeaturemodes#sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV25vehicleRestrictionsActiveSSvpZ" class="token"><code>vehicleRestrictionsActive</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Inactive time-based restrictions are not shown.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let vehicleRestrictionsActive: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV16safetyCamerasAllSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-safetyCamerasAll" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-mapfeaturemodes#sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV16safetyCamerasAllSSvpZ" class="token"><code>safetyCamerasAll</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  All types of safety cameras are shown. Includes speed, red light, red light + speed, bus lane, distance and speed section cameras.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let safetyCamerasAll: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV16terrainHillshadeSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-terrainHillshade" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-mapfeaturemodes#sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV16terrainHillshadeSSvpZ" class="token"><code>terrainHillshade</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Topography-shading is shown.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let terrainHillshade: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV9terrain3dSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-terrain3d" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-mapfeaturemodes#sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV9terrain3dSSvpZ" class="token"><code>terrain3d</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Topography-shading is shown on 3d terrain.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let terrain3d: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV16publicTransitAllSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-publicTransitAll" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-mapfeaturemodes#sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV16publicTransitAllSSvpZ" class="token"><code>publicTransitAll</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Line geometry for all available public transit systems is shown; including subway, tram, train, monorail, ferry and more.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let publicTransitAll: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV17publicTransitAsiaSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-publicTransitAsia" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-mapfeaturemodes#sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV17publicTransitAsiaSSvpZ" class="token"><code>publicTransitAsia</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Line geometry for selected public transit systems is shown: subway lines in Japan. Only available when Japan map is used.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let publicTransitAsia: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV25roadExitLabelsNumbersOnlySSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-roadExitLabelsNumbersOnly" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-mapfeaturemodes#sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV25roadExitLabelsNumbersOnlySSvpZ" class="token"><code>roadExitLabelsNumbersOnly</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Road exit labels are shown with numbers, if available.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let roadExitLabelsNumbersOnly: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV17roadExitLabelsAllSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-roadExitLabelsAll" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-mapfeaturemodes#sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV17roadExitLabelsAllSSvpZ" class="token"><code>roadExitLabelsAll</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Road exit labels are shown with numbers and names, if available.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let roadExitLabelsAll: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV10shadowsAllSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-shadowsAll" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-mapfeaturemodes#sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV10shadowsAllSSvpZ" class="token"><code>shadowsAll</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Shadows are shown for extruded buildings and landmarks.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let shadowsAll: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV19ambientOcclusionAllSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-ambientOcclusionAll" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-mapfeaturemodes#sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV19ambientOcclusionAllSSvpZ" class="token"><code>ambientOcclusionAll</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Ambient occlusion effect is shown for extruded buildings and landmarks.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let ambientOcclusionAll: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV11contoursAllSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-contoursAll" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-mapfeaturemodes#sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV11contoursAllSSvpZ" class="token"><code>contoursAll</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Contour lines indicating representing elevation changes are shown.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let contoursAll: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV22truckPreferredRoadsAllSSvpZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Variable-truckPreferredRoadsAll" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-mapfeaturemodes#sdk-for-ios-navigate-s-7heresdk15MapFeatureModesV22truckPreferredRoadsAllSSvpZ" class="token"><code>truckPreferredRoadsAll</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Display truck preferred roads

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static let truckPreferredRoadsAll: String
  ```

  </div>

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-navigate-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

