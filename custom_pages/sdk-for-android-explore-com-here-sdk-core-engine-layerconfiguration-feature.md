---
title: "LayerConfiguration.Feature (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration-feature"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- LayerConfiguration.Feature.html -->









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-com-here-sdk-core-engine-package-summary">com.here.sdk.core.engine</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">java.lang.Enum</a>&lt;<a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a>&gt;
<div class="inheritance">com.here.sdk.core.engine.LayerConfiguration.Feature</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a>&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" title="class or interface in java.lang.constant">Constable</a></code></dd>
</dl>
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-explore-layerconfiguration" title="class in com.here.sdk.core.engine">LayerConfiguration</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static enum </span><span class="element-name type-name-label">LayerConfiguration.Feature</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a>&gt;</span></div>
<div class="block"><p>Defines a list of possible map data features that can be enabled / disabled.
 See <a href="sdk-for-android-explore-sdkoptions#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>
</p><p>Following features are enabled by default:
 <ul>
<li><a href="sdk-for-android-explore-index#DETAIL_RENDERING"><code>DETAIL_RENDERING</code></a></li>
<li><a href="sdk-for-android-explore-index#LANDMARKS_3D"><code>LANDMARKS_3D</code></a></li>
<li><a href="sdk-for-android-explore-index#NAVIGATION"><code>NAVIGATION</code></a></li>
<li><a href="sdk-for-android-explore-index#OFFLINE_SEARCH"><code>OFFLINE_SEARCH</code></a></li>
<li><a href="sdk-for-android-explore-index#OFFLINE_ROUTING"><code>OFFLINE_ROUTING</code></a></li>
<li><a href="sdk-for-android-explore-index#RENDERING"><code>RENDERING</code></a></li>
</ul>
</p><p>All other features are disabled, by default.
 </p><p>Each feature enables a set of OCM layer groups to be downloaded by <code>sdk.maploader.MapDownloader</code>.
 Detailed description of each layer group available in the
 <a href="https://www.here.com/docs/bundle/optimized-client-map-developer-guide/page/README.html">HERE Optimized Client Map Developer Guide</a>
</p><p>Following features are enabled by default for implicit prefetch:
 <ul>
<li><a href="sdk-for-android-explore-index#NAVIGATION"><code>NAVIGATION</code></a></li>
</ul>
</p><p>Implicit prefetch downloads map content for implicit prefetch features within a view port currently showed by MapView.
 Explicit prefetching is done using <code>sdk.prefetcher.RoutePrefetcher</code> and <code>sdk.prefetcher.PolygonPrefetcher</code>.
 </p><p>Feature might have more than one layer group predefined to enable full experience. For example,
 <a href="sdk-for-android-explore-index#NAVIGATION"><code>NAVIGATION</code></a> requires routing attributes, visual-friendly
 street names, maneuvers data and ability to interconnect those data sets.
 </p><p>The same map data is useful for different features, for example <a href="sdk-for-android-explore-index#RENDERING"><code>RENDERING</code></a>
 uses Places data to present it on the MapView, while <a href="sdk-for-android-explore-index#OFFLINE_SEARCH"><code>OFFLINE_SEARCH</code></a> uses
 the same data to enable discoverability by name or category. Hence, features might have overlapping sets of enabled layer groups.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">

<div class="inherited-list">

<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">Enum.EnumDesc</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">E</a> extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">E</a>&gt;&gt;</code></div>
</section>
</li>
<!-- =========== ENUM CONSTANT SUMMARY =========== -->
<li>
<section class="constants-summary" id="enum-constant-summary">

<div class="caption"><span>Enum Constants</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Enum Constant</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#ADAS">ADAS</a></code></div>
<div class="col-last even-row-color">
<div class="block">Map data which provides ADAS information which includes slope,
 elevation and curvature information.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#DETAIL_RENDERING">DETAIL_RENDERING</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Additional rendering details like buildings.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#DETAILED_TERRAIN">DETAILED_TERRAIN</a></code></div>
<div class="col-last even-row-color">
<div class="block">Map data that provides detailed topography information.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#EHORIZON">EHORIZON</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Map data which provides information about the parts of foreign segments in a tile,
 where a foreign segment is a segment that is stored in another tile but intersects the current tile.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#EV">EV</a></code></div>
<div class="col-last even-row-color">
<div class="block">Offline map data for <code>EVChargingStation</code>.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#FUEL_STATION_ATTRIBUTES">FUEL_STATION_ATTRIBUTES</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Enables fuel attributes to be returned by Offline Search engine.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#JUNCTION_SIGN_16X9">JUNCTION_SIGN_16X9</a></code></div>
<div class="col-last even-row-color">
<div class="block">Map data that provides junction sign images with aspect ratio 16x9.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#JUNCTION_SIGN_3X4">JUNCTION_SIGN_3X4</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Map data that provides junction sign images with aspect ratio 3x4.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#JUNCTION_SIGN_3X5">JUNCTION_SIGN_3X5</a></code></div>
<div class="col-last even-row-color">
<div class="block">Map data that provides junction sign images with aspect ratio 3x5.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#JUNCTION_SIGN_4X3">JUNCTION_SIGN_4X3</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Map data that provides junction sign images with aspect ratio 4x3.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#JUNCTION_SIGN_5X3">JUNCTION_SIGN_5X3</a></code></div>
<div class="col-last even-row-color">
<div class="block">Map data that provides junction sign images with aspect ratio 5x3.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#JUNCTION_VIEW_16X9">JUNCTION_VIEW_16X9</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Map data that provides junction view images and assets with aspect ratio 16x9.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#JUNCTION_VIEW_3X4">JUNCTION_VIEW_3X4</a></code></div>
<div class="col-last even-row-color">
<div class="block">Map data that provides junction view images and assets with aspect ratio 3x4.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#LANDMARKS_3D">LANDMARKS_3D</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Map data that is used to render 3D landmarks.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#NAVIGATION">NAVIGATION</a></code></div>
<div class="col-last even-row-color">
<div class="block">Map data that is used for map matching during navigation.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#OFFLINE_BUS_ROUTING">OFFLINE_BUS_ROUTING</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Map data that is used to calculate bus routes.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#OFFLINE_ROUTING">OFFLINE_ROUTING</a></code></div>
<div class="col-last even-row-color">
<div class="block">Map data that is used to calculate routes.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#OFFLINE_SEARCH">OFFLINE_SEARCH</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Map data that is used to search.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#OFFLINE_SEARCH_GLOBAL">OFFLINE_SEARCH_GLOBAL</a></code></div>
<div class="col-last even-row-color">
<div class="block">Map data used for global search indexing.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#RDS_TRAFFIC">RDS_TRAFFIC</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Map data that provides traffic broadcast functionality using RDS-TMC format.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#RENDERING">RENDERING</a></code></div>
<div class="col-last even-row-color">
<div class="block">A basic set of rendering features such as carto POIs.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#TERRAIN">TERRAIN</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Map data that provides topography information.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#TRUCK">TRUCK</a></code></div>
<div class="col-last even-row-color">
<div class="block">Map data that is used to calculate truck routes.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#TRUCK_SERVICE_ATTRIBUTES">TRUCK_SERVICE_ATTRIBUTES</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Enables truck related attributes to be returned by Offline Search engine.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#valueOf(java.lang.String)">valueOf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the enum constant of this class with the specified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a>[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#values()">values</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns an array containing the constants of this enum class, in
the order they are declared.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Enum">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)" title="class or interface in java.lang">compareTo</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()" title="class or interface in java.lang">describeConstable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()" title="class or interface in java.lang">getDeclaringClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()" title="class or interface in java.lang">name</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()" title="class or interface in java.lang">ordinal</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String)" title="class or interface in java.lang">valueOf</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ ENUM CONSTANT DETAIL =========== -->
<li>
<section class="constant-details" id="enum-constant-detail">

<ul class="member-list">
<li>
<section class="detail" id="DETAIL_RENDERING">
<h3>DETAIL_RENDERING</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span class="element-name">DETAIL_RENDERING</span></div>
<div class="block"><p>Additional rendering details like buildings. Only used for the MapView.
 When not set, the data will be excluded when downloading offline regions or prefetching areas
 that contain such data. However, during online usage such data may still be downloaded into the
 cache and shown. Increase of 11-16% is to be expected for map size, in case of enabling this feature.
 </p><p>Feature enables following OCM layer groups:
 <ul>
<li>"detailed_rendering"</li>
</ul></p></div>
</section>
</li>
<li>
<section class="detail" id="NAVIGATION">
<h3>NAVIGATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span class="element-name">NAVIGATION</span></div>
<div class="block"><p>Map data that is used for map matching during navigation. When not set,
 navigation may not work properly when being used offline.
 Increase of 5-7% is to be expected for map size, but pay attention, that this feature is depended on
 other layer groups (e.g. routing), so, in total is takes about 21-29 % of map size.
 </p><p>Feature enables following OCM layer groups:
 <ul>
<li>"interop"</li>
<li>"rendering"</li>
<li>"navigation"</li>
<li>"routing"</li>
</ul></p></div>
</section>
</li>
<li>
<section class="detail" id="OFFLINE_SEARCH">
<h3>OFFLINE_SEARCH</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span class="element-name">OFFLINE_SEARCH</span></div>
<div class="block"><p>Map data that is used to search. When not set, the OfflineSearchEngine may not
 work properly when being used offline.
 </p><p>Feature enables following OCM layer groups:
 <ul>
<li>"rendering"</li>
<li>"routing"</li>
<li>"search"</li>
</ul></p></div>
</section>
</li>
<li>
<section class="detail" id="OFFLINE_SEARCH_GLOBAL">
<h3>OFFLINE_SEARCH_GLOBAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span class="element-name">OFFLINE_SEARCH_GLOBAL</span></div>
<div class="block"><p>Map data used for global search indexing. This feature enables searches
 across broader geographic areas and improves both performance and accuracy
 by leveraging global search indices.
 By default this feature is disabled.
 </p><p>Enables the HERE SDK to use the enhanced offline search algorithm for downloaded map regions when:
 <ul>
<li><code>OFFLINE_SEARCH_GLOBAL</code> is included in <a href="sdk-for-android-explore-layerconfiguration#enabledFeatures"><code>LayerConfiguration.enabledFeatures</code></a> and</li>
<li>downloaded map regions contain the required OCM layer groups listed below.</li>
</ul>
</p><p>Also enables the enhanced offline search algorithm for implicitly prefetched map content when:
 <ul>
<li><code>OFFLINE_SEARCH_GLOBAL</code> is included in <a href="sdk-for-android-explore-layerconfiguration#implicitlyPrefetchedFeatures"><code>LayerConfiguration.implicitlyPrefetchedFeatures</code></a> and</li>
<li>downloaded map regions (if present) contain the required OCM layer groups.</li>
</ul>
</p><p>Both options can be enabled together. However, if enabling the feature for
 implicitly prefetched content, it is recommended to also enable it for
 downloaded map regions to ensure consistent search behavior.
 </p><p><strong>Important</strong>: After enabling this feature, make sure to update the cached offline maps.
 If the cached maps are not updated, the algorithm will either:
 <ol>
<li>Fall back to the stable offline search if <code>OFFLINE_SEARCH</code> is still included in <a href="sdk-for-android-explore-layerconfiguration#enabledFeatures"><code>LayerConfiguration.enabledFeatures</code></a>, or</li>
<li>Produce a <code>LAYERS_NOT_DOWNLOADED</code> error if the necessary layers are missing.</li>
</ol>
</p><p>To prevent excessive map size growth, it is recommended to enable only one of
 <code>OFFLINE_SEARCH_GLOBAL</code> or <code>OFFLINE_SEARCH</code> at a time.
 </p><p>Enabling this feature increases storage requirements:
 <ul>
<li>Downloaded map region size by ~11–16% when enabled via <a href="sdk-for-android-explore-layerconfiguration#enabledFeatures"><code>LayerConfiguration.enabledFeatures</code></a>.</li>
<li>Map cache size by ~40–140% when enabled via <a href="sdk-for-android-explore-layerconfiguration#implicitlyPrefetchedFeatures"><code>LayerConfiguration.implicitlyPrefetchedFeatures</code></a>
 (upper bound occurs for long routes, e.g., Paris → Rome).</li>
</ul>
</p><p>Feature enables following OCM layer groups:
 <ul>
<li>"search_global"</li>
<li>"search_data"</li>
</ul>
</p><p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
</li>
<li>
<section class="detail" id="OFFLINE_ROUTING">
<h3>OFFLINE_ROUTING</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span class="element-name">OFFLINE_ROUTING</span></div>
<div class="block"><p>Map data that is used to calculate routes. When not set, the OfflineRoutingEngine
 may not work properly when being used offline.  Increase of 12-16.5% is to be expected for map size, but pay attention,
 that this feature is depended on other layer groups (e.g. navigation), so, in total is takes about 33-45 % of map size.
 </p><p>Feature enables following OCM layer groups:
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
<section class="detail" id="RENDERING">
<h3>RENDERING</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span class="element-name">RENDERING</span></div>
<div class="block"><p>A basic set of rendering features such as carto POIs. Increase of 16-22% is to be expected for map size, but pay attention,
 that this feature is depended on other layer groups (e.g. navigation), so, in total is takes about 21-29 % of map size.
 </p><p>Feature enables following OCM layer groups:
 <ul>
<li>"rendering"</li>
</ul></p></div>
</section>
</li>
<li>
<section class="detail" id="TRUCK">
<h3>TRUCK</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span class="element-name">TRUCK</span></div>
<div class="block"><p>Map data that is used to calculate truck routes. When not set,
 the <code>OfflineRoutingEngine</code> may not work properly when being used to calculate truck routes.
 It is also used for map matching during truck navigation and for vehicle restriction
 visualization.
 When not set, truck navigation may not work properly when being used offline.
 Online truck navigation will still work when the device has an online connection.
 Increase of 0.7-1.1% is to be expected for map size, in case of enabling this feature.
 By default this feature is disabled.
 </p><p>Feature enables following OCM layer groups:
 <ul>
<li>"truck"</li>
<li>"long_truck_offline_routing"</li>
<li>"truck_offline_routing"</li>
</ul></p></div>
</section>
</li>
<li>
<section class="detail" id="LANDMARKS_3D">
<h3>LANDMARKS_3D</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span class="element-name">LANDMARKS_3D</span></div>
<div class="block"><p>Map data that is used to render 3D landmarks. When not set, the data
 will be excluded when downloading offline regions or prefetching areas that contain such data.
 When the <code>landmarks</code> <code>MapFeature</code> is set to be visible for a <code>MapScene</code>, 3D landmarks will still be loaded and
 visible during online usage. Increase of 2-3% is to be expected for map size, in case of enabling this feature.
 </p><p>3D landmark rendering is enabled by default in grayscale on normal,
 logistics and topo schemes, and in textureless mode on lite schemes. However, when this map data feature is disabled,
 the 3D landmark rendering for the above schemes will not work in offline mode with the downloaded map packages.
 Feature enables following OCM layer groups:
 <ul>
<li>"landmarks"</li>
</ul></p></div>
</section>
</li>
<li>
<section class="detail" id="EV">
<h3>EV</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span class="element-name">EV</span></div>
<div class="block"><p>Offline map data for <code>EVChargingStation</code>.
 </p><p>Feature enables following OCM layer groups:
 <ul>
<li>"ev_charging_station_rendering_premium"</li>
<li>"ev_charging_station_search_premium"</li>
</ul></p></div>
</section>
</li>
<li>
<section class="detail" id="TRUCK_SERVICE_ATTRIBUTES">
<h3>TRUCK_SERVICE_ATTRIBUTES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span class="element-name">TRUCK_SERVICE_ATTRIBUTES</span></div>
<div class="block"><p>Enables truck related attributes to be returned by Offline Search engine.
 Feature enables following OCM layer groups:
 <ul>
<li>"truck_service_premium"</li>
</ul></p></div>
</section>
</li>
<li>
<section class="detail" id="FUEL_STATION_ATTRIBUTES">
<h3>FUEL_STATION_ATTRIBUTES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span class="element-name">FUEL_STATION_ATTRIBUTES</span></div>
<div class="block"><p>Enables fuel attributes to be returned by Offline Search engine.
 </p><p>Feature enables following OCM layer groups:
 <ul>
<li>"fueling_station_premium"</li>
</ul></p></div>
</section>
</li>
<li>
<section class="detail" id="OFFLINE_BUS_ROUTING">
<h3>OFFLINE_BUS_ROUTING</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span class="element-name">OFFLINE_BUS_ROUTING</span></div>
<div class="block"><p>Map data that is used to calculate bus routes.
 When not set, the <code>OfflineRoutingEngine</code> may not be able to calculate routes with <code>BusOptions</code>.
 </p><p>Feature enables following OCM layer groups:
 <ul>
<li>"bus_offline_routing"</li>
</ul></p></div>
</section>
</li>
<li>
<section class="detail" id="JUNCTION_VIEW_3X4">
<h3>JUNCTION_VIEW_3X4</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span class="element-name">JUNCTION_VIEW_3X4</span></div>
<div class="block"><p>Map data that provides junction view images and assets with aspect ratio 3x4.
 This will also provide common assets that do not depend on specific aspect ratio.
 By default this feature is disabled.
 </p><p>Feature enables following OCM layer groups:
 <ul>
<li>"junction_view_file_3x4"</li>
<li>"junction_view_asset_3x4"</li>
<li>"junction_view_asset_common"</li>
</ul></p></div>
</section>
</li>
<li>
<section class="detail" id="JUNCTION_VIEW_16X9">
<h3>JUNCTION_VIEW_16X9</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span class="element-name">JUNCTION_VIEW_16X9</span></div>
<div class="block"><p>Map data that provides junction view images and assets with aspect ratio 16x9.
 This will also provide common assets that do not depend on specific aspect ratio.
 By default this feature is disabled.
 </p><p>Feature enables following OCM layer groups:
 <ul>
<li>"junction_view_file_16x9"</li>
<li>"junction_view_asset_16x9"</li>
<li>"junction_view_asset_common"</li>
</ul></p></div>
</section>
</li>
<li>
<section class="detail" id="JUNCTION_SIGN_3X4">
<h3>JUNCTION_SIGN_3X4</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span class="element-name">JUNCTION_SIGN_3X4</span></div>
<div class="block"><p>Map data that provides junction sign images with aspect ratio 3x4.
 By default this feature is disabled.
 </p><p>Feature enables following OCM layer groups:
 <ul>
<li>"junction_sign_file_3x4"</li>
</ul></p></div>
</section>
</li>
<li>
<section class="detail" id="JUNCTION_SIGN_3X5">
<h3>JUNCTION_SIGN_3X5</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span class="element-name">JUNCTION_SIGN_3X5</span></div>
<div class="block"><p>Map data that provides junction sign images with aspect ratio 3x5.
 By default this feature is disabled.
 </p><p>Feature enables following OCM layer groups:
 <ul>
<li>"junction_sign_file_3x5"</li>
</ul></p></div>
</section>
</li>
<li>
<section class="detail" id="JUNCTION_SIGN_4X3">
<h3>JUNCTION_SIGN_4X3</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span class="element-name">JUNCTION_SIGN_4X3</span></div>
<div class="block"><p>Map data that provides junction sign images with aspect ratio 4x3.
 By default this feature is disabled.
 </p><p>Feature enables following OCM layer groups:
 <ul>
<li>"junction_sign_file_4x3"</li>
</ul></p></div>
</section>
</li>
<li>
<section class="detail" id="JUNCTION_SIGN_5X3">
<h3>JUNCTION_SIGN_5X3</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span class="element-name">JUNCTION_SIGN_5X3</span></div>
<div class="block"><p>Map data that provides junction sign images with aspect ratio 5x3.
 By default this feature is disabled.
 Feature enables following OCM layer groups:
 <ul>
<li>"junction_sign_file_5x3"</li>
</ul></p></div>
</section>
</li>
<li>
<section class="detail" id="JUNCTION_SIGN_16X9">
<h3>JUNCTION_SIGN_16X9</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span class="element-name">JUNCTION_SIGN_16X9</span></div>
<div class="block"><p>Map data that provides junction sign images with aspect ratio 16x9.
 By default this feature is disabled.
 </p><p>Feature enables following OCM layer groups:
 <ul>
<li>"junction_sign_file_16x9"</li>
</ul></p></div>
</section>
</li>
<li>
<section class="detail" id="TERRAIN">
<h3>TERRAIN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span class="element-name">TERRAIN</span></div>
<div class="block"><p>Map data that provides topography information.
 The related map feature  with mode
 is enabled by default on topo map schemes.
 It is disabled by default on all other schemes.
 </p><p>Note that this change has performance implications, with additional data consumption and
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
<section class="detail" id="DETAILED_TERRAIN">
<h3>DETAILED_TERRAIN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span class="element-name">DETAILED_TERRAIN</span></div>
<div class="block"><p>Map data that provides detailed topography information.
 By default this feature is disabled.
 Feature enables following OCM layer groups:
 <ul>
<li>"detailed_terrain"</li>
</ul></p></div>
</section>
</li>
<li>
<section class="detail" id="ADAS">
<h3>ADAS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span class="element-name">ADAS</span></div>
<div class="block"><p>Map data which provides ADAS information which includes slope,
 elevation and curvature information.
 By default this feature is disabled.
 Feature enables following OCM layer groups:
 <ul>
<li>"adas"</li>
</ul></p></div>
</section>
</li>
<li>
<section class="detail" id="EHORIZON">
<h3>EHORIZON</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span class="element-name">EHORIZON</span></div>
<div class="block"><p>Map data which provides information about the parts of foreign segments in a tile,
 where a foreign segment is a segment that is stored in another tile but intersects the current tile.
 By default this feature is disabled.
 Feature enables following OCM layer groups:
 <ul>
<li>"ehorizon"</li>
</ul></p></div>
</section>
</li>
<li>
<section class="detail" id="RDS_TRAFFIC">
<h3>RDS_TRAFFIC</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span class="element-name">RDS_TRAFFIC</span></div>
<div class="block"><p>Map data that provides traffic broadcast functionality using RDS-TMC format.
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
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="values()">
<h3>values</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a>[]</span> <span class="element-name">values</span>()</div>
<div class="block">Returns an array containing the constants of this enum class, in
the order they are declared.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>an array containing the constants of this enum class, in the order they are declared</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="valueOf(java.lang.String)">
<h3>valueOf</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></span> <span class="element-name">valueOf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Returns the enum constant of this class with the specified name.
The string must match <i>exactly</i> an identifier used to declare an
enum constant in this class.  (Extraneous whitespace characters are 
not permitted.)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the name of the enum constant to be returned.</dd>
<dt>Returns:</dt>
<dd>the enum constant with the specified name</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if this enum class has no constant with the specified name</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html" title="class or interface in java.lang">NullPointerException</a></code> - if the argument is null</dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>





</div>
`
}</HTMLBlock>
