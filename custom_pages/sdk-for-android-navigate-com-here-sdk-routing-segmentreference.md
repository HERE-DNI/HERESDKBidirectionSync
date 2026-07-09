---
title: "SegmentReference (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-segmentreference"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- SegmentReference.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.routing</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.routing.SegmentReference</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">SegmentReference</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Reference to a segment id with a travel direction.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang">Long</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference#localId">localId</a></code></div>
<div className="col-last even-row-color">
<div className="block">Local ID of the segment inside the OCM tile.</div>
</div>
<div className="col-first odd-row-color"><code>double</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference#offsetEnd">offsetEnd</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The end offset is a non-negative number between 0 and 1, representing the end of the referenced range using a proportion of the length of the segment.</div>
</div>
<div className="col-first even-row-color"><code>double</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference#offsetStart">offsetStart</a></code></div>
<div className="col-last even-row-color">
<div className="block">The start offset is a non-negative number between 0 and 1, representing the start of the referenced range using a proportion of the length of the segment.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference#segmentId">segmentId</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Topology segment id representing a unique identifier within the HERE platform catalogs.</div>
</div>
<div className="col-first even-row-color"><code>long</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference#tilePartitionId">tilePartitionId</a></code></div>
<div className="col-last even-row-color">
<div className="block">HERE tile partition id (Morton-encoding + level indicator) of the segment.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-traveldirection" title="enum class in com.here.sdk.routing">TravelDirection</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference#travelDirection">travelDirection</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Travel direction of the segment.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference#%3Cinit%3E()">SegmentReference</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference#%3Cinit%3E(java.lang.String)">SegmentReference</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> segmentId)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a new instance.</div>
</div>
<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference#%3Cinit%3E(java.lang.String,com.here.sdk.routing.TravelDirection)">SegmentReference</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> segmentId,
 <a href="sdk-for-android-navigate-com-here-sdk-routing-traveldirection" title="enum class in com.here.sdk.routing">TravelDirection</a> travelDirection)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference#%3Cinit%3E(java.lang.String,com.here.sdk.routing.TravelDirection,double)">SegmentReference</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> segmentId,
 <a href="sdk-for-android-navigate-com-here-sdk-routing-traveldirection" title="enum class in com.here.sdk.routing">TravelDirection</a> travelDirection,
 double offsetStart)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a new instance.</div>
</div>
<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference#%3Cinit%3E(java.lang.String,com.here.sdk.routing.TravelDirection,double,double)">SegmentReference</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> segmentId,
 <a href="sdk-for-android-navigate-com-here-sdk-routing-traveldirection" title="enum class in com.here.sdk.routing">TravelDirection</a> travelDirection,
 double offsetStart,
 double offsetEnd)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference#%3Cinit%3E(java.lang.String,com.here.sdk.routing.TravelDirection,double,double,long)">SegmentReference</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> segmentId,
 <a href="sdk-for-android-navigate-com-here-sdk-routing-traveldirection" title="enum class in com.here.sdk.routing">TravelDirection</a> travelDirection,
 double offsetStart,
 double offsetEnd,
 long tilePartitionId)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a new instance.</div>
</div>
<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference#%3Cinit%3E(java.lang.String,com.here.sdk.routing.TravelDirection,double,double,long,java.lang.Long)">SegmentReference</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> segmentId,
 <a href="sdk-for-android-navigate-com-here-sdk-routing-traveldirection" title="enum class in com.here.sdk.routing">TravelDirection</a> travelDirection,
 double offsetStart,
 double offsetEnd,
 long tilePartitionId,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang">Long</a> localId)</code></div>
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
<section className="detail" id="segmentId">
<h3>segmentId</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">segmentId</span></div>
<div className="block"><p>Topology segment id representing a unique identifier within the HERE platform catalogs.</p></div>
</section>
</li>
<li>
<section className="detail" id="travelDirection">
<h3>travelDirection</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-traveldirection" title="enum class in com.here.sdk.routing">TravelDirection</a></span> <span className="element-name">travelDirection</span></div>
<div className="block"><p>Travel direction of the segment.</p></div>
</section>
</li>
<li>
<section className="detail" id="offsetStart">
<h3>offsetStart</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">offsetStart</span></div>
<div className="block"><p>The start offset is a non-negative number between 0 and 1, representing the start of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)</p></div>
</section>
</li>
<li>
<section className="detail" id="offsetEnd">
<h3>offsetEnd</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">offsetEnd</span></div>
<div className="block"><p>The end offset is a non-negative number between 0 and 1, representing the end of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)</p></div>
</section>
</li>
<li>
<section className="detail" id="tilePartitionId">
<h3>tilePartitionId</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">long</span> <span className="element-name">tilePartitionId</span></div>
<div className="block"><p>HERE tile partition id (Morton-encoding + level indicator) of the segment.
 As in HERE Map Content.</p></div>
</section>
</li>
<li>
<section className="detail" id="localId">
<h3>localId</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang">Long</a></span> <span className="element-name">localId</span></div>
<div className="block"><p>Local ID of the segment inside the OCM tile.</p></div>
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
<section className="detail" id="&lt;init&gt;()">
<h3>SegmentReference</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">SegmentReference</span>()</div>
<div className="block"><p>Creates a new instance.</p></div>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(java.lang.String)">
<h3>SegmentReference</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">SegmentReference</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> segmentId)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>segmentId</code> - <p>Topology segment id representing a unique identifier within the HERE platform catalogs.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(java.lang.String,com.here.sdk.routing.TravelDirection)">
<h3>SegmentReference</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">SegmentReference</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> segmentId,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-traveldirection" title="enum class in com.here.sdk.routing">TravelDirection</a> travelDirection)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>segmentId</code> - <p>Topology segment id representing a unique identifier within the HERE platform catalogs.</p></dd>
<dd><code>travelDirection</code> - <p>Travel direction of the segment.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(java.lang.String,com.here.sdk.routing.TravelDirection,double)">
<h3>SegmentReference</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">SegmentReference</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> segmentId,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-traveldirection" title="enum class in com.here.sdk.routing">TravelDirection</a> travelDirection,
 double offsetStart)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>segmentId</code> - <p>Topology segment id representing a unique identifier within the HERE platform catalogs.</p></dd>
<dd><code>travelDirection</code> - <p>Travel direction of the segment.</p></dd>
<dd><code>offsetStart</code> - <p>The start offset is a non-negative number between 0 and 1, representing the start of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(java.lang.String,com.here.sdk.routing.TravelDirection,double,double)">
<h3>SegmentReference</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">SegmentReference</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> segmentId,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-traveldirection" title="enum class in com.here.sdk.routing">TravelDirection</a> travelDirection,
 double offsetStart,
 double offsetEnd)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>segmentId</code> - <p>Topology segment id representing a unique identifier within the HERE platform catalogs.</p></dd>
<dd><code>travelDirection</code> - <p>Travel direction of the segment.</p></dd>
<dd><code>offsetStart</code> - <p>The start offset is a non-negative number between 0 and 1, representing the start of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)</p></dd>
<dd><code>offsetEnd</code> - <p>The end offset is a non-negative number between 0 and 1, representing the end of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(java.lang.String,com.here.sdk.routing.TravelDirection,double,double,long)">
<h3>SegmentReference</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">SegmentReference</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> segmentId,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-traveldirection" title="enum class in com.here.sdk.routing">TravelDirection</a> travelDirection,
 double offsetStart,
 double offsetEnd,
 long tilePartitionId)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>segmentId</code> - <p>Topology segment id representing a unique identifier within the HERE platform catalogs.</p></dd>
<dd><code>travelDirection</code> - <p>Travel direction of the segment.</p></dd>
<dd><code>offsetStart</code> - <p>The start offset is a non-negative number between 0 and 1, representing the start of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)</p></dd>
<dd><code>offsetEnd</code> - <p>The end offset is a non-negative number between 0 and 1, representing the end of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)</p></dd>
<dd><code>tilePartitionId</code> - <p>HERE tile partition id (Morton-encoding + level indicator) of the segment.
 As in HERE Map Content.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(java.lang.String,com.here.sdk.routing.TravelDirection,double,double,long,java.lang.Long)">
<h3>SegmentReference</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">SegmentReference</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> segmentId,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-traveldirection" title="enum class in com.here.sdk.routing">TravelDirection</a> travelDirection,
 double offsetStart,
 double offsetEnd,
 long tilePartitionId,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang">Long</a> localId)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>segmentId</code> - <p>Topology segment id representing a unique identifier within the HERE platform catalogs.</p></dd>
<dd><code>travelDirection</code> - <p>Travel direction of the segment.</p></dd>
<dd><code>offsetStart</code> - <p>The start offset is a non-negative number between 0 and 1, representing the start of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)</p></dd>
<dd><code>offsetEnd</code> - <p>The end offset is a non-negative number between 0 and 1, representing the end of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)</p></dd>
<dd><code>tilePartitionId</code> - <p>HERE tile partition id (Morton-encoding + level indicator) of the segment.
 As in HERE Map Content.</p></dd>
<dd><code>localId</code> - <p>Local ID of the segment inside the OCM tile.</p></dd>
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
<li>
<section className="detail" id="fromString(java.lang.String)">
<h3>fromString</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference" title="class in com.here.sdk.routing">SegmentReference</a></span> <span className="element-name">fromString</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> segmentRef)</span></div>
<div className="block"><p>Returns an instance of this struct from a string if it's well-formatted, <code>null</code> otherwise.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>segmentRef</code> - <p>The string to parse</p></dd>
<dt>Returns:</dt>
<dd><p>An instance of <a href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference" title="class in com.here.sdk.routing"><code>SegmentReference</code></a> from a string if it's well-formatted, <code>null</code> otherwise.</p></dd>
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
