---
title: "MapSceneLoadOptionsBuilder (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapsceneloadoptionsbuilder"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapSceneLoadOptionsBuilder.html -->









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-com-here-sdk-mapview-package-summary">com.here.sdk.mapview</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-explore-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapview.MapSceneLoadOptionsBuilder</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">MapSceneLoadOptionsBuilder</span>
<span class="extends-implements">extends <a href="sdk-for-android-explore-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Builder for creating <a href="sdk-for-android-explore-mapsceneloadoptions" title="class in com.here.sdk.mapview"><code>MapSceneLoadOptions</code></a> instances.
 This builder ensures that either a MapScheme or a configuration file is set, but not both.
 </p><p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
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
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-mapsceneloadoptionsbuilder.instantiationerrorcode" title="enum class in com.here.sdk.mapview">MapSceneLoadOptionsBuilder.InstantiationErrorCode</a></code></div>
<div class="col-last even-row-color">
<div class="block">Describes a reason for failing to build a <a href="sdk-for-android-explore-mapsceneloadoptions" title="class in com.here.sdk.mapview"><code>MapSceneLoadOptions</code></a>.</div>
</div>
<div class="col-first odd-row-color"><code>static final class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-mapsceneloadoptionsbuilder.instantiationerrordetails" title="class in com.here.sdk.mapview">MapSceneLoadOptionsBuilder.InstantiationErrorDetails</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Describes the reason for failing to build a <a href="sdk-for-android-explore-mapsceneloadoptions" title="class in com.here.sdk.mapview"><code>MapSceneLoadOptions</code></a>.</div>
</div>
<div class="col-first even-row-color"><code>static final class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-mapsceneloadoptionsbuilder.instantiationexception" title="class in com.here.sdk.mapview">MapSceneLoadOptionsBuilder.InstantiationException</a></code></div>
<div class="col-last even-row-color">
<div class="block">Thrown when failing to build a <a href="sdk-for-android-explore-mapsceneloadoptions" title="class in com.here.sdk.mapview"><code>MapSceneLoadOptions</code></a>.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#%3Cinit%3E()">MapSceneLoadOptionsBuilder</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new builder instance.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-mapsceneloadoptions" title="class in com.here.sdk.mapview">MapSceneLoadOptions</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#build()">build</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Builds the <a href="sdk-for-android-explore-mapsceneloadoptions" title="class in com.here.sdk.mapview"><code>MapSceneLoadOptions</code></a> instance.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-mapsceneloadoptionsbuilder" title="class in com.here.sdk.mapview">MapSceneLoadOptionsBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#withConfigurationFile(java.lang.String)">withConfigurationFile</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> configurationFile)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the configuration file path to load.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-mapsceneloadoptionsbuilder" title="class in com.here.sdk.mapview">MapSceneLoadOptionsBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#withDisabledFeatures(java.util.List)">withDisabledFeatures</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; disabledFeatures)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the features to disable in the new configuration.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-mapsceneloadoptionsbuilder" title="class in com.here.sdk.mapview">MapSceneLoadOptionsBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#withEnabledFeatures(java.util.Map)">withEnabledFeatures</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; enabledFeatures)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the features to enable in the new configuration.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-mapsceneloadoptionsbuilder" title="class in com.here.sdk.mapview">MapSceneLoadOptionsBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#withMapScheme(com.here.sdk.mapview.MapScheme)">withMapScheme</a><wbr/>(<a href="sdk-for-android-explore-mapscheme" title="enum class in com.here.sdk.mapview">MapScheme</a> mapScheme)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the map scheme to load.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-mapsceneloadoptionsbuilder" title="class in com.here.sdk.mapview">MapSceneLoadOptionsBuilder</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#withOverridingMapStyle(com.here.sdk.mapview.Style)">withOverridingMapStyle</a><wbr/>(<a href="sdk-for-android-explore-style" title="class in com.here.sdk.mapview">Style</a> overridingMapStyle)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the style to override what is defined in the scene configuration.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-mapsceneloadoptionsbuilder" title="class in com.here.sdk.mapview">MapSceneLoadOptionsBuilder</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#withWatermarkStyle(com.here.sdk.mapview.WatermarkStyle)">withWatermarkStyle</a><wbr/>(<a href="sdk-for-android-explore-watermarkstyle" title="enum class in com.here.sdk.mapview">WatermarkStyle</a> watermarkStyle)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the watermark style.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>MapSceneLoadOptionsBuilder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MapSceneLoadOptionsBuilder</span>()</div>
<div class="block"><p>Creates a new builder instance.</p></div>
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
<section class="detail" id="withMapScheme(com.here.sdk.mapview.MapScheme)">
<h3>withMapScheme</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-mapsceneloadoptionsbuilder" title="class in com.here.sdk.mapview">MapSceneLoadOptionsBuilder</a></span> <span class="element-name">withMapScheme</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-mapscheme" title="enum class in com.here.sdk.mapview">MapScheme</a> mapScheme)</span></div>
<div class="block"><p>Sets the map scheme to load.
 Any configuration file set through <a href="sdk-for-android-explore-index#withConfigurationFile(java.lang.String)"><code>withConfigurationFile(java.lang.String)</code></a> will be discarded.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mapScheme</code> - <p>Map scheme to load.</p></dd>
<dt>Returns:</dt>
<dd><p>This class instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="withConfigurationFile(java.lang.String)">
<h3>withConfigurationFile</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-mapsceneloadoptionsbuilder" title="class in com.here.sdk.mapview">MapSceneLoadOptionsBuilder</a></span> <span class="element-name">withConfigurationFile</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> configurationFile)</span></div>
<div class="block"><p>Sets the configuration file path to load.
 Any map scheme set through <a href="sdk-for-android-explore-index#withMapScheme(com.here.sdk.mapview.MapScheme)"><code>withMapScheme(com.here.sdk.mapview.MapScheme)</code></a> will be discarded.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>configurationFile</code> - <p>Configuration file path to load.</p></dd>
<dt>Returns:</dt>
<dd><p>This class instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="withEnabledFeatures(java.util.Map)">
<h3>withEnabledFeatures</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-mapsceneloadoptionsbuilder" title="class in com.here.sdk.mapview">MapSceneLoadOptionsBuilder</a></span> <span class="element-name">withEnabledFeatures</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; enabledFeatures)</span></div>
<div class="block"><p>Sets the features to enable in the new configuration.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>enabledFeatures</code> - <p>Features to enable. Key = feature name, value = mode name.</p></dd>
<dt>Returns:</dt>
<dd><p>This class instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="withDisabledFeatures(java.util.List)">
<h3>withDisabledFeatures</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-mapsceneloadoptionsbuilder" title="class in com.here.sdk.mapview">MapSceneLoadOptionsBuilder</a></span> <span class="element-name">withDisabledFeatures</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; disabledFeatures)</span></div>
<div class="block"><p>Sets the features to disable in the new configuration.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>disabledFeatures</code> - <p>Features to disable.</p></dd>
<dt>Returns:</dt>
<dd><p>This class instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="withWatermarkStyle(com.here.sdk.mapview.WatermarkStyle)">
<h3>withWatermarkStyle</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-mapsceneloadoptionsbuilder" title="class in com.here.sdk.mapview">MapSceneLoadOptionsBuilder</a></span> <span class="element-name">withWatermarkStyle</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-watermarkstyle" title="enum class in com.here.sdk.mapview">WatermarkStyle</a> watermarkStyle)</span></div>
<div class="block"><p>Sets the watermark style.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>watermarkStyle</code> - <p>Watermark style to use.</p></dd>
<dt>Returns:</dt>
<dd><p>This class instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="withOverridingMapStyle(com.here.sdk.mapview.Style)">
<h3>withOverridingMapStyle</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-mapsceneloadoptionsbuilder" title="class in com.here.sdk.mapview">MapSceneLoadOptionsBuilder</a></span> <span class="element-name">withOverridingMapStyle</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-style" title="class in com.here.sdk.mapview">Style</a> overridingMapStyle)</span></div>
<div class="block"><p>Sets the style to override what is defined in the scene configuration.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>overridingMapStyle</code> - <p>Map style to override the scene configuration.</p></dd>
<dt>Returns:</dt>
<dd><p>This class instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="build()">
<h3>build</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-mapsceneloadoptions" title="class in com.here.sdk.mapview">MapSceneLoadOptions</a></span> <span class="element-name">build</span>()
                          throws <span class="exceptions"><a href="sdk-for-android-explore-mapsceneloadoptionsbuilder.instantiationexception" title="class in com.here.sdk.mapview">MapSceneLoadOptionsBuilder.InstantiationException</a></span></div>
<div class="block"><p>Builds the <a href="sdk-for-android-explore-mapsceneloadoptions" title="class in com.here.sdk.mapview"><code>MapSceneLoadOptions</code></a> instance.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>A new MapSceneLoadOptions instance.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-explore-mapsceneloadoptionsbuilder.instantiationexception" title="class in com.here.sdk.mapview">MapSceneLoadOptionsBuilder.InstantiationException</a></code> - <p>Indicates an instantiation issue.</p></dd>
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
