---
title: "TaskHandle (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- TaskHandle.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.core.threading</a></div>

</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">TaskHandle</span></div>
<div className="block"><p>Handle used for the manipulation of the task.</p></div>
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
<section className="detail" id="cancel()">
<h3>cancel</h3>
<div className="member-signature"><span className="return-type">boolean</span> <span className="element-name">cancel</span>()</div>
<div className="block"><p>Sets internal state of task to 'canceled'. If the task is still in the queue, it will be
 removed from it immediately. However, if the task is in a running state, it will nevertheless be completed, as there is no way
 to interrupt it.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>True, if the task was canceled. False, if the task can't be canceled due to a
     platform dependent reason.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="isFinished()">
<h3>isFinished</h3>
<div className="member-signature"><span className="return-type">boolean</span> <span className="element-name">isFinished</span>()</div>
<div className="block"><p>Gets a boolean indicating if this task is completed.
 True, if this task is completed. Completion may be due to normal termination,
 an exception, or cancellation - in all of these cases, result will return <code>true</code>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Completion indication.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="isCancelled()">
<h3>isCancelled</h3>
<div className="member-signature"><span className="return-type">boolean</span> <span className="element-name">isCancelled</span>()</div>
<div className="block"><p>Gets a boolean indicating if this task is cancelled.
 True, if this task was canceled before it completed normally.</p></div>
<dl className="notes">
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

</div>
</div>



</div>
`
}</HTMLBlock>
