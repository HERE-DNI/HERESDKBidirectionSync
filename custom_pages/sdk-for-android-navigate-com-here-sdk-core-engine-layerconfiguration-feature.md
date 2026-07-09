---
title: "LayerConfiguration.Feature (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- LayerConfiguration.Feature.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.core.engine</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">java.lang.Enum</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a>&gt;
<div className="inheritance">com.here.sdk.core.engine.LayerConfiguration.Feature</div>
</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a>&gt;</code>, <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" title="class or interface in java.lang.constant">Constable</a></code></dd>
</dl>
<dl className="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration" title="class in com.here.sdk.core.engine">LayerConfiguration</a></dd>
</dl>

<div className="type-signature"><span className="modifiers">public static enum </span><span className="element-name type-name-label">LayerConfiguration.Feature</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a>&gt;</span></div>
<div className="block"><p>Defines a list of possible map data features that can be enabled / disabled.
 See <a href="sdk-for-android-navigate-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>
Following features are enabled by default:
 <ul>
<li><a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature#DETAIL_RENDERING"><code>DETAIL_RENDERING</code></a></li>
<li><a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature#LANDMARKS_3D"><code>LANDMARKS_3D</code></a></li>
<li><a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature#NAVIGATION"><code>NAVIGATION</code></a></li>
<li><a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature#OFFLINE_SEARCH"><code>OFFLINE_SEARCH</code></a></li>
<li><a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature#OFFLINE_ROUTING"><code>OFFLINE_ROUTING</code></a></li>
<li><a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature#RENDERING"><code>RENDERING</code></a></li>
</ul>
All other features are disabled, by default.
 Each feature enables a set of OCM layer groups to be downloaded by <code>sdk.maploader.MapDownloader</code>.
 Detailed description of each layer group available in the
 <a href="https://www.here.com/docs/bundle/optimized-client-map-developer-guide/page/README.html">HERE Optimized Client Map Developer Guide</a>
Following features are enabled by default for implicit prefetch:
 <ul>
<li><a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature#NAVIGATION"><code>NAVIGATION</code></a></li>
</ul>
Implicit prefetch downloads map content for implicit prefetch features within a view port currently showed by MapView.
 Explicit prefetching is done using <code>sdk.prefetcher.RoutePrefetcher</code> and <code>sdk.prefetcher.PolygonPrefetcher</code>.
 Feature might have more than one layer group predefined to enable full experience. For example,
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature#NAVIGATION"><code>NAVIGATION</code></a> requires routing attributes, visual-friendly
 street names, maneuvers data and ability to interconnect those data sets.
 The same map data is useful for different features, for example <a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature#RENDERING"><code>RENDERING</code></a>
 uses Places data to present it on the MapView, while <a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature#OFFLINE_SEARCH"><code>OFFLINE_SEARCH</code></a> uses
 the same data to enable discoverability by name or category. Hence, features might have overlapping sets of enabled layer groups.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="inherited-list">

<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">Enum.EnumDesc</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">E</a> extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">E</a>&gt;&gt;</code></div>
</section>
</li>
<!-- =========== ENUM CONSTANT SUMMARY =========== -->
<li>
<section className="constants-summary" id="enum-constant-summary">

<div className="caption"><span>Enum Constants</span></div>
<div className="summary-table two-column-summary">


<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature#ADAS">ADAS</a></code></div>
<div className="col-last even-row-color">
<div className="block">Map data which provides ADAS information which includes slope,
 elevation and curvature information.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature#DETAIL_RENDERING">DETAIL_RENDERING</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Additional rendering details like buildings.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature#DETAILED_TERRAIN">DETAILED_TERRAIN</a></code></div>
<div className="col-last even-row-color">
<div className="block">Map data that provides detailed topography information.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature#EHORIZON">EHORIZON</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Map data which provides information about the parts of foreign segments in a tile,
 where a foreign segment is a segment that is stored in another tile but intersects the current tile.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature#EV">EV</a></code></div>
<div className="col-last even-row-color">
<div className="block">Offline map data for <code>EVChargingStation</code>.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature#FUEL_STATION_ATTRIBUTES">FUEL_STATION_ATTRIBUTES</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Enables fuel attributes to be returned by Offline Search engine.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature#JUNCTION_SIGN_16X9">JUNCTION_SIGN_16X9</a></code></div>
<div className="col-last even-row-color">
<div className="block">Map data that provides junction sign images with aspect ratio 16x9.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature#JUNCTION_SIGN_3X4">JUNCTION_SIGN_3X4</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Map data that provides junction sign images with aspect ratio 3x4.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature#JUNCTION_SIGN_3X5">JUNCTION_SIGN_3X5</a></code></div>
<div className="col-last even-row-color">
<div className="block">Map data that provides junction sign images with aspect ratio 3x5.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature#JUNCTION_SIGN_4X3">JUNCTION_SIGN_4X3</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Map data that provides junction sign images with aspect ratio 4x3.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature#JUNCTION_SIGN_5X3">JUNCTION_SIGN_5X3</a></code></div>
<div className="col-last even-row-color">
<div className="block">Map data that provides junction sign images with aspect ratio 5x3.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature#JUNCTION_VIEW_16X9">JUNCTION_VIEW_16X9</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Map data that provides junction view images and assets with aspect ratio 16x9.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature#JUNCTION_VIEW_3X4">JUNCTION_VIEW_3X4</a></code></div>
<div className="col-last even-row-color">
<div className="block">Map data that provides junction view images and assets with aspect ratio 3x4.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature#LANDMARKS_3D">LANDMARKS_3D</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Map data that is used to render 3D landmarks.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature#NAVIGATION">NAVIGATION</a></code></div>
<div className="col-last even-row-color">
<div className="block">Map data that is used for map matching during navigation.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature#OFFLINE_BUS_ROUTING">OFFLINE_BUS_ROUTING</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Map data that is used to calculate bus routes.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature#OFFLINE_ROUTING">OFFLINE_ROUTING</a></code></div>
<div className="col-last even-row-color">
<div className="block">Map data that is used to calculate routes.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature#OFFLINE_SEARCH">OFFLINE_SEARCH</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Map data that is used to search.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature#OFFLINE_SEARCH_GLOBAL">OFFLINE_SEARCH_GLOBAL</a></code></div>
<div className="col-last even-row-color">
<div className="block">Map data used for global search indexing.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature#RDS_TRAFFIC">RDS_TRAFFIC</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Map data that provides traffic broadcast functionality using RDS-TMC format.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature#RENDERING">RENDERING</a></code></div>
<div className="col-last even-row-color">
<div className="block">A basic set of rendering features such as carto POIs.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature#TERRAIN">TERRAIN</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Map data that provides topography information.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature#TRUCK">TRUCK</a></code></div>
<div className="col-last even-row-color">
<div className="block">Map data that is used to calculate truck routes.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature#TRUCK_SERVICE_ATTRIBUTES">TRUCK_SERVICE_ATTRIBUTES</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Enables truck related attributes to be returned by Offline Search engine.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Enum">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)" title="class or interface in java.lang">compareTo</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()" title="class or interface in java.lang">describeConstable</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()" title="class or interface in java.lang">getDeclaringClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()" title="class or interface in java.lang">name</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()" title="class or interface in java.lang">ordinal</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String)" title="class or interface in java.lang">valueOf</a></code></div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ ENUM CONSTANT DETAIL =========== -->
<li>
<section className="constant-details" id="enum-constant-detail">

<ul className="member-list">
<li>
<section className="detail" id="DETAIL_RENDERING">
<h3>DETAIL_RENDERING</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span className="element-name">DETAIL_RENDERING</span></div>
<div className="block"><p>Additional rendering details like buildings. Only used for the MapView.
 When not set, the data will be excluded when downloading offline regions or prefetching areas
 that contain such data. However, during online usage such data may still be downloaded into the
 cache and shown. Increase of 11-16% is to be expected for map size, in case of enabling this feature.
 Feature enables following OCM layer groups:
 <ul>
<li>"detailed_rendering"</li>
</ul></p></div>
</section>
</li>
<li>
<section className="detail" id="NAVIGATION">
<h3>NAVIGATION</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span className="element-name">NAVIGATION</span></div>
<div className="block"><p>Map data that is used for map matching during navigation. When not set,
 navigation may not work properly when being used offline.
 Increase of 5-7% is to be expected for map size, but pay attention, that this feature is depended on
 other layer groups (e.g. routing), so, in total is takes about 21-29 % of map size.
 Feature enables following OCM layer groups:
 <ul>
<li>"interop"</li>
<li>"rendering"</li>
<li>"navigation"</li>
<li>"routing"</li>
</ul></p></div>
</section>
</li>
<li>
<section className="detail" id="OFFLINE_SEARCH">
<h3>OFFLINE_SEARCH</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span className="element-name">OFFLINE_SEARCH</span></div>
<div className="block"><p>Map data that is used to search. When not set, the OfflineSearchEngine may not
 work properly when being used offline.
 Feature enables following OCM layer groups:
 <ul>
<li>"rendering"</li>
<li>"routing"</li>
<li>"search"</li>
</ul></p></div>
</section>
</li>
<li>
<section className="detail" id="OFFLINE_SEARCH_GLOBAL">
<h3>OFFLINE_SEARCH_GLOBAL</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span className="element-name">OFFLINE_SEARCH_GLOBAL</span></div>
<div className="block"><p>Map data used for global search indexing. This feature enables searches
 across broader geographic areas and improves both performance and accuracy
 by leveraging global search indices.
 By default this feature is disabled.
 Enables the HERE SDK to use the enhanced offline search algorithm for downloaded map regions when:
 <ul>
<li><code>OFFLINE_SEARCH_GLOBAL</code> is included in <a href="sdk-for-android-navigate-layerconfiguration#enabledFeatures"><code>LayerConfiguration.enabledFeatures</code></a> and</li>
<li>downloaded map regions contain the required OCM layer groups listed below.</li>
</ul>
Also enables the enhanced offline search algorithm for implicitly prefetched map content when:
 <ul>
<li><code>OFFLINE_SEARCH_GLOBAL</code> is included in <a href="sdk-for-android-navigate-layerconfiguration#implicitlyPrefetchedFeatures"><code>LayerConfiguration.implicitlyPrefetchedFeatures</code></a> and</li>
<li>downloaded map regions (if present) contain the required OCM layer groups.</li>
</ul>
Both options can be enabled together. However, if enabling the feature for
 implicitly prefetched content, it is recommended to also enable it for
 downloaded map regions to ensure consistent search behavior.
 <strong>Important</strong>: After enabling this feature, make sure to update the cached offline maps.
 If the cached maps are not updated, the algorithm will either:
 <ol>
<li>Fall back to the stable offline search if <code>OFFLINE_SEARCH</code> is still included in <a href="sdk-for-android-navigate-layerconfiguration#enabledFeatures"><code>LayerConfiguration.enabledFeatures</code></a>, or</li>
<li>Produce a <code>LAYERS_NOT_DOWNLOADED</code> error if the necessary layers are missing.</li>
</ol>
To prevent excessive map size growth, it is recommended to enable only one of
 <code>OFFLINE_SEARCH_GLOBAL</code> or <code>OFFLINE_SEARCH</code> at a time.
 Enabling this feature increases storage requirements:
 <ul>
<li>Downloaded map region size by ~11–16% when enabled via <a href="sdk-for-android-navigate-layerconfiguration#enabledFeatures"><code>LayerConfiguration.enabledFeatures</code></a>.</li>
<li>Map cache size by ~40–140% when enabled via <a href="sdk-for-android-navigate-layerconfiguration#implicitlyPrefetchedFeatures"><code>LayerConfiguration.implicitlyPrefetchedFeatures</code></a>
 (upper bound occurs for long routes, e.g., Paris → Rome).</li>
</ul>
Feature enables following OCM layer groups:
 <ul>
<li>"search_global"</li>
<li>"search_data"</li>
</ul>
Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
</li>
<li>
<section className="detail" id="OFFLINE_ROUTING">
<h3>OFFLINE_ROUTING</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span className="element-name">OFFLINE_ROUTING</span></div>
<div className="block"><p>Map data that is used to calculate routes. When not set, the OfflineRoutingEngine
 may not work properly when being used offline.  Increase of 12-16.5% is to be expected for map size, but pay attention,
 that this feature is depended on other layer groups (e.g. navigation), so, in total is takes about 33-45 % of map size.
 Feature enables following OCM layer groups:
 <ul>
<li>"rendering"</li>
<li>"navigation"</li>
<li>"routing"</li>
<li>"interop"</li>
<li>"car_offline_routing"</li>
</ul></p></div>
</section>
</li>
<li>
<section className="detail" id="RENDERING">
<h3>RENDERING</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span className="element-name">RENDERING</span></div>
<div className="block"><p>A basic set of rendering features such as carto POIs. Increase of 16-22% is to be expected for map size, but pay attention,
 that this feature is depended on other layer groups (e.g. navigation), so, in total is takes about 21-29 % of map size.
 Feature enables following OCM layer groups:
 <ul>
<li>"rendering"</li>
</ul></p></div>
</section>
</li>
<li>
<section className="detail" id="TRUCK">
<h3>TRUCK</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span className="element-name">TRUCK</span></div>
<div className="block"><p>Map data that is used to calculate truck routes. When not set,
 the <code>OfflineRoutingEngine</code> may not work properly when being used to calculate truck routes.
 It is also used for map matching during truck navigation and for vehicle restriction
 visualization.
 When not set, truck navigation may not work properly when being used offline.
 Online truck navigation will still work when the device has an online connection.
 Increase of 0.7-1.1% is to be expected for map size, in case of enabling this feature.
 By default this feature is disabled.
 Feature enables following OCM layer groups:
 <ul>
<li>"truck"</li>
<li>"long_truck_offline_routing"</li>
<li>"truck_offline_routing"</li>
</ul></p></div>
</section>
</li>
<li>
<section className="detail" id="LANDMARKS_3D">
<h3>LANDMARKS_3D</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span className="element-name">LANDMARKS_3D</span></div>
<div className="block"><p>Map data that is used to render 3D landmarks. When not set, the data
 will be excluded when downloading offline regions or prefetching areas that contain such data.
 When the <code>landmarks</code> <code>MapFeature</code> is set to be visible for a <code>MapScene</code>, 3D landmarks will still be loaded and
 visible during online usage. Increase of 2-3% is to be expected for map size, in case of enabling this feature.
 3D landmark rendering is enabled by default in grayscale on normal,
 logistics and topo schemes, and in textureless mode on lite schemes. However, when this map data feature is disabled,
 the 3D landmark rendering for the above schemes will not work in offline mode with the downloaded map packages.
 Feature enables following OCM layer groups:
 <ul>
<li>"landmarks"</li>
</ul></p></div>
</section>
</li>
<li>
<section className="detail" id="EV">
<h3>EV</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span className="element-name">EV</span></div>
<div className="block"><p>Offline map data for <code>EVChargingStation</code>.
 Feature enables following OCM layer groups:
 <ul>
<li>"ev_charging_station_rendering_premium"</li>
<li>"ev_charging_station_search_premium"</li>
</ul></p></div>
</section>
</li>
<li>
<section className="detail" id="TRUCK_SERVICE_ATTRIBUTES">
<h3>TRUCK_SERVICE_ATTRIBUTES</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span className="element-name">TRUCK_SERVICE_ATTRIBUTES</span></div>
<div className="block"><p>Enables truck related attributes to be returned by Offline Search engine.
 Feature enables following OCM layer groups:
 <ul>
<li>"truck_service_premium"</li>
</ul></p></div>
</section>
</li>
<li>
<section className="detail" id="FUEL_STATION_ATTRIBUTES">
<h3>FUEL_STATION_ATTRIBUTES</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span className="element-name">FUEL_STATION_ATTRIBUTES</span></div>
<div className="block"><p>Enables fuel attributes to be returned by Offline Search engine.
 Feature enables following OCM layer groups:
 <ul>
<li>"fueling_station_premium"</li>
</ul></p></div>
</section>
</li>
<li>
<section className="detail" id="OFFLINE_BUS_ROUTING">
<h3>OFFLINE_BUS_ROUTING</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span className="element-name">OFFLINE_BUS_ROUTING</span></div>
<div className="block"><p>Map data that is used to calculate bus routes.
 When not set, the <code>OfflineRoutingEngine</code> may not be able to calculate routes with <code>BusOptions</code>.
 Feature enables following OCM layer groups:
 <ul>
<li>"bus_offline_routing"</li>
</ul></p></div>
</section>
</li>
<li>
<section className="detail" id="JUNCTION_VIEW_3X4">
<h3>JUNCTION_VIEW_3X4</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span className="element-name">JUNCTION_VIEW_3X4</span></div>
<div className="block"><p>Map data that provides junction view images and assets with aspect ratio 3x4.
 This will also provide common assets that do not depend on specific aspect ratio.
 By default this feature is disabled.
 Feature enables following OCM layer groups:
 <ul>
<li>"junction_view_file_3x4"</li>
<li>"junction_view_asset_3x4"</li>
<li>"junction_view_asset_common"</li>
</ul></p></div>
</section>
</li>
<li>
<section className="detail" id="JUNCTION_VIEW_16X9">
<h3>JUNCTION_VIEW_16X9</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span className="element-name">JUNCTION_VIEW_16X9</span></div>
<div className="block"><p>Map data that provides junction view images and assets with aspect ratio 16x9.
 This will also provide common assets that do not depend on specific aspect ratio.
 By default this feature is disabled.
 Feature enables following OCM layer groups:
 <ul>
<li>"junction_view_file_16x9"</li>
<li>"junction_view_asset_16x9"</li>
<li>"junction_view_asset_common"</li>
</ul></p></div>
</section>
</li>
<li>
<section className="detail" id="JUNCTION_SIGN_3X4">
<h3>JUNCTION_SIGN_3X4</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span className="element-name">JUNCTION_SIGN_3X4</span></div>
<div className="block"><p>Map data that provides junction sign images with aspect ratio 3x4.
 By default this feature is disabled.
 Feature enables following OCM layer groups:
 <ul>
<li>"junction_sign_file_3x4"</li>
</ul></p></div>
</section>
</li>
<li>
<section className="detail" id="JUNCTION_SIGN_3X5">
<h3>JUNCTION_SIGN_3X5</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span className="element-name">JUNCTION_SIGN_3X5</span></div>
<div className="block"><p>Map data that provides junction sign images with aspect ratio 3x5.
 By default this feature is disabled.
 Feature enables following OCM layer groups:
 <ul>
<li>"junction_sign_file_3x5"</li>
</ul></p></div>
</section>
</li>
<li>
<section className="detail" id="JUNCTION_SIGN_4X3">
<h3>JUNCTION_SIGN_4X3</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span className="element-name">JUNCTION_SIGN_4X3</span></div>
<div className="block"><p>Map data that provides junction sign images with aspect ratio 4x3.
 By default this feature is disabled.
 Feature enables following OCM layer groups:
 <ul>
<li>"junction_sign_file_4x3"</li>
</ul></p></div>
</section>
</li>
<li>
<section className="detail" id="JUNCTION_SIGN_5X3">
<h3>JUNCTION_SIGN_5X3</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span className="element-name">JUNCTION_SIGN_5X3</span></div>
<div className="block"><p>Map data that provides junction sign images with aspect ratio 5x3.
 By default this feature is disabled.
 Feature enables following OCM layer groups:
 <ul>
<li>"junction_sign_file_5x3"</li>
</ul></p></div>
</section>
</li>
<li>
<section className="detail" id="JUNCTION_SIGN_16X9">
<h3>JUNCTION_SIGN_16X9</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span className="element-name">JUNCTION_SIGN_16X9</span></div>
<div className="block"><p>Map data that provides junction sign images with aspect ratio 16x9.
 By default this feature is disabled.
 Feature enables following OCM layer groups:
 <ul>
<li>"junction_sign_file_16x9"</li>
</ul></p></div>
</section>
</li>
<li>
<section className="detail" id="TERRAIN">
<h3>TERRAIN</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span className="element-name">TERRAIN</span></div>
<div className="block"><p>Map data that provides topography information.
 The related map feature  with mode
 is enabled by default on topo map schemes.
 It is disabled by default on all other schemes.
 Note that this change has performance implications, with additional data consumption and
 impact on rendering frame rate.
 If performance is a concern, this feature can be disabled from the application side when
 loading the map scene.
 However, when this map data feature is disabled,
 the terrain rendering for the above schemes will not work in offline mode with the downloaded map packages.
 Feature enables following OCM layer groups:
 <ul>
<li>"terrain"</li>
</ul></p></div>
</section>
</li>
<li>
<section className="detail" id="DETAILED_TERRAIN">
<h3>DETAILED_TERRAIN</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span className="element-name">DETAILED_TERRAIN</span></div>
<div className="block"><p>Map data that provides detailed topography information.
 By default this feature is disabled.
 Feature enables following OCM layer groups:
 <ul>
<li>"detailed_terrain"</li>
</ul></p></div>
</section>
</li>
<li>
<section className="detail" id="ADAS">
<h3>ADAS</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span className="element-name">ADAS</span></div>
<div className="block"><p>Map data which provides ADAS information which includes slope,
 elevation and curvature information.
 By default this feature is disabled.
 Feature enables following OCM layer groups:
 <ul>
<li>"adas"</li>
</ul></p></div>
</section>
</li>
<li>
<section className="detail" id="EHORIZON">
<h3>EHORIZON</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span className="element-name">EHORIZON</span></div>
<div className="block"><p>Map data which provides information about the parts of foreign segments in a tile,
 where a foreign segment is a segment that is stored in another tile but intersects the current tile.
 By default this feature is disabled.
 Feature enables following OCM layer groups:
 <ul>
<li>"ehorizon"</li>
</ul></p></div>
</section>
</li>
<li>
<section className="detail" id="RDS_TRAFFIC">
<h3>RDS_TRAFFIC</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span className="element-name">RDS_TRAFFIC</span></div>
<div className="block"><p>Map data that provides traffic broadcast functionality using RDS-TMC format.
 It should be used when there is no internet connection, so that the routing module can utilize
 traffic data coming over the radio channel to build a route in the offline mode.
 Feature enables following OCM layer groups:
 <ul>
<li>"traffic"</li>
</ul></p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="values()">
<h3>values</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a>[]</span> <span className="element-name">values</span>()</div>
<div className="block">Returns an array containing the constants of this enum class, in
the order they are declared.</div>
<dl className="notes">
<dt>Returns:</dt>
<dd>an array containing the constants of this enum class, in the order they are declared</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="valueOf(java.lang.String)">
<h3>valueOf</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-layerconfiguration-feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span className="element-name">valueOf</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div className="block">Returns the enum constant of this class with the specified name.
The string must match <i>exactly</i> an identifier used to declare an
enum constant in this class.  (Extraneous whitespace characters are 
not permitted.)</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the name of the enum constant to be returned.</dd>
<dt>Returns:</dt>
<dd>the enum constant with the specified name</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if this enum class has no constant with the specified name</dd>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html" title="class or interface in java.lang">NullPointerException</a></code> - if the argument is null</dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->

</div>
</div>



</div>
`
}</HTMLBlock>
