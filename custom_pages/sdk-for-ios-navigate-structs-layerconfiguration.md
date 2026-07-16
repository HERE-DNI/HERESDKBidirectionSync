---
title: "LayerConfiguration Structure Reference"
slug: "sdk-for-ios-navigate-structs-layerconfiguration"
---

# LayerConfiguration

<div class="declaration">

<div class="language">

``` highlight
public struct LayerConfiguration : Hashable
```

</div>

</div>

A class to configure which layers should be enabled or disabled in the OCM map data. Disabling a layer allows to reduce the amount of data that will be downloaded or prefetched from the internet, for example, when panning the map view online or when downloading maps for offline use.

`LayerConfiguration` changes made via <a href="sdk-for-ios-navigate-structs-sdkoptions">`SDKOptions`</a> require `sdk.maploader.MapUpdater` to align previously downloaded content. To ensure that the changes in <a href="sdk-for-ios-navigate-structs-sdkoptions">`SDKOptions`</a> affect the map data, it is recommended to trigger a map update. Without calling

    mapUpdater.updateCatalog(...)

, the adjustments will apply only to future map downloads and will not impact the currently installed map data, either in the cache or in the persisted storage. Note that calling

    updateCatalog(...)

will update the version, only when a map update is available in the catalog.
</p>

**Notes**

- The `LayerConfiguration` is only available for the Navigate licenses that contains the offline maps feature. It has no effect on other license.

- The `LayerConfiguration` cannot be set separately for a region, it will be applied globally for all regions that will be downloaded in the future.

- It is not possible to specify a separate `LayerConfiguration` for the map cache and offline maps. The `LayerConfiguration` will be always applied to both.

- If a `LayerConfiguration` is applied, then only the listed features will be enabled, all others will be disabled. For example, if you want to disable only one feature, then all other features need to be present, or they will be also disabled.

The `LayerConfiguration` controls which content will be subject of

- map download for features in

      enabledFeatures()

  ,

- explicit prefetching using `sdk.prefetcher.RoutePrefetcher, sdk.prefetcher.PolygonPrefetcher` and implicit prefetching, such as when displaying a map view, for features in

      implicitlyPrefetchedFeatures()

  .

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18LayerConfigurationV15enabledFeaturesSayAC7FeatureOGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-enabledFeatures" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-layerconfiguration#sdk-for-ios-navigate-s-7heresdk18LayerConfigurationV15enabledFeaturesSayAC7FeatureOGvp" class="token"><code>enabledFeatures</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies feature configuration for enabling list of features enabled for map download. Empty list disables map download, as no map content specified for download in this case.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var enabledFeatures: [LayerConfiguration.Feature]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-layerconfiguration-feature">Feature</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18LayerConfigurationV28implicitlyPrefetchedFeaturesSayAC7FeatureOGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-implicitlyPrefetchedFeatures" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-layerconfiguration#sdk-for-ios-navigate-s-7heresdk18LayerConfigurationV28implicitlyPrefetchedFeaturesSayAC7FeatureOGvp" class="token"><code>implicitlyPrefetchedFeatures</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies the list of features enabled for implicit and explicit map prefetch. Implicit map prefetch will download map content for implicit prefetch features when showing a map in the MapView.

  Allows to specify an empty list, effectively disabling implicit prefetching. In this case, the system will prioritize minimal network usage, at the cost of reduced offline map availability. When disabling certain implicitly prefetched features, less data will be prefetched when the map is rendered. Map data that was already cached will not be removed until the least recently used strategy (LRU) applies. That means you cannot remove any content from the map cache by updating the `LayerConfiguration`. However, for new map data, it will be applied.

  By default the list contains:

  - <a href="sdk-for-ios-navigate-structs-layerconfiguration-feature#sdk-for-ios-navigate-s-7heresdk18LayerConfigurationV7FeatureO10navigationyA2EmF">`LayerConfiguration.Feature.navigation`</a>

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var implicitlyPrefetchedFeatures: [LayerConfiguration.Feature]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-layerconfiguration-feature">Feature</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18LayerConfigurationV15enabledFeaturesACSayAC7FeatureOG_tcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-enabledFeatures" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-layerconfiguration#sdk-for-ios-navigate-s-7heresdk18LayerConfigurationV15enabledFeaturesACSayAC7FeatureOG_tcfc" class="token"><code>init(enabledFeatures:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Initializes both, `enabled_features` and `implicitly_prefetched_features` with value passed to constructor.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(enabledFeatures: [LayerConfiguration.Feature])
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-layerconfiguration-feature">Feature</a>

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
  <td><code> </code><em><code>enabledFeatures</code></em><code> </code></td>
  <td><div>
  <p>List of map features to downloader through <a href="sdk-for-ios-navigate-classes-mapdownloader"><code>MapDownloader</code></a>, and implicitly prefetch when using <a href="sdk-for-ios-navigate-classes-mapview"><code>MapView</code></a></p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18LayerConfigurationV7FeatureO"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Enum-Feature" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-layerconfiguration#sdk-for-ios-navigate-s-7heresdk18LayerConfigurationV7FeatureO" class="token"><code>Feature</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines a list of possible map data features that can be enabled / disabled. See <a href="sdk-for-ios-navigate-structs-sdkoptions#sdk-for-ios-navigate-s-7heresdk10SDKOptionsV18layerConfigurationAA05LayerD0Vvp">`SDKOptions.layerConfiguration`</a>

  Following features are enabled by default:

  - <a href="sdk-for-ios-navigate-structs-layerconfiguration-feature#sdk-for-ios-navigate-s-7heresdk18LayerConfigurationV7FeatureO15detailRenderingyA2EmF">`LayerConfiguration.Feature.detailRendering`</a>
  - <a href="sdk-for-ios-navigate-structs-layerconfiguration-feature#sdk-for-ios-navigate-s-7heresdk18LayerConfigurationV7FeatureO11landmarks3dyA2EmF">`LayerConfiguration.Feature.landmarks3d`</a>
  - <a href="sdk-for-ios-navigate-structs-layerconfiguration-feature#sdk-for-ios-navigate-s-7heresdk18LayerConfigurationV7FeatureO10navigationyA2EmF">`LayerConfiguration.Feature.navigation`</a>
  - <a href="sdk-for-ios-navigate-structs-layerconfiguration-feature#sdk-for-ios-navigate-s-7heresdk18LayerConfigurationV7FeatureO13offlineSearchyA2EmF">`LayerConfiguration.Feature.offlineSearch`</a>
  - <a href="sdk-for-ios-navigate-structs-layerconfiguration-feature#sdk-for-ios-navigate-s-7heresdk18LayerConfigurationV7FeatureO14offlineRoutingyA2EmF">`LayerConfiguration.Feature.offlineRouting`</a>
  - <a href="sdk-for-ios-navigate-structs-layerconfiguration-feature#sdk-for-ios-navigate-s-7heresdk18LayerConfigurationV7FeatureO9renderingyA2EmF">`LayerConfiguration.Feature.rendering`</a>

  All other features are disabled, by default.

  Each feature enables a set of OCM layer groups to be downloaded by `sdk.maploader.MapDownloader`. Detailed description of each layer group available in the <a href="https://www.here.com/docs/bundle/optimized-client-map-developer-guide/page/README.html">HERE Optimized Client Map Developer Guide</a>

  Following features are enabled by default for implicit prefetch:

  - <a href="sdk-for-ios-navigate-structs-layerconfiguration-feature#sdk-for-ios-navigate-s-7heresdk18LayerConfigurationV7FeatureO10navigationyA2EmF">`LayerConfiguration.Feature.navigation`</a>

  Implicit prefetch downloads map content for implicit prefetch features within a view port currently showed by MapView. Explicit prefetching is done using `sdk.prefetcher.RoutePrefetcher` and `sdk.prefetcher.PolygonPrefetcher`.

  Feature might have more than one layer group predefined to enable full experience. For example, <a href="sdk-for-ios-navigate-structs-layerconfiguration-feature#sdk-for-ios-navigate-s-7heresdk18LayerConfigurationV7FeatureO10navigationyA2EmF">`LayerConfiguration.Feature.navigation`</a> requires routing attributes, visual-friendly street names, maneuvers data and ability to interconnect those data sets.

  The same map data is useful for different features, for example <a href="sdk-for-ios-navigate-structs-layerconfiguration-feature#sdk-for-ios-navigate-s-7heresdk18LayerConfigurationV7FeatureO9renderingyA2EmF">`LayerConfiguration.Feature.rendering`</a> uses Places data to present it on the MapView, while <a href="sdk-for-ios-navigate-structs-layerconfiguration-feature#sdk-for-ios-navigate-s-7heresdk18LayerConfigurationV7FeatureO13offlineSearchyA2EmF">`LayerConfiguration.Feature.offlineSearch`</a> uses the same data to enable discoverability by name or category. Hence, features might have overlapping sets of enabled layer groups.

  <a href="sdk-for-ios-navigate-structs-layerconfiguration-feature" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum Feature : UInt32, CaseIterable, Codable
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

