---
title: "EventText (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-eventtext"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- EventText.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.navigation.EventText</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">EventText</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Contains all the information regarding the next text announcement.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>double</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-eventtext#distanceInMeters">distanceInMeters</a></code></div>
<div className="col-last even-row-color">
<div className="block">Distance in meters to the location of the event for which the text notification is given.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationdetails" title="class in com.here.sdk.navigation">ManeuverNotificationDetails</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-eventtext#maneuverNotificationDetails">maneuverNotificationDetails</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Information about the next maneuver.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-spatialnotificationdetails" title="class in com.here.sdk.navigation">SpatialNotificationDetails</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-eventtext#spatialNotificationDetails">spatialNotificationDetails</a></code></div>
<div className="col-last even-row-color">
<div className="block">Information for a spatial text notifications.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-eventtext#text">text</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The text notification instruction.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-textnotificationtype" title="enum class in com.here.sdk.navigation">TextNotificationType</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-eventtext#type">type</a></code></div>
<div className="col-last even-row-color">
<div className="block">Indicates the type of text announcement</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-eventtext#%3Cinit%3E(com.here.sdk.navigation.TextNotificationType,double,java.lang.String)">EventText</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-navigation-textnotificationtype" title="enum class in com.here.sdk.navigation">TextNotificationType</a> type,
 double distanceInMeters,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
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
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section className="field-details" id="field-detail">

<ul className="member-list">
<li>
<section className="detail" id="type">
<h3>type</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-textnotificationtype" title="enum class in com.here.sdk.navigation">TextNotificationType</a></span> <span className="element-name">type</span></div>
<div className="block"><p>Indicates the type of text announcement</p></div>
</section>
</li>
<li>
<section className="detail" id="distanceInMeters">
<h3>distanceInMeters</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">distanceInMeters</span></div>
<div className="block"><p>Distance in meters to the location of the event for which the text notification is given.
 <strong>Note:</strong> For greater distances, distance in kilometers is rounded to the nearest digit (0.5 or
 greater rounds up, else down) to simplify the distance phrase in <code>ManeuverNotifications</code> texts
 during navigation. Distance in miles is rounded to the nearest 0.5 step. For example, 3.5 kilometers
 are rounded to 4 kilometers and the notification will begin with <code>After 4 kilometers...</code>. However,
 3.5 miles are not rounded up and the notification will begin with <code>After three and a half miles...</code>.
 Same for 3.7 miles, whereas 3.8 miles are rounded to 4 miles. Note that the measurement units itself
 are defined in the <code>UnitSystem</code> class.</p></div>
</section>
</li>
<li>
<section className="detail" id="text">
<h3>text</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">text</span></div>
<div className="block"><p>The text notification instruction. The text is formatted and localized as specified via
 <a href="sdk-for-android-navigate-com-here-sdk-routing-routetextoptions" title="class in com.here.sdk.routing"><code>RouteTextOptions</code></a>.
 <strong>Note:</strong> During navigation, the text will be always empty when the <a href="sdk-for-android-navigate-com-here-sdk-routing-maneuver" title="class in com.here.sdk.routing"><code>Maneuver</code></a> is
 taken from the <code>Navigator</code> or <code>VisualNavigator</code> instance via the provided index.
 The text instruction that can be accessed from the <a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing"><code>Route</code></a> instance is meant
 as preview and it is not necessarily matching the more comprehensive maneuver information you
 can access during navigation. This information can be enhanced with real-time <code>ManeuverNotifications</code>
 texts that can be used for spoken text notifications during a trip.</p></div>
</section>
</li>
<li>
<section className="detail" id="maneuverNotificationDetails">
<h3>maneuverNotificationDetails</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-maneuvernotificationdetails" title="class in com.here.sdk.navigation">ManeuverNotificationDetails</a></span> <span className="element-name">maneuverNotificationDetails</span></div>
<div className="block"><p>Information about the next maneuver.
 Is non-<code>null</code> only for <a href="sdk-for-android-navigate-com-here-sdk-navigation-eventtext#type"><code>type</code></a> equals to <a href="sdk-for-android-navigate-textnotificationtype#MANEUVER"><code>TextNotificationType.MANEUVER</code></a>.</p></div>
</section>
</li>
<li>
<section className="detail" id="spatialNotificationDetails">
<h3>spatialNotificationDetails</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-spatialnotificationdetails" title="class in com.here.sdk.navigation">SpatialNotificationDetails</a></span> <span className="element-name">spatialNotificationDetails</span></div>
<div className="block"><p>Information for a spatial text notifications.
 When <a href="sdk-for-android-navigate-eventtextoptions#enableSpatialAudio"><code>EventTextOptions.enableSpatialAudio</code></a> is false,
 then this attribute will be <code>null</code>.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.navigation.TextNotificationType,double,java.lang.String)">
<h3>EventText</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">EventText</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-textnotificationtype" title="enum class in com.here.sdk.navigation">TextNotificationType</a> type,
 double distanceInMeters,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - <p>Indicates the type of text announcement</p></dd>
<dd><code>distanceInMeters</code> - <p>Distance in meters to the location of the event for which the text notification is given.
 <strong>Note:</strong> For greater distances, distance in kilometers is rounded to the nearest digit (0.5 or
 greater rounds up, else down) to simplify the distance phrase in <code>ManeuverNotifications</code> texts
 during navigation. Distance in miles is rounded to the nearest 0.5 step. For example, 3.5 kilometers
 are rounded to 4 kilometers and the notification will begin with <code>After 4 kilometers...</code>. However,
 3.5 miles are not rounded up and the notification will begin with <code>After three and a half miles...</code>.
 Same for 3.7 miles, whereas 3.8 miles are rounded to 4 miles. Note that the measurement units itself
 are defined in the <code>UnitSystem</code> class.</p></dd>
<dd><code>text</code> - <p>The text notification instruction. The text is formatted and localized as specified via
 <a href="sdk-for-android-navigate-com-here-sdk-routing-routetextoptions" title="class in com.here.sdk.routing"><code>RouteTextOptions</code></a>.
 <strong>Note:</strong> During navigation, the text will be always empty when the <a href="sdk-for-android-navigate-com-here-sdk-routing-maneuver" title="class in com.here.sdk.routing"><code>Maneuver</code></a> is
 taken from the <code>Navigator</code> or <code>VisualNavigator</code> instance via the provided index.
 The text instruction that can be accessed from the <a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing"><code>Route</code></a> instance is meant
 as preview and it is not necessarily matching the more comprehensive maneuver information you
 can access during navigation. This information can be enhanced with real-time <code>ManeuverNotifications</code>
 texts that can be used for spoken text notifications during a trip.</p></dd>
</dl>
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
<section className="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">equals</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="hashCode()">
<h3>hashCode</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">hashCode</span>()</div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
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
