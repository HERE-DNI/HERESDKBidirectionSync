---
title: "Maneuver (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-maneuver"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- Maneuver.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-explore-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.routing.Maneuver</div>
</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">Maneuver</span>
<span class="extends-implements">extends <a href="sdk-for-android-explore-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>This class provides all the information for a maneuver. The directional information (e.g. road names, road
 numbers and signpost direction) is stored in <a href="sdk-for-android-explore-com-here-sdk-routing-maneuver#getRoadTexts()"><code>getRoadTexts()</code></a> and <a href="sdk-for-android-explore-com-here-sdk-routing-maneuver#getNextRoadTexts()"><code>getNextRoadTexts()</code></a> attributes.
 As for the motorway exit information, it can be obtained from <a href="sdk-for-android-explore-com-here-sdk-routing-maneuver#getExitSignTexts()"><code>getExitSignTexts()</code></a> attribute.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-com-here-sdk-routing-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-maneuver#getAction()">getAction</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the maneuver action.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-maneuver#getCoordinates()">getCoordinates</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the geographic coordinates where the maneuver is located.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-maneuver#getCountryCode()">getCountryCode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the country code of the maneuver position.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-duration" title="class in com.here.time">Duration</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-maneuver#getDuration()">getDuration</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the estimated time in seconds needed to perform the maneuver.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-localizedtexts" title="class in com.here.sdk.core">LocalizedTexts</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-maneuver#getExitSignTexts()">getExitSignTexts</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the textual attributes of the exit sign.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-localizedtexts" title="class in com.here.sdk.core">LocalizedTexts</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-maneuver#getIntersectionNames()">getIntersectionNames</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the textual attributes of the intersection.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-maneuver#getLengthInMeters()">getLengthInMeters</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the length of the maneuver in meters.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-com-here-sdk-routing-roadtexts" title="class in com.here.sdk.routing">RoadTexts</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-maneuver#getNextRoadTexts()">getNextRoadTexts</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the textual attributes of the next road containing the corresponding road name(s) and road number(s) after the maneuver point.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-maneuver#getOffset()">getOffset</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the index over <a href="sdk-for-android-explore-section#getGeometry()"><code>Section.getGeometry()</code></a> where the maneuver is located.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-com-here-sdk-routing-roadtexts" title="class in com.here.sdk.routing">RoadTexts</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-maneuver#getRoadTexts()">getRoadTexts</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the textual attributes of the current road containing road names, road numbers and signpost direction (towards) information.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-maneuver#getRoundaboutAngleInDegrees()">getRoundaboutAngleInDegrees</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The angle is estimated between the incoming and outgoing route parts before entering the actual roundabout.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-maneuver#getSectionIndex()">getSectionIndex</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the index over <a href="sdk-for-android-explore-route#getSections()"><code>Route.getSections()</code></a> indicating the section to which the maneuver belongs to.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-com-here-sdk-routing-signpost" title="class in com.here.sdk.routing">Signpost</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-maneuver#getSignpost()">getSignpost</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets <a href="sdk-for-android-explore-com-here-sdk-routing-signpost" title="class in com.here.sdk.routing"><code>Signpost</code></a> object.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-maneuver#getSpanIndex()">getSpanIndex</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the index over <a href="sdk-for-android-explore-section#getSpans()"><code>Section.getSpans()</code></a> indicating the first span after the maneuver point.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-maneuver#getText()">getText</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the maneuver instruction.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-maneuver#getTurnAngleInDegrees()">getTurnAngleInDegrees</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the angle of the turn component of the maneuver.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="getAction()">
<h3>getAction</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-routing-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">getAction</span>()</div>
<div class="block"><p>Gets the maneuver action.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Indicates the maneuver action.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCoordinates()">
<h3>getCoordinates</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span class="element-name">getCoordinates</span>()</div>
<div class="block"><p>Gets the geographic coordinates where the maneuver is located.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Geographic coordinates where the maneuver is located.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOffset()">
<h3>getOffset</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getOffset</span>()</div>
<div class="block"><p>Gets the index over <a href="sdk-for-android-explore-section#getGeometry()"><code>Section.getGeometry()</code></a> where the maneuver is located.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Index over <a href="sdk-for-android-explore-section#getGeometry()"><code>Section.getGeometry()</code></a> where the maneuver is located.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCountryCode()">
<h3>getCountryCode</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getCountryCode</span>()</div>
<div class="block"><p>Gets the country code of the maneuver position. The value is <code>null</code> when no data is available.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The country code of the maneuver position. The value is <code>null</code> when no data is available.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getExitSignTexts()">
<h3>getExitSignTexts</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-localizedtexts" title="class in com.here.sdk.core">LocalizedTexts</a></span> <span class="element-name">getExitSignTexts</span>()</div>
<div class="block"><p>Gets the textual attributes of the exit sign. These might contain exit number(s) and/or name(s).
 These attributes are only available for the Navigate license.
 Otherwise, the attributes are always empty.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The textual attributes of the exit sign. These might contain exit number(s) and/or name(s).</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLengthInMeters()">
<h3>getLengthInMeters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getLengthInMeters</span>()</div>
<div class="block"><p>Gets the length of the maneuver in meters.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The length of the maneuver in meters.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRoadTexts()">
<h3>getRoadTexts</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-routing-roadtexts" title="class in com.here.sdk.routing">RoadTexts</a></span> <span class="element-name">getRoadTexts</span>()</div>
<div class="block"><p>Gets the textual attributes of the current road containing road names, road numbers and signpost direction (towards) information.
 <strong>Note:</strong> These attributes are only available for the Navigate license.
 Otherwise, the attributes are always empty.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The textual attributes of the current road containing road names, road numbers and signpost direction (towards) information.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNextRoadTexts()">
<h3>getNextRoadTexts</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-routing-roadtexts" title="class in com.here.sdk.routing">RoadTexts</a></span> <span class="element-name">getNextRoadTexts</span>()</div>
<div class="block"><p>Gets the textual attributes of the next road containing the corresponding road name(s) and road number(s) after the maneuver point.
 These attributes are only available for the Navigate license.
 Otherwise, the attributes are always empty.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The textual attributes of the next road containing the corresponding road name(s) and road number(s) after the maneuver point.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSignpost()">
<h3>getSignpost</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-routing-signpost" title="class in com.here.sdk.routing">Signpost</a></span> <span class="element-name">getSignpost</span>()</div>
<div class="block"><p>Gets <a href="sdk-for-android-explore-com-here-sdk-routing-signpost" title="class in com.here.sdk.routing"><code>Signpost</code></a> object.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Gets the <a href="sdk-for-android-explore-com-here-sdk-routing-signpost" title="class in com.here.sdk.routing"><code>Signpost</code></a> object.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIntersectionNames()">
<h3>getIntersectionNames</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-localizedtexts" title="class in com.here.sdk.core">LocalizedTexts</a></span> <span class="element-name">getIntersectionNames</span>()</div>
<div class="block"><p>Gets the textual attributes of the intersection.
 These attributes are only available for the Navigate license.
 Otherwise, the attributes are always empty.
 <strong>Note:</strong> Routes calculated with OfflineRoutingEngine are not supported.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The textual attributes of the intersection.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getText()">
<h3>getText</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getText</span>()</div>
<div class="block"><p>Gets the maneuver instruction. The text is formatted and localized as specified via
 <a href="sdk-for-android-explore-com-here-sdk-routing-routetextoptions" title="class in com.here.sdk.routing"><code>RouteTextOptions</code></a>.
 <strong>Note for users of the Navigate license:</strong> This text is meant to be displayed in a preview context, whereas real-time <code>EventTextListener</code> texts are meant to be used
 for spoken voice announcements during a trip.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The maneuver instruction. The text is formatted and localized as specified via
     <a href="sdk-for-android-explore-com-here-sdk-routing-routetextoptions" title="class in com.here.sdk.routing"><code>RouteTextOptions</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSectionIndex()">
<h3>getSectionIndex</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getSectionIndex</span>()</div>
<div class="block"><p>Gets the index over <a href="sdk-for-android-explore-route#getSections()"><code>Route.getSections()</code></a> indicating the section to which the maneuver belongs to.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Index over <a href="sdk-for-android-explore-route#getSections()"><code>Route.getSections()</code></a> indicating the section to which the maneuver belongs to.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSpanIndex()">
<h3>getSpanIndex</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getSpanIndex</span>()</div>
<div class="block"><p>Gets the index over <a href="sdk-for-android-explore-section#getSpans()"><code>Section.getSpans()</code></a> indicating the first span after the maneuver point.
 <strong>Note:</strong> The span index for the last maneuvers (those maneuvers with maneuver action set to
 <a href="sdk-for-android-explore-maneuveraction#ARRIVE"><code>ManeuverAction.ARRIVE</code></a>) cannot be used, since these maneuvers are placed after the last span of the route and
 the span index for them would be greater than the span list size.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Index over <a href="sdk-for-android-explore-section#getSpans()"><code>Section.getSpans()</code></a> indicating the first span after the maneuver point.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDuration()">
<h3>getDuration</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">getDuration</span>()</div>
<div class="block"><p>Gets the estimated time in seconds needed to perform the maneuver.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The estimated time in seconds needed to perform the maneuver.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTurnAngleInDegrees()">
<h3>getTurnAngleInDegrees</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">getTurnAngleInDegrees</span>()</div>
<div class="block"><p>Gets the angle of the turn component of the maneuver. The value is in degrees and from -180 to 180.
 The angle increases clockwise and small values are used for going straight, i.e. a positive number
 means there is a right turn and a negative number is a left turn.
 Some maneuvers like Depart, Arrive and Roundabout pass doesn't have a well defined angle, so the value
 is omitted.
 <strong>Note:</strong> These attributes are only available for the Navigate license.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The angle of the turn component of the maneuver.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRoundaboutAngleInDegrees()">
<h3>getRoundaboutAngleInDegrees</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">getRoundaboutAngleInDegrees</span>()</div>
<div class="block"><p>The angle is estimated between the incoming and outgoing route parts before entering the actual roundabout.
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
<dl class="notes">
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
`
}</HTMLBlock>
