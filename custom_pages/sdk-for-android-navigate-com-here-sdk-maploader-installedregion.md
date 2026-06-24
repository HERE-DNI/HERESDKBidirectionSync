---
title: "InstalledRegion (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-installedregion"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- InstalledRegion.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.maploader.InstalledRegion</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">InstalledRegion</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Represents a region, from persistent map storage.</p></div>
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
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-installedregion#lastUpdateTime">lastUpdateTime</a></code></div>
<div class="col-last even-row-color">
<div class="block">The last update time of the region in the persistent map storage.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-regionid" title="class in com.here.sdk.maploader">RegionId</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-installedregion#parentId">parentId</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Parent region identifier.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-regionid" title="class in com.here.sdk.maploader">RegionId</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-installedregion#regionId">regionId</a></code></div>
<div class="col-last even-row-color">
<div class="block">Unique identifier specifying a region.</div>
</div>
<div class="col-first odd-row-color"><code>long</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-installedregion#sizeOnDiskInBytes">sizeOnDiskInBytes</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Region size on disk in bytes.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-installedregionstatus" title="enum class in com.here.sdk.maploader">InstalledRegionStatus</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-installedregion#status">status</a></code></div>
<div class="col-last even-row-color">
<div class="block">Status of the region in the persistent map storage.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-installedregion#%3Cinit%3E(com.here.sdk.maploader.RegionId,com.here.sdk.maploader.RegionId,long,com.here.sdk.maploader.InstalledRegionStatus)">InstalledRegion</a><wbr/>(<a href="sdk-for-android-navigate-regionid" title="class in com.here.sdk.maploader">RegionId</a> regionId,
 <a href="sdk-for-android-navigate-regionid" title="class in com.here.sdk.maploader">RegionId</a> parentId,
 long sizeOnDiskInBytes,
 <a href="sdk-for-android-navigate-installedregionstatus" title="enum class in com.here.sdk.maploader">InstalledRegionStatus</a> status)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-installedregion#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>

<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-installedregion#hashCode()">hashCode</a>()</code></div>

</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="regionId">
<h3>regionId</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-regionid" title="class in com.here.sdk.maploader">RegionId</a></span> <span class="element-name">regionId</span></div>
<div class="block"><p>Unique identifier specifying a region.</p></div>
</section>
</li>
<li>
<section class="detail" id="parentId">
<h3>parentId</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-regionid" title="class in com.here.sdk.maploader">RegionId</a></span> <span class="element-name">parentId</span></div>
<div class="block"><p>Parent region identifier. Continents have a parent_id of 0.</p></div>
</section>
</li>
<li>
<section class="detail" id="sizeOnDiskInBytes">
<h3>sizeOnDiskInBytes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">sizeOnDiskInBytes</span></div>
<div class="block"><p>Region size on disk in bytes.</p></div>
</section>
</li>
<li>
<section class="detail" id="status">
<h3>status</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-installedregionstatus" title="enum class in com.here.sdk.maploader">InstalledRegionStatus</a></span> <span class="element-name">status</span></div>
<div class="block"><p>Status of the region in the persistent map storage.</p></div>
</section>
</li>
<li>
<section class="detail" id="lastUpdateTime">
<h3>lastUpdateTime</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a></span> <span class="element-name">lastUpdateTime</span></div>
<div class="block"><p>The last update time of the region in the persistent map storage.</p></div>
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
<section class="detail" id="&lt;init&gt;(com.here.sdk.maploader.RegionId,com.here.sdk.maploader.RegionId,long,com.here.sdk.maploader.InstalledRegionStatus)">
<h3>InstalledRegion</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">InstalledRegion</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-regionid" title="class in com.here.sdk.maploader">RegionId</a> regionId,
 @NonNull
 <a href="sdk-for-android-navigate-regionid" title="class in com.here.sdk.maploader">RegionId</a> parentId,
 long sizeOnDiskInBytes,
 @NonNull
 <a href="sdk-for-android-navigate-installedregionstatus" title="enum class in com.here.sdk.maploader">InstalledRegionStatus</a> status)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
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
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
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
`
}</HTMLBlock>
