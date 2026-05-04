---
title: "LayerConfiguration (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestlayerconfiguration"
hidden: false
---

Package [com.here.sdk.core.engine](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class LayerConfiguration

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.core.engine.LayerConfiguration
------------------------------------------------------------------------
public final class LayerConfiguration extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
A class to configure which layers should be enabled or disabled in the OCM map data. Disabling a layer allows to reduce the amount of data that will be downloaded or prefetched from the internet, for example, when panning the map view online or when downloading maps for offline use.

`LayerConfiguration` changes made via [`SDKOptions`](sdk-for-android-explore-api-reference-latestsdkoptions "class in com.here.sdk.core.engine") require `sdk.maploader.MapUpdater` to align previously downloaded content. To ensure that the changes in [`SDKOptions`](sdk-for-android-explore-api-reference-latestsdkoptions "class in com.here.sdk.core.engine") affect the map data, it is recommended to trigger a map update. Without calling `mapUpdater.updateCatalog(...)`, the adjustments will apply only to future map downloads and will not impact the currently installed map data, either in the cache or in the persisted storage. Note that calling `updateCatalog(...)` will update the version, only when a map update is available in the catalog.

**Notes**

- The `LayerConfiguration` is only available for the Navigate licenses that contains the offline maps feature. It has no effect on other license.

Note that the `RENDERING` layer is a base layer that cannot be disabled: Therefore, it is not necessary to explicitly add the layer to a feature configuration - it will be always enabled.

- The `LayerConfiguration` cannot be set separately for a region, it will be applied globally for all regions that will be downloaded in the future.
- It is not possible to specify a separate `LayerConfiguration` for the map cache and offline maps. The `LayerConfiguration` will be always applied to both.
- If a `LayerConfiguration` is applied, then only the listed features will be enabled, all others will be disabled. For example, if you want to disable only one feature, then all other features need to be present, or they will be also disabled.

The `LayerConfiguration` controls which content will be subject of

- map download for features in `enabledFeatures()`,
- explicit prefetching using `sdk.prefetcher.RoutePrefetcher`, `sdk.prefetcher.PolygonPrefetcher` and implicit prefetching, such as when displaying a map view, for features in `implicitlyPrefetchedFeatures()`.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static enum `

  [LayerConfiguration.Feature](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature)

Defines a list of possible map data features that can be enabled / disabled.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`LayerConfiguration.Feature`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine")`>`

  [enabledFeatures](#enabledFeatures)

Specifies feature configuration for enabling list of features enabled for map download.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`LayerConfiguration.Feature`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine")`>`

  [implicitlyPrefetchedFeatures](#implicitlyPrefetchedFeatures)

Specifies the list of features enabled for implicit and explicit map prefetch.

## Constructor Summary

Constructors

Constructor

  Description

  [LayerConfiguration](#%3Cinit%3E())`()`

Initializes `enabled_features`, `implicitly_prefetched_features` and `on_demand_implicitly_prefetched_features` with it's default values.

[LayerConfiguration](#%3Cinit%3E(java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`LayerConfiguration.Feature`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine")`> enabledFeatures)`

Initializes both, `enabled_features` and `implicitly_prefetched_features` with value passed to constructor.

[LayerConfiguration](#%3Cinit%3E(java.util.List,java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`LayerConfiguration.Feature`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine")`> enabledFeatures, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`LayerConfiguration.Feature`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine")`> implicitlyPrefetchedFeatures)`

Creates a new instance.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `boolean`

  [equals](#equals(java.lang.Object))`(`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)` obj)`

  `int`

  [hashCode](#hashCode())`()`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### enabledFeatures

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[LayerConfiguration.Feature](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine")\> enabledFeatures

    Specifies feature configuration for enabling list of features enabled for map download. Empty list disables map download, as no map content specified for download in this case.

### implicitlyPrefetchedFeatures

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[LayerConfiguration.Feature](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine")\> implicitlyPrefetchedFeatures

    Specifies the list of features enabled for implicit and explicit map prefetch. Implicit map prefetch will download map content for implicit prefetch features when showing a map in the MapView.

    Allows to specify an empty list, effectively disabling implicit prefetching. In this case, the system will prioritize minimal network usage, at the cost of reduced offline map availability. When disabling certain implicitly prefetched features, less data will be prefetched when the map is rendered. Map data that was already cached will not be removed until the least recently used strategy (LRU) applies. That means you cannot remove any content from the map cache by updating the `LayerConfiguration`. However, for new map data, it will be applied.

    By default the list contains:

    - [`LayerConfiguration.Feature.DETAIL_RENDERING`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#DETAIL_RENDERING)
    - [`LayerConfiguration.Feature.NAVIGATION`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#NAVIGATION)
    - [`LayerConfiguration.Feature.OFFLINE_SEARCH`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#OFFLINE_SEARCH)
    - [`LayerConfiguration.Feature.OFFLINE_ROUTING`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#OFFLINE_ROUTING)
    - [`LayerConfiguration.Feature.RENDERING`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#RENDERING)
    - [`LayerConfiguration.Feature.TRUCK`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#TRUCK)

    Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

## Constructor Details

  - (java.util.List)" class="section detail">

### LayerConfiguration

public LayerConfiguration(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[LayerConfiguration.Feature](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine")\> enabledFeatures)

    Initializes both, `enabled_features` and `implicitly_prefetched_features` with value passed to constructor.
Parameters:
    `enabledFeatures` -

    List of map features to downloader through `MapDownloader`, and implicitly prefetch when using `MapView`
- ()" class="section detail">

### LayerConfiguration

public LayerConfiguration()

    Initializes `enabled_features`, `implicitly_prefetched_features` and `on_demand_implicitly_prefetched_features` with it's default values.

  - (java.util.List,java.util.List)" class="section detail">

### LayerConfiguration

public LayerConfiguration(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[LayerConfiguration.Feature](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine")\> enabledFeatures, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[LayerConfiguration.Feature](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature "enum class in com.here.sdk.core.engine")\> implicitlyPrefetchedFeatures)

    Creates a new instance.
Parameters:
    `enabledFeatures` -

    Specifies feature configuration for enabling list of features enabled for map download. Empty list disables map download, as no map content specified for download in this case.

    `implicitlyPrefetchedFeatures` -

    Specifies the list of features enabled for implicit and explicit map prefetch. Implicit map prefetch will download map content for implicit prefetch features when showing a map in the MapView.

    Allows to specify an empty list, effectively disabling implicit prefetching. In this case, the system will prioritize minimal network usage, at the cost of reduced offline map availability. When disabling certain implicitly prefetched features, less data will be prefetched when the map is rendered. Map data that was already cached will not be removed until the least recently used strategy (LRU) applies. That means you cannot remove any content from the map cache by updating the `LayerConfiguration`. However, for new map data, it will be applied.

    By default the list contains:

    - [`LayerConfiguration.Feature.DETAIL_RENDERING`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#DETAIL_RENDERING)
    - [`LayerConfiguration.Feature.NAVIGATION`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#NAVIGATION)
    - [`LayerConfiguration.Feature.OFFLINE_SEARCH`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#OFFLINE_SEARCH)
    - [`LayerConfiguration.Feature.OFFLINE_ROUTING`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#OFFLINE_ROUTING)
    - [`LayerConfiguration.Feature.RENDERING`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#RENDERING)
    - [`LayerConfiguration.Feature.TRUCK`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#TRUCK)

    Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
