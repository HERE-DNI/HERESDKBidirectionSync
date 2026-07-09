---
title: "MapScene.MapPickFilter.ContentType (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapscene-mappickfilter-contenttype"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapScene.MapPickFilter.ContentType.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">java.lang.Enum</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene-mappickfilter-contenttype" title="enum class in com.here.sdk.mapview">MapScene.MapPickFilter.ContentType</a>&gt;
<div className="inheritance">com.here.sdk.mapview.MapScene.MapPickFilter.ContentType</div>
</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene-mappickfilter-contenttype" title="enum class in com.here.sdk.mapview">MapScene.MapPickFilter.ContentType</a>&gt;</code>, <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" title="class or interface in java.lang.constant">Constable</a></code></dd>
</dl>
<dl className="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene-mappickfilter" title="class in com.here.sdk.mapview">MapScene.MapPickFilter</a></dd>
</dl>

<div className="type-signature"><span className="modifiers">public static enum </span><span className="element-name type-name-label">MapScene.MapPickFilter.ContentType</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene-mappickfilter-contenttype" title="enum class in com.here.sdk.mapview">MapScene.MapPickFilter.ContentType</a>&gt;</span></div>
<div className="block"><p>Type of the map content to be picked.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="inherited-list">

<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">Enum.EnumDesc</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">E</a> extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">E</a>&gt;&gt;</code></div>
</section>
</li>
<!-- =========== ENUM CONSTANT SUMMARY =========== -->
<li>
<section className="constants-summary" id="enum-constant-summary">

<div className="caption"><span>Enum Constants</span></div>
<div className="summary-table two-column-summary">


<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene-mappickfilter-contenttype#CUSTOM_LAYER_DATA">CUSTOM_LAYER_DATA</a></code></div>
<div className="col-last even-row-color">
<div className="block">Custom user map content added using custom datasources e.g.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene-mappickfilter-contenttype#MAP_CONTENT">MAP_CONTENT</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Pickable map content currently consists of:
 
 Embedded carto POI markers that by default are available on the map.
 Traffic incidents that are visible when they are enabled using <a href="sdk-for-android-navigate-mapscene#enableFeatures(java.util.Map)"><code>MapScene.enableFeatures(java.util.Map<java.lang.string, java.lang.string="">)</java.lang.string,></code></a>
 with <a href="sdk-for-android-navigate-mapfeatures#TRAFFIC_INCIDENTS"><code>MapFeatures.TRAFFIC_INCIDENTS</code></a>.
 Vehicle restrictions are only available for the Navigate license.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene-mappickfilter-contenttype#MAP_ITEMS">MAP_ITEMS</a></code></div>
<div className="col-last even-row-color">
<div className="block">Map items added through a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene" title="class in com.here.sdk.mapview"><code>MapScene</code></a> like <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a>, <a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline" title="class in com.here.sdk.mapview"><code>MapPolyline</code></a>, <a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolygon" title="class in com.here.sdk.mapview"><code>MapPolygon</code></a>.</div>
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
<h3 id="methods-inherited-from-class-java.lang.Enum">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)" title="class or interface in java.lang">compareTo</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()" title="class or interface in java.lang">describeConstable</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()" title="class or interface in java.lang">getDeclaringClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()" title="class or interface in java.lang">name</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()" title="class or interface in java.lang">ordinal</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String)" title="class or interface in java.lang">valueOf</a></code></div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ ENUM CONSTANT DETAIL =========== -->
<li>
<section className="constant-details" id="enum-constant-detail">

<ul className="member-list">
<li>
<section className="detail" id="MAP_ITEMS">
<h3>MAP_ITEMS</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene-mappickfilter-contenttype" title="enum class in com.here.sdk.mapview">MapScene.MapPickFilter.ContentType</a></span> <span className="element-name">MAP_ITEMS</span></div>
<div className="block"><p>Map items added through a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene" title="class in com.here.sdk.mapview"><code>MapScene</code></a> like <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a>, <a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline" title="class in com.here.sdk.mapview"><code>MapPolyline</code></a>, <a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolygon" title="class in com.here.sdk.mapview"><code>MapPolygon</code></a>.</p></div>
</section>
</li>
<li>
<section className="detail" id="MAP_CONTENT">
<h3>MAP_CONTENT</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene-mappickfilter-contenttype" title="enum class in com.here.sdk.mapview">MapScene.MapPickFilter.ContentType</a></span> <span className="element-name">MAP_CONTENT</span></div>
<div className="block"><p>Pickable map content currently consists of:
 <ul>
<li>Embedded carto POI markers that by default are available on the map.</li>
<li>Traffic incidents that are visible when they are enabled using <a href="sdk-for-android-navigate-mapscene#enableFeatures(java.util.Map)"><code>MapScene.enableFeatures(java.util.Map<java.lang.string, java.lang.string="">)</java.lang.string,></code></a>
 with <a href="sdk-for-android-navigate-mapfeatures#TRAFFIC_INCIDENTS"><code>MapFeatures.TRAFFIC_INCIDENTS</code></a>.</li>
<li>Vehicle restrictions are only available for the Navigate license.
 Vehicle restrictions are enabled using <a href="sdk-for-android-navigate-mapscene#enableFeatures(java.util.Map)"><code>MapScene.enableFeatures(java.util.Map<java.lang.string, java.lang.string="">)</java.lang.string,></code></a> with
 <code>MapFeatures.VEHICLE_RESTRICTIONS</code>. Please note that the vehicle restriction line marking the
 affected street is pickable and not the restriction icon itself.
 Only visible POIs, traffic incidents and vehicle restrictions lines can be picked, i.e. only
 those categories that are not hidden and those that are not covered by any custom marker.</li>
</ul></p></div>
</section>
</li>
<li>
<section className="detail" id="CUSTOM_LAYER_DATA">
<h3>CUSTOM_LAYER_DATA</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene-mappickfilter-contenttype" title="enum class in com.here.sdk.mapview">MapScene.MapPickFilter.ContentType</a></span> <span className="element-name">CUSTOM_LAYER_DATA</span></div>
<div className="block"><p>Custom user map content added using custom datasources e.g. <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-linedatasource" title="class in com.here.sdk.mapview.datasource"><code>LineDataSource</code></a>,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-polygondatasource" title="class in com.here.sdk.mapview.datasource"><code>PolygonDataSource</code></a> and layers.</p></div>
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
<section className="detail" id="values()">
<h3>values</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene-mappickfilter-contenttype" title="enum class in com.here.sdk.mapview">MapScene.MapPickFilter.ContentType</a>[]</span> <span className="element-name">values</span>()</div>
<div className="block">Returns an array containing the constants of this enum class, in
the order they are declared.</div>
<dl className="notes">
<dt>Returns:</dt>
<dd>an array containing the constants of this enum class, in the order they are declared</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="valueOf(java.lang.String)">
<h3>valueOf</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscene-mappickfilter-contenttype" title="enum class in com.here.sdk.mapview">MapScene.MapPickFilter.ContentType</a></span> <span className="element-name">valueOf</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div className="block">Returns the enum constant of this class with the specified name.
The string must match <i>exactly</i> an identifier used to declare an
enum constant in this class.  (Extraneous whitespace characters are 
not permitted.)</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the name of the enum constant to be returned.</dd>
<dt>Returns:</dt>
<dd>the enum constant with the specified name</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if this enum class has no constant with the specified name</dd>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html" title="class or interface in java.lang">NullPointerException</a></code> - if the argument is null</dd>
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
