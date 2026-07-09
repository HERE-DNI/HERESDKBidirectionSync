---
title: "MapUpdater.MapUpdateVersionCommitPolicy (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-mapupdater-mapupdateversioncommitpolicy"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapUpdater.MapUpdateVersionCommitPolicy.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.maploader</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">java.lang.Enum</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdater-mapupdateversioncommitpolicy" title="enum class in com.here.sdk.maploader">MapUpdater.MapUpdateVersionCommitPolicy</a>&gt;
<div className="inheritance">com.here.sdk.maploader.MapUpdater.MapUpdateVersionCommitPolicy</div>
</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdater-mapupdateversioncommitpolicy" title="enum class in com.here.sdk.maploader">MapUpdater.MapUpdateVersionCommitPolicy</a>&gt;</code>, <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" title="class or interface in java.lang.constant">Constable</a></code></dd>
</dl>
<dl className="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdater" title="class in com.here.sdk.maploader">MapUpdater</a></dd>
</dl>

<div className="type-signature"><span className="modifiers">public static enum </span><span className="element-name type-name-label">MapUpdater.MapUpdateVersionCommitPolicy</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdater-mapupdateversioncommitpolicy" title="enum class in com.here.sdk.maploader">MapUpdater.MapUpdateVersionCommitPolicy</a>&gt;</span></div>
<div className="block"><p>Defines if installed regions and subregions are updated one-by-one or if all regions are
 updated only once the updates for all installed regions have been downloaded entirely.
 This influences the required size of the storage during an update.
 Regardless of the set policy, during an update, the previous region data is kept
 until the new region data is committed successfully to the persisted storage.
 This allows to revert to the previous version in case the update fails.
 With <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdater-mapupdateversioncommitpolicy#ON_COMPLETE"><code>ON_COMPLETE</code></a>, more data has to be kept until
 the update process finishes, while <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdater-mapupdateversioncommitpolicy#ON_FIRST_REGION"><code>ON_FIRST_REGION</code></a>
 allows to make faster use of the downloaded region and requires less disk space as only the
 currently updated region is kept until the process completes.
 However, with an <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdater-mapupdateversioncommitpolicy#ON_FIRST_REGION"><code>ON_FIRST_REGION</code></a> policy the overall
 process can be less reliable and bears a higher risk of errors.</p></div>
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


<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdater-mapupdateversioncommitpolicy#ON_COMPLETE">ON_COMPLETE</a></code></div>
<div className="col-last even-row-color">
<div className="block">Commits the new map version to the cache and the persisted storage once all previously
 installed regions have been updated.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdater-mapupdateversioncommitpolicy#ON_FIRST_REGION">ON_FIRST_REGION</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Updates the cache and the persisted storage once the first region was fully downloaded.</div>
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
<section className="detail" id="ON_FIRST_REGION">
<h3>ON_FIRST_REGION</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdater-mapupdateversioncommitpolicy" title="enum class in com.here.sdk.maploader">MapUpdater.MapUpdateVersionCommitPolicy</a></span> <span className="element-name">ON_FIRST_REGION</span></div>
<div className="block"><p>Updates the cache and the persisted storage once the first region was fully downloaded.
 If only one region was requested, this setting is equivalent to <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdater-mapupdateversioncommitpolicy#ON_COMPLETE"><code>ON_COMPLETE</code></a>.
 If more regions or subregions are requested, then the policy will apply.
 For example, if Germany is requested to be updated, then the cache and the persisted
 storage will be updated as soon as any contained subregion such as Berlin or Brandenburg
 has been fully downloaded. The previous data for a region will be removed once
 that specific region has been updated successfully.
 However, the <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapversionhandle" title="class in com.here.sdk.maploader"><code>MapVersionHandle</code></a> will be updated once the first region has
 been installed. This inconsistency will be gone, once the update process completes.
 In case of errors, or an aborted update process, <a href="sdk-for-android-navigate-com-here-sdk-maploader-catalogsupdateinfocallback" title="interface in com.here.sdk.maploader"><code>CatalogsUpdateInfoCallback</code></a>
 indicates that still an update is available until the process was successfully repeated.</p></div>
</section>
</li>
<li>
<section className="detail" id="ON_COMPLETE">
<h3>ON_COMPLETE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdater-mapupdateversioncommitpolicy" title="enum class in com.here.sdk.maploader">MapUpdater.MapUpdateVersionCommitPolicy</a></span> <span className="element-name">ON_COMPLETE</span></div>
<div className="block"><p>Commits the new map version to the cache and the persisted storage once all previously
 installed regions have been updated. For example, if Germany needs an update, then
 all previous data is kept until Germany including all subregions has been downloaded.
 This update process is more reliable than <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdater-mapupdateversioncommitpolicy#ON_FIRST_REGION"><code>ON_FIRST_REGION</code></a>,
 but requires more free storage space until the process completes. Besides, users need to wait longer until
 they can use all updated regions.</p></div>
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
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdater-mapupdateversioncommitpolicy" title="enum class in com.here.sdk.maploader">MapUpdater.MapUpdateVersionCommitPolicy</a>[]</span> <span className="element-name">values</span>()</div>
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
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdater-mapupdateversioncommitpolicy" title="enum class in com.here.sdk.maploader">MapUpdater.MapUpdateVersionCommitPolicy</a></span> <span className="element-name">valueOf</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
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
