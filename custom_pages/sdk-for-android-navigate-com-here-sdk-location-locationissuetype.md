---
title: "LocationIssueType (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-location-locationissuetype"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- LocationIssueType.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">java.lang.Enum</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a>&gt;
<div class="inheritance">com.here.sdk.location.LocationIssueType</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a>&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" title="class or interface in java.lang.constant">Constable</a></code></dd>
</dl>

<div class="type-signature"><span class="modifiers">public enum </span><span class="element-name type-name-label">LocationIssueType</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a>&gt;</span></div>
<div class="block"><p>Represents specific issues affecting location retrieval quality, availability, or functionality.
 <ul>
<li>Issues are detected automatically by the positioning system and reported via
 LocationIssueListener.</li>
<li>Multiple issues may be active simultaneously (e.g., both quality degradation and
 connectivity problems).</li>
<li>Issues clear automatically when underlying conditions improve (no manual dismissal needed).</li>
</ul></p></div>
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
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#FEATURE_NOT_INCLUDED">FEATURE_NOT_INCLUDED</a></code></div>
<div class="col-last even-row-color">
<div class="block">Requested feature not available for the used license.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#FEATURE_NOT_LICENSED">FEATURE_NOT_LICENSED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Requested feature requires a valid license (missing or expired).</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#HDGNSS_CONNECTION_NOT_AVAILABLE">HDGNSS_CONNECTION_NOT_AVAILABLE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Network connection to HD GNSS assistance server is unavailable.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#HDGNSS_DEGRADED_MEASUREMENT_QUALITY">HDGNSS_DEGRADED_MEASUREMENT_QUALITY</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Satellite measurement quality is degraded; HD GNSS accuracy level may not be achieved.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#HDGNSS_DEVICE_NOT_SUPPORTED">HDGNSS_DEVICE_NOT_SUPPORTED</a></code></div>
<div class="col-last even-row-color">
<div class="block">Device hardware does not support HD GNSS positioning capabilities.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#HDGNSS_INSUFFICIENT_MEASUREMENT_QUALITY">HDGNSS_INSUFFICIENT_MEASUREMENT_QUALITY</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Satellite measurement quality is insufficient to achieve HD GNSS accuracy level.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#HDGNSS_OS_VERSION_NOT_SUPPORTED">HDGNSS_OS_VERSION_NOT_SUPPORTED</a></code></div>
<div class="col-last even-row-color">
<div class="block">Operating system version is below minimum required for HD GNSS (Android 12+).</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#HDGNSS_POS_EXTRAPOLATED">HDGNSS_POS_EXTRAPOLATED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Hd gnss position was calculated by extrapolation.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#POSITION_CELL_SCAN_ERROR">POSITION_CELL_SCAN_ERROR</a></code></div>
<div class="col-last even-row-color">
<div class="block">Failed to scan for cellular network signals.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#POSITION_NO_CELL_MEASUREMENTS">POSITION_NO_CELL_MEASUREMENTS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">No usable cellular network signal measurements available for positioning.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#POSITION_NO_WLAN_MEASUREMENTS">POSITION_NO_WLAN_MEASUREMENTS</a></code></div>
<div class="col-last even-row-color">
<div class="block">No usable Wi-Fi network signal measurements available for positioning.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#POSITION_NOT_FOUND">POSITION_NOT_FOUND</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Unable to determine position from available positioning sources.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#POSITION_WLAN_SCAN_ERROR">POSITION_WLAN_SCAN_ERROR</a></code></div>
<div class="col-last even-row-color">
<div class="block">Failed to scan for Wi-Fi network signals.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#SENSOR_POSITIONING_NOT_AVAILABLE">SENSOR_POSITIONING_NOT_AVAILABLE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Device sensors required for sensor fusion positioning are unavailable.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#valueOf(java.lang.String)">valueOf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the enum constant of this class with the specified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a>[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#values()">values</a>()</code></div>
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
<section class="detail" id="HDGNSS_DEVICE_NOT_SUPPORTED">
<h3>HDGNSS_DEVICE_NOT_SUPPORTED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span class="element-name">HDGNSS_DEVICE_NOT_SUPPORTED</span></div>
<div class="block"><p>Device hardware does not support HD GNSS positioning capabilities.</p></div>
</section>
</li>
<li>
<section class="detail" id="HDGNSS_OS_VERSION_NOT_SUPPORTED">
<h3>HDGNSS_OS_VERSION_NOT_SUPPORTED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span class="element-name">HDGNSS_OS_VERSION_NOT_SUPPORTED</span></div>
<div class="block"><p>Operating system version is below minimum required for HD GNSS (Android 12+).</p></div>
</section>
</li>
<li>
<section class="detail" id="HDGNSS_CONNECTION_NOT_AVAILABLE">
<h3>HDGNSS_CONNECTION_NOT_AVAILABLE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span class="element-name">HDGNSS_CONNECTION_NOT_AVAILABLE</span></div>
<div class="block"><p>Network connection to HD GNSS assistance server is unavailable.</p></div>
</section>
</li>
<li>
<section class="detail" id="HDGNSS_DEGRADED_MEASUREMENT_QUALITY">
<h3>HDGNSS_DEGRADED_MEASUREMENT_QUALITY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span class="element-name">HDGNSS_DEGRADED_MEASUREMENT_QUALITY</span></div>
<div class="block"><p>Satellite measurement quality is degraded; HD GNSS accuracy level may not be achieved.</p></div>
</section>
</li>
<li>
<section class="detail" id="HDGNSS_INSUFFICIENT_MEASUREMENT_QUALITY">
<h3>HDGNSS_INSUFFICIENT_MEASUREMENT_QUALITY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span class="element-name">HDGNSS_INSUFFICIENT_MEASUREMENT_QUALITY</span></div>
<div class="block"><p>Satellite measurement quality is insufficient to achieve HD GNSS accuracy level.</p></div>
</section>
</li>
<li>
<section class="detail" id="FEATURE_NOT_LICENSED">
<h3>FEATURE_NOT_LICENSED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span class="element-name">FEATURE_NOT_LICENSED</span></div>
<div class="block"><p>Requested feature requires a valid license (missing or expired).</p></div>
</section>
</li>
<li>
<section class="detail" id="FEATURE_NOT_INCLUDED">
<h3>FEATURE_NOT_INCLUDED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span class="element-name">FEATURE_NOT_INCLUDED</span></div>
<div class="block"><p>Requested feature not available for the used license.</p></div>
</section>
</li>
<li>
<section class="detail" id="SENSOR_POSITIONING_NOT_AVAILABLE">
<h3>SENSOR_POSITIONING_NOT_AVAILABLE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span class="element-name">SENSOR_POSITIONING_NOT_AVAILABLE</span></div>
<div class="block"><p>Device sensors required for sensor fusion positioning are unavailable.</p></div>
</section>
</li>
<li>
<section class="detail" id="POSITION_NOT_FOUND">
<h3>POSITION_NOT_FOUND</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span class="element-name">POSITION_NOT_FOUND</span></div>
<div class="block"><p>Unable to determine position from available positioning sources.</p></div>
</section>
</li>
<li>
<section class="detail" id="POSITION_NO_CELL_MEASUREMENTS">
<h3>POSITION_NO_CELL_MEASUREMENTS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span class="element-name">POSITION_NO_CELL_MEASUREMENTS</span></div>
<div class="block"><p>No usable cellular network signal measurements available for positioning.</p></div>
</section>
</li>
<li>
<section class="detail" id="POSITION_NO_WLAN_MEASUREMENTS">
<h3>POSITION_NO_WLAN_MEASUREMENTS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span class="element-name">POSITION_NO_WLAN_MEASUREMENTS</span></div>
<div class="block"><p>No usable Wi-Fi network signal measurements available for positioning.</p></div>
</section>
</li>
<li>
<section class="detail" id="POSITION_CELL_SCAN_ERROR">
<h3>POSITION_CELL_SCAN_ERROR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span class="element-name">POSITION_CELL_SCAN_ERROR</span></div>
<div class="block"><p>Failed to scan for cellular network signals.</p></div>
</section>
</li>
<li>
<section class="detail" id="POSITION_WLAN_SCAN_ERROR">
<h3>POSITION_WLAN_SCAN_ERROR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span class="element-name">POSITION_WLAN_SCAN_ERROR</span></div>
<div class="block"><p>Failed to scan for Wi-Fi network signals.</p></div>
</section>
</li>
<li>
<section class="detail" id="HDGNSS_POS_EXTRAPOLATED">
<h3>HDGNSS_POS_EXTRAPOLATED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span class="element-name">HDGNSS_POS_EXTRAPOLATED</span></div>
<div class="block"><p>Hd gnss position was calculated by extrapolation.</p></div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a>[]</span> <span class="element-name">values</span>()</div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span class="element-name">valueOf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
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
