---
title: "CustomWarningProvider (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-warner-customwarningprovider"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- CustomWarningProvider.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.warner</a></div>

</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">CustomWarningProvider</span></div>
<div className="block"><p>A interface representing a provider of custom warnings based on vehicle position.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
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
<section className="detail" id="getCustomWarningType()">
<h3>getCustomWarningType</h3>
<div className="member-signature"><span className="return-type">int</span> <span className="element-name">getCustomWarningType</span>()</div>
<div className="block"><p>Returns the custom warning type identifier produced by this provider.
 The returned value corresponds to <a href="sdk-for-android-navigate-customwarning#customWarningType"><code>CustomWarning.customWarningType</code></a> and
 <a href="sdk-for-android-navigate-warning#customWarningType"><code>Warning.customWarningType</code></a> and is used to apply per-type configuration,
 such as notification distances.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The custom warning type identifier for this provider.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getWarnings(com.here.sdk.mapdata.SegmentData,com.here.sdk.mapdata.SegmentData)">
<h3>getWarnings</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-warner-customwarning" title="class in com.here.sdk.warner">CustomWarning</a>&gt;</span> <span className="element-name">getWarnings</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdata" title="class in com.here.sdk.mapdata">SegmentData</a> currentSegment,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdata" title="class in com.here.sdk.mapdata">SegmentData</a> previousSegment)</span></div>
<div className="block"><p>Returns a list of custom warnings for the given vehicle position.
 This method evaluates the custom warning provider using the current
 vehicle position on the electronic horizon and returns the resulting
 custom warnings along with corresponding payload.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>currentSegment</code> - <p>Segment data representing the vehicle’s current
     position on the electronic horizon.</p></dd>
<dd><code>previousSegment</code> - <p>Segment data representing the vehicle’s previous
     position on the electronic horizon. This parameter may be null if no
     previous position information is available.</p></dd>
<dt>Returns:</dt>
<dd><p>A list of <code>CustomWarning</code> instances representing all applicable
     custom warnings. The list may be empty if no warnings apply.</p></dd>
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
