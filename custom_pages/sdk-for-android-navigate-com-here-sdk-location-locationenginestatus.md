---
title: "LocationEngineStatus (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-location-locationenginestatus"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- LocationEngineStatus.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.location</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">java.lang.Enum</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a>&gt;
<div className="inheritance">com.here.sdk.location.LocationEngineStatus</div>
</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a>&gt;</code>, <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" title="class or interface in java.lang.constant">Constable</a></code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public enum </span><span className="element-name type-name-label">LocationEngineStatus</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a>&gt;</span></div>
<div className="block"><p>Indicates the status of the LocationEngine.</p></div>
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


<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus#ALREADY_STARTED">ALREADY_STARTED</a></code></div>
<div className="col-last even-row-color">
<div className="block">Tried to start LocationEngine that is already started.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus#AUTHENTICATION_FAILED">AUTHENTICATION_FAILED</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Authentication failed.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus#ENGINE_STARTED">ENGINE_STARTED</a></code></div>
<div className="col-last even-row-color">
<div className="block">LocationEngine successfully started.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus#ENGINE_STOPPED">ENGINE_STOPPED</a></code></div>
<div className="col-last odd-row-color">
<div className="block">LocationEngine has been stopped.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus#LOCATION_SERVICES_DISABLED">LOCATION_SERVICES_DISABLED</a></code></div>
<div className="col-last even-row-color">
<div className="block">Location services are disabled in the system settings.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus#MISSING_PERMISSIONS">MISSING_PERMISSIONS</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Missing one or more user permissions.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus#NOT_ALLOWED">NOT_ALLOWED</a></code></div>
<div className="col-last even-row-color">
<div className="block">Request is not supported in current region.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus#NOT_READY">NOT_READY</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Engine is not ready for the requested action.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus#NOT_SUPPORTED">NOT_SUPPORTED</a></code></div>
<div className="col-last even-row-color">
<div className="block">Request is not supported.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus#OK">OK</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Requested operation succeeded.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus#PRIVACY_NOTICE_UNCONFIRMED">PRIVACY_NOTICE_UNCONFIRMED</a></code></div>
<div className="col-last even-row-color">
<div className="block">Method confirmHEREPrivacyNoticeInclusion() (or alternatively confirmHEREPrivacyNoticeException())
 was not called before starting the <code>LocationEngine</code> or HERE privacy notice exception was not
 permitted.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus#START_FAILED">START_FAILED</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Start failed due to an internal error.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus#USER_CONSENT_NOT_HANDLED">USER_CONSENT_NOT_HANDLED</a></code></div>
<div className="col-last even-row-color">
<div className="block">User consent has not been handled yet.</div>
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
<section className="detail" id="ENGINE_STARTED">
<h3>ENGINE_STARTED</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span className="element-name">ENGINE_STARTED</span></div>
<div className="block"><p>LocationEngine successfully started.</p></div>
</section>
</li>
<li>
<section className="detail" id="ALREADY_STARTED">
<h3>ALREADY_STARTED</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span className="element-name">ALREADY_STARTED</span></div>
<div className="block"><p>Tried to start LocationEngine that is already started.</p></div>
</section>
</li>
<li>
<section className="detail" id="ENGINE_STOPPED">
<h3>ENGINE_STOPPED</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span className="element-name">ENGINE_STOPPED</span></div>
<div className="block"><p>LocationEngine has been stopped.</p></div>
</section>
</li>
<li>
<section className="detail" id="START_FAILED">
<h3>START_FAILED</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span className="element-name">START_FAILED</span></div>
<div className="block"><p>Start failed due to an internal error.</p></div>
</section>
</li>
<li>
<section className="detail" id="USER_CONSENT_NOT_HANDLED">
<h3>USER_CONSENT_NOT_HANDLED</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span className="element-name">USER_CONSENT_NOT_HANDLED</span></div>
<div className="block"><p>User consent has not been handled yet.</p></div>
</section>
</li>
<li>
<section className="detail" id="MISSING_PERMISSIONS">
<h3>MISSING_PERMISSIONS</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span className="element-name">MISSING_PERMISSIONS</span></div>
<div className="block"><p>Missing one or more user permissions.</p></div>
</section>
</li>
<li>
<section className="detail" id="AUTHENTICATION_FAILED">
<h3>AUTHENTICATION_FAILED</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span className="element-name">AUTHENTICATION_FAILED</span></div>
<div className="block"><p>Authentication failed. Check your credentials.</p></div>
</section>
</li>
<li>
<section className="detail" id="NOT_SUPPORTED">
<h3>NOT_SUPPORTED</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span className="element-name">NOT_SUPPORTED</span></div>
<div className="block"><p>Request is not supported.</p></div>
</section>
</li>
<li>
<section className="detail" id="NOT_ALLOWED">
<h3>NOT_ALLOWED</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span className="element-name">NOT_ALLOWED</span></div>
<div className="block"><p>Request is not supported in current region.</p></div>
</section>
</li>
<li>
<section className="detail" id="NOT_READY">
<h3>NOT_READY</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span className="element-name">NOT_READY</span></div>
<div className="block"><p>Engine is not ready for the requested action.</p></div>
</section>
</li>
<li>
<section className="detail" id="LOCATION_SERVICES_DISABLED">
<h3>LOCATION_SERVICES_DISABLED</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span className="element-name">LOCATION_SERVICES_DISABLED</span></div>
<div className="block"><p>Location services are disabled in the system settings.</p></div>
</section>
</li>
<li>
<section className="detail" id="PRIVACY_NOTICE_UNCONFIRMED">
<h3>PRIVACY_NOTICE_UNCONFIRMED</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span className="element-name">PRIVACY_NOTICE_UNCONFIRMED</span></div>
<div className="block"><p>Method confirmHEREPrivacyNoticeInclusion() (or alternatively confirmHEREPrivacyNoticeException())
 was not called before starting the <code>LocationEngine</code> or HERE privacy notice exception was not
 permitted.</p></div>
</section>
</li>
<li>
<section className="detail" id="OK">
<h3>OK</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span className="element-name">OK</span></div>
<div className="block"><p>Requested operation succeeded.</p></div>
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
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a>[]</span> <span className="element-name">values</span>()</div>
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
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span className="element-name">valueOf</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
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
