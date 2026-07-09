---
title: "LocationIssueType (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-location-locationissuetype"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- LocationIssueType.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.location</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">java.lang.Enum</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a>&gt;
<div className="inheritance">com.here.sdk.location.LocationIssueType</div>
</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a>&gt;</code>, <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" title="class or interface in java.lang.constant">Constable</a></code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public enum </span><span className="element-name type-name-label">LocationIssueType</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a>&gt;</span></div>
<div className="block"><p>Represents specific issues affecting location retrieval quality, availability, or functionality.
 <ul>
<li>Issues are detected automatically by the positioning system and reported via
 LocationIssueListener.</li>
<li>Multiple issues may be active simultaneously (e.g., both quality degradation and
 connectivity problems).</li>
<li>Issues clear automatically when underlying conditions improve (no manual dismissal needed).</li>
</ul></p></div>
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


<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#FEATURE_NOT_INCLUDED">FEATURE_NOT_INCLUDED</a></code></div>
<div className="col-last even-row-color">
<div className="block">Requested feature not available for the used license.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#FEATURE_NOT_LICENSED">FEATURE_NOT_LICENSED</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Requested feature requires a valid license (missing or expired).</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#HDGNSS_CONNECTION_NOT_AVAILABLE">HDGNSS_CONNECTION_NOT_AVAILABLE</a></code></div>
<div className="col-last even-row-color">
<div className="block">Network connection to HD GNSS assistance server is unavailable.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#HDGNSS_DEGRADED_MEASUREMENT_QUALITY">HDGNSS_DEGRADED_MEASUREMENT_QUALITY</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Satellite measurement quality is degraded; HD GNSS accuracy level may not be achieved.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#HDGNSS_DEVICE_NOT_SUPPORTED">HDGNSS_DEVICE_NOT_SUPPORTED</a></code></div>
<div className="col-last even-row-color">
<div className="block">Device hardware does not support HD GNSS positioning capabilities.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#HDGNSS_INSUFFICIENT_MEASUREMENT_QUALITY">HDGNSS_INSUFFICIENT_MEASUREMENT_QUALITY</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Satellite measurement quality is insufficient to achieve HD GNSS accuracy level.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#HDGNSS_OS_VERSION_NOT_SUPPORTED">HDGNSS_OS_VERSION_NOT_SUPPORTED</a></code></div>
<div className="col-last even-row-color">
<div className="block">Operating system version is below minimum required for HD GNSS (Android 12+).</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#HDGNSS_POS_EXTRAPOLATED">HDGNSS_POS_EXTRAPOLATED</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Hd gnss position was calculated by extrapolation.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#POSITION_CELL_SCAN_ERROR">POSITION_CELL_SCAN_ERROR</a></code></div>
<div className="col-last even-row-color">
<div className="block">Failed to scan for cellular network signals.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#POSITION_NO_CELL_MEASUREMENTS">POSITION_NO_CELL_MEASUREMENTS</a></code></div>
<div className="col-last odd-row-color">
<div className="block">No usable cellular network signal measurements available for positioning.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#POSITION_NO_WLAN_MEASUREMENTS">POSITION_NO_WLAN_MEASUREMENTS</a></code></div>
<div className="col-last even-row-color">
<div className="block">No usable Wi-Fi network signal measurements available for positioning.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#POSITION_NOT_FOUND">POSITION_NOT_FOUND</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Unable to determine position from available positioning sources.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#POSITION_WLAN_SCAN_ERROR">POSITION_WLAN_SCAN_ERROR</a></code></div>
<div className="col-last even-row-color">
<div className="block">Failed to scan for Wi-Fi network signals.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#SENSOR_POSITIONING_NOT_AVAILABLE">SENSOR_POSITIONING_NOT_AVAILABLE</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Device sensors required for sensor fusion positioning are unavailable.</div>
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
<section className="detail" id="HDGNSS_DEVICE_NOT_SUPPORTED">
<h3>HDGNSS_DEVICE_NOT_SUPPORTED</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span className="element-name">HDGNSS_DEVICE_NOT_SUPPORTED</span></div>
<div className="block"><p>Device hardware does not support HD GNSS positioning capabilities.</p></div>
</section>
</li>
<li>
<section className="detail" id="HDGNSS_OS_VERSION_NOT_SUPPORTED">
<h3>HDGNSS_OS_VERSION_NOT_SUPPORTED</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span className="element-name">HDGNSS_OS_VERSION_NOT_SUPPORTED</span></div>
<div className="block"><p>Operating system version is below minimum required for HD GNSS (Android 12+).</p></div>
</section>
</li>
<li>
<section className="detail" id="HDGNSS_CONNECTION_NOT_AVAILABLE">
<h3>HDGNSS_CONNECTION_NOT_AVAILABLE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span className="element-name">HDGNSS_CONNECTION_NOT_AVAILABLE</span></div>
<div className="block"><p>Network connection to HD GNSS assistance server is unavailable.</p></div>
</section>
</li>
<li>
<section className="detail" id="HDGNSS_DEGRADED_MEASUREMENT_QUALITY">
<h3>HDGNSS_DEGRADED_MEASUREMENT_QUALITY</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span className="element-name">HDGNSS_DEGRADED_MEASUREMENT_QUALITY</span></div>
<div className="block"><p>Satellite measurement quality is degraded; HD GNSS accuracy level may not be achieved.</p></div>
</section>
</li>
<li>
<section className="detail" id="HDGNSS_INSUFFICIENT_MEASUREMENT_QUALITY">
<h3>HDGNSS_INSUFFICIENT_MEASUREMENT_QUALITY</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span className="element-name">HDGNSS_INSUFFICIENT_MEASUREMENT_QUALITY</span></div>
<div className="block"><p>Satellite measurement quality is insufficient to achieve HD GNSS accuracy level.</p></div>
</section>
</li>
<li>
<section className="detail" id="FEATURE_NOT_LICENSED">
<h3>FEATURE_NOT_LICENSED</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span className="element-name">FEATURE_NOT_LICENSED</span></div>
<div className="block"><p>Requested feature requires a valid license (missing or expired).</p></div>
</section>
</li>
<li>
<section className="detail" id="FEATURE_NOT_INCLUDED">
<h3>FEATURE_NOT_INCLUDED</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span className="element-name">FEATURE_NOT_INCLUDED</span></div>
<div className="block"><p>Requested feature not available for the used license.</p></div>
</section>
</li>
<li>
<section className="detail" id="SENSOR_POSITIONING_NOT_AVAILABLE">
<h3>SENSOR_POSITIONING_NOT_AVAILABLE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span className="element-name">SENSOR_POSITIONING_NOT_AVAILABLE</span></div>
<div className="block"><p>Device sensors required for sensor fusion positioning are unavailable.</p></div>
</section>
</li>
<li>
<section className="detail" id="POSITION_NOT_FOUND">
<h3>POSITION_NOT_FOUND</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span className="element-name">POSITION_NOT_FOUND</span></div>
<div className="block"><p>Unable to determine position from available positioning sources.</p></div>
</section>
</li>
<li>
<section className="detail" id="POSITION_NO_CELL_MEASUREMENTS">
<h3>POSITION_NO_CELL_MEASUREMENTS</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span className="element-name">POSITION_NO_CELL_MEASUREMENTS</span></div>
<div className="block"><p>No usable cellular network signal measurements available for positioning.</p></div>
</section>
</li>
<li>
<section className="detail" id="POSITION_NO_WLAN_MEASUREMENTS">
<h3>POSITION_NO_WLAN_MEASUREMENTS</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span className="element-name">POSITION_NO_WLAN_MEASUREMENTS</span></div>
<div className="block"><p>No usable Wi-Fi network signal measurements available for positioning.</p></div>
</section>
</li>
<li>
<section className="detail" id="POSITION_CELL_SCAN_ERROR">
<h3>POSITION_CELL_SCAN_ERROR</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span className="element-name">POSITION_CELL_SCAN_ERROR</span></div>
<div className="block"><p>Failed to scan for cellular network signals.</p></div>
</section>
</li>
<li>
<section className="detail" id="POSITION_WLAN_SCAN_ERROR">
<h3>POSITION_WLAN_SCAN_ERROR</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span className="element-name">POSITION_WLAN_SCAN_ERROR</span></div>
<div className="block"><p>Failed to scan for Wi-Fi network signals.</p></div>
</section>
</li>
<li>
<section className="detail" id="HDGNSS_POS_EXTRAPOLATED">
<h3>HDGNSS_POS_EXTRAPOLATED</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span className="element-name">HDGNSS_POS_EXTRAPOLATED</span></div>
<div className="block"><p>Hd gnss position was calculated by extrapolation.</p></div>
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
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a>[]</span> <span className="element-name">values</span>()</div>
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
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span className="element-name">valueOf</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
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
