---
title: "MapFeatureModes (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapFeatureModes.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.mapview.MapFeatureModes</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">MapFeatureModes</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Holds constants for map feature modes, to be used with <a href="sdk-for-android-navigate-mapscene#enableFeatures(java.util.Map)"><code>MapScene.enableFeatures(java.util.Map<java.lang.string, java.lang.string="">)</java.lang.string,></code></a>.
 Use <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#DEFAULT"><code>DEFAULT</code></a> to enable a feature with its default mode.
 Note: The default mode is defined by the currently loaded map scene configuration and
 may vary per <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscheme" title="enum class in com.here.sdk.mapview"><code>MapScheme</code></a>. The currently active features and modes can be inspected
 using <a href="sdk-for-android-navigate-mapscene#getActiveFeatures()"><code>MapScene.getActiveFeatures()</code></a> after the scene is loaded.
 See <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeatures" title="class in com.here.sdk.mapview"><code>MapFeatures</code></a> for constants representing the feature names.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#AMBIENT_OCCLUSION_ALL">AMBIENT_OCCLUSION_ALL</a></code></div>
<div className="col-last even-row-color">
<div className="block">Ambient occlusion effect is shown for extruded buildings and landmarks.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#BUILDING_FOOTPRINTS_ALL">BUILDING_FOOTPRINTS_ALL</a></code></div>
<div className="col-last odd-row-color">
<div className="block">All building footprints are shown.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#CONGESTION_ZONES_ALL">CONGESTION_ZONES_ALL</a></code></div>
<div className="col-last even-row-color">
<div className="block">All congestion zones are shown.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#CONTOURS_ALL">CONTOURS_ALL</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Contour lines indicating representing elevation changes are shown.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#DEFAULT">DEFAULT</a></code></div>
<div className="col-last even-row-color">
<div className="block">Enables the default mode of a map feature.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#ENVIRONMENTAL_ZONES_ALL">ENVIRONMENTAL_ZONES_ALL</a></code></div>
<div className="col-last odd-row-color">
<div className="block">All environmental zones are shown.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#EXTRUDED_BUILDINGS_ALL">EXTRUDED_BUILDINGS_ALL</a></code></div>
<div className="col-last even-row-color">
<div className="block">All extruded buildings are shown.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#LANDMARKS_GRAYSCALE">LANDMARKS_GRAYSCALE</a></code></div>
<div className="col-last odd-row-color">
<div className="block">3D landmarks are textured with grayscale filter.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#LANDMARKS_TEXTURED">LANDMARKS_TEXTURED</a></code></div>
<div className="col-last even-row-color">
<div className="block">3D landmarks are textured.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#LANDMARKS_TEXTURELESS">LANDMARKS_TEXTURELESS</a></code></div>
<div className="col-last odd-row-color">
<div className="block">3D landmarks have solid color.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#LOW_SPEED_ZONES_ALL">LOW_SPEED_ZONES_ALL</a></code></div>
<div className="col-last even-row-color">
<div className="block">All low speed zones are shown.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#PUBLIC_TRANSIT_ALL">PUBLIC_TRANSIT_ALL</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Line geometry for all available public transit systems is shown; including subway, tram, train,
 monorail, ferry and more.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#PUBLIC_TRANSIT_ASIA">PUBLIC_TRANSIT_ASIA</a></code></div>
<div className="col-last even-row-color">
<div className="block">Line geometry for selected public transit systems is shown: subway lines in Japan.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#ROAD_EXIT_LABELS_ALL">ROAD_EXIT_LABELS_ALL</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Road exit labels are shown with numbers and names, if available.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#ROAD_EXIT_LABELS_NUMBERS_ONLY">ROAD_EXIT_LABELS_NUMBERS_ONLY</a></code></div>
<div className="col-last even-row-color">
<div className="block">Road exit labels are shown with numbers, if available.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#SAFETY_CAMERAS_ALL">SAFETY_CAMERAS_ALL</a></code></div>
<div className="col-last odd-row-color">
<div className="block">All types of safety cameras are shown.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#SHADOWS_ALL">SHADOWS_ALL</a></code></div>
<div className="col-last even-row-color">
<div className="block">Shadows are shown for extruded buildings and landmarks.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#TERRAIN_3D">TERRAIN_3D</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Topography-shading is shown on 3d terrain.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#TERRAIN_HILLSHADE">TERRAIN_HILLSHADE</a></code></div>
<div className="col-last even-row-color">
<div className="block">Topography-shading is shown.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW">TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Only available when Japan map is used.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#TRAFFIC_FLOW_WITH_FREE_FLOW">TRAFFIC_FLOW_WITH_FREE_FLOW</a></code></div>
<div className="col-last even-row-color">
<div className="block">Traffic flow shows green lines when there is no traffic congestion.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#TRAFFIC_FLOW_WITHOUT_FREE_FLOW">TRAFFIC_FLOW_WITHOUT_FREE_FLOW</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Traffic flow does not show green lines when there is no traffic congestion.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#TRAFFIC_INCIDENTS_ALL">TRAFFIC_INCIDENTS_ALL</a></code></div>
<div className="col-last even-row-color">
<div className="block">All available traffic incidents are shown.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#TRAFFIC_LIGHTS_ALL">TRAFFIC_LIGHTS_ALL</a></code></div>
<div className="col-last odd-row-color">
<div className="block">All available traffic lights are shown.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#TRUCK_PREFERRED_ROADS_ALL">TRUCK_PREFERRED_ROADS_ALL</a></code></div>
<div className="col-last even-row-color">
<div className="block">Display truck preferred roads</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#VEHICLE_RESTRICTIONS_ACTIVE">VEHICLE_RESTRICTIONS_ACTIVE</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Inactive time-based restrictions are not shown.</div>
</div>
<div className="col-first even-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#VEHICLE_RESTRICTIONS_ACTIVE_AND_INACTIVE">VEHICLE_RESTRICTIONS_ACTIVE_AND_INACTIVE</a></code></div>
<div className="col-last even-row-color">
<div className="block">Both active and inactive time-based restrictions are shown.</div>
</div>
<div className="col-first odd-row-color"><code>static final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#VEHICLE_RESTRICTIONS_ACTIVE_AND_INACTIVE_DIFFERENTIATED">VEHICLE_RESTRICTIONS_ACTIVE_AND_INACTIVE_DIFFERENTIATED</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Both active and inactive restrictions are shown, but inactive time-based restrictions are
 shown as faded.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#%3Cinit%3E()">MapFeatureModes</a>()</code></div>
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
<section className="detail" id="DEFAULT">
<h3>DEFAULT</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">DEFAULT</span></div>
<div className="block"><p>Enables the default mode of a map feature. Can be used with any map feature.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.DEFAULT">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="BUILDING_FOOTPRINTS_ALL">
<h3>BUILDING_FOOTPRINTS_ALL</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">BUILDING_FOOTPRINTS_ALL</span></div>
<div className="block"><p>All building footprints are shown.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.BUILDING_FOOTPRINTS_ALL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="CONGESTION_ZONES_ALL">
<h3>CONGESTION_ZONES_ALL</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">CONGESTION_ZONES_ALL</span></div>
<div className="block"><p>All congestion zones are shown.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.CONGESTION_ZONES_ALL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="EXTRUDED_BUILDINGS_ALL">
<h3>EXTRUDED_BUILDINGS_ALL</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">EXTRUDED_BUILDINGS_ALL</span></div>
<div className="block"><p>All extruded buildings are shown.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.EXTRUDED_BUILDINGS_ALL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="ENVIRONMENTAL_ZONES_ALL">
<h3>ENVIRONMENTAL_ZONES_ALL</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">ENVIRONMENTAL_ZONES_ALL</span></div>
<div className="block"><p>All environmental zones are shown.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.ENVIRONMENTAL_ZONES_ALL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="LOW_SPEED_ZONES_ALL">
<h3>LOW_SPEED_ZONES_ALL</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">LOW_SPEED_ZONES_ALL</span></div>
<div className="block"><p>All low speed zones are shown.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.LOW_SPEED_ZONES_ALL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW">
<h3>TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW</span></div>
<div className="block"><p>Only available when Japan map is used.
 Traffic flow shows green lines depending on the region.
 In Japan green lines will not be shown,
 as if the <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#TRAFFIC_FLOW_WITHOUT_FREE_FLOW"><code>TRAFFIC_FLOW_WITHOUT_FREE_FLOW</code></a> were used.
 In rest of the world, green lines will be shown, as if
 the <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapfeaturemodes#TRAFFIC_FLOW_WITH_FREE_FLOW"><code>TRAFFIC_FLOW_WITH_FREE_FLOW</code></a> were used.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="TRAFFIC_FLOW_WITH_FREE_FLOW">
<h3>TRAFFIC_FLOW_WITH_FREE_FLOW</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">TRAFFIC_FLOW_WITH_FREE_FLOW</span></div>
<div className="block"><p>Traffic flow shows green lines when there is no traffic congestion.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.TRAFFIC_FLOW_WITH_FREE_FLOW">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="TRAFFIC_FLOW_WITHOUT_FREE_FLOW">
<h3>TRAFFIC_FLOW_WITHOUT_FREE_FLOW</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">TRAFFIC_FLOW_WITHOUT_FREE_FLOW</span></div>
<div className="block"><p>Traffic flow does not show green lines when there is no traffic congestion.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.TRAFFIC_FLOW_WITHOUT_FREE_FLOW">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="TRAFFIC_INCIDENTS_ALL">
<h3>TRAFFIC_INCIDENTS_ALL</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">TRAFFIC_INCIDENTS_ALL</span></div>
<div className="block"><p>All available traffic incidents are shown.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.TRAFFIC_INCIDENTS_ALL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="TRAFFIC_LIGHTS_ALL">
<h3>TRAFFIC_LIGHTS_ALL</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">TRAFFIC_LIGHTS_ALL</span></div>
<div className="block"><p>All available traffic lights are shown.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.TRAFFIC_LIGHTS_ALL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="LANDMARKS_TEXTURED">
<h3>LANDMARKS_TEXTURED</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">LANDMARKS_TEXTURED</span></div>
<div className="block"><p>3D landmarks are textured.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.LANDMARKS_TEXTURED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="LANDMARKS_GRAYSCALE">
<h3>LANDMARKS_GRAYSCALE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">LANDMARKS_GRAYSCALE</span></div>
<div className="block"><p>3D landmarks are textured with grayscale filter.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.LANDMARKS_GRAYSCALE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="LANDMARKS_TEXTURELESS">
<h3>LANDMARKS_TEXTURELESS</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">LANDMARKS_TEXTURELESS</span></div>
<div className="block"><p>3D landmarks have solid color.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.LANDMARKS_TEXTURELESS">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="VEHICLE_RESTRICTIONS_ACTIVE_AND_INACTIVE">
<h3>VEHICLE_RESTRICTIONS_ACTIVE_AND_INACTIVE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">VEHICLE_RESTRICTIONS_ACTIVE_AND_INACTIVE</span></div>
<div className="block"><p>Both active and inactive time-based restrictions are shown.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.VEHICLE_RESTRICTIONS_ACTIVE_AND_INACTIVE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="VEHICLE_RESTRICTIONS_ACTIVE_AND_INACTIVE_DIFFERENTIATED">
<h3>VEHICLE_RESTRICTIONS_ACTIVE_AND_INACTIVE_DIFFERENTIATED</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">VEHICLE_RESTRICTIONS_ACTIVE_AND_INACTIVE_DIFFERENTIATED</span></div>
<div className="block"><p>Both active and inactive restrictions are shown, but inactive time-based restrictions are
 shown as faded.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.VEHICLE_RESTRICTIONS_ACTIVE_AND_INACTIVE_DIFFERENTIATED">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="VEHICLE_RESTRICTIONS_ACTIVE">
<h3>VEHICLE_RESTRICTIONS_ACTIVE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">VEHICLE_RESTRICTIONS_ACTIVE</span></div>
<div className="block"><p>Inactive time-based restrictions are not shown.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.VEHICLE_RESTRICTIONS_ACTIVE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="SAFETY_CAMERAS_ALL">
<h3>SAFETY_CAMERAS_ALL</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">SAFETY_CAMERAS_ALL</span></div>
<div className="block"><p>All types of safety cameras are shown. Includes speed, red light, red light + speed,
 bus lane, distance and speed section cameras.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.SAFETY_CAMERAS_ALL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="TERRAIN_HILLSHADE">
<h3>TERRAIN_HILLSHADE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">TERRAIN_HILLSHADE</span></div>
<div className="block"><p>Topography-shading is shown.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.TERRAIN_HILLSHADE">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="TERRAIN_3D">
<h3>TERRAIN_3D</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">TERRAIN_3D</span></div>
<div className="block"><p>Topography-shading is shown on 3d terrain.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.TERRAIN_3D">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="PUBLIC_TRANSIT_ALL">
<h3>PUBLIC_TRANSIT_ALL</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">PUBLIC_TRANSIT_ALL</span></div>
<div className="block"><p>Line geometry for all available public transit systems is shown; including subway, tram, train,
 monorail, ferry and more.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.PUBLIC_TRANSIT_ALL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="PUBLIC_TRANSIT_ASIA">
<h3>PUBLIC_TRANSIT_ASIA</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">PUBLIC_TRANSIT_ASIA</span></div>
<div className="block"><p>Line geometry for selected public transit systems is shown: subway lines in Japan.
 Only available when Japan map is used.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.PUBLIC_TRANSIT_ASIA">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="ROAD_EXIT_LABELS_NUMBERS_ONLY">
<h3>ROAD_EXIT_LABELS_NUMBERS_ONLY</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">ROAD_EXIT_LABELS_NUMBERS_ONLY</span></div>
<div className="block"><p>Road exit labels are shown with numbers, if available.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.ROAD_EXIT_LABELS_NUMBERS_ONLY">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="ROAD_EXIT_LABELS_ALL">
<h3>ROAD_EXIT_LABELS_ALL</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">ROAD_EXIT_LABELS_ALL</span></div>
<div className="block"><p>Road exit labels are shown with numbers and names, if available.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.ROAD_EXIT_LABELS_ALL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="SHADOWS_ALL">
<h3>SHADOWS_ALL</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">SHADOWS_ALL</span></div>
<div className="block"><p>Shadows are shown for extruded buildings and landmarks.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.SHADOWS_ALL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="AMBIENT_OCCLUSION_ALL">
<h3>AMBIENT_OCCLUSION_ALL</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">AMBIENT_OCCLUSION_ALL</span></div>
<div className="block"><p>Ambient occlusion effect is shown for extruded buildings and landmarks.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.AMBIENT_OCCLUSION_ALL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="CONTOURS_ALL">
<h3>CONTOURS_ALL</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">CONTOURS_ALL</span></div>
<div className="block"><p>Contour lines indicating representing elevation changes are shown.</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.CONTOURS_ALL">Constant Field Values</a></li>
</ul>
</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="TRUCK_PREFERRED_ROADS_ALL">
<h3>TRUCK_PREFERRED_ROADS_ALL</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">TRUCK_PREFERRED_ROADS_ALL</span></div>
<div className="block"><p>Display truck preferred roads</p></div>
<dl className="notes">
<dt>See Also:</dt>
<dd>
<ul className="see-list">
<li><a href="sdk-for-android-navigate-constant-values#com.here.sdk.mapview.MapFeatureModes.TRUCK_PREFERRED_ROADS_ALL">Constant Field Values</a></li>
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
<h3>MapFeatureModes</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">MapFeatureModes</span>()</div>
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
