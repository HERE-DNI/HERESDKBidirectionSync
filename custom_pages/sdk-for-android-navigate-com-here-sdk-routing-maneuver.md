---
title: "Maneuver (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-maneuver"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- Maneuver.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.routing</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.routing.Maneuver</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">Maneuver</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>This class provides all the information for a maneuver. The directional information (e.g. road names, road
 numbers and signpost direction) is stored in <a href="sdk-for-android-navigate-com-here-sdk-routing-maneuver#getRoadTexts()"><code>getRoadTexts()</code></a> and <a href="sdk-for-android-navigate-com-here-sdk-routing-maneuver#getNextRoadTexts()"><code>getNextRoadTexts()</code></a> attributes.
 As for the motorway exit information, it can be obtained from <a href="sdk-for-android-navigate-com-here-sdk-routing-maneuver#getExitSignTexts()"><code>getExitSignTexts()</code></a> attribute.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="getAction()">
<h3>getAction</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span className="element-name">getAction</span>()</div>
<div className="block"><p>Gets the maneuver action.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Indicates the maneuver action.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getCoordinates()">
<h3>getCoordinates</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span className="element-name">getCoordinates</span>()</div>
<div className="block"><p>Gets the geographic coordinates where the maneuver is located.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Geographic coordinates where the maneuver is located.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getOffset()">
<h3>getOffset</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">getOffset</span>()</div>
<div className="block"><p>Gets the index over <a href="sdk-for-android-navigate-section#getGeometry()"><code>Section.getGeometry()</code></a> where the maneuver is located.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Index over <a href="sdk-for-android-navigate-section#getGeometry()"><code>Section.getGeometry()</code></a> where the maneuver is located.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getCountryCode()">
<h3>getCountryCode</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getCountryCode</span>()</div>
<div className="block"><p>Gets the country code of the maneuver position. The value is <code>null</code> when no data is available.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The country code of the maneuver position. The value is <code>null</code> when no data is available.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getExitSignTexts()">
<h3>getExitSignTexts</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtexts" title="class in com.here.sdk.core">LocalizedTexts</a></span> <span className="element-name">getExitSignTexts</span>()</div>
<div className="block"><p>Gets the textual attributes of the exit sign. These might contain exit number(s) and/or name(s).
 These attributes are only available for the Navigate license.
 Otherwise, the attributes are always empty.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The textual attributes of the exit sign. These might contain exit number(s) and/or name(s).</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getLengthInMeters()">
<h3>getLengthInMeters</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">getLengthInMeters</span>()</div>
<div className="block"><p>Gets the length of the maneuver in meters.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The length of the maneuver in meters.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getRoadTexts()">
<h3>getRoadTexts</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-roadtexts" title="class in com.here.sdk.routing">RoadTexts</a></span> <span className="element-name">getRoadTexts</span>()</div>
<div className="block"><p>Gets the textual attributes of the current road containing road names, road numbers and signpost direction (towards) information.
 <strong>Note:</strong> These attributes are only available for the Navigate license.
 Otherwise, the attributes are always empty.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The textual attributes of the current road containing road names, road numbers and signpost direction (towards) information.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getNextRoadTexts()">
<h3>getNextRoadTexts</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-roadtexts" title="class in com.here.sdk.routing">RoadTexts</a></span> <span className="element-name">getNextRoadTexts</span>()</div>
<div className="block"><p>Gets the textual attributes of the next road containing the corresponding road name(s) and road number(s) after the maneuver point.
 These attributes are only available for the Navigate license.
 Otherwise, the attributes are always empty.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The textual attributes of the next road containing the corresponding road name(s) and road number(s) after the maneuver point.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSignpost()">
<h3>getSignpost</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-signpost" title="class in com.here.sdk.routing">Signpost</a></span> <span className="element-name">getSignpost</span>()</div>
<div className="block"><p>Gets <a href="sdk-for-android-navigate-com-here-sdk-routing-signpost" title="class in com.here.sdk.routing"><code>Signpost</code></a> object.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Gets the <a href="sdk-for-android-navigate-com-here-sdk-routing-signpost" title="class in com.here.sdk.routing"><code>Signpost</code></a> object.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getIntersectionNames()">
<h3>getIntersectionNames</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtexts" title="class in com.here.sdk.core">LocalizedTexts</a></span> <span className="element-name">getIntersectionNames</span>()</div>
<div className="block"><p>Gets the textual attributes of the intersection.
 These attributes are only available for the Navigate license.
 Otherwise, the attributes are always empty.
 <strong>Note:</strong> Routes calculated with OfflineRoutingEngine are not supported.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The textual attributes of the intersection.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getText()">
<h3>getText</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getText</span>()</div>
<div className="block"><p>Gets the maneuver instruction. The text is formatted and localized as specified via
 <a href="sdk-for-android-navigate-com-here-sdk-routing-routetextoptions" title="class in com.here.sdk.routing"><code>RouteTextOptions</code></a>.
 <strong>Note for users of the Navigate license:</strong> This text is meant to be displayed in a preview context, whereas real-time <code>EventTextListener</code> texts are meant to be used
 for spoken voice announcements during a trip.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The maneuver instruction. The text is formatted and localized as specified via
     <a href="sdk-for-android-navigate-com-here-sdk-routing-routetextoptions" title="class in com.here.sdk.routing"><code>RouteTextOptions</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSectionIndex()">
<h3>getSectionIndex</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">getSectionIndex</span>()</div>
<div className="block"><p>Gets the index over <a href="sdk-for-android-navigate-route#getSections()"><code>Route.getSections()</code></a> indicating the section to which the maneuver belongs to.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Index over <a href="sdk-for-android-navigate-route#getSections()"><code>Route.getSections()</code></a> indicating the section to which the maneuver belongs to.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSpanIndex()">
<h3>getSpanIndex</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">getSpanIndex</span>()</div>
<div className="block"><p>Gets the index over <a href="sdk-for-android-navigate-section#getSpans()"><code>Section.getSpans()</code></a> indicating the first span after the maneuver point.
 <strong>Note:</strong> The span index for the last maneuvers (those maneuvers with maneuver action set to
 <a href="sdk-for-android-navigate-maneuveraction#ARRIVE"><code>ManeuverAction.ARRIVE</code></a>) cannot be used, since these maneuvers are placed after the last span of the route and
 the span index for them would be greater than the span list size.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Index over <a href="sdk-for-android-navigate-section#getSpans()"><code>Section.getSpans()</code></a> indicating the first span after the maneuver point.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDuration()">
<h3>getDuration</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span className="element-name">getDuration</span>()</div>
<div className="block"><p>Gets the estimated time in seconds needed to perform the maneuver.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The estimated time in seconds needed to perform the maneuver.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTurnAngleInDegrees()">
<h3>getTurnAngleInDegrees</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">getTurnAngleInDegrees</span>()</div>
<div className="block"><p>Gets the angle of the turn component of the maneuver. The value is in degrees and from -180 to 180.
 The angle increases clockwise and small values are used for going straight, i.e. a positive number
 means there is a right turn and a negative number is a left turn.
 Some maneuvers like Depart, Arrive and Roundabout pass doesn't have a well defined angle, so the value
 is omitted.
 <strong>Note:</strong> These attributes are only available for the Navigate license.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The angle of the turn component of the maneuver.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getRoundaboutAngleInDegrees()">
<h3>getRoundaboutAngleInDegrees</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">getRoundaboutAngleInDegrees</span>()</div>
<div className="block"><p>The angle is estimated between the incoming and outgoing route parts before entering the actual roundabout.
 This is done to provide a better orientation for drivers. For better results, the incoming and outcoming route
 parts can be around 50 meters in length. In addition, these parts lie usually around 30 meters away from
 the actual roundabout. Therefore, the resulting arc does not necessarily represent the exact curved path a
 vehicle has to follow within a roundabout from the point of entry to the point of exit. Instead, it reflects
 the route path before and after the roundabout to highlight the directional change along the route. The angle can have a value from -360.0 to 360.0, and it is positive
 in right-hand side driving country, and negative in left-hand side countries.
 Note that the value is available for both the enter roundabout actions and the exit roundabout
 actions. Both maneuvers have the same value. When the incoming or outgoing route parts are curvy or when the
 roundabout itself is not representing a perfect circle, then the accuracy of the angle may be
 compromised.
 <strong>Note:</strong> These attributes are only available for the Navigate license.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The angle is estimated between the incoming and outgoing route parts before entering the actual roundabout.</p></dd>
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
