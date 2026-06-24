---
title: "LayerConfiguration (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- LayerConfiguration.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.core.engine.LayerConfiguration</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">LayerConfiguration</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>A class to configure which layers should be enabled or disabled in the OCM map data.
 Disabling a layer allows to reduce the amount of data that will be
 downloaded or prefetched from the internet, for example, when panning the map view online or when downloading maps for offline use.
 </p><p><code>LayerConfiguration</code> changes made via <a href="sdk-for-android-explore-sdkoptions" title="class in com.here.sdk.core.engine"><code>SDKOptions</code></a> require <code>sdk.maploader.MapUpdater</code> to align previously downloaded content.
 To ensure that the changes in <a href="sdk-for-android-explore-sdkoptions" title="class in com.here.sdk.core.engine"><code>SDKOptions</code></a> affect the map data,
 it is recommended to trigger a map update. Without calling <code>mapUpdater.updateCatalog(...)</code>,
 the adjustments will apply only to future map downloads and will not impact the currently installed map data, either in the cache or in the persisted storage.
 Note that calling <code>updateCatalog(...)</code> will
 update the version, only when a map update is available in the catalog.
 </p><p><strong>Notes</strong>
<ul>
<li>
<p>The <code>LayerConfiguration</code> is only available for the Navigate licenses that contains the offline maps
 feature. It has no effect on other license.
 </p></li>
<li>
<p>The <code>LayerConfiguration</code> cannot be set separately for a region, it will be applied globally
 for all regions that will be downloaded in the future.
 </p></li>
<li>
<p>It is not possible to specify a separate <code>LayerConfiguration</code> for the map cache and offline maps.
 The <code>LayerConfiguration</code> will be always applied to both.
 </p></li>
<li>
<p>If a <code>LayerConfiguration</code> is applied, then only the listed features will be enabled,
 all others will be disabled. For example, if you want to
 disable only one feature, then all other features need to be present, or they will be also disabled.
 </p></li>
</ul>
</p><p>The <code>LayerConfiguration</code> controls which content will be subject of
 <ul>
<li>map download for features in <code>enabledFeatures()</code>,</li>
<li>explicit prefetching using <code>sdk.prefetcher.RoutePrefetcher</code>, <code>sdk.prefetcher.PolygonPrefetcher</code> and
 implicit prefetching, such as when displaying a map view, for features in <code>implicitlyPrefetchedFeatures()</code>.</li>
</ul></p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">

<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a></code></div>
<div class="col-last even-row-color">
<div class="block">Defines a list of possible map data features that can be enabled / disabled.</div>
</div>
</div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">

<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration#enabledFeatures">enabledFeatures</a></code></div>
<div class="col-last even-row-color">
<div class="block">Specifies feature configuration for enabling list of features enabled for map download.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration#implicitlyPrefetchedFeatures">implicitlyPrefetchedFeatures</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Specifies the list of features enabled for implicit and explicit map prefetch.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration#%3Cinit%3E()">LayerConfiguration</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Initializes <code>enabled_features</code>, <code>implicitly_prefetched_features</code> and <code>on_demand_implicitly_prefetched_features</code> with it's default values.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration#%3Cinit%3E(java.util.List)">LayerConfiguration</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a>&gt; enabledFeatures)</code></div>
<div class="col-last odd-row-color">
<div class="block">Initializes both, <code>enabled_features</code> and <code>implicitly_prefetched_features</code> with value passed to constructor.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration#%3Cinit%3E(java.util.List,java.util.List)">LayerConfiguration</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a>&gt; enabledFeatures,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a>&gt; implicitlyPrefetchedFeatures)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>

<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-engine-layerconfiguration#hashCode()">hashCode</a>()</code></div>

</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">

<ul class="member-list">
<li>
<section class="detail" id="enabledFeatures">
<h3>enabledFeatures</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a>&gt;</span> <span class="element-name">enabledFeatures</span></div>
<div class="block"><p>Specifies feature configuration for enabling list of features enabled for map download.
 Empty list disables map download, as no map content specified for download in this case.</p></div>
</section>
</li>
<li>
<section class="detail" id="implicitlyPrefetchedFeatures">
<h3>implicitlyPrefetchedFeatures</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a>&gt;</span> <span class="element-name">implicitlyPrefetchedFeatures</span></div>
<div class="block"><p>Specifies the list of features enabled for implicit and explicit map prefetch.
 Implicit map prefetch will download map content for implicit prefetch features when showing a map in the MapView.
 </p><p>Allows to specify an empty list, effectively disabling implicit prefetching. In this case,
 the system will prioritize minimal network usage, at the cost of reduced offline map availability.
 When disabling certain implicitly prefetched features, less data will be prefetched when the map is rendered. Map
 data that was already cached will not be removed until the least recently used strategy (LRU)
 applies. That means you cannot remove any content from the map cache by updating the
 <code>LayerConfiguration</code>. However, for new map data, it will be applied.
 </p><p>By default the list contains:
 <ul>
<li><a href="sdk-for-android-explore-layerconfiguration.feature#NAVIGATION"><code>LayerConfiguration.Feature.NAVIGATION</code></a></li>
</ul>
</p><p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(java.util.List)">
<h3>LayerConfiguration</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">LayerConfiguration</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a>&gt; enabledFeatures)</span></div>
<div class="block"><p>Initializes both, <code>enabled_features</code> and <code>implicitly_prefetched_features</code> with value passed to constructor.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>enabledFeatures</code> - <p>List of map features to downloader through <code>MapDownloader</code>, and implicitly prefetch when using <code>MapView</code></p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>LayerConfiguration</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">LayerConfiguration</span>()</div>
<div class="block"><p>Initializes <code>enabled_features</code>, <code>implicitly_prefetched_features</code> and <code>on_demand_implicitly_prefetched_features</code> with it's default values.</p></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.util.List,java.util.List)">
<h3>LayerConfiguration</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">LayerConfiguration</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a>&gt; enabledFeatures,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-layerconfiguration.feature" title="enum class in com.here.sdk.core.engine">LayerConfiguration.Feature</a>&gt; implicitlyPrefetchedFeatures)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>enabledFeatures</code> - <p>Specifies feature configuration for enabling list of features enabled for map download.
 Empty list disables map download, as no map content specified for download in this case.</p></dd>
<dd><code>implicitlyPrefetchedFeatures</code> - <p>Specifies the list of features enabled for implicit and explicit map prefetch.
 Implicit map prefetch will download map content for implicit prefetch features when showing a map in the MapView.
 </p><p>Allows to specify an empty list, effectively disabling implicit prefetching. In this case,
 the system will prioritize minimal network usage, at the cost of reduced offline map availability.
 When disabling certain implicitly prefetched features, less data will be prefetched when the map is rendered. Map
 data that was already cached will not be removed until the least recently used strategy (LRU)
 applies. That means you cannot remove any content from the map cache by updating the
 <code>LayerConfiguration</code>. However, for new map data, it will be applied.
 </p><p>By default the list contains:
 <ul>
<li><a href="sdk-for-android-explore-layerconfiguration.feature#NAVIGATION"><code>LayerConfiguration.Feature.NAVIGATION</code></a></li>
</ul>
</p><p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></dd>
</dl>
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
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
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
`
}</HTMLBlock>
