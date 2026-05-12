---
title: "MapMatcher (API Reference)"
slug: "sdk-for-android-navigate-mapmatcher"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapMatcher.html -->
<!DOCTYPE HTML>

<html lang="en">

<body class="class-declaration-page">


<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-navigate-index">Overview</a></li>
<li><a href="sdk-for-android-navigate-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-navigate-package-tree">Tree</a></li>
<li><a href="sdk-for-android-navigate-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-navigate-index-all">Index</a></li>
<li><a href="sdk-for-android-navigate-help-doc#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li>Nested | </li>
<li>Field | </li>
<li><a href="#constructor-summary">Constr</a> | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li>Field | </li>
<li><a href="#constructor-detail">Constr</a> | </li>
<li><a href="#method-detail">Method</a></li>
</ul>
</div>

</div>
<!-- ========= END OF TOP NAVBAR ========= -->
<span class="skip-nav" id="skip-navbar-top"></span></nav>
</header>
<div class="flex-content">
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapmatcher</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapmatcher.MapMatcher</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">MapMatcher</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>This class provides map-matching functionality. It determines whether a location can be
 matched to a nearby road network and provides additional OCM map data for that location.
 <p><strong>Note:</strong> This is a <strong>beta</strong> release of this feature. There may be bugs and unexpected
 behaviors. Related APIs may change in future releases without a deprecation process.
 <p>A <code>MapMatcher</code> maintains an internal state across location updates.
 This helps to check if the match is consistent with previous matches or if an unrealistic jump occurred due to low accuracy
 of the provided location.
 <p>A <code>MapMatcher</code> requires OCM tile data, either through caching, prefetching, or installed <code>Region</code> data.
 If the necessary tiles are not found, an online request is initiated. Note that in such cases,
 the download is triggered silently in the background, and <code>null</code> is returned
 immediately.
 <p>The <code>MapMatcher</code> supports two layer configurations for retrieving segment geometry data:
 <ul>
<li>
<p><strong>Rendering layer (<code>LayerConfiguration.Feature.RENDERING</code>)</strong>: Enabled by default.
 If your application uses map rendering or <code>MapView</code> components, using this layer is recommended.
 </p></li>
<li>
<p><strong>eHorizon layer (<code>LayerConfiguration.Feature.EHORIZON</code>)</strong>: Not enabled by default.
 It encodes segment geometries outside the rendering layer groups to reduce the amount of downloaded data.
 Use the eHorizon layer when:
 <ul>
<li>No <code>MapView</code> is used in your application.</li>
<li>Only the eHorizon layer is used in your application.
 In these cases, using the eHorizon layer will reduce the required data to download. If the rendering layer is enabled, it will increase the required data to download.</li>
</ul>
</p></li>
</ul>
<p><strong>Important</strong>: If <code>useRenderingLayers</code> is set to <code>false</code> without properly enabling the eHorizon layer,
 it may produce incorrect results. Layer configuration is especially important when prefetching or installing
 region data. Missing data will be downloaded online automatically as needed.
 <p>If your hardware supports pitch and high precision altitude information and you want to use them in the <code>MapMatcher</code>
 to improve map-matching, then enable the <code>LayerConfiguration.Feature.ADAS</code> layer:
 <ol>
<li>Turn on the <code>ADAS</code> layer via <code>LayerConfiguration.enabledFeatures</code> (it will increase data consumption).</li>
<li>If available, set <code>location.pitchInDegrees</code>, <code>location.coordinates.altitude</code> and <code>location.verticalAccuracyInMeters</code>.</li>
<li>In case of issues, please contact your HERE representative.</li>
</ol></p></p></p></p></p></p></p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">MapMatcher</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance of this class.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine)">MapMatcher</a><wbr/>(<a href="sdk-for-android-navigate-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance of this class.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine,boolean)">MapMatcher</a><wbr/>(<a href="sdk-for-android-navigate-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 boolean useRenderingLayers)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance of this class.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-navigation-mapmatchedlocation" title="class in com.here.sdk.navigation">MapMatchedLocation</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#match(com.here.sdk.core.Location)">match</a><wbr/>(<a href="sdk-for-android-navigate-core-location" title="class in com.here.sdk.core">Location</a> location)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">This method computes the map-matched location for the provided input location.</div>
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
<h3>MapMatcher</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MapMatcher</span>()
           throws <span class="exceptions"><a href="sdk-for-android-navigate-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of this class.</p></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine)">
<h3>MapMatcher</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MapMatcher</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</span>
           throws <span class="exceptions"><a href="sdk-for-android-navigate-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of this class.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>A SDKEngine instance.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine,boolean)">
<h3>MapMatcher</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MapMatcher</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 boolean useRenderingLayers)</span>
           throws <span class="exceptions"><a href="sdk-for-android-navigate-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of this class.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>A SDKEngine instance.</p></dd>
<dd><code>useRenderingLayers</code> - <p>When set to true, <code>LayerConfiguration.Feature.RENDERING</code> is used;
     otherwise, <code>LayerConfiguration.Feature.EHORIZON</code> is used to retrieve segment geometry data from the OCM map.
     Note: Ensure the corresponding layer is properly enabled in your <code>LayerConfiguration</code> to avoid incorrect results.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
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
<section class="detail" id="match(com.here.sdk.core.Location)">
<h3>match</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-navigation-mapmatchedlocation" title="class in com.here.sdk.navigation">MapMatchedLocation</a></span> <span class="element-name">match</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-core-location" title="class in com.here.sdk.core">Location</a> location)</span></div>
<div class="block"><p>This method computes the map-matched location for the provided input location.
 <p>Currently, matching is performed within a 50-meter radius of the provided location. If no road network is found
 within that radius, <code>null</code> is returned.
 <p>It's required to set <code>time</code> field for each <code>Location</code> object for the <code>MapMatcher</code> to work properly. In case no time is provided,
 <code>null</code> is returned and an error message is logged. It is used to calculate the distance in time between
 consecutive matches. Together with <code>speed</code>, this allows to calculate how likely a match is consistent with a previous match.
 To improve matching accuracy, it is recommended to provide <code>bearing</code> and <code>speed</code> parameters for each <code>Location</code> object.</p></p></p></div>
<dl class="notes">
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
</main>
</div>
</div>
</body>
</html>

</div>
`
}</HTMLBlock>
