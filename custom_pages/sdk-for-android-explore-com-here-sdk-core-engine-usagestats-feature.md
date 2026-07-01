---
title: "UsageStats.Feature (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core.engine](sdk-for-android-explore-com-here-sdk-core-engine-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
java.lang.Enum<UsageStats.Feature>com.here.sdk.core.engine.UsageStats.Feature
→ java.lang.Enum → UsageStats.Feature →
com.here.sdk.core.engine.UsageStats.Feature

</div>

<div id="class-description" class="section class-description">

All Implemented Interfaces:  
<a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html"
class="external-link"
title="class or interface in java.io"><code>Serializable</code></a>, <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html"
class="external-link"
title="class or interface in java.lang"><code>Comparable</code></a>`<`[`UsageStats.Feature`](sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature "enum class in com.here.sdk.core.engine")`>`,
<a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html"
class="external-link"
title="class or interface in java.lang.constant"><code>Constable</code></a>

<!-- -->

Enclosing class:  
[UsageStats](sdk-for-android-explore-com-here-sdk-core-engine-usagestats "class in com.here.sdk.core.engine")

<div class="type-signature">

<span class="modifiers">public static enum
</span><span class="element-name type-name-label">UsageStats.Feature</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html"
class="external-link" title="class or interface in java.lang">Enum</a><[UsageStats.Feature](sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature "enum class in com.here.sdk.core.engine")></span>

</div>

<div class="block">

Represents the feature enum associated with the gathered usage stats.

</div>

</div>

<div class="section summary">

- <div id="nested-class-summary" class="section nested-class-summary">

  <div class="inherited-list">

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

- <div id="enum-constant-summary" class="section constants-summary">

  <div class="caption">

  Enum Constants

  </div>

  <table>
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <thead>
  <tr>
  <th>Enum Constant</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature#DETAILED_RENDERING"
  class="member-name-link"><code>DETAILED_RENDERING</code></a></td>
  <td><div class="block">
  Represents network traffic statistics for online usage corresponding to
  the LayerConfiguration.Feature.DETAIL_RENDERING layer configuration.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature#EV_RENDERING"
  class="member-name-link"><code>EV_RENDERING</code></a></td>
  <td><div class="block">
  Represents network traffic statistics for online usage corresponding to
  the "ev_charging_station_rendering_premium" layer group, enabled with
  LayerConfiguration.Feature.EV .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature#EV_SEARCH"
  class="member-name-link"><code>EV_SEARCH</code></a></td>
  <td><div class="block">
  Represents network traffic statistics for online usage corresponding to
  the "ev_charging_station_search_premium" layer group, enabled with
  LayerConfiguration.Feature.EV .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature#NAVIGATION"
  class="member-name-link"><code>NAVIGATION</code></a></td>
  <td><div class="block">
  Represents network traffic statistics for online usage corresponding to
  the "adas", "ehorizon", "interop", "isa" OCM layers.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature#OTHER"
  class="member-name-link"><code>OTHER</code></a></td>
  <td><div class="block">
  Represents network traffic statistics for feature that doesn't fit into
  other categories.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature#PLACES"
  class="member-name-link"><code>PLACES</code></a></td>
  <td><div class="block">
  Represents network traffic statistics for places search.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature#POSITIONING"
  class="member-name-link"><code>POSITIONING</code></a></td>
  <td><div class="block">
  Represents network traffic statistics for Here Positioning.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature#RDS_TRAFFIC"
  class="member-name-link"><code>RDS_TRAFFIC</code></a></td>
  <td><div class="block">
  Represents network traffic statistics for online usage corresponding to
  the LayerConfiguration.Feature.RDS_TRAFFIC layer configuration.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature#RENDERING"
  class="member-name-link"><code>RENDERING</code></a></td>
  <td><div class="block">
  Represents network traffic statistics for online usage corresponding to
  the LayerConfiguration.Feature.RENDERING layer configuration.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature#ROUTER"
  class="member-name-link"><code>ROUTER</code></a></td>
  <td><div class="block">
  Represents network traffic statistics for online usage corresponding to
  the RoutingEngine .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature#ROUTING"
  class="member-name-link"><code>ROUTING</code></a></td>
  <td><div class="block">
  Represents network traffic statistics for online usage corresponding to
  the following layer configurations:
  LayerConfiguration.Feature.OFFLINE_ROUTING
  LayerConfiguration.Feature.OFFLINE_BUS_ROUTING Counted when data for the
  corresponding layer is requested by the application by performing one of
  the following actions: Pan the map view to areas that have not been
  cached, prefetched or installed before. Use MapDownloader to download
  and install a Region . Prefetch map data into the map cache with the
  RoutePrefetcher for areas that have not been cached, prefetched or
  installed before.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature#SATELLITES"
  class="member-name-link"><code>SATELLITES</code></a></td>
  <td><div class="block">
  Represents network traffic statistics to show satellite map scheme.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature#SEARCH"
  class="member-name-link"><code>SEARCH</code></a></td>
  <td><div class="block">
  Represents network traffic statistics for online usage corresponding to
  the "search", "ev_charging_station_search_premium",
  "fueling_station_premium" OCM layers.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature#SEARCH_ONLINE"
  class="member-name-link"><code>SEARCH_ONLINE</code></a></td>
  <td><div class="block">
  Represents network traffic statistics for online usage corresponding to
  the SearchEngine .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature#TRAFFIC"
  class="member-name-link"><code>TRAFFIC</code></a></td>
  <td><div class="block">
  Represents network traffic statistics for online usage corresponding to
  the calls of TrafficEngine .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature#TRAFFIC_VECTOR_TILES"
  class="member-name-link"><code>TRAFFIC_VECTOR_TILES</code></a></td>
  <td><div class="block">
  Represents network traffic statistics for traffic vector tiles.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature#TRANSIT"
  class="member-name-link"><code>TRANSIT</code></a></td>
  <td><div class="block">
  Represents network traffic statistics for online usage corresponding to
  the "transit" OCM layer.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature#TRANSIT_ROUTING_ENGINE"
  class="member-name-link"><code>TRANSIT_ROUTING_ENGINE</code></a></td>
  <td><div class="block">
  Represents network traffic statistics for online usage corresponding to
  the TransitRoutingEngine .
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature#TRUCK"
  class="member-name-link"><code>TRUCK</code></a></td>
  <td><div class="block">
  Represents network traffic statistics for online usage corresponding to
  the LayerConfiguration.Feature.TRUCK layer configuration.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature#VECTOR_TILES"
  class="member-name-link"><code>VECTOR_TILES</code></a></td>
  <td><div class="block">
  Represents network traffic statistics for online usage corresponding to
  the vector tiles.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Static Methods
  Concrete Methods

  </div>

  <div id="method-summary-table.tabpanel"
  aria-labelledby="method-summary-table-tab0" role="tabpanel">

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Method</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature"
  title="enum class in com.here.sdk.core.engine"><code>UsageStats.Feature</code></a></td>
  <td><pre><code>valueOf(String name)</code></pre></td>
  <td><div class="block">
  Returns the enum constant of this class with the specified name.
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature"
  title="enum class in com.here.sdk.core.engine"><code>UsageStats.Feature</code></a><code>[]</code></td>
  <td><pre><code>values()</code></pre></td>
  <td><div class="block">
  Returns an array containing the constants of this enum class, in the
  order they are declared.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html"
  class="external-link" title="class or interface in java.lang">Enum</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)"
  class="external-link"
  title="class or interface in java.lang"><code>compareTo</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()"
  class="external-link"
  title="class or interface in java.lang"><code>describeConstable</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getDeclaringClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()"
  class="external-link"
  title="class or interface in java.lang"><code>name</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()"
  class="external-link"
  title="class or interface in java.lang"><code>ordinal</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>`, `<a
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
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="enum-constant-detail" class="section constant-details">

  - <div id="DETAILED_RENDERING" class="section detail">

    ### DETAILED_RENDERING

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[UsageStats.Feature](sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">DETAILED_RENDERING</span>

    </div>

    <div class="block">

    Represents network traffic statistics for online usage corresponding
    to the LayerConfiguration.Feature.DETAIL_RENDERING layer
    configuration. Counted when data for the corresponding layer is
    requested by the application by performing one of the following
    actions: Pan the map view to areas that have not been cached,
    prefetched or installed before. Use MapDownloader to download and
    install a Region . Prefetch map data into the map cache with the
    RoutePrefetcher for areas that have not been cached, prefetched or
    installed before. Note that you can enable or disable this feature
    by calling: LayerConfiguration.enabledFeatures(..) or
    LayerConfiguration.implicitlyPrefetchedFeatures() .

    </div>

    </div>

  - <div id="EV_RENDERING" class="section detail">

    ### EV_RENDERING

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[UsageStats.Feature](sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">EV_RENDERING</span>

    </div>

    <div class="block">

    Represents network traffic statistics for online usage corresponding
    to the "ev_charging_station_rendering_premium" layer group, enabled
    with LayerConfiguration.Feature.EV . Note, that
    LayerConfiguration.Feature.EV also enables
    "ev_charging_station_search_premium" layer group, which is
    represented with \[UsageStats.Feature.EV_SEARCH\]. Counted when data
    for the corresponding layer is requested by the application by
    performing one of the following actions: Pan the map view to areas
    that have not been cached, prefetched or installed before. Use
    MapDownloader to download and install a Region . Prefetch map data
    into the map cache with the RoutePrefetcher for areas that have not
    been cached, prefetched or installed before. As of now, this layer
    cannot be turned off.

    </div>

    </div>

  - <div id="EV_SEARCH" class="section detail">

    ### EV_SEARCH

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[UsageStats.Feature](sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">EV_SEARCH</span>

    </div>

    <div class="block">

    Represents network traffic statistics for online usage corresponding
    to the "ev_charging_station_search_premium" layer group, enabled
    with LayerConfiguration.Feature.EV . Note, that
    LayerConfiguration.Feature.EV also enables
    "ev_charging_station_rendering_premium" layer group, which is
    represented with \[UsageStats.Feature.EV_RENDERING\]. Counted when
    data for the corresponding layer is requested by the application by
    performing one of the following actions: Pan the map view to areas
    that have not been cached, prefetched or installed before. Use
    MapDownloader to download and install a Region . Prefetch map data
    into the map cache with the RoutePrefetcher for areas that have not
    been cached, prefetched or installed before. As of now, this layer
    cannot be turned off.

    </div>

    </div>

  - <div id="NAVIGATION" class="section detail">

    ### NAVIGATION

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[UsageStats.Feature](sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">NAVIGATION</span>

    </div>

    <div class="block">

    Represents network traffic statistics for online usage corresponding
    to the "adas", "ehorizon", "interop", "isa" OCM layers. In addition,
    it is also tracking the following layer configurations:
    LayerConfiguration.Feature.NAVIGATION
    LayerConfiguration.Feature.JUNCTION_VIEW_3X4
    LayerConfiguration.Feature.JUNCTION_VIEW_16X9
    LayerConfiguration.Feature.JUNCTION_SIGN_3X4
    LayerConfiguration.Feature.JUNCTION_SIGN_3X5
    LayerConfiguration.Feature.JUNCTION_SIGN_4X3
    LayerConfiguration.Feature.JUNCTION_SIGN_5X3
    LayerConfiguration.Feature.JUNCTION_SIGN_16X9 Counted when data for
    the corresponding layer is requested by the application by
    performing one of the following actions: Pan the map view to areas
    that have not been cached, prefetched or installed before. Use
    MapDownloader to download and install a Region . Prefetch map data
    into the map cache with the RoutePrefetcher for areas that have not
    been cached, prefetched or installed before. Using online navigation
    when the requested data is not cached, prefetched, or installed
    before. As of now, the above listed OCM layers cannot be turned off
    except for those that are exposed as layer configuration.

    </div>

    </div>

  - <div id="PLACES" class="section detail">

    ### PLACES

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[UsageStats.Feature](sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">PLACES</span>

    </div>

    <div class="block">

    Represents network traffic statistics for places search. This is
    legacy statistic which is now replaced by SEARCH_ONLINE .

    </div>

    </div>

  - <div id="RDS_TRAFFIC" class="section detail">

    ### RDS_TRAFFIC

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[UsageStats.Feature](sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">RDS_TRAFFIC</span>

    </div>

    <div class="block">

    Represents network traffic statistics for online usage corresponding
    to the LayerConfiguration.Feature.RDS_TRAFFIC layer configuration.
    Counted when data for the corresponding layer is requested by the
    application by performing one of the following actions: Pan the map
    view to areas that have not been cached, prefetched or installed
    before. Use MapDownloader to download and install a Region .
    Prefetch map data into the map cache with the RoutePrefetcher for
    areas that have not been cached, prefetched or installed before.
    Note that you can enable or disable this feature by calling:
    LayerConfiguration.enabledFeatures(..) or
    LayerConfiguration.implicitlyPrefetchedFeatures() .

    </div>

    </div>

  - <div id="RENDERING" class="section detail">

    ### RENDERING

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[UsageStats.Feature](sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">RENDERING</span>

    </div>

    <div class="block">

    Represents network traffic statistics for online usage corresponding
    to the LayerConfiguration.Feature.RENDERING layer configuration.
    Counted when data for the corresponding layer is requested by the
    application by performing one of the following actions: Pan the map
    view to areas that have not been cached, prefetched or installed
    before. Use MapDownloader to download and install a Region .
    Prefetch map data into the map cache with the RoutePrefetcher for
    areas that have not been cached, prefetched or installed before.
    Note that you can enable or disable this feature by calling:
    LayerConfiguration.enabledFeatures(..) or
    LayerConfiguration.implicitlyPrefetchedFeatures() .

    </div>

    </div>

  - <div id="ROUTER" class="section detail">

    ### ROUTER

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[UsageStats.Feature](sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">ROUTER</span>

    </div>

    <div class="block">

    Represents network traffic statistics for online usage corresponding
    to the RoutingEngine . Includes the following transaction counts and
    APIs: Routing Car, Bicycle, Pedestrian with HRN
    hrn:here:service::olp-here:routing-8:base counted with the use of
    RoutingEngine with CarOptions,BicycleOptions or PedestrianOptions .
    Routing Scooter with HRN
    hrn:here:service::olp-here:routing-8:scooter counted with the use of
    RoutingEngine with ScooterOptions Routing Taxi with HRN
    hrn:here:service::olp-here:routing-8:taxi counted with the use of
    RoutingEngine with TaxiOptions Routing Truck with HRN
    hrn:here:service::olp-here:routing-8:truck counted with the use of
    RoutingEngine with TruckOptions Time-Aware Routing with HRN
    hrn:here:service::olp-here:routing-8:traffic counted with the use of
    RouteOptions with arrivalTime or departureTime Routing EV with HRN
    hrn:here:service::olp-here:routing-8:ev counted with the use of
    RoutingEngine with EVTRuckOptions or EVCarOptions and
    evCarOptions.ensureReachability = true . Route Import with HRN
    hrn:here:service::olp-here:routing-8:import counted with the use of
    RoutingEngine.importRoutes(...) Toll Cost with HRN
    hrn:here:service::olp-here:routing-8:tolls counted with the use of
    RoutingEngine with RouteOptions.enableTolls Routing Bus with HRN
    hrn:here:service::olp-here:routing-8:bus counted with the use of
    RoutingEngine with BusOptions Isoline Routing with HRN
    hrn:here:service::olp-here:isoline-routing-8 counted with the use of
    RoutingEngine with IsolineOptions

    </div>

    </div>

  - <div id="ROUTING" class="section detail">

    ### ROUTING

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[UsageStats.Feature](sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">ROUTING</span>

    </div>

    <div class="block">

    Represents network traffic statistics for online usage corresponding
    to the following layer configurations:
    LayerConfiguration.Feature.OFFLINE_ROUTING
    LayerConfiguration.Feature.OFFLINE_BUS_ROUTING Counted when data for
    the corresponding layer is requested by the application by
    performing one of the following actions: Pan the map view to areas
    that have not been cached, prefetched or installed before. Use
    MapDownloader to download and install a Region . Prefetch map data
    into the map cache with the RoutePrefetcher for areas that have not
    been cached, prefetched or installed before. Note that you can
    enable or disable this feature by calling:
    LayerConfiguration.enabledFeatures(..) or
    LayerConfiguration.implicitlyPrefetchedFeatures() .

    </div>

    </div>

  - <div id="SATELLITES" class="section detail">

    ### SATELLITES

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[UsageStats.Feature](sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">SATELLITES</span>

    </div>

    <div class="block">

    Represents network traffic statistics to show satellite map scheme.
    This includes a Raster Tile Base transaction count with HRN
    hrn:here:service::olp-here:rendering-raster-tiles-3:base .

    </div>

    </div>

  - <div id="SEARCH" class="section detail">

    ### SEARCH

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[UsageStats.Feature](sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">SEARCH</span>

    </div>

    <div class="block">

    Represents network traffic statistics for online usage corresponding
    to the "search", "ev_charging_station_search_premium",
    "fueling_station_premium" OCM layers. Counted when data for the
    corresponding layer is requested by the application by performing
    one of the following actions: Pan the map view to areas that have
    not been cached, prefetched or installed before. Use MapDownloader
    to download and install a Region . Prefetch map data into the map
    cache with the RoutePrefetcher for areas that have not been cached,
    prefetched or installed before. As of now, these layers cannot be
    turned off.

    </div>

    </div>

  - <div id="SEARCH_ONLINE" class="section detail">

    ### SEARCH_ONLINE

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[UsageStats.Feature](sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">SEARCH_ONLINE</span>

    </div>

    <div class="block">

    Represents network traffic statistics for online usage corresponding
    to the SearchEngine . Includes the following transaction counts and
    APIs: Discover/Search with HRN
    hrn:here:service::olp-here:search-opensearch-1 counted with the use
    of SearchEngine textquery search Geocode & Reverse Geocode with HRN
    hrn:here:service::olp-here:geocode-7 counted with the use of
    SearchEngine addressQuery & GeoCoordinates search Autosuggest with
    HRN hrn:here:service::olp-here:search-autosuggest-7 counted with the
    use of SearchEngine suggest

    </div>

    </div>

  - <div id="TRANSIT" class="section detail">

    ### TRANSIT

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[UsageStats.Feature](sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">TRANSIT</span>

    </div>

    <div class="block">

    Represents network traffic statistics for online usage corresponding
    to the "transit" OCM layer. Counted when data for the corresponding
    layer is requested by the application by performing one of the
    following actions: Pan the map view to areas that have not been
    cached, prefetched or installed before. Use MapDownloader to
    download and install a Region . Prefetch map data into the map cache
    with the RoutePrefetcher for areas that have not been cached,
    prefetched or installed before. As of now, this layer cannot be
    turned off.

    </div>

    </div>

  - <div id="TRANSIT_ROUTING_ENGINE" class="section detail">

    ### TRANSIT_ROUTING_ENGINE

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[UsageStats.Feature](sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">TRANSIT_ROUTING_ENGINE</span>

    </div>

    <div class="block">

    Represents network traffic statistics for online usage corresponding
    to the TransitRoutingEngine . This includes a Public Transit
    transaction count with HRN: hrn:here:service::olp-here:transit-8 .

    </div>

    </div>

  - <div id="TRAFFIC" class="section detail">

    ### TRAFFIC

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[UsageStats.Feature](sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">TRAFFIC</span>

    </div>

    <div class="block">

    Represents network traffic statistics for online usage corresponding
    to the calls of TrafficEngine . All calls to TrafficEngine result in
    transaction counts for HRN
    hrn:here:service::olp-here:traffic-api-7:standard .

    </div>

    </div>

  - <div id="TRAFFIC_VECTOR_TILES" class="section detail">

    ### TRAFFIC_VECTOR_TILES

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[UsageStats.Feature](sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">TRAFFIC_VECTOR_TILES</span>

    </div>

    <div class="block">

    Represents network traffic statistics for traffic vector tiles. This
    includes a Traffic vector tile transaction count with HRN:
    hrn:here:service::olp-here:traffic-vector-tiles-2 .

    </div>

    </div>

  - <div id="TRUCK" class="section detail">

    ### TRUCK

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[UsageStats.Feature](sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">TRUCK</span>

    </div>

    <div class="block">

    Represents network traffic statistics for online usage corresponding
    to the LayerConfiguration.Feature.TRUCK layer configuration. Counted
    when data for the corresponding layer is requested by the
    application by performing one of the following actions: Pan the map
    view to areas that have not been cached, prefetched or installed
    before. Use MapDownloader to download and install a Region .
    Prefetch map data into the map cache with the RoutePrefetcher for
    areas that have not been cached, prefetched or installed before.
    Note that you can enable or disable this feature by calling:
    LayerConfiguration.enabledFeatures(..) or
    LayerConfiguration.implicitlyPrefetchedFeatures() .

    </div>

    </div>

  - <div id="VECTOR_TILES" class="section detail">

    ### VECTOR_TILES

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[UsageStats.Feature](sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">VECTOR_TILES</span>

    </div>

    <div class="block">

    Represents network traffic statistics for online usage corresponding
    to the vector tiles. This includes a Vector tile transaction count
    with HRN: hrn:here:service::olp-here:rendering-vector-tiles-2 . This
    statistic is only counted for the HERE SDK (Explore) when showing
    the map view.

    </div>

    </div>

  - <div id="OTHER" class="section detail">

    ### OTHER

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[UsageStats.Feature](sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">OTHER</span>

    </div>

    <div class="block">

    Represents network traffic statistics for feature that doesn't fit
    into other categories. Some examples include: Authentication
    Analytics Any feature not mapped in the existing list.

    </div>

    </div>

  - <div id="POSITIONING" class="section detail">

    ### POSITIONING

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[UsageStats.Feature](sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">POSITIONING</span>

    </div>

    <div class="block">

    Represents network traffic statistics for Here Positioning. This
    includes a Network Positioning transaction count with HRN
    hrn:here:service::olp-here:positioning-2 .

    </div>

    </div>

  </div>

- <div id="method-detail" class="section method-details">

  - <div id="values()" class="section detail">

    ### values

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">[UsageStats.Feature](sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature "enum class in com.here.sdk.core.engine")\[\]</span> <span class="element-name">values</span>()

    </div>

    <div class="block">

    Returns an array containing the constants of this enum class, in the
    order they are declared.

    </div>

    Returns:  
    an array containing the constants of this enum class, in the order
    they are declared

    </div>

  - <div id="valueOf(java.lang.String)" class="section detail">

    ### valueOf

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">[UsageStats.Feature](sdk-for-android-explore-com-here-sdk-core-engine-usagestats-feature "enum class in com.here.sdk.core.engine")</span> <span class="element-name">valueOf</span><span class="parameters">(<a
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

</div>

