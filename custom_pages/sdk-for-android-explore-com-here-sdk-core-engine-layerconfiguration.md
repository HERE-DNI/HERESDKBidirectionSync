---
title: "LayerConfiguration (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core.engine](sdk-for-android-explore-com-here-sdk-core-engine-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.core.engine.LayerConfiguration → com.here.sdk.core.engine.LayerConfiguration

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">LayerConfiguration</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

A class to configure which layers should be enabled or disabled in the OCM map data. Disabling a layer allows to reduce the amount of data that will be downloaded or prefetched from the internet, for example, when panning the map view online or when downloading maps for offline use. LayerConfiguration changes made via SDKOptions require sdk.maploader.MapUpdater to align previously downloaded content. To ensure that the changes in SDKOptions affect the map data, it is recommended to trigger a map update. Without calling mapUpdater.updateCatalog(...) , the adjustments will apply only to future map downloads and will not impact the currently installed map data, either in the cache or in the persisted storage. Note that calling updateCatalog(...) will update the version, only when a map update is available in the catalog. Notes The LayerConfiguration is only available for the Navigate licenses that contains the offline maps feature. It has no effect on other license. The LayerConfiguration cannot be set separately for a region, it will be applied globally for all regions that will be downloaded in the future. It is not possible to specify a separate LayerConfiguration for the map cache and offline maps. The LayerConfiguration will be always applied to both. If a LayerConfiguration is applied, then only the listed features will be enabled, all others will be disabled. For example, if you want to disable only one feature, then all other features need to be present, or they will be also disabled. The LayerConfiguration controls which content will be subject of map download for features in enabledFeatures() , explicit prefetching using sdk.prefetcher.RoutePrefetcher , sdk.prefetcher.PolygonPrefetcher and implicit prefetching, such as when displaying a map view, for features in implicitlyPrefetchedFeatures() .

</div>

</div>

- <div id="sdk-for-android-explore-nested-class-summary" class="section nested-class-summary">

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

  <a href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature" class="type-name-link" title="enum class in com.here.sdk.core.engine"><code>LayerConfiguration.Feature</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Defines a list of possible map data features that can be enabled / disabled.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-field-summary" class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Field

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`[`LayerConfiguration.Feature`](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")`>`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration#enabledFeatures" class="member-name-link"><code>enabledFeatures</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Specifies feature configuration for enabling list of features enabled for map download.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`[`LayerConfiguration.Feature`](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")`>`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration#implicitlyPrefetchedFeatures" class="member-name-link"><code>implicitlyPrefetchedFeatures</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Specifies the list of features enabled for implicit and explicit map prefetch.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-constructor-summary" class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Constructor

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-constructor-name even-row-color">

      LayerConfiguration ()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Initializes enabled_features , implicitly_prefetched_features and on_demand_implicitly_prefetched_features with it's default values.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      LayerConfiguration ( List < LayerConfiguration.Feature > enabledFeatures)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Initializes both, enabled_features and implicitly_prefetched_features with value passed to constructor.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      LayerConfiguration ( List < LayerConfiguration.Feature > enabledFeatures, List < LayerConfiguration.Feature > implicitlyPrefetchedFeatures)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary" class="section method-summary">

  <div id="sdk-for-android-explore-method-summary-table">

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      equals ( Object obj)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-field-detail" class="section field-details">

  - <div id="sdk-for-android-explore-enabledFeatures" class="section detail">

    ### enabledFeatures

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[LayerConfiguration.Feature](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")\></span> <span class="element-name">enabledFeatures</span>

    </div>

    <div class="block">

    Specifies feature configuration for enabling list of features enabled for map download. Empty list disables map download, as no map content specified for download in this case.

    </div>

    </div>

  - <div id="sdk-for-android-explore-implicitlyPrefetchedFeatures" class="section detail">

    ### implicitlyPrefetchedFeatures

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[LayerConfiguration.Feature](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")\></span> <span class="element-name">implicitlyPrefetchedFeatures</span>

    </div>

    <div class="block">

    Specifies the list of features enabled for implicit and explicit map prefetch. Implicit map prefetch will download map content for implicit prefetch features when showing a map in the MapView. Allows to specify an empty list, effectively disabling implicit prefetching. In this case, the system will prioritize minimal network usage, at the cost of reduced offline map availability. When disabling certain implicitly prefetched features, less data will be prefetched when the map is rendered. Map data that was already cached will not be removed until the least recently used strategy (LRU) applies. That means you cannot remove any content from the map cache by updating the LayerConfiguration . However, for new map data, it will be applied. By default the list contains: LayerConfiguration.Feature.NAVIGATION Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-explore-init-java-util-List" class="section detail">

    ### LayerConfiguration

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">LayerConfiguration</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[LayerConfiguration.Feature](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")\> enabledFeatures)</span>

    </div>

    <div class="block">

    Initializes both, enabled_features and implicitly_prefetched_features with value passed to constructor.

    </div>

    Parameters:  
    `enabledFeatures` -

    List of map features to downloader through `MapDownloader`, and implicitly prefetch when using `MapView`

    </div>

  - <div id="sdk-for-android-explore-init" class="section detail">

    ### LayerConfiguration

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">LayerConfiguration</span>()

    </div>

    <div class="block">

    Initializes enabled_features , implicitly_prefetched_features and on_demand_implicitly_prefetched_features with it's default values.

    </div>

    </div>

  - <div id="sdk-for-android-explore-init-java-util-List-java-util-List" class="section detail">

    ### LayerConfiguration

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">LayerConfiguration</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[LayerConfiguration.Feature](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")\> enabledFeatures, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[LayerConfiguration.Feature](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")\> implicitlyPrefetchedFeatures)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `enabledFeatures` -

    Specifies feature configuration for enabling list of features enabled for map download. Empty list disables map download, as no map content specified for download in this case.

    `implicitlyPrefetchedFeatures` -

    Specifies the list of features enabled for implicit and explicit map prefetch. Implicit map prefetch will download map content for implicit prefetch features when showing a map in the MapView. Allows to specify an empty list, effectively disabling implicit prefetching. In this case, the system will prioritize minimal network usage, at the cost of reduced offline map availability. When disabling certain implicitly prefetched features, less data will be prefetched when the map is rendered. Map data that was already cached will not be removed until the least recently used strategy (LRU) applies. That means you cannot remove any content from the map cache by updating the `LayerConfiguration`. However, for new map data, it will be applied. By default the list contains:

    - [`LayerConfiguration.Feature.NAVIGATION`](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#NAVIGATION)

    Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    </p>

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-equals-java-lang-Object" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-explore-hashCode" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

