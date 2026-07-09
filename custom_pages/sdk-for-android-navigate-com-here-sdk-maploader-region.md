---
title: "Region (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-region"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- Region.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.maploader</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.maploader.Region</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">Region</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Defines an area, especially part of a country or the world that can be downloaded.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-maploader-region" title="class in com.here.sdk.maploader">Region</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-region#childRegions">childRegions</a></code></div>
<div className="col-last even-row-color">
<div className="block">All child regions for current region.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-region#name">name</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Name of region.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-maploader-navigabilitytype" title="enum class in com.here.sdk.maploader">NavigabilityType</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-region#navigability">navigability</a></code></div>
<div className="col-last even-row-color">
<div className="block">Indicates the navigability type of this region.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-maploader-regionid" title="class in com.here.sdk.maploader">RegionId</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-region#regionId">regionId</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Unique identifier specifying a region.</div>
</div>
<div className="col-first even-row-color"><code>long</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-region#sizeOnDiskInBytes">sizeOnDiskInBytes</a></code></div>
<div className="col-last even-row-color">
<div className="block">Represents the total size of the region on disk in bytes, assuming no pre-existing data on the disk.</div>
</div>
<div className="col-first odd-row-color"><code>long</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-region#sizeOnNetworkInBytes">sizeOnNetworkInBytes</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Region size, for downloading/during network operations, in bytes.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-region#%3Cinit%3E(com.here.sdk.maploader.RegionId)">Region</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-maploader-regionid" title="class in com.here.sdk.maploader">RegionId</a> regionId)</code></div>
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
<section className="detail" id="regionId">
<h3>regionId</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-regionid" title="class in com.here.sdk.maploader">RegionId</a></span> <span className="element-name">regionId</span></div>
<div className="block"><p>Unique identifier specifying a region.</p></div>
</section>
</li>
<li>
<section className="detail" id="name">
<h3>name</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">name</span></div>
<div className="block"><p>Name of region. Language is determined by the requested <a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core"><code>LanguageCode</code></a>. By default,
 it is in <a href="sdk-for-android-navigate-languagecode#EN_US"><code>LanguageCode.EN_US</code></a>.</p></div>
</section>
</li>
<li>
<section className="detail" id="sizeOnDiskInBytes">
<h3>sizeOnDiskInBytes</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">long</span> <span className="element-name">sizeOnDiskInBytes</span></div>
<div className="block"><p>Represents the total size of the region on disk in bytes, assuming no pre-existing data on the disk.
 This value is a theoretical maximum for the region's size allocation.
 Note: If overlapping regions exist or data is already present on the disk,
 the actual size occupied might be less than this value due to shared or reused map data.</p></div>
</section>
</li>
<li>
<section className="detail" id="sizeOnNetworkInBytes">
<h3>sizeOnNetworkInBytes</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">long</span> <span className="element-name">sizeOnNetworkInBytes</span></div>
<div className="block"><p>Region size, for downloading/during network operations, in bytes. Regions are downloaded in
 compressed form and hence they have reduced size on network.
 Note: This value represents the theoretical maximum size required for the
 region during transfer. If overlapping data already exists, the actual size
 downloaded may be smaller due to map data reuse.</p></div>
</section>
</li>
<li>
<section className="detail" id="childRegions">
<h3>childRegions</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-maploader-region" title="class in com.here.sdk.maploader">Region</a>&gt;</span> <span className="element-name">childRegions</span></div>
<div className="block"><p>All child regions for current region.
 Note that each child can again contain multiple children.
 A downloadable region will contain the content of all children.</p></div>
</section>
</li>
<li>
<section className="detail" id="navigability">
<h3>navigability</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-navigabilitytype" title="enum class in com.here.sdk.maploader">NavigabilityType</a></span> <span className="element-name">navigability</span></div>
<div className="block"><p>Indicates the navigability type of this region.</p></div>
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
<section className="detail" id="&lt;init&gt;(com.here.sdk.maploader.RegionId)">
<h3>Region</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">Region</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-regionid" title="class in com.here.sdk.maploader">RegionId</a> regionId)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>regionId</code> - <p>Unique identifier specifying a region.</p></dd>
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
