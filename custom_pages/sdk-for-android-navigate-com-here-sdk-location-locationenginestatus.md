---
title: "LocationEngineStatus (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-location-locationenginestatus"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- LocationEngineStatus.html -->






<div class="flex-box">

<div class="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.location</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">java.lang.Enum</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a>&gt;
<div class="inheritance">com.here.sdk.location.LocationEngineStatus</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a>&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" title="class or interface in java.lang.constant">Constable</a></code></dd>
</dl>

<div class="type-signature"><span class="modifiers">public enum </span><span class="element-name type-name-label">LocationEngineStatus</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a>&gt;</span></div>
<div class="block"><p>Indicates the status of the LocationEngine.</p></div>
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
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus#ALREADY_STARTED">ALREADY_STARTED</a></code></div>
<div class="col-last even-row-color">
<div class="block">Tried to start LocationEngine that is already started.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus#AUTHENTICATION_FAILED">AUTHENTICATION_FAILED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Authentication failed.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus#ENGINE_STARTED">ENGINE_STARTED</a></code></div>
<div class="col-last even-row-color">
<div class="block">LocationEngine successfully started.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus#ENGINE_STOPPED">ENGINE_STOPPED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">LocationEngine has been stopped.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus#LOCATION_SERVICES_DISABLED">LOCATION_SERVICES_DISABLED</a></code></div>
<div class="col-last even-row-color">
<div class="block">Location services are disabled in the system settings.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus#MISSING_PERMISSIONS">MISSING_PERMISSIONS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Missing one or more user permissions.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus#NOT_ALLOWED">NOT_ALLOWED</a></code></div>
<div class="col-last even-row-color">
<div class="block">Request is not supported in current region.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus#NOT_READY">NOT_READY</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Engine is not ready for the requested action.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus#NOT_SUPPORTED">NOT_SUPPORTED</a></code></div>
<div class="col-last even-row-color">
<div class="block">Request is not supported.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus#OK">OK</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Requested operation succeeded.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus#PRIVACY_NOTICE_UNCONFIRMED">PRIVACY_NOTICE_UNCONFIRMED</a></code></div>
<div class="col-last even-row-color">
<div class="block">Method confirmHEREPrivacyNoticeInclusion() (or alternatively confirmHEREPrivacyNoticeException())
 was not called before starting the <code>LocationEngine</code> or HERE privacy notice exception was not
 permitted.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus#START_FAILED">START_FAILED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Start failed due to an internal error.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus#USER_CONSENT_NOT_HANDLED">USER_CONSENT_NOT_HANDLED</a></code></div>
<div class="col-last even-row-color">
<div class="block">User consent has not been handled yet.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus#valueOf(java.lang.String)">valueOf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the enum constant of this class with the specified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a>[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus#values()">values</a>()</code></div>
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
<section class="detail" id="ENGINE_STARTED">
<h3>ENGINE_STARTED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span class="element-name">ENGINE_STARTED</span></div>
<div class="block"><p>LocationEngine successfully started.</p></div>
</section>
</li>
<li>
<section class="detail" id="ALREADY_STARTED">
<h3>ALREADY_STARTED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span class="element-name">ALREADY_STARTED</span></div>
<div class="block"><p>Tried to start LocationEngine that is already started.</p></div>
</section>
</li>
<li>
<section class="detail" id="ENGINE_STOPPED">
<h3>ENGINE_STOPPED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span class="element-name">ENGINE_STOPPED</span></div>
<div class="block"><p>LocationEngine has been stopped.</p></div>
</section>
</li>
<li>
<section class="detail" id="START_FAILED">
<h3>START_FAILED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span class="element-name">START_FAILED</span></div>
<div class="block"><p>Start failed due to an internal error.</p></div>
</section>
</li>
<li>
<section class="detail" id="USER_CONSENT_NOT_HANDLED">
<h3>USER_CONSENT_NOT_HANDLED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span class="element-name">USER_CONSENT_NOT_HANDLED</span></div>
<div class="block"><p>User consent has not been handled yet.</p></div>
</section>
</li>
<li>
<section class="detail" id="MISSING_PERMISSIONS">
<h3>MISSING_PERMISSIONS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span class="element-name">MISSING_PERMISSIONS</span></div>
<div class="block"><p>Missing one or more user permissions.</p></div>
</section>
</li>
<li>
<section class="detail" id="AUTHENTICATION_FAILED">
<h3>AUTHENTICATION_FAILED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span class="element-name">AUTHENTICATION_FAILED</span></div>
<div class="block"><p>Authentication failed. Check your credentials.</p></div>
</section>
</li>
<li>
<section class="detail" id="NOT_SUPPORTED">
<h3>NOT_SUPPORTED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span class="element-name">NOT_SUPPORTED</span></div>
<div class="block"><p>Request is not supported.</p></div>
</section>
</li>
<li>
<section class="detail" id="NOT_ALLOWED">
<h3>NOT_ALLOWED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span class="element-name">NOT_ALLOWED</span></div>
<div class="block"><p>Request is not supported in current region.</p></div>
</section>
</li>
<li>
<section class="detail" id="NOT_READY">
<h3>NOT_READY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span class="element-name">NOT_READY</span></div>
<div class="block"><p>Engine is not ready for the requested action.</p></div>
</section>
</li>
<li>
<section class="detail" id="LOCATION_SERVICES_DISABLED">
<h3>LOCATION_SERVICES_DISABLED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span class="element-name">LOCATION_SERVICES_DISABLED</span></div>
<div class="block"><p>Location services are disabled in the system settings.</p></div>
</section>
</li>
<li>
<section class="detail" id="PRIVACY_NOTICE_UNCONFIRMED">
<h3>PRIVACY_NOTICE_UNCONFIRMED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span class="element-name">PRIVACY_NOTICE_UNCONFIRMED</span></div>
<div class="block"><p>Method confirmHEREPrivacyNoticeInclusion() (or alternatively confirmHEREPrivacyNoticeException())
 was not called before starting the <code>LocationEngine</code> or HERE privacy notice exception was not
 permitted.</p></div>
</section>
</li>
<li>
<section class="detail" id="OK">
<h3>OK</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span class="element-name">OK</span></div>
<div class="block"><p>Requested operation succeeded.</p></div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a>[]</span> <span class="element-name">values</span>()</div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span class="element-name">valueOf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
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
</div>



</div>
`
}</HTMLBlock>
