---
title: "LocationIssueListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-location-locationissuelistener"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- LocationIssueListener.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.location</a></div>

</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">LocationIssueListener</span></div>
<div className="block"><p>interface receiving notifications when the set of
 currently active location issues changes.
 Location issues represent unexpected or degraded conditions affecting positioning quality,
 availability, or functionality. The LocationEngine monitors various positioning subsystems
 and aggregates detected issues into a unified snapshot delivered via this interface.
 <ul>
<li>Each callback delivers the complete current set of active issues.</li>
<li>An empty list indicates all previously reported issues have cleared.</li>
<li>Issues are transient by design and automatically removed once underlying conditions improve.
 No explicit clear/dismiss API is provided.</li>
</ul></p></div>
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
<section className="detail" id="onLocationIssueChanged(java.util.List)">
<h3>onLocationIssueChanged</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onLocationIssueChanged</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a>&gt; issues)</span></div>
<div className="block"><p>Called when the snapshot of currently active location issues changes.
 Invoked whenever the LocationEngine detects a change in the set of active issues,
 including when all issues clear (empty list). Replace any previously stored issue
 list with this snapshot.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>issues</code> - <p>Current snapshot of active location issues. Empty list indicates no active issues.</p></dd>
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
