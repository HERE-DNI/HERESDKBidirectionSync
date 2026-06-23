---
title: "PersistentMapRepairError (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-persistentmaprepairerror"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- PersistentMapRepairError.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">java.lang.Enum</a>&lt;<a href="sdk-for-android-navigate-persistentmaprepairerror" title="enum class in com.here.sdk.maploader">PersistentMapRepairError</a>&gt;
<div class="inheritance">com.here.sdk.maploader.PersistentMapRepairError</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="sdk-for-android-navigate-persistentmaprepairerror" title="enum class in com.here.sdk.maploader">PersistentMapRepairError</a>&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" title="class or interface in java.lang.constant">Constable</a></code></dd>
</dl>

<div class="type-signature"><span class="modifiers">public enum </span><span class="element-name type-name-label">PersistentMapRepairError</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a href="sdk-for-android-navigate-persistentmaprepairerror" title="enum class in com.here.sdk.maploader">PersistentMapRepairError</a>&gt;</span></div>
<div class="block"><p>Specifies possible errors that may result after a map repair operation has been completed.</p></div>
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
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#BROKEN_DB">BROKEN_DB</a></code></div>
<div class="col-last even-row-color">
<div class="block">The persisted map data can't be recovered and all map data was fully deleted.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#BROKEN_UPDATE">BROKEN_UPDATE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Unrecoverable error during construction of pending update parameters.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#INVALID_PATH">INVALID_PATH</a></code></div>
<div class="col-last even-row-color">
<div class="block">Invalid persistent map path.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#NO_JOURNAL">NO_JOURNAL</a></code></div>
<div class="col-last odd-row-color">
<div class="block">It is not possible to retrieve the list of downloaded regions.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#NO_OFFLINE_VERSION">NO_OFFLINE_VERSION</a></code></div>
<div class="col-last even-row-color">
<div class="block">The map data version was not cached.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#OPERATION_AFTER_DISPOSE">OPERATION_AFTER_DISPOSE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Repair is invoked on object connected to the disposed <a href="sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a></div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#PARTIALLY_RESTORED">PARTIALLY_RESTORED</a></code></div>
<div class="col-last even-row-color">
<div class="block">Persistent map is repaired, but some map data is lost.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#UNKNOWN">UNKNOWN</a></code></div>
<div class="col-last odd-row-color">
<div class="block">An unknown error occurred.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-persistentmaprepairerror" title="enum class in com.here.sdk.maploader">PersistentMapRepairError</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#valueOf(java.lang.String)">valueOf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the enum constant of this class with the specified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-persistentmaprepairerror" title="enum class in com.here.sdk.maploader">PersistentMapRepairError</a>[]</code></div>
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
<section class="detail" id="PARTIALLY_RESTORED">
<h3>PARTIALLY_RESTORED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-persistentmaprepairerror" title="enum class in com.here.sdk.maploader">PersistentMapRepairError</a></span> <span class="element-name">PARTIALLY_RESTORED</span></div>
<div class="block"><p>Persistent map is repaired, but some map data is lost. Lost regions marked with a PENDING status.</p></div>
</section>
</li>
<li>
<section class="detail" id="INVALID_PATH">
<h3>INVALID_PATH</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-persistentmaprepairerror" title="enum class in com.here.sdk.maploader">PersistentMapRepairError</a></span> <span class="element-name">INVALID_PATH</span></div>
<div class="block"><p>Invalid persistent map path. The provided path to store the persistent map data doesn't own the required Read/Write (RW) permissions.
 Try to choose a different path with RW permissions.</p></div>
</section>
</li>
<li>
<section class="detail" id="BROKEN_DB">
<h3>BROKEN_DB</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-persistentmaprepairerror" title="enum class in com.here.sdk.maploader">PersistentMapRepairError</a></span> <span class="element-name">BROKEN_DB</span></div>
<div class="block"><p>The persisted map data can't be recovered and all map data was fully deleted. It is recommended, to ask
 the user if they want to try to download the lost regions again.</p></div>
</section>
</li>
<li>
<section class="detail" id="NO_OFFLINE_VERSION">
<h3>NO_OFFLINE_VERSION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-persistentmaprepairerror" title="enum class in com.here.sdk.maploader">PersistentMapRepairError</a></span> <span class="element-name">NO_OFFLINE_VERSION</span></div>
<div class="block"><p>The map data version was not cached. The region list data will be cleared from the persisted storage.
 It is recommended to download the list of downloadable regions again.
 After this it is recommended to try to repair the corrupted map data again.</p></div>
</section>
</li>
<li>
<section class="detail" id="NO_JOURNAL">
<h3>NO_JOURNAL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-persistentmaprepairerror" title="enum class in com.here.sdk.maploader">PersistentMapRepairError</a></span> <span class="element-name">NO_JOURNAL</span></div>
<div class="block"><p>It is not possible to retrieve the list of downloaded regions. The region list data will be cleared from the persisted storage.
 It is recommended to download the list of downloadable regions again.
 After this it is recommended to try to repair the corrupted map data again.</p></div>
</section>
</li>
<li>
<section class="detail" id="BROKEN_UPDATE">
<h3>BROKEN_UPDATE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-persistentmaprepairerror" title="enum class in com.here.sdk.maploader">PersistentMapRepairError</a></span> <span class="element-name">BROKEN_UPDATE</span></div>
<div class="block"><p>Unrecoverable error during construction of pending update parameters.
 Operations such as catalog updates or region downloads will fail.
 The healing procedure is to clean persistent map with <code>sdk.maploader.MapDownloader.clear_persistent_map_storage</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="OPERATION_AFTER_DISPOSE">
<h3>OPERATION_AFTER_DISPOSE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-persistentmaprepairerror" title="enum class in com.here.sdk.maploader">PersistentMapRepairError</a></span> <span class="element-name">OPERATION_AFTER_DISPOSE</span></div>
<div class="block"><p>Repair is invoked on object connected to the disposed <a href="sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a></p></div>
</section>
</li>
<li>
<section class="detail" id="UNKNOWN">
<h3>UNKNOWN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-persistentmaprepairerror" title="enum class in com.here.sdk.maploader">PersistentMapRepairError</a></span> <span class="element-name">UNKNOWN</span></div>
<div class="block"><p>An unknown error occurred. Try to clear the persisted storage by calling <code>sdk.maploader.MapDownloader.clear_persistent_map_storage</code>.
 It is recommended, to ask the user if they want to try to download the lost regions again.</p></div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-persistentmaprepairerror" title="enum class in com.here.sdk.maploader">PersistentMapRepairError</a>[]</span> <span class="element-name">values</span>()</div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-persistentmaprepairerror" title="enum class in com.here.sdk.maploader">PersistentMapRepairError</a></span> <span class="element-name">valueOf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
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






</div>
`
}</HTMLBlock>
