---
title: "SegmentSpanData (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapdata-segmentspandata"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- SegmentSpanData.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapdata</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapdata.SegmentSpanData</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">SegmentSpanData</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Contains attributes that are not necessarily constant on a full segment.
 A Span is a portion of a Segment where the requested attributes are constant.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
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
<section className="detail" id="getStartOffsetInMeters()">
<h3>getStartOffsetInMeters</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">getStartOffsetInMeters</span>()</div>
<div className="block"><p>Gets the start offset in meters of the span.
 The offset in meters from the beginning of the segment to the start of the span
 in positive direction or from the end of the segment to the start of the span in negative direction.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Start offset.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSpanLengthInMeters()">
<h3>getSpanLengthInMeters</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">getSpanLengthInMeters</span>()</div>
<div className="block"><p>Gets the length of this span in meters.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The length of this span in meters.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTravelDirection()">
<h3>getTravelDirection</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-traveldirection" title="enum class in com.here.sdk.routing">TravelDirection</a></span> <span className="element-name">getTravelDirection</span>()</div>
<div className="block"><p>Gets the <a href="sdk-for-android-navigate-com-here-sdk-routing-traveldirection" title="enum class in com.here.sdk.routing"><code>TravelDirection</code></a>.
 Gets the <a href="sdk-for-android-navigate-com-here-sdk-routing-traveldirection" title="enum class in com.here.sdk.routing"><code>TravelDirection</code></a> object for the portion of the segment.
 Returns <code>null</code> if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadTravelDirection"><code>SegmentDataLoaderOptions.loadTravelDirection</code></a> is set to <code>false</code>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-com-here-sdk-routing-traveldirection" title="enum class in com.here.sdk.routing"><code>TravelDirection</code></a> object representing the allowed travel directions.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getAllowedTransportModes()">
<h3>getAllowedTransportModes</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-allowedtransportmodes" title="class in com.here.sdk.mapdata">AllowedTransportModes</a></span> <span className="element-name">getAllowedTransportModes</span>()</div>
<div className="block"><p>Gets the <a href="sdk-for-android-navigate-com-here-sdk-mapdata-allowedtransportmodes" title="class in com.here.sdk.mapdata"><code>AllowedTransportModes</code></a> object.
 Returns <code>null</code> if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadTransportModesAccess"><code>SegmentDataLoaderOptions.loadTransportModesAccess</code></a> is set to <code>false</code>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-com-here-sdk-mapdata-allowedtransportmodes" title="class in com.here.sdk.mapdata"><code>AllowedTransportModes</code></a> object representing the allowed transport modes.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getFunctionalRoadClass()">
<h3>getFunctionalRoadClass</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-functionalroadclass" title="enum class in com.here.sdk.routing">FunctionalRoadClass</a></span> <span className="element-name">getFunctionalRoadClass</span>()</div>
<div className="block"><p>Gets the <a href="sdk-for-android-navigate-com-here-sdk-routing-functionalroadclass" title="enum class in com.here.sdk.routing"><code>FunctionalRoadClass</code></a> object representing the polyline of this section.
 Returns <code>null</code> if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadFunctionalRoadClass"><code>SegmentDataLoaderOptions.loadFunctionalRoadClass</code></a> is set to <code>false</code>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-com-here-sdk-routing-functionalroadclass" title="enum class in com.here.sdk.routing"><code>FunctionalRoadClass</code></a> object representing the polyline of this segment.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getPositiveDirectionSpeedLimit()">
<h3>getPositiveDirectionSpeedLimit</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspeedlimit" title="class in com.here.sdk.mapdata">SegmentSpeedLimit</a></span> <span className="element-name">getPositiveDirectionSpeedLimit</span>()</div>
<div className="block"><p>Gets the <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspeedlimit" title="class in com.here.sdk.mapdata"><code>SegmentSpeedLimit</code></a> object representing the speed limit of this segment span.
 Returns <code>null</code> if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadSpeedLimits"><code>SegmentDataLoaderOptions.loadSpeedLimits</code></a> is set to <code>false</code>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspeedlimit" title="class in com.here.sdk.mapdata"><code>SegmentSpeedLimit</code></a> object representing the speed limit of this segment span in the positive
     tavel direction.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getNegativeDirectionSpeedLimit()">
<h3>getNegativeDirectionSpeedLimit</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspeedlimit" title="class in com.here.sdk.mapdata">SegmentSpeedLimit</a></span> <span className="element-name">getNegativeDirectionSpeedLimit</span>()</div>
<div className="block"><p>Gets the <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspeedlimit" title="class in com.here.sdk.mapdata"><code>SegmentSpeedLimit</code></a> object representing the speed limit of this segment span.
 Returns <code>null</code> if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadSpeedLimits"><code>SegmentDataLoaderOptions.loadSpeedLimits</code></a> is set to <code>false</code>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspeedlimit" title="class in com.here.sdk.mapdata"><code>SegmentSpeedLimit</code></a> object representing the speed limit of this segment span in the negative
     travel direction.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSpeedLimit()">
<h3>getSpeedLimit</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspeedlimit" title="class in com.here.sdk.mapdata">SegmentSpeedLimit</a></span> <span className="element-name">getSpeedLimit</span>()</div>
<div className="block"><p>Gets the <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspeedlimit" title="class in com.here.sdk.mapdata"><code>SegmentSpeedLimit</code></a> object representing the speed limit of this segment span.
 Will be loaded if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadSpeedLimits"><code>SegmentDataLoaderOptions.loadSpeedLimits</code></a> is <code>true</code>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspeedlimit" title="class in com.here.sdk.mapdata"><code>SegmentSpeedLimit</code></a> object representing the speed limit of this segment span.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getPositiveDirectionBaseSpeedInMetersPerSecond()">
<h3>getPositiveDirectionBaseSpeedInMetersPerSecond</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">getPositiveDirectionBaseSpeedInMetersPerSecond</span>()</div>
<div className="block"><p>Gets the average speed in the positive direction.
 Returns <code>null</code> if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadBaseSpeeds"><code>SegmentDataLoaderOptions.loadBaseSpeeds</code></a> is set to <code>false</code>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The average speed expected for this segment in positive direction with a car or a similar
     vehicle.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getNegativeDirectionBaseSpeedInMetersPerSecond()">
<h3>getNegativeDirectionBaseSpeedInMetersPerSecond</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">getNegativeDirectionBaseSpeedInMetersPerSecond</span>()</div>
<div className="block"><p>Gets the average speed in the negative direction.
 Returns <code>null</code> if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadBaseSpeeds"><code>SegmentDataLoaderOptions.loadBaseSpeeds</code></a> is set to <code>false</code>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The average speed expected for this segment in negative direction with a car or a similar
     vehicle.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getBaseSpeedInMetersPerSecond()">
<h3>getBaseSpeedInMetersPerSecond</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">getBaseSpeedInMetersPerSecond</span>()</div>
<div className="block"><p>Gets the average speed for this segment span.
 Will be loaded if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadBaseSpeeds"><code>SegmentDataLoaderOptions.loadBaseSpeeds</code></a> is <code>true</code>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The average speed expected for this segment span with a car or a similar vehicle.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getLocalRoadCharacteristics()">
<h3>getLocalRoadCharacteristics</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapdata-localroadcharacteristic" title="enum class in com.here.sdk.mapdata">LocalRoadCharacteristic</a>&gt;</span> <span className="element-name">getLocalRoadCharacteristics</span>()</div>
<div className="block"><p>Gets the local road characteristics.
 Returns <code>null</code> if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadLocalRoadCharacteristics"><code>SegmentDataLoaderOptions.loadLocalRoadCharacteristics</code></a> is set to <code>false</code>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The local road characteristics of the segment: frontage, parking lot road, or POI access road.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getStreetNames()">
<h3>getStreetNames</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-localizedtexts" title="class in com.here.sdk.core">LocalizedTexts</a></span> <span className="element-name">getStreetNames</span>()</div>
<div className="block"><p>The street names on the span.
 Returns <code>null</code> if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadStreetNamesAndRoadNumbers"><code>SegmentDataLoaderOptions.loadStreetNamesAndRoadNumbers</code></a> is set to <code>false</code>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The street names on the span.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getRoadNumbers()">
<h3>getRoadNumbers</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-localizedroadnumbers" title="class in com.here.sdk.routing">LocalizedRoadNumbers</a></span> <span className="element-name">getRoadNumbers</span>()</div>
<div className="block"><p>Gets the road numbers on the span enriched with information specific to <em>route numbers</em>
 of a road such as I-10, US-50, or A3.
 Returns <code>null</code> if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadStreetNamesAndRoadNumbers"><code>SegmentDataLoaderOptions.loadStreetNamesAndRoadNumbers</code></a> is set to <code>false</code>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The road numbers on the span enriched with information specific to <em>route numbers</em>
     of a road such as I-10, US-50, or A3.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getPhysicalAttributes()">
<h3>getPhysicalAttributes</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-physicalattributes" title="class in com.here.sdk.mapdata">PhysicalAttributes</a></span> <span className="element-name">getPhysicalAttributes</span>()</div>
<div className="block"><p>Gets the physical attributes.
 Returns <code>null</code> if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadRoadAttributes"><code>SegmentDataLoaderOptions.loadRoadAttributes</code></a> is set to <code>false</code>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The physical attributes of the segment.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getRoadUsages()">
<h3>getRoadUsages</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-roadusages" title="class in com.here.sdk.mapdata">RoadUsages</a></span> <span className="element-name">getRoadUsages</span>()</div>
<div className="block"><p>Gets the road usages.
 Returns <code>null</code> if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadRoadAttributes"><code>SegmentDataLoaderOptions.loadRoadAttributes</code></a> is set to <code>false</code>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The road usages of the segment.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getAdministrativeRules()">
<h3>getAdministrativeRules</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules" title="class in com.here.sdk.mapdata">AdministrativeRules</a></span> <span className="element-name">getAdministrativeRules</span>()</div>
<div className="block"><p>Gets the <a href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules" title="class in com.here.sdk.mapdata"><code>AdministrativeRules</code></a> for the segment.
 Returns <code>null</code> if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadAdministrativeRules"><code>SegmentDataLoaderOptions.loadAdministrativeRules</code></a> is set to <code>false</code>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-com-here-sdk-mapdata-administrativerules" title="class in com.here.sdk.mapdata"><code>AdministrativeRules</code></a> for the segment, containing information
     about country code, state code, unit system, tolls, pre-trip planning and other
     administrative information.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="isUrban()">
<h3>isUrban</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span className="element-name">isUrban</span>()</div>
<div className="block"><p>Gets the urban attribute of the segment.
 Returns <code>null</code> if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadUrban"><code>SegmentDataLoaderOptions.loadUrban</code></a> is set to <code>false</code>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The urban attribute of the segment.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSpecialSpeedSituations()">
<h3>getSpecialSpeedSituations</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspecialspeedsituation" title="class in com.here.sdk.mapdata">SegmentSpecialSpeedSituation</a>&gt;</span> <span className="element-name">getSpecialSpeedSituations</span>()</div>
<div className="block"><p>Gets the list of <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspecialspeedsituation" title="class in com.here.sdk.mapdata"><code>SegmentSpecialSpeedSituation</code></a>.
 Will be loaded if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadSpecialSpeedSituations"><code>SegmentDataLoaderOptions.loadSpecialSpeedSituations</code></a> is <code>true</code>.
 <strong>Note:</strong> To get timezone offset and daylight saving time values for TimeRule, [sdk.mapdata.SegmentDataLoaderOptions.load_administrative_rules] must also be set to <code>true</code>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The special speed situations of the segment.</p></dd>
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
