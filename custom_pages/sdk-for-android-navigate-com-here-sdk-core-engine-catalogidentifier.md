---
title: "CatalogIdentifier (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-engine-catalogidentifier"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- CatalogIdentifier.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.core.engine</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.core.engine.CatalogIdentifier</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">CatalogIdentifier</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>This class is used to identify any catalog in the HERE platform.
 A catalog is a storage-representation to store map data on the HERE platform.
 The data inside a catalog is divided into layers, where each layer consists
 of datasets with similar functional attributes in the physical world.
 For example, there can be a layer for road-topology, a layer for
 road-attributes (such as speed limits) and a layer for places and business
 addresses. All these layers, in different geographic regions, can be grouped together into a
 catalog to create a representation of the world we live in, called HERE map.
 It can be also used to render a <code>MapView</code>. Each geographic region is cut into geospatial
 tiles for efficient search, map display, routing, map matching, and driver warnings.
 Each tile partitions the map data (in one or more layers, depending on the product)
 in the geolocation of that specific tile.
 The data inside a catalog is logically managed and access controlled
 as a single set. If you have any data that you want to bring to the HERE
 platform, you need a catalog to contain it.
 For additional information about catalogs, and related concepts of data representation
 on the HERE platform, refer to
 <a href="https://www.here.com/docs/bundle/data-api-developer-guide/page/rest/catalogs.html">the Data API</a>
 and <a href="https://www.here.com/docs/bundle/introduction-to-mapping-concepts-user-guide/page/topics/maps-layers-tiles.html">Introduction to Mapping Concepts</a></p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-catalogidentifier#hrn">hrn</a></code></div>
<div className="col-last even-row-color">
<div className="block">A HERE Resource Name (HRN) for this catalog.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang">Long</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-catalogidentifier#version">version</a></code></div>
<div className="col-last odd-row-color">
<div className="block">A version number for a catalog.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-catalogidentifier#%3Cinit%3E()">CatalogIdentifier</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
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
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section className="detail" id="hrn">
<h3>hrn</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">hrn</span></div>
<div className="block"><p>A HERE Resource Name (HRN) for this catalog. This is a unique string returned by the HERE platform when you add a new
 catalog to your project. For information about catalog creation process refer to
 <a href="https://www.here.com/docs/bundle/data-api-developer-guide/page/rest/creating-a-catalog.html">the Data API</a>
 By default, this field points to a default catalog on HERE platform, which contains data for the whole world excluding the region of Japan.
 Use <a href="sdk-for-android-navigate-catalogconfiguration#getDefault(com.here.sdk.core.engine.CatalogType)"><code>CatalogConfiguration.getDefault(com.here.sdk.core.engine.CatalogType)</code></a> to get the default HRN value for use with the HERE platform.</p></div>
</section>
</li>
<li>
<section className="detail" id="version">
<h3>version</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang">Long</a></span> <span className="element-name">version</span></div>
<div className="block"><p>A version number for a catalog. When accessing a catalog, this version must be specified.
 Set <code>null</code> to automatically get the latest version for a catalog.
 The field defaults to <code>null</code>.
 Since the data inside a catalog can be updated, each published modification needs to correlate
 to a specific version number.
 Note: when <code>CatalogIdentifier</code> created with <a href="sdk-for-android-navigate-com-here-sdk-core-engine-desiredcatalog" title="class in com.here.sdk.core.engine"><code>DesiredCatalog</code></a> then:
 <ul>
<li>numerical <code>-1</code> corresponds to <a href="sdk-for-android-navigate-catalogversionhint#latest(boolean)"><code>CatalogVersionHint.latest(boolean)</code></a> with <code>ignoreCachedData</code> set to <code>true</code>;</li>
<li><code>null</code> corresponds to <a href="sdk-for-android-navigate-catalogversionhint#latest(boolean)"><code>CatalogVersionHint.latest(boolean)</code></a> with <code>ignoreCachedData</code> set to <code>false</code>;</li>
<li>other numerical values correspond to <code>version</code> passed to <a href="sdk-for-android-navigate-catalogversionhint#specific(long)"><code>CatalogVersionHint.specific(long)</code></a>.</li>
</ul></p></div>
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
<h3>CatalogIdentifier</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">CatalogIdentifier</span>()</div>
<div className="block"><p>Creates a new instance.</p></div>
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
<section className="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">equals</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="hashCode()">
<h3>hashCode</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">hashCode</span>()</div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
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
