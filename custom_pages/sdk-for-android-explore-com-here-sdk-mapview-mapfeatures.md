---
title: "MapFeatures (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapfeatures"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapFeatures.html -->
<!DOCTYPE HTML>






<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-explore-..-..-..-..-index">Overview</a></li>
<li><a href="sdk-for-android-explore-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-explore-package-tree">Tree</a></li>
<li><a href="sdk-for-android-explore-..-..-..-..-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-explore-..-..-..-..-index-all">Index</a></li>
<li><a href="sdk-for-android-explore-..-..-..-..-help-doc#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li>Nested | </li>
<li><a href="#field-summary">Field</a> | </li>
<li><a href="#constructor-summary">Constr</a> | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li><a href="#field-detail">Field</a> | </li>
<li><a href="#constructor-detail">Constr</a> | </li>
<li>Method</li>
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-package-summary">com.here.sdk.mapview</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.mapview.MapFeatures</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">MapFeatures</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Holds constants for map features, to be used with
 <a href="sdk-for-android-explore-mapscene#enableFeatures(java.util.Map)"><code>MapScene.enableFeatures(java.util.Map&lt;java.lang.String, java.lang.String&gt;)</code></a> and <a href="sdk-for-android-explore-mapscene#disableFeatures(java.util.List)"><code>MapScene.disableFeatures(java.util.List&lt;java.lang.String&gt;)</code></a>.
 </p><p>See <a href="sdk-for-android-explore-mapfeaturemodes" title="class in com.here.sdk.mapview"><code>MapFeatureModes</code></a> for constants representing feature modes.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">

<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#AMBIENT_OCCLUSION">AMBIENT_OCCLUSION</a></code></div>
<div class="col-last even-row-color">
<div class="block">Ambient occlusion effect for 3D geometries (extruded buildings and landmarks).</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#BUILDING_FOOTPRINTS">BUILDING_FOOTPRINTS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The 2D footprint of buildings.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#CONGESTION_ZONES">CONGESTION_ZONES</a></code></div>
<div class="col-last even-row-color">
<div class="block">City areas designated as congestion zones (or congestion charge zones),
 which impose fees on entering such areas.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ENVIRONMENTAL_ZONES">ENVIRONMENTAL_ZONES</a></code></div>
<div class="col-last odd-row-color">
<div class="block">City areas designated as environmental zones, which empose limitations
 on the type of vehicles that are allowed to enter such areas.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#EXTRUDED_BUILDINGS">EXTRUDED_BUILDINGS</a></code></div>
<div class="col-last even-row-color">
<div class="block">Simple 3D representation of buildings.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#LOW_SPEED_ZONES">LOW_SPEED_ZONES</a></code></div>
<div class="col-last odd-row-color">
<div class="block">City areas designated as low speed zones.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#ROAD_EXIT_LABELS">ROAD_EXIT_LABELS</a></code></div>
<div class="col-last even-row-color">
<div class="block">Show or hide road exit labels, if available.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#SHADOWS">SHADOWS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Shadows for all building types (extruded buildings and landmarks).</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TRAFFIC_FLOW">TRAFFIC_FLOW</a></code></div>
<div class="col-last even-row-color">
<div class="block">Traffic flow speed.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#TRAFFIC_INCIDENTS">TRAFFIC_INCIDENTS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Traffic incidents.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#TRAFFIC_LIGHTS">TRAFFIC_LIGHTS</a></code></div>
<div class="col-last even-row-color">
<div class="block">Traffic lights.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">MapFeatures</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="EXTRUDED_BUILDINGS">
<h3>EXTRUDED_BUILDINGS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">EXTRUDED_BUILDINGS</span></div>
<div class="block"><p>Simple 3D representation of buildings.
 </p><p>Supports only one mode: <a href="sdk-for-android-explore-mapfeaturemodes#EXTRUDED_BUILDINGS_ALL"><code>MapFeatureModes.EXTRUDED_BUILDINGS_ALL</code></a>.
 </p><p>Not supported for <a href="sdk-for-android-explore-mapscheme#SATELLITE"><code>MapScheme.SATELLITE</code></a>, <a href="sdk-for-android-explore-mapscheme#ROAD_NETWORK_DAY"><code>MapScheme.ROAD_NETWORK_DAY</code></a>,
 <a href="sdk-for-android-explore-mapscheme#ROAD_NETWORK_NIGHT"><code>MapScheme.ROAD_NETWORK_NIGHT</code></a> and all hybrid schemes: <a href="sdk-for-android-explore-mapscheme#HYBRID_DAY"><code>MapScheme.HYBRID_DAY</code></a>
<a href="sdk-for-android-explore-mapscheme#HYBRID_NIGHT"><code>MapScheme.HYBRID_NIGHT</code></a>, <a href="sdk-for-android-explore-mapscheme#LITE_HYBRID_DAY"><code>MapScheme.LITE_HYBRID_DAY</code></a>
<a href="sdk-for-android-explore-mapscheme#LITE_HYBRID_NIGHT"><code>MapScheme.LITE_HYBRID_NIGHT</code></a>, <a href="sdk-for-android-explore-mapscheme#LOGISTICS_HYBRID_DAY"><code>MapScheme.LOGISTICS_HYBRID_DAY</code></a> and
 <a href="sdk-for-android-explore-mapscheme#LOGISTICS_HYBRID_NIGHT"><code>MapScheme.LOGISTICS_HYBRID_NIGHT</code></a>.
 </p><p>By default, extruded buildings are enabled on all compatible map schemes.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-..-..-..-..-constant-values#com.here.sdk.mapview.MapFeatures.EXTRUDED_BUILDINGS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BUILDING_FOOTPRINTS">
<h3>BUILDING_FOOTPRINTS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BUILDING_FOOTPRINTS</span></div>
<div class="block"><p>The 2D footprint of buildings.
 </p><p>Supports only one mode: <a href="sdk-for-android-explore-mapfeaturemodes#BUILDING_FOOTPRINTS_ALL"><code>MapFeatureModes.BUILDING_FOOTPRINTS_ALL</code></a>.
 </p><p>Not supported for <a href="sdk-for-android-explore-mapscheme#SATELLITE"><code>MapScheme.SATELLITE</code></a>, <a href="sdk-for-android-explore-mapscheme#ROAD_NETWORK_DAY"><code>MapScheme.ROAD_NETWORK_DAY</code></a>,
 <a href="sdk-for-android-explore-mapscheme#ROAD_NETWORK_NIGHT"><code>MapScheme.ROAD_NETWORK_NIGHT</code></a> and all hybrid schemes: <a href="sdk-for-android-explore-mapscheme#HYBRID_DAY"><code>MapScheme.HYBRID_DAY</code></a>
<a href="sdk-for-android-explore-mapscheme#HYBRID_NIGHT"><code>MapScheme.HYBRID_NIGHT</code></a>, <a href="sdk-for-android-explore-mapscheme#LITE_HYBRID_DAY"><code>MapScheme.LITE_HYBRID_DAY</code></a>
<a href="sdk-for-android-explore-mapscheme#LITE_HYBRID_NIGHT"><code>MapScheme.LITE_HYBRID_NIGHT</code></a>, <a href="sdk-for-android-explore-mapscheme#LOGISTICS_HYBRID_DAY"><code>MapScheme.LOGISTICS_HYBRID_DAY</code></a> and
 <a href="sdk-for-android-explore-mapscheme#LOGISTICS_HYBRID_NIGHT"><code>MapScheme.LOGISTICS_HYBRID_NIGHT</code></a>.
 </p><p>By default, building footprints are enabled on all compatible map schemes.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-..-..-..-..-constant-values#com.here.sdk.mapview.MapFeatures.BUILDING_FOOTPRINTS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TRAFFIC_FLOW">
<h3>TRAFFIC_FLOW</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TRAFFIC_FLOW</span></div>
<div class="block"><p>Traffic flow speed. An online connection is required for the traffic
 flow to be shown.
 </p><p>If the offline-mode is enabled for offline maps usage,
 the live traffic flow can still be shown in offline mode by enabling
 pass-through feature for traffic flow on <code>sdk.core.engine.SDKNativeEngine</code>.
 See <code>sdk.core.engine.SDKNativeEngine.pass_through_features</code> for details.
 </p><p>Supported modes:
 <ul>
<li><a href="sdk-for-android-explore-mapfeaturemodes#TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW"><code>MapFeatureModes.TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW</code></a>,</li>
<li><a href="sdk-for-android-explore-mapfeaturemodes#TRAFFIC_FLOW_WITH_FREE_FLOW"><code>MapFeatureModes.TRAFFIC_FLOW_WITH_FREE_FLOW</code></a>,</li>
<li><a href="sdk-for-android-explore-mapfeaturemodes#TRAFFIC_FLOW_WITHOUT_FREE_FLOW"><code>MapFeatureModes.TRAFFIC_FLOW_WITHOUT_FREE_FLOW</code></a>.</li>
</ul>
</p><p>Default mode is <a href="sdk-for-android-explore-mapfeaturemodes#TRAFFIC_FLOW_WITH_FREE_FLOW"><code>MapFeatureModes.TRAFFIC_FLOW_WITH_FREE_FLOW</code></a>.
 </p><p>Not supported for <a href="sdk-for-android-explore-mapscheme#SATELLITE"><code>MapScheme.SATELLITE</code></a>, <a href="sdk-for-android-explore-mapscheme#ROAD_NETWORK_DAY"><code>MapScheme.ROAD_NETWORK_DAY</code></a>
 and <a href="sdk-for-android-explore-mapscheme#ROAD_NETWORK_NIGHT"><code>MapScheme.ROAD_NETWORK_NIGHT</code></a>.
 By default, this map feature is not enabled.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-..-..-..-..-constant-values#com.here.sdk.mapview.MapFeatures.TRAFFIC_FLOW">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TRAFFIC_INCIDENTS">
<h3>TRAFFIC_INCIDENTS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TRAFFIC_INCIDENTS</span></div>
<div class="block"><p>Traffic incidents. An online connection is required for the traffic
 incidents to be shown.
 </p><p>If the offline-mode is enabled for offline maps usage,
 the live traffic incidents can still be shown in offline mode by enabling
 pass-through feature for traffic incidents on <code>sdk.core.engine.SDKNativeEngine</code>.
 See <code>sdk.core.engine.SDKNativeEngine.pass_through_features</code> for details.
 </p><p>Supports only one mode: <a href="sdk-for-android-explore-mapfeaturemodes#TRAFFIC_INCIDENTS_ALL"><code>MapFeatureModes.TRAFFIC_INCIDENTS_ALL</code></a>.
 </p><p>Not supported for <a href="sdk-for-android-explore-mapscheme#SATELLITE"><code>MapScheme.SATELLITE</code></a>, <a href="sdk-for-android-explore-mapscheme#ROAD_NETWORK_DAY"><code>MapScheme.ROAD_NETWORK_DAY</code></a>
 and <a href="sdk-for-android-explore-mapscheme#ROAD_NETWORK_NIGHT"><code>MapScheme.ROAD_NETWORK_NIGHT</code></a>.
 By default, this map feature is not enabled.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-..-..-..-..-constant-values#com.here.sdk.mapview.MapFeatures.TRAFFIC_INCIDENTS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TRAFFIC_LIGHTS">
<h3>TRAFFIC_LIGHTS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TRAFFIC_LIGHTS</span></div>
<div class="block"><p>Traffic lights.
 </p><p>Supports only one mode: <a href="sdk-for-android-explore-mapfeaturemodes#TRAFFIC_LIGHTS_ALL"><code>MapFeatureModes.TRAFFIC_LIGHTS_ALL</code></a>
</p><p>Not supported for <a href="sdk-for-android-explore-mapscheme#SATELLITE"><code>MapScheme.SATELLITE</code></a>, <a href="sdk-for-android-explore-mapscheme#ROAD_NETWORK_DAY"><code>MapScheme.ROAD_NETWORK_DAY</code></a>
 and <a href="sdk-for-android-explore-mapscheme#ROAD_NETWORK_NIGHT"><code>MapScheme.ROAD_NETWORK_NIGHT</code></a>.
 </p><p>By default, traffic lights are enabled on all compatible map schemes.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-..-..-..-..-constant-values#com.here.sdk.mapview.MapFeatures.TRAFFIC_LIGHTS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ENVIRONMENTAL_ZONES">
<h3>ENVIRONMENTAL_ZONES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ENVIRONMENTAL_ZONES</span></div>
<div class="block"><p>City areas designated as environmental zones, which empose limitations
 on the type of vehicles that are allowed to enter such areas.
 </p><p>Supports only one mode: <a href="sdk-for-android-explore-mapfeaturemodes#ENVIRONMENTAL_ZONES_ALL"><code>MapFeatureModes.ENVIRONMENTAL_ZONES_ALL</code></a>.
 </p><p>Not supported for <a href="sdk-for-android-explore-mapscheme#SATELLITE"><code>MapScheme.SATELLITE</code></a>, <a href="sdk-for-android-explore-mapscheme#ROAD_NETWORK_DAY"><code>MapScheme.ROAD_NETWORK_DAY</code></a>
 and <a href="sdk-for-android-explore-mapscheme#ROAD_NETWORK_NIGHT"><code>MapScheme.ROAD_NETWORK_NIGHT</code></a>.
 By default, this map feature is not enabled.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-..-..-..-..-constant-values#com.here.sdk.mapview.MapFeatures.ENVIRONMENTAL_ZONES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CONGESTION_ZONES">
<h3>CONGESTION_ZONES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CONGESTION_ZONES</span></div>
<div class="block"><p>City areas designated as congestion zones (or congestion charge zones),
 which impose fees on entering such areas.
 </p><p>Supports only one mode: <a href="sdk-for-android-explore-mapfeaturemodes#CONGESTION_ZONES_ALL"><code>MapFeatureModes.CONGESTION_ZONES_ALL</code></a>.
 </p><p>Not supported for <a href="sdk-for-android-explore-mapscheme#SATELLITE"><code>MapScheme.SATELLITE</code></a>, <a href="sdk-for-android-explore-mapscheme#ROAD_NETWORK_DAY"><code>MapScheme.ROAD_NETWORK_DAY</code></a>
 and <a href="sdk-for-android-explore-mapscheme#ROAD_NETWORK_NIGHT"><code>MapScheme.ROAD_NETWORK_NIGHT</code></a>.
 By default, this map feature is not enabled.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-..-..-..-..-constant-values#com.here.sdk.mapview.MapFeatures.CONGESTION_ZONES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LOW_SPEED_ZONES">
<h3>LOW_SPEED_ZONES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">LOW_SPEED_ZONES</span></div>
<div class="block"><p>City areas designated as low speed zones.
 Only available when Japan map is used.
 </p><p>Supports only one mode: <a href="sdk-for-android-explore-mapfeaturemodes#LOW_SPEED_ZONES_ALL"><code>MapFeatureModes.LOW_SPEED_ZONES_ALL</code></a>.
 </p><p>Not supported for <a href="sdk-for-android-explore-mapscheme#SATELLITE"><code>MapScheme.SATELLITE</code></a>, <a href="sdk-for-android-explore-mapscheme#ROAD_NETWORK_DAY"><code>MapScheme.ROAD_NETWORK_DAY</code></a>
 and <a href="sdk-for-android-explore-mapscheme#ROAD_NETWORK_NIGHT"><code>MapScheme.ROAD_NETWORK_NIGHT</code></a>.
 By default, this map feature is not enabled.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-..-..-..-..-constant-values#com.here.sdk.mapview.MapFeatures.LOW_SPEED_ZONES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ROAD_EXIT_LABELS">
<h3>ROAD_EXIT_LABELS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ROAD_EXIT_LABELS</span></div>
<div class="block"><p>Show or hide road exit labels, if available.
 </p><p>Supported modes: <a href="sdk-for-android-explore-mapfeaturemodes#ROAD_EXIT_LABELS_NUMBERS_ONLY"><code>MapFeatureModes.ROAD_EXIT_LABELS_NUMBERS_ONLY</code></a>,
 <a href="sdk-for-android-explore-mapfeaturemodes#ROAD_EXIT_LABELS_ALL"><code>MapFeatureModes.ROAD_EXIT_LABELS_ALL</code></a>
</p><p>Default mode is <a href="sdk-for-android-explore-mapfeaturemodes#ROAD_EXIT_LABELS_NUMBERS_ONLY"><code>MapFeatureModes.ROAD_EXIT_LABELS_NUMBERS_ONLY</code></a>.
 </p><p>Road exit labels are enabled by default with <a href="sdk-for-android-explore-mapfeaturemodes#ROAD_EXIT_LABELS_NUMBERS_ONLY"><code>MapFeatureModes.ROAD_EXIT_LABELS_NUMBERS_ONLY</code></a>
 on normal, lite and topo schemes and with <a href="sdk-for-android-explore-mapfeaturemodes#ROAD_EXIT_LABELS_ALL"><code>MapFeatureModes.ROAD_EXIT_LABELS_ALL</code></a> on logistics
 schemes. Note that topo schemes are only available in the HERE SDK Navigate variant.
 </p><p>Not supported for <a href="sdk-for-android-explore-mapscheme#SATELLITE"><code>MapScheme.SATELLITE</code></a>, <a href="sdk-for-android-explore-mapscheme#ROAD_NETWORK_DAY"><code>MapScheme.ROAD_NETWORK_DAY</code></a>
 and <a href="sdk-for-android-explore-mapscheme#ROAD_NETWORK_NIGHT"><code>MapScheme.ROAD_NETWORK_NIGHT</code></a>.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-..-..-..-..-constant-values#com.here.sdk.mapview.MapFeatures.ROAD_EXIT_LABELS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHADOWS">
<h3>SHADOWS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHADOWS</span></div>
<div class="block"><p>Shadows for all building types (extruded buildings and landmarks).
 </p><p>Supports only one mode: <a href="sdk-for-android-explore-mapfeaturemodes#SHADOWS_ALL"><code>MapFeatureModes.SHADOWS_ALL</code></a>.
 </p><p>A <a href="sdk-for-android-explore-shadowquality" title="enum class in com.here.sdk.mapview"><code>ShadowQuality</code></a> must be set on the MapContext through a MapView or the feature has no
 effect.
 </p><p>Shadows have a performance impact and should be considered only for devices with
 sufficient performance.
 </p><p>Not supported for <a href="sdk-for-android-explore-mapscheme#SATELLITE"><code>MapScheme.SATELLITE</code></a>, <a href="sdk-for-android-explore-mapscheme#ROAD_NETWORK_DAY"><code>MapScheme.ROAD_NETWORK_DAY</code></a>,
 <a href="sdk-for-android-explore-mapscheme#ROAD_NETWORK_NIGHT"><code>MapScheme.ROAD_NETWORK_NIGHT</code></a> and all hybrid schemes: <a href="sdk-for-android-explore-mapscheme#HYBRID_DAY"><code>MapScheme.HYBRID_DAY</code></a>
<a href="sdk-for-android-explore-mapscheme#HYBRID_NIGHT"><code>MapScheme.HYBRID_NIGHT</code></a>, <a href="sdk-for-android-explore-mapscheme#LITE_HYBRID_DAY"><code>MapScheme.LITE_HYBRID_DAY</code></a>
<a href="sdk-for-android-explore-mapscheme#LITE_HYBRID_NIGHT"><code>MapScheme.LITE_HYBRID_NIGHT</code></a>, <a href="sdk-for-android-explore-mapscheme#LOGISTICS_HYBRID_DAY"><code>MapScheme.LOGISTICS_HYBRID_DAY</code></a> and
 <a href="sdk-for-android-explore-mapscheme#LOGISTICS_HYBRID_NIGHT"><code>MapScheme.LOGISTICS_HYBRID_NIGHT</code></a>.
 </p><p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.
 By default, this map feature is not enabled.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-..-..-..-..-constant-values#com.here.sdk.mapview.MapFeatures.SHADOWS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="AMBIENT_OCCLUSION">
<h3>AMBIENT_OCCLUSION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">AMBIENT_OCCLUSION</span></div>
<div class="block"><p>Ambient occlusion effect for 3D geometries (extruded buildings and landmarks).
 </p><p>Supports only one mode: <a href="sdk-for-android-explore-mapfeaturemodes#AMBIENT_OCCLUSION_ALL"><code>MapFeatureModes.AMBIENT_OCCLUSION_ALL</code></a>.
 </p><p>This visual effect has a performance impact and should be considered only for devices with
 sufficient performance.
 </p><p>Not supported for <a href="sdk-for-android-explore-mapscheme#SATELLITE"><code>MapScheme.SATELLITE</code></a>, <a href="sdk-for-android-explore-mapscheme#ROAD_NETWORK_DAY"><code>MapScheme.ROAD_NETWORK_DAY</code></a>,
 <a href="sdk-for-android-explore-mapscheme#ROAD_NETWORK_NIGHT"><code>MapScheme.ROAD_NETWORK_NIGHT</code></a> and all hybrid schemes: <a href="sdk-for-android-explore-mapscheme#HYBRID_DAY"><code>MapScheme.HYBRID_DAY</code></a>
<a href="sdk-for-android-explore-mapscheme#HYBRID_NIGHT"><code>MapScheme.HYBRID_NIGHT</code></a>, <a href="sdk-for-android-explore-mapscheme#LITE_HYBRID_DAY"><code>MapScheme.LITE_HYBRID_DAY</code></a>
<a href="sdk-for-android-explore-mapscheme#LITE_HYBRID_NIGHT"><code>MapScheme.LITE_HYBRID_NIGHT</code></a>, <a href="sdk-for-android-explore-mapscheme#LOGISTICS_HYBRID_DAY"><code>MapScheme.LOGISTICS_HYBRID_DAY</code></a> and
 <a href="sdk-for-android-explore-mapscheme#LOGISTICS_HYBRID_NIGHT"><code>MapScheme.LOGISTICS_HYBRID_NIGHT</code></a>.
 </p><p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.
 By default, this map feature is not enabled.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-..-..-..-..-constant-values#com.here.sdk.mapview.MapFeatures.AMBIENT_OCCLUSION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
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
<section class="detail" id="&lt;init&gt;()">
<h3>MapFeatures</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MapFeatures</span>()</div>
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



</div>
`
}</HTMLBlock>
