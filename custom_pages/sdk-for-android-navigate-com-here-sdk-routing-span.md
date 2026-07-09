---
title: "Span (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-span"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- Span.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.routing</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.routing.Span</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">Span</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>A span is a part of the <a href="sdk-for-android-navigate-com-here-sdk-routing-section" title="class in com.here.sdk.routing"><code>Section</code></a> which is traversable or navigable. Each span
 usually has some geometry associated with it.</p></div>
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
<section className="detail" id="getShieldText(com.here.sdk.routing.LocalizedRoadNumber)">
<h3>getShieldText</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getShieldText</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-localizedroadnumber" title="class in com.here.sdk.routing">LocalizedRoadNumber</a> roadNumber)</span></div>
<div className="block"><p>Converts full route number to the value to be displayed on the road shield.
 The results are based on country code and state code of <code>Span</code> object and route type of passed <code>road_number</code> argument.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>roadNumber</code> - <p>Route number to convert to shield text.</p></dd>
<dt>Returns:</dt>
<dd><p>Text on the road shield to display.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getGeometry()">
<h3>getGeometry</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geopolyline" title="class in com.here.sdk.core">GeoPolyline</a></span> <span className="element-name">getGeometry</span>()</div>
<div className="block"><p>Gets the <a href="sdk-for-android-navigate-com-here-sdk-core-geopolyline" title="class in com.here.sdk.core"><code>GeoPolyline</code></a> object representing the polyline of this span.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-com-here-sdk-core-geopolyline" title="class in com.here.sdk.core"><code>GeoPolyline</code></a> object representing the polyline of this span.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getLengthInMeters()">
<h3>getLengthInMeters</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">getLengthInMeters</span>()</div>
<div className="block"><p>Gets the length of this span in meters.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The length of this span in meters.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getNoticeIndexes()">
<h3>getNoticeIndexes</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt;</span> <span className="element-name">getNoticeIndexes</span>()</div>
<div className="block"><p>Gets the list of indexes to <a href="sdk-for-android-navigate-section#getSectionNotices()"><code>Section.getSectionNotices()</code></a> the parent section owns.
 In case the list is not empty, the user must judge all the indexed <a href="sdk-for-android-navigate-com-here-sdk-routing-sectionnotice" title="class in com.here.sdk.routing"><code>SectionNotice</code></a>'s
 carefully before proceeding.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The list of indexes to <a href="sdk-for-android-navigate-section#getSectionNotices()"><code>Section.getSectionNotices()</code></a> the parent section owns.
     In case the list is not empty, the user must judge all the indexed <a href="sdk-for-android-navigate-com-here-sdk-routing-sectionnotice" title="class in com.here.sdk.routing"><code>SectionNotice</code></a>s
     carefully before proceeding.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSegmentReference()">
<h3>getSegmentReference</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference" title="class in com.here.sdk.routing">SegmentReference</a></span> <span className="element-name">getSegmentReference</span>()</div>
<div className="block"><p>Gets the segment reference of this span.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The segment reference of this span.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTrafficIncidentIndexes()">
<h3>getTrafficIncidentIndexes</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt;</span> <span className="element-name">getTrafficIncidentIndexes</span>()</div>
<div className="block"><p>The indexes of traffic incidents from the field <a href="sdk-for-android-navigate-section#getTrafficIncidents()"><code>Section.getTrafficIncidents()</code></a> of the parent <a href="sdk-for-android-navigate-com-here-sdk-routing-section" title="class in com.here.sdk.routing"><code>Section</code></a>.
 Each matching incident takes at least a whole <a href="sdk-for-android-navigate-com-here-sdk-routing-span#getGeometry()"><code>getGeometry()</code></a>.
 The same incident can take other spans and an area out of the built route as well.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The indexes of traffic incidents from the field <a href="sdk-for-android-navigate-section#getTrafficIncidents()"><code>Section.getTrafficIncidents()</code></a> of the parent <a href="sdk-for-android-navigate-com-here-sdk-routing-section" title="class in com.here.sdk.routing"><code>Section</code></a>.
     Each matching incident takes at least a whole <a href="sdk-for-android-navigate-com-here-sdk-routing-span#getGeometry()"><code>getGeometry()</code></a>.
     The same incident can take other spans and an area out of the built route as well.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSectionPolylineOffset()">
<h3>getSectionPolylineOffset</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">getSectionPolylineOffset</span>()</div>
<div className="block"><p>Gets the position of the span inside the section's geometry, given as an offset. The span geometry starts from
 this offset and ends on the offset of the next span, both start offset point and end offset point being
 included in the span, because the spans' geometry share a point in the section's geometry.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The position of the span inside the section's geometry, given as an offset. The span geometry starts from
     this offset and ends on the offset of the next span, both start offset point and end offset point being
     included in the span, because the spans' geometry share a point in the section's geometry.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDynamicSpeedInfo()">
<h3>getDynamicSpeedInfo</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-dynamicspeedinfo" title="class in com.here.sdk.routing">DynamicSpeedInfo</a></span> <span className="element-name">getDynamicSpeedInfo</span>()</div>
<div className="block"><p>The dynamic speed information on the span.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The dynamic speed information on the span.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getStreetAttributes()">
<h3>getStreetAttributes</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-streetattributes" title="enum class in com.here.sdk.routing">StreetAttributes</a>&gt;</span> <span className="element-name">getStreetAttributes</span>()</div>
<div className="block"><p>The list of street attributes on the span.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The list of street attributes on the span.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getCarAttributes()">
<h3>getCarAttributes</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-accessattributes" title="enum class in com.here.sdk.routing">AccessAttributes</a>&gt;</span> <span className="element-name">getCarAttributes</span>()</div>
<div className="block"><p>The list of car access attributes on the span.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The list of car access attributes on the span.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTruckAttributes()">
<h3>getTruckAttributes</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-accessattributes" title="enum class in com.here.sdk.routing">AccessAttributes</a>&gt;</span> <span className="element-name">getTruckAttributes</span>()</div>
<div className="block"><p>The list of truck access attributes on the span.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The list of truck access attributes on the span.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getScooterAttributes()">
<h3>getScooterAttributes</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-accessattributes" title="enum class in com.here.sdk.routing">AccessAttributes</a>&gt;</span> <span className="element-name">getScooterAttributes</span>()</div>
<div className="block"><p>The list of scooter access attributes on the span.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The list of scooter access attributes on the span.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getWalkAttributes()">
<h3>getWalkAttributes</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-walkattributes" title="enum class in com.here.sdk.routing">WalkAttributes</a>&gt;</span> <span className="element-name">getWalkAttributes</span>()</div>
<div className="block"><p>The list of walk attributes on the span.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The list of walk attributes on the span.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getStreetNames()">
<h3>getStreetNames</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtexts" title="class in com.here.sdk.core">LocalizedTexts</a></span> <span className="element-name">getStreetNames</span>()</div>
<div className="block"><p>The street names on the span.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The street names on the span.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getRoadNumbers()">
<h3>getRoadNumbers</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-localizedroadnumbers" title="class in com.here.sdk.routing">LocalizedRoadNumbers</a></span> <span className="element-name">getRoadNumbers</span>()</div>
<div className="block"><p>Gets the road numbers on the span enriched with information specific to <em>route numbers</em>
 of a road such as I-10, US-50, or A3, and cardinal direction, if available, and a road level classification (<code>RouteType</code>).</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The road numbers on the span enriched with information specific to <em>route numbers</em>
     of a road such as I-10, US-50, or A3, and cardinal direction, if available, and a road level classification (<code>RouteType</code>).</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSpeedLimitInMetersPerSecond()">
<h3>getSpeedLimitInMetersPerSecond</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">getSpeedLimitInMetersPerSecond</span>()</div>
<div className="block"><p>Gets the speed limit in meters per second on the span.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The speed limit in meters per second on the span.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getConsumptionInKilowattHours()">
<h3>getConsumptionInKilowattHours</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">getConsumptionInKilowattHours</span>()</div>
<div className="block"><p>Gets the power consumption in kilowatt per hour necessary to traverse the span.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The power consumption in kilowatt per hour necessary to traverse the span.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getFunctionalRoadClass()">
<h3>getFunctionalRoadClass</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-functionalroadclass" title="enum class in com.here.sdk.routing">FunctionalRoadClass</a></span> <span className="element-name">getFunctionalRoadClass</span>()</div>
<div className="block"><p>Gets the functional road class of the span.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The functional road class of the span.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDuration()">
<h3>getDuration</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span className="element-name">getDuration</span>()</div>
<div className="block"><p>Gets the time duration necessary to traverse the span, using the speed provided
 in <a href="sdk-for-android-navigate-com-here-sdk-routing-span#getDynamicSpeedInfo()"><code>getDynamicSpeedInfo()</code></a>. This duration takes also into
 consideration the delays caused by the traffic.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The time duration necessary to traverse the span, using the speed provided
     in <a href="sdk-for-android-navigate-com-here-sdk-routing-span#getDynamicSpeedInfo()"><code>getDynamicSpeedInfo()</code></a>. This duration takes also into
     consideration the delays caused by the traffic.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getBaseDuration()">
<h3>getBaseDuration</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span className="element-name">getBaseDuration</span>()</div>
<div className="block"><p>Gets the time duration necessary to traverse the span, using the speed provided
 in <a href="sdk-for-android-navigate-com-here-sdk-routing-span#getDynamicSpeedInfo()"><code>getDynamicSpeedInfo()</code></a> without taking into consideration
 the delays caused by the traffic.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The time duration necessary to traverse the span, using the speed provided
     in <a href="sdk-for-android-navigate-com-here-sdk-routing-span#getDynamicSpeedInfo()"><code>getDynamicSpeedInfo()</code></a> without taking into consideration
     the delays caused by the traffic.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getCountryCode()">
<h3>getCountryCode</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getCountryCode</span>()</div>
<div className="block"><p>Gets the country code of the span. The value is <code>null</code> when no data is available.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The country code of the span. The value is <code>null</code> when no data is available.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getStateCode()">
<h3>getStateCode</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getStateCode</span>()</div>
<div className="block"><p>Gets the state code of the span. State code is available in some countries to denote principal
 subdivisions(provinces or states), e.g. in the United States, AK stands for Alaska and OH stands for Ohio.
 The format of state code can vary for different countries, take the United States as example,
 it consists of two alphabet letters. The value is <code>null</code> when no data is available.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The state code of the span. State code is available in some countries to denote principal
     subdivisions(provinces or states), e.g. in the United States, AK stands for Alaska and OH stands for Ohio.
     The format of state code can vary for different countries, take the United States as example,
     it consists of two alphabet letters.
     The value is <code>null</code> when no data is available.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getNoThroughRestrictionsIndexes()">
<h3>getNoThroughRestrictionsIndexes</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt;</span> <span className="element-name">getNoThroughRestrictionsIndexes</span>()</div>
<div className="block"><p>Get the list of indexes to <a href="sdk-for-android-navigate-section#getNoThroughRestrictions()"><code>Section.getNoThroughRestrictions()</code></a> the parent section owns.
 In case the list is not empty, the user must judge all the indexed <a href="sdk-for-android-navigate-section#getNoThroughRestrictions()"><code>Section.getNoThroughRestrictions()</code></a>'s
 carefully before proceeding.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The list of indexes to <a href="sdk-for-android-navigate-section#getNoThroughRestrictions()"><code>Section.getNoThroughRestrictions()</code></a> the parent section owns.
     In case the list is not empty, the user must judge all the indexed sdk routing noThroughRestriction's
     carefully before proceeding.</p></dd>
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
