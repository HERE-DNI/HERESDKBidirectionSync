---
title: "InstalledRegion (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-installedregion"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- InstalledRegion.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.maploader</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.maploader.InstalledRegion</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">InstalledRegion</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Represents a region, from persistent map storage.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-installedregion#lastUpdateTime">lastUpdateTime</a></code></div>
<div className="col-last even-row-color">
<div className="block">The last update time of the region in the persistent map storage.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-maploader-regionid" title="class in com.here.sdk.maploader">RegionId</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-installedregion#parentId">parentId</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Parent region identifier.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-maploader-regionid" title="class in com.here.sdk.maploader">RegionId</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-installedregion#regionId">regionId</a></code></div>
<div className="col-last even-row-color">
<div className="block">Unique identifier specifying a region.</div>
</div>
<div className="col-first odd-row-color"><code>long</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-installedregion#sizeOnDiskInBytes">sizeOnDiskInBytes</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Region size on disk in bytes.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-maploader-installedregionstatus" title="enum class in com.here.sdk.maploader">InstalledRegionStatus</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-installedregion#status">status</a></code></div>
<div className="col-last even-row-color">
<div className="block">Status of the region in the persistent map storage.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-installedregion#%3Cinit%3E(com.here.sdk.maploader.RegionId,com.here.sdk.maploader.RegionId,long,com.here.sdk.maploader.InstalledRegionStatus)">InstalledRegion</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-maploader-regionid" title="class in com.here.sdk.maploader">RegionId</a> regionId,
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-regionid" title="class in com.here.sdk.maploader">RegionId</a> parentId,
 long sizeOnDiskInBytes,
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-installedregionstatus" title="enum class in com.here.sdk.maploader">InstalledRegionStatus</a> status)</code></div>
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
<section className="detail" id="parentId">
<h3>parentId</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-regionid" title="class in com.here.sdk.maploader">RegionId</a></span> <span className="element-name">parentId</span></div>
<div className="block"><p>Parent region identifier. Continents have a parent_id of 0.</p></div>
</section>
</li>
<li>
<section className="detail" id="sizeOnDiskInBytes">
<h3>sizeOnDiskInBytes</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">long</span> <span className="element-name">sizeOnDiskInBytes</span></div>
<div className="block"><p>Region size on disk in bytes.</p></div>
</section>
</li>
<li>
<section className="detail" id="status">
<h3>status</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-installedregionstatus" title="enum class in com.here.sdk.maploader">InstalledRegionStatus</a></span> <span className="element-name">status</span></div>
<div className="block"><p>Status of the region in the persistent map storage.</p></div>
</section>
</li>
<li>
<section className="detail" id="lastUpdateTime">
<h3>lastUpdateTime</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></span> <span className="element-name">lastUpdateTime</span></div>
<div className="block"><p>The last update time of the region in the persistent map storage.</p></div>
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
<section className="detail" id="&lt;init&gt;(com.here.sdk.maploader.RegionId,com.here.sdk.maploader.RegionId,long,com.here.sdk.maploader.InstalledRegionStatus)">
<h3>InstalledRegion</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">InstalledRegion</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-regionid" title="class in com.here.sdk.maploader">RegionId</a> regionId,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-regionid" title="class in com.here.sdk.maploader">RegionId</a> parentId,
 long sizeOnDiskInBytes,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-installedregionstatus" title="enum class in com.here.sdk.maploader">InstalledRegionStatus</a> status)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>regionId</code> - <p>Unique identifier specifying a region.</p></dd>
<dd><code>parentId</code> - <p>Parent region identifier. Continents have a parent_id of 0.</p></dd>
<dd><code>sizeOnDiskInBytes</code> - <p>Region size on disk in bytes.</p></dd>
<dd><code>status</code> - <p>Status of the region in the persistent map storage.</p></dd>
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
