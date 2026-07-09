---
title: "LocationAccuracy (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-location-locationaccuracy"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- LocationAccuracy.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.location</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">java.lang.Enum</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-location-locationaccuracy" title="enum class in com.here.sdk.location">LocationAccuracy</a>&gt;
<div className="inheritance">com.here.sdk.location.LocationAccuracy</div>
</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-location-locationaccuracy" title="enum class in com.here.sdk.location">LocationAccuracy</a>&gt;</code>, <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" title="class or interface in java.lang.constant">Constable</a></code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public enum </span><span className="element-name type-name-label">LocationAccuracy</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-location-locationaccuracy" title="enum class in com.here.sdk.location">LocationAccuracy</a>&gt;</span></div>
<div className="block"><p>Indicates the desired location accuracy, however the actual accuracy is not
 guaranteed. When requesting high-accuracy locations, the initial update delivered
 by the LocationEngine may not have the requested accuracy. Requesting higher
 accuracy location updates usually means higher power consumption, therefore
 you should use the lowest accuracy suitable for your use case to preserve the
 device battery.</p></div>
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


<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationaccuracy#BEST_AVAILABLE">BEST_AVAILABLE</a></code></div>
<div className="col-last even-row-color">
<div className="block">The best accuracy available, using all possible sources: satellite, WiFi and Cell positioning.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationaccuracy#HUNDREDS_OF_METERS">HUNDREDS_OF_METERS</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Accurate to within hundreds of meters of the desired target.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationaccuracy#KILOMETERS">KILOMETERS</a></code></div>
<div className="col-last even-row-color">
<div className="block">Accurate to within kilometers of the desired target.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationaccuracy#NAVIGATION">NAVIGATION</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The default accuracy when navigation is needed, using satellite and WiFi positioning.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationaccuracy#SUB_METER_NAVIGATION">SUB_METER_NAVIGATION</a></code></div>
<div className="col-last even-row-color">
<div className="block">Decimeter accurate navigation using satellite and WiFi positioning.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationaccuracy#TENS_OF_METERS">TENS_OF_METERS</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Accurate to within tens of meters of the desired target.</div>
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
<section className="detail" id="BEST_AVAILABLE">
<h3>BEST_AVAILABLE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationaccuracy" title="enum class in com.here.sdk.location">LocationAccuracy</a></span> <span className="element-name">BEST_AVAILABLE</span></div>
<div className="block"><p>The best accuracy available, using all possible sources: satellite, WiFi and Cell positioning.
 Additional sensor data may be used for improving positioning accuracy.
 Update frequency may vary between 1 second to about 30 seconds, so this is not the best option for navigation purposes, see <a href="sdk-for-android-navigate-com-here-sdk-location-locationaccuracy#NAVIGATION"><code>NAVIGATION</code></a>
 and <a href="sdk-for-android-navigate-com-here-sdk-location-locationaccuracy#SUB_METER_NAVIGATION"><code>SUB_METER_NAVIGATION</code></a>.</p></div>
</section>
</li>
<li>
<section className="detail" id="SUB_METER_NAVIGATION">
<h3>SUB_METER_NAVIGATION</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationaccuracy" title="enum class in com.here.sdk.location">LocationAccuracy</a></span> <span className="element-name">SUB_METER_NAVIGATION</span></div>
<div className="block"><p>Decimeter accurate navigation using satellite and WiFi positioning.
 Additional sensor data may be used for improving positioning accuracy.
 Update frequency is as close to once per second as possible.
 This feature requires Android 12 or later and dual frequency GNSS receiver and raw GNSS measurements.
 This feature is disabled by default: <a href="https://www.here.com/platform/positioning">Contact us</a> to enable it.
 If it is not enabled or the OS/device requirements are not met, fallback to other positioning technologies may occur and desired accuracy level may not be reached.</p></div>
</section>
</li>
<li>
<section className="detail" id="NAVIGATION">
<h3>NAVIGATION</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationaccuracy" title="enum class in com.here.sdk.location">LocationAccuracy</a></span> <span className="element-name">NAVIGATION</span></div>
<div className="block"><p>The default accuracy when navigation is needed, using satellite and WiFi positioning.
 Additional sensor data is used for improving navigation accuracy. Update frequency is as close to once per second as possible.</p></div>
</section>
</li>
<li>
<section className="detail" id="TENS_OF_METERS">
<h3>TENS_OF_METERS</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationaccuracy" title="enum class in com.here.sdk.location">LocationAccuracy</a></span> <span className="element-name">TENS_OF_METERS</span></div>
<div className="block"><p>Accurate to within tens of meters of the desired target.
 Additional sensor data may be used for improving localization accuracy.</p></div>
</section>
</li>
<li>
<section className="detail" id="HUNDREDS_OF_METERS">
<h3>HUNDREDS_OF_METERS</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationaccuracy" title="enum class in com.here.sdk.location">LocationAccuracy</a></span> <span className="element-name">HUNDREDS_OF_METERS</span></div>
<div className="block"><p>Accurate to within hundreds of meters of the desired target.</p></div>
</section>
</li>
<li>
<section className="detail" id="KILOMETERS">
<h3>KILOMETERS</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationaccuracy" title="enum class in com.here.sdk.location">LocationAccuracy</a></span> <span className="element-name">KILOMETERS</span></div>
<div className="block"><p>Accurate to within kilometers of the desired target.</p></div>
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
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationaccuracy" title="enum class in com.here.sdk.location">LocationAccuracy</a>[]</span> <span className="element-name">values</span>()</div>
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
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationaccuracy" title="enum class in com.here.sdk.location">LocationAccuracy</a></span> <span className="element-name">valueOf</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
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
