---
title: "MapSceneLoadOptionsBuilder (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapsceneloadoptionsbuilder"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapSceneLoadOptionsBuilder.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapview.MapSceneLoadOptionsBuilder</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">MapSceneLoadOptionsBuilder</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Builder for creating <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapsceneloadoptions" title="class in com.here.sdk.mapview"><code>MapSceneLoadOptions</code></a> instances.
 This builder ensures that either a MapScheme or a configuration file is set, but not both.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="caption"><span>Nested Classes</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static enum </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapsceneloadoptionsbuilder-instantiationerrorcode" title="enum class in com.here.sdk.mapview">MapSceneLoadOptionsBuilder.InstantiationErrorCode</a></code></div>
<div className="col-last even-row-color">
<div className="block">Describes a reason for failing to build a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapsceneloadoptions" title="class in com.here.sdk.mapview"><code>MapSceneLoadOptions</code></a>.</div>
</div>
<div className="col-first odd-row-color"><code>static final class </code></div>
<div className="col-second odd-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapsceneloadoptionsbuilder-instantiationerrordetails" title="class in com.here.sdk.mapview">MapSceneLoadOptionsBuilder.InstantiationErrorDetails</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Describes the reason for failing to build a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapsceneloadoptions" title="class in com.here.sdk.mapview"><code>MapSceneLoadOptions</code></a>.</div>
</div>
<div className="col-first even-row-color"><code>static final class </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapsceneloadoptionsbuilder-instantiationexception" title="class in com.here.sdk.mapview">MapSceneLoadOptionsBuilder.InstantiationException</a></code></div>
<div className="col-last even-row-color">
<div className="block">Thrown when failing to build a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapsceneloadoptions" title="class in com.here.sdk.mapview"><code>MapSceneLoadOptions</code></a>.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapsceneloadoptionsbuilder#%3Cinit%3E()">MapSceneLoadOptionsBuilder</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new builder instance.</div>
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
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;()">
<h3>MapSceneLoadOptionsBuilder</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">MapSceneLoadOptionsBuilder</span>()</div>
<div className="block"><p>Creates a new builder instance.</p></div>
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
<section className="detail" id="withMapScheme(com.here.sdk.mapview.MapScheme)">
<h3>withMapScheme</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapsceneloadoptionsbuilder" title="class in com.here.sdk.mapview">MapSceneLoadOptionsBuilder</a></span> <span className="element-name">withMapScheme</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscheme" title="enum class in com.here.sdk.mapview">MapScheme</a> mapScheme)</span></div>
<div className="block"><p>Sets the map scheme to load.
 Any configuration file set through <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapsceneloadoptionsbuilder#withConfigurationFile(java.lang.String)"><code>withConfigurationFile(java.lang.String)</code></a> will be discarded.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>mapScheme</code> - <p>Map scheme to load.</p></dd>
<dt>Returns:</dt>
<dd><p>This class instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="withConfigurationFile(java.lang.String)">
<h3>withConfigurationFile</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapsceneloadoptionsbuilder" title="class in com.here.sdk.mapview">MapSceneLoadOptionsBuilder</a></span> <span className="element-name">withConfigurationFile</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> configurationFile)</span></div>
<div className="block"><p>Sets the configuration file path to load.
 Any map scheme set through <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapsceneloadoptionsbuilder#withMapScheme(com.here.sdk.mapview.MapScheme)"><code>withMapScheme(com.here.sdk.mapview.MapScheme)</code></a> will be discarded.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>configurationFile</code> - <p>Configuration file path to load.</p></dd>
<dt>Returns:</dt>
<dd><p>This class instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="withEnabledFeatures(java.util.Map)">
<h3>withEnabledFeatures</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapsceneloadoptionsbuilder" title="class in com.here.sdk.mapview">MapSceneLoadOptionsBuilder</a></span> <span className="element-name">withEnabledFeatures</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; enabledFeatures)</span></div>
<div className="block"><p>Sets the features to enable in the new configuration.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>enabledFeatures</code> - <p>Features to enable. Key = feature name, value = mode name.</p></dd>
<dt>Returns:</dt>
<dd><p>This class instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="withDisabledFeatures(java.util.List)">
<h3>withDisabledFeatures</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapsceneloadoptionsbuilder" title="class in com.here.sdk.mapview">MapSceneLoadOptionsBuilder</a></span> <span className="element-name">withDisabledFeatures</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; disabledFeatures)</span></div>
<div className="block"><p>Sets the features to disable in the new configuration.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>disabledFeatures</code> - <p>Features to disable.</p></dd>
<dt>Returns:</dt>
<dd><p>This class instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="withWatermarkStyle(com.here.sdk.mapview.WatermarkStyle)">
<h3>withWatermarkStyle</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapsceneloadoptionsbuilder" title="class in com.here.sdk.mapview">MapSceneLoadOptionsBuilder</a></span> <span className="element-name">withWatermarkStyle</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-watermarkstyle" title="enum class in com.here.sdk.mapview">WatermarkStyle</a> watermarkStyle)</span></div>
<div className="block"><p>Sets the watermark style.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>watermarkStyle</code> - <p>Watermark style to use.</p></dd>
<dt>Returns:</dt>
<dd><p>This class instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="withOverridingMapStyle(com.here.sdk.mapview.Style)">
<h3>withOverridingMapStyle</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapsceneloadoptionsbuilder" title="class in com.here.sdk.mapview">MapSceneLoadOptionsBuilder</a></span> <span className="element-name">withOverridingMapStyle</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-style" title="class in com.here.sdk.mapview">Style</a> overridingMapStyle)</span></div>
<div className="block"><p>Sets the style to override what is defined in the scene configuration.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>overridingMapStyle</code> - <p>Map style to override the scene configuration.</p></dd>
<dt>Returns:</dt>
<dd><p>This class instance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="build()">
<h3>build</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapsceneloadoptions" title="class in com.here.sdk.mapview">MapSceneLoadOptions</a></span> <span className="element-name">build</span>()
                          throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapsceneloadoptionsbuilder-instantiationexception" title="class in com.here.sdk.mapview">MapSceneLoadOptionsBuilder.InstantiationException</a></span></div>
<div className="block"><p>Builds the <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapsceneloadoptions" title="class in com.here.sdk.mapview"><code>MapSceneLoadOptions</code></a> instance.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>A new MapSceneLoadOptions instance.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapsceneloadoptionsbuilder-instantiationexception" title="class in com.here.sdk.mapview">MapSceneLoadOptionsBuilder.InstantiationException</a></code> - <p>Indicates an instantiation issue.</p></dd>
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
