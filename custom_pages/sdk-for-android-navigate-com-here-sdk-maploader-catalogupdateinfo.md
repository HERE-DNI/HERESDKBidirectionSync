---
title: "CatalogUpdateInfo (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-catalogupdateinfo"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- CatalogUpdateInfo.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.maploader</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.maploader.CatalogUpdateInfo</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">CatalogUpdateInfo</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Holds information for the catalog update intent. Provides information regarding installed catalog
 and its latest available version.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>long</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-catalogupdateinfo#diskSizeInBytes">diskSizeInBytes</a></code></div>
<div className="col-last even-row-color">
<div className="block">Estimates the size of the offline maps after an update.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-maploader-installedcatalog" title="class in com.here.sdk.maploader">InstalledCatalog</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-catalogupdateinfo#installedCatalog">installedCatalog</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Installed catalog.</div>
</div>
<div className="col-first even-row-color"><code>long</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-catalogupdateinfo#latestVersion">latestVersion</a></code></div>
<div className="col-last even-row-color">
<div className="block">Latest version available for a catalog.</div>
</div>
<div className="col-first odd-row-color"><code>long</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-catalogupdateinfo#networkSizeInBytes">networkSizeInBytes</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Total size in bytes that needs to be downloaded over the network to update the installed catalog.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-maploader-catalogupdatestate" title="enum class in com.here.sdk.maploader">CatalogUpdateState</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-catalogupdateinfo#state">state</a></code></div>
<div className="col-last even-row-color">
<div className="block">State of current catalog update.</div>
</div>
<div className="col-first odd-row-color"><code>long</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-catalogupdateinfo#temporaryDiskRequirementInBytes">temporaryDiskRequirementInBytes</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Performing an update requires additional storage on top of existing offline maps.</div>
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
<section className="detail" id="installedCatalog">
<h3>installedCatalog</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-installedcatalog" title="class in com.here.sdk.maploader">InstalledCatalog</a></span> <span className="element-name">installedCatalog</span></div>
<div className="block"><p>Installed catalog.</p></div>
</section>
</li>
<li>
<section className="detail" id="latestVersion">
<h3>latestVersion</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">long</span> <span className="element-name">latestVersion</span></div>
<div className="block"><p>Latest version available for a catalog.</p></div>
</section>
</li>
<li>
<section className="detail" id="state">
<h3>state</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-catalogupdatestate" title="enum class in com.here.sdk.maploader">CatalogUpdateState</a></span> <span className="element-name">state</span></div>
<div className="block"><p>State of current catalog update.</p></div>
</section>
</li>
<li>
<section className="detail" id="networkSizeInBytes">
<h3>networkSizeInBytes</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">long</span> <span className="element-name">networkSizeInBytes</span></div>
<div className="block"><p>Total size in bytes that needs to be downloaded over the network to update the installed catalog.</p></div>
</section>
</li>
<li>
<section className="detail" id="diskSizeInBytes">
<h3>diskSizeInBytes</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">long</span> <span className="element-name">diskSizeInBytes</span></div>
<div className="block"><p>Estimates the size of the offline maps after an update.
 <strong>Note</strong>
 In order to estimate, if catalog update is feasible, given the amount of free space on the disk,
 application can compare amount of the free space on the disk with <code>disk_size_in_bytes + temporary_disk_requirement_in_bytes</code>.</p></div>
</section>
</li>
<li>
<section className="detail" id="temporaryDiskRequirementInBytes">
<h3>temporaryDiskRequirementInBytes</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">long</span> <span className="element-name">temporaryDiskRequirementInBytes</span></div>
<div className="block"><p>Performing an update requires additional storage on top of existing offline maps.
 This space is used to store intermittent copy of map content according to
 the specified <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdater-mapupdateversioncommitpolicy" title="enum class in com.here.sdk.maploader"><code>MapUpdater.MapUpdateVersionCommitPolicy</code></a>.
 <strong>Note</strong>
 In order to estimate, if catalog update is feasible, given the amount of free space on the disk,
 application can compare amount of the free space on the disk with <code>disk_size_in_bytes + temporary_disk_requirement_in_bytes</code>.</p></div>
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
