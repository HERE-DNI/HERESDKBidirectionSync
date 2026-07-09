---
title: "MapLoaderError (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-maploadererror"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapLoaderError.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.maploader</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">java.lang.Enum</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a>&gt;
<div className="inheritance">com.here.sdk.maploader.MapLoaderError</div>
</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a>&gt;</code>, <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" title="class or interface in java.lang.constant">Constable</a></code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public enum </span><span className="element-name type-name-label">MapLoaderError</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a>&gt;</span></div>
<div className="block"><p>Specifies possible errors that may result from map downloading/prefetching.</p></div>
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


<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#ACCESS_DENIED">ACCESS_DENIED</a></code></div>
<div className="col-last even-row-color">
<div className="block">The access is denied due to invalid credentials.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#ALREADY_INSTALLED">ALREADY_INSTALLED</a></code></div>
<div className="col-last odd-row-color">
<div className="block">All tiles of requested regions were already installed, no need for any download.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#BROKEN_UPDATE">BROKEN_UPDATE</a></code></div>
<div className="col-last even-row-color">
<div className="block">Unrecoverable error during construction of pending update parameters.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#CACHE_IO_ERROR">CACHE_IO_ERROR</a></code></div>
<div className="col-last odd-row-color">
<div className="block">A cache IO error occurred.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#CATALOG_CONFIGURATION_ERROR">CATALOG_CONFIGURATION_ERROR</a></code></div>
<div className="col-last even-row-color">
<div className="block">Misconfiguration of catalogs.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#FORBIDDEN">FORBIDDEN</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The operation is forbidden, make sure your credentials grant the necessary permissions.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#INCOMPLETE_DATA">INCOMPLETE_DATA</a></code></div>
<div className="col-last even-row-color">
<div className="block">The data to process is incomplete, failed decoding the tile.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#INTERNAL_ERROR">INTERNAL_ERROR</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Internal error occurred.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#INVALID_ARGUMENT">INVALID_ARGUMENT</a></code></div>
<div className="col-last even-row-color">
<div className="block">The request passed invalid arguments.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#MAP_DATA_ERROR">MAP_DATA_ERROR</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Downloaded map data is invalid or a <code>sdk.maploader.RegionId</code> passed to the method
 <code>sdk.maploader.MapDownloader.delete_regions</code> is incorrect.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#MAP_MANAGER_ERROR">MAP_MANAGER_ERROR</a></code></div>
<div className="col-last even-row-color">
<div className="block">Error occurred inside the map manager and might be related to network issues.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#MIGRATION_REQUIRED">MIGRATION_REQUIRED</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Operation on the protected cache cannot be done due to required migration.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#NETWORK_CONNECTION_ERROR">NETWORK_CONNECTION_ERROR</a></code></div>
<div className="col-last even-row-color">
<div className="block">A network connection error has happened.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#NOT_ENOUGH_SPACE">NOT_ENOUGH_SPACE</a></code></div>
<div className="col-last odd-row-color">
<div className="block">There's no sufficient space on the disk to finish operation.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#NOT_READY">NOT_READY</a></code></div>
<div className="col-last even-row-color">
<div className="block">There's a problem with an ongoing download or update: If an operation is in a paused state,
 you can resume or cancel it.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#OFFLINE">OFFLINE</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Online operation is not permitted because offline mode is enabled.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#ONLINE_NAVIGATE_ONLY">ONLINE_NAVIGATE_ONLY</a></code></div>
<div className="col-last even-row-color">
<div className="block">This version of HERE SDK does not support the ability to download maps.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#OPERATION_AFTER_DISPOSE">OPERATION_AFTER_DISPOSE</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Method is invoked on object connected to the disposed SDKNativeEngine.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#OPERATION_CANCELLED">OPERATION_CANCELLED</a></code></div>
<div className="col-last even-row-color">
<div className="block">The request was cancelled (usually by the user).</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#PARALLEL_REQUEST">PARALLEL_REQUEST</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Parallel request is already running and conflicting with the current one (e.g updating map and deleting map regions)</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#PENDING_UPDATE">PENDING_UPDATE</a></code></div>
<div className="col-last even-row-color">
<div className="block">Map regions update was interrupted.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#PROTECTED_CACHE_CORRUPTED">PROTECTED_CACHE_CORRUPTED</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Protected cache is corrupted.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#PROXY_AUTHENTICATION_FAILED">PROXY_AUTHENTICATION_FAILED</a></code></div>
<div className="col-last even-row-color">
<div className="block">Proxy is not authenticated.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#PROXY_SERVER_UNREACHABLE">PROXY_SERVER_UNREACHABLE</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Proxy server unreachable.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#REQUEST_LIMIT_REACHED">REQUEST_LIMIT_REACHED</a></code></div>
<div className="col-last even-row-color">
<div className="block">Request limit reached for set a credentials for a particular period of time.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#RESOURCE_NOT_FOUND">RESOURCE_NOT_FOUND</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The requested resource is not found.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#SERVICE_ACCESS_FAILED">SERVICE_ACCESS_FAILED</a></code></div>
<div className="col-last even-row-color">
<div className="block">The conditions to access the service are not satisfied.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#SERVICE_UNAVAILABLE">SERVICE_UNAVAILABLE</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The requested service is unavailable.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#TIME_OUT">TIME_OUT</a></code></div>
<div className="col-last even-row-color">
<div className="block">The request exceeded the timeout limit.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#UNEXPECTED_SERVER_RESPONSE">UNEXPECTED_SERVER_RESPONSE</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Received unexpected response from the backend.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror#UPDATE_BLOCKED_AS_ANOTHER_PENDING">UPDATE_BLOCKED_AS_ANOTHER_PENDING</a></code></div>
<div className="col-last even-row-color">
<div className="block">Catalog update cannot proceed as another catalog update is in PENDING_UPDATE state.</div>
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
<section className="detail" id="RESOURCE_NOT_FOUND">
<h3>RESOURCE_NOT_FOUND</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span className="element-name">RESOURCE_NOT_FOUND</span></div>
<div className="block"><p>The requested resource is not found.</p></div>
</section>
</li>
<li>
<section className="detail" id="NOT_READY">
<h3>NOT_READY</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span className="element-name">NOT_READY</span></div>
<div className="block"><p>There's a problem with an ongoing download or update: If an operation is in a paused state,
 you can resume or cancel it. If no operation is in a paused state: Either wait for active
 downloads to finish, or cancel existing <code>sdk.maploader.MapDownloader</code> requests and
 call <code>sdk.maploader.MapDownloader.get_initial_persistent_map_status</code>. If there is a
 problem, call <code>sdk.maploader.MapDownloader.repair_persistent_map</code> to repair before
 continuing with other <code>sdk.maploader.MapDownloader</code> operations.
 This error may occur when an on-going or paused operation prevents the requested task.</p></div>
</section>
</li>
<li>
<section className="detail" id="INVALID_ARGUMENT">
<h3>INVALID_ARGUMENT</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span className="element-name">INVALID_ARGUMENT</span></div>
<div className="block"><p>The request passed invalid arguments.</p></div>
</section>
</li>
<li>
<section className="detail" id="OPERATION_CANCELLED">
<h3>OPERATION_CANCELLED</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span className="element-name">OPERATION_CANCELLED</span></div>
<div className="block"><p>The request was cancelled (usually by the user).</p></div>
</section>
</li>
<li>
<section className="detail" id="ALREADY_INSTALLED">
<h3>ALREADY_INSTALLED</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span className="element-name">ALREADY_INSTALLED</span></div>
<div className="block"><p>All tiles of requested regions were already installed, no need for any download.</p></div>
</section>
</li>
<li>
<section className="detail" id="TIME_OUT">
<h3>TIME_OUT</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span className="element-name">TIME_OUT</span></div>
<div className="block"><p>The request exceeded the timeout limit.</p></div>
</section>
</li>
<li>
<section className="detail" id="SERVICE_UNAVAILABLE">
<h3>SERVICE_UNAVAILABLE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span className="element-name">SERVICE_UNAVAILABLE</span></div>
<div className="block"><p>The requested service is unavailable.</p></div>
</section>
</li>
<li>
<section className="detail" id="ACCESS_DENIED">
<h3>ACCESS_DENIED</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span className="element-name">ACCESS_DENIED</span></div>
<div className="block"><p>The access is denied due to invalid credentials.</p></div>
</section>
</li>
<li>
<section className="detail" id="REQUEST_LIMIT_REACHED">
<h3>REQUEST_LIMIT_REACHED</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span className="element-name">REQUEST_LIMIT_REACHED</span></div>
<div className="block"><p>Request limit reached for set a credentials for a particular period of time.</p></div>
</section>
</li>
<li>
<section className="detail" id="NETWORK_CONNECTION_ERROR">
<h3>NETWORK_CONNECTION_ERROR</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span className="element-name">NETWORK_CONNECTION_ERROR</span></div>
<div className="block"><p>A network connection error has happened.</p></div>
</section>
</li>
<li>
<section className="detail" id="FORBIDDEN">
<h3>FORBIDDEN</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span className="element-name">FORBIDDEN</span></div>
<div className="block"><p>The operation is forbidden, make sure your credentials grant the necessary permissions.</p></div>
</section>
</li>
<li>
<section className="detail" id="MAP_DATA_ERROR">
<h3>MAP_DATA_ERROR</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span className="element-name">MAP_DATA_ERROR</span></div>
<div className="block"><p>Downloaded map data is invalid or a <code>sdk.maploader.RegionId</code> passed to the method
 <code>sdk.maploader.MapDownloader.delete_regions</code> is incorrect.</p></div>
</section>
</li>
<li>
<section className="detail" id="UNEXPECTED_SERVER_RESPONSE">
<h3>UNEXPECTED_SERVER_RESPONSE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span className="element-name">UNEXPECTED_SERVER_RESPONSE</span></div>
<div className="block"><p>Received unexpected response from the backend. It means the response is malformed or
 server returned an internal error. Try repeating the request.</p></div>
</section>
</li>
<li>
<section className="detail" id="MAP_MANAGER_ERROR">
<h3>MAP_MANAGER_ERROR</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span className="element-name">MAP_MANAGER_ERROR</span></div>
<div className="block"><p>Error occurred inside the map manager and might be related to network issues. Try
 repeating the request.</p></div>
</section>
</li>
<li>
<section className="detail" id="INCOMPLETE_DATA">
<h3>INCOMPLETE_DATA</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span className="element-name">INCOMPLETE_DATA</span></div>
<div className="block"><p>The data to process is incomplete, failed decoding the tile.</p></div>
</section>
</li>
<li>
<section className="detail" id="SERVICE_ACCESS_FAILED">
<h3>SERVICE_ACCESS_FAILED</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span className="element-name">SERVICE_ACCESS_FAILED</span></div>
<div className="block"><p>The conditions to access the service are not satisfied. Check if correct
 <code>sdk.maploader.RegionId</code> was passed to <code>sdk.maploader.MapDownloader.download_regions</code> or
 download for passed <code>sdk.maploader.RegionId</code> already started. Further control for
 started download must be performed through <code>sdk.maploader.MapDownloaderTask</code>.</p></div>
</section>
</li>
<li>
<section className="detail" id="INTERNAL_ERROR">
<h3>INTERNAL_ERROR</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span className="element-name">INTERNAL_ERROR</span></div>
<div className="block"><p>Internal error occurred.</p></div>
</section>
</li>
<li>
<section className="detail" id="OFFLINE">
<h3>OFFLINE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span className="element-name">OFFLINE</span></div>
<div className="block"><p>Online operation is not permitted because offline mode is enabled.</p></div>
</section>
</li>
<li>
<section className="detail" id="CACHE_IO_ERROR">
<h3>CACHE_IO_ERROR</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span className="element-name">CACHE_IO_ERROR</span></div>
<div className="block"><p>A cache IO error occurred.</p></div>
</section>
</li>
<li>
<section className="detail" id="PROTECTED_CACHE_CORRUPTED">
<h3>PROTECTED_CACHE_CORRUPTED</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span className="element-name">PROTECTED_CACHE_CORRUPTED</span></div>
<div className="block"><p>Protected cache is corrupted. It can be a result of downloading the map in the background
 and the OS killing the application at that time. Use method
 <code>sdk.maploader.MapDownloader.get_initial_persistent_map_status</code> to get the status of the
 map and method repair_persistent_map in the MapDownloader to try to fix the cache if it is
 broken.</p></div>
</section>
</li>
<li>
<section className="detail" id="MIGRATION_REQUIRED">
<h3>MIGRATION_REQUIRED</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span className="element-name">MIGRATION_REQUIRED</span></div>
<div className="block"><p>Operation on the protected cache cannot be done due to required migration.
 Call <code>sdk.maploader.MapDownloader.repair_persistent_map</code> to perform migration.</p></div>
</section>
</li>
<li>
<section className="detail" id="OPERATION_AFTER_DISPOSE">
<h3>OPERATION_AFTER_DISPOSE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span className="element-name">OPERATION_AFTER_DISPOSE</span></div>
<div className="block"><p>Method is invoked on object connected to the disposed SDKNativeEngine.</p></div>
</section>
</li>
<li>
<section className="detail" id="CATALOG_CONFIGURATION_ERROR">
<h3>CATALOG_CONFIGURATION_ERROR</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span className="element-name">CATALOG_CONFIGURATION_ERROR</span></div>
<div className="block"><p>Misconfiguration of catalogs.
 This error may occur when <code>sdk.core.engine.CatalogConfiguration</code> is misconfigured and
 cannot be used for any operation with <code>MapDownloader</code> or <code>MapUpdater</code>.
 Verify <a href="sdk-for-android-navigate-sdkoptions#catalogConfigurations"><code>SDKOptions.catalogConfigurations</code></a>.</p></div>
</section>
</li>
<li>
<section className="detail" id="PENDING_UPDATE">
<h3>PENDING_UPDATE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span className="element-name">PENDING_UPDATE</span></div>
<div className="block"><p>Map regions update was interrupted. Indicates that the cache state is wrong after an
 update that was finished not in correct way (e.g sudden app shutdown).
 Prefetching or removing of map regions are blocked until
 the update has been completed successfully.</p></div>
</section>
</li>
<li>
<section className="detail" id="UPDATE_BLOCKED_AS_ANOTHER_PENDING">
<h3>UPDATE_BLOCKED_AS_ANOTHER_PENDING</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span className="element-name">UPDATE_BLOCKED_AS_ANOTHER_PENDING</span></div>
<div className="block"><p>Catalog update cannot proceed as another catalog update is in PENDING_UPDATE state.
 Update the catalog in PENDING_UPDATE state first, before trying to update another catalog.</p></div>
</section>
</li>
<li>
<section className="detail" id="BROKEN_UPDATE">
<h3>BROKEN_UPDATE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span className="element-name">BROKEN_UPDATE</span></div>
<div className="block"><p>Unrecoverable error during construction of pending update parameters.
 Operations such as catalog updates or region downloads will fail.
 The healing procedure is to clean persistent map with <code>sdk.maploader.MapDownloader.clear_persistent_map_storage</code>.</p></div>
</section>
</li>
<li>
<section className="detail" id="PARALLEL_REQUEST">
<h3>PARALLEL_REQUEST</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span className="element-name">PARALLEL_REQUEST</span></div>
<div className="block"><p>Parallel request is already running and conflicting with the current one (e.g updating map and deleting map regions)</p></div>
</section>
</li>
<li>
<section className="detail" id="PROXY_AUTHENTICATION_FAILED">
<h3>PROXY_AUTHENTICATION_FAILED</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span className="element-name">PROXY_AUTHENTICATION_FAILED</span></div>
<div className="block"><p>Proxy is not authenticated. Check your proxy credentials.</p></div>
</section>
</li>
<li>
<section className="detail" id="PROXY_SERVER_UNREACHABLE">
<h3>PROXY_SERVER_UNREACHABLE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span className="element-name">PROXY_SERVER_UNREACHABLE</span></div>
<div className="block"><p>Proxy server unreachable.</p></div>
</section>
</li>
<li>
<section className="detail" id="NOT_ENOUGH_SPACE">
<h3>NOT_ENOUGH_SPACE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span className="element-name">NOT_ENOUGH_SPACE</span></div>
<div className="block"><p>There's no sufficient space on the disk to finish operation.
 For offline maps operation (download or update), it means that
 there's not enough space on the device.
 For prefetch operations, it means that there's not enough space
 in the mutable cache to store the prefetched data.</p></div>
</section>
</li>
<li>
<section className="detail" id="ONLINE_NAVIGATE_ONLY">
<h3>ONLINE_NAVIGATE_ONLY</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span className="element-name">ONLINE_NAVIGATE_ONLY</span></div>
<div className="block"><p>This version of HERE SDK does not support the ability to download maps.
 Contact the sales team to get access to the full version.</p></div>
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
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a>[]</span> <span className="element-name">values</span>()</div>
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
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></span> <span className="element-name">valueOf</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
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
