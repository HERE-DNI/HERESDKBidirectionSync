---
title: "MapMatcher Class Reference"
slug: "sdk-for-ios-explore-classes-mapmatcher"
---

# MapMatcher

<div class="declaration">

<div class="language">

``` highlight
public class MapMatcher
```

``` highlight
extension MapMatcher: NativeBase
```

``` highlight
extension MapMatcher: Hashable
```

</div>

</div>

This class provides map-matching functionality. It determines whether a location can be matched to a nearby road network and provides additional OCM map data for that location.

**Note:** This is a **beta** release of this feature. There may be bugs and unexpected behaviors. Related APIs may change in future releases without a deprecation process.

A `MapMatcher` maintains an internal state across location updates. This helps to check if the match is consistent with previous matches or if an unrealistic jump occurred due to low accuracy of the provided location.

A `MapMatcher` requires OCM tile data, either through caching, prefetching, or installed <a href="sdk-for-ios-explore-structs-region">`Region`</a> data. If the necessary tiles are not found, an online request is initiated. Note that in such cases, the download is triggered silently in the background, and `nil` is returned immediately.

The `MapMatcher` supports two layer configurations for retrieving segment geometry data:

- **Rendering layer (`LayerConfiguration.Feature.RENDERING`)**: Enabled by default. If your application uses map rendering or <a href="sdk-for-ios-explore-classes-mapview">`MapView`</a> components, using this layer is recommended.

- **eHorizon layer (`LayerConfiguration.Feature.EHORIZON`)**: Not enabled by default. It encodes segment geometries outside the rendering layer groups to reduce the amount of downloaded data. Use the eHorizon layer when:

  - No <a href="sdk-for-ios-explore-classes-mapview">`MapView`</a> is used in your application.
  - Only the eHorizon layer is used in your application. In these cases, using the eHorizon layer will reduce the required data to download. If the rendering layer is enabled, it will increase the required data to download.

**Important**: If `useRenderingLayers` is set to `false` without properly enabling the eHorizon layer, it may produce incorrect results. Layer configuration is especially important when prefetching or installing region data. Missing data will be downloaded online automatically as needed.

If your hardware supports pitch and high precision altitude information and you want to use them in the `MapMatcher` to improve map-matching, then enable the `LayerConfiguration.Feature.ADAS` layer:

1.  Turn on the `ADAS` layer via <a href="sdk-for-ios-explore-structs-layerconfiguration#sdk-for-ios-explore-s-7heresdk18LayerConfigurationV15enabledFeaturesSayAC7FeatureOGvp">`LayerConfiguration.enabledFeatures`</a> (it will increase data consumption).
2.  If available, set `location.pitchInDegrees, location.coordinates.altitude` and `location.verticalAccuracyInMeters`.
3.  In case of issues, please contact your HERE representative.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10MapMatcherCACyKcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapmatcher#sdk-for-ios-explore-s-7heresdk10MapMatcherCACyKcfc" class="token"><code>init()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of this class.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-explore-core#sdk-for-ios-explore-s-7heresdk18InstantiationErrora">`InstantiationError`</a> Indicates what went wrong when the instantiation was attempted.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init() throws
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10MapMatcherC9sdkEngineAcA09SDKNativeE0C_tKcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-sdkEngine" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapmatcher#sdk-for-ios-explore-s-7heresdk10MapMatcherC9sdkEngineAcA09SDKNativeE0C_tKcfc" class="token"><code>init(sdkEngine:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of this class.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-explore-core#sdk-for-ios-explore-s-7heresdk18InstantiationErrora">`InstantiationError`</a> Indicates what went wrong when the instantiation was attempted.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(sdkEngine: SDKNativeEngine) throws
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-sdknativeengine">SDKNativeEngine</a>

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
  <td><code> </code><em><code>sdkEngine</code></em><code> </code></td>
  <td><div>
  <p>A SDKEngine instance.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10MapMatcherC9sdkEngine18useRenderingLayersAcA09SDKNativeE0C_SbtKcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-sdkEngine-useRenderingLayers" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapmatcher#sdk-for-ios-explore-s-7heresdk10MapMatcherC9sdkEngine18useRenderingLayersAcA09SDKNativeE0C_SbtKcfc" class="token"><code>init(sdkEngine:</code><wbr></wbr><code>useRenderingLayers:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of this class.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-explore-core#sdk-for-ios-explore-s-7heresdk18InstantiationErrora">`InstantiationError`</a> Indicates what went wrong when the instantiation was attempted.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(sdkEngine: SDKNativeEngine, useRenderingLayers: Bool) throws
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-sdknativeengine">SDKNativeEngine</a>

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
  <td><code> </code><em><code>sdkEngine</code></em><code> </code></td>
  <td><div>
  <p>A SDKEngine instance.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>useRenderingLayers</code></em><code> </code></td>
  <td><div>
  <p>When set to true, <code>LayerConfiguration.Feature.RENDERING</code> is used; otherwise, <code>LayerConfiguration.Feature.EHORIZON</code> is used to retrieve segment geometry data from the OCM map. Note: Ensure the corresponding layer is properly enabled in your <a href="sdk-for-ios-explore-structs-layerconfiguration"><code>LayerConfiguration</code></a> to avoid incorrect results.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10MapMatcherC5match8locationAA0B15MatchedLocationVSgAA0G0V_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-match-location" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapmatcher#sdk-for-ios-explore-s-7heresdk10MapMatcherC5match8locationAA0B15MatchedLocationVSgAA0G0V_tF" class="token"><code>match(location:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This method computes the map-matched location for the provided input location.

  Currently, matching is performed within a 50-meter radius of the provided location. If no road network is found within that radius, `nil` is returned.

  It’s required to set `time` field for each <a href="sdk-for-ios-explore-structs-location">`Location`</a> object for the `MapMatcher` to work properly. In case no time is provided, `nil` is returned and an error message is logged. It is used to calculate the distance in time between consecutive matches. Together with `speed`, this allows to calculate how likely a match is consistent with a previous match. To improve matching accuracy, it is recommended to provide `bearing` and `speed` parameters for each <a href="sdk-for-ios-explore-structs-location">`Location`</a> object.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func match(location: Location) -> MapMatchedLocation?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-location">Location</a>
  - <a href="sdk-for-ios-explore-structs-mapmatchedlocation">MapMatchedLocation</a>

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
  <td><code> </code><em><code>location</code></em><code> </code></td>
  <td><div>
  <p>The input location.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  map-matched location or `nil` if the location could not be matched to a road network.

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

