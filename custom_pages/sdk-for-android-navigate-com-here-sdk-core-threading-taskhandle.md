---
title: "TaskHandle (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- TaskHandle.html -->
<!DOCTYPE HTML>









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-package-summary">com.here.sdk.core.threading</a></div>

</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">TaskHandle</span></div>
<div class="block"><p>Handle used for the manipulation of the task.</p></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#cancel()">cancel</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets internal state of task to 'canceled'.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#isCancelled()">isCancelled</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets a boolean indicating if this task is cancelled.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#isFinished()">isFinished</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets a boolean indicating if this task is completed.</div>
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
<section class="detail" id="cancel()">
<h3>cancel</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">cancel</span>()</div>
<div class="block"><p>Sets internal state of task to 'canceled'. If the task is still in the queue, it will be
 removed from it immediately. However, if the task is in a running state, it will nevertheless be completed, as there is no way
 to interrupt it.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>True, if the task was canceled. False, if the task can't be canceled due to a
     platform dependent reason.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isFinished()">
<h3>isFinished</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isFinished</span>()</div>
<div class="block"><p>Gets a boolean indicating if this task is completed.
 </p><p>True, if this task is completed. Completion may be due to normal termination,
 an exception, or cancellation - in all of these cases, result will return <code>true</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Completion indication.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isCancelled()">
<h3>isCancelled</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">isCancelled</span>()</div>
<div class="block"><p>Gets a boolean indicating if this task is cancelled.
 </p><p>True, if this task was canceled before it completed normally.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Completion indication.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>





</div>
`
}</HTMLBlock>
