---
title: "MapFeatureModes (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapFeatureModes.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.mapview.MapFeatureModes</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">MapFeatureModes</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Holds constants for map feature modes, to be used with <a href="sdk-for-android-explore-mapscene#enableFeatures(java.util.Map)"><code>MapScene.enableFeatures(java.util.Map&lt;java.lang.String, java.lang.String&gt;)</code></a>.
 Use <a href="sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes#DEFAULT"><code>DEFAULT</code></a> to enable a feature with its default mode.
 Note: The default mode is defined by the currently loaded map scene configuration and
 may vary per <a href="sdk-for-android-explore-mapscheme" title="enum class in com.here.sdk.mapview"><code>MapScheme</code></a>. The currently active features and modes can be inspected
 using <a href="sdk-for-android-explore-mapscene#getActiveFeatures()"><code>MapScene.getActiveFeatures()</code></a> after the scene is loaded.
 See <a href="sdk-for-android-explore-mapfeatures" title="class in com.here.sdk.mapview"><code>MapFeatures</code></a> for constants representing the feature names.</p></div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes#AMBIENT_OCCLUSION_ALL">AMBIENT_OCCLUSION_ALL</a></code></div>
<div class="col-last even-row-color">
<div class="block">Ambient occlusion effect is shown for extruded buildings and landmarks.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes#BUILDING_FOOTPRINTS_ALL">BUILDING_FOOTPRINTS_ALL</a></code></div>
<div class="col-last odd-row-color">
<div class="block">All building footprints are shown.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes#CONGESTION_ZONES_ALL">CONGESTION_ZONES_ALL</a></code></div>
<div class="col-last even-row-color">
<div class="block">All congestion zones are shown.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes#DEFAULT">DEFAULT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Enables the default mode of a map feature.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes#ENVIRONMENTAL_ZONES_ALL">ENVIRONMENTAL_ZONES_ALL</a></code></div>
<div class="col-last even-row-color">
<div class="block">All environmental zones are shown.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes#EXTRUDED_BUILDINGS_ALL">EXTRUDED_BUILDINGS_ALL</a></code></div>
<div class="col-last odd-row-color">
<div class="block">All extruded buildings are shown.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes#LOW_SPEED_ZONES_ALL">LOW_SPEED_ZONES_ALL</a></code></div>
<div class="col-last even-row-color">
<div class="block">All low speed zones are shown.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes#ROAD_EXIT_LABELS_ALL">ROAD_EXIT_LABELS_ALL</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Road exit labels are shown with numbers and names, if available.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes#ROAD_EXIT_LABELS_NUMBERS_ONLY">ROAD_EXIT_LABELS_NUMBERS_ONLY</a></code></div>
<div class="col-last even-row-color">
<div class="block">Road exit labels are shown with numbers, if available.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes#SHADOWS_ALL">SHADOWS_ALL</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Shadows are shown for extruded buildings and landmarks.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes#TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW">TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW</a></code></div>
<div class="col-last even-row-color">
<div class="block">Only available when Japan map is used.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes#TRAFFIC_FLOW_WITH_FREE_FLOW">TRAFFIC_FLOW_WITH_FREE_FLOW</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Traffic flow shows green lines when there is no traffic congestion.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes#TRAFFIC_FLOW_WITHOUT_FREE_FLOW">TRAFFIC_FLOW_WITHOUT_FREE_FLOW</a></code></div>
<div class="col-last even-row-color">
<div class="block">Traffic flow does not show green lines when there is no traffic congestion.</div>
</div>
<div class="col-first odd-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes#TRAFFIC_INCIDENTS_ALL">TRAFFIC_INCIDENTS_ALL</a></code></div>
<div class="col-last odd-row-color">
<div class="block">All available traffic incidents are shown.</div>
</div>
<div class="col-first even-row-color"><code>static final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes#TRAFFIC_LIGHTS_ALL">TRAFFIC_LIGHTS_ALL</a></code></div>
<div class="col-last even-row-color">
<div class="block">All available traffic lights are shown.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes#%3Cinit%3E()">MapFeatureModes</a>()</code></div>

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
<section class="detail" id="DEFAULT">
<h3>DEFAULT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">DEFAULT</span></div>
<div class="block"><p>Enables the default mode of a map feature. Can be used with any map feature.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapFeatureModes.DEFAULT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="BUILDING_FOOTPRINTS_ALL">
<h3>BUILDING_FOOTPRINTS_ALL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">BUILDING_FOOTPRINTS_ALL</span></div>
<div class="block"><p>All building footprints are shown.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapFeatureModes.BUILDING_FOOTPRINTS_ALL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="CONGESTION_ZONES_ALL">
<h3>CONGESTION_ZONES_ALL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">CONGESTION_ZONES_ALL</span></div>
<div class="block"><p>All congestion zones are shown.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapFeatureModes.CONGESTION_ZONES_ALL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="EXTRUDED_BUILDINGS_ALL">
<h3>EXTRUDED_BUILDINGS_ALL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">EXTRUDED_BUILDINGS_ALL</span></div>
<div class="block"><p>All extruded buildings are shown.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapFeatureModes.EXTRUDED_BUILDINGS_ALL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ENVIRONMENTAL_ZONES_ALL">
<h3>ENVIRONMENTAL_ZONES_ALL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ENVIRONMENTAL_ZONES_ALL</span></div>
<div class="block"><p>All environmental zones are shown.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapFeatureModes.ENVIRONMENTAL_ZONES_ALL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="LOW_SPEED_ZONES_ALL">
<h3>LOW_SPEED_ZONES_ALL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">LOW_SPEED_ZONES_ALL</span></div>
<div class="block"><p>All low speed zones are shown.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapFeatureModes.LOW_SPEED_ZONES_ALL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW">
<h3>TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW</span></div>
<div class="block"><p>Only available when Japan map is used.
 Traffic flow shows green lines depending on the region.
 In Japan green lines will not be shown,
 as if the <a href="sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes#TRAFFIC_FLOW_WITHOUT_FREE_FLOW"><code>TRAFFIC_FLOW_WITHOUT_FREE_FLOW</code></a> were used.
 In rest of the world, green lines will be shown, as if
 the <a href="sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes#TRAFFIC_FLOW_WITH_FREE_FLOW"><code>TRAFFIC_FLOW_WITH_FREE_FLOW</code></a> were used.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapFeatureModes.TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TRAFFIC_FLOW_WITH_FREE_FLOW">
<h3>TRAFFIC_FLOW_WITH_FREE_FLOW</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TRAFFIC_FLOW_WITH_FREE_FLOW</span></div>
<div class="block"><p>Traffic flow shows green lines when there is no traffic congestion.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapFeatureModes.TRAFFIC_FLOW_WITH_FREE_FLOW">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TRAFFIC_FLOW_WITHOUT_FREE_FLOW">
<h3>TRAFFIC_FLOW_WITHOUT_FREE_FLOW</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TRAFFIC_FLOW_WITHOUT_FREE_FLOW</span></div>
<div class="block"><p>Traffic flow does not show green lines when there is no traffic congestion.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapFeatureModes.TRAFFIC_FLOW_WITHOUT_FREE_FLOW">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TRAFFIC_INCIDENTS_ALL">
<h3>TRAFFIC_INCIDENTS_ALL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TRAFFIC_INCIDENTS_ALL</span></div>
<div class="block"><p>All available traffic incidents are shown.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapFeatureModes.TRAFFIC_INCIDENTS_ALL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="TRAFFIC_LIGHTS_ALL">
<h3>TRAFFIC_LIGHTS_ALL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">TRAFFIC_LIGHTS_ALL</span></div>
<div class="block"><p>All available traffic lights are shown.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapFeatureModes.TRAFFIC_LIGHTS_ALL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ROAD_EXIT_LABELS_NUMBERS_ONLY">
<h3>ROAD_EXIT_LABELS_NUMBERS_ONLY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ROAD_EXIT_LABELS_NUMBERS_ONLY</span></div>
<div class="block"><p>Road exit labels are shown with numbers, if available.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapFeatureModes.ROAD_EXIT_LABELS_NUMBERS_ONLY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ROAD_EXIT_LABELS_ALL">
<h3>ROAD_EXIT_LABELS_ALL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">ROAD_EXIT_LABELS_ALL</span></div>
<div class="block"><p>Road exit labels are shown with numbers and names, if available.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapFeatureModes.ROAD_EXIT_LABELS_ALL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="SHADOWS_ALL">
<h3>SHADOWS_ALL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">SHADOWS_ALL</span></div>
<div class="block"><p>Shadows are shown for extruded buildings and landmarks.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapFeatureModes.SHADOWS_ALL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="AMBIENT_OCCLUSION_ALL">
<h3>AMBIENT_OCCLUSION_ALL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">AMBIENT_OCCLUSION_ALL</span></div>
<div class="block"><p>Ambient occlusion effect is shown for extruded buildings and landmarks.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list">
<li><a href="sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapFeatureModes.AMBIENT_OCCLUSION_ALL">Constant Field Values</a></li>
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
<h3>MapFeatureModes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MapFeatureModes</span>()</div>
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
