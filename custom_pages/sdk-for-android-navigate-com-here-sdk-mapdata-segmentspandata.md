---
title: "SegmentSpanData (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapdata-segmentspandata"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- SegmentSpanData.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapdata.SegmentSpanData</div>
</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">SegmentSpanData</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Contains attributes that are not necessarily constant on a full segment.
 A Span is a portion of a Segment where the requested attributes are constant.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-administrativerules" title="class in com.here.sdk.mapdata">AdministrativeRules</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspandata#getAdministrativeRules()">getAdministrativeRules</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the <a href="sdk-for-android-navigate-administrativerules" title="class in com.here.sdk.mapdata"><code>AdministrativeRules</code></a> for the segment.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-allowedtransportmodes" title="class in com.here.sdk.mapdata">AllowedTransportModes</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspandata#getAllowedTransportModes()">getAllowedTransportModes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the <a href="sdk-for-android-navigate-allowedtransportmodes" title="class in com.here.sdk.mapdata"><code>AllowedTransportModes</code></a> object.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspandata#getBaseSpeedInMetersPerSecond()">getBaseSpeedInMetersPerSecond</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the average speed for this segment span.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-functionalroadclass" title="enum class in com.here.sdk.routing">FunctionalRoadClass</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspandata#getFunctionalRoadClass()">getFunctionalRoadClass</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the <a href="sdk-for-android-navigate-functionalroadclass" title="enum class in com.here.sdk.routing"><code>FunctionalRoadClass</code></a> object representing the polyline of this section.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-localroadcharacteristic" title="enum class in com.here.sdk.mapdata">LocalRoadCharacteristic</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspandata#getLocalRoadCharacteristics()">getLocalRoadCharacteristics</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the local road characteristics.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspandata#getNegativeDirectionBaseSpeedInMetersPerSecond()">getNegativeDirectionBaseSpeedInMetersPerSecond</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the average speed in the negative direction.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-segmentspeedlimit" title="class in com.here.sdk.mapdata">SegmentSpeedLimit</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspandata#getNegativeDirectionSpeedLimit()">getNegativeDirectionSpeedLimit</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the <a href="sdk-for-android-navigate-segmentspeedlimit" title="class in com.here.sdk.mapdata"><code>SegmentSpeedLimit</code></a> object representing the speed limit of this segment span.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-physicalattributes" title="class in com.here.sdk.mapdata">PhysicalAttributes</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspandata#getPhysicalAttributes()">getPhysicalAttributes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the physical attributes.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspandata#getPositiveDirectionBaseSpeedInMetersPerSecond()">getPositiveDirectionBaseSpeedInMetersPerSecond</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the average speed in the positive direction.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-segmentspeedlimit" title="class in com.here.sdk.mapdata">SegmentSpeedLimit</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspandata#getPositiveDirectionSpeedLimit()">getPositiveDirectionSpeedLimit</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the <a href="sdk-for-android-navigate-segmentspeedlimit" title="class in com.here.sdk.mapdata"><code>SegmentSpeedLimit</code></a> object representing the speed limit of this segment span.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-localizedroadnumbers" title="class in com.here.sdk.routing">LocalizedRoadNumbers</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspandata#getRoadNumbers()">getRoadNumbers</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the road numbers on the span enriched with information specific to <em>route numbers</em>
 of a road such as I-10, US-50, or A3.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-roadusages" title="class in com.here.sdk.mapdata">RoadUsages</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspandata#getRoadUsages()">getRoadUsages</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the road usages.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspandata#getSpanLengthInMeters()">getSpanLengthInMeters</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the length of this span in meters.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-segmentspecialspeedsituation" title="class in com.here.sdk.mapdata">SegmentSpecialSpeedSituation</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspandata#getSpecialSpeedSituations()">getSpecialSpeedSituations</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the list of <a href="sdk-for-android-navigate-segmentspecialspeedsituation" title="class in com.here.sdk.mapdata"><code>SegmentSpecialSpeedSituation</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-segmentspeedlimit" title="class in com.here.sdk.mapdata">SegmentSpeedLimit</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspandata#getSpeedLimit()">getSpeedLimit</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the <a href="sdk-for-android-navigate-segmentspeedlimit" title="class in com.here.sdk.mapdata"><code>SegmentSpeedLimit</code></a> object representing the speed limit of this segment span.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspandata#getStartOffsetInMeters()">getStartOffsetInMeters</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the start offset in meters of the span.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-localizedtexts" title="class in com.here.sdk.core">LocalizedTexts</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspandata#getStreetNames()">getStreetNames</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The street names on the span.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-traveldirection" title="enum class in com.here.sdk.routing">TravelDirection</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspandata#getTravelDirection()">getTravelDirection</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the <a href="sdk-for-android-navigate-traveldirection" title="enum class in com.here.sdk.routing"><code>TravelDirection</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspandata#isUrban()">isUrban</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the urban attribute of the segment.</div>
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
<section class="detail" id="getStartOffsetInMeters()">
<h3>getStartOffsetInMeters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getStartOffsetInMeters</span>()</div>
<div class="block"><p>Gets the start offset in meters of the span.
 The offset in meters from the beginning of the segment to the start of the span
 in positive direction or from the end of the segment to the start of the span in negative direction.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Start offset.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSpanLengthInMeters()">
<h3>getSpanLengthInMeters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getSpanLengthInMeters</span>()</div>
<div class="block"><p>Gets the length of this span in meters.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The length of this span in meters.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTravelDirection()">
<h3>getTravelDirection</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-traveldirection" title="enum class in com.here.sdk.routing">TravelDirection</a></span> <span class="element-name">getTravelDirection</span>()</div>
<div class="block"><p>Gets the <a href="sdk-for-android-navigate-traveldirection" title="enum class in com.here.sdk.routing"><code>TravelDirection</code></a>.
 Gets the <a href="sdk-for-android-navigate-traveldirection" title="enum class in com.here.sdk.routing"><code>TravelDirection</code></a> object for the portion of the segment.
 Returns <code>null</code> if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadTravelDirection"><code>SegmentDataLoaderOptions.loadTravelDirection</code></a> is set to <code>false</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-traveldirection" title="enum class in com.here.sdk.routing"><code>TravelDirection</code></a> object representing the allowed travel directions.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAllowedTransportModes()">
<h3>getAllowedTransportModes</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-allowedtransportmodes" title="class in com.here.sdk.mapdata">AllowedTransportModes</a></span> <span class="element-name">getAllowedTransportModes</span>()</div>
<div class="block"><p>Gets the <a href="sdk-for-android-navigate-allowedtransportmodes" title="class in com.here.sdk.mapdata"><code>AllowedTransportModes</code></a> object.
 Returns <code>null</code> if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadTransportModesAccess"><code>SegmentDataLoaderOptions.loadTransportModesAccess</code></a> is set to <code>false</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-allowedtransportmodes" title="class in com.here.sdk.mapdata"><code>AllowedTransportModes</code></a> object representing the allowed transport modes.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFunctionalRoadClass()">
<h3>getFunctionalRoadClass</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-functionalroadclass" title="enum class in com.here.sdk.routing">FunctionalRoadClass</a></span> <span class="element-name">getFunctionalRoadClass</span>()</div>
<div class="block"><p>Gets the <a href="sdk-for-android-navigate-functionalroadclass" title="enum class in com.here.sdk.routing"><code>FunctionalRoadClass</code></a> object representing the polyline of this section.
 Returns <code>null</code> if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadFunctionalRoadClass"><code>SegmentDataLoaderOptions.loadFunctionalRoadClass</code></a> is set to <code>false</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-functionalroadclass" title="enum class in com.here.sdk.routing"><code>FunctionalRoadClass</code></a> object representing the polyline of this segment.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPositiveDirectionSpeedLimit()">
<h3>getPositiveDirectionSpeedLimit</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-segmentspeedlimit" title="class in com.here.sdk.mapdata">SegmentSpeedLimit</a></span> <span class="element-name">getPositiveDirectionSpeedLimit</span>()</div>
<div class="block"><p>Gets the <a href="sdk-for-android-navigate-segmentspeedlimit" title="class in com.here.sdk.mapdata"><code>SegmentSpeedLimit</code></a> object representing the speed limit of this segment span.
 Returns <code>null</code> if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadSpeedLimits"><code>SegmentDataLoaderOptions.loadSpeedLimits</code></a> is set to <code>false</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-segmentspeedlimit" title="class in com.here.sdk.mapdata"><code>SegmentSpeedLimit</code></a> object representing the speed limit of this segment span in the positive
     tavel direction.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNegativeDirectionSpeedLimit()">
<h3>getNegativeDirectionSpeedLimit</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-segmentspeedlimit" title="class in com.here.sdk.mapdata">SegmentSpeedLimit</a></span> <span class="element-name">getNegativeDirectionSpeedLimit</span>()</div>
<div class="block"><p>Gets the <a href="sdk-for-android-navigate-segmentspeedlimit" title="class in com.here.sdk.mapdata"><code>SegmentSpeedLimit</code></a> object representing the speed limit of this segment span.
 Returns <code>null</code> if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadSpeedLimits"><code>SegmentDataLoaderOptions.loadSpeedLimits</code></a> is set to <code>false</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-segmentspeedlimit" title="class in com.here.sdk.mapdata"><code>SegmentSpeedLimit</code></a> object representing the speed limit of this segment span in the negative
     travel direction.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSpeedLimit()">
<h3>getSpeedLimit</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-segmentspeedlimit" title="class in com.here.sdk.mapdata">SegmentSpeedLimit</a></span> <span class="element-name">getSpeedLimit</span>()</div>
<div class="block"><p>Gets the <a href="sdk-for-android-navigate-segmentspeedlimit" title="class in com.here.sdk.mapdata"><code>SegmentSpeedLimit</code></a> object representing the speed limit of this segment span.
 Will be loaded if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadSpeedLimits"><code>SegmentDataLoaderOptions.loadSpeedLimits</code></a> is <code>true</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-segmentspeedlimit" title="class in com.here.sdk.mapdata"><code>SegmentSpeedLimit</code></a> object representing the speed limit of this segment span.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPositiveDirectionBaseSpeedInMetersPerSecond()">
<h3>getPositiveDirectionBaseSpeedInMetersPerSecond</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">getPositiveDirectionBaseSpeedInMetersPerSecond</span>()</div>
<div class="block"><p>Gets the average speed in the positive direction.
 Returns <code>null</code> if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadBaseSpeeds"><code>SegmentDataLoaderOptions.loadBaseSpeeds</code></a> is set to <code>false</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The average speed expected for this segment in positive direction with a car or a similar
     vehicle.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNegativeDirectionBaseSpeedInMetersPerSecond()">
<h3>getNegativeDirectionBaseSpeedInMetersPerSecond</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">getNegativeDirectionBaseSpeedInMetersPerSecond</span>()</div>
<div class="block"><p>Gets the average speed in the negative direction.
 Returns <code>null</code> if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadBaseSpeeds"><code>SegmentDataLoaderOptions.loadBaseSpeeds</code></a> is set to <code>false</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The average speed expected for this segment in negative direction with a car or a similar
     vehicle.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBaseSpeedInMetersPerSecond()">
<h3>getBaseSpeedInMetersPerSecond</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">getBaseSpeedInMetersPerSecond</span>()</div>
<div class="block"><p>Gets the average speed for this segment span.
 Will be loaded if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadBaseSpeeds"><code>SegmentDataLoaderOptions.loadBaseSpeeds</code></a> is <code>true</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The average speed expected for this segment span with a car or a similar vehicle.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLocalRoadCharacteristics()">
<h3>getLocalRoadCharacteristics</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-localroadcharacteristic" title="enum class in com.here.sdk.mapdata">LocalRoadCharacteristic</a>&gt;</span> <span class="element-name">getLocalRoadCharacteristics</span>()</div>
<div class="block"><p>Gets the local road characteristics.
 Returns <code>null</code> if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadLocalRoadCharacteristics"><code>SegmentDataLoaderOptions.loadLocalRoadCharacteristics</code></a> is set to <code>false</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The local road characteristics of the segment: frontage, parking lot road, or POI access road.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStreetNames()">
<h3>getStreetNames</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-localizedtexts" title="class in com.here.sdk.core">LocalizedTexts</a></span> <span class="element-name">getStreetNames</span>()</div>
<div class="block"><p>The street names on the span.
 Returns <code>null</code> if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadStreetNamesAndRoadNumbers"><code>SegmentDataLoaderOptions.loadStreetNamesAndRoadNumbers</code></a> is set to <code>false</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The street names on the span.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRoadNumbers()">
<h3>getRoadNumbers</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-localizedroadnumbers" title="class in com.here.sdk.routing">LocalizedRoadNumbers</a></span> <span class="element-name">getRoadNumbers</span>()</div>
<div class="block"><p>Gets the road numbers on the span enriched with information specific to <em>route numbers</em>
 of a road such as I-10, US-50, or A3.
 Returns <code>null</code> if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadStreetNamesAndRoadNumbers"><code>SegmentDataLoaderOptions.loadStreetNamesAndRoadNumbers</code></a> is set to <code>false</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The road numbers on the span enriched with information specific to <em>route numbers</em>
     of a road such as I-10, US-50, or A3.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPhysicalAttributes()">
<h3>getPhysicalAttributes</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-physicalattributes" title="class in com.here.sdk.mapdata">PhysicalAttributes</a></span> <span class="element-name">getPhysicalAttributes</span>()</div>
<div class="block"><p>Gets the physical attributes.
 Returns <code>null</code> if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadRoadAttributes"><code>SegmentDataLoaderOptions.loadRoadAttributes</code></a> is set to <code>false</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The physical attributes of the segment.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRoadUsages()">
<h3>getRoadUsages</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-roadusages" title="class in com.here.sdk.mapdata">RoadUsages</a></span> <span class="element-name">getRoadUsages</span>()</div>
<div class="block"><p>Gets the road usages.
 Returns <code>null</code> if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadRoadAttributes"><code>SegmentDataLoaderOptions.loadRoadAttributes</code></a> is set to <code>false</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The road usages of the segment.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAdministrativeRules()">
<h3>getAdministrativeRules</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-administrativerules" title="class in com.here.sdk.mapdata">AdministrativeRules</a></span> <span class="element-name">getAdministrativeRules</span>()</div>
<div class="block"><p>Gets the <a href="sdk-for-android-navigate-administrativerules" title="class in com.here.sdk.mapdata"><code>AdministrativeRules</code></a> for the segment.
 Returns <code>null</code> if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadAdministrativeRules"><code>SegmentDataLoaderOptions.loadAdministrativeRules</code></a> is set to <code>false</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-administrativerules" title="class in com.here.sdk.mapdata"><code>AdministrativeRules</code></a> for the segment, containing information
     about country code, state code, unit system, tolls, pre-trip planning and other
     administrative information.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isUrban()">
<h3>isUrban</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html" title="class or interface in java.lang">Boolean</a></span> <span class="element-name">isUrban</span>()</div>
<div class="block"><p>Gets the urban attribute of the segment.
 Returns <code>null</code> if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadUrban"><code>SegmentDataLoaderOptions.loadUrban</code></a> is set to <code>false</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The urban attribute of the segment.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSpecialSpeedSituations()">
<h3>getSpecialSpeedSituations</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-segmentspecialspeedsituation" title="class in com.here.sdk.mapdata">SegmentSpecialSpeedSituation</a>&gt;</span> <span class="element-name">getSpecialSpeedSituations</span>()</div>
<div class="block"><p>Gets the list of <a href="sdk-for-android-navigate-segmentspecialspeedsituation" title="class in com.here.sdk.mapdata"><code>SegmentSpecialSpeedSituation</code></a>.
 Will be loaded if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadSpecialSpeedSituations"><code>SegmentDataLoaderOptions.loadSpecialSpeedSituations</code></a> is <code>true</code>.
 <strong>Note:</strong> To get timezone offset and daylight saving time values for TimeRule, [sdk.mapdata.SegmentDataLoaderOptions.load_administrative_rules] must also be set to <code>true</code>.</p></div>
<dl class="notes">
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
`
}</HTMLBlock>
