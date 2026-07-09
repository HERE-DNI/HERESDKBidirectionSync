---
title: "PersistentMapRepairError (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-persistentmaprepairerror"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- PersistentMapRepairError.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.maploader</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">java.lang.Enum</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmaprepairerror" title="enum class in com.here.sdk.maploader">PersistentMapRepairError</a>&gt;
<div className="inheritance">com.here.sdk.maploader.PersistentMapRepairError</div>
</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmaprepairerror" title="enum class in com.here.sdk.maploader">PersistentMapRepairError</a>&gt;</code>, <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" title="class or interface in java.lang.constant">Constable</a></code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public enum </span><span className="element-name type-name-label">PersistentMapRepairError</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmaprepairerror" title="enum class in com.here.sdk.maploader">PersistentMapRepairError</a>&gt;</span></div>
<div className="block"><p>Specifies possible errors that may result after a map repair operation has been completed.</p></div>
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


<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmaprepairerror#BROKEN_DB">BROKEN_DB</a></code></div>
<div className="col-last even-row-color">
<div className="block">The persisted map data can't be recovered and all map data was fully deleted.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmaprepairerror#BROKEN_UPDATE">BROKEN_UPDATE</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Unrecoverable error during construction of pending update parameters.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmaprepairerror#INVALID_PATH">INVALID_PATH</a></code></div>
<div className="col-last even-row-color">
<div className="block">Invalid persistent map path.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmaprepairerror#NO_JOURNAL">NO_JOURNAL</a></code></div>
<div className="col-last odd-row-color">
<div className="block">It is not possible to retrieve the list of downloaded regions.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmaprepairerror#NO_OFFLINE_VERSION">NO_OFFLINE_VERSION</a></code></div>
<div className="col-last even-row-color">
<div className="block">The map data version was not cached.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmaprepairerror#OPERATION_AFTER_DISPOSE">OPERATION_AFTER_DISPOSE</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Repair is invoked on object connected to the disposed <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a></div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmaprepairerror#PARTIALLY_RESTORED">PARTIALLY_RESTORED</a></code></div>
<div className="col-last even-row-color">
<div className="block">Persistent map is repaired, but some map data is lost.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmaprepairerror#UNKNOWN">UNKNOWN</a></code></div>
<div className="col-last odd-row-color">
<div className="block">An unknown error occurred.</div>
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
<section className="detail" id="PARTIALLY_RESTORED">
<h3>PARTIALLY_RESTORED</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmaprepairerror" title="enum class in com.here.sdk.maploader">PersistentMapRepairError</a></span> <span className="element-name">PARTIALLY_RESTORED</span></div>
<div className="block"><p>Persistent map is repaired, but some map data is lost. Lost regions marked with a PENDING status.</p></div>
</section>
</li>
<li>
<section className="detail" id="INVALID_PATH">
<h3>INVALID_PATH</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmaprepairerror" title="enum class in com.here.sdk.maploader">PersistentMapRepairError</a></span> <span className="element-name">INVALID_PATH</span></div>
<div className="block"><p>Invalid persistent map path. The provided path to store the persistent map data doesn't own the required Read/Write (RW) permissions.
 Try to choose a different path with RW permissions.</p></div>
</section>
</li>
<li>
<section className="detail" id="BROKEN_DB">
<h3>BROKEN_DB</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmaprepairerror" title="enum class in com.here.sdk.maploader">PersistentMapRepairError</a></span> <span className="element-name">BROKEN_DB</span></div>
<div className="block"><p>The persisted map data can't be recovered and all map data was fully deleted. It is recommended, to ask
 the user if they want to try to download the lost regions again.</p></div>
</section>
</li>
<li>
<section className="detail" id="NO_OFFLINE_VERSION">
<h3>NO_OFFLINE_VERSION</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmaprepairerror" title="enum class in com.here.sdk.maploader">PersistentMapRepairError</a></span> <span className="element-name">NO_OFFLINE_VERSION</span></div>
<div className="block"><p>The map data version was not cached. The region list data will be cleared from the persisted storage.
 It is recommended to download the list of downloadable regions again.
 After this it is recommended to try to repair the corrupted map data again.</p></div>
</section>
</li>
<li>
<section className="detail" id="NO_JOURNAL">
<h3>NO_JOURNAL</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmaprepairerror" title="enum class in com.here.sdk.maploader">PersistentMapRepairError</a></span> <span className="element-name">NO_JOURNAL</span></div>
<div className="block"><p>It is not possible to retrieve the list of downloaded regions. The region list data will be cleared from the persisted storage.
 It is recommended to download the list of downloadable regions again.
 After this it is recommended to try to repair the corrupted map data again.</p></div>
</section>
</li>
<li>
<section className="detail" id="BROKEN_UPDATE">
<h3>BROKEN_UPDATE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmaprepairerror" title="enum class in com.here.sdk.maploader">PersistentMapRepairError</a></span> <span className="element-name">BROKEN_UPDATE</span></div>
<div className="block"><p>Unrecoverable error during construction of pending update parameters.
 Operations such as catalog updates or region downloads will fail.
 The healing procedure is to clean persistent map with <code>sdk.maploader.MapDownloader.clear_persistent_map_storage</code>.</p></div>
</section>
</li>
<li>
<section className="detail" id="OPERATION_AFTER_DISPOSE">
<h3>OPERATION_AFTER_DISPOSE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmaprepairerror" title="enum class in com.here.sdk.maploader">PersistentMapRepairError</a></span> <span className="element-name">OPERATION_AFTER_DISPOSE</span></div>
<div className="block"><p>Repair is invoked on object connected to the disposed <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a></p></div>
</section>
</li>
<li>
<section className="detail" id="UNKNOWN">
<h3>UNKNOWN</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmaprepairerror" title="enum class in com.here.sdk.maploader">PersistentMapRepairError</a></span> <span className="element-name">UNKNOWN</span></div>
<div className="block"><p>An unknown error occurred. Try to clear the persisted storage by calling <code>sdk.maploader.MapDownloader.clear_persistent_map_storage</code>.
 It is recommended, to ask the user if they want to try to download the lost regions again.</p></div>
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
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmaprepairerror" title="enum class in com.here.sdk.maploader">PersistentMapRepairError</a>[]</span> <span className="element-name">values</span>()</div>
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
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmaprepairerror" title="enum class in com.here.sdk.maploader">PersistentMapRepairError</a></span> <span className="element-name">valueOf</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
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
