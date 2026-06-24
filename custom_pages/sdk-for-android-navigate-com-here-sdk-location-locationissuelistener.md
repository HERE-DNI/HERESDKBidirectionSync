---
title: "LocationIssueListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-location-locationissuelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- LocationIssueListener.html -->










<!-- ======== START OF CLASS DATA ======== -->

<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">LocationIssueListener</span></div>
<div class="block"><p>interface receiving notifications when the set of
 currently active location issues changes.
 </p><p>Location issues represent unexpected or degraded conditions affecting positioning quality,
 availability, or functionality. The LocationEngine monitors various positioning subsystems
 and aggregates detected issues into a unified snapshot delivered via this interface.
 <ul>
<li>Each callback delivers the complete current set of active issues.</li>
<li>An empty list indicates all previously reported issues have cleared.</li>
<li>Issues are transient by design and automatically removed once underlying conditions improve.
 No explicit clear/dismiss API is provided.</li>
</ul></p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-location-locationissuelistener#onLocationIssueChanged(java.util.List)">onLocationIssueChanged</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a>&gt; issues)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called when the snapshot of currently active location issues changes.</div>
</div>
</div>
</div>
</div>
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
<section class="detail" id="onLocationIssueChanged(java.util.List)">
<h3>onLocationIssueChanged</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onLocationIssueChanged</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a>&gt; issues)</span></div>
<div class="block"><p>Called when the snapshot of currently active location issues changes.
 </p><p>Invoked whenever the LocationEngine detects a change in the set of active issues,
 including when all issues clear (empty list). Replace any previously stored issue
 list with this snapshot.</p></div>
<dl class="notes">
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
`
}</HTMLBlock>
