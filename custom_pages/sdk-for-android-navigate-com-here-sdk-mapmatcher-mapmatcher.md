---
title: "MapMatcher (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapmatcher-mapmatcher"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapMatcher.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapmatcher</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapmatcher.MapMatcher</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">MapMatcher</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>This class provides map-matching functionality. It determines whether a location can be
 matched to a nearby road network and provides additional OCM map data for that location.
 <strong>Note:</strong> This is a <strong>beta</strong> release of this feature. There may be bugs and unexpected
 behaviors. Related APIs may change in future releases without a deprecation process.
 A <code>MapMatcher</code> maintains an internal state across location updates.
 This helps to check if the match is consistent with previous matches or if an unrealistic jump occurred due to low accuracy
 of the provided location.
 A <code>MapMatcher</code> requires OCM tile data, either through caching, prefetching, or installed <code>Region</code> data.
 If the necessary tiles are not found, an online request is initiated. Note that in such cases,
 the download is triggered silently in the background, and <code>null</code> is returned
 immediately.
 The <code>MapMatcher</code> supports two layer configurations for retrieving segment geometry data:
 <ul>
<li>
<strong>Rendering layer (<code>LayerConfiguration.Feature.RENDERING</code>)</strong>: Enabled by default.
 If your application uses map rendering or <code>MapView</code> components, using this layer is recommended.
 </li>
<li>
<strong>eHorizon layer (<code>LayerConfiguration.Feature.EHORIZON</code>)</strong>: Not enabled by default.
 It encodes segment geometries outside the rendering layer groups to reduce the amount of downloaded data.
 Use the eHorizon layer when:
 <ul>
<li>No <code>MapView</code> is used in your application.</li>
<li>Only the eHorizon layer is used in your application.
 In these cases, using the eHorizon layer will reduce the required data to download. If the rendering layer is enabled, it will increase the required data to download.</li>
</ul>
</li>
</ul>
<strong>Important</strong>: If <code>useRenderingLayers</code> is set to <code>false</code> without properly enabling the eHorizon layer,
 it may produce incorrect results. Layer configuration is especially important when prefetching or installing
 region data. Missing data will be downloaded online automatically as needed.
 If your hardware supports pitch and high precision altitude information and you want to use them in the <code>MapMatcher</code>
 to improve map-matching, then enable the <code>LayerConfiguration.Feature.ADAS</code> layer:
 <ol>
<li>Turn on the <code>ADAS</code> layer via <code>LayerConfiguration.enabledFeatures</code> (it will increase data consumption).</li>
<li>If available, set <code>location.pitchInDegrees</code>, <code>location.coordinates.altitude</code> and <code>location.verticalAccuracyInMeters</code>.</li>
<li>In case of issues, please contact your HERE representative.</li>
</ol></p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapmatcher-mapmatcher#%3Cinit%3E()">MapMatcher</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance of this class.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapmatcher-mapmatcher#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine)">MapMatcher</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a new instance of this class.</div>
</div>
<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapmatcher-mapmatcher#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine,boolean)">MapMatcher</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 boolean useRenderingLayers)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance of this class.</div>
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
<h3>MapMatcher</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">MapMatcher</span>()
           throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div className="block"><p>Creates a new instance of this class.</p></div>
<dl className="notes">
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine)">
<h3>MapMatcher</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">MapMatcher</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</span>
           throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div className="block"><p>Creates a new instance of this class.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>A SDKEngine instance.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine,boolean)">
<h3>MapMatcher</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">MapMatcher</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 boolean useRenderingLayers)</span>
           throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div className="block"><p>Creates a new instance of this class.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>A SDKEngine instance.</p></dd>
<dd><code>useRenderingLayers</code> - <p>When set to true, <code>LayerConfiguration.Feature.RENDERING</code> is used;
     otherwise, <code>LayerConfiguration.Feature.EHORIZON</code> is used to retrieve segment geometry data from the OCM map.
     Note: Ensure the corresponding layer is properly enabled in your <code>LayerConfiguration</code> to avoid incorrect results.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
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
<section className="detail" id="match(com.here.sdk.core.Location)">
<h3>match</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-mapmatchedlocation" title="class in com.here.sdk.navigation">MapMatchedLocation</a></span> <span className="element-name">match</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-location" title="class in com.here.sdk.core">Location</a> location)</span></div>
<div className="block"><p>This method computes the map-matched location for the provided input location.
 Currently, matching is performed within a 50-meter radius of the provided location. If no road network is found
 within that radius, <code>null</code> is returned.
 It's required to set <code>time</code> field for each <code>Location</code> object for the <code>MapMatcher</code> to work properly. In case no time is provided,
 <code>null</code> is returned and an error message is logged. It is used to calculate the distance in time between
 consecutive matches. Together with <code>speed</code>, this allows to calculate how likely a match is consistent with a previous match.
 To improve matching accuracy, it is recommended to provide <code>bearing</code> and <code>speed</code> parameters for each <code>Location</code> object.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>location</code> - <p>The input location.</p></dd>
<dt>Returns:</dt>
<dd><p>map-matched location or <code>null</code> if the location could not be matched to a road network.</p></dd>
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
