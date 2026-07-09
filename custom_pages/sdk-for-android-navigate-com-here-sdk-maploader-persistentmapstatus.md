---
title: "PersistentMapStatus (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- PersistentMapStatus.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.maploader</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">java.lang.Enum</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a>&gt;
<div className="inheritance">com.here.sdk.maploader.PersistentMapStatus</div>
</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a>&gt;</code>, <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" title="class or interface in java.lang.constant">Constable</a></code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public enum </span><span className="element-name type-name-label">PersistentMapStatus</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a>&gt;</span></div>
<div className="block"><p>Specifies possible statuses of the already downloaded map regions as a whole.
 Note: This can be valid only for a single region in case of a <a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus#CORRUPTED"><code>CORRUPTED</code></a> state.</p></div>
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


<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus#BROKEN_UPDATE">BROKEN_UPDATE</a></code></div>
<div className="col-last even-row-color">
<div className="block">Unrecoverable error during construction of pending update parameters.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus#CORRUPTED">CORRUPTED</a></code></div>
<div className="col-last odd-row-color">
<div className="block">One or more downloaded regions failed to open and a repair action should be performed to mitigate this
 issue.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus#INVALID_PATH">INVALID_PATH</a></code></div>
<div className="col-last even-row-color">
<div className="block">Unreachable <a href="sdk-for-android-navigate-sdkoptions#cachePath"><code>SDKOptions.cachePath</code></a> or <a href="sdk-for-android-navigate-sdkoptions#persistentMapStoragePath"><code>SDKOptions.persistentMapStoragePath</code></a>.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus#INVALID_STATE">INVALID_STATE</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Unrecoverable error during construction of internal map access object.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus#MIGRATION_NEEDED">MIGRATION_NEEDED</a></code></div>
<div className="col-last even-row-color">
<div className="block">Indicates that the downloaded regions need to be migrated to a new internal format by calling
 <code>sdk.maploader.MapDownloader.repair_persistent_map</code>.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus#OK">OK</a></code></div>
<div className="col-last odd-row-color">
<div className="block">All downloaded regions are in a workable state, no issues found.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus#PENDING_UPDATE">PENDING_UPDATE</a></code></div>
<div className="col-last even-row-color">
<div className="block">A map update operation initiated by a user has been interrupted.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus#STORAGE_CLOSED">STORAGE_CLOSED</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Indicates that the status cannot be retrieved as the map storage is already closed due to disposal of <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a>.</div>
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
<section className="detail" id="OK">
<h3>OK</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a></span> <span className="element-name">OK</span></div>
<div className="block"><p>All downloaded regions are in a workable state, no issues found.</p></div>
</section>
</li>
<li>
<section className="detail" id="CORRUPTED">
<h3>CORRUPTED</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a></span> <span className="element-name">CORRUPTED</span></div>
<div className="block"><p>One or more downloaded regions failed to open and a repair action should be performed to mitigate this
 issue. All map download and map update operations (except for
 <code>sdk.maploader.MapDownloader.repair_persistent_map</code>) will return <code>sdk.maploader.MapLoaderError.NOT_READY</code>.</p></div>
</section>
</li>
<li>
<section className="detail" id="BROKEN_UPDATE">
<h3>BROKEN_UPDATE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a></span> <span className="element-name">BROKEN_UPDATE</span></div>
<div className="block"><p>Unrecoverable error during construction of pending update parameters.
 Operations such as catalog updates or region downloads will fail.
 The healing procedure is to clean persistent map with <code>sdk.maploader.MapDownloader.clear_persistent_map_storage</code>.</p></div>
</section>
</li>
<li>
<section className="detail" id="MIGRATION_NEEDED">
<h3>MIGRATION_NEEDED</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a></span> <span className="element-name">MIGRATION_NEEDED</span></div>
<div className="block"><p>Indicates that the downloaded regions need to be migrated to a new internal format by calling
 <code>sdk.maploader.MapDownloader.repair_persistent_map</code>. This error is not a result of a data loss,
 nor any data will be lost when performing the repair operation and the map version will stay
 unchanged afterwards.</p></div>
</section>
</li>
<li>
<section className="detail" id="PENDING_UPDATE">
<h3>PENDING_UPDATE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a></span> <span className="element-name">PENDING_UPDATE</span></div>
<div className="block"><p>A map update operation initiated by a user has been interrupted.
 Calls to <code>sdk.maploader.MapDownloader.download_regions</code> and
 <code>sdk.maploader.MapDownloader.delete_regions</code> will fail with <code>sdk.maploader.MapLoaderError.INTERNAL_ERROR</code>.
 To repair a map, call again <code>sdk.maploader.MapUpdater.update_catalog</code> for the affected catalog.
 <code>sdk.maploader.MapUpdater.retrieve_catalogs_update_info</code> returns a list of <code>sdk.maploader.CatalogUpdateInfo</code> items:
 The affected catalog can be identified by the state, which is set to <code>sdk.maploader.CatalogUpdateState.PENDING_UPDATE</code>.
 To know if a map needs to be repaired, check if <code>sdk.maploader.MapLoaderError.PENDING_UPDATE</code> has occurred.</p></div>
</section>
</li>
<li>
<section className="detail" id="INVALID_PATH">
<h3>INVALID_PATH</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a></span> <span className="element-name">INVALID_PATH</span></div>
<div className="block"><p>Unreachable <a href="sdk-for-android-navigate-sdkoptions#cachePath"><code>SDKOptions.cachePath</code></a> or <a href="sdk-for-android-navigate-sdkoptions#persistentMapStoragePath"><code>SDKOptions.persistentMapStoragePath</code></a>.
 Make sure that <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdkoptions" title="class in com.here.sdk.core.engine"><code>SDKOptions</code></a> has accessible <a href="sdk-for-android-navigate-sdkoptions#cachePath"><code>SDKOptions.cachePath</code></a>
 and <a href="sdk-for-android-navigate-sdkoptions#persistentMapStoragePath"><code>SDKOptions.persistentMapStoragePath</code></a></p></div>
</section>
</li>
<li>
<section className="detail" id="INVALID_STATE">
<h3>INVALID_STATE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a></span> <span className="element-name">INVALID_STATE</span></div>
<div className="block"><p>Unrecoverable error during construction of internal map access object.
 The healing procedure is to clean persistent map with <code>sdk.maploader.MapDownloader.clear_persistent_map_storage</code>.</p></div>
</section>
</li>
<li>
<section className="detail" id="STORAGE_CLOSED">
<h3>STORAGE_CLOSED</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a></span> <span className="element-name">STORAGE_CLOSED</span></div>
<div className="block"><p>Indicates that the status cannot be retrieved as the map storage is already closed due to disposal of <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a>.</p></div>
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
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a>[]</span> <span className="element-name">values</span>()</div>
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
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a></span> <span className="element-name">valueOf</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
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
