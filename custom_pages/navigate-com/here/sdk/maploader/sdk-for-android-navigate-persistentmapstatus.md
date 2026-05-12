---
title: "PersistentMapStatus (API Reference)"
slug: "sdk-for-android-navigate-persistentmapstatus"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- PersistentMapStatus.html -->
<!DOCTYPE HTML>

<html lang="en">

<body class="class-declaration-page">


<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-navigate-index">Overview</a></li>
<li><a href="sdk-for-android-navigate-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-navigate-package-tree">Tree</a></li>
<li><a href="sdk-for-android-navigate-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-navigate-index-all">Index</a></li>
<li><a href="sdk-for-android-navigate-help-doc#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li><a href="#nested-class-summary">Nested</a> | </li>
<li><a href="#enum-constant-summary">Enum Constants</a> | </li>
<li>Field | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li><a href="#enum-constant-detail">Enum Constants</a> | </li>
<li>Field | </li>
<li><a href="#method-detail">Method</a></li>
</ul>
</div>

</div>
<!-- ========= END OF TOP NAVBAR ========= -->
<span class="skip-nav" id="skip-navbar-top"></span></nav>
</header>
<div class="flex-content">
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.maploader</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">java.lang.Enum</a>&lt;<a href="sdk-for-android-navigate-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a>&gt;
<div class="inheritance">com.here.sdk.maploader.PersistentMapStatus</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="sdk-for-android-navigate-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a>&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" title="class or interface in java.lang.constant">Constable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public enum </span><span class="element-name type-name-label">PersistentMapStatus</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a href="sdk-for-android-navigate-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a>&gt;</span></div>
<div class="block"><p>Specifies possible statuses of the already downloaded map regions as a whole.
 Note: This can be valid only for a single region in case of a <a href="#CORRUPTED"><code>CORRUPTED</code></a> state.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">

<div class="inherited-list">

<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">Enum.EnumDesc</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">E</a> extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">E</a>&gt;&gt;</code></div>
</section>
</li>
<!-- =========== ENUM CONSTANT SUMMARY =========== -->
<li>
<section class="constants-summary" id="enum-constant-summary">

<div class="caption"><span>Enum Constants</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Enum Constant</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#BROKEN_UPDATE">BROKEN_UPDATE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Unrecoverable error during construction of pending update parameters.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#CORRUPTED">CORRUPTED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">One or more downloaded regions failed to open and a repair action should be performed to mitigate this
 issue.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#INVALID_PATH">INVALID_PATH</a></code></div>
<div class="col-last even-row-color">
<div class="block">Unreachable <a href="sdk-for-android-navigate-core-engine-sdkoptions#cachePath"><code>SDKOptions.cachePath</code></a> or <a href="sdk-for-android-navigate-core-engine-sdkoptions#persistentMapStoragePath"><code>SDKOptions.persistentMapStoragePath</code></a>.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#INVALID_STATE">INVALID_STATE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Unrecoverable error during construction of internal map access object.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#MIGRATION_NEEDED">MIGRATION_NEEDED</a></code></div>
<div class="col-last even-row-color">
<div class="block">Indicates that the downloaded regions need to be migrated to a new internal format by calling
 <code>sdk.maploader.MapDownloader.repair_persistent_map</code>.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#OK">OK</a></code></div>
<div class="col-last odd-row-color">
<div class="block">All downloaded regions are in a workable state, no issues found.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#PENDING_UPDATE">PENDING_UPDATE</a></code></div>
<div class="col-last even-row-color">
<div class="block">A map update operation initiated by a user has been interrupted.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#STORAGE_CLOSED">STORAGE_CLOSED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Indicates that the status cannot be retrieved as the map storage is already closed due to disposal of <a href="sdk-for-android-navigate-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a>.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#valueOf(java.lang.String)">valueOf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the enum constant of this class with the specified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a>[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#values()">values</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns an array containing the constants of this enum class, in
the order they are declared.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Enum">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)" title="class or interface in java.lang">compareTo</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()" title="class or interface in java.lang">describeConstable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()" title="class or interface in java.lang">getDeclaringClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()" title="class or interface in java.lang">name</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()" title="class or interface in java.lang">ordinal</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String)" title="class or interface in java.lang">valueOf</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ ENUM CONSTANT DETAIL =========== -->
<li>
<section class="constant-details" id="enum-constant-detail">

<ul class="member-list">
<li>
<section class="detail" id="OK">
<h3>OK</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a></span> <span class="element-name">OK</span></div>
<div class="block"><p>All downloaded regions are in a workable state, no issues found.</p></div>
</section>
</li>
<li>
<section class="detail" id="CORRUPTED">
<h3>CORRUPTED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a></span> <span class="element-name">CORRUPTED</span></div>
<div class="block"><p>One or more downloaded regions failed to open and a repair action should be performed to mitigate this
 issue. All map download and map update operations (except for
 <code>sdk.maploader.MapDownloader.repair_persistent_map</code>) will return <code>sdk.maploader.MapLoaderError.NOT_READY</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="BROKEN_UPDATE">
<h3>BROKEN_UPDATE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a></span> <span class="element-name">BROKEN_UPDATE</span></div>
<div class="block"><p>Unrecoverable error during construction of pending update parameters.
 Operations such as catalog updates or region downloads will fail.
 The healing procedure is to clean persistent map with <code>sdk.maploader.MapDownloader.clear_persistent_map_storage</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="MIGRATION_NEEDED">
<h3>MIGRATION_NEEDED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a></span> <span class="element-name">MIGRATION_NEEDED</span></div>
<div class="block"><p>Indicates that the downloaded regions need to be migrated to a new internal format by calling
 <code>sdk.maploader.MapDownloader.repair_persistent_map</code>. This error is not a result of a data loss,
 nor any data will be lost when performing the repair operation and the map version will stay
 unchanged afterwards.</p></div>
</section>
</li>
<li>
<section class="detail" id="PENDING_UPDATE">
<h3>PENDING_UPDATE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a></span> <span class="element-name">PENDING_UPDATE</span></div>
<div class="block"><p>A map update operation initiated by a user has been interrupted.
 Calls to <code>sdk.maploader.MapDownloader.download_regions</code> and
 <code>sdk.maploader.MapDownloader.delete_regions</code> will fail with <code>sdk.maploader.MapLoaderError.INTERNAL_ERROR</code>.
 To repair a map, call again <code>sdk.maploader.MapUpdater.update_catalog</code> for the affected catalog.
 <code>sdk.maploader.MapUpdater.retrieve_catalogs_update_info</code> returns a list of <code>sdk.maploader.CatalogUpdateInfo</code> items:
 The affected catalog can be identified by the state, which is set to <code>sdk.maploader.CatalogUpdateState.PENDING_UPDATE</code>.
 To know if a map needs to be repaired, check if <code>sdk.maploader.MapLoaderError.PENDING_UPDATE</code> has occurred.</p></div>
</section>
</li>
<li>
<section class="detail" id="INVALID_PATH">
<h3>INVALID_PATH</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a></span> <span class="element-name">INVALID_PATH</span></div>
<div class="block"><p>Unreachable <a href="sdk-for-android-navigate-core-engine-sdkoptions#cachePath"><code>SDKOptions.cachePath</code></a> or <a href="sdk-for-android-navigate-core-engine-sdkoptions#persistentMapStoragePath"><code>SDKOptions.persistentMapStoragePath</code></a>.
 Make sure that <a href="sdk-for-android-navigate-core-engine-sdkoptions" title="class in com.here.sdk.core.engine"><code>SDKOptions</code></a> has accessible <a href="sdk-for-android-navigate-core-engine-sdkoptions#cachePath"><code>SDKOptions.cachePath</code></a>
 and <a href="sdk-for-android-navigate-core-engine-sdkoptions#persistentMapStoragePath"><code>SDKOptions.persistentMapStoragePath</code></a></p></div>
</section>
</li>
<li>
<section class="detail" id="INVALID_STATE">
<h3>INVALID_STATE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a></span> <span class="element-name">INVALID_STATE</span></div>
<div class="block"><p>Unrecoverable error during construction of internal map access object.
 The healing procedure is to clean persistent map with <code>sdk.maploader.MapDownloader.clear_persistent_map_storage</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="STORAGE_CLOSED">
<h3>STORAGE_CLOSED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a></span> <span class="element-name">STORAGE_CLOSED</span></div>
<div class="block"><p>Indicates that the status cannot be retrieved as the map storage is already closed due to disposal of <a href="sdk-for-android-navigate-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a>.</p></div>
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
<section class="detail" id="values()">
<h3>values</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a>[]</span> <span class="element-name">values</span>()</div>
<div class="block">Returns an array containing the constants of this enum class, in
the order they are declared.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>an array containing the constants of this enum class, in the order they are declared</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="valueOf(java.lang.String)">
<h3>valueOf</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a></span> <span class="element-name">valueOf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Returns the enum constant of this class with the specified name.
The string must match <i>exactly</i> an identifier used to declare an
enum constant in this class.  (Extraneous whitespace characters are 
not permitted.)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the name of the enum constant to be returned.</dd>
<dt>Returns:</dt>
<dd>the enum constant with the specified name</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if this enum class has no constant with the specified name</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html" title="class or interface in java.lang">NullPointerException</a></code> - if the argument is null</dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
</div>
</div>
</body>
</html>

</div>
`
}</HTMLBlock>
