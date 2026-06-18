---
title: "MapLoaderError (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-maploadererror"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapLoaderError.html -->









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-maploader-package-summary">com.here.sdk.maploader</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">java.lang.Enum</a>&lt;<a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a>&gt;
<div class="inheritance">com.here.sdk.maploader.MapLoaderError</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a>&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" title="class or interface in java.lang.constant">Constable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public enum </span><span class="element-name type-name-label">MapLoaderError</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a>&gt;</span></div>
<div class="block"><p>Specifies possible errors that may result from map downloading/prefetching.</p></div>
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
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#ACCESS_DENIED">ACCESS_DENIED</a></code></div>
<div class="col-last even-row-color">
<div class="block">The access is denied due to invalid credentials.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#ALREADY_INSTALLED">ALREADY_INSTALLED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">All tiles of requested regions were already installed, no need for any download.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#BROKEN_UPDATE">BROKEN_UPDATE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Unrecoverable error during construction of pending update parameters.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#CACHE_IO_ERROR">CACHE_IO_ERROR</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A cache IO error occurred.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#CATALOG_CONFIGURATION_ERROR">CATALOG_CONFIGURATION_ERROR</a></code></div>
<div class="col-last even-row-color">
<div class="block">Misconfiguration of catalogs.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#FORBIDDEN">FORBIDDEN</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The operation is forbidden, make sure your credentials grant the necessary permissions.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#INCOMPLETE_DATA">INCOMPLETE_DATA</a></code></div>
<div class="col-last even-row-color">
<div class="block">The data to process is incomplete, failed decoding the tile.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#INTERNAL_ERROR">INTERNAL_ERROR</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Internal error occurred.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#INVALID_ARGUMENT">INVALID_ARGUMENT</a></code></div>
<div class="col-last even-row-color">
<div class="block">The request passed invalid arguments.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#MAP_DATA_ERROR">MAP_DATA_ERROR</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Downloaded map data is invalid or a <code>sdk.maploader.RegionId</code> passed to the method
 <code>sdk.maploader.MapDownloader.delete_regions</code> is incorrect.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#MAP_MANAGER_ERROR">MAP_MANAGER_ERROR</a></code></div>
<div class="col-last even-row-color">
<div class="block">Error occurred inside the map manager and might be related to network issues.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#MIGRATION_REQUIRED">MIGRATION_REQUIRED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Operation on the protected cache cannot be done due to required migration.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#NETWORK_CONNECTION_ERROR">NETWORK_CONNECTION_ERROR</a></code></div>
<div class="col-last even-row-color">
<div class="block">A network connection error has happened.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#NOT_ENOUGH_SPACE">NOT_ENOUGH_SPACE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">There's no sufficient space on the disk to finish operation.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#NOT_READY">NOT_READY</a></code></div>
<div class="col-last even-row-color">
<div class="block">There's a problem with an ongoing download or update: If an operation is in a paused state,
 you can resume or cancel it.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#OFFLINE">OFFLINE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Online operation is not permitted because offline mode is enabled.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#ONLINE_NAVIGATE_ONLY">ONLINE_NAVIGATE_ONLY</a></code></div>
<div class="col-last even-row-color">
<div class="block">This version of HERE SDK does not support the ability to download maps.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#OPERATION_AFTER_DISPOSE">OPERATION_AFTER_DISPOSE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Method is invoked on object connected to the disposed SDKNativeEngine.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#OPERATION_CANCELLED">OPERATION_CANCELLED</a></code></div>
<div class="col-last even-row-color">
<div class="block">The request was cancelled (usually by the user).</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#PARALLEL_REQUEST">PARALLEL_REQUEST</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Parallel request is already running and conflicting with the current one (e.g updating map and deleting map regions)</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#PENDING_UPDATE">PENDING_UPDATE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Map regions update was interrupted.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#PROTECTED_CACHE_CORRUPTED">PROTECTED_CACHE_CORRUPTED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Protected cache is corrupted.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#PROXY_AUTHENTICATION_FAILED">PROXY_AUTHENTICATION_FAILED</a></code></div>
<div class="col-last even-row-color">
<div class="block">Proxy is not authenticated.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#PROXY_SERVER_UNREACHABLE">PROXY_SERVER_UNREACHABLE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Proxy server unreachable.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#REQUEST_LIMIT_REACHED">REQUEST_LIMIT_REACHED</a></code></div>
<div class="col-last even-row-color">
<div class="block">Request limit reached for set a credentials for a particular period of time.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#RESOURCE_NOT_FOUND">RESOURCE_NOT_FOUND</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The requested resource is not found.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#SERVICE_ACCESS_FAILED">SERVICE_ACCESS_FAILED</a></code></div>
<div class="col-last even-row-color">
<div class="block">The conditions to access the service are not satisfied.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#SERVICE_UNAVAILABLE">SERVICE_UNAVAILABLE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The requested service is unavailable.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#TIME_OUT">TIME_OUT</a></code></div>
<div class="col-last even-row-color">
<div class="block">The request exceeded the timeout limit.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#UNEXPECTED_SERVER_RESPONSE">UNEXPECTED_SERVER_RESPONSE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Received unexpected response from the backend.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#UPDATE_BLOCKED_AS_ANOTHER_PENDING">UPDATE_BLOCKED_AS_ANOTHER_PENDING</a></code></div>
<div class="col-last even-row-color">
<div class="block">Catalog update cannot proceed as another catalog update is in PENDING_UPDATE state.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#valueOf(java.lang.String)">valueOf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the enum constant of this class with the specified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a>[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#values()">values</a>()</code></div>
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
<section class="detail" id="RESOURCE_NOT_FOUND">
<h3>RESOURCE_NOT_FOUND</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">RESOURCE_NOT_FOUND</span></div>
<div class="block"><p>The requested resource is not found.</p></div>
</section>
</li>
<li>
<section class="detail" id="NOT_READY">
<h3>NOT_READY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">NOT_READY</span></div>
<div class="block"><p>There's a problem with an ongoing download or update: If an operation is in a paused state,
 you can resume or cancel it. If no operation is in a paused state: Either wait for active
 downloads to finish, or cancel existing <code>sdk.maploader.MapDownloader</code> requests and
 call <code>sdk.maploader.MapDownloader.get_initial_persistent_map_status</code>. If there is a
 problem, call <code>sdk.maploader.MapDownloader.repair_persistent_map</code> to repair before
 continuing with other <code>sdk.maploader.MapDownloader</code> operations.
 This error may occur when an on-going or paused operation prevents the requested task.</p></div>
</section>
</li>
<li>
<section class="detail" id="INVALID_ARGUMENT">
<h3>INVALID_ARGUMENT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">INVALID_ARGUMENT</span></div>
<div class="block"><p>The request passed invalid arguments.</p></div>
</section>
</li>
<li>
<section class="detail" id="OPERATION_CANCELLED">
<h3>OPERATION_CANCELLED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">OPERATION_CANCELLED</span></div>
<div class="block"><p>The request was cancelled (usually by the user).</p></div>
</section>
</li>
<li>
<section class="detail" id="ALREADY_INSTALLED">
<h3>ALREADY_INSTALLED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">ALREADY_INSTALLED</span></div>
<div class="block"><p>All tiles of requested regions were already installed, no need for any download.</p></div>
</section>
</li>
<li>
<section class="detail" id="TIME_OUT">
<h3>TIME_OUT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">TIME_OUT</span></div>
<div class="block"><p>The request exceeded the timeout limit.</p></div>
</section>
</li>
<li>
<section class="detail" id="SERVICE_UNAVAILABLE">
<h3>SERVICE_UNAVAILABLE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">SERVICE_UNAVAILABLE</span></div>
<div class="block"><p>The requested service is unavailable.</p></div>
</section>
</li>
<li>
<section class="detail" id="ACCESS_DENIED">
<h3>ACCESS_DENIED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">ACCESS_DENIED</span></div>
<div class="block"><p>The access is denied due to invalid credentials.</p></div>
</section>
</li>
<li>
<section class="detail" id="REQUEST_LIMIT_REACHED">
<h3>REQUEST_LIMIT_REACHED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">REQUEST_LIMIT_REACHED</span></div>
<div class="block"><p>Request limit reached for set a credentials for a particular period of time.</p></div>
</section>
</li>
<li>
<section class="detail" id="NETWORK_CONNECTION_ERROR">
<h3>NETWORK_CONNECTION_ERROR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">NETWORK_CONNECTION_ERROR</span></div>
<div class="block"><p>A network connection error has happened.</p></div>
</section>
</li>
<li>
<section class="detail" id="FORBIDDEN">
<h3>FORBIDDEN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">FORBIDDEN</span></div>
<div class="block"><p>The operation is forbidden, make sure your credentials grant the necessary permissions.</p></div>
</section>
</li>
<li>
<section class="detail" id="MAP_DATA_ERROR">
<h3>MAP_DATA_ERROR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">MAP_DATA_ERROR</span></div>
<div class="block"><p>Downloaded map data is invalid or a <code>sdk.maploader.RegionId</code> passed to the method
 <code>sdk.maploader.MapDownloader.delete_regions</code> is incorrect.</p></div>
</section>
</li>
<li>
<section class="detail" id="UNEXPECTED_SERVER_RESPONSE">
<h3>UNEXPECTED_SERVER_RESPONSE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">UNEXPECTED_SERVER_RESPONSE</span></div>
<div class="block"><p>Received unexpected response from the backend. It means the response is malformed or
 server returned an internal error. Try repeating the request.</p></div>
</section>
</li>
<li>
<section class="detail" id="MAP_MANAGER_ERROR">
<h3>MAP_MANAGER_ERROR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">MAP_MANAGER_ERROR</span></div>
<div class="block"><p>Error occurred inside the map manager and might be related to network issues. Try
 repeating the request.</p></div>
</section>
</li>
<li>
<section class="detail" id="INCOMPLETE_DATA">
<h3>INCOMPLETE_DATA</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">INCOMPLETE_DATA</span></div>
<div class="block"><p>The data to process is incomplete, failed decoding the tile.</p></div>
</section>
</li>
<li>
<section class="detail" id="SERVICE_ACCESS_FAILED">
<h3>SERVICE_ACCESS_FAILED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">SERVICE_ACCESS_FAILED</span></div>
<div class="block"><p>The conditions to access the service are not satisfied. Check if correct
 <code>sdk.maploader.RegionId</code> was passed to <code>sdk.maploader.MapDownloader.download_regions</code> or
 download for passed <code>sdk.maploader.RegionId</code> already started. Further control for
 started download must be performed through <code>sdk.maploader.MapDownloaderTask</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="INTERNAL_ERROR">
<h3>INTERNAL_ERROR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">INTERNAL_ERROR</span></div>
<div class="block"><p>Internal error occurred.</p></div>
</section>
</li>
<li>
<section class="detail" id="OFFLINE">
<h3>OFFLINE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">OFFLINE</span></div>
<div class="block"><p>Online operation is not permitted because offline mode is enabled.</p></div>
</section>
</li>
<li>
<section class="detail" id="CACHE_IO_ERROR">
<h3>CACHE_IO_ERROR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">CACHE_IO_ERROR</span></div>
<div class="block"><p>A cache IO error occurred.</p></div>
</section>
</li>
<li>
<section class="detail" id="PROTECTED_CACHE_CORRUPTED">
<h3>PROTECTED_CACHE_CORRUPTED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">PROTECTED_CACHE_CORRUPTED</span></div>
<div class="block"><p>Protected cache is corrupted. It can be a result of downloading the map in the background
 and the OS killing the application at that time. Use method
 <code>sdk.maploader.MapDownloader.get_initial_persistent_map_status</code> to get the status of the
 map and method repair_persistent_map in the MapDownloader to try to fix the cache if it is
 broken.</p></div>
</section>
</li>
<li>
<section class="detail" id="MIGRATION_REQUIRED">
<h3>MIGRATION_REQUIRED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">MIGRATION_REQUIRED</span></div>
<div class="block"><p>Operation on the protected cache cannot be done due to required migration.
 Call <code>sdk.maploader.MapDownloader.repair_persistent_map</code> to perform migration.</p></div>
</section>
</li>
<li>
<section class="detail" id="OPERATION_AFTER_DISPOSE">
<h3>OPERATION_AFTER_DISPOSE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">OPERATION_AFTER_DISPOSE</span></div>
<div class="block"><p>Method is invoked on object connected to the disposed SDKNativeEngine.</p></div>
</section>
</li>
<li>
<section class="detail" id="CATALOG_CONFIGURATION_ERROR">
<h3>CATALOG_CONFIGURATION_ERROR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">CATALOG_CONFIGURATION_ERROR</span></div>
<div class="block"><p>Misconfiguration of catalogs.
 This error may occur when <code>sdk.core.engine.CatalogConfiguration</code> is misconfigured and
 cannot be used for any operation with <code>MapDownloader</code> or <code>MapUpdater</code>.
 Verify <a href="sdk-for-android-navigate-sdkoptions#catalogConfigurations"><code>SDKOptions.catalogConfigurations</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="PENDING_UPDATE">
<h3>PENDING_UPDATE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">PENDING_UPDATE</span></div>
<div class="block"><p>Map regions update was interrupted. Indicates that the cache state is wrong after an
 update that was finished not in correct way (e.g sudden app shutdown).
 Prefetching or removing of map regions are blocked until
 the update has been completed successfully.</p></div>
</section>
</li>
<li>
<section class="detail" id="UPDATE_BLOCKED_AS_ANOTHER_PENDING">
<h3>UPDATE_BLOCKED_AS_ANOTHER_PENDING</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">UPDATE_BLOCKED_AS_ANOTHER_PENDING</span></div>
<div class="block"><p>Catalog update cannot proceed as another catalog update is in PENDING_UPDATE state.
 Update the catalog in PENDING_UPDATE state first, before trying to update another catalog.</p></div>
</section>
</li>
<li>
<section class="detail" id="BROKEN_UPDATE">
<h3>BROKEN_UPDATE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">BROKEN_UPDATE</span></div>
<div class="block"><p>Unrecoverable error during construction of pending update parameters.
 Operations such as catalog updates or region downloads will fail.
 The healing procedure is to clean persistent map with <code>sdk.maploader.MapDownloader.clear_persistent_map_storage</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="PARALLEL_REQUEST">
<h3>PARALLEL_REQUEST</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">PARALLEL_REQUEST</span></div>
<div class="block"><p>Parallel request is already running and conflicting with the current one (e.g updating map and deleting map regions)</p></div>
</section>
</li>
<li>
<section class="detail" id="PROXY_AUTHENTICATION_FAILED">
<h3>PROXY_AUTHENTICATION_FAILED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">PROXY_AUTHENTICATION_FAILED</span></div>
<div class="block"><p>Proxy is not authenticated. Check your proxy credentials.</p></div>
</section>
</li>
<li>
<section class="detail" id="PROXY_SERVER_UNREACHABLE">
<h3>PROXY_SERVER_UNREACHABLE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">PROXY_SERVER_UNREACHABLE</span></div>
<div class="block"><p>Proxy server unreachable.</p></div>
</section>
</li>
<li>
<section class="detail" id="NOT_ENOUGH_SPACE">
<h3>NOT_ENOUGH_SPACE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">NOT_ENOUGH_SPACE</span></div>
<div class="block"><p>There's no sufficient space on the disk to finish operation.
 For offline maps operation (download or update), it means that
 there's not enough space on the device.
 For prefetch operations, it means that there's not enough space
 in the mutable cache to store the prefetched data.</p></div>
</section>
</li>
<li>
<section class="detail" id="ONLINE_NAVIGATE_ONLY">
<h3>ONLINE_NAVIGATE_ONLY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">ONLINE_NAVIGATE_ONLY</span></div>
<div class="block"><p>This version of HERE SDK does not support the ability to download maps.
 Contact the sales team to get access to the full version.</p></div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a>[]</span> <span class="element-name">values</span>()</div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span class="element-name">valueOf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
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
`
}</HTMLBlock>
