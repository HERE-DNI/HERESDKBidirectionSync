---
title: "MapFeatures (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapFeatures.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.mapview.MapFeatures</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">MapFeatures</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Holds constants for map features, to be used with
 <a href="sdk-for-android-navigate-mapscene#enableFeatures(java.util.Map)"><code>MapScene.enableFeatures(java.util.Map<java.lang.string, java.lang.string="">)</java.lang.string,></code></a> and <a href="sdk-for-android-navigate-mapscene#disableFeatures(java.util.List)"><code>MapScene.disableFeatures(java.util.List<java.lang.string>)</java.lang.string></code></a>.
 See <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes" title="class in com.here.sdk.mapview"><code>MapFeatureModes</code></a> for constants representing feature modes.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures#AMBIENT_OCCLUSION">AMBIENT_OCCLUSION</a></code></div>
<div className="col-last even-row-color">
<div className="block">Ambient occlusion effect for 3D geometries (extruded buildings and landmarks).</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures#BUILDING_FOOTPRINTS">BUILDING_FOOTPRINTS</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The 2D footprint of buildings.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures#CONGESTION_ZONES">CONGESTION_ZONES</a></code></div>
<div className="col-last even-row-color">
<div className="block">City areas designated as congestion zones (or congestion charge zones),
 which impose fees on entering such areas.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures#CONTOURS">CONTOURS</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Show or hide contour lines on the map to represent elevation changes.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures#ENVIRONMENTAL_ZONES">ENVIRONMENTAL_ZONES</a></code></div>
<div className="col-last even-row-color">
<div className="block">City areas designated as environmental zones, which empose limitations
 on the type of vehicles that are allowed to enter such areas.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures#EXTRUDED_BUILDINGS">EXTRUDED_BUILDINGS</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Simple 3D representation of buildings.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures#LANDMARKS">LANDMARKS</a></code></div>
<div className="col-last even-row-color">
<div className="block">Displays 3D landmarks on the map.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures#LOW_SPEED_ZONES">LOW_SPEED_ZONES</a></code></div>
<div className="col-last odd-row-color">
<div className="block">City areas designated as low speed zones.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures#PUBLIC_TRANSIT">PUBLIC_TRANSIT</a></code></div>
<div className="col-last even-row-color">
<div className="block">Toggles the display of public transit lines for systems like subway, tram, train, monorail,
 and ferry, based on the selected mode.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures#ROAD_EXIT_LABELS">ROAD_EXIT_LABELS</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Show or hide road exit labels, if available.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures#SAFETY_CAMERAS">SAFETY_CAMERAS</a></code></div>
<div className="col-last even-row-color">
<div className="block">Safety and speed cameras.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures#SHADOWS">SHADOWS</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Shadows for all building types (extruded buildings and landmarks).</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures#TERRAIN">TERRAIN</a></code></div>
<div className="col-last even-row-color">
<div className="block">Show elevation topography.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures#TRAFFIC_FLOW">TRAFFIC_FLOW</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Traffic flow speed.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures#TRAFFIC_INCIDENTS">TRAFFIC_INCIDENTS</a></code></div>
<div className="col-last even-row-color">
<div className="block">Traffic incidents.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures#TRAFFIC_LIGHTS">TRAFFIC_LIGHTS</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Traffic lights.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures#TRUCK_PREFERRED_ROADS">TRUCK_PREFERRED_ROADS</a></code></div>
<div className="col-last even-row-color">
<div className="block">Show or hide truck preferred road</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures#VEHICLE_RESTRICTIONS">VEHICLE_RESTRICTIONS</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Vehicle restrictions.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures#%3Cinit%3E()">MapFeatures</a>()</code></div>
<div className="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section className="field-details" id="field-detail">

<ul className="member-list">
<li>
<section className="detail" id="EXTRUDED_BUILDINGS">
<h3>EXTRUDED_BUILDINGS</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">EXTRUDED_BUILDINGS</span></div>
<div className="block"><p>Simple 3D representation of buildings.
 Supports only one mode: <a href="sdk-for-android-navigate-mapfeaturemodes#EXTRUDED_BUILDINGS_ALL"><code>MapFeatureModes.EXTRUDED_BUILDINGS_ALL</code></a>.
 Not supported for <a href="sdk-for-android-navigate-mapscheme#SATELLITE"><code>MapScheme.SATELLITE</code></a>, <a href="sdk-for-android-navigate-mapscheme#ROAD_NETWORK_DAY"><code>MapScheme.ROAD_NETWORK_DAY</code></a>,
 <a href="sdk-for-android-navigate-mapscheme#ROAD_NETWORK_NIGHT"><code>MapScheme.ROAD_NETWORK_NIGHT</code></a> and all hybrid schemes: <a href="sdk-for-android-navigate-mapscheme#HYBRID_DAY"><code>MapScheme.HYBRID_DAY</code></a>
<a href="sdk-for-android-navigate-mapscheme#HYBRID_NIGHT"><code>MapScheme.HYBRID_NIGHT</code></a>, <a href="sdk-for-android-navigate-mapscheme#LITE_HYBRID_DAY"><code>MapScheme.LITE_HYBRID_DAY</code></a>
<a href="sdk-for-android-navigate-mapscheme#LITE_HYBRID_NIGHT"><code>MapScheme.LITE_HYBRID_NIGHT</code></a>, <a href="sdk-for-android-navigate-mapscheme#LOGISTICS_HYBRID_DAY"><code>MapScheme.LOGISTICS_HYBRID_DAY</code></a> and
 <a href="sdk-for-android-navigate-mapscheme#LOGISTICS_HYBRID_NIGHT"><code>MapScheme.LOGISTICS_HYBRID_NIGHT</code></a>.
 By default, extruded buildings are enabled on all compatible map schemes.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatures.EXTRUDED_BUILDINGS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="BUILDING_FOOTPRINTS">
<h3>BUILDING_FOOTPRINTS</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">BUILDING_FOOTPRINTS</span></div>
<div className="block"><p>The 2D footprint of buildings.
 Supports only one mode: <a href="sdk-for-android-navigate-mapfeaturemodes#BUILDING_FOOTPRINTS_ALL"><code>MapFeatureModes.BUILDING_FOOTPRINTS_ALL</code></a>.
 Not supported for <a href="sdk-for-android-navigate-mapscheme#SATELLITE"><code>MapScheme.SATELLITE</code></a>, <a href="sdk-for-android-navigate-mapscheme#ROAD_NETWORK_DAY"><code>MapScheme.ROAD_NETWORK_DAY</code></a>,
 <a href="sdk-for-android-navigate-mapscheme#ROAD_NETWORK_NIGHT"><code>MapScheme.ROAD_NETWORK_NIGHT</code></a> and all hybrid schemes: <a href="sdk-for-android-navigate-mapscheme#HYBRID_DAY"><code>MapScheme.HYBRID_DAY</code></a>
<a href="sdk-for-android-navigate-mapscheme#HYBRID_NIGHT"><code>MapScheme.HYBRID_NIGHT</code></a>, <a href="sdk-for-android-navigate-mapscheme#LITE_HYBRID_DAY"><code>MapScheme.LITE_HYBRID_DAY</code></a>
<a href="sdk-for-android-navigate-mapscheme#LITE_HYBRID_NIGHT"><code>MapScheme.LITE_HYBRID_NIGHT</code></a>, <a href="sdk-for-android-navigate-mapscheme#LOGISTICS_HYBRID_DAY"><code>MapScheme.LOGISTICS_HYBRID_DAY</code></a> and
 <a href="sdk-for-android-navigate-mapscheme#LOGISTICS_HYBRID_NIGHT"><code>MapScheme.LOGISTICS_HYBRID_NIGHT</code></a>.
 By default, building footprints are enabled on all compatible map schemes.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatures.BUILDING_FOOTPRINTS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="TRAFFIC_FLOW">
<h3>TRAFFIC_FLOW</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">TRAFFIC_FLOW</span></div>
<div className="block"><p>Traffic flow speed. An online connection is required for the traffic
 flow to be shown.
 If the offline-mode is enabled for offline maps usage,
 the live traffic flow can still be shown in offline mode by enabling
 pass-through feature for traffic flow on <code>sdk.core.engine.SDKNativeEngine</code>.
 See <code>sdk.core.engine.SDKNativeEngine.pass_through_features</code> for details.
 Supported modes:
 <ul>
<li><a href="sdk-for-android-navigate-mapfeaturemodes#TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW"><code>MapFeatureModes.TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW</code></a>,</li>
<li><a href="sdk-for-android-navigate-mapfeaturemodes#TRAFFIC_FLOW_WITH_FREE_FLOW"><code>MapFeatureModes.TRAFFIC_FLOW_WITH_FREE_FLOW</code></a>,</li>
<li><a href="sdk-for-android-navigate-mapfeaturemodes#TRAFFIC_FLOW_WITHOUT_FREE_FLOW"><code>MapFeatureModes.TRAFFIC_FLOW_WITHOUT_FREE_FLOW</code></a>.</li>
</ul>
Default mode is <a href="sdk-for-android-navigate-mapfeaturemodes#TRAFFIC_FLOW_WITH_FREE_FLOW"><code>MapFeatureModes.TRAFFIC_FLOW_WITH_FREE_FLOW</code></a>.
 Not supported for <a href="sdk-for-android-navigate-mapscheme#SATELLITE"><code>MapScheme.SATELLITE</code></a>, <a href="sdk-for-android-navigate-mapscheme#ROAD_NETWORK_DAY"><code>MapScheme.ROAD_NETWORK_DAY</code></a>
 and <a href="sdk-for-android-navigate-mapscheme#ROAD_NETWORK_NIGHT"><code>MapScheme.ROAD_NETWORK_NIGHT</code></a>.
 By default, this map feature is not enabled.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatures.TRAFFIC_FLOW">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="TRAFFIC_INCIDENTS">
<h3>TRAFFIC_INCIDENTS</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">TRAFFIC_INCIDENTS</span></div>
<div className="block"><p>Traffic incidents. An online connection is required for the traffic
 incidents to be shown.
 If the offline-mode is enabled for offline maps usage,
 the live traffic incidents can still be shown in offline mode by enabling
 pass-through feature for traffic incidents on <code>sdk.core.engine.SDKNativeEngine</code>.
 See <code>sdk.core.engine.SDKNativeEngine.pass_through_features</code> for details.
 Supports only one mode: <a href="sdk-for-android-navigate-mapfeaturemodes#TRAFFIC_INCIDENTS_ALL"><code>MapFeatureModes.TRAFFIC_INCIDENTS_ALL</code></a>.
 Not supported for <a href="sdk-for-android-navigate-mapscheme#SATELLITE"><code>MapScheme.SATELLITE</code></a>, <a href="sdk-for-android-navigate-mapscheme#ROAD_NETWORK_DAY"><code>MapScheme.ROAD_NETWORK_DAY</code></a>
 and <a href="sdk-for-android-navigate-mapscheme#ROAD_NETWORK_NIGHT"><code>MapScheme.ROAD_NETWORK_NIGHT</code></a>.
 By default, this map feature is not enabled.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatures.TRAFFIC_INCIDENTS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="TRAFFIC_LIGHTS">
<h3>TRAFFIC_LIGHTS</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">TRAFFIC_LIGHTS</span></div>
<div className="block"><p>Traffic lights.
 Supports only one mode: <a href="sdk-for-android-navigate-mapfeaturemodes#TRAFFIC_LIGHTS_ALL"><code>MapFeatureModes.TRAFFIC_LIGHTS_ALL</code></a>
Not supported for <a href="sdk-for-android-navigate-mapscheme#SATELLITE"><code>MapScheme.SATELLITE</code></a>, <a href="sdk-for-android-navigate-mapscheme#ROAD_NETWORK_DAY"><code>MapScheme.ROAD_NETWORK_DAY</code></a>
 and <a href="sdk-for-android-navigate-mapscheme#ROAD_NETWORK_NIGHT"><code>MapScheme.ROAD_NETWORK_NIGHT</code></a>.
 By default, traffic lights are enabled on all compatible map schemes.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatures.TRAFFIC_LIGHTS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="VEHICLE_RESTRICTIONS">
<h3>VEHICLE_RESTRICTIONS</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">VEHICLE_RESTRICTIONS</span></div>
<div className="block"><p>Vehicle restrictions. Requires map version 25 as minimum. If old map
 data is stored on disk, it might require updating using <code>MapUpdater</code>.
 Supported modes: <a href="sdk-for-android-navigate-mapfeaturemodes#VEHICLE_RESTRICTIONS_ACTIVE"><code>MapFeatureModes.VEHICLE_RESTRICTIONS_ACTIVE</code></a>,
 <a href="sdk-for-android-navigate-mapfeaturemodes#VEHICLE_RESTRICTIONS_ACTIVE_AND_INACTIVE"><code>MapFeatureModes.VEHICLE_RESTRICTIONS_ACTIVE_AND_INACTIVE</code></a> and
 <a href="sdk-for-android-navigate-mapfeaturemodes#VEHICLE_RESTRICTIONS_ACTIVE_AND_INACTIVE_DIFFERENTIATED"><code>MapFeatureModes.VEHICLE_RESTRICTIONS_ACTIVE_AND_INACTIVE_DIFFERENTIATED</code></a>.
 Default mode when enabled is
 <a href="sdk-for-android-navigate-mapfeaturemodes#VEHICLE_RESTRICTIONS_ACTIVE_AND_INACTIVE"><code>MapFeatureModes.VEHICLE_RESTRICTIONS_ACTIVE_AND_INACTIVE</code></a>.
 Not supported for <a href="sdk-for-android-navigate-mapscheme#SATELLITE"><code>MapScheme.SATELLITE</code></a>, <a href="sdk-for-android-navigate-mapscheme#ROAD_NETWORK_DAY"><code>MapScheme.ROAD_NETWORK_DAY</code></a>
 and <a href="sdk-for-android-navigate-mapscheme#ROAD_NETWORK_NIGHT"><code>MapScheme.ROAD_NETWORK_NIGHT</code></a>.
 By default, this map feature is not enabled.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatures.VEHICLE_RESTRICTIONS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="SAFETY_CAMERAS">
<h3>SAFETY_CAMERAS</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">SAFETY_CAMERAS</span></div>
<div className="block"><p>Safety and speed cameras.
 Supports only one mode: <a href="sdk-for-android-navigate-mapfeaturemodes#SAFETY_CAMERAS_ALL"><code>MapFeatureModes.SAFETY_CAMERAS_ALL</code></a>.
 Not supported for <a href="sdk-for-android-navigate-mapscheme#SATELLITE"><code>MapScheme.SATELLITE</code></a>, <a href="sdk-for-android-navigate-mapscheme#ROAD_NETWORK_DAY"><code>MapScheme.ROAD_NETWORK_DAY</code></a>
 and <a href="sdk-for-android-navigate-mapscheme#ROAD_NETWORK_NIGHT"><code>MapScheme.ROAD_NETWORK_NIGHT</code></a>.
 By default, this map feature is not enabled.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatures.SAFETY_CAMERAS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="LANDMARKS">
<h3>LANDMARKS</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">LANDMARKS</span></div>
<div className="block"><p>Displays 3D landmarks on the map.
 Please note: Enabling 3D landmarks with 3D terrain may result in instances where
 landmarks sink into or float above the terrain.
 Supported modes: <a href="sdk-for-android-navigate-mapfeaturemodes#LANDMARKS_TEXTURED"><code>MapFeatureModes.LANDMARKS_TEXTURED</code></a>,
 <a href="sdk-for-android-navigate-mapfeaturemodes#LANDMARKS_GRAYSCALE"><code>MapFeatureModes.LANDMARKS_GRAYSCALE</code></a> and <a href="sdk-for-android-navigate-mapfeaturemodes#LANDMARKS_TEXTURELESS"><code>MapFeatureModes.LANDMARKS_TEXTURELESS</code></a>.
 Default mode is <a href="sdk-for-android-navigate-mapfeaturemodes#LANDMARKS_GRAYSCALE"><code>MapFeatureModes.LANDMARKS_GRAYSCALE</code></a>.
 By default, 3D landmarks are enabled on all compatible map schemes.
 Not supported for <a href="sdk-for-android-navigate-mapscheme#SATELLITE"><code>MapScheme.SATELLITE</code></a>, <a href="sdk-for-android-navigate-mapscheme#ROAD_NETWORK_DAY"><code>MapScheme.ROAD_NETWORK_DAY</code></a>,
 <a href="sdk-for-android-navigate-mapscheme#ROAD_NETWORK_NIGHT"><code>MapScheme.ROAD_NETWORK_NIGHT</code></a> and all hybrid schemes: <a href="sdk-for-android-navigate-mapscheme#HYBRID_DAY"><code>MapScheme.HYBRID_DAY</code></a>
<a href="sdk-for-android-navigate-mapscheme#HYBRID_NIGHT"><code>MapScheme.HYBRID_NIGHT</code></a>, <a href="sdk-for-android-navigate-mapscheme#LITE_HYBRID_DAY"><code>MapScheme.LITE_HYBRID_DAY</code></a>
<a href="sdk-for-android-navigate-mapscheme#LITE_HYBRID_NIGHT"><code>MapScheme.LITE_HYBRID_NIGHT</code></a>, <a href="sdk-for-android-navigate-mapscheme#LOGISTICS_HYBRID_DAY"><code>MapScheme.LOGISTICS_HYBRID_DAY</code></a> and
 <a href="sdk-for-android-navigate-mapscheme#LOGISTICS_HYBRID_NIGHT"><code>MapScheme.LOGISTICS_HYBRID_NIGHT</code></a>.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatures.LANDMARKS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="ENVIRONMENTAL_ZONES">
<h3>ENVIRONMENTAL_ZONES</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">ENVIRONMENTAL_ZONES</span></div>
<div className="block"><p>City areas designated as environmental zones, which empose limitations
 on the type of vehicles that are allowed to enter such areas.
 Supports only one mode: <a href="sdk-for-android-navigate-mapfeaturemodes#ENVIRONMENTAL_ZONES_ALL"><code>MapFeatureModes.ENVIRONMENTAL_ZONES_ALL</code></a>.
 Not supported for <a href="sdk-for-android-navigate-mapscheme#SATELLITE"><code>MapScheme.SATELLITE</code></a>, <a href="sdk-for-android-navigate-mapscheme#ROAD_NETWORK_DAY"><code>MapScheme.ROAD_NETWORK_DAY</code></a>
 and <a href="sdk-for-android-navigate-mapscheme#ROAD_NETWORK_NIGHT"><code>MapScheme.ROAD_NETWORK_NIGHT</code></a>.
 By default, this map feature is not enabled.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatures.ENVIRONMENTAL_ZONES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="CONGESTION_ZONES">
<h3>CONGESTION_ZONES</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">CONGESTION_ZONES</span></div>
<div className="block"><p>City areas designated as congestion zones (or congestion charge zones),
 which impose fees on entering such areas.
 Supports only one mode: <a href="sdk-for-android-navigate-mapfeaturemodes#CONGESTION_ZONES_ALL"><code>MapFeatureModes.CONGESTION_ZONES_ALL</code></a>.
 Not supported for <a href="sdk-for-android-navigate-mapscheme#SATELLITE"><code>MapScheme.SATELLITE</code></a>, <a href="sdk-for-android-navigate-mapscheme#ROAD_NETWORK_DAY"><code>MapScheme.ROAD_NETWORK_DAY</code></a>
 and <a href="sdk-for-android-navigate-mapscheme#ROAD_NETWORK_NIGHT"><code>MapScheme.ROAD_NETWORK_NIGHT</code></a>.
 By default, this map feature is not enabled.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatures.CONGESTION_ZONES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="LOW_SPEED_ZONES">
<h3>LOW_SPEED_ZONES</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">LOW_SPEED_ZONES</span></div>
<div className="block"><p>City areas designated as low speed zones.
 Only available when Japan map is used.
 Supports only one mode: <a href="sdk-for-android-navigate-mapfeaturemodes#LOW_SPEED_ZONES_ALL"><code>MapFeatureModes.LOW_SPEED_ZONES_ALL</code></a>.
 Not supported for <a href="sdk-for-android-navigate-mapscheme#SATELLITE"><code>MapScheme.SATELLITE</code></a>, <a href="sdk-for-android-navigate-mapscheme#ROAD_NETWORK_DAY"><code>MapScheme.ROAD_NETWORK_DAY</code></a>
 and <a href="sdk-for-android-navigate-mapscheme#ROAD_NETWORK_NIGHT"><code>MapScheme.ROAD_NETWORK_NIGHT</code></a>.
 By default, this map feature is not enabled.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatures.LOW_SPEED_ZONES">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="TERRAIN">
<h3>TERRAIN</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">TERRAIN</span></div>
<div className="block"><p>Show elevation topography.
 Supported modes: <a href="sdk-for-android-navigate-mapfeaturemodes#TERRAIN_HILLSHADE"><code>MapFeatureModes.TERRAIN_HILLSHADE</code></a>, <a href="sdk-for-android-navigate-mapfeaturemodes#TERRAIN_3D"><code>MapFeatureModes.TERRAIN_3D</code></a>.
 <a href="sdk-for-android-navigate-mapfeaturemodes#TERRAIN_HILLSHADE"><code>MapFeatureModes.TERRAIN_HILLSHADE</code></a> is only supported for schemes <a href="sdk-for-android-navigate-mapscheme#NORMAL_DAY"><code>MapScheme.NORMAL_DAY</code></a>,
 <a href="sdk-for-android-navigate-mapscheme#NORMAL_NIGHT"><code>MapScheme.NORMAL_NIGHT</code></a>, <a href="sdk-for-android-navigate-mapscheme#LITE_DAY"><code>MapScheme.LITE_DAY</code></a>, <a href="sdk-for-android-navigate-mapscheme#LITE_NIGHT"><code>MapScheme.LITE_NIGHT</code></a>,
 <a href="sdk-for-android-navigate-mapscheme#LOGISTICS_DAY"><code>MapScheme.LOGISTICS_DAY</code></a> and <a href="sdk-for-android-navigate-mapscheme#LOGISTICS_NIGHT"><code>MapScheme.LOGISTICS_NIGHT</code></a>, <a href="sdk-for-android-navigate-mapscheme#TOPO_DAY"><code>MapScheme.TOPO_DAY</code></a> and
 <a href="sdk-for-android-navigate-mapscheme#TOPO_NIGHT"><code>MapScheme.TOPO_NIGHT</code></a>.
 Default mode is <a href="sdk-for-android-navigate-mapfeaturemodes#TERRAIN_HILLSHADE"><code>MapFeatureModes.TERRAIN_HILLSHADE</code></a> for the supporting schemes.
 By default, terrain is disabled, except for <a href="sdk-for-android-navigate-mapscheme#TOPO_DAY"><code>MapScheme.TOPO_DAY</code></a> and <a href="sdk-for-android-navigate-mapscheme#TOPO_NIGHT"><code>MapScheme.TOPO_NIGHT</code></a>.
 Note that this feature has performance implications, with extra data use and impact on
 frame rate.
 If performance is a concern, this feature can be disabled from the application side when
 loading the map scene.
 Not supported for <a href="sdk-for-android-navigate-mapscheme#SATELLITE"><code>MapScheme.SATELLITE</code></a>, <a href="sdk-for-android-navigate-mapscheme#ROAD_NETWORK_DAY"><code>MapScheme.ROAD_NETWORK_DAY</code></a>
 and <a href="sdk-for-android-navigate-mapscheme#ROAD_NETWORK_NIGHT"><code>MapScheme.ROAD_NETWORK_NIGHT</code></a>.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatures.TERRAIN">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="PUBLIC_TRANSIT">
<h3>PUBLIC_TRANSIT</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">PUBLIC_TRANSIT</span></div>
<div className="block"><p>Toggles the display of public transit lines for systems like subway, tram, train, monorail,
 and ferry, based on the selected mode.
 Supported modes: <a href="sdk-for-android-navigate-mapfeaturemodes#PUBLIC_TRANSIT_ALL"><code>MapFeatureModes.PUBLIC_TRANSIT_ALL</code></a>, <a href="sdk-for-android-navigate-mapfeaturemodes#PUBLIC_TRANSIT_ASIA"><code>MapFeatureModes.PUBLIC_TRANSIT_ASIA</code></a>.
 <a href="sdk-for-android-navigate-mapfeaturemodes#PUBLIC_TRANSIT_ASIA"><code>MapFeatureModes.PUBLIC_TRANSIT_ASIA</code></a> is supported only when credentials enabled for the
 enriched Japan map are used.
 Public transit is disabled by default for all map
 schemes when using Rest-of-World map data. When using enriched Japan map
 data, public transit is enabled by default with
 <a href="sdk-for-android-navigate-mapfeaturemodes#PUBLIC_TRANSIT_ASIA"><code>MapFeatureModes.PUBLIC_TRANSIT_ASIA</code></a> on normal, lite and topo schemes
 (including their hybrid variants) and disabled by default on logistics
 schemes.
 Not supported for <a href="sdk-for-android-navigate-mapscheme#SATELLITE"><code>MapScheme.SATELLITE</code></a>, <a href="sdk-for-android-navigate-mapscheme#ROAD_NETWORK_DAY"><code>MapScheme.ROAD_NETWORK_DAY</code></a>
 and <a href="sdk-for-android-navigate-mapscheme#ROAD_NETWORK_NIGHT"><code>MapScheme.ROAD_NETWORK_NIGHT</code></a>.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatures.PUBLIC_TRANSIT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="ROAD_EXIT_LABELS">
<h3>ROAD_EXIT_LABELS</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">ROAD_EXIT_LABELS</span></div>
<div className="block"><p>Show or hide road exit labels, if available.
 Supported modes: <a href="sdk-for-android-navigate-mapfeaturemodes#ROAD_EXIT_LABELS_NUMBERS_ONLY"><code>MapFeatureModes.ROAD_EXIT_LABELS_NUMBERS_ONLY</code></a>,
 <a href="sdk-for-android-navigate-mapfeaturemodes#ROAD_EXIT_LABELS_ALL"><code>MapFeatureModes.ROAD_EXIT_LABELS_ALL</code></a>
Default mode is <a href="sdk-for-android-navigate-mapfeaturemodes#ROAD_EXIT_LABELS_NUMBERS_ONLY"><code>MapFeatureModes.ROAD_EXIT_LABELS_NUMBERS_ONLY</code></a>.
 Road exit labels are enabled by default with <a href="sdk-for-android-navigate-mapfeaturemodes#ROAD_EXIT_LABELS_NUMBERS_ONLY"><code>MapFeatureModes.ROAD_EXIT_LABELS_NUMBERS_ONLY</code></a>
 on normal, lite and topo schemes and with <a href="sdk-for-android-navigate-mapfeaturemodes#ROAD_EXIT_LABELS_ALL"><code>MapFeatureModes.ROAD_EXIT_LABELS_ALL</code></a> on logistics
 schemes. Note that topo schemes are only available in the HERE SDK Navigate variant.
 Not supported for <a href="sdk-for-android-navigate-mapscheme#SATELLITE"><code>MapScheme.SATELLITE</code></a>, <a href="sdk-for-android-navigate-mapscheme#ROAD_NETWORK_DAY"><code>MapScheme.ROAD_NETWORK_DAY</code></a>
 and <a href="sdk-for-android-navigate-mapscheme#ROAD_NETWORK_NIGHT"><code>MapScheme.ROAD_NETWORK_NIGHT</code></a>.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatures.ROAD_EXIT_LABELS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="SHADOWS">
<h3>SHADOWS</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">SHADOWS</span></div>
<div className="block"><p>Shadows for all building types (extruded buildings and landmarks).
 Supports only one mode: <a href="sdk-for-android-navigate-mapfeaturemodes#SHADOWS_ALL"><code>MapFeatureModes.SHADOWS_ALL</code></a>.
 A <a href="sdk-for-android-navigate-com-here-sdk-mapview-shadowquality" title="enum class in com.here.sdk.mapview"><code>ShadowQuality</code></a> must be set on the MapContext through a MapView or the feature has no
 effect.
 Shadows have a performance impact and should be considered only for devices with
 sufficient performance.
 Not supported for <a href="sdk-for-android-navigate-mapscheme#SATELLITE"><code>MapScheme.SATELLITE</code></a>, <a href="sdk-for-android-navigate-mapscheme#ROAD_NETWORK_DAY"><code>MapScheme.ROAD_NETWORK_DAY</code></a>,
 <a href="sdk-for-android-navigate-mapscheme#ROAD_NETWORK_NIGHT"><code>MapScheme.ROAD_NETWORK_NIGHT</code></a> and all hybrid schemes: <a href="sdk-for-android-navigate-mapscheme#HYBRID_DAY"><code>MapScheme.HYBRID_DAY</code></a>
<a href="sdk-for-android-navigate-mapscheme#HYBRID_NIGHT"><code>MapScheme.HYBRID_NIGHT</code></a>, <a href="sdk-for-android-navigate-mapscheme#LITE_HYBRID_DAY"><code>MapScheme.LITE_HYBRID_DAY</code></a>
<a href="sdk-for-android-navigate-mapscheme#LITE_HYBRID_NIGHT"><code>MapScheme.LITE_HYBRID_NIGHT</code></a>, <a href="sdk-for-android-navigate-mapscheme#LOGISTICS_HYBRID_DAY"><code>MapScheme.LOGISTICS_HYBRID_DAY</code></a> and
 <a href="sdk-for-android-navigate-mapscheme#LOGISTICS_HYBRID_NIGHT"><code>MapScheme.LOGISTICS_HYBRID_NIGHT</code></a>.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.
 By default, this map feature is not enabled.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatures.SHADOWS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="AMBIENT_OCCLUSION">
<h3>AMBIENT_OCCLUSION</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">AMBIENT_OCCLUSION</span></div>
<div className="block"><p>Ambient occlusion effect for 3D geometries (extruded buildings and landmarks).
 Supports only one mode: <a href="sdk-for-android-navigate-mapfeaturemodes#AMBIENT_OCCLUSION_ALL"><code>MapFeatureModes.AMBIENT_OCCLUSION_ALL</code></a>.
 This visual effect has a performance impact and should be considered only for devices with
 sufficient performance.
 Not supported for <a href="sdk-for-android-navigate-mapscheme#SATELLITE"><code>MapScheme.SATELLITE</code></a>, <a href="sdk-for-android-navigate-mapscheme#ROAD_NETWORK_DAY"><code>MapScheme.ROAD_NETWORK_DAY</code></a>,
 <a href="sdk-for-android-navigate-mapscheme#ROAD_NETWORK_NIGHT"><code>MapScheme.ROAD_NETWORK_NIGHT</code></a> and all hybrid schemes: <a href="sdk-for-android-navigate-mapscheme#HYBRID_DAY"><code>MapScheme.HYBRID_DAY</code></a>
<a href="sdk-for-android-navigate-mapscheme#HYBRID_NIGHT"><code>MapScheme.HYBRID_NIGHT</code></a>, <a href="sdk-for-android-navigate-mapscheme#LITE_HYBRID_DAY"><code>MapScheme.LITE_HYBRID_DAY</code></a>
<a href="sdk-for-android-navigate-mapscheme#LITE_HYBRID_NIGHT"><code>MapScheme.LITE_HYBRID_NIGHT</code></a>, <a href="sdk-for-android-navigate-mapscheme#LOGISTICS_HYBRID_DAY"><code>MapScheme.LOGISTICS_HYBRID_DAY</code></a> and
 <a href="sdk-for-android-navigate-mapscheme#LOGISTICS_HYBRID_NIGHT"><code>MapScheme.LOGISTICS_HYBRID_NIGHT</code></a>.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.
 By default, this map feature is not enabled.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatures.AMBIENT_OCCLUSION">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="CONTOURS">
<h3>CONTOURS</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">CONTOURS</span></div>
<div className="block"><p>Show or hide contour lines on the map to represent elevation changes.
 Supports only one mode: <a href="sdk-for-android-navigate-mapfeaturemodes#CONTOURS_ALL"><code>MapFeatureModes.CONTOURS_ALL</code></a>
Not supported for <a href="sdk-for-android-navigate-mapscheme#SATELLITE"><code>MapScheme.SATELLITE</code></a>, <a href="sdk-for-android-navigate-mapscheme#ROAD_NETWORK_DAY"><code>MapScheme.ROAD_NETWORK_DAY</code></a>,
 <a href="sdk-for-android-navigate-mapscheme#ROAD_NETWORK_NIGHT"><code>MapScheme.ROAD_NETWORK_NIGHT</code></a> and all hybrid schemes: <a href="sdk-for-android-navigate-mapscheme#HYBRID_DAY"><code>MapScheme.HYBRID_DAY</code></a>
<a href="sdk-for-android-navigate-mapscheme#HYBRID_NIGHT"><code>MapScheme.HYBRID_NIGHT</code></a>, <a href="sdk-for-android-navigate-mapscheme#LITE_HYBRID_DAY"><code>MapScheme.LITE_HYBRID_DAY</code></a>
<a href="sdk-for-android-navigate-mapscheme#LITE_HYBRID_NIGHT"><code>MapScheme.LITE_HYBRID_NIGHT</code></a>, <a href="sdk-for-android-navigate-mapscheme#LOGISTICS_HYBRID_DAY"><code>MapScheme.LOGISTICS_HYBRID_DAY</code></a> and
 <a href="sdk-for-android-navigate-mapscheme#LOGISTICS_HYBRID_NIGHT"><code>MapScheme.LOGISTICS_HYBRID_NIGHT</code></a>.
 Contours are enabled by default on topo schemes and disabled by default on other schemes.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatures.CONTOURS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="TRUCK_PREFERRED_ROADS">
<h3>TRUCK_PREFERRED_ROADS</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">TRUCK_PREFERRED_ROADS</span></div>
<div className="block"><p>Show or hide truck preferred road
 Supported modes: <a href="sdk-for-android-navigate-mapfeaturemodes#TRUCK_PREFERRED_ROADS_ALL"><code>MapFeatureModes.TRUCK_PREFERRED_ROADS_ALL</code></a>
Not supported for <a href="sdk-for-android-navigate-mapscheme#SATELLITE"><code>MapScheme.SATELLITE</code></a>, <a href="sdk-for-android-navigate-mapscheme#ROAD_NETWORK_DAY"><code>MapScheme.ROAD_NETWORK_DAY</code></a>
 and <a href="sdk-for-android-navigate-mapscheme#ROAD_NETWORK_NIGHT"><code>MapScheme.ROAD_NETWORK_NIGHT</code></a>.
 By default, this map feature is not enabled.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatures.TRUCK_PREFERRED_ROADS">Constant Field Values</a></li>
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
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;()">
<h3>MapFeatures</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">MapFeatures</span>()</div>
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
