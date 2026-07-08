---
title: "LayerConfiguration.Feature (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature"
---

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core.engine](sdk-for-android-explore-com-here-sdk-core-engine-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object java.lang.Enum \< LayerConfiguration.Feature \>
com.here.sdk.core.engine.LayerConfiguration.Feature → java.lang.Enum \<
LayerConfiguration.Feature \>
com.here.sdk.core.engine.LayerConfiguration.Feature →
com.here.sdk.core.engine.LayerConfiguration.Feature

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

All Implemented Interfaces:  
<a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html"
class="external-link"
title="class or interface in java.io"><code>Serializable</code></a>, <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html"
class="external-link"
title="class or interface in java.lang"><code>Comparable</code></a>`<`[`LayerConfiguration.Feature`](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")`>`,
<a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html"
class="external-link"
title="class or interface in java.lang.constant"><code>Constable</code></a>

<!-- -->

Enclosing class:  
[LayerConfiguration](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration "class in com.here.sdk.core.engine")

<div class="type-signature">

<span class="modifiers">public static enum
</span><span class="element-name type-name-label">LayerConfiguration.Feature</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html"
class="external-link" title="class or interface in java.lang">Enum</a>\<[LayerConfiguration.Feature](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")\></span>

</div>

<div class="block">

Defines a list of possible map data features that can be enabled /
disabled. See SDKOptions.layerConfiguration Following features are
enabled by default: DETAIL_RENDERING LANDMARKS_3D NAVIGATION
OFFLINE_SEARCH OFFLINE_ROUTING RENDERING All other features are
disabled, by default. Each feature enables a set of OCM layer groups to
be downloaded by sdk.maploader.MapDownloader . Detailed description of
each layer group available in the HERE Optimized Client Map Developer
Guide Following features are enabled by default for implicit prefetch:
NAVIGATION Implicit prefetch downloads map content for implicit prefetch
features within a view port currently showed by MapView. Explicit
prefetching is done using sdk.prefetcher.RoutePrefetcher and
sdk.prefetcher.PolygonPrefetcher . Feature might have more than one
layer group predefined to enable full experience. For example,
NAVIGATION requires routing attributes, visual-friendly street names,
maneuvers data and ability to interconnect those data sets. The same map
data is useful for different features, for example RENDERING uses Places
data to present it on the MapView, while OFFLINE_SEARCH uses the same
data to enable discoverability by name or category. Hence, features
might have overlapping sets of enabled layer groups.

</div>

</div>

- <div id="sdk-for-android-explore-nested-class-summary"
  class="section nested-class-summary">

  <div class="inherited-list">

  ## Nested classes/interfaces inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html"
  class="external-link" title="class or interface in java.lang">Enum</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html"
  class="external-link"
  title="class or interface in java.lang"><code>Enum.EnumDesc</code></a>`<`<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html"
  class="external-link"
  title="class or interface in java.lang"><code>E</code></a>` extends `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html"
  class="external-link"
  title="class or interface in java.lang"><code>Enum</code></a>`<`<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html"
  class="external-link"
  title="class or interface in java.lang"><code>E</code></a>`>>`

  </div>

  </div>

- <div id="sdk-for-android-explore-enum-constant-summary"
  class="section constants-summary">

  ## Enum Constant Summary

  <div class="caption">

  Enum Constants

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Enum Constant

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#ADAS"
  class="member-name-link"><code>ADAS</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Map data which provides ADAS information which includes slope,
  elevation and curvature information.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#DETAIL_RENDERING"
  class="member-name-link"><code>DETAIL_RENDERING</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Additional rendering details like buildings.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#DETAILED_TERRAIN"
  class="member-name-link"><code>DETAILED_TERRAIN</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Map data that provides detailed topography information.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#EHORIZON"
  class="member-name-link"><code>EHORIZON</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Map data which provides information about the parts of foreign
  segments in a tile, where a foreign segment is a segment that is
  stored in another tile but intersects the current tile.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#EV"
  class="member-name-link"><code>EV</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Offline map data for EVChargingStation .

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#FUEL_STATION_ATTRIBUTES"
  class="member-name-link"><code>FUEL_STATION_ATTRIBUTES</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Enables fuel attributes to be returned by Offline Search engine.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#JUNCTION_SIGN_16X9"
  class="member-name-link"><code>JUNCTION_SIGN_16X9</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Map data that provides junction sign images with aspect ratio 16x9.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#JUNCTION_SIGN_3X4"
  class="member-name-link"><code>JUNCTION_SIGN_3X4</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Map data that provides junction sign images with aspect ratio 3x4.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#JUNCTION_SIGN_3X5"
  class="member-name-link"><code>JUNCTION_SIGN_3X5</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Map data that provides junction sign images with aspect ratio 3x5.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#JUNCTION_SIGN_4X3"
  class="member-name-link"><code>JUNCTION_SIGN_4X3</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Map data that provides junction sign images with aspect ratio 4x3.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#JUNCTION_SIGN_5X3"
  class="member-name-link"><code>JUNCTION_SIGN_5X3</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Map data that provides junction sign images with aspect ratio 5x3.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#JUNCTION_VIEW_16X9"
  class="member-name-link"><code>JUNCTION_VIEW_16X9</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Map data that provides junction view images and assets with aspect
  ratio 16x9.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#JUNCTION_VIEW_3X4"
  class="member-name-link"><code>JUNCTION_VIEW_3X4</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Map data that provides junction view images and assets with aspect
  ratio 3x4.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#LANDMARKS_3D"
  class="member-name-link"><code>LANDMARKS_3D</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Map data that is used to render 3D landmarks.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#NAVIGATION"
  class="member-name-link"><code>NAVIGATION</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Map data that is used for map matching during navigation.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#OFFLINE_BUS_ROUTING"
  class="member-name-link"><code>OFFLINE_BUS_ROUTING</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Map data that is used to calculate bus routes.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#OFFLINE_ROUTING"
  class="member-name-link"><code>OFFLINE_ROUTING</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Map data that is used to calculate routes.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#OFFLINE_SEARCH"
  class="member-name-link"><code>OFFLINE_SEARCH</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Map data that is used to search.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#OFFLINE_SEARCH_GLOBAL"
  class="member-name-link"><code>OFFLINE_SEARCH_GLOBAL</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Map data used for global search indexing.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#RDS_TRAFFIC"
  class="member-name-link"><code>RDS_TRAFFIC</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Map data that provides traffic broadcast functionality using RDS-TMC
  format.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#RENDERING"
  class="member-name-link"><code>RENDERING</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  A basic set of rendering features such as carto POIs.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#TERRAIN"
  class="member-name-link"><code>TERRAIN</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Map data that provides topography information.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#TRUCK"
  class="member-name-link"><code>TRUCK</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Map data that is used to calculate truck routes.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature#TRUCK_SERVICE_ATTRIBUTES"
  class="member-name-link"><code>TRUCK_SERVICE_ATTRIBUTES</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Enables truck related attributes to be returned by Offline Search
  engine.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary"
  class="section method-summary">

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `[`LayerConfiguration.Feature`](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      valueOf ( String name)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Returns the enum constant of this class with the specified name.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `[`LayerConfiguration.Feature`](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")`[]`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      values ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Returns an array containing the constants of this enum class, in the
  order they are declared.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html"
  class="external-link" title="class or interface in java.lang">Enum</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)"
  class="external-link"
  title="class or interface in java.lang"><code>compareTo</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()"
  class="external-link"
  title="class or interface in java.lang"><code>describeConstable</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getDeclaringClass</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()"
  class="external-link"
  title="class or interface in java.lang"><code>name</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()"
  class="external-link"
  title="class or interface in java.lang"><code>ordinal</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String)"
  class="external-link"
  title="class or interface in java.lang"><code>valueOf</code></a>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-enum-constant-detail"
  class="section constant-details">

  ## Enum Constant Details

  - <div id="sdk-for-android-explore-DETAIL_RENDERING"
    class="section detail">

    ### DETAIL_RENDERING

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[LayerConfiguration.Feature](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">DETAIL_RENDERING</span>

    </div>

    <div class="block">

    Additional rendering details like buildings. Only used for the
    MapView. When not set, the data will be excluded when downloading
    offline regions or prefetching areas that contain such data.
    However, during online usage such data may still be downloaded into
    the cache and shown. Increase of 11-16% is to be expected for map
    size, in case of enabling this feature. Feature enables following
    OCM layer groups: "detailed_rendering"

    </div>

    </div>

  - <div id="sdk-for-android-explore-NAVIGATION" class="section detail">

    ### NAVIGATION

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[LayerConfiguration.Feature](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">NAVIGATION</span>

    </div>

    <div class="block">

    Map data that is used for map matching during navigation. When not
    set, navigation may not work properly when being used offline.
    Increase of 5-7% is to be expected for map size, but pay attention,
    that this feature is depended on other layer groups (e.g. routing),
    so, in total is takes about 21-29 % of map size. Feature enables
    following OCM layer groups: "interop" "rendering" "navigation"
    "routing"

    </div>

    </div>

  - <div id="sdk-for-android-explore-OFFLINE_SEARCH"
    class="section detail">

    ### OFFLINE_SEARCH

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[LayerConfiguration.Feature](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">OFFLINE_SEARCH</span>

    </div>

    <div class="block">

    Map data that is used to search. When not set, the
    OfflineSearchEngine may not work properly when being used offline.
    Feature enables following OCM layer groups: "rendering" "routing"
    "search"

    </div>

    </div>

  - <div id="sdk-for-android-explore-OFFLINE_SEARCH_GLOBAL"
    class="section detail">

    ### OFFLINE_SEARCH_GLOBAL

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[LayerConfiguration.Feature](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">OFFLINE_SEARCH_GLOBAL</span>

    </div>

    <div class="block">

    Map data used for global search indexing. This feature enables
    searches across broader geographic areas and improves both
    performance and accuracy by leveraging global search indices. By
    default this feature is disabled. Enables the HERE SDK to use the
    enhanced offline search algorithm for downloaded map regions when:
    OFFLINE_SEARCH_GLOBAL is included in
    LayerConfiguration.enabledFeatures and downloaded map regions
    contain the required OCM layer groups listed below. Also enables the
    enhanced offline search algorithm for implicitly prefetched map
    content when: OFFLINE_SEARCH_GLOBAL is included in
    LayerConfiguration.implicitlyPrefetchedFeatures and downloaded map
    regions (if present) contain the required OCM layer groups. Both
    options can be enabled together. However, if enabling the feature
    for implicitly prefetched content, it is recommended to also enable
    it for downloaded map regions to ensure consistent search behavior.
    Important : After enabling this feature, make sure to update the
    cached offline maps. If the cached maps are not updated, the
    algorithm will either: Fall back to the stable offline search if
    OFFLINE_SEARCH is still included in
    LayerConfiguration.enabledFeatures , or Produce a
    LAYERS_NOT_DOWNLOADED error if the necessary layers are missing. To
    prevent excessive map size growth, it is recommended to enable only
    one of OFFLINE_SEARCH_GLOBAL or OFFLINE_SEARCH at a time. Enabling
    this feature increases storage requirements: Downloaded map region
    size by ~11–16% when enabled via LayerConfiguration.enabledFeatures
    . Map cache size by ~40–140% when enabled via
    LayerConfiguration.implicitlyPrefetchedFeatures (upper bound occurs
    for long routes, e.g., Paris → Rome). Feature enables following OCM
    layer groups: "search_global" "search_data" Note: This is a beta
    release of this feature, so there could be a few bugs and unexpected
    behaviors. Related APIs may change for new releases without a
    deprecation process.

    </div>

    </div>

  - <div id="sdk-for-android-explore-OFFLINE_ROUTING"
    class="section detail">

    ### OFFLINE_ROUTING

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[LayerConfiguration.Feature](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">OFFLINE_ROUTING</span>

    </div>

    <div class="block">

    Map data that is used to calculate routes. When not set, the
    OfflineRoutingEngine may not work properly when being used offline.
    Increase of 12-16.5% is to be expected for map size, but pay
    attention, that this feature is depended on other layer groups (e.g.
    navigation), so, in total is takes about 33-45 % of map size.
    Feature enables following OCM layer groups: "rendering" "navigation"
    "routing" "interop" "car_offline_routing"

    </div>

    </div>

  - <div id="sdk-for-android-explore-RENDERING" class="section detail">

    ### RENDERING

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[LayerConfiguration.Feature](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">RENDERING</span>

    </div>

    <div class="block">

    A basic set of rendering features such as carto POIs. Increase of
    16-22% is to be expected for map size, but pay attention, that this
    feature is depended on other layer groups (e.g. navigation), so, in
    total is takes about 21-29 % of map size. Feature enables following
    OCM layer groups: "rendering"

    </div>

    </div>

  - <div id="sdk-for-android-explore-TRUCK" class="section detail">

    ### TRUCK

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[LayerConfiguration.Feature](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">TRUCK</span>

    </div>

    <div class="block">

    Map data that is used to calculate truck routes. When not set, the
    OfflineRoutingEngine may not work properly when being used to
    calculate truck routes. It is also used for map matching during
    truck navigation and for vehicle restriction visualization. When not
    set, truck navigation may not work properly when being used offline.
    Online truck navigation will still work when the device has an
    online connection. Increase of 0.7-1.1% is to be expected for map
    size, in case of enabling this feature. By default this feature is
    disabled. Feature enables following OCM layer groups: "truck"
    "long_truck_offline_routing" "truck_offline_routing"

    </div>

    </div>

  - <div id="sdk-for-android-explore-LANDMARKS_3D"
    class="section detail">

    ### LANDMARKS_3D

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[LayerConfiguration.Feature](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">LANDMARKS_3D</span>

    </div>

    <div class="block">

    Map data that is used to render 3D landmarks. When not set, the data
    will be excluded when downloading offline regions or prefetching
    areas that contain such data. When the landmarks MapFeature is set
    to be visible for a MapScene , 3D landmarks will still be loaded and
    visible during online usage. Increase of 2-3% is to be expected for
    map size, in case of enabling this feature. 3D landmark rendering is
    enabled by default in grayscale on normal, logistics and topo
    schemes, and in textureless mode on lite schemes. However, when this
    map data feature is disabled, the 3D landmark rendering for the
    above schemes will not work in offline mode with the downloaded map
    packages. Feature enables following OCM layer groups: "landmarks"

    </div>

    </div>

  - <div id="sdk-for-android-explore-EV" class="section detail">

    ### EV

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[LayerConfiguration.Feature](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">EV</span>

    </div>

    <div class="block">

    Offline map data for EVChargingStation . Feature enables following
    OCM layer groups: "ev_charging_station_rendering_premium"
    "ev_charging_station_search_premium"

    </div>

    </div>

  - <div id="sdk-for-android-explore-TRUCK_SERVICE_ATTRIBUTES"
    class="section detail">

    ### TRUCK_SERVICE_ATTRIBUTES

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[LayerConfiguration.Feature](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">TRUCK_SERVICE_ATTRIBUTES</span>

    </div>

    <div class="block">

    Enables truck related attributes to be returned by Offline Search
    engine. Feature enables following OCM layer groups:
    "truck_service_premium"

    </div>

    </div>

  - <div id="sdk-for-android-explore-FUEL_STATION_ATTRIBUTES"
    class="section detail">

    ### FUEL_STATION_ATTRIBUTES

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[LayerConfiguration.Feature](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">FUEL_STATION_ATTRIBUTES</span>

    </div>

    <div class="block">

    Enables fuel attributes to be returned by Offline Search engine.
    Feature enables following OCM layer groups:
    "fueling_station_premium"

    </div>

    </div>

  - <div id="sdk-for-android-explore-OFFLINE_BUS_ROUTING"
    class="section detail">

    ### OFFLINE_BUS_ROUTING

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[LayerConfiguration.Feature](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">OFFLINE_BUS_ROUTING</span>

    </div>

    <div class="block">

    Map data that is used to calculate bus routes. When not set, the
    OfflineRoutingEngine may not be able to calculate routes with
    BusOptions . Feature enables following OCM layer groups:
    "bus_offline_routing"

    </div>

    </div>

  - <div id="sdk-for-android-explore-JUNCTION_VIEW_3X4"
    class="section detail">

    ### JUNCTION_VIEW_3X4

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[LayerConfiguration.Feature](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">JUNCTION_VIEW_3X4</span>

    </div>

    <div class="block">

    Map data that provides junction view images and assets with aspect
    ratio 3x4. This will also provide common assets that do not depend
    on specific aspect ratio. By default this feature is disabled.
    Feature enables following OCM layer groups: "junction_view_file_3x4"
    "junction_view_asset_3x4" "junction_view_asset_common"

    </div>

    </div>

  - <div id="sdk-for-android-explore-JUNCTION_VIEW_16X9"
    class="section detail">

    ### JUNCTION_VIEW_16X9

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[LayerConfiguration.Feature](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">JUNCTION_VIEW_16X9</span>

    </div>

    <div class="block">

    Map data that provides junction view images and assets with aspect
    ratio 16x9. This will also provide common assets that do not depend
    on specific aspect ratio. By default this feature is disabled.
    Feature enables following OCM layer groups:
    "junction_view_file_16x9" "junction_view_asset_16x9"
    "junction_view_asset_common"

    </div>

    </div>

  - <div id="sdk-for-android-explore-JUNCTION_SIGN_3X4"
    class="section detail">

    ### JUNCTION_SIGN_3X4

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[LayerConfiguration.Feature](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">JUNCTION_SIGN_3X4</span>

    </div>

    <div class="block">

    Map data that provides junction sign images with aspect ratio 3x4.
    By default this feature is disabled. Feature enables following OCM
    layer groups: "junction_sign_file_3x4"

    </div>

    </div>

  - <div id="sdk-for-android-explore-JUNCTION_SIGN_3X5"
    class="section detail">

    ### JUNCTION_SIGN_3X5

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[LayerConfiguration.Feature](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">JUNCTION_SIGN_3X5</span>

    </div>

    <div class="block">

    Map data that provides junction sign images with aspect ratio 3x5.
    By default this feature is disabled. Feature enables following OCM
    layer groups: "junction_sign_file_3x5"

    </div>

    </div>

  - <div id="sdk-for-android-explore-JUNCTION_SIGN_4X3"
    class="section detail">

    ### JUNCTION_SIGN_4X3

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[LayerConfiguration.Feature](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">JUNCTION_SIGN_4X3</span>

    </div>

    <div class="block">

    Map data that provides junction sign images with aspect ratio 4x3.
    By default this feature is disabled. Feature enables following OCM
    layer groups: "junction_sign_file_4x3"

    </div>

    </div>

  - <div id="sdk-for-android-explore-JUNCTION_SIGN_5X3"
    class="section detail">

    ### JUNCTION_SIGN_5X3

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[LayerConfiguration.Feature](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">JUNCTION_SIGN_5X3</span>

    </div>

    <div class="block">

    Map data that provides junction sign images with aspect ratio 5x3.
    By default this feature is disabled. Feature enables following OCM
    layer groups: "junction_sign_file_5x3"

    </div>

    </div>

  - <div id="sdk-for-android-explore-JUNCTION_SIGN_16X9"
    class="section detail">

    ### JUNCTION_SIGN_16X9

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[LayerConfiguration.Feature](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">JUNCTION_SIGN_16X9</span>

    </div>

    <div class="block">

    Map data that provides junction sign images with aspect ratio 16x9.
    By default this feature is disabled. Feature enables following OCM
    layer groups: "junction_sign_file_16x9"

    </div>

    </div>

  - <div id="sdk-for-android-explore-TERRAIN" class="section detail">

    ### TERRAIN

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[LayerConfiguration.Feature](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">TERRAIN</span>

    </div>

    <div class="block">

    Map data that provides topography information. The related map
    feature with mode is enabled by default on topo map schemes. It is
    disabled by default on all other schemes. Note that this change has
    performance implications, with additional data consumption and
    impact on rendering frame rate. If performance is a concern, this
    feature can be disabled from the application side when loading the
    map scene. However, when this map data feature is disabled, the
    terrain rendering for the above schemes will not work in offline
    mode with the downloaded map packages. Feature enables following OCM
    layer groups: "terrain"

    </div>

    </div>

  - <div id="sdk-for-android-explore-DETAILED_TERRAIN"
    class="section detail">

    ### DETAILED_TERRAIN

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[LayerConfiguration.Feature](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">DETAILED_TERRAIN</span>

    </div>

    <div class="block">

    Map data that provides detailed topography information. By default
    this feature is disabled. Feature enables following OCM layer
    groups: "detailed_terrain"

    </div>

    </div>

  - <div id="sdk-for-android-explore-ADAS" class="section detail">

    ### ADAS

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[LayerConfiguration.Feature](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">ADAS</span>

    </div>

    <div class="block">

    Map data which provides ADAS information which includes slope,
    elevation and curvature information. By default this feature is
    disabled. Feature enables following OCM layer groups: "adas"

    </div>

    </div>

  - <div id="sdk-for-android-explore-EHORIZON" class="section detail">

    ### EHORIZON

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[LayerConfiguration.Feature](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">EHORIZON</span>

    </div>

    <div class="block">

    Map data which provides information about the parts of foreign
    segments in a tile, where a foreign segment is a segment that is
    stored in another tile but intersects the current tile. By default
    this feature is disabled. Feature enables following OCM layer
    groups: "ehorizon"

    </div>

    </div>

  - <div id="sdk-for-android-explore-RDS_TRAFFIC"
    class="section detail">

    ### RDS_TRAFFIC

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[LayerConfiguration.Feature](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">RDS_TRAFFIC</span>

    </div>

    <div class="block">

    Map data that provides traffic broadcast functionality using RDS-TMC
    format. It should be used when there is no internet connection, so
    that the routing module can utilize traffic data coming over the
    radio channel to build a route in the offline mode. Feature enables
    following OCM layer groups: "traffic"

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-values" class="section detail">

    ### values

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">[LayerConfiguration.Feature](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")\[\]</span> <span class="element-name">values</span>()

    </div>

    <div class="block">

    Returns an array containing the constants of this enum class, in the
    order they are declared.

    </div>

    Returns:  
    an array containing the constants of this enum class, in the order
    they are declared

    </div>

  - <div id="sdk-for-android-explore-valueOf-java-lang-String"
    class="section detail">

    ### valueOf

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">[LayerConfiguration.Feature](sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">valueOf</span><span class="parameters">(<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> name)</span>

    </div>

    <div class="block">

    Returns the enum constant of this class with the specified name. The
    string must match exactly an identifier used to declare an enum
    constant in this class. (Extraneous whitespace characters are not
    permitted.)

    </div>

    Parameters:  
    `name` - the name of the enum constant to be returned.

    Returns:  
    the enum constant with the specified name

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html"
    class="external-link"
    title="class or interface in java.lang"><code>IllegalArgumentException</code></a> -
    if this enum class has no constant with the specified name

    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html"
    class="external-link"
    title="class or interface in java.lang"><code>NullPointerException</code></a> -
    if the argument is null

    </div>

  </div>

